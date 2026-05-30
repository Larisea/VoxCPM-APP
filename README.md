# VoxCPM Demo

基于 [VoxCPM](https://github.com/OpenBMB/VoxCPM) 的语音合成与克隆演示项目。

## 功能

- **基础 TTS** — 文本转语音（中英文）
- **语音克隆** — 用参考音频克隆声音
- **Web 界面** — 浏览器操作的完整 UI
- **歌曲翻唱** — 集成 RVC 工具进行 AI 翻唱

## 环境要求

- Python 3.10+
- CUDA 12.x（推荐，需约 6GB 显存）
- Conda（推荐用于环境管理）

## 快速开始

### 1. 配置环境

双击运行 `setup_env.bat`，或手动执行：

```bash
conda create -n voxcpm python=3.10 -y
conda activate voxcpm
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

### 2. 启动 Web 界面

```bash
python app_server.py
```

浏览器访问 http://localhost:8868

### 3. 命令行示例

```bash
# 基础 TTS
python 01_basic_tts.py

# 录制参考音频
python 01_record_voice.py

# 语音克隆 + 交互对话
python 02_clone_and_speak.py
```

## 项目结构

```
VoxCPM_Demo/
├── server/                  # Web 服务
│   ├── config.py            # 配置
│   ├── model.py             # 模型管理
│   ├── tasks.py             # 任务队列
│   ├── routes.py            # API 路由
│   └── static/              # 前端文件
├── app_server.py            # 启动入口
├── 01_basic_tts.py          # 基础 TTS 示例
├── 01_record_voice.py       # 录音工具
├── 02_clone_and_speak.py    # 语音克隆示例
├── setup_env.bat            # 环境配置脚本
├── restart_server.bat       # 重启服务脚本
├── reference_audio/         # 参考音频
├── output/                  # 生成的音频
└── RVC/                     # RVC 翻唱工具
```

## 注意事项

- 首次运行会自动下载模型（约 2GB）
- VoxCPM1.5 适配 6GB 显存，VoxCPM2 需要 8GB+
- 语音克隆需要提供参考音频及对应文本
