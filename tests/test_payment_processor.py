import pytest
import time
from unittest.mock import MagicMock
from payment_processor import PaymentProcessor

def test_calculate_total_discount():
    db = MagicMock()
    gateway = MagicMock()
    processor = PaymentProcessor(db, gateway)
    items = [{"price": 100, "quantity": 1}]
    total = processor.calculate_total(items, discount_code="SAVE20")
    assert total == 80.0

def test_process_refund_invalid_id():
    db = MagicMock()
    db.find.return_value = None
    gateway = MagicMock()
    processor = PaymentProcessor(db, gateway)
    result = processor.process_refund("invalid_id", 50)
    assert result is False

def test_retry_failed_payment_terminates():
    db = MagicMock()
    gateway = MagicMock()
    gateway.charge.side_effect = Exception("Payment failed")
    processor = PaymentProcessor(db, gateway)
    
    original_sleep = time.sleep
    time.sleep = MagicMock()
    
    try:
        result = processor.retry_failed_payment({"amount": 100}, max_retries=3)
        assert result is False
        assert gateway.charge.call_count == 3
        assert time.sleep.call_count == 3
    finally:
        time.sleep = original_sleep