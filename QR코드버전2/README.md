# AI탐구메이트 QR코드버전2

USB 제출용으로 정리한 실행 폴더입니다. 실행에 필요한 핵심 파일만 포함했습니다.

## 실행 방법

1. Windows PC에 Python이 설치되어 있는지 확인합니다.
2. 이 폴더의 `run_server.bat` 파일을 더블클릭합니다.
3. 서버가 켜지면 실행 PC에서는 아래 주소로 접속합니다.

```text
http://127.0.0.1:8000
```

4. 학생 기기에서는 같은 Wi-Fi에 연결한 뒤, 실행 PC의 IP 주소로 접속합니다.

```text
http://실행PC_IP주소:8000
```

## 폴더 구성

```text
QR코드버전2/
├─ run_server.bat
├─ backend/
├─ frontend/
├─ data/
└─ README.md
```

## 교사 로그인

기본 비밀번호는 `teacher1234`입니다.

## 주의

- `data/` 폴더에는 학생 탐구 기록과 교사 피드백이 저장됩니다.
- `data/settings.json`에 OpenAI API 키가 저장될 수 있으므로 제출 전 확인하세요.
- `__pycache__`, `.git`, `build`, `dist`, `.venv` 같은 개발/캐시 폴더는 포함하지 않았습니다.
