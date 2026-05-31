"""RVC API客户端模块"""
import httpx
import os
from pathlib import Path
from typing import Optional

RVC_BASE_URL = "http://localhost:7865"


async def check_rvc_status() -> dict:
    """检测RVC WebUI是否运行"""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"{RVC_BASE_URL}/")
            if response.status_code == 200:
                return {"status": "online", "url": RVC_BASE_URL}
            else:
                return {"status": "offline", "error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"status": "offline", "error": str(e)}


async def upload_audio_to_rvc(audio_path: str) -> dict:
    """上传音频到RVC训练目录"""
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            with open(audio_path, "rb") as f:
                files = {"audio": (Path(audio_path).name, f, "audio/wav")}
                response = await client.post(
                    f"{RVC_BASE_URL}/api/upload_audio",
                    files=files
                )
            if response.status_code == 200:
                return response.json()
            else:
                return {"status": "error", "error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"status": "error", "error": str(e)}


async def start_training(audio_path: str, model_name: str, params: Optional[dict] = None) -> dict:
    """启动RVC训练任务"""
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            data = {
                "audio_path": audio_path,
                "model_name": model_name,
                **(params or {})
            }
            response = await client.post(
                f"{RVC_BASE_URL}/api/train",
                json=data
            )
            if response.status_code == 200:
                return response.json()
            else:
                return {"status": "error", "error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"status": "error", "error": str(e)}


async def get_training_status() -> dict:
    """获取训练状态"""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"{RVC_BASE_URL}/api/training_status")
            if response.status_code == 200:
                return response.json()
            else:
                return {"status": "error", "error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"status": "error", "error": str(e)}


async def list_models() -> dict:
    """列出可用模型"""
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{RVC_BASE_URL}/api/models")
            if response.status_code == 200:
                return response.json()
            else:
                return {"status": "error", "error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"status": "error", "error": str(e)}


async def delete_model(model_name: str) -> dict:
    """删除模型"""
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.delete(f"{RVC_BASE_URL}/api/models/{model_name}")
            if response.status_code == 200:
                return response.json()
            else:
                return {"status": "error", "error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"status": "error", "error": str(e)}


async def voice_change(audio_path: str, model_name: str, params: Optional[dict] = None) -> dict:
    """翻唱生成"""
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            with open(audio_path, "rb") as f:
                files = {"audio": (Path(audio_path).name, f, "audio/wav")}
                data = {
                    "model_name": model_name,
                    **(params or {})
                }
                response = await client.post(
                    f"{RVC_BASE_URL}/api/voice_change",
                    files=files,
                    data=data
                )
            if response.status_code == 200:
                # 保存输出音频
                output_dir = Path("output")
                output_dir.mkdir(exist_ok=True)
                output_path = output_dir / f"cover_{Path(audio_path).stem}_{model_name}.wav"
                with open(output_path, "wb") as f:
                    f.write(response.content)
                return {"status": "success", "audio_path": str(output_path)}
            else:
                return {"status": "error", "error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"status": "error", "error": str(e)}
