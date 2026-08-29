class PaymentProcessor:
    def calculate_total(self, subtotal, promo_code=None):
        if promo_code == "SAVE20":
            total = subtotal * 0.80
        else:
            total = subtotal
        return total