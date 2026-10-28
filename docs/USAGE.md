# Usage

## Install a category in the project

```bash
gncore export --specific web-frontend
gncore export --skills web-backend code-build
```

Then ask a compatible host agent to use the category:

```text
$web-frontend Build a clinic booking site with clear service and appointment flows.
$web-frontend Build a premium hotel website with no animation.
$web-backend Add an authenticated booking API to this repository.
$code-build Fix the failing booking tests and verify the regression.
```

If a theme is omitted, the frontend skill chooses a coherent starting direction from the audience, task, content, and constraints. If a theme is supplied, it honors that choice. For changes to an existing product, it preserves the current design language unless a redesign is requested.

Invocation syntax and automatic discovery depend on the host agent. The export location follows the `.agents/skills/<id>/SKILL.md` convention; the host must support and enable skills. GNCore itself does not start an AI session.

## Inspect before use

```bash
gncore list skills
gncore list workflows
gncore show finance-accounting
gncore search "contract review"
```

One category file contains its workflow selection and focused procedures. Read substantial references only for the relevant task. Supporting tools, browser runtimes, connectors, and credentials are not installed by exporting a skill.

## Full and portable exports

```bash
gncore export --all
gncore export --all --directory ./custom-skills
gncore export --all --output gncore-categories.zip
```

Use GNCore export when exact resource preservation matters. Some external skill installers omit files named `metadata.json`; GNCore preserves every declared resource, including provenance and notices.

## Existing projects

Legacy IDs such as `train`, `web-front-minimalism`, and `web-backend-fastapi` remain CLI/API aliases. Exporting them writes their canonical category folders. Existing old folders in other projects are not deleted automatically. Back up custom edits before retiring older installations; see [Migration](../MIGRATION.md).
