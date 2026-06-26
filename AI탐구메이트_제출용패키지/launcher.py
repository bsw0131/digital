import sys
import threading
import time
import webbrowser
import os
from pathlib import Path

import uvicorn

if getattr(sys, "frozen", False):
    base_dir = Path(getattr(sys, "_MEIPASS"))
else:
    base_dir = Path(__file__).resolve().parent.parent

backend_dir = base_dir / "backend"
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

HOST = os.getenv("AI_TAMGU_HOST", "127.0.0.1")
PORT = int(os.getenv("AI_TAMGU_PORT", "8000"))
LOCAL_URL = f"http://127.0.0.1:{PORT}"
OPEN_BROWSER = os.getenv("AI_TAMGU_OPEN_BROWSER", "1") != "0"


def open_browser():
    time.sleep(1.5)
    webbrowser.open(LOCAL_URL)


def main():
    print("AI탐구메이트를 시작합니다.")
    print(f"브라우저가 열리지 않으면 {LOCAL_URL} 주소로 접속하세요.")
    if OPEN_BROWSER:
        threading.Thread(target=open_browser, daemon=True).start()
    uvicorn.run("main:app", host=HOST, port=PORT, reload=False, log_level="info")


if __name__ == "__main__":
    main()
