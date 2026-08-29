def calculate_discount(price, discount_rate):
    if price is None:
        return 0.0
    return price * (1 - discount_rate)