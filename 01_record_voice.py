"""
录音采集脚本 — 录制你自己的声音作为 VoxCPM 克隆参考音频
==============================================================
使用方法: python 01_record_voice.py

录制要求:
  - 安静环境，减少背景噪音
  - 正常语速，清晰朗读
  - 建议录制 15-30 秒
  - 采样率 16kHz（VoxCPM 要求）
  - 输出为 WAV 格式
  - 请记住你朗读的具体内容（后续克隆需要用到）
"""
import os
import sys
import io
import time
import sounddevice as sd
import soundfile as sf
import numpy as np

# Windows UTF-8 编码
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
REF_DIR = os.path.join(PROJECT_DIR, "reference_audio")
os.makedirs(REF_DIR, exist_ok=True)

SAMPLE_RATE = 16000  # VoxCPM 要求的采样率
CHANNELS = 1         # 单声道


def list_devices():
    """列出所有音频设备"""
    print("\n可用的音频设备:")
    print("-" * 60)
    devices = sd.query_devices()
    for i, dev in enumerate(devices):
        if dev['max_input_channels'] > 0:
            print(f"  [{i}] {dev['name']} (输入通道: {dev['max_input_channels']})")
    print("-" * 60)


def record_voice(duration=15, device=None):
    """录制语音"""
    print(f"\n准备录制 {duration} 秒音频...")
    print(f"采样率: {SAMPLE_RATE} Hz | 声道: 单声道")
    print()

    # 倒计时
    for i in range(3, 0, -1):
        print(f"\r  {i} 秒后开始录音...", end="", flush=True)
        time.sleep(1)
    print("\r  正在录音中，请朗读文本：")
    print()
    print("  " + "=" * 50)
    print("  推荐朗读内容:")
    print("  「大家好，我是XXX，今天我们来测试一下语音克隆的效果。」")
    print("  " + "=" * 50)
    print()

    # 开始录音
    recording = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype='float32',
        device=device,
    )

    # 显示录音进度
    start_time = time.time()
    while time.time() - start_time < duration:
        elapsed = time.time() - start_time
        remaining = duration - elapsed
        bar_len = 30
        filled = int(bar_len * elapsed / duration)
        bar = '#' * filled + '-' * (bar_len - filled)
        print(f"\r  [{bar}] {remaining:.0f}s 剩余", end="", flush=True)
        time.sleep(0.1)

    sd.wait()
    print("\r  录音完成！" + " " * 40)

    return recording.flatten()


def save_and_verify(recording, filename):
    """保存音频并验证"""
    filepath = os.path.join(REF_DIR, filename)
    sf.write(filepath, recording, SAMPLE_RATE)

    info = sf.info(filepath)
    file_size_kb = os.path.getsize(filepath) / 1024

    print(f"\n音频已保存:")
    print(f"  文件: {filepath}")
    print(f"  时长: {info.duration:.1f} 秒")
    print(f"  采样率: {info.samplerate} Hz")
    print(f"  大小: {file_size_kb:.1f} KB")
    print(f"  最大振幅: {np.max(np.abs(recording)):.3f}")

    max_amp = np.max(np.abs(recording))
    if max_amp < 0.01:
        print(f"\n  警告: 音量过低！请靠近麦克风后重新录制")
    elif max_amp > 0.95:
        print(f"\n  警告: 音量过高，请稍微远离麦克风")
    else:
        print(f"\n  音量正常")

    return filepath


def main():
    print("=" * 55)
    print("  VoxCPM 声音采集工具")
    print("=" * 55)

    list_devices()

    print("\n请选择录音时长:")
    print("  [1] 10 秒（快速测试）")
    print("  [2] 20 秒（推荐）")
    print("  [3] 30 秒（最佳效果）")
    print("  [4] 自定义")

    try:
        choice = input("\n请输入选项 (1-4, 默认 2): ").strip()
        if choice == "1":
            duration = 10
        elif choice == "3":
            duration = 30
        elif choice == "4":
            duration = int(input("请输入录音时长(秒): ").strip())
        else:
            duration = 20
    except (ValueError, EOFError):
        duration = 20

    # 选择设备
    try:
        dev_input = input("\n请输入音频设备编号 (直接回车使用默认): ").strip()
        device = int(dev_input) if dev_input else None
    except (ValueError, EOFError):
        device = None

    # 文件名
    try:
        name_input = input("\n输入文件名 (默认: my_voice.wav): ").strip()
        filename = name_input if name_input else "my_voice.wav"
        if not filename.endswith(".wav"):
            filename += ".wav"
    except (EOFError):
        filename = "my_voice.wav"

    # 录音
    try:
        recording = record_voice(duration=duration, device=device)
    except Exception as e:
        print(f"\n录音失败: {e}")
        print("\n提示:")
        print("  1. 检查麦克风是否已连接")
        print("  2. pip install sounddevice")
        sys.exit(1)

    filepath = save_and_verify(recording, filename)

    # 提醒记录文本
    print()
    print("=" * 55)
    print("  重要提醒！")
    print("  语音克隆需要知道参考音频对应的文本内容。")
    print("  请在 02_clone_and_speak.py 中使用时提供 prompt_text 参数。")
    print()
    print(f"  参考音频: {filepath}")
    print(f"  下一步: python 02_clone_and_speak.py")
    print("=" * 55)


if __name__ == "__main__":
    main()
