import json
import os
from pathlib import Path

from database import DATA_DIR

SETTINGS_PATH = DATA_DIR / "settings.json"
DEFAULT_MODEL = "gpt-5.6-terra"


def _read_file() -> dict:
    if not SETTINGS_PATH.exists():
        return {}
    try:
        return json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _write_file(settings: dict) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    SETTINGS_PATH.write_text(json.dumps(settings, ensure_ascii=False, indent=2), encoding="utf-8")


def _looks_like_openai_key(api_key: str) -> bool:
    value = (api_key or "").strip()
    return value.startswith("sk-") and len(value) >= 20


def validate_openai_api_key(api_key: str) -> None:
    value = (api_key or "").strip()
    if not _looks_like_openai_key(value):
        raise ValueError("OpenAI API 키 형식이 올바르지 않습니다. sk-로 시작하는 키를 입력하세요.")

    from openai import APIConnectionError, AuthenticationError, OpenAI, OpenAIError, RateLimitError

    try:
        client = OpenAI(api_key=value, timeout=12.0, max_retries=0)
        client.models.list()
    except AuthenticationError as exc:
        raise ValueError("유효하지 않은 OpenAI API 키입니다. 키를 다시 확인하세요.") from exc
    except (APIConnectionError, RateLimitError) as exc:
        raise RuntimeError("OpenAI 서버에 연결하지 못해 키를 확인할 수 없습니다. 잠시 후 다시 시도하세요.") from exc
    except OpenAIError as exc:
        raise RuntimeError("OpenAI API 키 확인에 실패했습니다. 계정 상태와 인터넷 연결을 확인하세요.") from exc


def _mask_key(api_key: str) -> str:
    if not api_key:
        return ""
    if len(api_key) <= 12:
        return "저장됨"
    return f"{api_key[:7]}...{api_key[-4:]}"


def get_ai_settings_private() -> dict:
    saved = _read_file()
    api_key = saved.get("openai_api_key") or os.getenv("OPENAI_API_KEY", "")
    has_valid_format = _looks_like_openai_key(api_key)
    return {
        "online_ai_enabled": bool(saved.get("online_ai_enabled", False) and has_valid_format),
        "openai_api_key": api_key,
        "model": saved.get("model") or DEFAULT_MODEL,
        "has_saved_key": has_valid_format,
        "key_source": "settings" if saved.get("openai_api_key") else ("environment" if os.getenv("OPENAI_API_KEY") else "none"),
    }


def get_teacher_auth_public() -> dict:
    saved = _read_file()
    return {
        "has_password": bool(saved.get("teacher_password")),
        "has_hint": bool((saved.get("teacher_password_hint") or "").strip()),
    }


def verify_teacher_password(password: str = "") -> bool:
    saved = _read_file()
    teacher_password = saved.get("teacher_password") or ""
    if not teacher_password:
        return True
    return (password or "") == teacher_password


def save_teacher_password(password: str, hint: str = "", current_password: str = "") -> dict:
    new_password = (password or "").strip()
    if not new_password:
        raise ValueError("password is required")
    saved = _read_file()
    if saved.get("teacher_password") and not verify_teacher_password(current_password):
        raise PermissionError("invalid teacher password")
    saved["teacher_password"] = new_password
    saved["teacher_password_hint"] = (hint or "").strip()
    _write_file(saved)
    return get_teacher_auth_public()


def recover_teacher_password(hint: str = "") -> str:
    saved = _read_file()
    expected_hint = (saved.get("teacher_password_hint") or "").strip()
    if not saved.get("teacher_password") or not expected_hint:
        return ""
    if (hint or "").strip() != expected_hint:
        return ""
    return saved.get("teacher_password") or ""


def get_ai_settings_public() -> dict:
    private = get_ai_settings_private()
    return {
        "online_ai_enabled": private["online_ai_enabled"],
        "has_api_key": private["has_saved_key"],
        "masked_api_key": _mask_key(private["openai_api_key"]),
        "model": private["model"],
        "key_source": private["key_source"],
    }


def save_ai_settings(online_ai_enabled: bool, openai_api_key: str = "", clear_api_key: bool = False) -> dict:
    current = _read_file()
    api_key = (openai_api_key or "").strip()
    existing_key = current.get("openai_api_key") or os.getenv("OPENAI_API_KEY", "")

    if clear_api_key:
        current["openai_api_key"] = ""
        current["online_ai_enabled"] = False
    else:
        candidate_key = api_key or existing_key
        if api_key or online_ai_enabled:
            if not candidate_key:
                raise ValueError("AI 모드를 사용하려면 OpenAI API 키를 입력하세요.")
            validate_openai_api_key(candidate_key)
        if api_key:
            current["openai_api_key"] = api_key
        elif "openai_api_key" not in current:
            current["openai_api_key"] = ""
        current["online_ai_enabled"] = bool(online_ai_enabled and candidate_key)

    current["model"] = DEFAULT_MODEL
    _write_file(current)
    return get_ai_settings_public()


def set_ai_mode_enabled(enabled: bool) -> dict:
    current = _read_file()
    api_key = current.get("openai_api_key") or os.getenv("OPENAI_API_KEY", "")
    if enabled:
        if not api_key:
            raise ValueError("AI 모드를 사용하려면 API 키를 먼저 저장하세요.")
        validate_openai_api_key(api_key)
    current["online_ai_enabled"] = bool(enabled and api_key)
    current["model"] = DEFAULT_MODEL
    _write_file(current)
    return get_ai_settings_public()
