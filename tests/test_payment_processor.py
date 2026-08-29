import pytest
from payment_processor import PaymentProcessor

def test_save20_discount():
    processor = PaymentProcessor()
    subtotal = 100.0
    total = processor.calculate_total(subtotal, promo_code="SAVE20")
    assert total == 80.0

def test_no_discount():
    processor = PaymentProcessor()
    subtotal = 100.0
    total = processor.calculate_total(subtotal)
    assert total == 100.0