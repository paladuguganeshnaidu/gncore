def allocate_cents(total, weights):
    if isinstance(total, bool) or not isinstance(total, int):
        raise TypeError("total must be a non-boolean integer")
    if total < 0:
        raise ValueError("total must be nonnegative")
    if isinstance(weights, bool) or not isinstance(weights, list):
        raise TypeError("weights must be a list")
    if len(weights) == 0:
        raise ValueError("weights must be nonempty")
    for w in weights:
        if isinstance(w, bool) or not isinstance(w, int):
            raise TypeError("weight must be a non-boolean integer")
        if w <= 0:
            raise ValueError("weight must be positive")

    sum_weights = sum(weights)
    floor_shares = [(total * w) // sum_weights for w in weights]
    remainders = [(total * w) % sum_weights for w in weights]
    leftover = total - sum(floor_shares)

    sorted_indices = sorted(range(len(weights)), key=lambda i: (-remainders[i], i))
    allocations = list(floor_shares)
    for i in range(leftover):
        allocations[sorted_indices[i]] += 1

    return allocations