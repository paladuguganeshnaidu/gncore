# Usage

Install from this prepared checkout, inspect a skill, and export its standard project folder:

```bash
python -m pip install .
gncore route "Check neural network gradients"
gncore show neural-networks
gncore export --specific neural-networks
gncore verify
```

A compatible host agent can use `$neural-networks` with the task and project constraints. Automatic discovery/invocation depends on the host. GNCore does not install ML frameworks, launch a model or override permissions.

```bash
gncore search "Postgres"
gncore list domains
gncore list workflows
gncore export --skills web-frontend web-backend
gncore export --all --output gncore-developer-skills.zip
gncore audit
gncore evaluate --validate
```

To replace an inventory-managed old catalog, preview `gncore export --all --prune-retired --dry-run` first. Modified managed active files stop the update; modified/unmanaged old categories are preserved and reported. See [migration](../MIGRATION.md) and [installation/recovery](INSTALLATION.md).

The phase-two candidate is not publicly installable from PyPI until approved publication. The future explicit prerelease command is `python -m pip install --pre gncore==7.0.0rc1`.
