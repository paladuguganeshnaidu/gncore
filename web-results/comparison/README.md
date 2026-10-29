# GNCore comparison evidence

Start with EXECUTIVE-REPORT.pdf for a plain-language explanation and four landscape scorecards. TECHNICAL-REPORT.pdf describes the experimental design, sources, scoring, failures and limits. The same reports are available as Markdown.

The charts show measured task checks, not universal efficiency or security. All30 categories are represented; missing rendered UI checks stay gray. The initial revised trial and three-entrypoint adaptive follow-up are distinct conditions.

## Evidence map

| File or folder | Meaning |
| --- | --- |
| charts/ | Four Matplotlib landscape sheets, each with six metric panels and a30-category heatmap; PNG, SVG and PDF |
| category-scores.csv | Per-category applicable manual check counts; incomplete cases have no percentage |
| failed-checks.csv | Every failed frozen criterion and its evidence |
| review-results.json | Compiled frozen-criterion decisions plus linked execution/browser logs |
| source-snapshots.json | Thirty references, fourteen pinned repositories, content hashes and source-specific license metadata |
| runs/ | Copied public IDE answers, normalized JSON, generated code and actual fixture/browser logs |
| initial-candidate/ | Fingerprints and three entrypoints from the first revised trial |
| final-followup-input.json | Final three-entrypoint pack identity; adaptive known-task evaluation |
| IDE-RUN-METADATA.json | Observed executable/model metadata and operational interruptions |
| candidate-integrity.json | Existing workflow/resource/license preservation against cd77d82 |
| package-outside-sync-tests.txt | Full post-fix suite:148 passed,1 skipped |
| package-after-lock-fix-tests.txt | Synced-folder failure retained:147 passed,1 failed,1 skipped |
| release-verification.json | Clean wheel, all1660 installed files,1630 resources and accepted artifact identities |
| release-SHA256SUMS | Exact wheel, source archive and portable skill ZIP hashes |
| accepted-sdist-smoke.json | Exact accepted source archive installed and imported outside the checkout |
| website-ready.json | Local website commit, static checks and committed PDF byte preservation |

Frozen task/rubric files, manual review decisions and the protocol are in ../../benchmarks/comparison. Downloaded upstream snapshots are kept in ignored working storage; no source helper was automatically executed. IDE screenshots containing account UI were not added to this public evidence bundle.

Publication remains held. Files in this folder do not prove the candidate is available on PyPI or the live website.

The accepted local artifacts are under .work/benchmark-v2/accepted-release. Earlier build directories are superseded. The Windows skip is the symlink-creation test because this account cannot create symlinks; it is not counted as a pass. The source archive intentionally excludes the experimental response bundle, which remains in this repository.
