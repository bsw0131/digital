$ErrorActionPreference = 'Stop'

$PackageDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = Split-Path -Parent $PackageDir
$SpecPath = Join-Path $PackageDir 'ai_inquiry_mate.spec'
$DistRoot = Join-Path $Root 'dist'
$SubmitDir = Join-Path $DistRoot 'AI탐구메이트'
$BuildDir = Join-Path $Root 'build'

Set-Location $Root

Write-Host '[1/5] Checking Python...' -ForegroundColor Cyan
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    throw 'Python command was not found. Reinstall Python and check "Add python.exe to PATH".'
}
python --version

Write-Host '[2/5] Installing packages...' -ForegroundColor Cyan
python -m pip install --upgrade pip
python -m pip install -r (Join-Path $Root 'backend\requirements.txt')
python -m pip install pyinstaller

Write-Host '[3/5] Cleaning previous build...' -ForegroundColor Cyan
if (Test-Path $BuildDir) { Remove-Item $BuildDir -Recurse -Force }
if (Test-Path $SubmitDir) { Remove-Item $SubmitDir -Recurse -Force }
New-Item -ItemType Directory -Force -Path $SubmitDir | Out-Null

Write-Host '[4/5] Building AI탐구메이트.exe...' -ForegroundColor Cyan
python -m PyInstaller $SpecPath --noconfirm --distpath $SubmitDir --workpath $BuildDir

Write-Host '[5/5] Creating USB submission folders...' -ForegroundColor Cyan
New-Item -ItemType Directory -Force -Path (Join-Path $SubmitDir 'data') | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $SubmitDir 'assets') | Out-Null
Copy-Item (Join-Path $PackageDir 'README_실행방법.txt') (Join-Path $SubmitDir 'README_실행방법.txt') -Force
Copy-Item (Join-Path $PackageDir '사용설명서_인쇄용.md') (Join-Path $SubmitDir '사용설명서_인쇄용.md') -Force

Write-Host ''
Write-Host 'Build complete.' -ForegroundColor Green
Write-Host "Submission folder: $SubmitDir" -ForegroundColor Green
Write-Host 'Copy this folder to your USB drive.' -ForegroundColor Green
