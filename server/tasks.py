"""异步任务队列管理"""
import time
import uuid
import base64
import threading
import logging

from .config import OUTPUT_DIR, TASK_EXPIRE_HOURS, CLEANUP_INTERVAL_MINUTES

logger = logging.getLogger(__name__)

_tasks = {}
_tasks_lock = threading.Lock()


def _cleanup_expired():
    """定期清理过期任务"""
    while True:
        time.sleep(CLEANUP_INTERVAL_MINUTES * 60)
        now = time.time()
        expired = []
        with _tasks_lock:
            for tid, task in _tasks.items():
                if task["status"] in ("done", "error"):
                    age_hours = (now - task["created_at"]) / 3600
                    if age_hours > TASK_EXPIRE_HOURS:
                        expired.append(tid)
            for tid in expired:
                del _tasks[tid]
        if expired:
            logger.info(f"清理过期任务: {len(expired)} 个")


_cleanup_thread = threading.Thread(target=_cleanup_expired, daemon=True)
_cleanup_thread.start()


def create_task(text):
    """创建新任务，返回 task_id"""
    task_id = uuid.uuid4().hex[:12]
    with _tasks_lock:
        _tasks[task_id] = {
            "id": task_id,
            "status": "pending",
            "progress": 0,
            "message": "排队中...",
            "text": text,
            "created_at": time.time(),
        }
    return task_id


def update_task(task_id, **kwargs):
    with _tasks_lock:
        if task_id in _tasks:
            _tasks[task_id].update(kwargs)


def get_task(task_id):
    with _tasks_lock:
        return _tasks.get(task_id)


def run_tts_task(task_id, text, prompt_wav, prompt_text, cfg, steps):
    """后台执行 TTS 任务"""
    import soundfile as sf
    from .model import generate_speech

    try:
        update_task(task_id, status="running", progress=10, message="正在生成语音...")
        wav, sr = generate_speech(text, prompt_wav, prompt_text, cfg, steps)

        out_path = OUTPUT_DIR / f"tts_{task_id}.wav"
        sf.write(str(out_path), wav, sr)

        duration = len(wav) / sr

        with open(out_path, "rb") as f:
            audio_b64 = base64.b64encode(f.read()).decode()

        update_task(task_id, status="done", progress=100, message="完成",
                    result={
                        "filename": out_path.name,
                        "duration": round(duration, 1),
                        "sample_rate": sr,
                        "audio_base64": audio_b64,
                    })
    except Exception as e:
        update_task(task_id, status="error", message=str(e))
