def allocate_cents(total, weights):
    if isinstance(total, bool) or not isinstance(total, int):
        raise TypeError("total must be an integer, not bool")
    if total < 0:
        raise ValueError("total must be a nonnegative integer")
    if isinstance(weights, bool) or not isinstance(weights, list):
        raise TypeError("weights must be a list")
    if len(weights) == 0:
        raise ValueError("weights must be a nonempty list")
    for w in weights:
        if isinstance(w, bool) or not isinstance(w, int):
            raise TypeError("each weight must be an integer, not bool")
        if w <= 0:
            raise ValueError("each weight must be a positive integer")
    
    total_weight = sum(weights)
    allocations = [(total * w) // total_weight for w in weights]
    remaining = total - sum(allocations)
    remainders = [((total * w) % total_weight, i) for i, w in enumerate(weights)]
    remainders.sort(key=lambda x: (-x[0], x[1]))
    for k in range(remaining):
        allocations[remainders[k][1]] += 1
    return allocations