import pytest
from unittest.mock import MagicMock
from backend.services.payment_processor import PaymentProcessor

def test_process_refund_transaction_not_found():
    mock_db = MagicMock()
    mock_db.find.return_value = None
    processor = PaymentProcessor(mock_db)
    success, message = processor.process_refund("non_existent_id", 50.0)
    assert success is False
    assert message == "Transaction not found"
