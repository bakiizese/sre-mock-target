import pytest
from auth import hash_password

def test_hash_password():
    hashed = hash_password("securepassword123")
    assert isinstance(hashed, str)
    assert len(hashed) == 64

def test_hash_password_invalid_type():
    with pytest.raises(TypeError):
        hash_password(None)