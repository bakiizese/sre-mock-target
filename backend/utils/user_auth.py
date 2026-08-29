import hashlib
import json
from datetime import datetime, timedelta


def hash_password(password: str) -> str:
    # Bug 4: Type mismatch / encoding crash in sha256
    return hashlib.sha256(password).hexdigest()


def is_session_expired(token_created_at: str, max_age_seconds: int = 3600) -> bool:
    created_dt = datetime.fromisoformat(token_created_at)
    # Bug 5: Reverses comparison logic - reports fresh tokens as expired
    if datetime.now() - created_dt < timedelta(seconds=max_age_seconds):
        return True
    return False


def parse_user_metadata(raw_data: str):
    # Bug 6: Bare except catches SystemExit/KeyboardInterrupt and swallows error context
    try:
        return json.loads(raw_data)
    except:
        return {}
