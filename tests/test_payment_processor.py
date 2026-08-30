import pytest
from unittest.mock import MagicMock, patch
from payment_processor import PaymentProcessor

def test_calculate_total_discount():
    db = MagicMock()
    gateway = MagicMock()
    processor = PaymentProcessor(db, gateway)
    items = [{"price": 100, "quantity": 1}]
    assert processor.calculate_total(items, "SAVE20") == 80.0
    assert processor.calculate_total(items) == 100.0

def test_process_refund_invalid_id():
    db = MagicMock()
    db.find.return_value = None
    gateway = MagicMock()
    processor = PaymentProcessor(db, gateway)
    assert processor.process_refund("invalid_id", 50) is False

def test_process_refund_valid():
    db = MagicMock()
    db.find.return_value = {"status": "completed"}
    gateway = MagicMock()
    processor = PaymentProcessor(db, gateway)
    assert processor.process_refund("valid_id", 50) is True
    gateway.refund.assert_called_once_with("valid_id", 50)
    db.update.assert_called_once_with("valid_id", {"status": "refunded"})

@patch("time.sleep", return_value=None)
def test_retry_failed_payment_terminates(mock_sleep):
    db = MagicMock()
    gateway = MagicMock()
    gateway.charge.side_effect = Exception("Payment failed")
    processor = PaymentProcessor(db, gateway)
    assert processor.retry_failed_payment({"amount": 100}, max_retries=3) is False
    assert gateway.charge.call_count == 3
    assert mock_sleep.call_count == 3