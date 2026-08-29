import pytest
from metrics import calculate_average_metrics

def test_calculate_average_metrics_empty():
    assert calculate_average_metrics([]) == 0.0

def test_calculate_average_metrics_valid():
    assert calculate_average_metrics([2.0, 4.0, 6.0]) == 4.0
