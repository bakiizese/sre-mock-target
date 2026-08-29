import pytest
from backend.services.payment_processor import PaymentProcessor

class MockDB:
    def __init__(self, data=None):
        self.data = data or {}

    def find(self, transaction_id):
        return self.data.get(transaction_id)

def test_process_refund_non_existent():
    db = MockDB({})
    processor = PaymentProcessor(db)
    success, message = processor.process_refund("non_existent_id", 50.0)
    assert success is False
    assert message == "Transaction not found"