Viewed SKILL.md:1-389
Viewed SKILL.md:1-458

## CASE A — Frontend Architecture: Neighborhood Physiotherapy Booking

Guided by the GNCore [web-frontend](../../src/gncore/skills/unified_data/web-frontend/SKILL.md) skill.

### 1. Visual Direction
A **quiet organic minimalist** direction tailored for patients in physical discomfort or anxiety:
- **Palette**: Low-arousal, warm neutrals (soft linen `#F8F7F4` canvas, stone-gray `#EAE7E1` card surfaces, deep slate `#1E2429` for text yielding $\ge 7:1$ contrast, and an earthy sage/terracotta accent `#3D5A50` for interactive states).
- **Surfaces & Geometry**: Flat cards with subtle 1px borders (`#D6D2CA`), 8px border radii, zero harsh box-shadows, and calm pacing with generous whitespace to prevent cognitive overload.

### 2. Typography Hierarchy
A human-centered grotesk/sans system with generous line spacing:
- **H1 (Page Title)**: 28px/1.25, semi-bold (`font-weight: 600`), e.g., "Schedule an Appointment".
- **H2 (Step Headers)**: 20px/1.3, medium (`font-weight: 500`).
- **Body & Labels**: 16px/1.5, regular (`font-weight: 400`), max line length 60ch.
- **Microcopy / Validation**: 14px/1.4, regular, linked via `aria-describedby`.

### 3. Keyboard and Focus Behavior
- **Focus Rings**: Dual-tone, high-contrast indicator (`outline: 2px solid #1E2429; outline-offset: 2px`) visible on both dark and light surfaces without relying solely on color.
- **Tab Flow**: Strict linear sequence: `Service Selection` $\rightarrow$ `Practitioner` $\rightarrow$ `Date Picker` $\rightarrow$ `Available Slots` $\rightarrow$ `Patient Info` $\rightarrow$ `Submit Booking`.
- **Composite Controls**: Arrow-key navigation (`roving tabindex`) across the date grid and time-slot pill group.
- **Assistive Tech**: Time slots load into an `aria-live="polite"` region. Field errors announce dynamically with `role="alert"`.

### 4. Small-Screen Layout (Mobile Viewport $\le 390\text{px}$)
A single-column vertical stack avoiding horizontal scrolling and modal popups:
1. **Clinic Header**: Sticky top bar (48px) with clinic contact, location, and progress pill ("Step 2 of 3").
2. **Step Cards**: Vertically stacked accordion-like cards:
   - *Card 1 (Service & Therapist)*: Radio tiles (minimum touch target $52\text{px} \times 52\text{px}$).
   - *Card 2 (Date & Time)*: Horizontal snap date scrollbar followed by a 2-column grid of time slots ($48\text{px}$ touch targets).
   - *Card 3 (Details Form)*: Full-width stacked inputs (`Name`, `Phone`, `Notes`) with auto-capitalization and explicit labels above inputs.
3. **Sticky Bottom Action Bar**: Fixed bar containing appointment summary and a full-width primary CTA button ("Confirm Booking"), pinned above mobile browser chrome.

### 5. GNCore Workflow IDs
- `web-front-design`: Product-grounded visual identity and palette.
- `web-front-organic`: Natural, low-stress surface treatments.
- `web-front-accessibility`: Keyboard traversal, touch targets, and ARIA semantics.
- `web-front-styling`: Responsive small-screen layout tokens.

### 6. Validation Status
- **Completed Validation**: Analytical verification of semantic HTML structure, keyboard traversal logic, contrast ratios ($\ge 7:1$), and touch target clearance ($\ge 48\text{px}$).
- **Intended Validation (Unexecuted)**: Live browser Playwright audits, screen-reader passes (NVDA/VoiceOver), and responsive viewport resize tests—*not run per pure reasoning constraints*.

---

## CASE B — Backend Architecture: Idempotent Order Creation

Guided by the GNCore [web-backend](../../src/gncore/skills/unified_data/web-backend/SKILL.md) skill.

### 1. Assumptions
- Relational database with ACID transaction support (e.g., PostgreSQL).
- Tenant identity is authenticated via a verified JWT or server session.
- Downstream payment or dispatch side effects are executed asynchronously via a transactional outbox table.

### 2. Request Validation
- **Endpoint**: `POST /v1/orders`
- **Headers**:
  - `Idempotency-Key`: Required string (UUIDv4 or client token, 16–128 chars).
  - `Authorization`: Bearer token determining `tenant_id`.
- **Payload Validation**: Strict JSON schema: `items` (non-empty array, positive integer `quantity`, valid SKU `string`), `currency` (ISO-4217), and valid shipping payload. Rejects missing/malformed payloads with `400 Bad Request` before invoking business logic.

### 3. Tenant-Scoped Idempotency Keys & Schema
Idempotency state is strictly partitioned by tenant:
```sql
CREATE TABLE idempotency_records (
    tenant_id VARCHAR(64) NOT NULL,
    idempotency_key VARCHAR(128) NOT NULL,
    request_hash CHAR(64) NOT NULL, -- SHA-256 of canonicalized request body
    status VARCHAR(20) NOT NULL,    -- 'IN_PROGRESS', 'COMPLETED', 'FAILED'
    response_code INT,
    response_body JSONB,
    order_id UUID,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    expires_at TIMESTAMPTZ NOT NULL,
    PRIMARY KEY (tenant_id, idempotency_key)
);
```

### 4. Concurrent Duplicate Handling
- An atomic `INSERT ... ON CONFLICT (tenant_id, idempotency_key)` is executed:
  - If a row already exists with status `'IN_PROGRESS'`: reject immediately with **`409 Conflict`** and header `Retry-After: 2` (or hold connection up to a bounded lock timeout).
  - If a row exists with different `request_hash`: reject with **`422 Unprocessable Entity`** ("Idempotency key reuse with mismatched payload").

### 5. Transaction Boundaries & Response Replay
1. **Begin DB Transaction**:
   - Claim idempotency key: `INSERT INTO idempotency_records (status='IN_PROGRESS')`.
   - Validate catalog/inventory, calculate totals, insert order and line items into `orders` and `order_items`.
   - Write message to `transactional_outbox` for async fulfillment/payments.
   - Update idempotency record: `status = 'COMPLETED'`, `response_code = 201`, `response_body = {...}`.
2. **Commit Transaction**: Returns `201 Created`.
3. **Response Replay**: If key exists with status `'COMPLETED'` and matching `request_hash`, bypass the order service and immediately replay `201 Created` with stored JSON body and header `Idempotent-Replay: true`.

### 6. Essential Contract Tests
1. **Standard Creation**: Valid request $\rightarrow$ `201 Created` with generated `order_id`.
2. **Timeout Retry Replay**: Secondary request with identical key and payload $\rightarrow$ `201 Created` with identical `order_id` and `Idempotent-Replay: true`.
3. **Concurrent Execution**: Two simultaneous identical requests $\rightarrow$ exactly one creates order (`201`), the other receives `409 Conflict`.
4. **Key Conflict**: Same key with altered body $\rightarrow$ `422 Unprocessable Entity`.
5. **Cross-Tenant Isolation**: Identical `Idempotency-Key` sent under Tenant B $\rightarrow$ independent order created; no interference with Tenant A.
6. **Rollback on Error**: Unhandled exception during order creation sets status to `'FAILED'` and rolls back the transaction, enabling safe future retries.

### 7. GNCore Workflow IDs & Execution Status
- **Workflows**: `web-backend-api-design`, `web-backend-patterns`, `web-backend-postgres-patterns`, `web-backend-contract-first`.
- **Execution Status**: All contracts, schemas, and tests are designed analytically. **No tests were run on a live runtime**, adhering to the pure reasoning instruction.