import pytest
from backend.services.payment_processor import PaymentProcessor

class MockDatabase:
    def find(self, transaction_id):
        if transaction_id == "valid_id":
            return {"status": "completed"}
        return None

def test_process_refund_non_existent():
    db = MockDatabase()
    processor = PaymentProcessor(db)
    success, message = processor.process_refund("invalid_id", 100.0)
    assert success is False
    assert message == "Transaction not found"
