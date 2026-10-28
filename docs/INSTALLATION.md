# Recoverable project installations

Directory exports and `scripts/install_categories.py` share a staged installer. It preflights every requested category before changing the installation, checks ownership through file digests, copies the existing tree, verifies staged payloads, and switches directories while retaining a backup. Source scripts remain inert.

## Preview and install

```bash
gncore export --all --dry-run
gncore export --all
gncore verify
```

Use `--directory ./custom-skills` on all three commands for a different destination. A dry run creates no destination, backup, lock, or inventory. Any unmanaged collision or modified managed file aborts the whole install. Moving those conflicting folders to a separate location after review lets an explicit fresh install proceed.

The `.gncore-install.json` inventory records a version and SHA-256 digests for each installed category's files. An older export without an inventory is adopted only if every expected file matches this package byte for byte. A familiar name, or the word `GNCore`, is not proof of ownership. Additional files are preserved as unmanaged files. Updates remove only obsolete inventory-listed files whose original digests still match.

This inventory detects change relative to an installation; it is not a signed publisher-authenticity claim. Modifying both the inventory and a file cannot establish trust in an unknown package.

## Legacy migration

```bash
python scripts/install_categories.py --migrate-managed --dry-run
python scripts/install_categories.py --migrate-managed
```

Only exact known legacy exports are retired. Older versions with different bytes, extra files, or custom edits stay in place and appear under `preserved_legacy`. All collisions are checked before migration. GNCore does not rewrite the separate third-party `skills-lock.json`; its own inventory tracks its writes.

## Verify and recover

`gncore verify` is read-only. It reports missing, modified, and unmanaged files. Missing or modified tracked content returns exit `1`; unknown extra files are reported without making an intact managed installation fail. Exit `2` reports invalid state or an operational error.

Transactions live in a sibling directory named `.gncore-<destination-name>-transactions/<transaction-id>/`. The printed journal path identifies the original-directory backup, staged tree, and transaction status. After a successful update the backup remains available for manual comparison; GNCore does not prune it automatically. Provision enough disk space for a staged copy and retained backups.

An ordinary failed stage or switch restores the original directory automatically. If a process stops during the switch, stop the original writer, then use the reported journal:

```bash
gncore recover --directory .agents/skills --journal .agents/.gncore-skills-transactions/TRANSACTION_ID/journal.json
```

Recovery restores the previous tree and retains a switched new tree as `failed-install`. If the journal already records a successful commit and only lock cleanup was interrupted, recovery verifies that installation and clears its stale writer lock. Other unfinished transactions prevent new writes until recovered. Do not recover a transaction while its original process is still running.

A stop before the journal is written cannot have switched the original tree; inspect that transaction and remove its stale `.gncore-<destination-name>.lock` only after confirming the writer has stopped. Recovery deliberately refuses a missing original backup after a switch instead of claiming restoration succeeded. Linked destinations and symlink/junction resources are unsupported. The installer protects its own cooperating writers and checks for edits while staging; it does not provide filesystem-wide locking or a power-loss durability guarantee.

ZIP export retains the portable category-folder format. Extracted ZIPs do not have an installation inventory until adopted through a directory export with matching package content.
