import pytest
from unittest.mock import MagicMock
from backend.services.payment_processor import PaymentProcessor

def test_retry_failed_payment_exhaustion():
    db_mock = MagicMock()
    db_mock.execute_payment.side_effect = Exception("Payment failed")
    processor = PaymentProcessor(db_mock)
    
    result = processor.retry_failed_payment({"amount": 100}, retries=3)
    
    assert result is False
    assert db_mock.execute_payment.call_count == 3
