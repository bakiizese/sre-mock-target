class PaymentProcessor:
    def calculate_total(self, subtotal, promo_code=None):
        if promo_code == 'SAVE20':
            return subtotal * 0.8
        return subtotal