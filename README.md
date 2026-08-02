# GNCore

GNCore is a universal AI Skill Installer for coding assistants.

Install it once:

```bash
pip install gncore
```

Then activate the skills you want:

```bash
gncore activate
```

GNCore detects supported applications, installs the bundled skills into the right adapter-specific locations, writes prompt and command bundles, configures MCP where supported, verifies the installation, and stores a manifest so updates, validation, backup, and rollback are safe.

## Supported applications

- VS Code Chat
- GitHub Copilot Chat
- Claude Desktop
- Claude Code
- Cursor
- Windsurf
- Continue.dev
- Gemini CLI
- OpenAI Codex CLI

## Commands

```bash
gncore activate
gncore deactivate
gncore update
gncore doctor
gncore list
gncore install
gncore uninstall
gncore backup
gncore restore
gncore validate
gncore version
```

## Quick start

```bash
pip install gncore
gncore list apps
gncore activate --apps cursor
gncore validate --apps cursor
gncore backup --output gncore-backup.zip
```

## What GNCore installs

Each bundled skill includes:

- metadata
- description
- system prompt
- examples
- commands
- configuration
- version
- dependencies
- permissions

GNCore serializes those skills into application-compatible bundles through adapters. Every adapter has the same core contract, so adding a new application only requires a new adapter class.

## Documentation

- [Usage Guide](docs/USAGE.md)
- [Architecture](ARCHITECTURE.md)
- [Developer Guide](docs/DEVELOPER.md)
- [API Reference](docs/API.md)
- [Contributing](CONTRIBUTING.md)
- [Release Workflow](docs/RELEASE.md)
- [Security](SECURITY.md)
