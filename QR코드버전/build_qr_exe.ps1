$ErrorActionPreference = 'Stop'

function Resolve-Python {
    $python = Get-Command python -ErrorAction SilentlyContinue
    if ($python) { return @($python.Source) }

    $py = Get-Command py -ErrorAction SilentlyContinue
    if ($py) { return @($py.Source, '-3') }

    throw 'Python was not found. Install Python 3.11+ and enable "Add python.exe to PATH", then run this script again.'
}

$PackageDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SpecPath = Join-Path $PackageDir 'AI탐구메이트_QR수업모드.spec'
$BuildDir = Join-Path $PackageDir 'build'
$DistDir = Join-Path $PackageDir 'dist'
$PythonArgs = Resolve-Python
$PythonExe = $PythonArgs[0]
$PythonPrefix = @()
if ($PythonArgs.Count -gt 1) {
    $PythonPrefix = $PythonArgs[1..($PythonArgs.Count - 1)]
}

Set-Location $PackageDir

Write-Host '[1/4] Checking Python...' -ForegroundColor Cyan
& $PythonExe @PythonPrefix --version

Write-Host '[2/4] Installing QR version packages...' -ForegroundColor Cyan
& $PythonExe @PythonPrefix -m pip install --upgrade pip
& $PythonExe @PythonPrefix -m pip install -r (Join-Path $PackageDir 'backend\requirements.txt')
& $PythonExe @PythonPrefix -m pip install pyinstaller

Write-Host '[3/4] Cleaning previous QR build...' -ForegroundColor Cyan
if (Test-Path $BuildDir) { Remove-Item $BuildDir -Recurse -Force }
if (Test-Path $DistDir) { Remove-Item $DistDir -Recurse -Force }

Write-Host '[4/4] Building QR classroom executable...' -ForegroundColor Cyan
& $PythonExe @PythonPrefix -m PyInstaller $SpecPath --noconfirm --distpath $DistDir --workpath $BuildDir

Write-Host ''
Write-Host 'QR classroom build complete.' -ForegroundColor Green
Write-Host ('Executable: ' + (Join-Path $DistDir 'AI탐구메이트_QR수업모드.exe')) -ForegroundColor Green
