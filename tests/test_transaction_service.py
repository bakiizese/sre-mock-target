import pytest
from unittest.mock import MagicMock
from transaction_service import TransactionService

def test_get_status_transaction_not_found():
    db_mock = MagicMock()
    db_mock.find.return_value = None
    service = TransactionService(db_mock)
    
    with pytest.raises(ValueError, match="Transaction not found"):
        service.get_status("non_existent_id")

def test_get_status_success():
    db_mock = MagicMock()
    db_mock.find.return_value = {"status": "completed"}
    service = TransactionService(db_mock)
    
    status = service.get_status("valid_id")
    assert status == "completed"