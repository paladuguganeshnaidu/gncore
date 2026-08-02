# Pattern library

A reference, not a per-build artifact — owned by no single stage, read by `04-architect.md` and `05-design.md` alongside `research-notes.md`.

**What this file is for:** durable, framework-agnostic decision *structure* — the shape of a good decision, not the specific answer. It exists because the baseline framework's strongest material (its theme-detection logic, its animation-library decision matrix, its package-name guidance) didn't survive this framework's rewrite, and that's a real capability gap: a model reasoning from zero domain defaults produces worse first drafts than one reasoning from good defaults, even when both eventually converge on the same answer.

**What this file is explicitly not for:** specific package names, specific version numbers, specific "current best practice" claims, or anything else that goes stale. That is `research-notes.md`'s job, every time, with a checked source and date. This file supplies the skeleton; `research-notes.md` supplies the current specifics that fill it in. Neither stage should assert a specific package name that didn't come from `research-notes.md` — see the Quality Gate item added to `04-architect.md` for the enforcement mechanism.

---

## 1. Visual-theme-to-design-token mapping

A visual direction is a *character*, not a hex code. Map the requested (or inferred-from-audience) theme to a character description, then let `05-design.md` derive actual tokens from that character plus current-as-of-project design conventions:

| Theme character | Palette tendency | Type tendency | Motion tendency | Density |
| --- | --- | --- | --- | --- |
| Minimal | Low saturation, high contrast, 1–2 accent colors max | Restrained type scale, generous whitespace-driven hierarchy | Subtle, short-duration, easing-forward only | Low — few simultaneous elements |
| Corporate/professional | Desaturated primary + one confident accent, high legibility | Conservative scale, strong hierarchy via weight not size | Minimal, functional only (state changes, not decoration) | Medium |
| Vibrant/consumer | Higher saturation, multi-color palettes intentional not accidental | Larger type scale, more expressive weight/size contrast | More visible, playful, still purposeful (not gratuitous) | Medium-high |
| Luxury/editorial | Restrained palette, often near-monochrome + one rich accent, generous negative space | Serif or high-contrast display type paired with a quiet body face | Slow, deliberate, rare | Low — negative space is the point |

This table is a starting *character*, not a rule — `05-design.md` still derives actual token values from the specific audience/purpose in `requirements.md`, and still has to justify the direction in one line, per that stage's existing process. This table just means that justification starts from a reasoned default instead of "modern clean."

## 2. Component-state checklist (already implied in `05-design.md`, made explicit here)

Every interactive component needs a defined value for each of these states before `06-scaffold.md` generates a tokens file:

`default` → `hover` → `focus` (and focus-**visible** specifically, not just `:focus`) → `active` → `disabled` → `error` → `loading`

A component missing any of these isn't "mostly done" — an undefined state is exactly the kind of gap `12-accessibility.md` and `09-review.md` exist to catch, but catching it there is a late, expensive fix versus defining it here, up front.

## 3. Data-model decision tree (relational vs. document store, in principle)

Not a recommendation for a specific database product — that's `research-notes.md`'s job once the shape below points toward a category:

- **Data is highly relational** (entities reference each other, referential integrity matters, ad-hoc queries across relationships are expected) → relational store fits the shape better.
- **Data is naturally document-shaped** (each record is mostly self-contained, schema varies per record, relationships are shallow or denormalized by design) → document store fits the shape better.
- **Both are present** (e.g., relational core + variable per-record metadata) → a relational store with a JSON/JSONB column for the variable part is usually simpler to operate than running two data stores, unless the variable part's query patterns genuinely need document-native indexing.
- **Write volume and consistency requirements** matter more than "which is trendier" — a chat app's message history and an e-commerce order/inventory system have very different tolerance for eventual consistency, and that tolerance should drive the choice before popularity does.

## 4. Deployment-topology decision tree (by requirement shape, not platform name)

- **No server-side logic, content doesn't change per-request** → static hosting fits. Cheapest, simplest, fewest failure modes.
- **Server-side logic needed, but usage is bursty/unpredictable or the project needs to scale to zero when idle** → serverless/functions fits the shape better than a fixed server.
- **Server-side logic needed, with steady/predictable load, long-lived connections (websockets, persistent state in memory), or workloads serverless cold-starts would hurt** → a persistent server-runtime fits better.
- **Requirement shape can change over the project's life** (e.g., a static MVP that's likely to need auth/server logic within the year) — note this explicitly in the ADR as a reason to prefer a topology with a clear upgrade path, not necessarily the cheapest option today.

Which specific platform within a chosen topology is a `research-notes.md` question (current pricing, region availability, build-minute limits) — this tree only narrows the category.

---

## How `04-architect.md` and `05-design.md` use this file

Read `pattern-library.md` for durable structure. Read `research-notes.md` for the current specifics that fill that structure in (actual package names, actual current versions, actual current pricing). If a concrete package/library name shows up in `architecture.md` and it didn't come from `research-notes.md`, that's a Quality Gate failure in `04-architect.md` — this file is a source of *shape*, never a source of *specific names*, and the gate exists specifically to keep it that way.
