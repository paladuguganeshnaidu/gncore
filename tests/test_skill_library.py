from collections import Counter

from gncore import builtin_skills, get_skill, list_categories, list_domains, list_workflows, search_skills, validate_skill_definition
from gncore.skills.library import legacy_skills
from gncore.skills.unified import unified_manifest, workflow_aliases


def test_one_primary_skill_per_category_preserves_every_existing_workflow():
    primary = builtin_skills()
    assert len(primary) == len(list_categories()) == 60
    assert len({s.metadata.skill_id for s in primary}) == 60
    assert all(not validate_skill_definition(s) for s in primary)
    assert {s.metadata.version for s in primary} == {"6.0.0"}
    old_ids = {s.metadata.skill_id for s in legacy_skills()}
    workflows = list_workflows()
    assert len(workflows) == len(old_ids) == 553
    assert {w.skill_id for w in workflows} == old_ids
    assert not [i for i, n in Counter(w.skill_id for w in workflows).items() if n != 1]
    assert {"web-frontend", "web-backend", "code-build", "word-documents", "finance-accounting"} <= {s.metadata.skill_id for s in primary}
    for old_id, target in workflow_aliases().items():
        assert get_skill(old_id).metadata.skill_id == target
    assert get_skill("frontend-engineering").metadata.skill_id == "web-frontend"
    assert get_skill("backend-api").metadata.skill_id == "web-backend"


def test_thirty_professional_domains_keep_their_ten_workflows_in_one_entrypoint():
    domains = list_domains()
    assert len(domains) == 30
    assert all(len(d.skill_ids) == 1 and len(d.workflow_ids) == 10 for d in domains)
    ids = [i for d in domains for i in d.workflow_ids]
    assert len(ids) == len(set(ids)) == 300
    for domain in domains:
        entrypoint = get_skill(domain.skill_ids[0])
        assert all(get_skill(i) == entrypoint for i in domain.workflow_ids)


def test_search_finds_category_from_legacy_workflow_terms():
    assert "machine-learning" in {s.metadata.skill_id for s in search_skills("train model")}
    assert "data-science" in {s.metadata.skill_id for s in search_skills("clean data")}
    assert "web-frontend" in {s.metadata.skill_id for s in search_skills("minimalism")}
    assert "web-backend" in {s.metadata.skill_id for s in search_skills("fastapi")}
    assert len(list_workflows("web-frontend")) == 40
    assert len(list_workflows("backend-engineering")) == 61
    assert len(list_workflows("code-engineering")) == 66


def test_single_file_entrypoints_contain_all_declared_workflow_procedures():
    for entry in unified_manifest():
        prompt = get_skill(entry["id"]).prompt
        for workflow in entry["workflows"]:
            assert workflow["id"] in prompt
            assert workflow["procedure"].strip() in prompt
