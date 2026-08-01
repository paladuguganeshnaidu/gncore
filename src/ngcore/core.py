from .loader import load


def think(prompt: str):
    return {
        "skill": load("think"),
        "prompt": prompt,
    }


def research(prompt: str):
    return {
        "skill": load("research"),
        "prompt": prompt,
    }


def plan(prompt: str):
    return {
        "skill": load("plan"),
        "prompt": prompt,
    }


def architect(prompt: str):
    return {
        "skill": load("architect"),
        "prompt": prompt,
    }


def design(prompt: str):
    return {
        "skill": load("design"),
        "prompt": prompt,
    }


def scaffold(prompt: str):
    return {
        "skill": load("scaffold"),
        "prompt": prompt,
    }


def build(prompt: str):
    return {
        "skill": load("build"),
        "prompt": prompt,
    }


def integrate(prompt: str):
    return {
        "skill": load("integrate"),
        "prompt": prompt,
    }


def review(prompt: str):
    return {
        "skill": load("review"),
        "prompt": prompt,
    }


def security(prompt: str):
    return {
        "skill": load("security"),
        "prompt": prompt,
    }


def performance(prompt: str):
    return {
        "skill": load("performance"),
        "prompt": prompt,
    }


def accessibility(prompt: str):
    return {
        "skill": load("accessibility"),
        "prompt": prompt,
    }


def test(prompt: str):
    return {
        "skill": load("test"),
        "prompt": prompt,
    }


def debug(prompt: str):
    return {
        "skill": load("debug"),
        "prompt": prompt,
    }


def refactor(prompt: str):
    return {
        "skill": load("refactor"),
        "prompt": prompt,
    }


def document(prompt: str):
    return {
        "skill": load("document"),
        "prompt": prompt,
    }


def deploy(prompt: str):
    return {
        "skill": load("deploy"),
        "prompt": prompt,
    }


def verify(prompt: str):
    return {
        "skill": load("verify"),
        "prompt": prompt,
    }


def git(prompt: str):
    return {
        "skill": load("git"),
        "prompt": prompt,
    }