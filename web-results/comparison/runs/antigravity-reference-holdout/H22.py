import math

def categorical_loss_grad(logits, labels):
    if not isinstance(logits, list) or len(logits) == 0:
        raise ValueError("logits must be a nonempty list")
    if not isinstance(labels, list) or len(labels) != len(logits):
        raise ValueError("labels must be a list matching logits length")
    
    N = len(logits)
    C = None
    for row in logits:
        if not isinstance(row, list) or len(row) < 2:
            raise ValueError("each logits row must be a list with at least 2 classes")
        if C is None:
            C = len(row)
        elif len(row) != C:
            raise ValueError("logits must be rectangular")
        for val in row:
            if isinstance(val, bool) or not isinstance(val, (int, float)):
                raise ValueError("logits values must be numbers, not bool")
            if math.isnan(val) or math.isinf(val):
                raise ValueError("logits values must be finite")
                
    for y in labels:
        if isinstance(y, bool) or not isinstance(y, int):
            raise ValueError("labels must be integers, not bool")
        if y < 0 or y >= C:
            raise ValueError("label index out of range")
            
    total_loss = 0.0
    grad = []
    
    for i in range(N):
        row = logits[i]
        y = labels[i]
        max_val = max(row)
        exps = [math.exp(v - max_val) for v in row]
        sum_exps = sum(exps)
        probs = [e / sum_exps for e in exps]
        
        loss_i = -(row[y] - max_val) + math.log(sum_exps)
        total_loss += loss_i
        
        row_grad = [(p - (1.0 if j == y else 0.0)) / N for j, p in enumerate(probs)]
        grad.append(row_grad)
        
    mean_loss = total_loss / N
    return mean_loss, grad