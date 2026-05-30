"""配置常量"""
import sys
from pathlib import Path

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = BASE_DIR / "output"
REFERENCE_DIR = BASE_DIR / "reference_audio"
UPLOAD_DIR = BASE_DIR / "uploads"

OUTPUT_DIR.mkdir(exist_ok=True)
REFERENCE_DIR.mkdir(exist_ok=True)
UPLOAD_DIR.mkdir(exist_ok=True)

MODEL_NAME = "openbmb/VoxCPM1.5"
MODEL_TYPE = "voxcpm1.5"
DEFAULT_PORT = 8868

MAX_TEXT_LENGTH = 500
TASK_EXPIRE_HOURS = 1
CLEANUP_INTERVAL_MINUTES = 10
