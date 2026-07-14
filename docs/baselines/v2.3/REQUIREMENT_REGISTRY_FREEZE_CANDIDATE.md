# Requirement Registry Freeze Candidate — Phase 1D

- Candidate ID: `V23-REQ-REGISTRY-FC2`
- Supersedes: `V23-REQ-REGISTRY-FC1`
- Baseline kind: `RECONCILED_REQUIREMENT_REGISTRY`
- Status: `CANDIDATE`
- Approval status: `PENDING_HUMAN_APPROVAL`
- Branch: `rebuild/v2.3-foundation`
- Source Git commit: `7f16d4c4b8ab514bd45de184f65ace221b03f4db`
- Generated on: `2026-07-14`

## Purpose

This Phase 1D candidate records the final audit of the completed Phase 1C BRD/UXF requirement extraction and reconciliation baseline. It provides a reproducible review payload for human approval without approving the underlying BRD/UXF content for implementation.

## FC1 Supersession and FC2 Repair

FC2 supersedes FC1. FC1 failed the required clean-checkout verification because its source hashes were calculated from raw working-tree bytes: 28 of 31 source files used CRLF in the main working tree, while their canonical Git blobs used LF. The main working-tree validation therefore passed, but a clean checkout could not reproduce 28 source hashes.

FC2 changes only the source hash contract. It hashes canonical Git blob content at source commit `7f16d4c4b8ab514bd45de184f65ace221b03f4db` with `source_hash_basis=GIT_BLOB_CONTENT_AT_SOURCE_COMMIT` and `line_ending_semantics=GIT_CANONICAL_TEXT`. Requirement extraction/reconciliation semantics, identities, scope, alias/composite/retired mappings, acceptance classifications, and counts are unchanged.

## Freeze Scope

The candidate freezes only:

- the source inventory used by extraction;
- extraction and reconciliation results;
- the current identity mapping;
- alias, composite, equivalence-class, and retired-key decisions;
- the current scope classification;
- traceability to source evidence;
- deferred documentation findings for the BRD/UXF correction phase.

## What This Candidate Does Not Approve

This candidate is not:

- the final BRD/UXF v2.3 freeze;
- the final acceptance baseline;
- architecture approval;
- implementation authorization;
- a declaration that active temporary keys are final canonical Requirement IDs.

## Source Baseline

The 31 source documents originate in the Architecture Baseline v2.2 documentation set. Under the v2.3 document baseline, BRD is `ADOPTED` as a business source and UXF is `DRAFT_REVIEW`; both still require the applicable v2.3 correction and approval work. This candidate hashes canonical Git blob bytes at the declared source commit and does not hash or approve working-tree representations of those documents.

Source inventory:

- BRD: **24 files**
- UXF: **7 files**
- Total: **31 files**

## Exact Audited Counts

| Metric | Count |
|---|---:|
| Active registry entries | 1185 |
| Canonical atomic requirements | 1174 |
| Implementation units | 1174 |
| Acceptance units | 1174 |
| Scope coverage units | 1174 |
| Active records with current/canonical IDs | 576 |
| Active temporary keys | 609 |
| Composite parents | 2 |
| Aliases | 9 |
| Retired temporary keys | 157 |
| Documentation findings | 15 |
| Unresolved records | 0 |
| Documented acceptance | 0 |
| Acceptance gap | 1174 |

The scope distribution totals **1174**, matching the canonical atomic scope-coverage count. The acceptance distribution totals **1174**, matching the acceptance-unit count.

## Reconciliation Result

- Validator result: `VALID_READY_TO_FREEZE`
- `unresolved_records`: empty
- Computed `ready_to_freeze`: `true`
- Duplicate canonical IDs: 0
- Duplicate active temporary keys: 0
- Dangling requirement references: 0
- Alias chains/cycles: 0
- Retired-key reuse: 0

Readiness means that the Phase 1C reconciliation payload is internally ready for freeze-candidate review. It does not remove the known blockers for final BRD/UXF freeze.

## Identity Model

- **Current/canonical IDs — 576:** active entries carrying existing source-backed Requirement IDs. This count includes source IDs preserved on alias records; canonical ownership remains defined by the alias mapping.
- **Active temporary keys — 609:** active traceable identities that must receive stable Requirement IDs in a later phase.
- **Canonical atomic requirements — 1174:** independent implementation/scope-coverage units after excluding aliases and non-atomic composite parents.
- **Composite parents — 2:** non-atomic parents using reciprocal `ALL_CHILDREN` coverage.
- **Aliases — 9:** non-implementation, non-acceptance, non-scope-coverage records pointing directly to active canonical units.
- **Retired temporary keys — 157:** ledger-preserved historical identities that are inactive and cannot be reused.

## Scope Status Distribution

Distribution across canonical atomic scope-coverage units:

| Scope status | Count |
|---|---:|
| `V2.3_ACTIVE` | 1068 |
| `FUTURE` | 74 |
| `DEFERRED` | 15 |
| `OUT_OF_SCOPE` | 17 |
| `UNCLEAR` | 0 |
| **Total** | **1174** |

## Lifecycle Distribution

Distribution across all active registry entries:

| Lifecycle status | Count |
|---|---:|
| `FROZEN` | 1020 |
| `DRAFT` | 165 |
| `CURRENT` | 0 |
| `DEPRECATED` | 0 |
| `SUPERSEDED` | 0 |
| `UNCLEAR` | 0 |
| **Total** | **1185** |

The source lifecycle values are retained historical/document states; they are not Phase 1D approval states.

## Requirement-Type Distribution

| Requirement type | Count |
|---|---:|
| `ACCESSIBILITY_REQUIREMENT` | 8 |
| `BUSINESS_DECISION` | 177 |
| `BUSINESS_REQUIREMENT` | 367 |
| `BUSINESS_RULE` | 14 |
| `DATA_REQUIREMENT` | 149 |
| `DESIGN_PRINCIPLE` | 18 |
| `INTEGRATION_REQUIREMENT` | 54 |
| `OPERATIONAL_REQUIREMENT` | 77 |
| `PERFORMANCE_REQUIREMENT` | 4 |
| `PRIVACY_REQUIREMENT` | 9 |
| `SCOPE_CONSTRAINT` | 116 |
| `SECURITY_REQUIREMENT` | 60 |
| `UX_REQUIREMENT` | 132 |
| **Total** | **1185** |

## Acceptance Status and Gap

Distribution across acceptance units:

| Acceptance status | Count |
|---|---:|
| `DIRECT` | 0 |
| `LINKED` | 0 |
| `INFERRED_ONLY` | 1174 |
| `MISSING` | 0 |
| **Total acceptance units** | **1174** |

The acceptance gap is **1174**. `INFERRED_ONLY` is valid extraction/reconciliation metadata for Phase 1C, but every such unit requires documented acceptance before final BRD/UXF freeze.

## Known Gaps and Next-Phase Obligations

The following are not Phase 1C consistency failures, but each blocks final BRD/UXF freeze:

1. The BRD/UXF source content comes from the v2.2 architecture baseline and requires v2.3 correction and approval under its document classification.
2. All **609** active temporary keys must be assigned stable Requirement IDs without reusing retired keys.
3. All **1174** `INFERRED_ONLY` acceptance units must receive documented `DIRECT` or `LINKED` acceptance evidence.
4. All **15** deferred documentation findings must be resolved in the appropriate BRD/UXF correction phase.

## Artifact Inventory

Phase 1C registry/report/QA/reconciliation payload hashed by the manifest:

- `docs/baselines/v2.3/BRD_UXF_INVENTORY.md`
- `docs/baselines/v2.3/REQUIREMENT_REGISTRY_QA.md`
- `docs/baselines/v2.3/REQUIREMENT_REGISTRY_RECONCILIATION.md`
- `docs/baselines/v2.3/REQUIREMENT_REGISTRY_REPORT.md`
- `docs/baselines/v2.3/requirements/brd-requirements.json`
- `docs/baselines/v2.3/requirements/registry-qa.json`
- `docs/baselines/v2.3/requirements/registry-reconciliation.json`
- `docs/baselines/v2.3/requirements/registry-summary.json`
- `docs/baselines/v2.3/requirements/uxf-requirements.json`

Validator payload:

- `scripts/docs/validate-requirement-registry.py`

Phase 1D candidate artifacts, intentionally excluded from the registry aggregate to avoid self-reference:

- `docs/baselines/v2.3/requirements/registry-freeze-manifest.json`
- `docs/baselines/v2.3/REQUIREMENT_REGISTRY_FREEZE_CANDIDATE.md`

The manifest contains the complete lexicographically sorted inventory and individual SHA-256 for all 24 BRD and 7 UXF source documents.

## Reproducible Hash Summary

- Hash algorithm: `SHA-256`
- Source hash basis: `GIT_BLOB_CONTENT_AT_SOURCE_COMMIT`
- Line-ending semantics: `GIT_CANONICAL_TEXT`
- Source aggregate: `34685bed33422505763d31ef8f86837a1139fd5aaf2946a9adcbfa9dd1cd9a35`
- Registry/validator aggregate: `832cc96192c72b89472964e030893ac4c01bcc0d20eb21f7e935b7a7c6288658`

For entries sorted lexicographically by relative POSIX path:

1. For each source document, read canonical blob bytes from `<source_git_commit>:<relative_posix_path>` and hash those bytes with SHA-256.
2. For each registry or validator artifact, hash its raw artifact bytes with SHA-256.
3. Create a UTF-8 record `<path>\0<lowercase_sha256>\n` for each file.
4. Concatenate the records in sorted path order and SHA-256 the concatenated bytes.

`source_aggregate_hash` covers `source_documents`. `registry_aggregate_hash` covers `registry_artifacts` plus `validator_artifacts`. Absolute paths and machine-specific data are excluded.

## Validation Commands

```bash
python3 scripts/docs/validate-requirement-registry.py
python3 scripts/docs/validate-requirement-registry-approval.py --candidate
git diff --check
git diff --name-only -- docs/BRD docs/UXF
git status --short
```

## Human Review Checklist

- [ ] Confirm the candidate scope is limited to the Phase 1C reconciliation payload.
- [ ] Confirm all 24 BRD and 7 UXF source hashes.
- [ ] Confirm exact registry, identity, scope, lifecycle, type, and acceptance counts.
- [ ] Confirm alias, composite, equivalence-class, and retired-key mappings.
- [ ] Confirm `unresolved_records` is empty and readiness is computed rather than asserted.
- [ ] Confirm the 609 active temporary keys remain a next-phase obligation.
- [ ] Confirm the 1174 inferred-only acceptance units remain a final-freeze blocker.
- [ ] Confirm all 15 documentation findings remain visible.
- [ ] Confirm no architecture or implementation approval is implied.

## Human Approval

- Status: PENDING
- Authorized Approver: PENDING
- Decision: PENDING
- Date: PENDING
- Signature: PENDING
