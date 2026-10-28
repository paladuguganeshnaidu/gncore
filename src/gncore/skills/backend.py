"""Backend and language-independent coding workflows and legacy lookups."""

from gncore.skills.bundles import bundle_manifest, bundle_resources, bundle_skills

LEGACY_BACKEND_IDS = {
    "backend-api": "web-backend-patterns",
    "api-design": "web-backend-api-design",
    "django-engineering": "web-backend-django",
    "fastapi-engineering": "web-backend-fastapi",
    "python-debugging": "code-debugging",
    "docker": "web-backend-docker",
    "git-workflow": "code-git-workflow",
    "security-review": "code-security-review",
    "web-application-security": "web-backend-security",
    "e2e-testing": "code-e2e-testing",
    "observability": "web-backend-observability",
}


def backend_manifest() -> tuple[dict, ...]:
    return bundle_manifest("backend_data")


def backend_skills():
    return bundle_skills("backend_data", "code-engineering")


def backend_resources(skill_id: str) -> dict[str, bytes]:
    return bundle_resources("backend_data", skill_id)
