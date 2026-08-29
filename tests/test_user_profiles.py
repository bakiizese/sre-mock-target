import pytest
from user_profiles import merge_user_profiles

def test_merge_user_profiles_mutation():
    default = {'theme': 'dark', 'notifications': True}
    base = {'theme': 'light'}
    
    result1 = merge_user_profiles(base, default)
    assert result1 == {'theme': 'light', 'notifications': True}
    
    # Verify that default was not mutated
    assert default == {'theme': 'dark', 'notifications': True}
    
    result2 = merge_user_profiles({}, default)
    assert result2 == {'theme': 'dark', 'notifications': True}