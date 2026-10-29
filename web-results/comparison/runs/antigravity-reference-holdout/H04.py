def allocate_cents(total, weights):
    if isinstance(total, bool) or not isinstance(total, int):
        raise TypeError("total must be an integer, not bool")
    if total < 0:
        raise ValueError("total must be a nonnegative integer")
    if isinstance(weights, bool) or not isinstance(weights, list):
        raise TypeError("weights must be a list")
    if len(weights) == 0:
        raise ValueError("weights must be nonempty")
    for w in weights:
        if isinstance(w, bool) or not isinstance(w, int):
            raise TypeError("each weight must be an integer, not bool")
        if w <= 0:
            raise ValueError("each weight must be a positive integer")
    
    total_weight = sum(weights)
    quotients = []
    remainders = []
    for i, w in enumerate(weights):
        prod = total * w
        q = prod // total_weight
        r = prod % total_weight
        quotients.append(q)
        remainders.append((r, i))
    
    allocated = sum(quotients)
    cents_left = total - allocated
    remainders.sort(key=lambda item: (-item[0], item[1]))
    
    allocations = list(quotients)
    for k in range(cents_left):
        idx = remainders[k][1]
        allocations[idx] += 1
    
    return allocations