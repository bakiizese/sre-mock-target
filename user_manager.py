def filter_active_users(users):
    for user in users[:]:
        if not user.get('active', True):
            users.remove(user)
    return users