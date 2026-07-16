import json
import os
import re
from pathlib import Path

from database import DATA_DIR

SETTINGS_PATH = DATA_DIR / "settings.json"
DEFAULT_MODEL = "gpt-4.1"
MODEL_PREFERENCES = ["gpt-5.6-terra", "gpt-5.6-luna", "gpt-4.1", "gpt-4.1-mini", "chat-latest"]


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
    return len((api_key or "").strip()) >= 20


def _probe_chat_model(client, model: str) -> None:
    from openai import BadRequestError

    params = {
        "model": model,
        "messages": [{"role": "user", "content": "연결 확인"}],
    }
    if model.startswith("gpt-5"):
        params["reasoning_effort"] = "none"
    try:
        response = client.chat.completions.create(**params, max_completion_tokens=96)
    except BadRequestError as exc:
        message = str(exc).lower()
        if "reasoning_effort" in message:
            params.pop("reasoning_effort", None)
            response = client.chat.completions.create(**params, max_completion_tokens=96)
        elif "max_completion_tokens" in message or "unsupported parameter" in message:
            params.pop("reasoning_effort", None)
            response = client.chat.completions.create(**params, max_tokens=96)
        else:
            raise
    if not (response.choices[0].message.content or "").strip():
        raise RuntimeError("모델이 텍스트를 반환하지 않았습니다.")


def select_working_model(api_key: str, current_model: str = "", excluded_models=None) -> str:
    value = (api_key or "").strip()
    excluded = set(excluded_models or [])
    if not _looks_like_openai_key(value):
        raise ValueError("OpenAI API 키가 너무 짧거나 형식이 올바르지 않습니다.")

    from openai import APIConnectionError, AuthenticationError, OpenAI, OpenAIError, RateLimitError

    client = OpenAI(api_key=value, timeout=25.0, max_retries=0)
    try:
        available = {item.id for item in client.models.list().data}
    except AuthenticationError as exc:
        raise ValueError("유효하지 않은 OpenAI API 키입니다. 키를 다시 확인하세요.") from exc
    except (APIConnectionError, RateLimitError) as exc:
        raise RuntimeError("OpenAI 서버에 연결하지 못해 모델을 확인할 수 없습니다. 잠시 후 다시 시도하세요.") from exc
    except OpenAIError as exc:
        raise RuntimeError(f"OpenAI 모델 목록 확인에 실패했습니다: {exc}") from exc

    candidates = []
    for model in [current_model, *MODEL_PREFERENCES]:
        if model and model in available and model not in candidates and model not in excluded:
            candidates.append(model)

    discovered = sorted(
        (
            model
            for model in available
            if model.startswith("gpt-")
            and not re.search(r"-\d{4}-\d{2}-\d{2}$", model)
            and not any(word in model for word in ["audio", "realtime", "transcribe", "tts", "image", "search", "instruct", "codex"])
        ),
        reverse=True,
    )
    candidates.extend(model for model in discovered if model not in candidates and model not in excluded)

    last_error = None
    for model in candidates:
        try:
            _probe_chat_model(client, model)
            return model
        except AuthenticationError as exc:
            raise ValueError("유효하지 않은 OpenAI API 키입니다. 키를 다시 확인하세요.") from exc
        except (OpenAIError, RuntimeError) as exc:
            last_error = exc

    detail = f" 마지막 오류: {last_error}" if last_error else ""
    raise RuntimeError("이 API 키로 사용할 수 있는 텍스트 생성 모델을 찾지 못했습니다." + detail)


def validate_openai_api_key(api_key: str, current_model: str = "") -> str:
    return select_working_model(api_key, current_model)


def refresh_ai_model(api_key: str, current_model: str = "", excluded_models=None) -> str:
    selected = select_working_model(api_key, current_model, excluded_models)
    settings = _read_file()
    settings["model"] = selected
    _write_file(settings)
    return selected


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
            selected_model = validate_openai_api_key(candidate_key, current.get("model", ""))
        if api_key:
            current["openai_api_key"] = api_key
        elif "openai_api_key" not in current:
            current["openai_api_key"] = ""
        current["online_ai_enabled"] = bool(online_ai_enabled and candidate_key)

    current["model"] = locals().get("selected_model", current.get("model") or DEFAULT_MODEL)
    _write_file(current)
    return get_ai_settings_public()


def set_ai_mode_enabled(enabled: bool) -> dict:
    current = _read_file()
    api_key = current.get("openai_api_key") or os.getenv("OPENAI_API_KEY", "")
    if enabled:
        if not api_key:
            raise ValueError("AI 모드를 사용하려면 API 키를 먼저 저장하세요.")
        selected_model = validate_openai_api_key(api_key, current.get("model", ""))
    current["online_ai_enabled"] = bool(enabled and api_key)
    current["model"] = locals().get("selected_model", current.get("model") or DEFAULT_MODEL)
    _write_file(current)
    return get_ai_settings_public()
