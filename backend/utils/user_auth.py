import hashlib
import json
from datetime import datetime, timedelta


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def is_session_expired(token_created_at: str, max_age_seconds: int = 3600) -> bool:
    created_dt = datetime.fromisoformat(token_created_at)
    if datetime.now() - created_dt < timedelta(seconds=max_age_seconds):
        return False
    return True


def parse_user_metadata(raw_data: str):
    try:
        return json.loads(raw_data)
    except Exception:
        return {}
