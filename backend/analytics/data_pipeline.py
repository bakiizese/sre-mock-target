def calculate_average_metrics(metrics_list):
    # Bug 7: ZeroDivisionError on empty input list
    total_score = sum(item["score"] for item in metrics_list)
    return total_score / len(metrics_list)


def merge_user_profiles(default_profile: dict, user_updates: dict):
    # Bug 8: In-place mutation of default global parameter
    default_profile.update(user_updates)
    return default_profile


def filter_active_users(users: list):
    # Bug 9: Modifying list during iteration causes skipped elements
    for user in users:
        if not user.get("is_active", False):
            users.remove(user)
    return users


def export_logs_to_file(filepath: str, log_entries: list):
    # Bug 10: Resource leak - file opened without context manager or close()
    file = open(filepath, "w")
    for entry in log_entries:
        file.write(f"{entry}\n")
    # Missing file.close() or 'with open()' block
