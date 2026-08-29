import pytest
from backend.analytics.data_pipeline import filter_active_users

def test_filter_active_users_consecutive_inactives():
    users = [
        {"id": 1, "is_active": False},
        {"id": 2, "is_active": False},
        {"id": 3, "is_active": True},
        {"id": 4, "is_active": False},
        {"id": 5, "is_active": False},
        {"id": 6, "is_active": True}
    ]
    result = filter_active_users(users)
    assert len(result) == 2
    assert result[0]["id"] == 3
    assert result[1]["id"] == 6