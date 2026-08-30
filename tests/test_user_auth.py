import pytest
from datetime import datetime, timedelta
from backend.utils.user_auth import hash_password, is_session_expired, parse_user_metadata

def test_hash_password():
    password = "secure_password123"
    hashed = hash_password(password)
    assert isinstance(hashed, str)
    assert len(hashed) == 64

def test_is_session_expired():
    fresh_time = (datetime.now() - timedelta(seconds=10)).isoformat()
    assert not is_session_expired(fresh_time, max_age_seconds=3600)
    expired_time = (datetime.now() - timedelta(seconds=4000)).isoformat()
    assert is_session_expired(expired_time, max_age_seconds=3600)

def test_parse_user_metadata():
    valid_json = '{"user_id": 1, "role": "admin"}'
    assert parse_user_metadata(valid_json) == {"user_id": 1, "role": "admin"}
    invalid_json = '{"user_id": 1,'
    assert parse_user_metadata(invalid_json) == {}
