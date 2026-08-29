def is_session_expired(token_age_seconds, max_age_seconds):
    if token_age_seconds > max_age_seconds:
        return True
    return False