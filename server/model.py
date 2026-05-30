"""模型管理 — 加载、语音生成"""
import os
import threading

from .config import MODEL_NAME

_model = None
_model_lock = threading.Lock()
_model_loaded = False
_generating = False
_gen_lock = threading.Lock()


def is_model_loaded():
    return _model_loaded


def is_generating():
    return _generating


def get_model():
    """获取全局模型（懒加载，线程安全）"""
    global _model, _model_loaded
    if _model is None:
        with _model_lock:
            if _model is None:
                print("[模型] 加载 VoxCPM1.5 ...")
                from voxcpm import VoxCPM
                _model = VoxCPM.from_pretrained(
                    MODEL_NAME,
                    load_denoiser=False,
                )
                _model_loaded = True
                print(f"[模型] 加载完成，采样率={_model.tts_model.sample_rate}")
    return _model


def generate_speech(text, prompt_wav_path=None, prompt_text=None,
                    cfg_value=2.0, timesteps=10):
    """使用 VoxCPM1.5 生成语音

    Returns:
        (wav_array, sample_rate)
    """
    global _generating
    model = get_model()

    kwargs = {
        "text": text,
        "cfg_value": cfg_value,
        "inference_timesteps": timesteps,
    }

    if prompt_wav_path and os.path.exists(prompt_wav_path) and prompt_text:
        kwargs["prompt_wav_path"] = prompt_wav_path
        kwargs["prompt_text"] = prompt_text
        print(f"[生成] 克隆模式: text={text[:30]}..., prompt={os.path.basename(prompt_wav_path)}")
    else:
        print(f"[生成] 标准模式: text={text[:30]}...")

    with _gen_lock:
        _generating = True
    try:
        wav = model.generate(**kwargs)
        return wav, model.tts_model.sample_rate
    finally:
        with _gen_lock:
            _generating = False
