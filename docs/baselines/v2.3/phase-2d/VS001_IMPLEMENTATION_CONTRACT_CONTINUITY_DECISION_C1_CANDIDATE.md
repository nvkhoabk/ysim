# VS001 Implementation Contract Continuity Decision C1

- Candidate: `V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DECISION-C1`
- Status: `CANDIDATE`
- Approval: `PENDING_HUMAN_APPROVAL`
- Implementation authorized: `false`
- Runtime evidence: `NOT_EXECUTED`
- Next gate: `HUMAN_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_CONTINUITY_DECISION_REQUIRED`

## Authority gap findings

### GAP-LOCALE-NEGOTIATION

```json
{
  "authorized_semantics": [
    "Locale input is Accept-Language.",
    "A supported exact locale wins.",
    "Storefront default is the fallback.",
    "Missing mandatory localized content excludes list and produces uniform detail not-found.",
    "Absent optional localized content is omitted.",
    "No localized slug, machine translation, Product-name inference or cross-Storefront locale fallback."
  ],
  "finding_id": "GAP-LOCALE-NEGOTIATION",
  "governing_decision": "V23-P2D-VS001-IMPLEMENTATION-DEC-002",
  "unresolved_observable_semantics": [
    "ordering among multiple language ranges and equal q-values",
    "q=0 handling",
    "wildcard handling",
    "malformed member handling",
    "language-subtag fallback versus exact-only matching",
    "public representation of the resolved content locale"
  ],
  "why_not_inferred": "The accepted option names Accept-Language and exact matching but contains no algorithm for multi-value negotiation or malformed/wildcard ranges. Each possible algorithm can return different localized public content."
}
```

### GAP-CURSOR-SNAPSHOT-CONTINUITY

```json
{
  "authorized_semantics": [
    "One HTTP request uses one injected UTC evaluation instant and one PostgreSQL repeatable-read snapshot.",
    "Ordering is public_slug then opaque public identity.",
    "Cursor carries an opaque representation of the last ordering tuple and snapshot identity.",
    "Continuation retains snapshot identity or fails closed.",
    "No claim that an unrelated later detail request shares historical state."
  ],
  "finding_id": "GAP-CURSOR-SNAPSHOT-CONTINUITY",
  "governing_decisions": [
    "V23-P2D-VS001-IMPLEMENTATION-DEC-003",
    "V23-P2D-VS001-IMPLEMENTATION-DEC-008"
  ],
  "unresolved_observable_semantics": [
    "stateless temporal/revision reconstruction versus server-held/exported PostgreSQL snapshot",
    "cursor lifetime and expiry",
    "treatment of inserts, updates and deletions between pages",
    "public status and error envelope for invalid, expired or unavailable snapshots",
    "resource ownership and cleanup for stateful snapshots"
  ],
  "why_not_inferred": "PostgreSQL repeatable-read is transaction-scoped and does not automatically span HTTP requests. The accepted option explicitly leaves snapshot continuation mechanisms and limits open."
}
```

## Decisions

### V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-001 — Deterministic Accept-Language Negotiation

- Selected option: `None`
- Recommended: `OPT-QORDER-EXACT-THEN-STOREFRONT-DEFAULT`

#### OPT-QORDER-EXACT-THEN-STOREFRONT-DEFAULT

```json
{
  "algorithm": {
    "malformed": "Ignore an individually malformed range; if no acceptable exact supported range remains, use Storefront default.",
    "mandatory_content_failure": "After Storefront default, missing mandatory localized fields excludes the list item and makes detail return the approved uniform Product not-found outcome.",
    "matching": "Case-insensitive BCP47 canonical comparison with exact supported-tag equality only; no language-subtag truncation.",
    "parse": "Parse comma-separated concrete BCP47 language ranges; a missing q-value is 1.0.",
    "priority": "Sort by descending q-value, preserving original header order for ties.",
    "q_zero": "q=0 ranges are explicitly unacceptable and never selected.",
    "resolved_locale_output": "Return the resolved locale in the Content-Language response header for list, detail and uniform detail not-found.",
    "wildcard": "Wildcard does not select an arbitrary supported locale; proceed to Storefront default."
  },
  "boundaries": [
    "fr-CA;q=0.8,en-US;q=1.0 selects supported en-US.",
    "fr-CA;q=0.8,en-US;q=0.8 selects the first supported header member.",
    "en;q=1 does not match en-US unless en itself is supported.",
    "*;q=1 and malformed-only input use Storefront default.",
    "en-US;q=0 never selects en-US."
  ],
  "impact": "Deterministic and aligned with the accepted exact-match rule without adding language-family fallback.",
  "non_inferences": [
    "No localized slug.",
    "No machine translation.",
    "No cross-Storefront fallback.",
    "No Product-name content inference."
  ],
  "option_id": "OPT-QORDER-EXACT-THEN-STOREFRONT-DEFAULT",
  "summary": "Parse Accept-Language deterministically by quality and header order, accept exact supported tags only, then use Storefront default.",
  "tradeoff": "Callers requesting only a related language tag may receive Storefront default instead of a same-language regional locale."
}
```

#### OPT-SINGLE-HIGHEST-QUALITY-THEN-DEFAULT

```json
{
  "impact": "Simple deterministic behavior with minimal negotiation surface.",
  "non_inferences": [
    "No subtag fallback.",
    "No wildcard locale selection.",
    "No localized slug."
  ],
  "option_id": "OPT-SINGLE-HIGHEST-QUALITY-THEN-DEFAULT",
  "summary": "Consider only the highest-quality valid concrete range; if it is unsupported, use Storefront default without trying lower-ranked ranges.",
  "tradeoff": "A lower-ranked supported caller preference is ignored and may unexpectedly produce Storefront default."
}
```

#### OPT-QORDER-WITH-BASIC-LANGUAGE-FALLBACK

```json
{
  "impact": "More callers receive content in the requested language family.",
  "non_inferences": [
    "No machine translation.",
    "No cross-Storefront fallback.",
    "No localized slug."
  ],
  "option_id": "OPT-QORDER-WITH-BASIC-LANGUAGE-FALLBACK",
  "summary": "Use q-value/header priority, exact match first, then progressively truncate language subtags before Storefront default.",
  "tradeoff": "Introduces observable fallback not stated by the accepted exact-match option and requires an approved truncation policy."
}
```

Recommendation rationale:

The recommended option gives deterministic standard preference ordering while preserving the accepted exact-supported-locale boundary and avoiding an unauthorized language-subtag fallback.

### V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-002 — Cross-Request Catalog Pagination Snapshot Continuity

- Selected option: `None`
- Recommended: `OPT-STATELESS-LOGICAL-REVISION-CURSOR`

#### OPT-STATELESS-LOGICAL-REVISION-CURSOR

```json
{
  "contract": {
    "cleanup": "No server-held snapshot resource; normal fixture ownership cleanup applies after evidence.",
    "concurrent_change": "Rows created after the revision are excluded; versioned/retired rows required by the revision remain queryable until cursor expiry; price, publication and validation resolve as-of the cursor revision and evaluation instant.",
    "cursor": "Opaque authenticated cursor binds Storefront, resolved locale, page limit, public_slug/public identity ordering tuple, UTC evaluation instant, logical catalog revision and 15-minute expiry.",
    "invalid_or_expired": "HTTP 400 with {error:{code:'INVALID_CURSOR',message:'Invalid cursor'}} for malformed, tampered, wrong-context, expired or no-longer-reconstructable cursors; no internal reason is disclosed.",
    "request_snapshot": "Each page request opens its own PostgreSQL repeatable-read transaction and captures no cross-request database transaction state."
  },
  "impact": "Stateless horizontal operation and deterministic pages across concurrent changes.",
  "non_inferences": [
    "No cache authority.",
    "No public database identity.",
    "No guarantee beyond cursor expiry.",
    "No historical state sharing with an unrelated detail request."
  ],
  "option_id": "OPT-STATELESS-LOGICAL-REVISION-CURSOR",
  "summary": "Use a signed opaque cursor containing a logical evaluation instant and catalog revision, with versioned records queried as-of that revision in a new repeatable-read transaction per page.",
  "tradeoff": "Requires temporal/revision retention and authenticated cursor validation through the expiry window."
}
```

#### OPT-SERVER-HELD-POSTGRES-SNAPSHOT-CURSOR

```json
{
  "contract": {
    "cursor": "Opaque authenticated handle binds Storefront, locale, ordering tuple and server snapshot handle; it exposes no PostgreSQL identifier.",
    "expiry": "Snapshot expires after 60 seconds and is closed on completion, error or cleanup.",
    "invalid_or_expired": "HTTP 400 uniform INVALID_CURSOR response without differentiating expiry, tampering or missing server state.",
    "request_snapshot": "First page exports a repeatable-read snapshot while an owned transaction remains open; later pages import/reference that snapshot through protected server state."
  },
  "impact": "True PostgreSQL MVCC continuity without temporal application tables.",
  "non_inferences": [
    "No public snapshot identifier.",
    "No snapshot reuse by unrelated detail requests.",
    "No unbounded transaction lifetime."
  ],
  "option_id": "OPT-SERVER-HELD-POSTGRES-SNAPSHOT-CURSOR",
  "summary": "Keep an exported PostgreSQL snapshot/owning transaction server-side and issue an opaque cursor that references it for a bounded 60-second continuation window.",
  "tradeoff": "Long-lived transactions and server affinity consume resources and complicate horizontal scaling and cleanup."
}
```

#### OPT-REQUEST-LOCAL-SNAPSHOT-FAIL-CLOSED

```json
{
  "contract": {
    "continuation": "Cursor continuation is accepted only if a stored snapshot/revision equality check proves unchanged catalog state; otherwise fail closed.",
    "failure": "HTTP 409 with {error:{code:'CATALOG_SNAPSHOT_UNAVAILABLE',message:'Catalog snapshot unavailable'}} and no internal change reason; caller must restart from the first page.",
    "request_snapshot": "Each page request has an independent repeatable-read snapshot and evaluation instant."
  },
  "impact": "Avoids temporal retention and long-lived database transactions.",
  "non_inferences": [
    "No best-effort mixed snapshot.",
    "No offset fallback.",
    "No hidden retry that changes the evaluation instant."
  ],
  "option_id": "OPT-REQUEST-LOCAL-SNAPSHOT-FAIL-CLOSED",
  "summary": "Guarantee consistency only within each page request and refuse continuation whenever the original logical snapshot cannot be reconstructed.",
  "tradeoff": "Concurrent catalog changes can prevent forward traversal and introduce a new observable restart outcome."
}
```

Recommendation rationale:

The stateless logical-revision cursor preserves deterministic traversal without long-lived PostgreSQL transactions, but its temporal retention, expiry and public invalid-cursor contract require explicit human approval.

## Non-claims

- `NOT_IMPLEMENTATION_CONTRACT_C1_R1_APPROVAL`
- `NOT_VS001_IMPLEMENTATION_AUTHORIZATION`
- `NOT_RUNTIME_EVIDENCE`
- `NOT_API_UI_OR_DATABASE_IMPLEMENTATION`
- `NOT_MIGRATION_OR_FIXTURE_EXECUTION`
- `NOT_BRD_UXF_OR_COMMISSIONING_MODIFICATION`
- `NOT_DEPLOYMENT_PRODUCTION_OR_YADF_WORK`
