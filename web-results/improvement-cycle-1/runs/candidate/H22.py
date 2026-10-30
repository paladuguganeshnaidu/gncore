import math

def categorical_loss_grad(logits, labels):
    if not isinstance(logits, list) or not logits:
        raise ValueError("logits must be a nonempty list")
    if not isinstance(labels, list) or len(labels) != len(logits):
        raise ValueError("labels must match the batch")
    if not isinstance(logits[0], list) or len(logits[0]) < 2:
        raise ValueError("at least two classes are required")
    classes = len(logits[0])
    rows = []
    for row in logits:
        if not isinstance(row, list) or len(row) != classes:
            raise ValueError("logits must be rectangular")
        values = []
        for value in row:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError("logits must be finite numbers")
            try:
                value = float(value)
            except (OverflowError, ValueError):
                raise ValueError("logit is not representable") from None
            if not math.isfinite(value):
                raise ValueError("logits must be finite")
            values.append(value)
        rows.append(values)
    for label in labels:
        if isinstance(label, bool) or not isinstance(label, int):
            raise ValueError("labels must be integer class indices")
        if not 0 <= label < classes:
            raise ValueError("label is outside the class range")
    n = len(rows)
    loss = 0.0
    gradient = []
    for row, label in zip(rows, labels):
        maximum = max(row)
        exponentials = [math.exp(value - maximum) for value in row]
        total = math.fsum(exponentials)
        # Scale before subtracting: the unscaled gap may overflow even
        # when its contribution to the batch mean is representable.
        loss += (maximum / n - row[label] / n) + math.log(total) / n
        gradient.append([
            (exponentials[j] / total - (1.0 if j == label else 0.0)) / n
            for j in range(classes)
        ])
    return loss, gradient
