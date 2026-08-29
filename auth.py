import hashlib

def hash_password(password: str) -> str:
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    return hashlib.sha256(password.encode('utf-8')).hexdigest()