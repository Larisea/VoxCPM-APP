"""
VoxCPM 语音助手 Web 界面
========================
启动: python app_server.py
访问: http://localhost:8868
"""
import uvicorn
from server.routes import create_app
from server.model import get_model
from server.config import DEFAULT_PORT

app = create_app()

if __name__ == "__main__":
    print("=" * 50)
    print("  VoxCPM 语音助手 Web 界面")
    print("=" * 50)
    print(f"  访问地址: http://localhost:{DEFAULT_PORT}")
    print("=" * 50)

    print("[启动] 预加载 VoxCPM 模型...")
    try:
        get_model()
    except Exception as e:
        print(f"[警告] 模型预加载失败: {e}")
        print("[提示] 首次访问时会自动加载")

    uvicorn.run(app, host="0.0.0.0", port=DEFAULT_PORT, log_level="info")
