# API and CLI

```python
from gncore import builtin_skills, get_skill, list_categories, list_domains, list_workflows, search_skills
```

`builtin_skills()` returns 30 developer definitions. `list_workflows(category=None)` returns 374 workflow metadata records, with canonical category filters. `list_domains()` returns six developer groups partitioning all category IDs. This replaces the professional-pack shape from version 6.

`get_skill(id)` prefers canonical categories, then historical technical category aliases, then active workflow aliases. Removed business IDs raise `KeyError` with a retirement explanation. Primary/category aliases can override an older generic workflow name; see [migration](../MIGRATION.md).

```text
gncore list [skills|categories|domains|workflows]
gncore search <terms> [--category <id>]
gncore show <id>
gncore route <brief> [--skill <id>] [--context <project.json>]
gncore plan <brief> [--theme <theme>] [--existing-theme <theme>]
gncore export (--skills <ids> | --specific <id> | --all) [--directory <path> | --output <archive.zip>] [--dry-run] [--prune-retired]
gncore verify [--directory <path>]
gncore recover [--directory <path>] --journal <journal.json>
gncore audit
gncore evaluate (--validate | --list | --case <id>) [--corpus <file>] [--response <record.json> --artifacts <directory>]
gncore version
```

`route` is a deterministic English hint with matched terms and alternatives. It abstains when unsupported or ambiguous. Explicit `--skill` wins. Context reads only a supplied small JSON file with `stack`, `brand`, `audience` and `preferred_skills`; it does not scan the project or collect secrets.

The frontend helper honors explicit themes, existing brand and inferred defaults in that order; negative constraints filter every path. Contradictions return a clear error. It supports bounded patterns and common spellings, including `britalisim`, rather than promising unrestricted natural-language interpretation.

Directory export checks source digests before staging. `--prune-retired` requires `--all` and a directory destination. It removes only unchanged tracked old folders and retains a full backup; custom/untracked folders are reported and preserved. `verify` is read-only; exit 1 indicates missing/modified tracked files, exit 2 invalid input/operational errors.

`audit` checks all merged procedures, migration hashes, resource hashes, entrypoint links and Python helper syntax. It does not execute imported helpers or grade arbitrary AI outputs. Evaluation exit 0 means structural checks pass, with semantic review still pending.
