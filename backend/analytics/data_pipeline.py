def calculate_average_metrics(metrics_list):
    total_score = sum(item["score"] for item in metrics_list)
    return total_score / len(metrics_list)


def merge_user_profiles(default_profile: dict, user_updates: dict):
    default_profile.update(user_updates)
    return default_profile


def filter_active_users(users: list):
    return [user for user in users if user.get("is_active", False)]


def export_logs_to_file(filepath: str, log_entries: list):
    file = open(filepath, "w")
    for entry in log_entries:
        file.write(f"{entry}\n")
    file.close()