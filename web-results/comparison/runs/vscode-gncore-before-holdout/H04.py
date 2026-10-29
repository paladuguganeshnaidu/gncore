def allocate_cents(total, weights):
    if isinstance(total, bool) or not isinstance(total, int):
        raise TypeError("total must be an integer")
    if not isinstance(weights, list):
        raise TypeError("weights must be a list")
    if not weights:
        raise ValueError("weights must not be empty")
    for weight in weights:
        if isinstance(weight, bool) or not isinstance(weight, int):
            raise TypeError("weights must contain integers")
        if weight <= 0:
            raise ValueError("weights must be positive")
    if total < 0:
        raise ValueError("total must be nonnegative")

    denominator = sum(weights)
    quotients = []
    remainders = []
    allocated = 0
    for weight in weights:
        numerator = total * weight
        quotient, remainder = divmod(numerator, denominator)
        quotients.append(quotient)
        remainders.append(remainder)
        allocated += quotient

    remaining = total - allocated
    order = sorted(range(len(weights)), key=lambda index: (-remainders[index], index))
    for index in order[:remaining]:
        quotients[index] += 1
    return quotients