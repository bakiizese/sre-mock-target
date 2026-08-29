def export_logs_to_file(filepath, logs):
    with open(filepath, 'w') as f:
        for log in logs:
            f.write(str(log) + '\n')