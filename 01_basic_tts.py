"""
VoxCPM 基础文本转语音示例
用法: python 01_basic_tts.py
"""
import os
import soundfile as sf
from voxcpm import VoxCPM

# 输出目录
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 50)
print("  VoxCPM 基础 TTS 示例")
print("=" * 50)

# 加载模型（首次运行会自动下载模型到缓存目录）
print("\n[1] 加载模型...")
model = VoxCPM.from_pretrained(
    "openbmb/VoxCPM1.5",  # 使用 1.5 版本，适配 6GB 显存
    load_denoiser=False,
)
print("    模型加载完成！")

# 中文合成
print("\n[2] 生成中文语音...")
wav_cn = model.generate(
    text="你好，欢迎使用 VoxCPM 文本转语音系统。这是一个基于扩散自回归架构的端到端语音合成模型。",
    cfg_value=2.0,
    inference_timesteps=10,
)
cn_path = os.path.join(OUTPUT_DIR, "chinese_demo.wav")
sf.write(cn_path, wav_cn, model.tts_model.sample_rate)
print(f"    已保存: {cn_path}")

# 英文合成
print("\n[3] 生成英文语音...")
wav_en = model.generate(
    text="Hello! Welcome to VoxCPM, a tokenizer-free text-to-speech system powered by diffusion autoregressive architecture.",
    cfg_value=2.0,
    inference_timesteps=10,
)
en_path = os.path.join(OUTPUT_DIR, "english_demo.wav")
sf.write(en_path, wav_en, model.tts_model.sample_rate)
print(f"    已保存: {en_path}")

print("\n" + "=" * 50)
print("  完成！请在 output 目录查看生成的音频文件")
print("=" * 50)
