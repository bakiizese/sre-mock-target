import pytest
from payment_processor import PaymentProcessor

def test_save20_discount():
    processor = PaymentProcessor()
    total = processor.calculate_total(100.0, promo_code='SAVE20')
    assert total == 80.0