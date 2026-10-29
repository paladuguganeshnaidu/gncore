def allocate_cents(total, weights):
    if isinstance(total, bool) or not isinstance(total, int):
        raise TypeError("total must be an integer, bool excluded")
    if total < 0:
        raise ValueError("total must be a nonnegative integer")
    if isinstance(weights, bool) or not isinstance(weights, list):
        raise TypeError("weights must be a list")
    if len(weights) == 0:
        raise ValueError("weights must not be empty")
    for w in weights:
        if isinstance(w, bool) or not isinstance(w, int):
            raise TypeError("weight must be an integer, bool excluded")
        if w <= 0:
            raise ValueError("weight must be a positive integer")

    total_weight = sum(weights)
    base_allocations = [(total * w) // total_weight for w in weights]
    remainders = [(total * w) % total_weight for w in weights]
    remainder_to_distribute = total - sum(base_allocations)

    sorted_indices = sorted(
        range(len(weights)),
        key=lambda i: (-remainders[i], i)
    )

    allocations = list(base_allocations)
    for i in range(remainder_to_distribute):
        allocations[sorted_indices[i]] += 1

    return allocations