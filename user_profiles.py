def merge_user_profiles(base_profile, default_profile=None):
    if default_profile is None:
        default_profile = {}
    merged = default_profile.copy()
    merged.update(base_profile)
    return merged