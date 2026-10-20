# GNCore Usage Guide

This guide covers every public GNCore command, the supported flags, and practical command combinations.

## Installation

To use the current checkout while developing GNCore:

```bash
python -m pip install -e .
```

After a release containing these changes is published, users can install the packaged CLI with:

```bash
pip install gncore
```

Check the installed version:

```bash
gncore version
```

## Command overview

| Command | Purpose |
| --- | --- |
| `gncore activate` | Install GNCore skills into selected applications |
| `gncore deactivate` | Remove the managed GNCore bundle from selected applications |
| `gncore update` | Reinstall the selected bundle and refresh managed files |
| `gncore doctor` | Check detected applications and installation health |
| `gncore list` | List applications, skills, domains, categories, or installed selections |
| `gncore install` | Install one or more named skills into selected applications |
| `gncore export` | Package skills as a ZIP for upload to ChatGPT Skills |
| `gncore search` | Search skills by name, description, category, or tag |
| `gncore uninstall` | Remove GNCore from selected applications |
| `gncore backup` | Create a backup archive of installed GNCore bundles |
| `gncore restore` | Restore GNCore bundles from a backup archive |
| `gncore validate` | Validate one or more installed application bundles |
| `gncore version` | Print the installed GNCore version |

## Selection flags

Most install-related commands accept the same application-selection flags:

- `--apps <key ...>` selects explicit application keys.
- `--all` targets every supported application.
- When neither is provided, GNCore detects installed applications and offers an interactive selection.

The supported application keys are:

- `vscode-chat`
- `vscode-codex`
- `vscode-claude-code`
- `antigravity`
- `github-copilot-chat`
- `claude-desktop`
- `claude-code`
- `cursor`
- `windsurf`
- `continue-dev`
- `gemini-cli`
- `openai-codex-cli`

## Skill selection

The bundled skills can be installed individually with `gncore install` or refreshed with `gncore update --skills ...`. Use `gncore list domains`, `gncore list skills`, and `gncore list categories` to browse the catalog. GNCore 4.0.0 includes 30 domain packs with 10 focused workflows each (300 domain workflows), alongside its existing specialist skills.

Domain packs (each contains 10 slash-invoked workflows):

| Area | Domain packs |
| --- | --- |
| Company and business | Company leadership (CEO, CFO, COO, CTO, CPO, CMO, CHRO, CISO, board, executive team), business strategy, product management, project/program management, business operations, sales/revenue, marketing/growth, finance/accounting, people/HR, customer success/support, legal/compliance, procurement/vendor, entrepreneurship |
| Technology | Software engineering, data analytics, AI/machine learning, cybersecurity, cloud/DevOps/SRE, quality engineering, design/UX |
| Documents and presentations | Word documents, PDF documents, PowerPoint presentations, spreadsheets |
| Specialist operations | Research/market intelligence, education/learning, healthcare operations, e-commerce/retail, business communications, supply chain/logistics |

Find a workflow by intent, then install its exact ID:

```bash
gncore list domains
gncore search "CEO strategy"
gncore search "clean data"
gncore install company-ceo train preprocess clean-data evaluate improve analyze word-draft pdf-extract ppt-create --apps vscode-codex --scope workspace
```

For the complete catalog of all 403 skill IDs, slash names, use cases, and one-skill install examples, see [ALL_SKILLS.md](ALL_SKILLS.md).

The shared skill contract guides the assistant through inspect → plan → implement → test → fix → retest → report. It requires evidence for checks, preserves unrelated work, reruns regressions after fixes, and stops when acceptance checks pass or a genuine blocker remains. For Word/PDF/PowerPoint artifacts, skills ask the assistant to reopen and inspect final saved output where tools permit; review quality depends on the target assistant's available capabilities.

### Search and install native agent skills

Search the catalog, then install selected skills into the current project:

```bash
gncore search model training
gncore search pytorch --category machine-learning
gncore install train preprocess clean-data evaluate improve analyze --apps antigravity --scope workspace
gncore install web-development machine-learning --apps vscode-chat --scope workspace
gncore install train evaluate --apps vscode-codex --scope workspace
gncore install web-security --apps vscode-claude-code --scope workspace
```

VS Code Copilot workspace skills are written under `.github/skills/<skill-id>/SKILL.md`; VS Code Codex and Antigravity use `.agents/skills/<skill-id>/SKILL.md`; VS Code Claude and Claude Code use `.claude/skills/<skill-id>/SKILL.md`. Codex CLI uses `.agents/skills`, and Gemini CLI uses `.gemini/skills`. These native skill folders expose slash invocation such as `/train` when supported by the selected agent harness.

For user-wide installation across workspaces:

```bash
gncore install web-development --apps vscode-chat --scope user
gncore install train --apps vscode-codex --scope user
gncore install web-security --apps claude-code --scope user
```

GNCore skips an existing skill folder unless it has GNCore's ownership marker. Uninstall removes only GNCore-managed skill folders. Skills provide instructions to the assistant; they do not run independently or authorize broad unrelated changes.

ChatGPT Skills are managed in the ChatGPT workspace UI rather than synchronized from a local skill folder. Export a ZIP and upload it through Skills > Create > Upload from your computer:

```bash
gncore export --app chatgpt --skills train --output chatgpt-train.zip
```

## Each command

### `gncore activate`

Installs the default bundled skills into the selected applications, writes the managed bundle, and validates the installation.

Examples:

```bash
gncore activate
gncore activate --all
gncore activate --apps cursor
gncore activate --apps cursor windsurf
gncore activate --apps claude-desktop --skills requirements architecture
```

### `gncore deactivate`

Removes the managed GNCore bundle from the selected applications.

Examples:

```bash
gncore deactivate --apps cursor
gncore deactivate --all
```

### `gncore update`

Reinstalls the selected bundle. This is useful after a package upgrade or after refreshing the built-in skill set.

Examples:

```bash
gncore update
gncore update --all
gncore update --apps cursor --skills requirements review testing
```

### `gncore doctor`

Reports which supported applications are detected, whether their config roots are writable, and whether the current installation validates.

Examples:

```bash
gncore doctor
```

### `gncore list`

Lists supported applications, bundled skills, or the last saved installed selection.

Examples:

```bash
gncore list apps
gncore list skills
gncore list installed
```

### `gncore install`

Installs one or more named skills into the selected applications.

Examples:

```bash
gncore install requirements --apps cursor
gncore install requirements architecture --apps cursor windsurf
gncore install review testing security --all
```

### `gncore export`

Packages one selected skill into a ZIP compatible with ChatGPT's skill upload flow. ChatGPT expects one skill bundle per ZIP. The command does not log into or modify a ChatGPT workspace.

```bash
gncore export --app chatgpt --skills train --output chatgpt-train.zip
```

### `gncore uninstall`

Removes GNCore from the selected applications.

Examples:

```bash
gncore uninstall --apps cursor
gncore uninstall --all
```

### `gncore backup`

Creates a zip archive that captures the managed bundle state for detected applications.

Examples:

```bash
gncore backup
gncore backup --output gncore-backup.zip
```

### `gncore restore`

Restores a backup archive into the recorded application locations.

Examples:

```bash
gncore restore gncore-backup.zip
```

### `gncore validate`

Checks that the manifest and recorded files still exist for the selected applications.

Examples:

```bash
gncore validate
gncore validate --apps cursor
gncore validate --all
```

### `gncore version`

Prints the installed package version.

Examples:

```bash
gncore version
```

## Common command combinations

### Fresh install

```bash
pip install gncore
gncore list apps
gncore activate
gncore validate
```

### Install into one editor only

```bash
gncore activate --apps cursor
gncore validate --apps cursor
```

### Install into multiple tools

```bash
gncore activate --apps cursor windsurf claude-desktop
gncore validate --apps cursor windsurf claude-desktop
```

### Install a smaller skill set

```bash
gncore install requirements architecture --apps cursor
gncore update --apps cursor --skills requirements architecture
```

### Refresh and verify

```bash
gncore update --all
gncore doctor
gncore validate --all
```

### Backup and rollback

```bash
gncore backup --output gncore-backup.zip
gncore deactivate --apps cursor
gncore restore gncore-backup.zip
```

### Inspect installed state

```bash
gncore list installed
gncore list skills
```

## Notes

- If you run a command without `--apps` or `--all`, GNCore detects available applications and prompts for a selection when interactive input is available.
- `gncore install` and `gncore update --skills ...` are the right commands when you want only part of the bundled skill set.
- `gncore deactivate` and `gncore uninstall` both remove the managed GNCore bundle from target applications.
