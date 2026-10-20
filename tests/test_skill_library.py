from __future__ import annotations

from collections import Counter

from gncore.skills.library import builtin_skills, list_categories, list_domains, search_skills, validate_skill_definition


def test_catalog_has_unique_valid_definitions_and_ml_slash_workflows() -> None:
    skills = builtin_skills()
    ids = [skill.metadata.skill_id for skill in skills]
    assert len(skills) >= 100
    assert not [skill_id for skill_id, count in Counter(ids).items() if count > 1]
    assert all(not validate_skill_definition(skill) for skill in skills)
    assert {"train", "preprocess", "clean-data", "evaluate", "improve", "analyze"} <= set(ids)


def test_catalog_domains_and_search_are_discoverable() -> None:
    skills = builtin_skills()
    categories = list_categories(skills=skills)
    assert {"machine-learning", "web-development", "security", "cloud", "quality-assurance"} <= set(categories)
    assert "train" in {skill.metadata.skill_id for skill in search_skills("train", skills=skills)}
    assert "clean-data" in {skill.metadata.skill_id for skill in search_skills("clean data", skills=skills)}


def test_thirty_domain_packs_have_ten_unique_workflows_each() -> None:
    domains = list_domains()
    skills = builtin_skills()
    assert len(domains) == 30
    assert all(len(domain.skill_ids) == 10 for domain in domains)
    domain_skill_ids = [skill_id for domain in domains for skill_id in domain.skill_ids]
    assert len(domain_skill_ids) == len(set(domain_skill_ids)) == 300
    assert set(domain_skill_ids) <= {skill.metadata.skill_id for skill in skills}
    assert {"company-ceo", "company-cfo", "word-draft", "pdf-extract", "ppt-create", "train", "preprocess", "clean-data", "evaluate", "improve", "analyze"} <= set(domain_skill_ids) | {skill.metadata.skill_id for skill in skills}
    assert all(not validate_skill_definition(skill) for skill in skills if skill.metadata.skill_id in set(domain_skill_ids))
    assert all("Execution loop:" in next(skill.prompt for skill in skills if skill.metadata.skill_id == domain.skill_ids[0]) for domain in domains)
