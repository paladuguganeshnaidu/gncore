def allocate_cents(total, weights):
    if isinstance(total, bool) or not isinstance(total, int):
        raise TypeError('total must be an integer')
    if not isinstance(weights, list):
        raise TypeError('weights must be a list')
    for weight in weights:
        if isinstance(weight, bool) or not isinstance(weight, int):
            raise TypeError('weights must contain integers')
    if total < 0:
        raise ValueError('total must be nonnegative')
    if not weights:
        raise ValueError('weights must be nonempty')
    if any(weight <= 0 for weight in weights):
        raise ValueError('weights must be positive')
    denominator = sum(weights)
    shares = [divmod(total * weight, denominator) for weight in weights]
    allocations = [share[0] for share in shares]
    remaining = total - sum(allocations)
    order = sorted(range(len(weights)), key=lambda index: (-shares[index][1], index))
    for index in order[:remaining]:
        allocations[index] += 1
    return allocations
