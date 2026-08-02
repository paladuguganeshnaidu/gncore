# Developer Guide

GNCore is organized around a small set of modules:

- `src/gncore/cli/` contains the command-line interface.
- `src/gncore/core/` contains managers and typed data models.
- `src/gncore/adapters/` contains the adapter base class and the built-in application adapters.
- `src/gncore/skills/` contains the bundled skill catalog.
- `src/gncore/utilities/` contains atomic file and logging helpers.
- `src/gncore/config.py` handles persistent GNCore configuration and platform paths.

## Adding a new application

Create one adapter class, point it at the target application's config roots, and register it in `builtin_adapters()`. The shared adapter base will take care of the rest.

## Adding a new skill

Add a new `SkillDefinition` to `builtin_skills()`. Provide metadata, prompt text, examples, commands, configuration, dependencies, and permissions.

## Validation strategy

The repository uses tests that exercise the public CLI and adapter registry. Keep any new behavior covered by tests that observe files on disk instead of internal implementation details.
