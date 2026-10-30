import math


def categorical_loss_grad(logits, labels):
    if not isinstance(logits, list) or not logits:
        raise ValueError('logits must be a nonempty list')
    if not isinstance(labels, list) or len(labels) != len(logits):
        raise ValueError('labels must match the batch')
    if not isinstance(logits[0], list) or len(logits[0]) < 2:
        raise ValueError('at least two classes are required')
    classes = len(logits[0])
    rows = []
    for row in logits:
        if not isinstance(row, list) or len(row) != classes:
            raise ValueError('logits must be rectangular')
        values = []
        for value in row:
            if not isinstance(value, (int, float)):
                raise ValueError('logits must be finite numbers')
            try:
                value = float(value)
            except (TypeError, ValueError, OverflowError):
                raise ValueError('logits must be finite numbers') from None
            if not math.isfinite(value):
                raise ValueError('logits must be finite numbers')
            values.append(value)
        rows.append(values)
    for label in labels:
        if isinstance(label, bool) or not isinstance(label, int):
            raise ValueError('labels must be integer indices')
        if not 0 <= label < classes:
            raise ValueError('label out of range')
    batch = len(rows)
    terms = []
    gradient = []
    for row, label in zip(rows, labels):
        maximum = max(row)
        weights = [math.exp(value - maximum) for value in row]
        total = math.fsum(weights)
        # fsum preserves cancellation of large common offsets.
        terms.extend([maximum / batch, -row[label] / batch,
                      math.log(total) / batch])
        gradient.append([
            (weight / total - (1.0 if j == label else 0.0)) / batch
            for j, weight in enumerate(weights)
        ])
    try:
        loss = math.fsum(terms)
    except OverflowError:
        loss = float('inf')
    return loss, gradient
