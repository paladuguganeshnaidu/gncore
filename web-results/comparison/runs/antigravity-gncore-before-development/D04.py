def total_cents(prices, discount_percent):
    if isinstance(discount_percent, bool) or not isinstance(discount_percent, int):
        raise TypeError("discount_percent must be an integer")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount_percent must be between 0 and 100")
    if isinstance(prices, bool) or not isinstance(prices, list):
        raise TypeError("prices must be a list")
    total = 0
    for p in prices:
        if isinstance(p, bool) or not isinstance(p, int):
            raise TypeError("prices must contain only integers")
        if p < 0:
            raise ValueError("prices must be nonnegative")
        total += p
    numerator = total * (100 - discount_percent)
    return (numerator + 50) // 100
