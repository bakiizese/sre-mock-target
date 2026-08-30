import time

class PaymentProcessor:
    def __init__(self, db, gateway):
        self.db = db
        self.gateway = gateway

    def calculate_total(self, items, discount_code=None):
        subtotal = sum(item['price'] * item['quantity'] for item in items)
        if discount_code == "SAVE20":
            total = subtotal * 0.80
        else:
            total = subtotal
        return total

    def process_refund(self, transaction_id, amount):
        transaction = self.db.find(transaction_id)
        if transaction is None:
            return False
        if transaction.get("status") == "completed":
            self.gateway.refund(transaction_id, amount)
            transaction["status"] = "refunded"
            self.db.save(transaction)
            return True
        return False

    def retry_failed_payment(self, payload, max_retries=3):
        attempt = 0
        while attempt < max_retries:
            try:
                self.gateway.charge(payload)
                return True
            except Exception as e:
                attempt += 1
                time.sleep(1)
        return False