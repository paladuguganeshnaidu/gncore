import math

def categorical_loss_grad(logits, labels):
    if not isinstance(logits, list) or not logits:
        raise ValueError("logits must be a nonempty list")
    if not isinstance(labels, list) or len(labels) != len(logits):
        raise ValueError("labels must match logits length")
    if len(logits[0]) < 2:
        raise ValueError("at least two classes are required")
    classes = len(logits[0])
    for row in logits:
        if not isinstance(row, list) or len(row) != classes:
            raise ValueError("logits must be rectangular")
        for value in row:
            if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value):
                raise ValueError("logits must contain finite numeric values")
    for label in labels:
        if isinstance(label, bool) or not isinstance(label, int) or label < 0 or label >= classes:
            raise ValueError("labels must be valid integer class indices")

    loss = 0.0
    gradients = []
    count = len(logits)
    for row, label in zip(logits, labels):
        maximum = max(row)
        exponentials = [math.exp(value - maximum) for value in row]
        total = sum(exponentials)
        probabilities = [value / total for value in exponentials]
        loss += -math.log(probabilities[label])
        gradients.append([(probability - (index == label)) / count for index, probability in enumerate(probabilities)])
    return loss / count, gradients