def allocate_cents(total, weights):
    if isinstance(total, bool) or not isinstance(total, int):
        raise TypeError("total must be an integer")
    if total < 0:
        raise ValueError("total must be nonnegative")
    if not isinstance(weights, list):
        raise TypeError("weights must be a list")
    if not weights:
        raise ValueError("weights must not be empty")
    for weight in weights:
        if isinstance(weight, bool) or not isinstance(weight, int):
            raise TypeError("weights must contain integers")
        if weight <= 0:
            raise ValueError("weights must be positive")

    denominator = sum(weights)
    allocations = []
    remainders = []
    for weight in weights:
        numerator = total * weight
        allocations.append(numerator // denominator)
        remainders.append(numerator % denominator)

    extra = total - sum(allocations)
    order = sorted(range(len(weights)), key=lambda index: (-remainders[index], index))
    for index in order[:extra]:
        allocations[index] += 1
    return allocations