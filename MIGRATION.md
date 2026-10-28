# Migration to GNCore 6

GNCore 6 replaces 553 separately listed workflow skills with **60 adaptive category entrypoints**. All 553 workflow procedures remain in their category modules. The 30 professional domain packs still contain ten workflows each.

## Primary names

| Earlier IDs | Primary category |
| --- | --- |
| `web-front`, `web-front-minimalism`, `web-front-react`, other frontend modes | `web-frontend` |
| `web-backend-fastapi`, `web-backend-codequality`, other backend modes | `web-backend` |
| `code-quality`, `code-debugging`, other general coding modes | `code-build` |
| `train`, `evaluate`, other ML workflows | `machine-learning` |
| `word-draft`, `word-edit`, other Word workflows | `word-documents` |
| `company-ceo`, `company-cfo`, other leadership workflows | `company-leadership` |

Use `gncore list workflows` for the complete mapping. Existing CLI/API lookups resolve aliases to the canonical category, so exporting multiple modes from one category creates one folder.

A new primary category name takes precedence over an older generic workflow with the same name. For example, `testing`, `security`, and `documentation` now address those full specialist categories. Their former general workflow procedures also remain inside `general`.

## Project installations

Back up customized old skill folders, then install the desired category entrypoints with `gncore export`. Old folders in other projects are not deleted automatically. Fresh exports use `.agents/skills/<category>/SKILL.md` and include supporting resources and notices.

Only primary category entrypoints are exposed as `SKILL.md` in the source distribution. Retired source entrypoints and nested source skills are reference guides, preventing duplicate automatic discovery.

## API changes

- `builtin_skills()` returns 60 primary definitions.
- `list_workflows()` exposes the 553 workflow metadata records.
- Each professional `SkillDomain` contains one canonical `skill_ids` entry and ten `workflow_ids`.
- Metadata includes license information; bundled material is not uniformly MIT-licensed.
