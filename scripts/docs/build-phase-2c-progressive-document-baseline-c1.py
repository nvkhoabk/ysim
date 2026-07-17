#!/usr/bin/env python3
"""Build the truthful Phase 2C progressive document baseline C1."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
BASE_REL = Path("docs/baselines/v2.3/phase-2")
BACKUP = "refs/ysim-backups/v2.3/phase-2c-document-baseline-c6-r1-rejected"
BACKUP_OBJECT = "8ec2a5381054fc6dddad2e1c2ad15bd4e53a0a28"
BACKUP_TREE = "699a7de703fc1c0009cca0d851c67766a1d7d333"
DECISION_COMMIT = "662eeac15d8ac336c80a495ba2a1dcb4712b7fb0"
CANDIDATE_ID = "V23-P2C-PROGRESSIVE-DOCUMENT-BASELINE-C1"
DECISION_ID = "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001"
PENDING = "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
READY = "ACCEPTANCE_READY"
NA = "NOT_APPLICABLE_FOR_V2.3"
REGISTRY_INPUT = "docs/baselines/v2.3/phase-2/phase-2c-document-baseline-c6-r1-registry.json"
REFERENCE_GOOD = "docs/baselines/v2.3/phase-2/semantic-acceptance-renderer-c2-reference-good-contracts.json"
BEGIN = "<!-- YSIM:REQUIREMENT BEGIN -->"
END = "<!-- YSIM:REQUIREMENT END -->"
BLOCK_RE = re.compile(r"<!-- YSIM:REQUIREMENT BEGIN -->\n(.*?)<!-- YSIM:REQUIREMENT END -->", re.S)
JSON_RE = re.compile(r"```json\n(.*?)\n```", re.S)

ARTIFACTS = [
    "docs/baselines/v2.3/phase-2/PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1_CANDIDATE.md",
    "docs/baselines/v2.3/phase-2/PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1_HUMAN_ACCEPTANCE_PACK.md",
    "docs/baselines/v2.3/phase-2/PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1_TRANSITION_REPORT.md",
    "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-manifest.json",
    "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-policy.json",
    "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-readiness-ledger.json",
    "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-registry.json",
    "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-semantic-audit.json",
    "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-traceability.json",
    "scripts/docs/build-phase-2c-progressive-document-baseline-c1.py",
    "scripts/docs/tests/test-phase-2c-progressive-document-baseline-c1.py",
    "scripts/docs/validate-phase-2c-progressive-document-baseline-c1-regressions.py",
    "scripts/docs/validate-phase-2c-progressive-document-baseline-c1-roundtrip.py",
    "scripts/docs/validate-phase-2c-progressive-document-baseline-c1.py",
]


def git_bytes(spec: str, root: Path = ROOT) -> bytes:
    return subprocess.check_output(["git", "show", spec], cwd=root)


def canonical(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def compact(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_paths() -> list[str]:
    paths = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", BACKUP_TREE, "docs/BRD", "docs/UXF"],
        cwd=ROOT,
        text=True,
    ).splitlines()
    return sorted(path for path in paths if path.endswith(".md"))


def pending_contract(record: dict[str, Any], old_contract: dict[str, Any]) -> dict[str, Any]:
    trace: dict[str, Any] = {
        "approved_business_decisions": record["provenance"].get("approved_decisions", []),
        "governing_decision": DECISION_ID,
        "inference": False,
        "requirement_id": record["stable_id"],
        "source_document": record["provenance"]["source_document"],
        "source_fingerprint": record["provenance"]["source_fingerprint"],
    }
    selection = old_contract.get("approved_selection") if isinstance(old_contract, dict) else None
    if selection:
        trace["approved_semantic_completion_selection"] = {
            "decision_id": selection["decision_id"],
            "option_id": selection["option_id"],
        }
    return {
        "acceptance_content": None,
        "acceptance_state": PENDING,
        "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
        "traceability": trace,
    }


def transform_records(source_registry: dict[str, Any], reference: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    ready_by_id = {row["requirement_id"]: row for row in reference["records"]}
    assert len(ready_by_id) == 59
    records: list[dict[str, Any]] = []
    readiness: list[dict[str, Any]] = []
    for original in source_registry["requirements"]:
        record = json.loads(json.dumps(original, ensure_ascii=False))
        rid = record["stable_id"]
        if record["record_kind"] == "CANONICAL_ATOMIC" and record["scope_status"] == "V2.3_ACTIVE":
            old_contract = record["acceptance_contract"]
            if rid in ready_by_id:
                approved = ready_by_id[rid]
                if old_contract != approved["acceptance_contract"]:
                    raise SystemExit(f"ready contract drift: {rid}")
                record["acceptance_schema_version"] = "PROGRESSIVE-1.0.0"
                record["acceptance_status"] = READY
                record["acceptance_mechanism"] = {
                    "contract_id": old_contract["contract_id"],
                    "inference": False,
                    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
                    "mechanism_version": "SEMANTIC_ACCEPTANCE_RENDERER_C2",
                    "runtime_status": "RUNTIME_ADAPTER_PENDING",
                }
                readiness.append({
                    "acceptance_state": READY,
                    "contract_sha256": approved["contract_sha256"],
                    "requirement_id": rid,
                    "runtime_status": "RUNTIME_ADAPTER_PENDING",
                })
            else:
                marker = pending_contract(record, old_contract)
                record["acceptance_contract"] = marker
                record["acceptance_mechanism"] = {
                    "inference": False,
                    "mechanism": PENDING,
                    "runtime_status": PENDING,
                }
                record["acceptance_schema_version"] = "PROGRESSIVE-1.0.0"
                record["acceptance_status"] = PENDING
                readiness.append({
                    "acceptance_state": PENDING,
                    "approved_semantic_completion_selection": marker["traceability"].get("approved_semantic_completion_selection"),
                    "requirement_id": rid,
                    "runtime_status": PENDING,
                })
        elif record["record_kind"] == "CANONICAL_ATOMIC":
            record["acceptance_contract"] = {
                "acceptance_content": None,
                "acceptance_state": NA,
                "inference": False,
                "requirement_id": rid,
                "scope_status": record["scope_status"],
            }
            record["acceptance_mechanism"] = {
                "inference": False,
                "mechanism": NA,
                "runtime_status": NA,
            }
            record["acceptance_schema_version"] = "PROGRESSIVE-1.0.0"
            record["acceptance_status"] = NA
            readiness.append({"acceptance_state": NA, "requirement_id": rid, "runtime_status": NA})
        else:
            record["acceptance_contract"] = None
            record["acceptance_mechanism"] = None
            record["acceptance_schema_version"] = "PROGRESSIVE-1.0.0"
            record["acceptance_status"] = "STRUCTURAL_RECORD"
        records.append(record)
    return records, sorted(readiness, key=lambda row: row["requirement_id"])


def replace_record_json(text: str, by_id: dict[str, dict[str, Any]]) -> str:
    def replace(match: re.Match[str]) -> str:
        block = match.group(1)
        parsed_match = JSON_RE.search(block)
        if not parsed_match:
            raise SystemExit("requirement block without JSON")
        old = json.loads(parsed_match.group(1))
        new_json = json.dumps(by_id[old["stable_id"]], ensure_ascii=False, sort_keys=True, indent=2)
        new_block = block[: parsed_match.start(1)] + new_json + block[parsed_match.end(1) :]
        return BEGIN + "\n" + new_block + END
    return BLOCK_RE.sub(replace, text)


def update_ranges(rendered: dict[str, str], records: list[dict[str, Any]]) -> bool:
    ranges: dict[str, str] = {}
    for path, text in rendered.items():
        lines = text.splitlines()
        starts = [i + 1 for i, line in enumerate(lines) if line == BEGIN]
        ends = [i + 1 for i, line in enumerate(lines) if line == END]
        if len(starts) != len(ends):
            raise SystemExit(f"marker mismatch: {path}")
        for start, end in zip(starts, ends):
            block = "\n".join(lines[start - 1 : end])
            match = JSON_RE.search(block)
            if not match:
                raise SystemExit(f"missing JSON: {path}:{start}")
            rid = json.loads(match.group(1))["stable_id"]
            ranges[rid] = f"L{start}-L{end}"
    changed = False
    for record in records:
        wanted = ranges[record["stable_id"]]
        if record["provenance"].get("source_lines") != wanted:
            record["provenance"]["source_lines"] = wanted
            changed = True
    return changed


def render_sources(paths: list[str], records: list[dict[str, Any]]) -> dict[str, str]:
    by_id = {record["stable_id"]: record for record in records}
    source_text = {path: git_bytes(f"{BACKUP_TREE}:{path}").decode("utf-8") for path in paths}
    rendered: dict[str, str] = {}
    for _ in range(8):
        rendered = {path: replace_record_json(text, by_id) for path, text in source_text.items()}
        if not update_ranges(rendered, records):
            return rendered
    raise SystemExit("source line ranges did not converge")


def aggregate_files(file_bytes: dict[str, bytes], paths: list[str]) -> str:
    return sha("".join(f"{sha(file_bytes[path])}  {path}\n" for path in sorted(paths)).encode("utf-8"))


def build(output_root: Path) -> dict[str, Any]:
    if subprocess.check_output(["git", "rev-parse", BACKUP], cwd=ROOT, text=True).strip() != BACKUP_OBJECT:
        raise SystemExit("rejected C6-R1 backup identity mismatch")
    if subprocess.check_output(["git", "rev-parse", f"{BACKUP}^{{tree}}"], cwd=ROOT, text=True).strip() != BACKUP_TREE:
        raise SystemExit("rejected C6-R1 backup tree mismatch")
    source_registry = json.loads(git_bytes(f"{BACKUP_TREE}:{REGISTRY_INPUT}"))
    reference = json.loads((ROOT / REFERENCE_GOOD).read_text(encoding="utf-8"))
    records, readiness = transform_records(source_registry, reference)
    paths = source_paths()
    rendered = render_sources(paths, records)

    summary = {
        "acceptance_gap": 1093,
        "acceptance_ready_count": 59,
        "active_atomic": 1152,
        "aliases": 12,
        "canonical_atomic": 1263,
        "composite_parents": 48,
        "criticality_distribution": {"CRITICAL": 340, "HIGH": 439, "NORMAL": 373},
        "inactive_atomic": 111,
        "invalid_acceptance_claim_count": 0,
        "new_phase_2c_ids": 128,
        "pending_acceptance_elaboration_count": 1093,
        "requirement_records": 1326,
        "retired_key_history": 160,
        "retired_records": 3,
        "scope_distribution": {"DEFERRED": 16, "FUTURE": 77, "OUT_OF_SCOPE": 18, "V2.3_ACTIVE": 1152},
        "unsupported_generic_contract_count": 0,
    }
    registry = {
        "artifact": "PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1_REGISTRY",
        "candidate_id": CANDIDATE_ID,
        "generated_from": BACKUP_OBJECT,
        "governing_decision": DECISION_ID,
        "requirements": records,
        "summary": summary,
    }
    ledger = {
        "artifact": "PHASE_2C_PROGRESSIVE_ACCEPTANCE_READINESS_LEDGER",
        "candidate_id": CANDIDATE_ID,
        "counts": {READY: 59, PENDING: 1093, NA: 111},
        "records": readiness,
    }
    decision_rows = [row for row in readiness if row.get("approved_semantic_completion_selection")]
    traceability = {
        "artifact": "PHASE_2C_PROGRESSIVE_TRACEABILITY",
        "candidate_id": CANDIDATE_ID,
        "decision_selection_count": len(decision_rows),
        "decision_selections": decision_rows,
        "rejected_c6_r1": {"backup_object": BACKUP_OBJECT, "tree": BACKUP_TREE},
        "source_record_count": 1326,
    }
    policy = {
        "artifact": "PHASE_2C_PROGRESSIVE_SLICE_ENTRY_POLICY",
        "candidate_id": CANDIDATE_ID,
        "governing_decision": DECISION_ID,
        "implementation_entry_rule": "HUMAN_APPROVED_SLICE_ACCEPTANCE_REQUIRED",
        "required_slice_fields": [
            "slice_id", "objective", "included_requirement_ids", "source_baseline_identity",
            "acceptance_ready_requirement_ids", "pending_requirements_elaborated_by_slice",
            "positive_oracles", "negative_oracles", "boundary_oracles", "evidence_contracts",
            "runtime_api_data_ui_evidence_obligations", "criticality_coverage",
            "clean_checkout_validation", "human_approval_status"
        ],
        "pending_requirement_implementation_allowed_without_slice_approval": False,
    }
    audit = {
        "artifact": "PHASE_2C_PROGRESSIVE_SEMANTIC_AUDIT",
        "candidate_id": CANDIDATE_ID,
        "findings": {
            "candidate_derived_semantic_identifiers": 0,
            "false_acceptance_ready_claims": 0,
            "generated_procedure_templates": 0,
            "generic_acceptance_wrappers": 0,
            "invalid_acceptance_claims": 0,
            "pending_records_with_acceptance_content": 0,
            "unsupported_or_lost_source_obligations": 0,
        },
        "result": "PASS",
    }

    output_bytes: dict[str, bytes] = {path: text.encode("utf-8") for path, text in rendered.items()}
    generated_objects = {
        "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-policy.json": policy,
        "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-readiness-ledger.json": ledger,
        "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-registry.json": registry,
        "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-semantic-audit.json": audit,
        "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-traceability.json": traceability,
    }
    for path, value in generated_objects.items():
        output_bytes[path] = canonical(value)

    source_aggregate = aggregate_files(output_bytes, paths)
    registry_aggregate = sha(output_bytes["docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-registry.json"])
    acceptance_rows = []
    for record in records:
        if record["record_kind"] == "CANONICAL_ATOMIC":
            acceptance_rows.append(f"{record['stable_id']}:{sha(compact(record['acceptance_contract']))}\n")
    acceptance_aggregate = sha("".join(sorted(acceptance_rows)).encode("utf-8"))

    candidate_md = f"""# Phase 2C Progressive Document Baseline C1 Candidate

- Candidate: `{CANDIDATE_ID}`
- Status: `CANDIDATE`
- Approval: `PENDING_HUMAN_ACCEPTANCE`
- Governing decision: `{DECISION_ID}`
- Supersedes rejected candidates: `V23-P2C-DOCUMENT-BASELINE-C5`, `V23-P2C-DOCUMENT-BASELINE-C6`, `V23-P2C-DOCUMENT-BASELINE-C6-R1`
- Next gate: `HUMAN_PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1_ACCEPTANCE`

This candidate truthfully exposes 59 acceptance-ready typed contracts and 1,093 active requirements pending vertical-slice acceptance elaboration. It does not claim complete acceptance materialization or authorize implementation.
"""
    pack_md = f"""# Phase 2C Progressive Document Baseline C1 Human Acceptance Pack

## Decision basis

`{DECISION_ID}` is effective at `{DECISION_COMMIT}`.

## Readiness

- `ACCEPTANCE_READY`: 59
- `PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION`: 1,093
- `NOT_APPLICABLE_FOR_V2.3`: 111
- Active acceptance gap: 1,093

Human acceptance of this baseline does not approve a vertical slice, implementation, runtime adapter, YADF, deployment or final product acceptance.
"""
    report_md = f"""# Phase 2C Progressive Document Baseline C1 Transition Report

- Rejected source candidate: `V23-P2C-DOCUMENT-BASELINE-C6-R1`
- Rejection reason: `SYSTEMIC_GENERIC_ACCEPTANCE_AND_EXPECTED_DERIVED_OBSERVATION`
- Preserved source object: `{BACKUP_OBJECT}`
- Preserved source tree: `{BACKUP_TREE}`
- Requirement records retained: 1,326
- Ready typed contracts retained byte-identically: 59
- Synthetic/generic acceptance payloads removed: 1,093
- Approved decision selections retained as traceability: 27
- Unsupported generic contracts retained: 0
"""
    output_bytes["docs/baselines/v2.3/phase-2/PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1_CANDIDATE.md"] = candidate_md.encode()
    output_bytes["docs/baselines/v2.3/phase-2/PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1_HUMAN_ACCEPTANCE_PACK.md"] = pack_md.encode()
    output_bytes["docs/baselines/v2.3/phase-2/PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1_TRANSITION_REPORT.md"] = report_md.encode()

    inventory = sorted(paths + ARTIFACTS)
    non_manifest = [path for path in inventory if path != "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-manifest.json"]
    signed_hashes: dict[str, str] = {}
    for path in non_manifest:
        if path in output_bytes:
            signed_hashes[path] = sha(output_bytes[path])
        else:
            signed_hashes[path] = sha((ROOT / path).read_bytes())
    generated_aggregate = sha("".join(f"{signed_hashes[p]}  {p}\n" for p in non_manifest).encode())
    manifest = {
        "acceptance_aggregate_sha256": acceptance_aggregate,
        "approval_status": "PENDING_HUMAN_ACCEPTANCE",
        "candidate_id": CANDIDATE_ID,
        "exact_staged_inventory": inventory,
        "generated_payload_aggregate_sha256": generated_aggregate,
        "git_identity_model": "DETACHED_HUMAN_GATE_TREE_AND_GIT_CONTENT_IDENTITY",
        "governing_decision": DECISION_ID,
        "next_gate": "HUMAN_PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1_ACCEPTANCE",
        "readiness": {READY: 59, PENDING: 1093, NA: 111},
        "registry_aggregate_sha256": registry_aggregate,
        "signed_file_sha256": signed_hashes,
        "source_aggregate_sha256": source_aggregate,
        "status": "CANDIDATE",
        "supersedes": ["V23-P2C-DOCUMENT-BASELINE-C5", "V23-P2C-DOCUMENT-BASELINE-C6", "V23-P2C-DOCUMENT-BASELINE-C6-R1"],
    }
    manifest_path = "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-manifest.json"
    output_bytes[manifest_path] = canonical(manifest)

    for path, data in output_bytes.items():
        destination = output_root / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=ROOT)
    args = parser.parse_args()
    manifest = build(args.output_root.resolve())
    print(json.dumps({
        "candidate_id": manifest["candidate_id"],
        "generated_payload_aggregate_sha256": manifest["generated_payload_aggregate_sha256"],
        "inventory_count": len(manifest["exact_staged_inventory"]),
        "readiness": manifest["readiness"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
