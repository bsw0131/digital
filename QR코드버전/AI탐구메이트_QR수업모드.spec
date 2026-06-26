# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

PACKAGE_DIR = Path(SPECPATH).resolve()

hiddenimports = [
    "ai_engine",
    "database",
    "offline_engine",
    "settings_store",
    "main",
    "qrcode",
    "qrcode.image.svg",
    "h11",
    "uvicorn.logging",
    "uvicorn.loops",
    "uvicorn.loops.auto",
    "uvicorn.protocols",
    "uvicorn.protocols.http",
    "uvicorn.protocols.http.auto",
    "uvicorn.protocols.websockets",
    "uvicorn.protocols.websockets.auto",
    "uvicorn.lifespan",
    "uvicorn.lifespan.on",
]

a = Analysis(
    [str(PACKAGE_DIR / "launcher.py")],
    pathex=[str(PACKAGE_DIR / "backend")],
    binaries=[],
    datas=[
        (str(PACKAGE_DIR / "frontend"), "frontend"),
        (str(PACKAGE_DIR / "backend"), "backend"),
    ],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["pytest", "IPython", "jupyter"],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="AI탐구메이트_QR수업모드",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
