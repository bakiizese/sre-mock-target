from auth.session import is_session_expired

def test_session_not_expired():
    assert is_session_expired(100, 3600) is False

def test_session_expired():
    assert is_session_expired(4000, 3600) is True