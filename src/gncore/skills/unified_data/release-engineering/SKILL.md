---
name: release-engineering
description: "Prepare tested software releases, reproducible artifacts, migrations and approval-ready publication plans."
license: MIT
---

# GNCore Release Engineering

Version: 7.0.0

## Choose the work

Synchronize versions and compatibility promises across code, docs, package metadata and website. Build once and promote verified artifacts; do not rebuild different bytes for each destination.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Versioned wheel/source or platform artifacts, checksums, release notes, migration evidence and a destination-specific publication/rollback plan.

Install from the built artifact with the source checkout excluded. Check contents and public contracts. Distinguish local commits, pushed source, tags, uploaded packages and verified public availability.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Link the accepted source revision, version, CI evidence and exact artifact hashes in one release record. Build once and promote those verified bytes to each destination; do not rebuild separately and assume equivalence. Inspect metadata/contents and install outside the checkout. Keep website/download claims pending until destination availability is verified. Plan partial-publication recovery and registry-specific yank/supersede behavior, retaining explicit preparation-only boundaries until publication is authorized.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- For each intended target artifact, link accepted source/version, CI evidence, metadata and hashes; promote those same verified bytes to destinations covered by authorization.
- Verify clean installs and actual destination availability before updating in-scope claims. Preserve recovery for partial publication; do not overwrite immutable registry files or imply unperformed publication.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `release-readiness` | Check a release candidate against explicit acceptance, compatibility, security, rollback, and communication gates. |
| `release-artifact-integrity` | Artifact integrity and promotion. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
