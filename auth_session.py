def is_session_expired(token_age: int, max_age_seconds: int) -> bool:
    return token_age >= max_age_seconds
