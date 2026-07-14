---
schema_version: "1.0"
document_code: V23-PHASE-2-REMEDIATION-CONTRACT
title: Phase 2 BRD/UXF Big-Bang Remediation Contract
product_baseline: "2.3"
document_revision: "0.1"
lifecycle_status: DRAFT
language: en
authority: PHASE_2_PREFLIGHT
supersedes: null
requirement_block_schema: YSIM-REQUIREMENT-BLOCK-1.0
---

# Phase 2 BRD/UXF Big-Bang Remediation Contract

## 1. Status and binding

- Artifact status: `DRAFT`.
- Phase: `PHASE_2A_PREFLIGHT`.
- Accepted registry commit:
  `8c2e41f89443048a5b8568b308c32129634d7241`.
- Accepted registry tag:
  `baseline/v2.3/requirements-registry/fc2-accepted`.
- Source document commit:
  `7f16d4c4b8ab514bd45de184f65ace221b03f4db`.
- Registry candidate: `V23-REQ-REGISTRY-FC2`.
- Source hash basis: `GIT_BLOB_CONTENT_AT_SOURCE_COMMIT`.
- Source aggregate:
  `34685bed33422505763d31ef8f86837a1139fd5aaf2946a9adcbfa9dd1cd9a35`.
- Registry aggregate:
  `832cc96192c72b89472964e030893ac4c01bcc0d20eb21f7e935b7a7c6288658`.

This contract records the proposed Phase 2 execution rules. It does not approve
the remediated source baseline and does not create implementation acceptance.

## 2. Big-bang change-set boundary

All 24 BRD and 7 UXF documents form one document-baseline change set. Work may
use automated internal checkpoints, but no individual domain or document may
be frozen, committed as an accepted sub-baseline, or human-accepted separately.
The 31 documents move together through:

```text
V2.3_DRAFT → V2.3_CANDIDATE → V2.3_FROZEN
```

A `V2.3_CANDIDATE` is prohibited while any temporary key, required active
acceptance gap, unsigned Human Decision Pack, or open criticality exception
remains.

## 3. Authority and source model

Authority is applied in this order:

1. Human-approved v2.3 decisions, including `P2D-01` through `P2D-14`.
2. Corrected BRD business meaning.
3. UXF aligned with corrected BRD.
4. Generated JSON registry projection.

The visible Markdown Requirement Block is authoritative. JSON is generated
from Markdown and must never silently override it. Legacy wording remains in
Git history and explicit change provenance; it is not copied into a second
competing normative source.

## 4. Stable Requirement ID contract

- Preserve all 576 current IDs.
- Assign the 609 active temporary keys the candidate IDs in
  `stable-id-mapping-candidate.json`.
- Reserve `BRD-CAP-INDEX-R029` for the new active `DATA_REQUIREMENT` selected
  by P2-DEC-005.
- Reserve `UXF-05-R054` for the new active `UX_REQUIREMENT` selected by
  P2-DEC-007.
- Keep the two reservations in `new_requirement_allocations`; they are not
  temporary-key mappings, so the temporary mapping count remains 609.
- Preserve the numeric suffix and origin document code; do not compact gaps.
- Preserve each temporary key in `previous_keys` provenance.
- Do not assign IDs to 157 retired temporary-key tombstones.
- Do not reuse existing, alias, composite-parent, retired, or planned IDs.
- An ID is type-neutral and remains stable when classification, scope,
  lifecycle, or current owning document changes without changing identity.
- Alias and composite-parent IDs remain their existing IDs.

## 5. Standard document front matter

Every remediated source document must begin with YAML front matter containing
exactly one value for each required field:

```yaml
---
schema_version: "<schema-version>"
document_code: <stable-document-code>
title: <document-title>
product_baseline: "2.3"
document_revision: "<document-revision>"
lifecycle_status: V2.3_DRAFT
language: vi-VN | en
authority: <authority-token>
supersedes: <historical-baseline-reference-or-null>
requirement_block_schema: YSIM-REQUIREMENT-BLOCK-1.0
---
```

BRD uses `vi-VN`; UXF uses `en`. `product_baseline` and `document_revision`
are separate. A document revision must not be used as a product version.

## 6. Requirement Block lexical grammar

Markers are visible HTML comments and must be on their own lines:

```text
<!-- YSIM:REQUIREMENT BEGIN -->
...one requirement block...
<!-- YSIM:REQUIREMENT END -->
```

Blocks must not nest. One begin marker has exactly one following end marker.
The block contains one stable Requirement ID and one record kind. Field labels
are case-sensitive. Enumerated tokens are case-sensitive. Unknown mandatory
fields fail validation; extension fields require a schema revision.

Conceptual grammar:

```ebnf
requirement-block = begin-marker, heading, common-fields, kind-fields,
                    end-marker ;
begin-marker      = "<!-- YSIM:REQUIREMENT BEGIN -->" ;
end-marker        = "<!-- YSIM:REQUIREMENT END -->" ;
heading           = "### Requirement ", requirement-id, " — ", title ;
record-kind       = "CANONICAL_ATOMIC" | "ALIAS" | "COMPOSITE_PARENT" ;
scope-status      = "V2.3_ACTIVE" | "FUTURE" | "DEFERRED" |
                    "OUT_OF_SCOPE" ;
criticality       = "CRITICAL" | "HIGH" | "NORMAL" ;
change-class      = "EDITORIAL" | "CLARIFICATION" | "SCOPE_UPDATE" |
                    "SEMANTIC_CHANGE" | "SPLIT" | "MERGE" | "ALIAS" ;
acceptance-scope  = "REQUIRED_FOR_V2.3" |
                    "NOT_APPLICABLE_FOR_V2.3" ;
```

The title is navigation metadata only. Requirement ID and normative statement
are authoritative. Title text is excluded from semantic fingerprints.

## 7. Canonical active atomic block

The following is a schema template, not real acceptance content:

```markdown
<!-- YSIM:REQUIREMENT BEGIN -->
### Requirement <STABLE-ID> — <Non-normative title>

- Record Kind: `CANONICAL_ATOMIC`
- Requirement Type: `<classification>`
- Scope Status: `V2.3_ACTIVE`
- Delivery Commitment: `REQUIRED`
- Verification Criticality: `CRITICAL|HIGH|NORMAL`
- Lifecycle Status: `V2.3_DRAFT`
- Acceptance Applicability: `REQUIRED_FOR_V2.3`
- Change Classification: `EDITORIAL|CLARIFICATION|SCOPE_UPDATE|SEMANTIC_CHANGE|SPLIT|MERGE`
- Change Provenance: `<approved-decision-or-editorial-provenance>`
- Previous Keys: `<temporary-key-list-or-empty>`

#### Normative Statement

<One authoritative normative statement.>

#### Acceptance Contract

- Acceptance ID: `<GLOBALLY-UNIQUE-AC-ID>`
- Verification Mode: `<BUSINESS_CONTRACT|API|DATA|RUNTIME|JOURNEY|ACCESSIBILITY|PERFORMANCE>`
- Required Evidence: `<runtime|api|data|screenshot|document list>`
- Observable Criterion: `<observable pass/fail outcome>`
- Non-applicable Risk Dimensions: `<dimension and rationale, or NONE>`
<!-- YSIM:REQUIREMENT END -->
```

Every `V2.3_ACTIVE` canonical atomic unit has delivery commitment `REQUIRED`.
Criticality never makes a requirement optional. Acceptance IDs are globally
unique across all 31 documents. Multiple criteria repeat the five Acceptance
Contract fields as a complete criterion group; no orphan criterion is allowed.

Risk-tier requirements:

- `CRITICAL`: positive and negative/fail-closed criteria, plus applicable
  recovery, retry, idempotency, concurrency, and authorization boundaries.
- `HIGH`: expected path and primary failure or edge path.
- `NORMAL`: at least one observable pass/fail criterion.
- Criteria must not be padded. A non-applicable dimension requires rationale.

BRD criteria remain at observable business or contract boundaries. UXF criteria
remain at journey, state, accessibility, or performance outcomes. Database,
framework, internal class, or topology details are prohibited unless already
an approved constraint.

## 8. Existing-ID and newly assigned-ID forms

An existing-ID requirement uses the active block without a temporary key:

```markdown
- Previous Keys: `[]`
- Change Provenance: `EXISTING_ID_PRESERVED_FROM_FC2`
```

A newly assigned stable-ID requirement uses the exact mapping candidate:

```markdown
- Previous Keys: `[TMP-<ORIGIN-DOCUMENT-CODE>-<NNN>]`
- Change Provenance: `P2D-02; stable-id-mapping-candidate.json`
```

These are provenance differences only; both use the same canonical atomic
grammar and neither form receives semantic priority over the other.

## 9. Canonical inactive atomic block

```markdown
<!-- YSIM:REQUIREMENT BEGIN -->
### Requirement <STABLE-ID> — <Non-normative title>

- Record Kind: `CANONICAL_ATOMIC`
- Requirement Type: `<classification>`
- Scope Status: `FUTURE|DEFERRED|OUT_OF_SCOPE`
- Delivery Commitment: `NOT_COMMITTED_FOR_V2.3`
- Verification Criticality: `NOT_ASSIGNED_FOR_V2.3`
- Lifecycle Status: `V2.3_DRAFT`
- Acceptance Applicability: `NOT_APPLICABLE_FOR_V2.3`
- Scope Rationale: `<source-explicit or approved-decision rationale>`
- Change Classification: `EDITORIAL|CLARIFICATION|SCOPE_UPDATE|SEMANTIC_CHANGE|SPLIT|MERGE`
- Change Provenance: `<approved-decision-or-editorial-provenance>`
- Previous Keys: `<temporary-key-list-or-empty>`

#### Normative Statement

<One authoritative normative scope statement.>
<!-- YSIM:REQUIREMENT END -->
```

Inactive blocks contain no implementation Acceptance ID and are excluded from
the v2.3 acceptance gap. Reactivation requires a documented Acceptance Contract
before candidate status.

## 10. Alias block

```markdown
<!-- YSIM:REQUIREMENT BEGIN -->
### Requirement <EXISTING-ALIAS-ID> — <Non-normative title>

- Record Kind: `ALIAS`
- Alias Of: `<CANONICAL-ACTIVE-ID>`
- Implementation Unit: `false`
- Acceptance Unit: `false`
- Scope Coverage Unit: `false`
- Coverage Mode: `CANONICAL`
- Lifecycle Status: `V2.3_DRAFT`
- Change Classification: `ALIAS`
- Change Provenance: `<approved-reconciliation-record>`

#### Historical Statement

<Preserved source statement.>
<!-- YSIM:REQUIREMENT END -->
```

Alias targets must be active canonical units. Alias chains and cycles are
invalid. Alias blocks contain no duplicated acceptance criteria.

## 11. Composite-parent block

```markdown
<!-- YSIM:REQUIREMENT BEGIN -->
### Requirement <EXISTING-COMPOSITE-ID> — <Non-normative title>

- Record Kind: `COMPOSITE_PARENT`
- Coverage Mode: `ALL_CHILDREN`
- Children: `[<CANONICAL-ACCEPTANCE-UNIT-ID>, ...]`
- Implementation Unit: `false`
- Acceptance Unit: `false`
- Lifecycle Status: `V2.3_DRAFT`
- Change Classification: `<approved classification>`
- Change Provenance: `<approved reconciliation record>`

#### Normative Composite Statement

<Preserved composite statement.>
<!-- YSIM:REQUIREMENT END -->
```

Every child must exist, be a canonical acceptance unit, and reciprocally name
the parent where the registry schema requires it. Alias and retired keys are
invalid children. Composite parents contain no duplicated acceptance.

## 12. Tombstones

Retired temporary keys exist only in the generated registry tombstone ledger.
They do not receive stable IDs and must not produce active source blocks. Each
tombstone preserves source evidence, historical derivation, retirement reason,
and `SUPERSEDED_BY` where applicable. A retired key can never be reused.

## 13. Controlled statement rewrite

`EDITORIAL` changes preserve meaning and require traceable editorial provenance.
All other change classifications require approved provenance. `SEMANTIC_CHANGE`,
`SPLIT`, `MERGE`, and changes of identity block remediation unless explicitly
approved. Stable ID remains when identity is unchanged. Acceptance must never
be invented to resolve ambiguous business meaning.

## 14. Criticality and exception workflow

The preflight projection applies P2D-05 rules to every `V2.3_ACTIVE` canonical
atomic unit, including the two selected split allocations. The current
projection is `CRITICAL 313`, `HIGH 409`, and `NORMAL 348` across 1,070 active
units. Every cross-tier, borderline, or override case is listed in
`PHASE_2_CRITICALITY_EXCEPTION_REGISTER.md` with status `OPEN`. An automated
proposal does not resolve the exception. Human disposition must preserve the
requirement's `REQUIRED` commitment.

## 15. Decision Register workflow

All ten semantic decisions have selected option 1 and are recorded as
`DECIDED_PENDING_PACK_APPROVAL`. Open semantic decision count is zero, but the
selection has no approved effect until
`PHASE_2_HUMAN_DECISION_PACK.md` is signed directly. The next gate is
`HUMAN_DECISION_PACK_APPROVAL`; no final candidate is allowed while the pack
remains pending.

## 16. Internal checkpoints

At minimum, automated checkpoints must validate:

1. All 31 canonical source blobs were read and match FC2 hashes.
2. All source documents have standard front matter.
3. Every normative record has one valid Requirement Block.
4. No active temporary key remains after ID application.
5. Alias, composite, and tombstone invariants remain reciprocal and unique.
6. Every active canonical atomic unit has documented risk-tiered acceptance.
7. Every inactive unit has rationale and no implementation Acceptance ID.
8. Human Decision Pack is signed and the criticality exception register is
   fully reviewed before candidate.
9. JSON projection regenerates byte-deterministically from source Markdown.
10. BRD/UXF move through lifecycle as one baseline.

## 17. Stop and approval conditions

Phase 2A stops after the selected Human Decision Pack and recomputed preflight
artifacts are staged for direct Markdown approval. It does not edit BRD/UXF,
add real source acceptance criteria, approve the pack, review or approve a
criticality exception, create a candidate, or authorize implementation.
