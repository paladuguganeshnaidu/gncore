import math

def categorical_loss_grad(logits, labels):
    if isinstance(logits, bool) or not isinstance(logits, list) or len(logits) == 0:
        raise ValueError("logits must be a nonempty list")
    if isinstance(labels, bool) or not isinstance(labels, list):
        raise ValueError("labels must be a list")

    n_samples = len(logits)
    if len(labels) != n_samples:
        raise ValueError("labels length must match logits length")

    n_classes = None
    for row in logits:
        if isinstance(row, bool) or not isinstance(row, list):
            raise ValueError("each row in logits must be a list")
        if n_classes is None:
            n_classes = len(row)
            if n_classes < 2:
                raise ValueError("logits must have at least 2 classes")
        elif len(row) != n_classes:
            raise ValueError("logits must be a rectangular matrix")
        for val in row:
            if isinstance(val, bool) or not isinstance(val, (int, float)):
                raise ValueError("logit values must be numbers, bool excluded")
            if not math.isfinite(val):
                raise ValueError("logit values must be finite")

    for y in labels:
        if isinstance(y, bool) or not isinstance(y, int):
            raise ValueError("labels must be integers, bool excluded")
        if y < 0 or y >= n_classes:
            raise ValueError("label index out of bounds")

    total_loss = 0.0
    grad_matrix = []

    for i in range(n_samples):
        row = logits[i]
        target = labels[i]
        max_val = max(row)
        exps = [math.exp(v - max_val) for v in row]
        sum_exps = sum(exps)
        log_sum_exp = max_val + math.log(sum_exps)
        loss_i = log_sum_exp - row[target]
        total_loss += loss_i

        probs = [e / sum_exps for e in exps]
        row_grad = [(p - (1.0 if c == target else 0.0)) / n_samples for c, p in enumerate(probs)]
        grad_matrix.append(row_grad)

    mean_loss = total_loss / n_samples
    return mean_loss, grad_matrix