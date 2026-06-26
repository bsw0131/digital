import os
import socket
import sys
import threading
import time
import webbrowser
from pathlib import Path

import uvicorn


if getattr(sys, "frozen", False):
    base_dir = Path(getattr(sys, "_MEIPASS"))
else:
    base_dir = Path(__file__).resolve().parent

backend_dir = base_dir / "backend"
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

HOST = os.getenv("AI_TAMGU_HOST", "0.0.0.0")
PORT = int(os.getenv("AI_TAMGU_PORT", "8000"))
OPEN_BROWSER = os.getenv("AI_TAMGU_OPEN_BROWSER", "1") != "0"


def detect_lan_ip() -> str:
    candidates = []
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
          sock.connect(("8.8.8.8", 80))
          candidates.append(sock.getsockname()[0])
    except OSError:
        pass
    try:
        host_name = socket.gethostname()
        for _, _, _, _, sockaddr in socket.getaddrinfo(host_name, None, socket.AF_INET):
            candidates.append(sockaddr[0])
    except OSError:
        pass
    for ip in candidates:
        if ip and not ip.startswith("127."):
            return ip
    return "127.0.0.1"


LAN_IP = os.getenv("AI_TAMGU_LAN_IP", detect_lan_ip())
os.environ["AI_TAMGU_LAN_IP"] = LAN_IP
os.environ["AI_TAMGU_PORT"] = str(PORT)

CLASS_URL = f"http://127.0.0.1:{PORT}/class.html"
STUDENT_URL = f"http://{LAN_IP}:{PORT}/student.html"
TEACHER_URL = f"http://{LAN_IP}:{PORT}/teacher.html"


def open_class_screen():
    time.sleep(1.8)
    webbrowser.open(CLASS_URL)


def main():
    print("")
    print("AI탐구메이트 QR 수업 모드를 시작합니다.")
    print("이 창을 닫으면 학생 접속도 함께 종료됩니다.")
    print("")
    print(f"교사용 안내 화면: {CLASS_URL}")
    print(f"학생 접속 주소: {STUDENT_URL}")
    print(f"교사 대시보드 주소: {TEACHER_URL}")
    print("")
    print("학생들은 선생님과 같은 와이파이에 연결한 뒤 QR코드 또는 학생 접속 주소로 들어오면 됩니다.")
    print("처음 실행할 때 Windows 방화벽 허용 창이 뜨면 '허용'을 눌러 주세요.")
    print("")
    if OPEN_BROWSER:
        threading.Thread(target=open_class_screen, daemon=True).start()
    uvicorn.run("main:app", host=HOST, port=PORT, reload=False, log_level="info")


if __name__ == "__main__":
    main()
