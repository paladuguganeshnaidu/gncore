from collections import Counter
import hashlib

import pytest

from gncore import builtin_skills, get_skill, list_categories, list_domains, list_workflows, search_skills, validate_skill_definition
from gncore.skills.library import migration_manifest
from gncore.skills.unified import unified_manifest, workflow_aliases


def test_active_catalog_is_developer_focused_and_each_category_is_discoverable():
    primary = builtin_skills()
    assert len(primary) == len(list_categories()) == 30
    assert len({s.metadata.skill_id for s in primary}) == 30
    assert all(not validate_skill_definition(s) for s in primary)
    assert {s.metadata.version for s in primary} == {"7.0.0rc1"}
    ids = {s.metadata.skill_id for s in primary}
    assert {"neural-networks", "deep-learning", "mlops", "embedded-systems", "systems-programming"} <= ids
    assert not {"finance-accounting", "word-documents", "company-leadership", "sales-revenue"} & ids
    assert len(list_workflows()) == 374
    assert all(count == 1 for count in Counter(w.skill_id for w in list_workflows()).values())


def test_every_phase_one_workflow_has_an_explicit_migration_outcome_and_exact_procedure_accounting():
    ledger = migration_manifest()["workflows"]
    assert len(ledger) == len({w["id"] for w in ledger}) == 553
    assert Counter(w["status"] for w in ledger) == {"preserved": 203, "rewritten": 116, "retired": 234}
    actual = {w["id"]: (entry["id"], w) for entry in unified_manifest() for w in entry["workflows"]}
    for old in ledger:
        if old["target"] is None:
            assert old["id"] not in actual
            continue
        target, workflow = actual[old["id"]]
        assert target == old["target"]
        digest = hashlib.sha256(workflow["procedure"].encode()).hexdigest()
        assert digest == old["procedure_sha256"]
        assert (digest == old["previous_procedure_sha256"]) == (old["status"] == "preserved")
    assert sum(w.get("revision") == "new original procedure" for e in unified_manifest() for w in e["workflows"]) == 55


def test_developer_domains_partition_categories_without_business_packs():
    domains = list_domains()
    assert len(domains) == 6
    assert sorted(i for d in domains for i in d.skill_ids) == sorted(s.metadata.skill_id for s in builtin_skills())
    assert sum(len(d.workflow_ids) for d in domains) == 374


def test_aliases_preserve_technical_capabilities_and_removed_business_ids_fail_clearly():
    for old_id, target in workflow_aliases().items():
        assert get_skill(old_id).metadata.skill_id == target
    assert get_skill("ui-minimalism").metadata.skill_id == "web-frontend"
    assert get_skill("backend-api").metadata.skill_id == "web-backend"
    assert get_skill("nlp").metadata.skill_id == "natural-language-processing"
    assert get_skill("security").metadata.skill_id == "cybersecurity"
    with pytest.raises(KeyError, match="retired"):
        get_skill("finance-budget")


def test_search_and_workflow_filters_follow_the_new_categories():
    assert "machine-learning" in {s.metadata.skill_id for s in search_skills("train model")}
    assert "neural-networks" in {s.metadata.skill_id for s in search_skills("neural network")}
    assert "web-frontend" in {s.metadata.skill_id for s in search_skills("minimalism")}
    assert len(list_workflows("web-frontend")) == 40
    assert len(list_workflows("web-backend")) == 60
    assert len(list_workflows("code-build")) == 85


def test_every_merged_procedure_is_present_and_distinct():
    procedures = []
    for entry in unified_manifest():
        prompt = get_skill(entry["id"]).prompt
        for workflow in entry["workflows"]:
            assert workflow["id"] in prompt
            assert workflow["procedure"].strip() in prompt
            procedures.append(workflow["procedure"].strip())
    assert len(procedures) == len(set(procedures))
