# GNCore next upgrade plan

Prepared on 2026-10-28 against commit `6321d72`. This roadmap now tracks a completed first implementation batch and the remaining upgrades. The detailed requirements below remain the targets; a pilot or partial implementation does not satisfy an entire later round.

## Implementation status

| Item | Current state |
| --- | --- |
| GN-01 | Implemented: constraint-filtered selection, multiword/spelling normalization, motion negation, documented precedence, and contradiction errors |
| GN-02 | Implemented: digest-based preflight, staged verified installs, preserved custom files, backups, dry runs, automatic rollback, and interrupted-process recovery |
| GN-03 | Pilot implemented: 36 scenarios across 12 categories and an offline structural runner; extension to all 60 and complete task executions remain |
| GN-04–GN-12 | Planned; no claim of comparative output reviews, complete mode rewrites, global routing, source locking, offline rebuilding, or profiles |
| GN-13 | Installed-file verification implemented; dependency reports and storage deduplication remain |
| GN-14 | Installation failure-path tests added, including actual process exit; expanded platform evidence and performance baselines remain |
| GN-15–GN-16 | Planned; source push and package checks do not constitute public release or automated source refresh |

See [installation and recovery](INSTALLATION.md), [evaluation format](EVALUATION.md), and the [local evidence](LOCAL_VERIFICATION.md). This first batch does not alter or relicense the 60 category playbooks.

## Outcome

Improve the quality of the result an agent produces from a short idea. Keep one adaptive entrypoint per category, retain every existing workflow, and make selection, implementation, verification, installation, and future maintenance more dependable.

The current baseline is 60 category skills, 553 workflows, 35 automated tests, and a verified resource-preserving export. Those checks establish catalog and software behavior. The next round needs evidence about actual task outcomes across the categories.

## Findings behind the priorities

| Finding | Evidence | Upgrade consequence |
| --- | --- | --- |
| An excluded theme can be selected as a fallback | `frontend_plan("A website, no minimalism and no swiss")` returns `swiss` while listing it as excluded | Filter every selection path, including fallbacks, through the constraints |
| A natural-language motion constraint is missed | `frontend_plan("A website, not animated")` permits motion | Expand constraint handling and test combinations and paraphrases |
| A spelling used in the original request is missed | `frontend_plan("A landing page in britalisim style")` returns inferred minimalism | Normalize documented style aliases and common spellings without guessing arbitrary unknown names |
| Many modes share their procedure text | Of 553 workflows, 459 have unique procedure texts; 116 workflows belong to 22 repeated-text groups | Keep useful shared foundations and add mode-specific decisions, artifacts, and verification where the modes differ |
| The planning command covers frontend direction | `planning.py` exposes `frontend_plan()` | Add task routing for the other categories with explicit ambiguity handling |
| Migration checks an unmanaged collision after moving legacy folders | `install_categories.py` calls `shutil.move()` before its primary-folder conflict check | Complete preflight before mutation and make failure recovery transactional |
| Export validates paths but has no declared resource digest check | `bundles.py` reads manifest-listed files without comparing a stored checksum | Add versioned content hashes and a scoped verification command |
| Research dates are fixed in importer code | Research/import scripts contain the date `2026-10-28` | Capture review dates per run and distinguish cached observations from a fresh review |
| Current source inclusion uses textual license and relevance heuristics | `license_review()` and `source_relevance()` in the category builder | Make automated screening distinct from a recorded inclusion decision |

The planner examples above were executed during this review. The migration and pipeline findings are from code inspection. Repeated procedure text is a review signal, not proof that every repeated procedure is inappropriate.

## Upgrade sequence

### Round 1 — reliability and safe changes

#### GN-01: Respect constraints on every planning path — P0

- Normalize explicit themes, common spellings, and multiword forms consistently.
- Interpret negative style and motion constraints, including “not animated,” “without movement,” and excluded fallback styles.
- Handle contradictory constraints with a clear unresolved decision instead of selecting a prohibited option.
- Preserve an explicit theme and an existing brand according to a documented precedence rule.

Acceptance: every returned theme is outside the exclusion set; the three reproduced cases above behave as intended; existing explicit-theme, brand, and product-context cases continue to pass.

#### GN-02: Preflight and recover installations — P0

- Inspect all intended destinations before moving or writing any folder.
- Identify managed files through recorded provenance and hashes rather than only the word `GNCore` in a file.
- Stage an installation, verify its completeness, then switch it into place with a recoverable backup.
- Preserve customized and unmanaged files and provide a dry-run change summary.

Acceptance: an unmanaged collision leaves the original installation untouched; an interrupted or failed install can restore the original state; successful migration preserves custom backups and installs a complete category set.

### Round 2 — evaluate real skill behavior

#### GN-03: Build a category evaluation corpus — P0 foundation

- Prepare three initial scenarios for every category: a normal task, an underspecified task, and a constraint/failure-boundary task. Initial scope: 180 scenarios across 60 categories.
- Each case records inputs, expected category/modes, required artifact properties, prohibited assumptions or actions, and an observable verification method.
- Start with 12 representative categories before extending the same format to all 60.

Acceptance: every category has a reviewed scenario set; the runner distinguishes objective checks, human review, and checks requiring unavailable tools.

#### GN-04: Compare output quality before and after revisions — P1

- Save a baseline output and a revised output for the same scenario and environment.
- Score task completion, factual grounding, constraint compliance, artifact correctness, usability, and verification evidence.
- Use blinded human review for subjective visual and editorial judgments. Optional model reviewers can supply supporting feedback.
- Keep hosted-model execution optional, with a configured provider and explicit cost limits. Offline fixtures remain usable without an account.

Acceptance: a changed skill has observable improvement evidence and relevant regression results. Structure checks and model confidence are not reported as expert-quality certification.

### Round 3 — deepen the workflow procedures

#### GN-05: Rewrite repeated and shallow modes — P1

For each mode that needs deeper guidance, define:

1. The inputs and context it needs.
2. The decisions that distinguish it from neighboring modes.
3. A useful procedure with relevant boundaries and failure cases.
4. The artifact or behavior it must deliver.
5. The checks that demonstrate a useful result.

Prioritize the repeated-text groups in `code-build` and `web-backend`, then extend the review to all categories. Keep shared execution guidance at category level and avoid repeating it inside every mode.

Acceptance: distinct modes have meaningful task-specific instructions; all existing workflow IDs remain accounted for; each rewrite is linked to evaluation cases. Line count is not a quality target.

#### GN-06: Add category-specific output contracts — P1

| Category family | Stronger artifact and verification requirements |
| --- | --- |
| Frontend and design | Product-specific tokens, real content, complete states, responsive screenshots, interaction and accessibility evidence |
| Backend and coding | Contracts, authorization boundaries, transaction and concurrency behavior, failure recovery, relevant tests |
| Data and ML | Data grain, leakage boundaries, reproducibility, reconciliations, baselines, uncertainty, measured evaluation |
| Business and operations | Source-backed facts, decision options, owners, dependencies, measurable outcomes, clear proposed actions |
| Word, PDF, presentations, spreadsheets | Valid files, render/recalculation checks, layout inspection, accurate links and calculations |
| Finance, legal, HR, healthcare administration | Traceable evidence, privacy boundaries, appropriate review, no invented figures or professional conclusions |
| Education | Objective/activity/assessment alignment, accurate examples and answer keys, accessibility, useful feedback |
| Mobile and games | Platform lifecycle, input and navigation, state transitions, loading/failure recovery, actual device or play-loop evidence |

Acceptance: every category specifies its deliverable and verification contract, with tool limitations stated honestly.

### Round 4 — improve selection across the library

#### GN-07: Add explainable task routing — P1

- Recommend a category, relevant modes, output type, constraints, and checks from a request.
- Support explicit category selection and cross-category work when the task requires it, such as financial analysis followed by a presentation.
- Return useful alternatives or an unresolved decision for ambiguous requests.
- Keep current frontend planning behavior compatible; introduce broader routing through an explicit option or separate command.

Acceptance: the evaluation corpus checks routing across all 60 categories. A task is not sent to frontend simply because a global router lacks a better match.

#### GN-08: Add project-context adaptation — P1

- Reuse the existing stack, brand, components, audience, document template, and data conventions from the supplied project context.
- Allow an optional project brief to record intentional preferences.
- Define precedence between the current request, explicit preferences, project conventions, and inferred defaults.
- Read only relevant project material and avoid collecting secrets or unrelated personal information.

Acceptance: explicit requests take priority, focused changes preserve the existing product, and missing context does not trigger unnecessary setup requirements.

### Round 5 — make research and source maintenance reproducible

#### GN-09: Add a versioned source lock — P1

- Record the immutable source identity, per-file digest, source-specific notices, review date, inclusion decision, and affected categories.
- Preserve distinct states for discovery, successful download, license screening, relevance review, accepted reference, and tested helper.
- Use resumable downloads, bounded retries, provider rate-limit handling, and a machine-readable failure report.

Acceptance: a cached result is not mislabeled as a fresh review; modified or missing source files are detected; unavailable sources do not silently become successful imports.

#### GN-10: Separate original guidance from reference obligations — P1

- Keep original GNCore authoring and third-party reference material identifiable.
- Preserve notices, attribution, modifications, and applicable share-alike requirements.
- Require a recorded inclusion decision when automatic screening is inconclusive.
- Review imported executable helpers separately from instructional prose and keep them inert during installation.

Acceptance: every shipped reference has traceable provenance and an inclusion record. Renaming or merging material never becomes a reason to erase its license terms.

#### GN-11: Rebuild from versioned inputs — P1

- Store the normalized authoring inputs and source lock needed to regenerate the catalog.
- Support an offline rebuild from approved available sources.
- Separate a fresh research operation from a routine rebuild.
- Compare generated trees from clean checkouts and explain intentional differences.

Acceptance: maintainers can reproduce the generated category files without relying on an unexplained `.work` state; builds do not trigger an unrequested research or network operation.

### Round 6 — improve installation size and maintenance

#### GN-12: Add deliberate installation profiles — P2

- Provide a core profile with complete category guidance and required attribution, and a full profile with relevant technical support resources.
- Offer focused category sets for common project types while retaining individual category selection.
- Keep omitted references from producing misleading instructions or broken required links.

Acceptance: a core installation can complete its advertised tasks; the full profile preserves all declared resources; profile changes do not remove customized files silently.

#### GN-13: Verify installed files and reduce duplication — P2

- Add a project-scoped verification report for missing, modified, and unmanaged files.
- Report dependency/tool requirements without installing them automatically.
- Measure duplicate resource bytes and reduce package duplication while keeping exported category folders self-contained.

Acceptance: verification is read-only by default, installed modifications are distinguished from corruption, and resource deduplication preserves portable paths and notices.

### Round 7 — improve cross-platform and operational evidence

#### GN-14: Expand failure and compatibility tests — P1

- Test paths with spaces, Unicode, source encodings, interrupted writes, corrupt metadata, missing resources, and permission failures.
- Check runtime compatibility separately from independent upstream-helper requirements.
- Add meaningful latency and package-size baselines before setting performance budgets.
- Preserve useful failure artifacts and avoid weakening assertions to obtain a passing run.

Acceptance: supported runtime/platform claims have evidence, and failed checks identify an actionable cause and recovery path.

### Round 8 — release and maintain the result

#### GN-15: Release from a clean, verified checkout — P1

- Regenerate the catalog and migration documentation from the accepted manifests.
- Run behavior, packaging, installation, source-integrity, and compatibility checks.
- Produce wheel, source archive, and skill ZIP artifacts with checksums and clear version information.
- Keep source pushes, merge decisions, release tags, and public package publication as distinct recorded states.

Acceptance: a clean installation behaves as documented, published artifacts match the verified build, and a release is announced only after its public state is verified.

#### GN-16: Define the next source-refresh process — P2

- Review upstream changes by affected category rather than replacing the library wholesale.
- Show content, license, dependency, and behavior changes before accepting an update.
- Rerun the affected evaluation cases and relevant shared regressions.
- Keep a rollback path to the previous accepted source lock and category bundle.

Acceptance: source refreshes have a reviewable diff, a stated reason, and comparison evidence. No recurring automation is created by this roadmap.

## First implementation batch

The recommended first batch is GN-01 and GN-02, plus the evaluation format and first 12-category scenario set from GN-03. These establish reliable planning and installation behavior and provide a way to measure subsequent content upgrades.

After that foundation, implement GN-05 and GN-07 against the evaluation cases. Source locking and reproducible authoring inputs should precede the next large source refresh. Installation profiles and resource deduplication follow the measured quality and integrity work.

Each batch should have a bounded diff, an acceptance report, migration notes where needed, and a verified GitHub state. No release version or completion date is promised by this plan.
