# Developer category evaluations

The versioned corpus has **90 concrete scenarios across all 30 active categories**: a normal task, an underspecified request and a boundary/failure case per category. Cases specify actual synthetic inputs/environment, expected category and relevant workflow IDs, a deliverable path, artifact properties, prohibited assumptions/actions and observable verification.

```bash
gncore evaluate --validate
gncore evaluate --list
```

Edit `catalog/evaluation_specs.py` and the retained explicit examples in `catalog/base_evaluations.json`; rebuild with `python scripts/build_evaluations.py`. Validation rejects missing category/kind combinations, duplicate IDs, unsafe paths and unknown mode references. A custom corpus uses the same `schema_version: 1` format as `src/gncore/evaluation_cases.json`.

Run a task in a compatible host with both its prompt and supplied context. Save the real artifact and a separate record, for example:

```json
{
  "case_id": "frontend-normal",
  "categories": ["web-frontend"],
  "workflows": ["web-front-design", "web-front-minimalism"],
  "decisions": {"motion": "none"}
}
```

```bash
gncore evaluate --case frontend-normal --response response.json --artifacts ./results/frontend-normal
```

Exit 0 means recorded category/workflow/decision checks and required nonempty artifact presence pass; exit 1 means an objective check fails; exit 2 means invalid input or an operational error. Artifact paths stay inside the supplied directory. Submitted commands are never executed by this runner.

**Structural success is not semantic success.** A placeholder file can pass presence checks. The report explicitly leaves human review pending and external tool checks unexecuted, with the required evidence. These 90 complete agent tasks have not all been run or blindly graded. Corpus completeness, source merge checks, runtime regressions and the actual CPU neural-network/browser probes are reported separately.
