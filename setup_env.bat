@echo off
chcp 65001 >nul
echo ============================================
echo   VoxCPM 环境一键配置脚本
echo ============================================
echo.

REM 检查 conda 是否可用
where conda >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未找到 conda，请先安装 Miniforge 或 Anaconda
    echo 下载地址: https://github.com/conda-forge/miniforge/releases
    pause
    exit /b 1
)

echo [1/4] 创建 Python 3.10 虚拟环境...
call conda create -n voxcpm python=3.10 -y
if %errorlevel% neq 0 (
    echo [错误] 创建环境失败
    pause
    exit /b 1
)

echo.
echo [2/4] 激活环境...
call conda activate voxcpm

echo.
echo [3/4] 安装 PyTorch (CUDA 12.x)...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

echo.
echo [4/4] 安装 VoxCPM...
pip install voxcpm

echo.
echo ============================================
echo   安装完成！
echo   使用方式：
echo      conda activate voxcpm
echo      python 01_basic_tts.py
echo ============================================
pause
