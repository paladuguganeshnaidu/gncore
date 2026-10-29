import math

def categorical_loss_grad(logits, labels):
    if not isinstance(logits, list) or not logits:
        raise ValueError("logits must be a nonempty list")
    if not isinstance(labels, list) or len(labels) != len(logits):
        raise ValueError("labels must match logits")
    class_count = None
    for row in logits:
        if not isinstance(row, list) or not row:
            raise ValueError("logits must contain nonempty rows")
        if class_count is None:
            class_count = len(row)
        elif len(row) != class_count:
            raise ValueError("logits must be rectangular")
        if class_count < 2:
            raise ValueError("at least two classes are required")
        for value in row:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError("logits must be numeric")
            if not math.isfinite(value):
                raise ValueError("logits must be finite")
    for label in labels:
        if isinstance(label, bool) or not isinstance(label, int):
            raise ValueError("labels must be integer class indices")
        if label < 0 or label >= class_count:
            raise ValueError("label is out of range")
    count = len(logits)
    loss = 0.0
    gradient = []
    for row, label in zip(logits, labels):
        maximum = max(row)
        exponentials = [math.exp(value - maximum) for value in row]
        total = sum(exponentials)
        probabilities = [value / total for value in exponentials]
        loss += maximum + math.log(total) - row[label]
        gradient.append([(probability - (index == label)) / count for index, probability in enumerate(probabilities)])
    return loss / count, gradient