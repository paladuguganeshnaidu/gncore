def total_cents(prices, discount_percent):
    if not isinstance(prices, list):
        raise TypeError("prices must be a list")
    if isinstance(discount_percent, bool) or not isinstance(discount_percent, int):
        raise TypeError("discount_percent must be an integer")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount_percent must be between 0 and 100")

    total = 0
    for price in prices:
        if isinstance(price, bool) or not isinstance(price, int):
            raise TypeError("prices must contain integers")
        if price < 0:
            raise ValueError("prices must be nonnegative")
        total += price

    numerator = total * (100 - discount_percent)
    return (numerator + 50) // 100