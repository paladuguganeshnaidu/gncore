def allocate_cents(total, weights):
    if isinstance(total, bool) or not isinstance(total, int):
        raise TypeError("total must be an integer")
    if not isinstance(weights, list):
        raise TypeError("weights must be a list")
    if not weights:
        raise ValueError("weights must not be empty")
    if total < 0:
        raise ValueError("total must be nonnegative")

    for weight in weights:
        if isinstance(weight, bool) or not isinstance(weight, int):
            raise TypeError("weights must contain integers")
        if weight <= 0:
            raise ValueError("weights must contain positive integers")

    weight_sum = sum(weights)
    allocations = []
    remainders = []
    allocated = 0

    for weight in weights:
        share, remainder = divmod(total * weight, weight_sum)
        allocations.append(share)
        remainders.append(remainder)
        allocated += share

    remaining = total - allocated
    order = sorted(range(len(weights)), key=lambda index: (-remainders[index], index))
    for index in order[:remaining]:
        allocations[index] += 1

    return allocations