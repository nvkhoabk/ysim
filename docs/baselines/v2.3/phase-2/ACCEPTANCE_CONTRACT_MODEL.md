# Acceptance Contract Model Candidate

- Candidate: `V23-P2C-ACCEPTANCE-MODEL-C1`
- Model: `HYBRID_ACCEPTANCE_PROFILES_AND_INLINE_CONTRACTS`
- Version: `1.0.0-candidate.1`
- Status: `CANDIDATE`
- Approval: `PENDING_HUMAN_APPROVAL`
- Base: `0df2d424e00f9cd27b8dcb6645eef827ce97b60e`
- Next gate: `HUMAN_ACCEPTANCE_MODEL_APPROVAL`

## Boundary

This candidate supersedes only the rejected free-text acceptance approach used by Phase 2C C1/C2. It does **not** supersede C2 source remediation, stable-ID mapping/allocation, structural reconciliation, scope decisions, criticality decisions, aliases, composites, or retired-key history. Existing C1/C2 acceptance prose is input evidence only and is not an accepted baseline.

This turn does not regenerate any acceptance block in the 31 BRD/UXF source documents, does not approve the document baseline, and does not authorize YADF implementation.

## Exclusive mechanisms

Every active canonical atomic requirement must receive exactly one mapping disposition:

1. `PROFILE_BINDING_HIGH_CONFIDENCE` — one versioned profile plus complete concrete source-grounded bindings.
2. `INLINE_CONTRACT_REQUIRED` — a complex or unique requirement whose obligations cannot be preserved by a shared profile.
3. `HUMAN_MAPPING_REVIEW` — no guess is made where mapping or binding remains ambiguous.
4. `INVALID_OR_BLOCKED` — source/provenance is insufficient to support either mechanism.

The first two are the eventual exclusive acceptance mechanisms. Review and blocked dispositions are gates, not fallback acceptance contracts.

## Profile-binding decision procedure

High confidence requires all five independent checks: compatible requirement type; semantic structure matching the narrow profile intent; complete typed bindings extracted from the normative statement, full source section, or approved decision; rendered positive/negative/edge oracles that refer to concrete bindings; and semantic audit proving qualifiers, scope, and failure behavior are retained. Keyword presence alone never grants high confidence.

## Inline routing

Fraud/risk, financial reconciliation, payment, pricing, promotion, procurement, allocation, fulfillment, refund, and complex multi-state workflows route to inline authoring when their domain semantics are present. Uncertainty alone does not route inline; it routes human review.

## Non-tautological evidence

Rendered contracts must identify observable business state, rendered UI state/action, security decision, external interaction, operation evidence, or conformance trace. Phrases such as “works as expected” or “requirement is satisfied” are prohibited, and no solution architecture may be inferred.

## Current blocker

`ACCEPTANCE_CONTRACT_MODEL_NOT_APPROVED`
