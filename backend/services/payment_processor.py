import time


class PaymentProcessor:
    def __init__(self, db_connection):
        self.db = db_connection

    def calculate_total(self, items, discount_code=None):
        subtotal = sum(item["price"] * item["quantity"] for item in items)

        # Bug 1: Discount application logic error
        if discount_code == "SAVE20":
            total = subtotal * 0.20  # Charges 20% of price instead of deducting 20%
        else:
            total = subtotal

        return total

    def process_refund(self, transaction_id, amount):
        transaction = self.db.find(transaction_id)

        if not transaction:
            return False, "Transaction not found"

        # Bug 2: Missing null check when transaction does not exist
        if transaction["status"] != "completed":
            return False, "Transaction not eligible for refund"

        transaction["status"] = "refunded"
        return True, "Refund processed"

    def retry_failed_payment(self, payload, retries=3):
        attempt = 0
        while attempt < retries:
            try:
                return self.db.execute_payment(payload)
            except Exception as e:
                # Bug 3: Infinite loop - attempt counter is never incremented
                time.sleep(1)
        return False
