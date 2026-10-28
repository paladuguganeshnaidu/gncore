# Offline category evaluations

The first evaluation corpus is a **12-category pilot with 36 authored scenarios**. Each category has a normal task, an underspecified request, and a constraint or failure-boundary case. The cases contain synthetic or supplied facts, expected workflows, a deliverable path, artifact properties, prohibited assumptions/actions, human review questions, and an observable verification method.

The pilot covers frontend, backend, coding, data engineering, machine learning, finance, presentations, research, legal intake, healthcare administration, education, and games. Extending this to all 60 categories and conducting comparative output reviews remain later roadmap work.

## Inspect the cases

```bash
gncore evaluate --validate
gncore evaluate --list
```

The packaged authoring source is `src/gncore/evaluation_cases.json`. Validation checks that category and workflow IDs exist and each listed category has all three kinds of scenario. A custom corpus uses the same format:

```bash
gncore evaluate --validate --corpus ./my-cases.json
```

Each case has these fields:

| Field | Meaning |
| --- | --- |
| `id`, `category`, `kind` | Unique case, primary category, and `normal`, `underspecified`, or `boundary` |
| `prompt`, `context` | Task and supplied inputs/environment; present both to the agent |
| `workflows` | Relevant known modes; at least one should appear in the recorded selection |
| `artifact` | Nonempty output file required relative to the artifact directory |
| `decisions` | Optional exact structural expectations for recorded decisions |
| `properties`, `prohibited` | Artifact rubric and assumptions/actions requiring review |
| `verification`, `human_review` | Required execution evidence and human judgment questions |

## Record and check a result

Run a case in a compatible host agent with the appropriate installed skill, using the case's prompt and context. Keep the actual artifact and relevant test/browser logs. Record selection and decisions in a separate JSON file, for example:

```json
{
  "case_id": "frontend-normal",
  "categories": ["web-frontend"],
  "workflows": ["web-front-design", "web-front-minimalism"],
  "decisions": {"motion": "none"}
}
```

With the generated `booking.html` in `./results/frontend-normal/`, run:

```bash
gncore evaluate --case frontend-normal --response ./response.json --artifacts ./results/frontend-normal
```

The runner checks recorded category/workflow selection, declared decisions, and actual artifact presence. Exit `0` means these structural checks pass; exit `1` means one fails; exit `2` means invalid input or an operational error. Artifact paths must stay inside the supplied directory. No submitted commands or imported tools are executed by the runner.

**A structural pass is not an output-quality pass.** A placeholder file can pass presence checks. The report therefore always leaves artifact-property review, prohibited-action review, and semantic quality pending. Required tool checks are marked `not-run`, with the evidence needed to complete them. Browser, database, renderer, or model access is never silently assumed. This prevents a passing JSON record from being presented as an independently verified website, model, document, or professional judgment.

The current corpus has been reviewed for concrete inputs, scope, expected modes, and observable criteria. It has not yet been executed as 36 complete agent tasks or used for blinded before/after quality scoring. No hosted-model calls or evaluation costs are incurred by these commands.
