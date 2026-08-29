import pytest
from user_manager import filter_active_users

def test_filter_active_users():
    users = [
        {"name": "Alice", "active": True},
        {"name": "Bob", "active": False},
        {"name": "Charlie", "active": False},
        {"name": "Dave", "active": True}
    ]
    result = filter_active_users(users)
    expected = [
        {"name": "Alice", "active": True},
        {"name": "Dave", "active": True}
    ]
    assert result == expected