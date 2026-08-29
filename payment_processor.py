class PaymentProcessor:
    def calculate_total(self, subtotal, discount_code=None):
        if discount_code == "SAVE20":
            return subtotal * 0.80
        return subtotal