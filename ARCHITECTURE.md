# Architecture

GNCore uses clean architecture boundaries:

- CLI
- Core services
- Adapters
- Skills
- Installer and backup services
- Validators
- Utilities
- Configuration

## Core flow

```mermaid
flowchart TD
    A[gncore activate] --> B[Detect installed applications]
    B --> C[Interactive selection]
    C --> D[Select skills]
    D --> E[Adapter-specific install]
    E --> F[Write prompt, command, MCP, settings bundles]
    F --> G[Validate installation]
    G --> H[Print success report]
```

## Layer responsibilities

The CLI parses user input and dispatches to managers. It never writes application files directly.

The core layer coordinates skill selection, adapter discovery, installation, rollback, backup, diagnostics, and version reporting.

The adapter layer contains one class per supported application. Each adapter resolves its own config root, discovers executables or config roots, and serializes skills in the format its application can load. Generic adapters write GNCore-managed bundles. Native skill adapters write `SKILL.md` folders to the target's documented workspace or user skill directory.

The skill layer contains the internal skill catalog. Skills are versioned, independently installable, and serializable into multiple output formats.

The utilities layer handles JSON and atomic file writing so the installer never leaves partial files behind.

## Adapter contract

Every adapter must implement the same behavior:

- detect the application
- resolve a writable config root
- install a selected skill set
- uninstall the managed bundle
- validate the installation

That keeps the application surface extensible without duplicating installer logic.

## Bundle shape

GNCore writes a managed `gncore/` bundle under each target application's config directory. The bundle includes:

- `manifest.json`
- `bundle.json`
- `settings.json`
- `mcp.json`
- `skills/<skill-id>/...`
- `prompts/<skill-id>.md`
- `commands/<skill-id>/<command>.md`

The generic bundle manifest makes update, backup, restore, and validation deterministic. Native skill adapters keep a separate GNCore manifest beside their target skill directory and add an ownership marker to each managed skill. They skip unmarked existing skill folders and remove only marked folders during uninstall.

## Native skills

Native skills use a directory named after the skill ID with a `SKILL.md` file containing YAML frontmatter (`name` and `description`) followed by the instructions. VS Code Copilot workspace skills use `.github/skills/`; VS Code Codex and Antigravity use `.agents/skills/`; VS Code Claude and Claude Code use `.claude/skills/`; Gemini CLI uses `.gemini/skills/`. User scope installs into each harness's supported home-directory location. Shared target directories track multiple GNCore owners so uninstalling one harness preserves skills still installed for another.

## Validation and rollback

Validation checks that the manifest exists and that every recorded skill file is still present. Backup writes a zip archive with a backup manifest, and restore replays the archive back into the recorded application roots.
