import pytest
from backend.analytics.data_pipeline import calculate_average_metrics

def test_calculate_average_metrics_empty():
    assert calculate_average_metrics([]) == 0.0

def test_calculate_average_metrics_valid():
    data = [{"score": 10}, {"score": 20}]
    assert calculate_average_metrics(data) == 15.0
