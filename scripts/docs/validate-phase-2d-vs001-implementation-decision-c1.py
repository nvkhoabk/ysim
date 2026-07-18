#!/usr/bin/env python3
"""Independent validator for the VS001 implementation decision C1 candidate."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GOVERNING = "4a0ff5700554023b30d9a6dba01d80d1dbc78867"
EXPECTED_CANONICAL_SHA256 = "08c22be8b5ff29e0d8b8dbd3aa3ddeeed74533fe866848d5ad051f832d7df705"
FILES = [
    "docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_DECISION_C1_CANDIDATE.md",
    "docs/baselines/v2.3/phase-2d/vs001-implementation-decision-c1.json",
    "docs/baselines/v2.3/phase-2d/vs001-implementation-decision-c1-manifest.json",
    "scripts/docs/build-phase-2d-vs001-implementation-decision-c1.py",
    "scripts/docs/validate-phase-2d-vs001-implementation-decision-c1.py",
    "scripts/docs/tests/test-phase-2d-vs001-implementation-decision-c1.py",
]
AUTHORITIES = {
    "COMMISSIONING_C1_APPROVAL": ("c3429e79b2e80ac050b21dd9dc5844dd64029ce0", "docs/baselines/v2.3/phase-2d/PRODUCT_IMPLEMENTATION_COMMISSIONING_C1_APPROVAL.md", "4aa6eef4bceeaa6416a39186b72301fe4f1a9883", "ae547142f29eb98950e86f99a1b61e301e082b8f8fe8ea9b6f6adba4025f5512"),
    "COMMISSIONING_I1_R1_APPROVAL": ("f7f2aeca3c1643996f77dec1b0b5caae22363ddc", "docs/baselines/v2.3/phase-2d/PRODUCT_IMPLEMENTATION_COMMISSIONING_I1_R1_APPROVAL.md", "f2a856c92f91e14b631e3dfa8ce2f8ed09ee06d1", "85ae4091af9fdcfb26c49bbbbf0623e9d85c62a69ce12e50235715368bfefc87"),
    "VS001_DECISION_C1_CANONICAL": ("f003eca82512887a616c4ee83ed4ab8da4432b8a", "docs/baselines/v2.3/phase-2d/vs001-acceptance-decision-c1.json", "d4786ec62ca6d4df9b667f7c835857c630ad3c89", "b5f7ffb9eae4167749ffd5c7ba1038afe401d9e0366103f6223dbb8966695b3f"),
    "VS001_DECISION_C1_APPROVAL": ("c818d734049fbf8997a5dce4e1e66e65d6a92f59", "docs/baselines/v2.3/phase-2d/VS001_ACCEPTANCE_DECISION_C1_APPROVAL.md", "7fd209449aee059da33324391b2e8e55aded7ee2", "7907d2b523dbe24facabbf00bb4c9c34594dc55ebf2dfe77b3ea274f3f0afad5"),
    "VS001_ELABORATION_C2_R2_CANONICAL": ("5780bf5e89c66103980fd4cda7c2b294fdc23f20", "docs/baselines/v2.3/phase-2d/vs001-acceptance-elaboration-c2-r2.json", "ab9535b8b54b9dcbff60761d24bf744b380a0b31", "d80d6c5b00660eb9dc5a8d3835f9dd6baecca93e732def903f568b675af71ac7"),
    "VS001_ELABORATION_C2_R2_APPROVAL": ("4a0ff5700554023b30d9a6dba01d80d1dbc78867", "docs/baselines/v2.3/phase-2d/VS001_ACCEPTANCE_ELABORATION_C2_R2_APPROVAL.md", "1cdb2c8f7f915d97755676732fde1760e55f3df1", "894892358e1bfaa8b22710b92abf7b962042e7a861fa12c12119a29531532987"),
}
REQUIREMENTS = {
    "BRD-UPDATE-01-R001", "BRD-WS-02-R002", "BRD-WS-02-R003", "BD-04-005", "UXF-010", "UXF-011", "UXF-109", "UXF-402", "UXF-405",
    "BD-02-001", "BD-02-002", "BD-04-001", "BD-04-002", "BD-04-003", "BRD-WS-04-R001", "BD-05-001", "UXF-003", "UXF-301", "UXF-304", "UXF-306",
    "UXF-04-R011", "UXF-05-R004", "UXF-05-R010", "UXF-05-R018", "UXF-05-R056",
}
DECISION_OPTIONS = {
    "V23-P2D-VS001-IMPLEMENTATION-DEC-001": {"OPT-V1-STOREFRONT-RESOURCE-HIERARCHY", "OPT-V1-CATALOG-RESOURCE-WITH-STOREFRONT-HEADER", "OPT-UNVERSIONED-STOREFRONT-RESOURCE"},
    "V23-P2D-VS001-IMPLEMENTATION-DEC-002": {"OPT-BCP47-REQUEST-THEN-STOREFRONT-DEFAULT", "OPT-EXACT-BCP47-NO-FALLBACK", "OPT-STOREFRONT-DEFAULT-LOCALE-ONLY"},
    "V23-P2D-VS001-IMPLEMENTATION-DEC-003": {"OPT-OPAQUE-CURSOR-SLUG-IDENTITY-ORDER", "OPT-OFFSET-LIMIT-SLUG-IDENTITY-ORDER", "OPT-UNPAGINATED-BOUNDED-VS001-LIST"},
    "V23-P2D-VS001-IMPLEMENTATION-DEC-004": {"OPT-EXPLICIT-DATA-META-DTO", "OPT-BARE-RESOURCE-DTO", "OPT-JSONAPI-LIKE-RESOURCE-DOCUMENT"},
    "V23-P2D-VS001-IMPLEMENTATION-DEC-005": {"OPT-STOREFRONT-ENTRY-SLUG-UUIDV7-PUBLIC-ID", "OPT-SEPARATE-PUBLIC-IDENTIFIER-UUIDV4", "OPT-DERIVED-SLUG-ENCODED-INTERNAL-ID"},
    "V23-P2D-VS001-IMPLEMENTATION-DEC-006": {"OPT-NORMALIZED-TYPED-RELATIONAL-MODEL", "OPT-HYBRID-RELATIONAL-CORE-JSONB-SPECIFICATION", "OPT-DENORMALIZED-PUBLIC-CATALOG-DOCUMENT"},
    "V23-P2D-VS001-IMPLEMENTATION-DEC-007": {"OPT-FORWARD-MIGRATION-SEPARATE-FIXTURE-LOADER", "OPT-MIGRATION-EMBEDS-REFERENCE-SEED", "OPT-RUNTIME-STARTUP-AUTO-SEED"},
    "V23-P2D-VS001-IMPLEMENTATION-DEC-008": {"OPT-REQUEST-TIMESTAMP-REPEATABLE-READ-SNAPSHOT", "OPT-REQUEST-TIMESTAMP-READ-COMMITTED-VERSION-CHECKS", "OPT-MATERIALIZED-ELIGIBLE-CATALOG-SNAPSHOT"},
    "V23-P2D-VS001-IMPLEMENTATION-DEC-009": {"OPT-SERVER-CORRELATION-ID-ALLOWLISTED-AUDIT", "OPT-INTERNAL-CORRELATION-ONLY", "OPT-VALIDATED-CLIENT-CORRELATION-ECHO"},
}
REQUIRED_TOKENS = {
    "V23-P2D-VS001-IMPLEMENTATION-DEC-001": ["/api/v1", "Storefront", "version"],
    "V23-P2D-VS001-IMPLEMENTATION-DEC-002": ["BCP 47", "Storefront default", "mandatory localized"],
    "V23-P2D-VS001-IMPLEMENTATION-DEC-003": ["cursor", "offset", "deterministic"],
    "V23-P2D-VS001-IMPLEMENTATION-DEC-004": ["PRODUCT_NOT_FOUND", "primary_image", "HTTP 404"],
    "V23-P2D-VS001-IMPLEMENTATION-DEC-005": ["unique(storefront_id,public_slug)", "UUID", "Supplier"],
    "V23-P2D-VS001-IMPLEMENTATION-DEC-006": ["foreign keys", "JSONB", "projection"],
    "V23-P2D-VS001-IMPLEMENTATION-DEC-007": ["forward-only", "fixture", "cleanup"],
    "V23-P2D-VS001-IMPLEMENTATION-DEC-008": ["evaluation instant", "publication validation", "price"],
    "V23-P2D-VS001-IMPLEMENTATION-DEC-009": ["correlation", "redact", "internal reason"],
}
BANNED_GENERIC = ["works as expected", "handled correctly", "appropriate evidence", "relevant boundary", "observe subject and demonstrate"]


class ValidationFailure(RuntimeError):
    pass


def fail(code: str, detail: str) -> None:
    raise ValidationFailure(f"{code}: {detail}")


def run(*args: str) -> bytes:
    return subprocess.check_output(args, cwd=ROOT)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def canonical_sha(value: object) -> str:
    return sha(canonical_bytes(value))


def aggregate(files: dict[str, bytes], paths: list[str]) -> str:
    return canonical_sha([{"path": path, "sha256": sha(files[path])} for path in sorted(paths)])


def git_bytes(commit: str, path: str) -> bytes:
    return run("git", "show", f"{commit}:{path}")


def validate_authorities(payload: dict) -> dict:
    declared = {item["authority_id"]: item for item in payload.get("authority_objects", [])}
    if set(declared) != set(AUTHORITIES):
        fail("AUTHORITY_SET_MISMATCH", repr(set(declared)))
    for authority_id, (commit, path, oid, expected_sha) in AUTHORITIES.items():
        item = declared[authority_id]
        if (item.get("commit"), item.get("path"), item.get("blob_oid"), item.get("sha256")) != (commit, path, oid, expected_sha):
            fail("AUTHORITY_DECLARATION_MISMATCH", authority_id)
        observed_oid = run("git", "rev-parse", f"{commit}:{path}").decode().strip()
        data = git_bytes(commit, path)
        if observed_oid != oid or sha(data) != expected_sha:
            fail("AUTHORITY_GIT_OBJECT_MISMATCH", authority_id)
    if run("git", "rev-parse", "4a0ff5700554023b30d9a6dba01d80d1dbc78867^").decode().strip() != "5780bf5e89c66103980fd4cda7c2b294fdc23f20":
        fail("ELABORATION_APPROVAL_CHAIN_MISMATCH", GOVERNING)
    if run("git", "rev-parse", "c818d734049fbf8997a5dce4e1e66e65d6a92f59^").decode().strip() != "f003eca82512887a616c4ee83ed4ab8da4432b8a":
        fail("DECISION_APPROVAL_CHAIN_MISMATCH", "c818d734")
    if run("git", "rev-parse", "f7f2aeca3c1643996f77dec1b0b5caae22363ddc^").decode().strip() != "5e4f373619140f575d061436ab3a08368f63c55a":
        fail("COMMISSIONING_APPROVAL_CHAIN_MISMATCH", "f7f2aeca")
    accepted = json.loads(git_bytes("5780bf5e89c66103980fd4cda7c2b294fdc23f20", "docs/baselines/v2.3/phase-2d/vs001-acceptance-elaboration-c2-r2.json"))
    contracts = [contract for batch in ("batch_1_contracts", "batch_2_contracts", "batch_3_contracts") for contract in accepted[batch]]
    observed_ids = {item["requirement_id"] for item in accepted["retained_contracts"]} | {item["requirement_id"] for item in contracts}
    obligations = sum(len(item["obligation_mapping"]) for item in contracts)
    criteria = sum(len(item["positive_outcomes"]) for item in contracts)
    clauses = accepted["decision_derived_acceptance_clauses"]
    if observed_ids != REQUIREMENTS or len(accepted["retained_contracts"]) != 9 or len(contracts) != 16 or obligations != 21 or criteria != 32 or len(clauses) != 124:
        fail("ACCEPTED_AUTHORITY_RECONCILIATION_MISMATCH", f"{len(observed_ids)}/9/{len(contracts)}/{obligations}/{criteria}/{len(clauses)}")
    return {"requirements": 25, "retained": 9, "elaborated": 16, "obligations": 21, "criteria": 32, "clauses": 124}


def validate_payload(payload: dict, enforce_root_hash: bool = True) -> dict:
    # Raw-byte root locking is performed by validate_all; mutation tests call
    # this semantic path with fresh in-memory payloads and independent oracles.
    expected_metadata = {
        "candidate_id": "V23-P2D-VS001-IMPLEMENTATION-DECISION-C1",
        "status": "CANDIDATE",
        "approval": "PENDING_HUMAN_APPROVAL",
        "implementation_authorized": False,
        "runtime_evidence_status": "NOT_EXECUTED",
        "implementation_contract_created": False,
        "governing_commit": GOVERNING,
        "next_gate": "HUMAN_PHASE_2D_VS001_IMPLEMENTATION_DECISION_REQUIRED",
    }
    for key, expected in expected_metadata.items():
        if payload.get(key) != expected:
            fail("CANDIDATE_METADATA_MISMATCH", key)
    rec = payload.get("authority_reconciliation", {})
    expected_counts = {"requirements_total": 25, "retained_contracts": 9, "elaborated_contracts": 16, "source_obligations": 21, "acceptance_criteria": 32, "decision_clauses": 124}
    for key, expected in expected_counts.items():
        if rec.get(key) != expected:
            fail("RECONCILIATION_COUNT_MISMATCH", key)
    if set(rec.get("requirement_ids", [])) != REQUIREMENTS or len(rec.get("requirement_ids", [])) != 25:
        fail("REQUIREMENT_SET_MISMATCH", "25 exact IDs required")
    selections = rec.get("effective_selections", {})
    if selections != {
        "V23-P2D-VS001-ACCEPTANCE-DEC-001": "OPT-PUBLISHED-STOREFRONT-ELIGIBLE",
        "V23-P2D-VS001-ACCEPTANCE-DEC-002": "OPT-MINIMUM-COMMERCIAL-DISPLAY-WITH-PRICE",
        "V23-P2D-VS001-ACCEPTANCE-DEC-003": "OPT-STABLE-SLUG-UNIFORM-NOT-FOUND",
    }:
        fail("GOVERNING_SELECTION_MISMATCH", repr(selections))
    audit = payload.get("technical_decision_audit", [])
    if len(audit) != 25 or {item.get("audit_id") for item in audit} != {f"TDA-{number:03d}" for number in range(1, 26)}:
        fail("TECHNICAL_AUDIT_INVENTORY_MISMATCH", str(len(audit)))
    for item in audit:
        if item.get("classification") not in {"A", "B", "C", "D"} or not item.get("topic") or not item.get("disposition"):
            fail("TECHNICAL_AUDIT_RECORD_INCOMPLETE", item.get("audit_id", "?"))
        if item["classification"] == "C" and item.get("decision_id") not in DECISION_OPTIONS:
            fail("TYPE_C_DECISION_MAPPING_MISSING", item["audit_id"])
        if item["classification"] != "C" and item.get("decision_id") is not None:
            fail("NON_TYPE_C_DECISION_MAPPING", item["audit_id"])
    decisions = payload.get("decisions", [])
    if {item.get("decision_id") for item in decisions} != set(DECISION_OPTIONS) or len(decisions) != 9:
        fail("DECISION_SET_MISMATCH", str(len(decisions)))
    all_option_ids: set[str] = set()
    for decision in decisions:
        decision_id = decision["decision_id"]
        if decision.get("classification") != "C" or decision.get("selected_option") is not None:
            fail("DECISION_PENDING_STATE_MISMATCH", decision_id)
        options = decision.get("options", [])
        option_ids = {item.get("option_id") for item in options}
        if len(options) != 3 or option_ids != DECISION_OPTIONS[decision_id]:
            fail("DECISION_OPTION_SET_MISMATCH", decision_id)
        if all_option_ids & option_ids:
            fail("DUPLICATE_GLOBAL_OPTION_ID", decision_id)
        all_option_ids |= option_ids
        if decision.get("recommended_option") not in option_ids:
            fail("RECOMMENDED_OPTION_MISSING", decision_id)
        for field in ("title", "question", "why_human", "recommendation_rationale"):
            if not isinstance(decision.get(field), str) or len(decision[field].strip()) < 24:
                fail("DECISION_SEMANTIC_FIELD_INCOMPLETE", f"{decision_id}:{field}")
        if not decision.get("source_authorities") or not set(decision["source_authorities"]) <= set(AUTHORITIES):
            fail("DECISION_AUTHORITY_INVALID", decision_id)
        if not decision.get("impacted_acceptance") or not set(decision["impacted_acceptance"]) <= REQUIREMENTS:
            fail("DECISION_ACCEPTANCE_CONTEXT_INVALID", decision_id)
        if len(decision.get("non_inferences", [])) < 3:
            fail("DECISION_NON_INFERENCE_INCOMPLETE", decision_id)
        semantic_text = json.dumps(decision, ensure_ascii=False)
        lowered = semantic_text.lower()
        if any(token in lowered for token in BANNED_GENERIC):
            fail("GENERIC_DECISION_SEMANTICS", decision_id)
        for token in REQUIRED_TOKENS[decision_id]:
            if token.lower() not in lowered:
                fail("REQUIRED_DECISION_SEMANTIC_MISSING", f"{decision_id}:{token}")
        for option in options:
            for field in ("summary", "contract", "impact", "rejection_tradeoff"):
                if not isinstance(option.get(field), str) or len(option[field].strip()) < 24:
                    fail("OPTION_SEMANTIC_FIELD_INCOMPLETE", f"{option.get('option_id')}:{field}")
    accounting = payload.get("decision_accounting", {})
    if accounting != {"total": 9, "selected": 0, "pending": 9, "options_per_decision": 3, "type_c_audit_topics": 18, "implementation_contract_blocked": True}:
        fail("DECISION_ACCOUNTING_MISMATCH", repr(accounting))
    blocker = payload.get("implementation_contract_blocker", {})
    if blocker.get("code") != "HUMAN_PHASE_2D_VS001_IMPLEMENTATION_DECISION_REQUIRED" or "Nine unresolved Type C" not in blocker.get("reason", ""):
        fail("IMPLEMENTATION_BLOCKER_MISMATCH", repr(blocker))
    text = json.dumps(payload, ensure_ascii=False)
    if '"runtime_evidence_status": "PASS"' in text or '"implementation_authorized": true' in text:
        fail("PREMATURE_EXECUTION_OR_AUTHORIZATION", "payload")
    return {"decisions": 9, "options": 27, "selected": 0, "audit": 25, "type_c": 18}


MARKER_RE = re.compile(rb"<!-- (METADATA_JSON|RECONCILIATION_JSON|AUDIT_JSON|DECISION_JSON|BLOCKER_JSON|NON_CLAIMS_JSON):([^ ]+) -->\n```json\n(.*?)\n```", re.S)


def validate_markdown(payload: dict, data: bytes) -> dict:
    if not data.endswith(b"\n") or data.endswith(b"\n\n"):
        fail("MARKDOWN_EOF_MISMATCH", "exactly one newline required")
    if any(line.rstrip(b" \t") != line for line in data.splitlines()):
        fail("MARKDOWN_TRAILING_WHITESPACE", "found")
    records = [(m.group(1).decode(), m.group(2).decode(), json.loads(m.group(3))) for m in MARKER_RE.finditer(data)]
    expected_metadata = {key: payload[key] for key in ["candidate_id", "status", "approval", "implementation_authorized", "runtime_evidence_status", "implementation_contract_created", "governing_commit", "next_gate"]}
    expected = [
        ("METADATA_JSON", payload["candidate_id"], expected_metadata),
        ("RECONCILIATION_JSON", "ACCEPTED_AUTHORITY", payload["authority_reconciliation"]),
        ("AUDIT_JSON", "TECHNICAL_DECISION_AUDIT", payload["technical_decision_audit"]),
    ]
    expected.extend(("DECISION_JSON", item["decision_id"], item) for item in payload["decisions"])
    expected.extend([
        ("BLOCKER_JSON", "IMPLEMENTATION_CONTRACT", payload["implementation_contract_blocker"]),
        ("NON_CLAIMS_JSON", "IMPLEMENTATION_DECISION_C1", payload["non_claims"]),
    ])
    if records != expected:
        fail("MARKDOWN_SEMANTIC_PROJECTION_MISMATCH", f"{len(records)}/{len(expected)}")
    required = ["# VS001 Implementation Decision C1 Candidate", "- Implementation authorized: `false`", "- Runtime evidence: `NOT_EXECUTED`", "HUMAN_PHASE_2D_VS001_IMPLEMENTATION_DECISION_REQUIRED"]
    decoded = data.decode()
    for token in required:
        if token not in decoded:
            fail("MARKDOWN_REQUIRED_FACT_MISSING", token)
    return {"markdown_projections": len(records)}


def validate_manifest(payload: dict, manifest: dict, files: dict[str, bytes]) -> dict:
    expected = {
        "candidate_id": payload["candidate_id"], "status": "CANDIDATE", "approval": "PENDING_HUMAN_APPROVAL",
        "implementation_authorized": False, "runtime_evidence_status": "NOT_EXECUTED", "implementation_contract_created": False,
        "next_gate": "HUMAN_PHASE_2D_VS001_IMPLEMENTATION_DECISION_REQUIRED", "decisions": 9, "selected_options": 0,
        "options_per_decision": 3, "type_c_blockers": 9, "self_reference_policy": "MANIFEST_HASH_AND_GIT_TREE_ARE_DETACHED_GATE_OUTPUTS",
        "staged_tree": None, "git_content_aggregate": None,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            fail("MANIFEST_STATE_MISMATCH", key)
    declared = manifest.get("working_file_sha256", {})
    expected_paths = set(FILES) - {FILES[2]}
    if set(declared) != expected_paths:
        fail("MANIFEST_HASH_INVENTORY_MISMATCH", repr(set(declared)))
    for path in expected_paths:
        if declared[path] != sha(files[path]):
            fail("MANIFEST_FILE_HASH_MISMATCH", path)
    generated = aggregate(files, [FILES[1], FILES[0]])
    if manifest.get("generated_payload_aggregate") != generated:
        fail("MANIFEST_GENERATED_AGGREGATE_MISMATCH", generated)
    return {"generated_payload_aggregate": generated, "stored_pass_trust": 0, "circular_hash": 0}


def lifecycle_files() -> tuple[str, dict[str, bytes], str | None]:
    head = run("git", "rev-parse", "HEAD").decode().strip()
    staged = set(run("git", "diff", "--cached", "--name-only").decode().splitlines())
    status = set(run("git", "status", "--porcelain=v1", "--untracked-files=all").decode().splitlines())
    expected = set(FILES)
    if head == GOVERNING and staged == expected:
        if status != {f"A  {path}" for path in expected}:
            fail("STAGED_LIFECYCLE_DIRTY", repr(status))
        # Tree materialization is a detached human-gate operation. Avoid
        # acquiring index.lock from a read-only validator subprocess.
        return "STAGED_OVER_GOVERNING", {path: run("git", "show", f":{path}") for path in FILES}, None
    if head == GOVERNING and not staged and status == {f"?? {path}" for path in expected}:
        return "WORKING_UNTRACKED_OVER_GOVERNING", {path: (ROOT / path).read_bytes() for path in FILES}, None
    try:
        parent = run("git", "rev-parse", "HEAD^").decode().strip()
    except subprocess.CalledProcessError:
        parent = ""
    if parent == GOVERNING and not status:
        delta = set(run("git", "diff", "--name-only", "HEAD^", "HEAD").decode().splitlines())
        if delta != expected:
            fail("COMMITTED_LIFECYCLE_INVENTORY_MISMATCH", repr(delta))
        return "COMMITTED_CANDIDATE", {path: git_bytes(head, path) for path in FILES}, run("git", "rev-parse", "HEAD^{tree}").decode().strip()
    fail("CANDIDATE_LIFECYCLE_INVALID", f"{head}:{status}")


def validate_all() -> dict:
    mode, files, tree = lifecycle_files()
    payload = json.loads(files[FILES[1]])
    if sha(files[FILES[1]]) != EXPECTED_CANONICAL_SHA256 and EXPECTED_CANONICAL_SHA256 != "TO_BE_FROZEN_AFTER_AUTHORING":
        fail("CANONICAL_JSON_HASH_MISMATCH", sha(files[FILES[1]]))
    authority = validate_authorities(payload)
    semantic = validate_payload(payload)
    markdown = validate_markdown(payload, files[FILES[0]])
    manifest = validate_manifest(payload, json.loads(files[FILES[2]]), files)
    protected = [path for path in run("git", "diff", "--name-only", GOVERNING, "HEAD").decode().splitlines() if path and path not in FILES] if mode == "COMMITTED_CANDIDATE" else []
    if protected:
        fail("PROTECTED_OR_IMPLEMENTATION_CHANGE", repr(protected))
    return {
        "result": "VALID_V23_P2D_VS001_IMPLEMENTATION_DECISION_C1",
        "lifecycle_mode": mode, "tree": tree, "candidate_files": 6,
        **authority, **semantic, **markdown, **manifest,
        "candidate_derived_authorities": 0, "builder_imported_or_called": 0,
        "implementation_changes": 0, "runtime_evidence_claims": 0,
    }


def main() -> None:
    try:
        result = validate_all()
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        print("VALID_V23_P2D_VS001_IMPLEMENTATION_DECISION_C1")
    except (ValidationFailure, KeyError, ValueError, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        print(f"INVALID_V23_P2D_VS001_IMPLEMENTATION_DECISION_C1: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
