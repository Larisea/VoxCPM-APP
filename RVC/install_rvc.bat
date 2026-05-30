@echo off
echo ========================================
echo   RVC (Retrieval-based Voice Conversion)
echo   歌曲翻唱工具 - 一键安装
echo ========================================
echo.

cd /d "D:\Workspace\VoxCPM_Demo\RVC"

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
echo   cd "D:\Workspace\VoxCPM_Demo\RVC\Retrieval-based-Voice-Conversion-WebUI"
echo   python infer-web.py
echo.
echo 访问 http://localhost:7865 开始使用
echo ========================================
pause
