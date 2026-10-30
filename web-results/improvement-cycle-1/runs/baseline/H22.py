import math

def categorical_loss_grad(logits, labels):
    if not isinstance(logits, list) or not logits:
        raise ValueError('logits must be a nonempty list')
    if not isinstance(labels, list) or len(labels) != len(logits):
        raise ValueError('labels must match the batch')
    if not isinstance(logits[0], list) or len(logits[0]) < 2:
        raise ValueError('at least two classes are required')
    n = len(logits)
    c = len(logits[0])
    rows = []
    for row in logits:
        if not isinstance(row, list) or len(row) != c:
            raise ValueError('logits must be rectangular')
        converted = []
        for value in row:
            if not isinstance(value, (int, float)):
                raise ValueError('logits must be numeric')
            try:
                value = float(value)
            except (TypeError, ValueError, OverflowError):
                raise ValueError('logits must be finite floats') from None
            if not math.isfinite(value):
                raise ValueError('logits must be finite')
            converted.append(value)
        rows.append(converted)
    for label in labels:
        if isinstance(label, bool) or not isinstance(label, int):
            raise ValueError('labels must be integer indices')
        if not 0 <= label < c:
            raise ValueError('label outside class range')
    mean_loss = 0.0
    gradient = []
    for row, label in zip(rows, labels):
        maximum = max(row)
        weights = [math.exp(value - maximum) for value in row]
        total = math.fsum(weights)
        gap = maximum - row[label]
        # Scale before subtracting only when the unscaled gap overflows.
        scaled_gap = gap / n if math.isfinite(gap) else maximum / n - row[label] / n
        mean_loss += scaled_gap + math.log(total) / n
        gradient.append([(weight / total - (1.0 if j == label else 0.0)) / n
                         for j, weight in enumerate(weights)])
    return mean_loss, gradient
