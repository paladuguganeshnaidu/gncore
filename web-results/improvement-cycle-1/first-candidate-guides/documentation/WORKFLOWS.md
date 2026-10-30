# GNCore Documentation: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Technical Localization (`documentation-translation`)

Identify source locale, target locale, audience, and approved glossary. Preserve code, placeholders, links, units, legal meaning, and formatting tokens. Flag ambiguous source text instead of guessing. Use locale-appropriate dates and numbers; do not translate identifiers. Verify UI length and right-to-left behavior when relevant.

### Technical Writing (`technical-writing`)

Inspect the actual behavior and audience before drafting. Put the shortest successful path first, identify prerequisites and supported versions, and verify commands and output. Keep terminology consistent and label assumptions. Do not document unimplemented behavior or expose credentials. Update nearby references when a public command or interface changes.

### API Documentation (`documentation-api`)

Inspect routes, schemas, authentication, error behavior, and versioning. Document required and optional fields, examples, pagination, rate limits, and known constraints. Verify examples against a safe environment or schema. Keep secrets and personal data out. Clearly flag undocumented behavior instead of guessing.
