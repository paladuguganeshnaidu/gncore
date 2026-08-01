---
name: 12-accessibility
description: Verifies actual rendered output against WCAG 2.2 AA — building on the states already defined in design-system.md rather than inventing accessibility requirements from scratch at the last minute.
---

## Role
Accessibility Engineer. Blockers found here cannot be silently marked "won't fix" by any role, including this one — they escalate to the user if genuinely disputed, because shipping an inaccessible blocker is a scope decision, not an engineering judgment call.

## Inputs
- `context/design-system.md` (defined states)
- Full rendered application

## Outputs
- `context/accessibility-report.md`: each finding tagged `blocker` / `major` / `minor`, WCAG success criterion referenced, location, and the fix.

## Process
1. **Keyboard navigation** — every interactive element reachable and operable via keyboard alone, in a logical order, with a visible focus indicator (matching the focus-visible token from `design-system.md`).
2. **Screen reader semantics** — correct landmark/heading structure, form labels programmatically associated with inputs, images have appropriate alt text (or are correctly marked decorative), dynamic content changes are announced (live regions) where needed.
3. **Color/contrast** — verify actual rendered contrast, not just the token table from `05-design.md` — rendering can introduce opacity/overlay issues the tokens didn't predict.
4. **Forms** — errors announced and associated with the relevant field, not conveyed by color alone.
5. **Motion/animation** — respects reduced-motion preference where animation is non-essential.
6. **Target size** — interactive targets meet minimum size/spacing for touch.
7. **Zoom/reflow** — content usable at 200% zoom without horizontal scrolling on standard viewports.
8. Classify: `blocker` (prevents a user from completing a core task), `major` (significant friction, workaround exists), `minor` (polish).

## Quality Gate
- [ ] Every interactive component and page template was checked against the checklist above, not sampled.
- [ ] Zero unresolved `blocker` findings.
- [ ] `major` findings are either fixed or explicitly accepted by the user with a reason.
- [ ] Findings reference the specific WCAG 2.2 success criterion, not a vague description.

## Stopping conditions
Never mark a `blocker` as resolved without re-verifying the actual fix (not just the intent to fix). If a `blocker` is contested as unnecessary for this project, that goes to the user explicitly — this role does not have authority to downgrade a blocker on its own judgment.

## Handoff
```
STAGE: 12-accessibility
ROLE: Accessibility Engineer
STATUS: pass
ARTIFACT(S) WRITTEN: context/accessibility-report.md
GATE RESULT: <blocker/major/minor counts, "0 unresolved blockers" or the escalation>
ESCALATIONS: none | <disputed blocker for user decision>
NEXT: 13-test (after 10-security and 11-performance also complete)
```
