"""Explainable local routing hints; host agents still make contextual decisions."""

import json
from pathlib import Path
import re

from gncore.skills.library import get_skill
from gncore.skills.unified import unified_manifest

SIGNALS = {
    "neural-networks": ("neural network", "backprop", "gradient check", "xor", "activation", "tensor shape"),
    "deep-learning": ("deep learning", "pytorch", "tensorflow", "checkpoint", "mixed precision", "distributed training", "fine tuning"),
    "computer-vision": ("computer vision", "image", "bounding box", "segmentation", "detection", "augmentation"),
    "natural-language-processing": ("nlp", "tokenization", "tokenizer", "text classification", "padding mask", "token alignment"),
    "mlops": ("mlops", "model serving", "model registry", "model drift", "model promotion", "prediction service"),
    "machine-learning": ("machine learning", "train model", "churn", "forecast", "time series", "classifier", "leakage", "feature engineering"),
    "ai-engineering": ("llm", "rag", "retrieval", "prompt injection", "tool calling", "agent", "mcp"),
    "web-frontend": ("website", "landing page", "frontend", "react", "css", "booking page", "web interface"),
    "web-backend": ("backend", "endpoint", "rest api", "fastapi", "django", "nestjs", "spring boot", "laravel"),
    "code-build": ("refactor", "code review", "failing test", "debug", "discount function", "function bug"),
    "design-ux": ("wireframe", "ux research", "user flow", "design system", "usability", "component specification"),
    "python": ("python package", "python library", "python migration", "wheel", "python performance"),
    "developer-tools": ("cli", "command line", "developer environment", "editor extension", "git workflow"),
    "documentation": ("documentation", "api reference", "tutorial", "migration guide", "technical localization"),
    "testing": ("test strategy", "unit test", "integration test", "end to end", "contract test", "property based", "pytest"),
    "cybersecurity": ("security audit", "threat model", "vulnerability", "authorization bypass", "csrf", "xss", "security review"),
    "cloud-devops-sre": ("kubernetes", "docker", "terraform", "ci pipeline", "devops", "cloud infrastructure", "rollout", "slo"),
    "release-engineering": ("release candidate", "pypi", "release notes", "publish package", "release artifact"),
    "automation": ("automation", "automate", "scheduled job", "resume workflow", "repetitive script"),
    "mobile-development": ("mobile app", "android", "ios", "flutter", "react native", "offline mobile"),
    "game-development": ("game", "unity", "godot", "unreal", "frame rate", "playable"),
    "data-engineering": ("etl", "data pipeline", "csv import", "data lineage", "streaming data", "backfill", "deduplicate events"),
    "data-science": ("statistical", "experiment analysis", "sql analysis", "data visualization", "join fanout", "cohort", "confidence interval"),
    "databases": ("database schema", "postgres", "sqlite", "sql migration", "query plan", "transaction isolation", "database restore"),
    "systems-programming": ("rust", "c++", "ffi", "abi", "memory safety", "use after free", "native component"),
    "embedded-systems": ("firmware", "microcontroller", "embedded", "i2c", "spi", "uart", "interrupt", "timer wraparound"),
    "performance-engineering": ("benchmark", "profiling", "tail latency", "memory allocation", "performance regression", "throughput"),
    "observability": ("observability", "telemetry", "tracing", "trace context", "structured logs", "metrics alert", "sentry"),
    "developer-research": ("technical comparison", "paper reproduction", "research paper", "api compatibility", "technical decision"),
    "distributed-systems": ("distributed system", "idempotency", "message queue", "stale writer", "retry budget", "fencing token", "partial failure"),
}


def context_from_file(path: Path) -> dict:
    if path.stat().st_size > 16384:
        raise ValueError("project context must be a small explicit JSON brief (at most 16 KiB)")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or set(value) - {"stack", "brand", "audience", "preferred_skills"}:
        raise ValueError("project context permits stack, brand, audience and preferred_skills only")
    for name in ("stack", "brand", "audience"):
        if name in value and not isinstance(value[name], str):
            raise ValueError(f"project context {name} must be text")
    preferred = value.get("preferred_skills", [])
    if not isinstance(preferred, list) or not all(isinstance(v, str) for v in preferred):
        raise ValueError("preferred_skills must be a list of skill IDs")
    value["preferred_skills"] = [get_skill(name).metadata.skill_id for name in preferred]
    return value


def route_task(brief: str, *, skill_id: str | None = None, context: dict | None = None) -> dict:
    if not brief.strip():
        raise ValueError("a task brief is required")
    text = re.sub(r"[-_]+", " ", brief.casefold())
    entries = {entry["id"]: entry for entry in unified_manifest()}
    candidates = []
    for name, signals in SIGNALS.items():
        hits = [signal for signal in signals if re.search(r"\b" + re.escape(signal) + r"s?\b", text)]
        score = sum(3 if " " in hit else 2 for hit in hits)
        if score:
            if name in (context or {}).get("preferred_skills", []):
                score += 0.5
            candidates.append({"skill_id": name, "score": score, "matched": hits})
    candidates.sort(key=lambda item: (-item["score"], item["skill_id"]))
    if skill_id:
        selected, status = get_skill(skill_id).metadata.skill_id, "explicit"
    elif not candidates:
        selected, status = None, "needs-context"
    elif len(candidates) > 1 and candidates[0]["score"] - candidates[1]["score"] <= 1:
        selected, status = None, "ambiguous"
    else:
        selected, status = candidates[0]["skill_id"], "suggested"
    workflows = []
    if selected:
        words = set(re.findall(r"[a-z0-9]+", text)) - {"a", "the", "and", "with", "for", "in", "to", "it", "build", "make"}
        scored = []
        for workflow in entries[selected]["workflows"]:
            tokens = set(re.findall(r"[a-z0-9]+", (workflow["id"]+" "+workflow["title"]+" "+workflow["description"]).casefold()))
            scored.append((len(words & tokens), workflow["id"]))
        workflows = [name for score, name in sorted(scored, key=lambda pair: (-pair[0], pair[1]))[:3] if score]
    return {"skill_id": selected, "status": status, "workflows": workflows, "alternatives": candidates[:5],
            "context": context or {}, "limitations": "Deterministic English keyword hints; not an AI execution or quality score. Ambiguous and unsupported requests are left unresolved."}
