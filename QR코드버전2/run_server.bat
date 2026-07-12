@echo off
chcp 65001 > nul
title AI탐구메이트 QR코드버전2
cd /d %~dp0backend
echo [AI탐구메이트] 필요한 패키지를 확인합니다.
python -m pip install -r requirements.txt
echo.
echo [AI탐구메이트] 서버를 실행합니다.
echo 실행 PC 주소: http://127.0.0.1:8000
echo 학생 접속 주소: http://실행PC_IP주소:8000
echo.
start "" http://127.0.0.1:8000
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
pause
