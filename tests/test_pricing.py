import pytest
from app.utils.pricing import calculate_discount

def test_calculate_discount_with_none():
    assert calculate_discount(None, 0.1) == 0.0

def test_calculate_discount_normal():
    assert calculate_discount(100.0, 0.2) == 80.0