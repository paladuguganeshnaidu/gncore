---
name: release-engineering
description: "Prepare tested software releases, reproducible artifacts, migrations and approval-ready publication plans."
license: MIT
---

# GNCore Release Engineering

Version: 7.0.0rc1

## Choose the work

Synchronize versions and compatibility promises across code, docs, package metadata and website. Build once and promote verified artifacts; do not rebuild different bytes for each destination.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

Versioned wheel/source or platform artifacts, checksums, release notes, migration evidence and a destination-specific publication/rollback plan.

Install from the built artifact with the source checkout excluded. Check contents and public contracts. Distinguish local commits, pushed source, tags, uploaded packages and verified public availability.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Link the accepted source revision, version, CI evidence and exact artifact hashes in one release record. Build once and promote those verified bytes to each destination; do not rebuild separately and assume equivalence. Inspect metadata/contents and install outside the checkout. Keep website/download claims pending until destination availability is verified. Plan partial-publication recovery and registry-specific yank/supersede behavior, retaining explicit preparation-only boundaries until publication is authorized.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `release-readiness` | Check a release candidate against explicit acceptance, compatibility, security, rollback, and communication gates. |
| `release-artifact-integrity` | Artifact integrity and promotion. |

## Focused procedures

### Release Readiness Review (`release-readiness`)

Inspect the release scope, version, changelog, artifacts, compatibility matrix, known issues, and rollback plan. Verify required checks and distinguish passed from skipped. Check migrations and external dependencies for rollout sequencing. Do not publish or deploy without authorization. End with a go/no-go recommendation tied to evidence and unresolved risks.

### Artifact integrity and promotion (`release-artifact-integrity`)

Build wheel/source/platform artifacts from a clean accepted tree, record checksums and install them outside the checkout. Verify declared resources, executable entrypoints and version agreement. Promote these bytes only after destination-specific publication approval.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
