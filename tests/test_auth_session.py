import pytest
from auth_session import is_session_expired

def test_is_session_expired_valid_token():
    token_age = 100
    max_age_seconds = 3600
    assert is_session_expired(token_age, max_age_seconds) is False

def test_is_session_expired_invalid_token():
    token_age = 4000
    max_age_seconds = 3600
    assert is_session_expired(token_age, max_age_seconds) is True
