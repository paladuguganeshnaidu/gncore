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
    weight_sum = sum(weights)
    numerators = [total * weight for weight in weights]
    allocations = [numerator // weight_sum for numerator in numerators]
    remaining = total - sum(allocations)
    order = sorted(range(len(weights)), key=lambda index: (-numerators[index] % weight_sum, index))
    for index in order[:remaining]:
        allocations[index] += 1
    return allocations