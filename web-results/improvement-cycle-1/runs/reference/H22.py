import math


def categorical_loss_grad(logits, labels):
    if not isinstance(logits, list) or not logits:
        raise ValueError("logits must be a nonempty list of rows")
    if not isinstance(labels, list) or len(labels) != len(logits):
        raise ValueError("labels must match the batch")
    if not isinstance(logits[0], list) or len(logits[0]) < 2:
        raise ValueError("at least two classes are required")
    classes = len(logits[0])
    rows = []
    for row, label in zip(logits, labels):
        if not isinstance(row, list) or len(row) != classes:
            raise ValueError("logits must be rectangular")
        if isinstance(label, bool) or not isinstance(label, int):
            raise ValueError("labels must be integer class indices")
        if not 0 <= label < classes:
            raise ValueError("class index out of range")
        converted = []
        for value in row:
            if not isinstance(value, (int, float)):
                raise ValueError("logits must be finite numbers")
            try:
                value = float(value)
            except (TypeError, ValueError, OverflowError) as exc:
                raise ValueError("logits must be finite numbers") from exc
            if not math.isfinite(value):
                raise ValueError("logits must be finite numbers")
            converted.append(value)
        rows.append(converted)

    batch = len(rows)
    losses = []
    gradient = []
    for row, label in zip(rows, labels):
        maximum = max(row)
        shifted = [value - maximum for value in row]
        weights = [math.exp(value) for value in shifted]
        denominator = math.fsum(weights)
        gap = maximum - row[label]
        if math.isfinite(gap):
            scaled_gap = gap / batch
        else:
            scaled_gap = maximum / batch - row[label] / batch
        losses.append(scaled_gap + math.log(denominator) / batch)
        gradient.append([
            (weight / denominator - (1.0 if column == label else 0.0)) / batch
            for column, weight in enumerate(weights)
        ])
    try:
        loss = math.fsum(losses)
    except OverflowError:
        loss = math.inf
    return loss, gradient
