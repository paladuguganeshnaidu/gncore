# API Reference

## Public package entry points

- `gncore.GncoreCli`
- `gncore.main`
- `gncore.get_adapter_registry`
- `gncore.builtin_skills()`
- `gncore.get_skill(skill_id)`
- `gncore.search_skills(query, category=None)`
- `gncore.list_categories()`
- `gncore.list_domains()`
- `gncore.validate_skill_definition(skill)`
- `gncore.SkillManager`
- `gncore.AdapterManager`
- `gncore.ConfigurationManager`
- `gncore.Installer`
- `gncore.Validator`
- `gncore.BackupManager`
- `gncore.RollbackManager`
- `gncore.DiagnosticsManager`

## Core models

- `SkillDefinition`
- `SkillMetadata`
- `SkillExample`
- `SkillCommand`
- `ApplicationDiscovery`
- `ApplicationSummary`
- `InstalledSkill`
- `InstalledApplication`
- `InstallReport`
- `ValidationIssue`
- `ValidationReport`
- `BackupArchive`

## Adapter extension point

Create a subclass of `ApplicationAdapter` with a single `AdapterTemplate`. The base class handles discovery, installation, uninstall, validation, manifest writing, and bundle generation.

## CLI contract

- `activate`: install the selected skills into selected applications
- `deactivate`: remove the managed GNCore bundle
- `update`: reinstall the selected bundle
- `doctor`: report detected applications and validation state
- `list`: show supported apps, skills, domains, categories, or installed selections
- `search`: find skills by ID, name, description, category, or tag
- `export`: package one skill as a ZIP for upload in ChatGPT Skills
- `install`: install a specific skill set
- `uninstall`: remove the bundle from a target application
- `backup`: create an archive of installed bundles
- `restore`: restore from a backup archive
- `validate`: validate the current installation
- `version`: print the package version

## Skill catalog API

```python
from gncore import get_skill, list_categories, list_domains, search_skills

domains = list_domains()  # 30 SkillDomain records; each has ten skill_ids
categories = list_categories()
matches = search_skills("pytorch training", category="machine-learning")
skill = get_skill("train")
```

Catalog functions return immutable tuples or `SkillDefinition` objects. `get_skill` raises `KeyError` when the ID is not present.
