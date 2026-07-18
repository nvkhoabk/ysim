#!/usr/bin/env python3
"""Deterministically render the VS001 implementation decision C1 candidate."""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs/baselines/v2.3/phase-2d/vs001-implementation-decision-c1.json"
MARKDOWN = ROOT / "docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_DECISION_C1_CANDIDATE.md"
MANIFEST = ROOT / "docs/baselines/v2.3/phase-2d/vs001-implementation-decision-c1-manifest.json"
BUILDER = ROOT / "scripts/docs/build-phase-2d-vs001-implementation-decision-c1.py"
VALIDATOR = ROOT / "scripts/docs/validate-phase-2d-vs001-implementation-decision-c1.py"
TESTS = ROOT / "scripts/docs/tests/test-phase-2d-vs001-implementation-decision-c1.py"

# Deliberate mutation switches used only by isolated adversarial tests.
INJECT_OMIT_DECISION = False
INJECT_GENERIC_OPTION = False
INJECT_REORDER = False
INJECT_FALSE_RUNTIME = False
INJECT_OMIT_AUDIT = False
INJECT_IMPLEMENTATION_TRUE = False


def canonical_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_sha(value: object) -> str:
    return sha(canonical_bytes(value))


def aggregate(records: list[dict[str, str]]) -> str:
    return canonical_sha(sorted(records, key=lambda item: item["path"]))


def projection(kind: str, identity: str, value: object) -> list[str]:
    return [f"<!-- {kind}:{identity} -->", "```json", canonical_bytes(value).decode().rstrip("\n"), "```", ""]


def render(payload: dict) -> bytes:
    data = deepcopy(payload)
    decisions = list(data["decisions"])
    if INJECT_OMIT_DECISION:
        decisions = decisions[:-1]
    if INJECT_REORDER:
        decisions = list(reversed(decisions))
    if INJECT_GENERIC_OPTION:
        decisions[0] = deepcopy(decisions[0])
        decisions[0]["options"][0]["contract"] = "The implementation works as expected."
    if INJECT_FALSE_RUNTIME:
        data["runtime_evidence_status"] = "PASS"
    if INJECT_IMPLEMENTATION_TRUE:
        data["implementation_authorized"] = True

    lines = [
        "# VS001 Implementation Decision C1 Candidate",
        "",
        f"- Candidate: `{data['candidate_id']}`",
        f"- Status: `{data['status']}`",
        f"- Approval: `{data['approval']}`",
        f"- Governing commit: `{data['governing_commit']}`",
        f"- Implementation authorized: `{str(data['implementation_authorized']).lower()}`",
        f"- Runtime evidence: `{data['runtime_evidence_status']}`",
        f"- Implementation contract created: `{str(data['implementation_contract_created']).lower()}`",
        f"- Next gate: `{data['next_gate']}`",
        "",
        data["purpose"],
        "",
        "## Authority objects",
        "",
        "| Authority | Commit | Git path | Blob | SHA-256 | Role |",
        "|---|---|---|---|---|---|",
    ]
    for item in data["authority_objects"]:
        lines.append(f"| `{item['authority_id']}` | `{item['commit']}` | `{item['path']}` | `{item['blob_oid']}` | `{item['sha256']}` | {item['role']} |")
    lines.extend(["", "## Accepted authority reconciliation", ""])
    rec = data["authority_reconciliation"]
    lines.extend([
        f"- Requirements: `{rec['requirements_total']}`",
        f"- Retained contracts: `{rec['retained_contracts']}`",
        f"- Elaborated contracts: `{rec['elaborated_contracts']}`",
        f"- Source obligations: `{rec['source_obligations']}`",
        f"- Acceptance criteria: `{rec['acceptance_criteria']}`",
        f"- Decision clauses: `{rec['decision_clauses']}`",
        "",
        "## Technical decision audit",
        "",
        "| ID | Topic | Class | Disposition | Decision |",
        "|---|---|---|---|---|",
    ])
    audit = [] if INJECT_OMIT_AUDIT else data["technical_decision_audit"]
    for item in audit:
        decision = f"`{item['decision_id']}`" if item["decision_id"] else "—"
        lines.append(f"| `{item['audit_id']}` | {item['topic']} | `{item['classification']}` | {item['disposition']} | {decision} |")
    lines.extend(["", "## Human decisions", ""])
    for decision in decisions:
        lines.extend([
            f"### {decision['decision_id']} — {decision['title']}",
            "",
            f"- Classification: `{decision['classification']}`",
            f"- Selected option: `{decision['selected_option']}`",
            f"- Recommended option: `{decision['recommended_option']}`",
            f"- Question: {decision['question']}",
            f"- Why human: {decision['why_human']}",
            f"- Source authorities: {', '.join(f'`{x}`' for x in decision['source_authorities'])}",
            f"- Impacted acceptance: {', '.join(f'`{x}`' for x in decision['impacted_acceptance'])}",
            "",
        ])
        for option in decision["options"]:
            lines.extend([
                f"#### {option['option_id']}",
                "",
                f"- Summary: {option['summary']}",
                f"- Contract: {option['contract']}",
                f"- Impact: {option['impact']}",
                f"- Rejection tradeoff: {option['rejection_tradeoff']}",
                "",
            ])
        lines.extend([
            f"Recommendation rationale: {decision['recommendation_rationale']}",
            "",
            "Non-inferences:",
            "",
            *[f"- {item}" for item in decision["non_inferences"]],
            "",
        ])
    lines.extend([
        "## Implementation-contract blocker",
        "",
        f"- Code: `{data['implementation_contract_blocker']['code']}`",
        f"- Reason: {data['implementation_contract_blocker']['reason']}",
        f"- Required resolution: {data['implementation_contract_blocker']['required_resolution']}",
        f"- Smallest next step: {data['implementation_contract_blocker']['smallest_next_step']}",
        "",
        "## Reused technical foundation",
        "",
        *[f"- {item}" for item in data["technical_foundation_reuse"]],
        "",
        "## Non-claims",
        "",
        *[f"- `{item}`" for item in data["non_claims"]],
        "",
        "## Independent machine-readable projections",
        "",
    ])
    metadata = {key: data[key] for key in [
        "candidate_id", "status", "approval", "implementation_authorized", "runtime_evidence_status",
        "implementation_contract_created", "governing_commit", "next_gate",
    ]}
    lines.extend(projection("METADATA_JSON", data["candidate_id"], metadata))
    lines.extend(projection("RECONCILIATION_JSON", "ACCEPTED_AUTHORITY", data["authority_reconciliation"]))
    lines.extend(projection("AUDIT_JSON", "TECHNICAL_DECISION_AUDIT", audit))
    for decision in decisions:
        lines.extend(projection("DECISION_JSON", decision["decision_id"], decision))
    lines.extend(projection("BLOCKER_JSON", "IMPLEMENTATION_CONTRACT", data["implementation_contract_blocker"]))
    lines.extend(projection("NON_CLAIMS_JSON", "IMPLEMENTATION_DECISION_C1", data["non_claims"]))
    return ("\n".join(lines).rstrip("\n") + "\n").encode()


def main() -> None:
    payload = json.loads(SOURCE.read_bytes())
    markdown = render(payload)
    MARKDOWN.write_bytes(markdown)
    hash_paths = [SOURCE, MARKDOWN, BUILDER, VALIDATOR, TESTS]
    file_hashes = {str(path.relative_to(ROOT)): sha(path.read_bytes()) for path in hash_paths}
    generated_records = [
        {"path": str(SOURCE.relative_to(ROOT)), "sha256": file_hashes[str(SOURCE.relative_to(ROOT))]},
        {"path": str(MARKDOWN.relative_to(ROOT)), "sha256": file_hashes[str(MARKDOWN.relative_to(ROOT))]},
    ]
    manifest = {
        "candidate_id": payload["candidate_id"],
        "status": payload["status"],
        "approval": payload["approval"],
        "implementation_authorized": payload["implementation_authorized"],
        "runtime_evidence_status": payload["runtime_evidence_status"],
        "implementation_contract_created": payload["implementation_contract_created"],
        "next_gate": payload["next_gate"],
        "decisions": len(payload["decisions"]),
        "selected_options": sum(item["selected_option"] is not None for item in payload["decisions"]),
        "options_per_decision": 3,
        "type_c_blockers": len(payload["decisions"]),
        "working_file_sha256": file_hashes,
        "generated_payload_aggregate": aggregate(generated_records),
        "self_reference_policy": "MANIFEST_HASH_AND_GIT_TREE_ARE_DETACHED_GATE_OUTPUTS",
        "staged_tree": None,
        "git_content_aggregate": None,
    }
    MANIFEST.write_bytes(canonical_bytes(manifest))


if __name__ == "__main__":
    main()
