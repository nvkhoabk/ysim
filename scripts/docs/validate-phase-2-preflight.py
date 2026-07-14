#!/usr/bin/env python3
"""Read-only validation for the Phase 2A human-decision preflight pack."""

from __future__ import annotations

import collections
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PHASE2 = ROOT / "docs/baselines/v2.3/phase-2"
REQUIREMENTS = ROOT / "docs/baselines/v2.3/requirements"
REGISTRY_VALIDATOR = ROOT / "scripts/docs/validate-requirement-registry.py"
APPROVAL_VALIDATOR = ROOT / "scripts/docs/validate-requirement-registry-approval.py"

ACCEPTED_COMMIT = "8c2e41f89443048a5b8568b308c32129634d7241"
ACCEPTED_TAG = "baseline/v2.3/requirements-registry/fc2-accepted"
SOURCE_COMMIT = "7f16d4c4b8ab514bd45de184f65ace221b03f4db"
SOURCE_AGGREGATE = "34685bed33422505763d31ef8f86837a1139fd5aaf2946a9adcbfa9dd1cd9a35"
REGISTRY_AGGREGATE = "832cc96192c72b89472964e030893ac4c01bcc0d20eb21f7e935b7a7c6288658"
EXPECTED_ALLOCATIONS = ["BRD-CAP-INDEX-R029", "UXF-05-R054"]
EXPECTED_CANDIDATE_IDENTITY = {
    "candidate_id": "V23-P2A-DECISION-PACK-C1",
    "status": "CANDIDATE",
    "approval_status": "PENDING_MARKDOWN_APPROVAL",
    "decision_count": 10,
    "open_decision_count": 0,
    "decided_pending_pack_approval_count": 10,
    "next_gate": "HUMAN_DECISION_PACK_APPROVAL",
    "source_registry_candidate_id": "V23-REQ-REGISTRY-FC2",
    "source_git_commit": "8c2e41f89443048a5b8568b308c32129634d7241",
    "hash_basis": "GIT_INDEX_BLOB_CONTENT",
    "line_endings": "GIT_CANONICAL_TEXT",
}
PENDING_APPROVAL = {
    "status": "PENDING",
    "authorized_approver": "PENDING",
    "decision": "PENDING",
    "date": "PENDING",
    "signature": "PENDING",
}
EXPECTED_DECISION_SHAPES = {
    "P2-DEC-001": [5, 5, 3, 5, 4],
    "P2-DEC-002": [18, 14, 11],
    "P2-DEC-003": [7, 6, 5],
    "P2-DEC-004": [18, 5, 6],
    "P2-DEC-005": [3, 8],
    "P2-DEC-006": [8, 8],
    "P2-DEC-007": [2, 7],
    "P2-DEC-008": [10, 14],
    "P2-DEC-009": [2, 7, 12, 2],
    "P2-DEC-010": [4, 5, 6, 7, 6, 5, 7, 2],
}
REQUIRED_DECISION_ANCHORS = {
    "P2-DEC-001": ["OIDC Authorization Code with PKCE", "SAML 2.0 Web Browser SSO", "Organization + Issuer + Subject", "Outbound IdP.", "SCIM."],
    "P2-DEC-002": ["security.authentication.succeeded", "security.break_glass.ended", "event_id", "Delivery is at least once", "Transport topology remains architecture-owned."],
    "P2-DEC-003": ["Connector Retry", "Operation Retry", "AMBIGUOUS_OUTCOME", "exactly-once", "P2-DEC-010"],
    "P2-DEC-004": ["operations.operation.started", "operations.recovery.failed", "monotonic per operation", "Transport topology remains architecture-owned."],
    "P2-DEC-005": ["Reclassify CAP-P07 as DESIGN_PRINCIPLE.", "CAP-EP-006 remains an alias.", "BRD-CAP-INDEX-R029", "event_role", "HIGH verification criticality"],
    "P2-DEC-006": ["External client to YSim API", "Internal domain API/event", "Business Domain never connects directly", "Production bypass is prohibited."],
    "P2-DEC-007": ["Reclassify UXF-505 as DESIGN_PRINCIPLE", "UXF-05-R054", "Internal Supplier ID", "fail-closed business behavior", "HIGH verification criticality"],
    "P2-DEC-008": ["at most one active User", "at most one active Customer", "Federation JIT creates User only.", "Email text matching is not ownership proof.", "Destructive Customer merge is outside v2.3."],
    "P2-DEC-009": ["Storefront: LCP 2.5s", "Embedded SDK", "rolling 28-day p75", "At least five lab runs", "https://web.dev/articles/vitals"],
    "P2-DEC-010": ["T0_INTEGRITY_CRITICAL", "Interactive read: 500ms / 1.5s.", "Online default is 15m.", "DEGRADED: error at least 5%", "F0_LIVE", "rolling 30-day", "https://sre.google/sre-book/service-level-objectives/"],
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run(command: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


def git_text(*args: str) -> str:
    result = run(["git", *args])
    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace"))
    return result.stdout.decode("utf-8").strip()


def index_blob(path: Path) -> bytes:
    relative = path.resolve().relative_to(ROOT).as_posix()
    result = run(["git", "show", ":" + relative])
    if result.returncode != 0:
        raise RuntimeError("missing staged Git blob: " + relative)
    return result.stdout


def optional_index_blob(path: Path) -> bytes | None:
    """Return an optional staged blob without consulting the working tree."""
    relative = path.resolve().relative_to(ROOT).as_posix()
    result = run(["git", "show", ":" + relative])
    if result.returncode != 0:
        return None
    return result.stdout


def load_index_json(path: Path) -> dict:
    return json.loads(index_blob(path).decode("utf-8"))


def canonical_atomic(record: dict) -> bool:
    return record.get("record_kind") != "ALIAS" and not record.get("is_composite")


def front_matter_fields(text: str) -> set[str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return set()
    fields: set[str] = set()
    for line in lines[1:]:
        if line == "---":
            return fields
        match = re.match(r"^([a-z_]+):", line)
        if match:
            fields.add(match.group(1))
    return set()


def all_strings(value: object):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield from all_strings(key)
            yield from all_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from all_strings(item)


def main() -> int:
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    # Existing immutable FC2 validators remain authoritative and must pass.
    registry_result = run([sys.executable, str(REGISTRY_VALIDATOR)])
    check(registry_result.returncode == 0, "existing FC2 registry validator failed")
    check(b"VALID_READY_TO_FREEZE" in registry_result.stdout, "FC2 readiness output missing")
    approval_result = run([sys.executable, str(APPROVAL_VALIDATOR)])
    check(approval_result.returncode == 0, "existing FC2 approval validator failed")
    check(b"VALID_APPROVED_RECONCILED_REGISTRY_BASELINE" in approval_result.stdout, "FC2 approval output missing")

    manifest = load_json(REQUIREMENTS / "registry-freeze-manifest.json")
    check(manifest.get("candidate_id") == "V23-REQ-REGISTRY-FC2", "FC2 candidate ID differs")
    check(manifest.get("source_git_commit") == SOURCE_COMMIT, "source commit differs")
    check(manifest.get("source_hash_basis") == "GIT_BLOB_CONTENT_AT_SOURCE_COMMIT", "source hash basis differs")
    check(manifest.get("line_ending_semantics") == "GIT_CANONICAL_TEXT", "line-ending semantics differs")
    check(manifest.get("source_aggregate_hash") == SOURCE_AGGREGATE, "source aggregate differs")
    check(manifest.get("registry_aggregate_hash") == REGISTRY_AGGREGATE, "registry aggregate differs")
    try:
        check(git_text("rev-parse", ACCEPTED_TAG + "^{commit}") == ACCEPTED_COMMIT, "accepted tag target differs")
        check(git_text("cat-file", "-t", SOURCE_COMMIT) == "commit", "source commit is not a commit object")
    except RuntimeError as exc:
        errors.append("cannot validate Git provenance: " + str(exc))

    verified_sources = 0
    for source in manifest.get("source_documents", []):
        result = run(["git", "cat-file", "blob", SOURCE_COMMIT + ":" + source.get("path", "")])
        if result.returncode != 0:
            errors.append("missing source Git blob: " + str(source.get("path")))
            continue
        if hashlib.sha256(result.stdout).hexdigest() != source.get("sha256"):
            errors.append("source Git blob SHA-256 differs: " + str(source.get("path")))
        else:
            verified_sources += 1
    check(len(manifest.get("source_documents", [])) == 31, "source inventory is not 31 documents")
    check(verified_sources == 31, "not all 31 source Git blob hashes match")

    decisions_path = PHASE2 / "phase-2-human-decisions.json"
    pack_path = PHASE2 / "PHASE_2_HUMAN_DECISION_PACK.md"
    mapping_path = PHASE2 / "stable-id-mapping-candidate.json"
    summary_path = PHASE2 / "phase-2-preflight-summary.json"
    register_path = PHASE2 / "PHASE_2_DECISION_REGISTER.md"
    exception_path = PHASE2 / "PHASE_2_CRITICALITY_EXCEPTION_REGISTER.md"
    contract_path = PHASE2 / "PHASE_2_DOCUMENT_REMEDIATION_CONTRACT.md"
    report_path = PHASE2 / "PHASE_2_PREFLIGHT_REPORT.md"
    detached_approval_path = PHASE2 / "PHASE_2_HUMAN_DECISION_PACK_APPROVAL.md"
    candidate_markdown_paths = [
        exception_path,
        register_path,
        contract_path,
        pack_path,
        report_path,
    ]
    candidate_json_paths = [decisions_path, summary_path, mapping_path]
    required_paths = candidate_markdown_paths + candidate_json_paths
    for path in required_paths:
        check(path.is_file(), "missing Phase 2 artifact: " + path.name)
        try:
            index_blob(path)
        except RuntimeError as exc:
            errors.append(str(exc))
    if errors:
        print("FAIL — PHASE_2_DECISION_PACK_PREFLIGHT_INVALID", file=sys.stderr)
        for error in errors:
            print("- " + error, file=sys.stderr)
        return 1

    decisions = load_index_json(decisions_path)
    mapping = load_index_json(mapping_path)
    summary = load_index_json(summary_path)
    pack_text = index_blob(pack_path).decode("utf-8")
    pack_lines = pack_text.splitlines()
    register_text = index_blob(register_path).decode("utf-8")
    exception_text = index_blob(exception_path).decode("utf-8")

    decision_identity = {key: decisions.get(key) for key in EXPECTED_CANDIDATE_IDENTITY}
    check(decision_identity == EXPECTED_CANDIDATE_IDENTITY, "decision JSON candidate identity/state differs or is incomplete")
    check(summary.get("decision_pack_candidate") == EXPECTED_CANDIDATE_IDENTITY, "summary candidate identity/state differs")
    summary_pack = summary.get("human_decision_pack", {})
    check({key: summary_pack.get(key) for key in EXPECTED_CANDIDATE_IDENTITY} == EXPECTED_CANDIDATE_IDENTITY, "summary Human Decision Pack identity/state differs")
    check(mapping.get("status") == "DRAFT", "stable-ID mapping status is not DRAFT")
    check(summary.get("status") == "PREFLIGHT", "preflight summary status is not PREFLIGHT")
    check(decisions.get("approval") == PENDING_APPROVAL, "decision JSON approval is not entirely pending")
    model = decisions.get("decision_status_model", {})
    check(model == {
        "decision_count": 10,
        "open_decision_count": 0,
        "decided_pending_pack_approval_count": 10,
        "selected_option": 1,
        "next_gate": "HUMAN_DECISION_PACK_APPROVAL",
    }, "decision status model differs")
    check(summary_pack.get("approval") == PENDING_APPROVAL, "summary approval block is not entirely pending")
    for payload_name, binding in (
        ("decision JSON", decisions.get("baseline_binding", {})),
        ("summary", summary.get("baseline_binding", {})),
    ):
        check(binding.get("source_registry_candidate_id") == "V23-REQ-REGISTRY-FC2", payload_name + " source FC2 identity differs")
        check(binding.get("accepted_registry_commit") == ACCEPTED_COMMIT, payload_name + " accepted registry commit differs")
        check(binding.get("source_hash_basis") == "GIT_BLOB_CONTENT_AT_SOURCE_COMMIT", payload_name + " FC2 source hash basis differs")
    decision_items = decisions.get("decisions", [])
    check([item.get("decision_id") for item in decision_items] == sorted(EXPECTED_DECISION_SHAPES), "decision IDs/order differ")
    check(len(decision_items) == decisions.get("decision_count"), "top-level decision_count differs from decision records")
    check(len({item.get("decision_id") for item in decision_items}) == len(decision_items), "decision IDs are duplicated")
    derived_open_count = sum(item.get("status") == "OPEN" for item in decision_items)
    derived_decided_count = sum(item.get("status") == "DECIDED_PENDING_PACK_APPROVAL" for item in decision_items)
    check(decisions.get("open_decision_count") == derived_open_count == 0, "top-level open_decision_count differs from decision records")
    check(decisions.get("decided_pending_pack_approval_count") == derived_decided_count == 10, "top-level decided count differs from decision records")
    for item in decision_items:
        decision_id = item.get("decision_id", "")
        check(item.get("selected_option") == 1, decision_id + " selected option is not 1")
        check(item.get("status") == "DECIDED_PENDING_PACK_APPROVAL", decision_id + " status differs")
        section_sizes = [len(section.get("items", [])) for section in item.get("sections", [])]
        check(section_sizes == EXPECTED_DECISION_SHAPES.get(decision_id), decision_id + " full decision shape differs")
        flattened = "\n".join(value for section in item.get("sections", []) for value in section.get("items", []))
        for anchor in REQUIRED_DECISION_ANCHORS.get(decision_id, []):
            check(anchor in flattened, decision_id + " required decision content missing: " + anchor)
        check(("## " + decision_id + " — ") in pack_text, decision_id + " Markdown section missing")
        for section in item.get("sections", []):
            check(("### " + section.get("heading", "")) in pack_lines, decision_id + " Markdown subsection missing")
            for value in section.get("items", []):
                check(("- " + value) in pack_lines, decision_id + " Markdown decision item missing: " + value)

    expected_pack_tail = """## Human Approval

- Status: PENDING
- Authorized Approver: PENDING
- Decision: PENDING
- Date: PENDING
- Signature: PENDING"""
    check(pack_text.rstrip().endswith(expected_pack_tail), "Human Decision Pack approval block is not exactly pending")
    for key, value in EXPECTED_CANDIDATE_IDENTITY.items():
        expected_line = "- {}: `{}`".format(key, value)
        check(pack_lines.count(expected_line) == 1, "Human Decision Pack candidate identity line missing or duplicated: " + expected_line)
    check(pack_lines.count("- Selected option: `1`.") == 10, "Human Decision Pack selected-option count differs")
    check(pack_lines.count("- Status: `DECIDED_PENDING_PACK_APPROVAL`.") == 10, "Human Decision Pack decision-status count differs")
    for required_pack_line in (
        "- `P2-DEC-005`: reserve `BRD-CAP-INDEX-R029` as a `V2.3_ACTIVE`",
        "- `P2-DEC-007`: reserve `UXF-05-R054` as a `V2.3_ACTIVE`",
        "- Projected registry entries: `1185 → 1187`.",
        "- Projected canonical atomic units: `1174 → 1176`.",
        "- Projected active acceptance denominator: `1068 → 1070`.",
        "- Proposed criticality: `CRITICAL 313`, `HIGH 409`, `NORMAL 348`.",
    ):
        check(required_pack_line in pack_lines, "Human Decision Pack projection line missing: " + required_pack_line)

    check(register_text.count("- Selected option: `1`.") == 10, "Decision Register selected-option count differs")
    check(register_text.count("- Status: `DECIDED_PENDING_PACK_APPROVAL`.") == 10, "Decision Register decided count differs")
    check("- Open semantic decisions: `0`." in register_lines if (register_lines := register_text.splitlines()) else False, "Decision Register open count is not zero")
    check("- Pack approval: `PENDING`." in register_lines, "Decision Register pack status differs")
    check("- Next preflight gate: `HUMAN_DECISION_PACK_APPROVAL`." in register_lines, "Decision Register next gate differs")
    check("- Status: `OPEN`." not in register_lines, "Decision Register still contains OPEN status")

    # Reconstruct the accepted registry and deterministic 609 mappings.
    registry_sets = [load_json(REQUIREMENTS / "brd-requirements.json"), load_json(REQUIREMENTS / "uxf-requirements.json")]
    records = [record for registry_set in registry_sets for record in registry_set["requirements"]]
    reconciliation = load_json(REQUIREMENTS / "registry-reconciliation.json")
    temp_records = sorted((record for record in records if record.get("temporary_key")), key=lambda record: record["temporary_key"])
    existing_ids = {record["current_id"] for record in records if record.get("current_id")}
    aliases = {record["current_id"] for record in records if record.get("record_kind") == "ALIAS"}
    composites = {record["current_id"] for record in records if record.get("is_composite")}
    retired_keys = set(reconciliation["retired_temporary_keys"])
    grammar = re.compile(r"^TMP-(BRD|UXF)-(.+)-([0-9]{3})$")
    mapping_items = mapping.get("mappings", [])
    check(len(mapping_items) == 609, "stable mapping count is not 609")
    check([item.get("temporary_key") for item in mapping_items] == [record["temporary_key"] for record in temp_records], "mapping keys/order differ from active temporary keys")
    planned_ids: set[str] = set()
    for item in mapping_items:
        match = grammar.fullmatch(item.get("temporary_key", ""))
        if not match:
            errors.append("temporary-key grammar failure: " + str(item.get("temporary_key")))
            continue
        expected_id = match.group(1) + "-" + match.group(2) + "-R" + match.group(3)
        check(item.get("proposed_stable_id") == expected_id, "non-deterministic stable mapping: " + item["temporary_key"])
        check(item.get("collision_status") == "CLEAR", "mapping collision status differs")
        check(item.get("reuse_status") == "NOT_REUSED", "mapping reuse status differs")
        planned_ids.add(expected_id)
    check(len(planned_ids) == 609, "planned stable mapping IDs are not unique")
    check(not (planned_ids & existing_ids), "planned mapping collides with existing IDs")
    check(not (planned_ids & aliases), "planned mapping collides with aliases")
    check(not (planned_ids & composites), "planned mapping collides with composite parents")

    allocations = mapping.get("new_requirement_allocations", [])
    check([item.get("proposed_stable_id") for item in allocations] == EXPECTED_ALLOCATIONS, "new allocation IDs differ")
    check(decisions.get("new_requirement_allocations") == allocations, "allocation ledgers differ between JSON artifacts")
    check(len(mapping.get("reservation_ledger", [])) == 2, "reservation ledger count differs")
    retired_reservations: set[str] = set()
    for key in retired_keys:
        match = grammar.fullmatch(key)
        if match:
            retired_reservations.add(match.group(1) + "-" + match.group(2) + "-R" + match.group(3))
    allocation_ids = {item.get("proposed_stable_id") for item in allocations}
    check(len(allocation_ids) == 2, "allocation IDs are not unique")
    check(not allocation_ids & (existing_ids | planned_ids | retired_reservations), "allocation collides with existing/planned/retired namespace")
    for item in allocations:
        prefix = item["origin_document_code"] + "-R"
        used = {value for value in existing_ids | planned_ids | retired_reservations if value.startswith(prefix)}
        suffixes = [int(value.rsplit("R", 1)[1]) for value in used]
        check(bool(suffixes), "allocation namespace has no provenance: " + prefix)
        if suffixes:
            check(item["reserved_suffix"] == max(suffixes) + 1, "allocation is not next never-used ID: " + item["proposed_stable_id"])
        check(item.get("collision_status") == "CLEAR", "allocation collision status differs")
        check(item.get("reuse_status") == "NOT_REUSED", "allocation reuse status differs")
        check(item.get("reservation_status") == "RESERVED_PENDING_PACK_APPROVAL", "allocation reservation status differs")

    atomic = [record for record in records if canonical_atomic(record)]
    active = [record for record in atomic if record.get("scope_status") == "V2.3_ACTIVE"]
    inactive = [record for record in atomic if record.get("scope_status") != "V2.3_ACTIVE"]
    check((len(records), len(atomic), len(active), len(inactive)) == (1185, 1174, 1068, 106), "accepted registry counts differ")
    projected = summary.get("stable_id_projection", {})
    check(projected.get("planned_ids_from_temporary_mappings") == 609, "projected temporary mappings differ")
    check(projected.get("new_requirement_allocations") == 2, "projected allocation count differs")
    check(projected.get("projected_active_registry_entries") == 1187, "projected registry entries differ")
    check(projected.get("projected_canonical_atomic_units") == 1176, "projected canonical units differ")
    check(projected.get("projected_registry_entries_with_id") == 1187, "projected with-ID count differs")
    check(projected.get("projected_active_registry_without_id") == 0, "projected without-ID count differs")
    check(projected.get("allocated_ids") == EXPECTED_ALLOCATIONS, "summary allocation IDs differ")
    check(decisions.get("projected_counts") == {
        "active_registry_entries": {"before": 1185, "after": 1187},
        "canonical_atomic_units": {"before": 1174, "after": 1176},
        "active_acceptance_denominator": {"before": 1068, "after": 1070},
        "inactive_not_applicable_denominator": {"before": 106, "after": 106},
        "existing_ids": 576,
        "temporary_key_mappings": 609,
        "new_stable_requirements": 2,
        "projected_entries_with_stable_id": 1187,
        "projected_without_id": 0,
        "criticality": {"CRITICAL": 313, "HIGH": 409, "NORMAL": 348},
        "criticality_exceptions": 46,
    }, "decision JSON projected counts differ")

    acceptance = summary.get("acceptance_projection", {})
    check(acceptance.get("acceptance_required_denominator") == 1070, "active acceptance denominator differs")
    check(acceptance.get("inactive_not_applicable_denominator") == 106, "inactive N/A denominator differs")
    check(acceptance.get("projected_active_acceptance_gap_before_remediation") == 1070, "projected acceptance gap before differs")
    check(acceptance.get("projected_active_acceptance_gap_after_complete_remediation") == 0, "projected acceptance gap after differs")

    criticality = summary.get("criticality_preflight", {})
    assignments = criticality.get("assignments", [])
    distribution = collections.Counter(item.get("verification_criticality") for item in assignments)
    check(len(assignments) == 1070, "criticality assignment count differs")
    check(len({item.get("stable_requirement_id") for item in assignments}) == 1070, "criticality IDs are not unique")
    check(distribution == {"CRITICAL": 313, "HIGH": 409, "NORMAL": 348}, "criticality distribution differs")
    exception_assignments = [item for item in assignments if item.get("exception_review_required")]
    check(len(exception_assignments) == 46, "criticality exception count differs")
    check(all(item.get("verification_criticality") == "HIGH" for item in assignments if item.get("stable_requirement_id") in allocation_ids), "new allocations are not HIGH")
    check(all(not item.get("exception_review_required") for item in assignments if item.get("stable_requirement_id") in allocation_ids), "new allocations unexpectedly require exceptions")

    all_exception_rows = re.findall(r"^\| P2-CRIT-EXC-[0-9]{3} \| `([^`]+)` \| `([^`]+)` .* \| `([^`]+)` \|$", exception_text, re.M)
    check(len(all_exception_rows) == 46, "criticality exception table row count differs")
    check(all(status == "OPEN" for _, _, status in all_exception_rows), "a criticality exception has been resolved or changed from OPEN")
    exception_rows = [(stable_id, tier) for stable_id, tier, status in all_exception_rows if status == "OPEN"]
    expected_exception_rows = [(item["stable_requirement_id"], item["verification_criticality"]) for item in exception_assignments]
    check(exception_rows == expected_exception_rows, "criticality exception register does not match summary")
    check("- Exception count: `46`." in exception_text, "criticality exception header differs")
    check("- Projected distribution: `CRITICAL 313`, `HIGH 409`, `NORMAL 348`." in exception_text, "criticality projected distribution missing")

    required_front_matter = {
        "schema_version", "document_code", "title", "product_baseline",
        "document_revision", "lifecycle_status", "language", "authority",
        "supersedes", "requirement_block_schema",
    }
    indexed_markdown_blobs = {
        path: index_blob(path)
        for path in candidate_markdown_paths
    }
    detached_approval_blob = optional_index_blob(detached_approval_path)
    if detached_approval_blob is not None:
        indexed_markdown_blobs[detached_approval_path] = detached_approval_blob
    for path, blob in sorted(indexed_markdown_blobs.items()):
        check(required_front_matter <= front_matter_fields(blob.decode("utf-8")), "required Markdown front matter missing: " + path.name)
    contract_text = indexed_markdown_blobs[contract_path].decode("utf-8")
    report_text = indexed_markdown_blobs[report_path].decode("utf-8")
    for required_text in (
        "`BRD-CAP-INDEX-R029`", "`UXF-05-R054`", "`HUMAN_DECISION_PACK_APPROVAL`",
        "`CRITICAL 313`, `HIGH 409`, and `NORMAL 348`",
    ):
        check(required_text in contract_text, "contract projection/gate text missing: " + required_text)
    for required_text in (
        "| Active registry entries | 1,185 | 1,187 |",
        "| Canonical atomic units | 1,174 | 1,176 |",
        "- Active acceptance denominator: `1,070`.",
        "Decision Register result: `0 OPEN`",
        "`BRD-CAP-INDEX-R029`", "`UXF-05-R054`",
    ):
        check(required_text in report_text, "preflight report projection text missing: " + required_text)
    for path in sorted(candidate_json_paths):
        try:
            payload = load_index_json(path)
            check(payload.get("schema_version") == "1.0", "JSON schema version differs: " + path.name)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append("invalid JSON " + path.name + ": " + str(exc))

    machine_path_pattern = re.compile(r"(?:^|\s)(?:/root/|/home/|/Users/|/tmp/|[A-Za-z]:\\\\)")
    indexed_artifacts = [*candidate_markdown_paths, *candidate_json_paths]
    if detached_approval_blob is not None:
        indexed_artifacts.append(detached_approval_path)
    for path in sorted(indexed_artifacts):
        if path in candidate_json_paths:
            values = all_strings(load_index_json(path))
        else:
            values = [indexed_markdown_blobs[path].decode("utf-8")]
        for value in values:
            check(not machine_path_pattern.search(value), "machine-specific path found in " + path.name)

    # Neither index/worktree nor accepted history may alter BRD/UXF source.
    check(run(["git", "diff", "--quiet", "HEAD", "--", "docs/BRD", "docs/UXF"]).returncode == 0, "BRD/UXF differ from HEAD")
    check(run(["git", "diff", "--quiet", SOURCE_COMMIT, "HEAD", "--", "docs/BRD", "docs/UXF"]).returncode == 0, "HEAD BRD/UXF differ from source baseline")
    check(run([
        "git", "diff", "--quiet", "--",
        "docs/baselines/v2.3/FRAMEWORK_DECISIONS.md",
        "docs/baselines/v2.3/phase-2",
        "scripts/docs/validate-phase-2-preflight.py",
    ]).returncode == 0, "Phase 2A working-tree content differs from staged Git content")

    if errors:
        print("FAIL — PHASE_2_DECISION_PACK_PREFLIGHT_INVALID", file=sys.stderr)
        for error in errors:
            print("- " + error, file=sys.stderr)
        return 1

    print("PASS — PHASE_2_DECISION_PACK_READY_FOR_HUMAN_APPROVAL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
