$ErrorActionPreference = 'Stop'

function Decode-Utf8Name($Base64Text) {
    return [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($Base64Text))
}

function Resolve-Python {
    $python = Get-Command python -ErrorAction SilentlyContinue
    if ($python) {
        return @($python.Source)
    }

    $py = Get-Command py -ErrorAction SilentlyContinue
    if ($py) {
        return @($py.Source, '-3')
    }

    throw 'Python was not found. Install Python 3.11+ and enable "Add python.exe to PATH", then run this script again.'
}

$AppName = Decode-Utf8Name 'QUntg5DqtazrqZTsnbTtirg='
$ReadmeName = Decode-Utf8Name 'UkVBRE1FX+yLpO2WieuwqeuylS50eHQ='
$GuideName = Decode-Utf8Name '7IKs7Jqp7ISk66qF7IScX+yduOyHhOyaqS5tZA=='

$PackageDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = Split-Path -Parent $PackageDir
$SpecPath = Join-Path $PackageDir 'ai_inquiry_mate.spec'
$DistRoot = Join-Path $Root 'dist'
$SubmitDir = Join-Path $DistRoot $AppName
$BuildDir = Join-Path $Root 'build'
$PythonArgs = Resolve-Python
$PythonExe = $PythonArgs[0]
$PythonPrefix = @()
if ($PythonArgs.Count -gt 1) {
    $PythonPrefix = $PythonArgs[1..($PythonArgs.Count - 1)]
}

Set-Location $Root

Write-Host '[1/5] Checking Python...' -ForegroundColor Cyan
& $PythonExe @PythonPrefix --version

Write-Host '[2/5] Installing build packages...' -ForegroundColor Cyan
& $PythonExe @PythonPrefix -m pip install --upgrade pip
& $PythonExe @PythonPrefix -m pip install -r (Join-Path $Root 'backend\requirements.txt')
& $PythonExe @PythonPrefix -m pip install pyinstaller

Write-Host '[3/5] Cleaning previous build...' -ForegroundColor Cyan
if (Test-Path $BuildDir) { Remove-Item $BuildDir -Recurse -Force }
if (Test-Path $SubmitDir) { Remove-Item $SubmitDir -Recurse -Force }
New-Item -ItemType Directory -Force -Path $SubmitDir | Out-Null

Write-Host '[4/5] Building executable with latest frontend/backend...' -ForegroundColor Cyan
& $PythonExe @PythonPrefix -m PyInstaller $SpecPath --noconfirm --distpath $SubmitDir --workpath $BuildDir

Write-Host '[5/5] Creating submission folders...' -ForegroundColor Cyan
New-Item -ItemType Directory -Force -Path (Join-Path $SubmitDir 'data') | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $SubmitDir 'assets') | Out-Null
Copy-Item (Join-Path $PackageDir $ReadmeName) (Join-Path $SubmitDir $ReadmeName) -Force
Copy-Item (Join-Path $PackageDir $GuideName) (Join-Path $SubmitDir $GuideName) -Force

Write-Host ''
Write-Host 'Build complete.' -ForegroundColor Green
Write-Host ('Submission folder: ' + $SubmitDir) -ForegroundColor Green
Write-Host 'Copy this folder to your USB drive or compress it for submission.' -ForegroundColor Green
