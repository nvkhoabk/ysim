#!/usr/bin/env python3
"""Validate the Phase 2C progressive document baseline C1."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any, Iterator


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3/phase-2"
REGISTRY_PATH = BASE / "phase-2c-progressive-document-baseline-c1-registry.json"
LEDGER_PATH = BASE / "phase-2c-progressive-document-baseline-c1-readiness-ledger.json"
MANIFEST_PATH = BASE / "phase-2c-progressive-document-baseline-c1-manifest.json"
POLICY_PATH = BASE / "phase-2c-progressive-document-baseline-c1-policy.json"
REFERENCE_PATH = BASE / "semantic-acceptance-renderer-c2-reference-good-contracts.json"
BACKUP = "refs/ysim-backups/v2.3/phase-2c-document-baseline-c6-r1-rejected"
BACKUP_OBJECT = "8ec2a5381054fc6dddad2e1c2ad15bd4e53a0a28"
BACKUP_TREE = "699a7de703fc1c0009cca0d851c67766a1d7d333"
SOURCE_REGISTRY = "docs/baselines/v2.3/phase-2/phase-2c-document-baseline-c6-r1-registry.json"
READY = "ACCEPTANCE_READY"
PENDING = "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
NA = "NOT_APPLICABLE_FOR_V2.3"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"INVALID_PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1: {message}")


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def git_bytes(spec: str) -> bytes:
    return subprocess.check_output(["git", "show", spec], cwd=ROOT)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def strings(value: Any) -> Iterator[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from strings(child)


def main() -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    reference = json.loads(REFERENCE_PATH.read_text(encoding="utf-8"))
    source = json.loads(git_bytes(f"{BACKUP_TREE}:{SOURCE_REGISTRY}"))

    require(git("rev-parse", BACKUP) == BACKUP_OBJECT, "backup object")
    require(git("rev-parse", f"{BACKUP}^{{tree}}") == BACKUP_TREE, "backup tree")
    records = registry["requirements"]
    require(len(records) == 1326, "record count")
    require(len({record["stable_id"] for record in records}) == 1326, "duplicate IDs")
    kinds = Counter(record["record_kind"] for record in records)
    require(kinds == Counter({"CANONICAL_ATOMIC": 1263, "COMPOSITE_PARENT": 48, "ALIAS": 12, "RETIRED_RECORD": 3}), "record kinds")
    canonical = [record for record in records if record["record_kind"] == "CANONICAL_ATOMIC"]
    active = [record for record in canonical if record["scope_status"] == "V2.3_ACTIVE"]
    inactive = [record for record in canonical if record["scope_status"] != "V2.3_ACTIVE"]
    require(len(active) == 1152 and len(inactive) == 111, "active/inactive")
    require(Counter(record["verification_criticality"] for record in active) == Counter({"CRITICAL": 340, "HIGH": 439, "NORMAL": 373}), "criticality")
    require(Counter(record["scope_status"] for record in canonical) == Counter({"V2.3_ACTIVE": 1152, "FUTURE": 77, "DEFERRED": 16, "OUT_OF_SCOPE": 18}), "scope")

    source_by_id = {record["stable_id"]: record for record in source["requirements"]}
    for record in records:
        old = source_by_id[record["stable_id"]]
        for field in ("stable_id", "record_kind", "normative_statement", "atomic_obligations", "scope_status", "verification_criticality", "relationships", "requirement_type"):
            require(record[field] == old[field], f"source/structure drift {record['stable_id']}:{field}")
        require(record["provenance"]["source_fingerprint"] == old["provenance"]["source_fingerprint"], f"fingerprint drift {record['stable_id']}")

    reference_by_id = {row["requirement_id"]: row for row in reference["records"]}
    ready = [record for record in active if record["acceptance_status"] == READY]
    pending = [record for record in active if record["acceptance_status"] == PENDING]
    require(len(ready) == 59 and len(pending) == 1093, "readiness distribution")
    require(set(record["stable_id"] for record in ready) == set(reference_by_id), "ready population")
    for record in ready:
        rid = record["stable_id"]
        require(record["acceptance_contract"] == reference_by_id[rid]["acceptance_contract"], f"ready contract bytes {rid}")
        require(record["acceptance_mechanism"]["mechanism"] == "APPROVED_TYPED_CUSTOM_AST", f"ready mechanism {rid}")
    expected_pending_keys = {"acceptance_content", "acceptance_state", "implementation_entry_policy", "traceability"}
    decision_selections = []
    for record in pending:
        rid = record["stable_id"]
        contract = record["acceptance_contract"]
        require(set(contract) == expected_pending_keys, f"pending payload keys {rid}")
        require(contract["acceptance_content"] is None and contract["acceptance_state"] == PENDING, f"pending content {rid}")
        require(record["acceptance_mechanism"] == {"inference": False, "mechanism": PENDING, "runtime_status": PENDING}, f"pending mechanism {rid}")
        selection = contract["traceability"].get("approved_semantic_completion_selection")
        if selection:
            decision_selections.append((rid, selection["decision_id"], selection["option_id"]))
        joined = "\n".join(strings(contract))
        require(not re.search(r"YSIM\.(?:C5|C6|C99)\.", joined), f"candidate identifier {rid}")
        require(not any(token in contract for token in ("positive_oracle", "negative_oracle", "boundary_oracle", "required_evidence", "concrete_bindings", "human_verification_procedure", "approved_typed_contract_ast")), f"acceptance content {rid}")
    require(len(decision_selections) == 27 and len({row[1] for row in decision_selections}) == 27, "approved decisions")

    for record in inactive:
        require(record["acceptance_status"] == NA, f"inactive status {record['stable_id']}")
        require(record["acceptance_contract"]["acceptance_state"] == NA, f"inactive state {record['stable_id']}")
        require(record["acceptance_contract"]["acceptance_content"] is None, f"inactive content {record['stable_id']}")

    require(ledger["counts"] == {READY: 59, PENDING: 1093, NA: 111}, "ledger counts")
    require(len(ledger["records"]) == 1263, "ledger rows")
    summary = registry["summary"]
    require(summary["acceptance_gap"] == 1093, "acceptance gap")
    require(summary["acceptance_ready_count"] == 59, "ready summary")
    require(summary["pending_acceptance_elaboration_count"] == 1093, "pending summary")
    require(summary["unsupported_generic_contract_count"] == 0, "generic count")
    require(summary["invalid_acceptance_claim_count"] == 0, "invalid claim count")
    require(policy["pending_requirement_implementation_allowed_without_slice_approval"] is False, "entry policy")
    require(len(policy["required_slice_fields"]) == 14, "slice fields")

    inventory = manifest["exact_staged_inventory"]
    require(len(inventory) == len(set(inventory)), "manifest duplicate inventory")
    require(len([path for path in inventory if path.startswith(("docs/BRD/", "docs/UXF/"))]) == 31, "source inventory")
    for path, expected in manifest["signed_file_sha256"].items():
        require(sha((ROOT / path).read_bytes()) == expected, f"signed hash {path}")
    require(manifest["status"] == "CANDIDATE" and manifest["approval_status"] == "PENDING_HUMAN_ACCEPTANCE", "candidate state")
    require(manifest["readiness"] == {READY: 59, PENDING: 1093, NA: 111}, "manifest readiness")
    acceptance_rows = [f"{record['stable_id']}:{sha(compact(record['acceptance_contract']))}\n" for record in canonical]
    require(sha("".join(sorted(acceptance_rows)).encode()) == manifest["acceptance_aggregate_sha256"], "acceptance aggregate")
    print("VALID_PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1")


if __name__ == "__main__":
    main()
