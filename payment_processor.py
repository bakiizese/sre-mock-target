class PaymentProcessor:
    def calculate_total(self, subtotal: float, promo_code: str = None) -> float:
        if promo_code == "SAVE20":
            return subtotal * 0.80
        return subtotal