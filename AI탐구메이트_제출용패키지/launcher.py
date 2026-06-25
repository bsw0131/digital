import sys
import threading
import time
import webbrowser
from pathlib import Path

import uvicorn

if getattr(sys, "frozen", False):
    base_dir = Path(getattr(sys, "_MEIPASS"))
else:
    base_dir = Path(__file__).resolve().parent.parent

backend_dir = base_dir / "backend"
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))


def open_browser():
    time.sleep(1.5)
    webbrowser.open("http://127.0.0.1:8000")


def main():
    threading.Thread(target=open_browser, daemon=True).start()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False, log_level="info")


if __name__ == "__main__":
    main()
