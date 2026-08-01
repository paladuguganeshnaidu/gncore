# Quality gate template

Use this shape for every stage's Quality Gate section in skills/*.md.

- [ ] binary, checkable criterion — not "looks good", but "returns 200" / "zero Critical findings" / "every requirement maps to a built feature"
- [ ] ...

## Stopping conditions
- Pass: all criteria above are true.
- Fail, fixable in-stage: iterate up to N times, then escalate.
- Fail, needs escalation: specific condition that always goes to the user rather than being guessed at.
