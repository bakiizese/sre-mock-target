def filter_active_users(users):
    for user in users[:]:
        if not user.get('active', False):
            users.remove(user)
    return users