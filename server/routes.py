"""API 路由"""
import os
import io
import sys
import time
import uuid
import subprocess
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, Form, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from .config import BASE_DIR, OUTPUT_DIR, REFERENCE_DIR, MAX_TEXT_LENGTH
from .model import get_model, is_model_loaded, is_generating
from .tasks import create_task, update_task, get_task, run_tts_task


def _safe_path(directory: Path, filename: str) -> Path | None:
    """安全路径拼接，防止路径遍历攻击"""
    resolved = (directory / filename).resolve()
    if resolved.is_relative_to(directory.resolve()):
        return resolved
    return None


def create_app():
    """创建 FastAPI 应用"""
    app = FastAPI(title="VoxCPM 语音助手")

    static_dir = Path(__file__).parent / "static"
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
    app.mount("/output", StaticFiles(directory=str(OUTPUT_DIR)), name="output")
    app.mount("/reference_audio", StaticFiles(directory=str(REFERENCE_DIR)), name="reference_audio")

    # ---- 路由 ----

    @app.get("/", response_class=HTMLResponse)
    async def index():
        html_path = static_dir / "landing.html"
        return HTMLResponse(html_path.read_text(encoding="utf-8"))

    @app.get("/app", response_class=HTMLResponse)
    async def app_page():
        html_path = static_dir / "index.html"
        return HTMLResponse(html_path.read_text(encoding="utf-8"))

    @app.get("/api/status")
    async def api_status():
        return {
            "model_loaded": is_model_loaded(),
            "model_type": "voxcpm1.5",
            "ready": is_model_loaded(),
        }

    @app.get("/api/busy")
    async def api_busy():
        return {"generating": is_generating()}

    @app.post("/api/load_model")
    async def api_load_model():
        try:
            get_model()
            return {"success": True, "model_type": "voxcpm1.5"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @app.get("/api/reference_audios")
    async def api_list_references():
        files = []
        for pattern in ["*.wav", "*.mp3", "*.webm", "*.flac", "*.ogg"]:
            for f in REFERENCE_DIR.glob(pattern):
                files.append({
                    "name": f.name,
                    "path": f.relative_to(BASE_DIR).as_posix(),
                    "size_kb": round(f.stat().st_size / 1024, 1),
                })
        return {"files": sorted(files, key=lambda x: x["name"])}

    @app.post("/api/upload_reference")
    async def api_upload_reference(file: UploadFile = File(...)):
        if not file.filename:
            return JSONResponse({"success": False, "error": "未选择文件"}, status_code=400)

        ext = Path(file.filename).suffix.lower()
        if ext not in [".wav", ".mp3", ".flac", ".ogg", ".webm"]:
            return JSONResponse({"success": False, "error": f"不支持的格式: {ext}"}, status_code=400)

        content = await file.read()
        base_name = Path(file.filename).stem
        safe_name = f"{uuid.uuid4().hex[:8]}_{base_name}.wav"
        save_path = REFERENCE_DIR / safe_name

        if ext == ".wav":
            with open(save_path, "wb") as f:
                f.write(content)
        else:
            try:
                import soundfile as sf
                audio, sr = sf.read(io.BytesIO(content))
                sf.write(str(save_path), audio, sr)
            except Exception:
                try:
                    import librosa
                    import soundfile as sf
                    audio, sr = librosa.load(io.BytesIO(content), sr=None, mono=False)
                    sf.write(str(save_path), audio, sr)
                except Exception as e:
                    return JSONResponse(
                        {"success": False, "error": f"音频解码失败: {e}"},
                        status_code=400,
                    )

        size_kb = round(save_path.stat().st_size / 1024, 1)
        return {"success": True, "filename": safe_name, "size_kb": size_kb}

    @app.post("/api/record")
    async def api_record():
        return {"success": True, "message": "请在前端录制并上传"}

    @app.post("/api/tts")
    async def api_tts(
        background_tasks: BackgroundTasks,
        text: str = Form(...),
        prompt_wav: str = Form(""),
        prompt_text: str = Form(""),
        cfg: float = Form(2.0),
        steps: int = Form(10),
    ):
        if not text.strip():
            return JSONResponse({"success": False, "error": "文本不能为空"}, status_code=400)

        if len(text) > MAX_TEXT_LENGTH:
            return JSONResponse(
                {"success": False, "error": f"文本过长，最多 {MAX_TEXT_LENGTH} 字"},
                status_code=400,
            )

        task_id = create_task(text)

        prompt_wav_path = None
        if prompt_wav:
            candidate = _safe_path(REFERENCE_DIR, Path(prompt_wav).name)
            if candidate and candidate.exists():
                prompt_wav_path = str(candidate)

        background_tasks.add_task(
            run_tts_task, task_id, text, prompt_wav_path, prompt_text, cfg, steps
        )

        return {"success": True, "task_id": task_id}

    @app.get("/api/task/{task_id}")
    async def api_task_status(task_id: str):
        task = get_task(task_id)
        if not task:
            return JSONResponse({"success": False, "error": "任务不存在"}, status_code=404)
        return {"success": True, "task": task}

    @app.get("/api/history")
    async def api_history():
        files = []
        for f in sorted(OUTPUT_DIR.glob("*.wav"), key=lambda x: x.stat().st_mtime, reverse=True)[:20]:
            files.append({
                "name": f.name,
                "path": f"output/{f.name}",
                "size_kb": round(f.stat().st_size / 1024, 1),
                "time": time.strftime("%H:%M:%S", time.localtime(f.stat().st_mtime)),
            })
        return {"files": files}

    @app.get("/api/download/{filename}")
    async def api_download(filename: str):
        safe = _safe_path(OUTPUT_DIR, filename)
        if not safe or not safe.exists():
            return JSONResponse({"success": False, "error": "文件不存在"}, status_code=404)
        return FileResponse(str(safe), filename=filename, media_type="audio/wav")

    @app.delete("/api/reference/{filename}")
    async def api_delete_reference(filename: str):
        safe = _safe_path(REFERENCE_DIR, filename)
        if not safe or not safe.exists():
            return JSONResponse({"success": False, "error": "文件不存在"}, status_code=404)
        safe.unlink()
        return {"success": True}

    @app.delete("/api/history/{filename}")
    async def api_delete_history(filename: str):
        safe = _safe_path(OUTPUT_DIR, filename)
        if not safe or not safe.exists():
            return JSONResponse({"success": False, "error": "文件不存在"}, status_code=404)
        safe.unlink()
        return {"success": True}

    @app.post("/api/install_rvc")
    async def api_install_rvc():
        rvc_dir = BASE_DIR / "RVC"
        rvc_dir.mkdir(exist_ok=True)

        install_script = rvc_dir / "install_rvc.bat"
        with open(install_script, "w", encoding="utf-8") as f:
            f.write(f"""@echo off
echo ========================================
echo   RVC (Retrieval-based Voice Conversion)
echo   歌曲翻唱工具 - 一键安装
echo ========================================
echo.

cd /d "{rvc_dir}"

:: 检查 git
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] 需要先安装 Git!
    echo 请从 https://git-scm.com/download/win 下载安装
    pause
    exit /b 1
)

:: 克隆 RVC
if not exist "Retrieval-based-Voice-Conversion-WebUI" (
    echo [1/4] 下载 RVC 源码...
    git clone https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI.git
)

cd Retrieval-based-Voice-Conversion-WebUI

:: 创建 conda 环境
echo [2/4] 创建 Python 环境...
call conda create -n rvc python=3.10 -y 2>nul

:: 安装依赖
echo [3/4] 安装 Python 依赖...
call conda run -n rvc pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
call conda run -n rvc pip install -r requirements.txt

:: 下载预训练模型
echo [4/4] 下载预训练模型...
call conda run -n rvc python tools/download_models.py

echo.
echo ========================================
echo   安装完成!
echo ========================================
echo.
echo 启动 RVC WebUI:
echo   conda activate rvc
echo   cd "{rvc_dir}\\Retrieval-based-Voice-Conversion-WebUI"
echo   python infer-web.py
echo.
echo 访问 http://localhost:7865 开始使用
echo ========================================
pause
""")

        try:
            subprocess.Popen(
                ["cmd", "/c", "start", str(install_script)],
                cwd=str(rvc_dir),
                creationflags=subprocess.CREATE_NEW_CONSOLE if sys.platform == "win32" else 0,
            )
            return {
                "success": True,
                "message": (
                    "RVC 安装脚本已启动！\n"
                    "请在弹出的命令行窗口中查看安装进度。\n\n"
                    "安装步骤:\n"
                    "1. 下载 RVC 源码 (约 100MB)\n"
                    "2. 创建 Python 3.10 环境\n"
                    "3. 安装 PyTorch + 依赖 (约 3-5GB)\n"
                    "4. 下载预训练模型 (约 500MB)\n\n"
                    "预计总时间: 10-20 分钟\n"
                    "安装完成后启动命令:\n"
                    f"  cd {rvc_dir}\\Retrieval-based-Voice-Conversion-WebUI\n"
                    "  conda activate rvc\n"
                    "  python infer-web.py"
                ),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    return app
