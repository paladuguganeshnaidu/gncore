# API Reference

## Public package entry points

- `gncore.GncoreCli`
- `gncore.main`
- `gncore.get_adapter_registry`
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
- `list`: show supported apps, skills, or installed selections
- `install`: install a specific skill set
- `uninstall`: remove the bundle from a target application
- `backup`: create an archive of installed bundles
- `restore`: restore from a backup archive
- `validate`: validate the current installation
- `version`: print the package version
