"""Original MIT-licensed CPU-only XOR/gradient fixture; no framework or downloads."""

import json
import math
import random

INPUTS = [(0.0, 0.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0)]
TARGETS = [0.0, 1.0, 1.0, 0.0]


def initial_parameters(seed=17):
    generator = random.Random(seed)
    # Four hidden units: two weights and a bias each; four output weights/bias.
    return [generator.uniform(-1, 1) for _ in range(17)]


def loss_and_gradient(parameters):
    if len(parameters) != 17 or not all(math.isfinite(p) for p in parameters):
        raise ValueError("expected 17 finite parameters")
    gradient, loss, predictions = [0.0] * 17, 0.0, []
    for (x0, x1), target in zip(INPUTS, TARGETS):
        hidden = [math.tanh(parameters[3*j]*x0 + parameters[3*j+1]*x1 + parameters[3*j+2]) for j in range(4)]
        logit = sum(parameters[12+j]*hidden[j] for j in range(4)) + parameters[16]
        probability = 1/(1+math.exp(-logit)) if logit >= 0 else math.exp(logit)/(1+math.exp(logit))
        predictions.append(probability)
        loss += (max(logit, 0) - logit*target + math.log1p(math.exp(-abs(logit)))) / 4
        delta = (probability-target)/4
        gradient[16] += delta
        for j in range(4):
            gradient[12+j] += delta*hidden[j]
            local = delta*parameters[12+j]*(1-hidden[j]**2)
            gradient[3*j] += local*x0
            gradient[3*j+1] += local*x1
            gradient[3*j+2] += local
    return loss, gradient, predictions


def gradient_error(parameters, epsilon=1e-5):
    analytic = loss_and_gradient(parameters)[1]
    errors = []
    for index in range(len(parameters)):
        plus, minus = parameters.copy(), parameters.copy()
        plus[index] += epsilon
        minus[index] -= epsilon
        numerical = (loss_and_gradient(plus)[0]-loss_and_gradient(minus)[0])/(2*epsilon)
        errors.append(abs(numerical-analytic[index])/max(1e-8, abs(numerical)+abs(analytic[index])))
    return max(errors)


def train(steps=2500, learning_rate=0.7):
    parameters = initial_parameters()
    initial = loss_and_gradient(parameters)[0]
    error = gradient_error(parameters)
    for _ in range(steps):
        loss, gradient, _ = loss_and_gradient(parameters)
        if not math.isfinite(loss):
            raise ValueError("nonfinite training loss")
        parameters = [p-learning_rate*g for p, g in zip(parameters, gradient)]
    loss, _, predictions = loss_and_gradient(parameters)
    return {"fixture": "synthetic-xor", "seed": 17, "steps": steps, "initial_loss": initial,
            "final_loss": loss, "max_relative_gradient_error": error, "predictions": predictions,
            "passed": error < 1e-5 and loss < 0.03 and [int(p >= 0.5) for p in predictions] == [0, 1, 1, 0]}


if __name__ == "__main__":
    result = train()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)
