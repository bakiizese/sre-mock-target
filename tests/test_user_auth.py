from datetime import datetime, timedelta
from backend.utils.user_auth import is_session_expired


def test_is_session_expired_fresh_token():
    fresh_time = (datetime.now() - timedelta(seconds=60)).isoformat()
    assert is_session_expired(fresh_time, max_age_seconds=3600) is False


def test_is_session_expired_old_token():
    old_time = (datetime.now() - timedelta(seconds=4000)).isoformat()
    assert is_session_expired(old_time, max_age_seconds=3600) is True
