class PaymentProcessor:
    def __init__(self, db):
        self.db = db

    def process_refund(self, transaction_id):
        transaction = self.db.find(transaction_id)
        if transaction is None:
            raise ValueError(f"Transaction with id {transaction_id} not found.")
        if transaction['status'] != 'completed':
            raise ValueError("Only completed transactions can be refunded.")
        return self.db.update(transaction_id, {'status': 'refunded'})