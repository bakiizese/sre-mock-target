import pytest
from user_manager import filter_active_users

def test_filter_active_users():
    users = [
        {"name": "Alice", "active": False},
        {"name": "Bob", "active": False},
        {"name": "Charlie", "active": True}
    ]
    filtered = filter_active_users(users)
    assert filtered == [{"name": "Charlie", "active": True}]