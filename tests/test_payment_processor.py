import pytest
from backend.services.payment_processor import PaymentProcessor

class DummyDB:
    def __init__(self, data=None):
        self.data = data or {}
    def find(self, tid):
        return self.data.get(tid)
    def update(self, tid, val):
        pass

def test_process_refund_non_existent():
    db = DummyDB({}) 
    processor = PaymentProcessor(db)
    with pytest.raises(ValueError, match="Transaction non_existent not found"):
        processor.process_refund("non_existent")