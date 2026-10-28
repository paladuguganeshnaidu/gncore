from __future__ import annotations

import gncore
from gncore import SkillDefinition, SkillDomain, get_skill, list_domains


def test_public_api_is_skill_catalog_only() -> None:
    assert gncore.__version__ == "6.0.0"
    assert isinstance(get_skill("train"), SkillDefinition)
    assert all(isinstance(domain, SkillDomain) for domain in list_domains())
    forbidden_exports = {
        "AdapterManager", "ApplicationAdapter", "Installer", "BackupManager",
        "RollbackManager", "DiagnosticsManager", "GncoreConfigManager",
    }
    assert forbidden_exports.isdisjoint(gncore.__all__)
