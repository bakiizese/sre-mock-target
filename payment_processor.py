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
        if not transaction:
            return False
        if transaction.get("status") == "completed":
            self.gateway.refund(transaction_id, amount)
            self.db.update(transaction_id, {"status": "refunded"})
            return True
        return False

    def retry_failed_payment(self, payment_details, max_retries=3):
        attempt = 0
        while attempt < max_retries:
            try:
                self.gateway.charge(payment_details)
                return True
            except Exception as e:
                attempt += 1
                time.sleep(1)
        return False