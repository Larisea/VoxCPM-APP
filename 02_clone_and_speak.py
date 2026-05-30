"""
语音克隆 + 文本转语音对话
==========================
使用方法: python 02_clone_and_speak.py

功能:
  1. 用你录制的参考音频 + 对应文本克隆你的声音
  2. 输入任意文本，用你的声音合成语音
  3. 支持交互式对话模式

VoxCPM1.5 使用 prompt_wav_path + prompt_text（延续模式）克隆声音
"""
import os
import sys
import io
import time
import soundfile as sf
from voxcpm import VoxCPM

# Windows UTF-8 编码
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
REF_DIR = os.path.join(PROJECT_DIR, "reference_audio")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def find_reference_audio():
    """查找参考音频文件"""
    wav_files = []
    if os.path.exists(REF_DIR):
        wav_files = sorted([
            f for f in os.listdir(REF_DIR) if f.endswith('.wav')
        ])

    if wav_files:
        print("\n找到以下参考音频:")
        for i, f in enumerate(wav_files):
            info = sf.info(os.path.join(REF_DIR, f))
            print(f"  [{i+1}] {f} ({info.duration:.1f}秒)")

        try:
            choice = input(f"\n请选择 (1-{len(wav_files)}, 默认 1): ").strip()
            idx = int(choice) - 1 if choice else 0
            if 0 <= idx < len(wav_files):
                return os.path.join(REF_DIR, wav_files[idx])
        except (ValueError, EOFError):
            pass
        return os.path.join(REF_DIR, wav_files[0])

    print("\n未找到参考音频文件！")
    print(f"请先将 WAV 音频放入: {REF_DIR}")
    print("或者运行录音脚本: python 01_record_voice.py")
    return None


def load_model():
    """加载 VoxCPM 模型"""
    print("\n加载 VoxCPM 模型...")
    t0 = time.time()
    model = VoxCPM.from_pretrained(
        "openbmb/VoxCPM1.5",
        load_denoiser=False,
    )
    print(f"模型加载完成！(耗时 {time.time()-t0:.0f} 秒)")
    return model


def speak_text(model, ref_audio, ref_text, text, output_name=None, show_info=True):
    """
    用克隆的声音合成语音 (VoxCPM1.5 prompt 模式)

    Args:
        model: VoxCPM 模型
        ref_audio: 参考音频路径
        ref_text: 参考音频对应的文本内容（重要！）
        text: 要合成的文本
        output_name: 输出文件名
        show_info: 是否显示详细信息

    Returns:
        输出文件路径
    """
    if show_info:
        print(f"\n{'='*50}")
        print(f"  合成: {text[:50]}{'...' if len(text) > 50 else ''}")

    t0 = time.time()

    wav = model.generate(
        text=text,
        prompt_wav_path=ref_audio,       # 参考音频
        prompt_text=ref_text,             # 参考音频的文本（延续模式）
        cfg_value=2.0,
        inference_timesteps=10,
    )

    elapsed = time.time() - t0
    audio_duration = len(wav) / model.tts_model.sample_rate
    rtf = elapsed / audio_duration if audio_duration > 0 else 0

    if output_name is None:
        timestamp = time.strftime("%H%M%S")
        output_name = f"clone_{timestamp}.wav"

    output_path = os.path.join(OUTPUT_DIR, output_name)
    sf.write(output_path, wav, model.tts_model.sample_rate)

    if show_info:
        print(f"  音频时长: {audio_duration:.1f}s | 生成耗时: {elapsed:.1f}s")
        print(f"  RTF: {rtf:.2f} | 已保存: {output_name}")

    return output_path


def interactive_mode(model, ref_audio, ref_text):
    """交互式对话模式"""
    print("\n" + "=" * 55)
    print("  语音克隆对话模式")
    print("=" * 55)
    print(f"  参考音频: {os.path.basename(ref_audio)}")
    print(f"  参考文本: {ref_text[:50]}...")
    print()
    print("  输入文本即可用你的声音合成语音")
    print("  命令: /quit 退出 | /demo 演示 | /help 帮助")
    print("=" * 55)

    count = 0

    while True:
        try:
            text = input("\n你说: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n对话结束，再见！")
            break

        if not text:
            continue

        if text.lower() == "/quit":
            print(f"\n本次共生成了 {count} 条语音，再见！")
            break

        if text.lower() == "/help":
            print("\n命令说明:")
            print("  直接输入文本 -> 用你的声音合成语音")
            print("  /quit         -> 退出")
            print("  /demo         -> 演示多个例句")
            continue

        if text.lower() == "/demo":
            demos = [
                "你好，我是AI语音助手，今天我能帮你做些什么呢？",
                "今天的天气真不错，适合出去走走。",
                "人工智能技术正在改变我们的生活方式。",
            ]
            for i, demo in enumerate(demos):
                output_name = f"demo_{i+1:02d}.wav"
                speak_text(model, ref_audio, ref_text, demo, output_name=output_name)
                count += 1
            print(f"\n已生成 {len(demos)} 条演示语音，在 output 目录查看")
            continue

        count += 1
        output_name = f"dialogue_{count:03d}.wav"
        speak_text(model, ref_audio, ref_text, text, output_name=output_name)


def batch_mode(model, ref_audio, ref_text):
    """批量处理模式"""
    input_file = os.path.join(PROJECT_DIR, "input.txt")

    if not os.path.exists(input_file):
        samples = [
            "你好，我是你的专属AI语音助手。",
            "有什么我可以帮你的吗？",
            "今天想聊点什么话题呢？",
        ]
        with open(input_file, "w", encoding="utf-8") as f:
            f.write("\n".join(samples))
        print(f"\n已创建示例输入文件: {input_file}")

    with open(input_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        print("input.txt 中没有文本内容")
        return

    print(f"\n批量处理 {len(lines)} 条文本...")
    for i, text in enumerate(lines, 1):
        output_name = f"batch_{i:03d}.wav"
        speak_text(model, ref_audio, ref_text, text, output_name=output_name, show_info=False)
        print(f"  [{i}/{len(lines)}] {text[:30]}... -> {output_name}")

    print(f"\n完成！共生成 {len(lines)} 条语音")


def main():
    print("=" * 55)
    print("  VoxCPM 语音克隆 + 对话系统")
    print("=" * 55)

    # 1. 查找参考音频
    ref_audio = find_reference_audio()
    if ref_audio is None:
        print("\n请先录制你的声音: python 01_record_voice.py")
        sys.exit(0)

    # 2. 获取参考音频的文本内容
    print()
    print("语音克隆需要参考音频对应的文本内容（即你录音时朗读的内容）。")
    print("这会帮助模型学习你的声音特征。")
    print()
    default_text = "大家好我是测试语音克隆的效果"
    try:
        ref_text = input(f"请输入参考音频的文本 (回车使用默认: \"{default_text}\"): ").strip()
    except EOFError:
        ref_text = ""

    if not ref_text:
        ref_text = default_text

    print(f"\n参考文本: {ref_text}")

    # 3. 加载模型
    model = load_model()

    # 4. 选择模式
    print("\n请选择模式:")
    print("  [1] 交互式对话 — 逐句输入，实时合成")
    print("  [2] 批量处理   — 读取 input.txt 批量合成")
    print("  [3] 单句测试   — 输入一句话测试效果")

    try:
        choice = input("\n请输入选项 (1-3, 默认 1): ").strip()
    except EOFError:
        choice = "1"

    if choice == "2":
        batch_mode(model, ref_audio, ref_text)
    elif choice == "3":
        try:
            text = input("请输入要合成的文本: ").strip()
        except EOFError:
            text = "你好，这是我的AI语音克隆测试。"
        if text:
            speak_text(model, ref_audio, ref_text, text)
    else:
        interactive_mode(model, ref_audio, ref_text)


if __name__ == "__main__":
    main()
