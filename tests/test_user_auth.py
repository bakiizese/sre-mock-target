import pytest
from backend.utils.user_auth import hash_password

def test_hash_password():
    password = "securepassword123"
    hashed = hash_password(password)
    assert isinstance(hashed, str)
    assert len(hashed) == 64
    # Verify it matches expected sha256 output for UTF-8 encoded string
    import hashlib
    expected = hashlib.sha256(password.encode('utf-8')).hexdigest()
    assert hashed == expected
