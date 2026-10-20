# Migration to GNCore 5.0

GNCore 5.0 is a breaking simplification to a skill catalog and portable export tool.

Removed APIs and commands include application adapters, detection, `activate`, `deactivate`, `install`, `uninstall`, `update`, `doctor`, `validate`, `backup`, and `restore`. The remaining CLI commands are `list`, `search`, `show`, `export`, and `version`.

Update code to use the skill catalog API:

```python
from gncore import get_skill, list_domains, search_skills

skill = get_skill("train")
matches = search_skills("training evaluation")
domains = list_domains()
```

Use `gncore show <skill-id>` to print one portable `SKILL.md`, or `gncore export --skills <id>... --output skills.zip` to create a portable archive. GNCore 5.0 does not read or modify files created by older application-management releases. Manage any old installation files using the host application's normal documentation and controls.
