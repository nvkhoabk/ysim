---
document_code: V3-R1-G00-S02-README
document_name: Governance Requirements Baseline Checkpoint Index
project: YSim v3
document_set: V3-R1-G00-S02
version: 0.1.0-candidate.1
status: FROZEN
language: en
---
# V3-R1 G00 S02 — Governance Requirements Baseline

This checkpoint preserves the Human-Accepted Governance Requirements Baseline
candidate byte-for-byte and records acceptance separately. It is stacked on
`V3-R1-G00-S01` at commit
`3afc37eb366769603f7a898c53432c444f50726a`, tree
`217db32ea46636a40bc0aa611c653836e461b6de`.

## Controlled documents

- [Governance Requirements Baseline Artifact Wrapper](governance-requirements-baseline.md)
  — governed integration/index metadata; the wrapper was not Human-Accepted.
- [Immutable accepted candidate](../../../../../factory/releases/v3-r1-g00-s02-governance-requirements-baseline/YSim_V3_R1_G00_S02_Governance_Requirements_Baseline_v0.1.0-candidate.1.md)
  — exact `28555` bytes with SHA-256
  `f3aa80a23a1ab95ab9914263d8c79bf11fc466579f162c79d0302cbfa77c9a77`;
  Human Acceptance binds only these raw bytes.
- [Acceptance Receipt](acceptance-receipt.yaml) — out-of-band Human Acceptance
  binding; it does not alter the candidate.
- [Package Specification](package-spec.yaml) — machine-readable scope,
  environment, baseline and mutation contract.
- [Manifest](MANIFEST.sha256) — SHA-256 coverage for every S02 payload and
  validation file except the manifest itself.
- [Governing standards provenance](standards/standards-provenance.yaml) — exact
  authoritative DOCX identity, deterministic extraction method and checksummed
  PCS/ENG/ENV bindings. The readable extracts are
  [YSIM-PCS-001 v1.27.1](standards/04_RELEASE_STANDARD_1.27.1.txt),
  [YSIM-ENG-001 v1.0.1](standards/05_ENGINEERING_AND_CODE_GENERATION_STANDARD_1.0.1.txt),
  and [YSIM-ENV-001 v3.2.1](standards/06_ENVIRONMENT_STANDARD_3.2.1.txt).
  Neither the extracts nor this repository binding was Human-Accepted.

## Validation

From the canonical WSL repository root:

```bash
PYTHONPATH=tools/ysf/src python tools/ysf/src/ysf/governance_baseline/validator.py \
  --snapshot-contract /tmp/ysim-v3-r1-g00-s02-final-snapshot.yaml \
  --json
```

The external snapshot contract is mandatory and has no default. It binds the
exact repository origin, branch, base, corrective parent, final head/tree,
commit topology, 15 changed paths and Git modes, plus both authoritative input
files and the complete standards extraction/redaction contract. The public API
and CLI compare independently observed Git and filesystem evidence against the
same exact contract and fail closed on any mismatch.

Authoritative verification always reads and hashes both the DOCX and its input
manifest through no-follow regular-file descriptors. The ENV extract preserves
the normative sandbox-recipient limitation from source block 700 while
replacing exactly three personal-mailbox values, in source order, with
deterministic ordinal markers. The provenance file specifies the reproduction
algorithm and does not retain those source values.

## Safety boundary

This checkpoint is documentation and deterministic validation only. It does
not authorize merge, tag, release, deployment, production activation,
provider execution, payment, fulfillment, customer communication, scheduler
execution, or any other business external effect. Safe stop is to preserve the
Draft PR and take no promotion action.
