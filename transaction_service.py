class TransactionService:
    def __init__(self, db):
        self.db = db

    def get_status(self, transaction_id):
        transaction = self.db.find(transaction_id)
        if transaction is None:
            raise ValueError("Transaction not found")
        return transaction['status']