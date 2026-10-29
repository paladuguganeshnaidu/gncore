import math

def categorical_loss_grad(logits, labels):
    if not isinstance(logits, list) or not logits:
        raise ValueError("logits must be a nonempty list")
    if not isinstance(labels, list) or len(labels) != len(logits):
        raise ValueError("labels must match logits length")

    classes = None
    for row in logits:
        if not isinstance(row, list) or not row:
            raise ValueError("logits must be nonempty lists")
        if classes is None:
            classes = len(row)
        elif len(row) != classes:
            raise ValueError("logits must be rectangular")
        for value in row:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError("logits must contain finite numbers")
            if not math.isfinite(value):
                raise ValueError("logits must contain finite numbers")
    if classes < 2:
        raise ValueError("logits must contain at least two classes")

    for label in labels:
        if isinstance(label, bool) or not isinstance(label, int):
            raise ValueError("labels must be integer class indices")
        if label < 0 or label >= classes:
            raise ValueError("label is out of range")

    count = len(logits)
    loss = 0.0
    gradient = []
    for row, label in zip(logits, labels):
        maximum = max(row)
        shifted = [math.exp(value - maximum) for value in row]
        total = sum(shifted)
        probabilities = [value / total for value in shifted]
        loss += math.log(total) + maximum - row[label]
        gradient.append([
            (probability - (1.0 if index == label else 0.0)) / count
            for index, probability in enumerate(probabilities)
        ])
    return loss / count, gradient