"""
RVC API 模拟服务器
提供翻唱功能所需的 API 端点
"""
import os
import sys
import uuid
import time
import asyncio
import uvicorn
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
from typing import Optional

app = FastAPI()

# 模拟数据
models = {}
training_tasks = {}
BASE_DIR = Path(__file__).parent
MODELS_DIR = BASE_DIR / "rvc_models"
MODELS_DIR.mkdir(exist_ok=True)


@app.get("/")
async def root():
    return {"message": "RVC API Server", "status": "running"}


@app.get("/api/status")
async def get_status():
    return {"status": "online", "version": "1.0.0"}


@app.get("/api/models")
async def list_models():
    """列出可用模型"""
    model_list = []
    for name, info in models.items():
        model_list.append({
            "name": name,
            "size": info.get("size", 0),
            "created": info.get("created", "")
        })
    return {"models": model_list}


@app.post("/api/train")
async def start_training(
    audio_path: str = Form(...),
    model_name: str = Form(...),
    epochs: int = Form(200),
    batch_size: int = Form(8)
):
    """启动训练任务"""
    task_id = str(uuid.uuid4())[:8]
    training_tasks[task_id] = {
        "status": "training",
        "model_name": model_name,
        "progress": 0,
        "epoch": 0,
        "total_epochs": epochs,
        "start_time": time.time()
    }
    
    # 模拟训练过程
    asyncio.create_task(simulate_training(task_id, model_name, epochs))
    
    return {"status": "training_started", "task_id": task_id}


async def simulate_training(task_id: str, model_name: str, epochs: int):
    """模拟训练过程"""
    for i in range(epochs):
        await asyncio.sleep(0.1)  # 模拟训练时间
        training_tasks[task_id]["epoch"] = i + 1
        training_tasks[task_id]["progress"] = int((i + 1) / epochs * 100)
    
    # 训练完成，保存模型
    model_path = MODELS_DIR / f"{model_name}.pth"
    model_path.touch()
    
    models[model_name] = {
        "path": str(model_path),
        "size": 1024 * 1024,  # 1MB 模拟大小
        "created": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    training_tasks[task_id]["status"] = "completed"


@app.get("/api/training_status")
async def get_training_status():
    """获取训练状态"""
    if not training_tasks:
        return {"status": "idle"}
    
    # 返回最新的训练任务状态
    latest_task = list(training_tasks.values())[-1]
    return latest_task


@app.delete("/api/models/{model_name}")
async def delete_model(model_name: str):
    """删除模型"""
    if model_name in models:
        model_path = Path(models[model_name]["path"])
        if model_path.exists():
            model_path.unlink()
        del models[model_name]
        return {"status": "deleted"}
    return JSONResponse({"error": "Model not found"}, status_code=404)


@app.post("/api/voice_change")
async def voice_change(
    audio: UploadFile = File(...),
    model_name: str = Form(...),
    pitch: int = Form(0),
    f0_method: str = Form("rmvpe")
):
    """翻唱生成"""
    if model_name not in models:
        return JSONResponse({"error": "Model not found"}, status_code=404)
    
    # 保存上传的音频
    temp_dir = BASE_DIR / "uploads" / "rvc"
    temp_dir.mkdir(parents=True, exist_ok=True)
    temp_path = temp_dir / f"{uuid.uuid4().hex[:8]}_{audio.filename}"
    
    content = await audio.read()
    with open(temp_path, "wb") as f:
        f.write(content)
    
    # 模拟翻唱处理
    output_dir = BASE_DIR / "output"
    output_dir.mkdir(exist_ok=True)
    output_filename = f"cover_{temp_path.stem}_{model_name}.wav"
    output_path = output_dir / output_filename
    
    # 复制输入音频作为输出（模拟翻唱）
    import shutil
    shutil.copy(temp_path, output_path)
    
    return FileResponse(
        output_path,
        media_type="audio/wav",
        filename=output_filename
    )


if __name__ == "__main__":
    print("=" * 50)
    print("  RVC API 模拟服务器")
    print("=" * 50)
    print(f"  访问地址: http://localhost:7865")
    print("=" * 50)
    uvicorn.run(app, host="0.0.0.0", port=7865, log_level="info")
