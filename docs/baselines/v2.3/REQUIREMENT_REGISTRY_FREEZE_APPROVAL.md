# Requirement Registry Freeze Approval History

## V23-REQ-REGISTRY-FC1 — Revision 1

- Candidate ID: `V23-REQ-REGISTRY-FC1`
- Approval revision: `1`
- Historical decision: `APPROVED`
- Historical authorized approver: `Khoa, Nguyen`
- Historical signature: `Khoa, Nguyen`
- Approval date: `2026-07-14`
- Timezone: `Asia/Ho_Chi_Minh`
- Revision status: `SUPERSEDED`
- Superseded by: `V23-REQ-REGISTRY-FC1 revision 2`
- Supersession reason: staged `git diff --check` detected one extra blank line at EOF.
- Previous manifest SHA-256: `d596e556125af8e8a8fc3e089489d0e6773e505ec39a36ffc22d0ee302057017`
- Formatting-only correction: normalized EOF from `7d 0a 0a` to `7d 0a`.

## V23-REQ-REGISTRY-FC1 — Revision 2

- Candidate ID: `V23-REQ-REGISTRY-FC1`
- Approval revision: `2`
- Historical decision: `APPROVED`
- Historical authorized approver: `Khoa, Nguyen`
- Historical signature: `Khoa, Nguyen`
- Approval date: `2026-07-14`
- Timezone: `Asia/Ho_Chi_Minh`
- Revision status: `SUPERSEDED`
- Superseded by: `V23-REQ-REGISTRY-FC2`
- Supersession reason: FC1 failed required clean-checkout source-hash verification.
- Root cause: raw CRLF working-tree source hashes were not reproducible from canonical LF Git blobs for 28 of 31 source documents.
- Corrected FC1 manifest SHA-256: `225b7e36096cff05576e140c17340e434789f34a7d22b0aaf657ceaf5344f6ea`
- FC1 source aggregate hash: `8be7aa7754ac5c439152b0d5ee1b2acafaef73eafcbdfe0cfef94582c1aa5e7b`
- FC1 registry aggregate hash: `92b17301fa03ba59ecde6b950b15e01cc3e3b98e8ac4043b021fa0d79d355b82`
- Semantic payload changed by EOF correction: `NO`

FC1 approval does not transfer automatically to FC2.

## V23-REQ-REGISTRY-FC2 — Pending Human Approval

- Candidate ID: `V23-REQ-REGISTRY-FC2`
- Baseline kind: `RECONCILED_REQUIREMENT_REGISTRY`
- Approval model: `DETACHED_MARKDOWN_APPROVAL`
- Status: `PENDING`
- Decision: `PENDING`
- Authorized Approver: `PENDING`
- Signature: `PENDING`
- Date: `PENDING`
- Source Git commit: `7f16d4c4b8ab514bd45de184f65ace221b03f4db`
- Source hash basis: `GIT_BLOB_CONTENT_AT_SOURCE_COMMIT`
- Line-ending semantics: `GIT_CANONICAL_TEXT`
- Manifest SHA-256: `ec9c6afc86a45e1465e674b7e1278113b296470ef82d2c36f5c0fb9b54cbba78`
- Source aggregate hash: `34685bed33422505763d31ef8f86837a1139fd5aaf2946a9adcbfa9dd1cd9a35`
- Registry aggregate hash: `832cc96192c72b89472964e030893ac4c01bcc0d20eb21f7e935b7a7c6288658`

FC2 requires human review against its new manifest and canonical Git-blob hashes. No FC1 approver name, signature, decision, or effective approval is carried forward to FC2.

## FC2 Review Scope

- Review the Phase 1C reconciled requirement registry baseline.
- Review the source inventory, extraction/reconciliation results, identity mappings, alias/composite/retired-key decisions, scope classifications, and traceability.
- Review the canonical Git-blob source hash contract and the FC2 aggregate hashes.
- If separately approved by a human, allow this baseline to be committed as controlled input for the BRD/UXF correction phase.

## Explicit Non-Claims

- Not final BRD/UXF v2.3 approval.
- Not a final acceptance baseline.
- Not architecture approval.
- Not implementation authorization.
- Does not declare temporary keys to be final canonical Requirement IDs.

## Acknowledged Known Gaps

- 609 active temporary keys.
- 1174 acceptance units remain `INFERRED_ONLY`.
- 15 documentation findings remain open for source correction.
- BRD/UXF v2.2 source content still requires correction and approval for v2.3.
