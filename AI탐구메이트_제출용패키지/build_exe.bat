@echo off
chcp 65001 > nul
setlocal

cd /d "%~dp0.."

echo [1/4] Python 패키지를 설치합니다.
python -m pip install --upgrade pip
python -m pip install -r backend\requirements.txt
python -m pip install pyinstaller

echo [2/4] 기존 빌드 결과를 정리합니다.
if exist build rmdir /s /q build
if exist dist\AI탐구메이트 rmdir /s /q dist\AI탐구메이트

echo [3/4] AI탐구메이트.exe를 만듭니다.
python -m PyInstaller AI탐구메이트_제출용패키지\AI탐구메이트.spec --noconfirm --distpath dist\AI탐구메이트 --workpath build

echo [4/4] 제출용 폴더를 구성합니다.
if not exist dist\AI탐구메이트\data mkdir dist\AI탐구메이트\data
if not exist dist\AI탐구메이트\assets mkdir dist\AI탐구메이트\assets
copy /Y AI탐구메이트_제출용패키지\README_실행방법.txt dist\AI탐구메이트\README_실행방법.txt > nul
copy /Y AI탐구메이트_제출용패키지\사용설명서_인쇄용.md dist\AI탐구메이트\사용설명서_인쇄용.md > nul

echo.
echo 완료되었습니다.
echo 제출용 폴더: dist\AI탐구메이트
echo 이 폴더를 USB에 복사하면 됩니다.
echo.
pause
