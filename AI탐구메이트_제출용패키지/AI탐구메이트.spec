# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

# Compatibility wrapper: the build script uses ai_inquiry_mate.spec.
exec((Path(SPECPATH).resolve() / "ai_inquiry_mate.spec").read_text(encoding="utf-8"))
