import json
import os
from database import DATA_DIR

SETTINGS_PATH = DATA_DIR / "settings.json"
DEFAULT_MODEL = "gpt-4o-mini"


def _read_file():
    if not SETTINGS_PATH.exists():
        return {}
    try:
        return json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _write_file(settings):
    DATA_DIR.mkdir(exist_ok=True)
    SETTINGS_PATH.write_text(json.dumps(settings, ensure_ascii=False, indent=2), encoding="utf-8")


def _mask_key(api_key):
    if not api_key:
        return ""
    return f"{api_key[:7]}...{api_key[-4:]}" if len(api_key) > 12 else "저장됨"


def get_ai_settings_private():
    saved = _read_file()
    api_key = saved.get("openai_api_key") or os.getenv("OPENAI_API_KEY", "")
    return {
        "online_ai_enabled": bool(saved.get("online_ai_enabled", False)),
        "openai_api_key": api_key,
        "model": saved.get("model") or DEFAULT_MODEL,
        "has_saved_key": bool(api_key),
        "key_source": "settings" if saved.get("openai_api_key") else ("environment" if os.getenv("OPENAI_API_KEY") else "none"),
    }


def get_ai_settings_public():
    private = get_ai_settings_private()
    return {
        "online_ai_enabled": private["online_ai_enabled"],
        "has_api_key": private["has_saved_key"],
        "masked_api_key": _mask_key(private["openai_api_key"]),
        "model": private["model"],
        "key_source": private["key_source"],
    }


def save_ai_settings(online_ai_enabled, openai_api_key="", clear_api_key=False, model=DEFAULT_MODEL):
    current = _read_file()
    api_key = (openai_api_key or "").strip()
    if clear_api_key:
        current["openai_api_key"] = ""
    elif api_key:
        current["openai_api_key"] = api_key
    elif "openai_api_key" not in current:
        current["openai_api_key"] = ""
    current["online_ai_enabled"] = bool(online_ai_enabled)
    current["model"] = (model or DEFAULT_MODEL).strip() or DEFAULT_MODEL
    _write_file(current)
    return get_ai_settings_public()
