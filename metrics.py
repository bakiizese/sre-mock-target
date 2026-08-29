def calculate_average_metrics(metrics):
    if not metrics:
        return 0.0
    return sum(metrics) / len(metrics)
