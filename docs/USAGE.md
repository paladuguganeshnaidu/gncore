# GNCore Usage Guide

This guide covers every public GNCore command, the supported flags, and practical command combinations.

## Installation

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
| `gncore list` | List applications, skills, or installed selections |
| `gncore install` | Install one or more named skills into selected applications |
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
- `github-copilot-chat`
- `claude-desktop`
- `claude-code`
- `cursor`
- `windsurf`
- `continue-dev`
- `gemini-cli`
- `openai-codex-cli`

## Skill selection

The bundled skills can be installed individually with `gncore install` or refreshed with `gncore update --skills ...`.

Current built-in skills:

- `requirements`
- `architecture`
- `implementation`
- `review`
- `testing`
- `security`
- `documentation`
- `release`

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
