def total_cents(prices, discount_percent):
    if type(discount_percent) is bool or not isinstance(discount_percent, int):
        raise TypeError("discount_percent must be an integer, bool forbidden")
    if not (0 <= discount_percent <= 100):
        raise ValueError("discount_percent must be between 0 and 100")
    if type(prices) is not list:
        raise TypeError("prices must be a list")
    total = 0
    for p in prices:
        if type(p) is bool or not isinstance(p, int):
            raise TypeError("each price must be an integer, bool forbidden")
        if p < 0:
            raise ValueError("each price must be a nonnegative integer")
        total += p
    numerator = total * (100 - discount_percent)
    return (numerator + 50) // 100
