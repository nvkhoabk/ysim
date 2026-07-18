#!/usr/bin/env python3
"""Independent final validator for VS001 Acceptance Elaboration C2-R2.

This module deliberately does not import or execute the builder.  Decision
rules and the blocked R1 baseline are loaded from Git objects; Markdown facts
are parsed independently from the canonical JSON.
"""

from __future__ import annotations

import hashlib
import difflib
import itertools
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "docs/baselines/v2.3/phase-2d"
SOURCE = DOC / "vs001-acceptance-elaboration-c2-r2.json"
MARKDOWN = DOC / "VS001_ACCEPTANCE_ELABORATION_C2_R2_CANDIDATE.md"
MANIFEST = DOC / "vs001-acceptance-elaboration-c2-r2-manifest.json"
BUILDER = ROOT / "scripts/docs/build-phase-2d-vs001-acceptance-elaboration-c2-r2.py"
VALIDATOR = ROOT / "scripts/docs/validate-phase-2d-vs001-acceptance-elaboration-c2-r2.py"
TESTS = ROOT / "scripts/docs/tests/test-phase-2d-vs001-acceptance-elaboration-c2-r2.py"

GOVERNING = "c818d734049fbf8997a5dce4e1e66e65d6a92f59"
DECISION_CANDIDATE = "f003eca82512887a616c4ee83ed4ab8da4432b8a"
DECISION_PATH = "docs/baselines/v2.3/phase-2d/vs001-acceptance-decision-c1.json"
APPROVAL_PATH = "docs/baselines/v2.3/phase-2d/VS001_ACCEPTANCE_DECISION_C1_APPROVAL.md"
DECISION_ID = "V23-P2D-VS001-ACCEPTANCE-DEC-001"
OPTION_ID = "OPT-PUBLISHED-STOREFRONT-ELIGIBLE"
DECISION_2_ID = "V23-P2D-VS001-ACCEPTANCE-DEC-002"
OPTION_2_ID = "OPT-MINIMUM-COMMERCIAL-DISPLAY-WITH-PRICE"
DECISION_3_ID = "V23-P2D-VS001-ACCEPTANCE-DEC-003"
OPTION_3_ID = "OPT-STABLE-SLUG-UNIFORM-NOT-FOUND"
AUTHORITY_OWNER = "V23-P2D-VS001-ACCEPTANCE-DECISION-C1"
R1_REF = "refs/ysim-backups/v2.3/phase-2d-vs001-acceptance-elaboration-c2-r1-final-audit-blocked"
R1_OBJECT = "4f02f5013548cab236573c4c462244e5b5f16832"
R1_TREE = "81915967e7befc7976c0d1f458a22432f35b9a6f"
R1_JSON_PATH = "docs/baselines/v2.3/phase-2d/vs001-acceptance-elaboration-c2-r1.json"
DEC1_REF = "refs/ysim-backups/v2.3/phase-2d-vs001-acceptance-elaboration-c2-r2-dec001"
DEC1_OBJECT = "1a5b1732ff517dcf91dd2aef0591b345583af48f"
DEC1_TREE = "c85d5c887e141f5b9e666714e68bca7825d68764"
DEC1_JSON_PATH = "docs/baselines/v2.3/phase-2d/vs001-acceptance-elaboration-c2-r2.json"
DEC2_REF = "refs/ysim-backups/v2.3/phase-2d-vs001-acceptance-elaboration-c2-r2-dec002"
DEC2_OBJECT = "c7ae7b91be7e4a46b0ea14bcebc15c0e59327a78"
DEC2_TREE = "b62c148e7738d8b762c8367d4865aa6c1335279a"
DEC3_REF = "refs/ysim-backups/v2.3/phase-2d-vs001-acceptance-elaboration-c2-r2-dec003"
DEC3_OBJECT = "87c93864538b20a61e40c9038ebe5b1082fd3cb5"
DEC3_TREE = "eb6cc3a2729858eb39fe46168aa94a9f6e9cf14d"
REGISTRY_PATH = "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-registry.json"
RETAINED_CANDIDATE = "120184748c70543b86220fb4f3f3089e99d175dc"
RETAINED_ACCEPTED = "374a808d3749dfda97a9d9534e4d798cbd6ae05a"
RETAINED_PARENT = "9a49377d9fcd3d25e922b80cc6af3a4474ec0975"
RETAINED_TREE = "364bb5e4c327e1c49af07fb50eed548e89a49cda"
RETAINED_PATH = "docs/baselines/v2.3/phase-2/semantic-acceptance-renderer-c2-reference-good-contracts.json"
RETAINED_APPROVAL_PATH = "docs/baselines/v2.3/phase-2/PHASE_2C_SEMANTIC_ACCEPTANCE_RENDERER_C2_APPROVAL.md"

EXPECTED_FILES = [
    "docs/baselines/v2.3/phase-2d/VS001_ACCEPTANCE_ELABORATION_C2_R2_CANDIDATE.md",
    "docs/baselines/v2.3/phase-2d/vs001-acceptance-elaboration-c2-r2.json",
    "docs/baselines/v2.3/phase-2d/vs001-acceptance-elaboration-c2-r2-manifest.json",
    "scripts/docs/build-phase-2d-vs001-acceptance-elaboration-c2-r2.py",
    "scripts/docs/validate-phase-2d-vs001-acceptance-elaboration-c2-r2.py",
    "scripts/docs/tests/test-phase-2d-vs001-acceptance-elaboration-c2-r2.py",
]
SOURCE_PATH = EXPECTED_FILES[1]
ELABORATED = {
    "BD-02-001", "BD-02-002", "BD-04-001", "BD-04-002", "BD-04-003",
    "BRD-WS-04-R001", "BD-05-001", "UXF-003", "UXF-301", "UXF-304",
    "UXF-306", "UXF-04-R011", "UXF-05-R004", "UXF-05-R010",
    "UXF-05-R018", "UXF-05-R056",
}
RETAINED = {
    "BRD-UPDATE-01-R001", "BRD-WS-02-R002", "BRD-WS-02-R003", "BD-04-005",
    "UXF-010", "UXF-011", "UXF-109", "UXF-402", "UXF-405",
}
SLICE_REQUIREMENTS = ELABORATED | RETAINED
PASS_KEYS = {
    "approval_ready", "retained_git_object_verification_complete",
    "full_63_mutation_gate_complete", "final_clean_checkout_complete",
    "final_mutation_gate_complete",
}
EXPECTED_SEMANTIC_HASHES = {
    DECISION_ID: "8ee06f257034ec896452360a51e6d0f9d6a23614a50882037ee0077757872339",
    DECISION_2_ID: "d9d0f66add0cb24b16ad75bfee7872b5a88fa85c4ae6e7c437037234e2bd9f99",
    DECISION_3_ID: "94d784a1ab858d2798c29c46a57a712648e484287c180c875ffc090e136b662d",
}
REQUIRED_CONTRACT_FIELDS = {
    "requirement_id", "source_document", "source_section", "source_range", "source_statement",
    "source_fingerprint", "semantic_anchors", "source_context_summary", "obligation_mapping",
    "applicable_decision_rules", "preconditions", "controlled_fixtures", "acceptance_criteria",
    "positive_outcomes", "prohibited_outcomes", "boundary_cases", "evidence_contract",
    "failure_semantics", "non_inferences", "technical_choices_deferred", "runtime_evidence_status",
    "implementation_authorized", "decision_clause_links",
}
GENERIC = (
    "works as expected", "behaves as expected", "correct result is returned",
    "appropriate evidence is recorded", "relevant boundary is handled",
    "system is configured correctly", "slug is handled correctly",
    "return not found",
)
UNIFORM_RULES = {"NO_PUBLIC_FAILURE_REASON", "INTERNAL_REASON_AUDIT_ONLY"}
UNIFORM_POPULATION_RULES = {
    "UNKNOWN_SLUG", "MALFORMED_SLUG", "WRONG_STOREFRONT", "PRODUCT_INACTIVE",
    "PRODUCT_RETIRED_OR_DELETED", "PRODUCT_UNPUBLISHED", "CATALOG_ENTRY_INACTIVE",
    "PUBLICATION_WINDOW_INVALID", "PUBLICATION_VALIDATION_NOT_PASS", "PRODUCT_VERSION_INVALID",
    "REFERENCE_INVALID", "PRICE_UNRESOLVED", "SCOPE_NOT_ACTIVE", "ANY_DEC001_PREDICATE_FAILED",
}
UNIFORM_RULES |= UNIFORM_POPULATION_RULES | {
    "HTTP_STATUS_404", "ERROR_CODE_PRODUCT_NOT_FOUND", "UNIFORM_PUBLIC_RESPONSE_SCHEMA",
    "NO_PUBLIC_UNKNOWN_UNAVAILABLE_DISTINCTION",
}


class ValidationError(Exception):
    def __init__(self, code: str, detail: str):
        self.code, self.detail = code, detail
        super().__init__(f"{code}: {detail}")


def fail(code: str, detail: str) -> None:
    raise ValidationError(code, detail)


def run(*args: str) -> bytes:
    return subprocess.check_output(args, cwd=ROOT)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_sha(value: object) -> str:
    return sha((json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode())


def git_bytes(commit: str, path: str) -> bytes:
    try:
        return run("git", "show", f"{commit}:{path}")
    except subprocess.CalledProcessError as exc:
        fail("GIT_AUTHORITY_OBJECT_MISSING", f"{commit}:{path}: {exc}")


def parse_range(value: str) -> tuple[int, int]:
    match = re.fullmatch(r"L(\d+)(?:-L(\d+))?", value or "")
    if not match:
        fail("PHYSICAL_SOURCE_RANGE_INVALID", value or "")
    return int(match.group(1)), int(match.group(2) or match.group(1))


def load_authorities() -> dict:
    head = run("git", "rev-parse", "HEAD").decode().strip()
    if head != GOVERNING:
        try:
            parent = run("git", "rev-parse", "HEAD^").decode().strip()
        except subprocess.CalledProcessError:
            parent = ""
        if parent != GOVERNING:
            fail("GOVERNING_HEAD_MISMATCH", "neither HEAD nor candidate parent is accepted Decision C1")
    if run("git", "rev-parse", f"{GOVERNING}^").decode().strip() != DECISION_CANDIDATE:
        fail("DECISION_LIFECYCLE_MISMATCH", "accepted Decision C1 direct parent changed")
    approval = git_bytes(GOVERNING, APPROVAL_PATH).decode()
    if (
        "Decision: APPROVED" not in approval
        or "Candidate commit: f003eca82512887a616c4ee83ed4ab8da4432b8a" not in approval
        or "Approver: Khoa, Nguyen" not in approval
        or OPTION_ID not in approval
        or OPTION_2_ID not in approval
        or OPTION_3_ID not in approval
    ):
        fail("DETACHED_DECISION_APPROVAL_MISMATCH", "effective DEC-001/DEC-002/DEC-003 selections are not signed")
    decision_raw = git_bytes(DECISION_CANDIDATE, DECISION_PATH)
    decision_payload = json.loads(decision_raw)
    rules, order = {}, []
    for decision_id, option_id, prefix in (
        (DECISION_ID, OPTION_ID, "DEC001"),
        (DECISION_2_ID, OPTION_2_ID, "DEC002"),
        (DECISION_3_ID, OPTION_3_ID, "DEC003"),
    ):
        decision_index = next((i for i, d in enumerate(decision_payload["decisions"]) if d["decision_id"] == decision_id), None)
        if decision_index is None:
            fail("DECISION_CANDIDATE_STATE_MISMATCH", decision_id)
        decision = decision_payload["decisions"][decision_index]
        if decision["selected_option"] is not None or decision["recommended_option"] != option_id:
            fail("DECISION_CANDIDATE_STATE_MISMATCH", decision_id)
        option_index = next((i for i, o in enumerate(decision["options"]) if o["option_id"] == option_id), None)
        if option_index is None:
            fail("DECISION_OPTION_MISSING", option_id)
        option = decision["options"][option_index]
        for group, group_rules in option["canonical_rule_groups"].items():
            for index, rule in enumerate(group_rules):
                rid = rule["rule_id"]
                key = f"{decision_id}|{rid}"
                if key in rules:
                    fail("AUTHORITATIVE_RULE_DUPLICATE", key)
                path = f"/decisions/{decision_index}/options/{option_index}/canonical_rule_groups/{group}/{index}"
                rules[key] = {
                    "rule": rule, "fingerprint": canonical_sha(rule), "path": path, "group": group,
                    "decision_id": decision_id, "option_id": option_id, "prefix": prefix, "rule_id": rid,
                }
                order.append(key)
    if len(rules) != 124:
        fail("AUTHORITATIVE_RULE_COUNT_MISMATCH", str(len(rules)))
    if run("git", "rev-parse", R1_REF).decode().strip() != R1_OBJECT:
        fail("R1_BACKUP_OBJECT_MISMATCH", R1_REF)
    if run("git", "rev-parse", f"{R1_REF}^{{tree}}").decode().strip() != R1_TREE:
        fail("R1_BACKUP_TREE_MISMATCH", R1_REF)
    r1 = json.loads(git_bytes(R1_REF, R1_JSON_PATH))
    if run("git", "rev-parse", DEC1_REF).decode().strip() != DEC1_OBJECT:
        fail("DEC001_CHECKPOINT_OBJECT_MISMATCH", DEC1_REF)
    if run("git", "rev-parse", f"{DEC1_REF}^{{tree}}").decode().strip() != DEC1_TREE:
        fail("DEC001_CHECKPOINT_TREE_MISMATCH", DEC1_REF)
    dec1_checkpoint = json.loads(git_bytes(DEC1_REF, DEC1_JSON_PATH))
    if run("git", "rev-parse", DEC2_REF).decode().strip() != DEC2_OBJECT:
        fail("DEC002_CHECKPOINT_OBJECT_MISMATCH", DEC2_REF)
    if run("git", "rev-parse", f"{DEC2_REF}^{{tree}}").decode().strip() != DEC2_TREE:
        fail("DEC002_CHECKPOINT_TREE_MISMATCH", DEC2_REF)
    dec2_checkpoint = json.loads(git_bytes(DEC2_REF, DEC1_JSON_PATH))
    if run("git", "rev-parse", DEC3_REF).decode().strip() != DEC3_OBJECT:
        fail("DEC003_CHECKPOINT_OBJECT_MISMATCH", DEC3_REF)
    if run("git", "rev-parse", f"{DEC3_REF}^{{tree}}").decode().strip() != DEC3_TREE:
        fail("DEC003_CHECKPOINT_TREE_MISMATCH", DEC3_REF)
    dec3_checkpoint = json.loads(git_bytes(DEC3_REF, DEC1_JSON_PATH))
    if run("git", "rev-parse", f"{RETAINED_ACCEPTED}^").decode().strip() != RETAINED_CANDIDATE:
        fail("RETAINED_LIFECYCLE_MISMATCH", RETAINED_ACCEPTED)
    if run("git", "rev-parse", f"{RETAINED_CANDIDATE}^").decode().strip() != RETAINED_PARENT:
        fail("RETAINED_LIFECYCLE_MISMATCH", RETAINED_CANDIDATE)
    if run("git", "rev-parse", f"{RETAINED_CANDIDATE}^{{tree}}").decode().strip() != RETAINED_TREE:
        fail("RETAINED_TREE_MISMATCH", RETAINED_CANDIDATE)
    retained_raw = git_bytes(RETAINED_CANDIDATE, RETAINED_PATH)
    retained_payload = json.loads(retained_raw)
    retained_records = {record["requirement_id"]: (index, record) for index, record in enumerate(retained_payload["records"])}
    retained_oid = run("git", "rev-parse", f"{RETAINED_CANDIDATE}:{RETAINED_PATH}").decode().strip()
    renderer_approval = git_bytes(RETAINED_ACCEPTED, RETAINED_APPROVAL_PATH).decode()
    if RETAINED_CANDIDATE not in renderer_approval:
        fail("RETAINED_APPROVAL_MISMATCH", RETAINED_CANDIDATE)
    registry_payload = json.loads(git_bytes(GOVERNING, REGISTRY_PATH))
    registry = {record["stable_id"]: record for record in registry_payload["requirements"]}
    return {
        "rules": rules, "order": order, "r1": r1,
        "dec1_checkpoint": dec1_checkpoint, "dec2_checkpoint": dec2_checkpoint,
        "dec3_checkpoint": dec3_checkpoint, "decision_sha": sha(decision_raw),
        "registry": registry, "retained_records": retained_records,
        "retained_raw": retained_raw, "retained_oid": retained_oid,
    }


def all_contracts(payload: dict):
    found = []
    for batch in ("batch_1_contracts", "batch_2_contracts", "batch_3_contracts"):
        for index, contract in enumerate(payload.get(batch, [])):
            found.append((batch, index, contract))
    ids = [c["requirement_id"] for _, _, c in found]
    if len(ids) != 16 or len(set(ids)) != 16 or set(ids) != ELABORATED:
        fail("ELABORATED_REQUIREMENT_SET_MISMATCH", repr(ids))
    return found


def _source_semantics(contract: dict) -> dict:
    value = json.loads(json.dumps(contract))
    value.pop("decision_rule_enforcements", None)
    value.pop("decision_clause_links", None)
    return value


def validate_preservation(payload: dict, authorities: dict) -> None:
    r1 = authorities["r1"]
    old = {c["requirement_id"]: c for _, _, c in all_contracts(r1)}
    new = {c["requirement_id"]: c for _, _, c in all_contracts(payload)}
    for rid in sorted(ELABORATED):
        if _source_semantics(old[rid]) != _source_semantics(new[rid]):
            fail("SOURCE_CONTRACT_SEMANTICS_CHANGED", rid)
    old_obligations = sum(len(c["obligation_mapping"]) for c in old.values())
    new_obligations = sum(len(c["obligation_mapping"]) for c in new.values())
    if (old_obligations, new_obligations) != (21, 21):
        fail("SOURCE_OBLIGATION_PRESERVATION_MISMATCH", f"{old_obligations}/{new_obligations}")
    old_retained = {r["requirement_id"]: r["canonical_contract_sha256"] for r in r1["retained_contracts"]}
    new_retained = {r["requirement_id"]: r["canonical_contract_sha256"] for r in payload["retained_contracts"]}
    if old_retained != new_retained or len(new_retained) != 9:
        fail("RETAINED_CONTRACT_IDENTITY_CHANGED", "retained canonical hashes differ from blocked R1")
    checkpoint = [c for c in authorities["dec1_checkpoint"]["decision_derived_acceptance_clauses"] if c["decision_id"] == DECISION_ID]
    current = [c for c in payload["decision_derived_acceptance_clauses"] if c["decision_id"] == DECISION_ID]
    if len(checkpoint) != 27 or current != checkpoint:
        fail("DEC001_CLAUSE_SEMANTICS_CHANGED", "DEC-001 canonical clauses differ from Batch A checkpoint")
    checkpoint2 = [c for c in authorities["dec2_checkpoint"]["decision_derived_acceptance_clauses"] if c["decision_id"] == DECISION_2_ID]
    current2 = [c for c in payload["decision_derived_acceptance_clauses"] if c["decision_id"] == DECISION_2_ID]
    if len(checkpoint2) != 54 or current2 != checkpoint2:
        fail("DEC002_CLAUSE_SEMANTICS_CHANGED", "DEC-002 canonical clauses differ from Batch B checkpoint")
    checkpoint3 = [c for c in authorities["dec3_checkpoint"]["decision_derived_acceptance_clauses"] if c["decision_id"] == DECISION_3_ID]
    current3 = [c for c in payload["decision_derived_acceptance_clauses"] if c["decision_id"] == DECISION_3_ID]
    if len(checkpoint3) != 43 or current3 != checkpoint3:
        fail("DEC003_CLAUSE_SEMANTICS_CHANGED", "DEC-003 canonical clauses differ from Batch C checkpoint")
    for decision_id, clauses in ((DECISION_ID, current), (DECISION_2_ID, current2), (DECISION_3_ID, current3)):
        digest = sha(json.dumps(clauses, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode())
        if digest != EXPECTED_SEMANTIC_HASHES[decision_id]:
            fail("DECISION_SEMANTIC_OBJECT_HASH_MISMATCH", decision_id)


def validate_metadata(payload: dict) -> None:
    expected = {
        "candidate_id": "V23-P2D-VS001-ACCEPTANCE-ELABORATION-C2-R2",
        "supersedes": "V23-P2D-VS001-ACCEPTANCE-ELABORATION-C2-R1",
        "supersession_reason": "SYSTEMIC_TEMPLATE_RULE_WRAPPERS_WRONG_REASON_MUTATIONS_AND_BUILDER_CONFORMANCE_GAP",
        "status": "CANDIDATE",
        "approval": "PENDING_HUMAN_APPROVAL",
        "approval_ready": True,
        "next_gate": "HUMAN_PHASE_2D_VS001_ACCEPTANCE_ELABORATION_C2_R2_CANDIDATE_REVIEW",
        "runtime_evidence_status": "NOT_EXECUTED",
        "implementation_authorized": False,
        "correction_pass": 2,
    }
    for key, value in expected.items():
        if payload.get(key) != value:
            fail("CANDIDATE_METADATA_MISMATCH", f"{key}: {payload.get(key)!r}")
    population = payload.get("population", {})
    expected_population = {
        "total": 25, "retained": 9, "elaborated": 16, "governing_decisions": 3,
        "acceptance_coverage": 25, "source_verification": 25,
        "runtime_evidence_executed": 0, "unresolved_contracts": 0,
        "invalid_or_blocked_contracts": 0,
    }
    if any(population.get(key) != value for key, value in expected_population.items()):
        fail("POPULATION_ACCOUNTING_MISMATCH", repr(population))
    choices = {d["decision_id"]: d["selected_option"] for d in payload.get("governing_decisions", [])}
    if choices.get(DECISION_ID) != OPTION_ID or choices.get(DECISION_2_ID) != OPTION_2_ID or choices.get(DECISION_3_ID) != OPTION_3_ID or len(choices) != 3:
        fail("EFFECTIVE_DECISION_SELECTION_MISMATCH", repr(choices))
    all_contracts(payload)


def validate_retained(payload: dict, authorities: dict) -> dict:
    records = payload.get("retained_contracts", [])
    ids = [record.get("requirement_id") for record in records]
    if len(ids) != 9 or set(ids) != RETAINED:
        fail("RETAINED_REQUIREMENT_SET_MISMATCH", repr(ids))
    for declared in records:
        rid = declared["requirement_id"]
        if set(declared) != {
            "requirement_id", "canonical_contract_sha256", "signed_legacy_contract_provenance",
            "independently_recomputed_current_source_provenance",
        }:
            fail("LEGACY_CURRENT_PROVENANCE_CONFLATION", rid)
        index, signed_record = authorities["retained_records"][rid]
        contract = signed_record["acceptance_contract"]
        expected_contract_hash = canonical_sha(contract)
        if declared["canonical_contract_sha256"] != expected_contract_hash or signed_record.get("contract_sha256") != expected_contract_hash:
            fail("RETAINED_CONTRACT_HASH_MISMATCH", rid)
        legacy = declared["signed_legacy_contract_provenance"]
        expected_legacy = {
            "renderer_lifecycle_id": "V23-P2C-SEMANTIC-ACCEPTANCE-RENDERER-C2",
            "renderer_candidate_commit": RETAINED_CANDIDATE,
            "renderer_accepted_commit": RETAINED_ACCEPTED,
            "signed_tree": RETAINED_TREE,
            "signed_blob_oid": authorities["retained_oid"],
            "signed_blob_sha256": sha(authorities["retained_raw"]),
            "repository_path": RETAINED_PATH,
            "canonical_json_path": f"records[{index}].acceptance_contract",
            "signed_canonical_contract_sha256": expected_contract_hash,
            "detached_approval_identity": "VALID_APPROVED_PHASE_2C_SEMANTIC_ACCEPTANCE_RENDERER_C2",
        }
        for key, expected in expected_legacy.items():
            if legacy.get(key) != expected:
                fail("RETAINED_LEGACY_IDENTITY_MISMATCH", f"{rid}:{key}")
        signed_provenance = contract.get("provenance", {})
        legacy_fields = legacy.get("legacy_registry_fields", {})
        for field, source_field in (
            ("source_document", "source_document"), ("source_section", "source_section"),
            ("source_range", "source_lines"), ("source_fingerprint", "source_fingerprint"),
        ):
            if legacy_fields.get(field) != signed_provenance.get(source_field):
                fail("RETAINED_LEGACY_REGISTRY_MISMATCH", f"{rid}:{field}")
        current = declared["independently_recomputed_current_source_provenance"]
        if current.get("authoritative_source_lifecycle_commit") != GOVERNING:
            fail("CURRENT_SOURCE_LIFECYCLE_MISMATCH", rid)
        path = current.get("git_path", "")
        blob = git_bytes(GOVERNING, path)
        oid = run("git", "rev-parse", f"{GOVERNING}:{path}").decode().strip()
        if current.get("git_blob_oid") != oid:
            fail("CURRENT_SOURCE_BLOB_MISMATCH", rid)
        start, end = parse_range(current.get("physical_statement_range", ""))
        lines = blob.splitlines(keepends=True)
        if start < 1 or end > len(lines) or start > end:
            fail("PHYSICAL_SOURCE_RANGE_INVALID", rid)
        excerpt = b"".join(lines[start - 1:end])
        if current.get("exact_statement_text") != excerpt.decode().rstrip("\n"):
            fail("PHYSICAL_SOURCE_RANGE_STATEMENT_MISMATCH", rid)
        if current.get("exact_statement_bytes_sha256") != sha(excerpt):
            fail("PHYSICAL_SOURCE_BYTES_MISMATCH", rid)
        expected_tuple = {
            "source_lifecycle_commit": GOVERNING, "git_path": path, "git_blob_oid": oid,
            "physical_statement_range": current["physical_statement_range"],
            "statement_bytes_sha256": sha(excerpt),
            "extraction_method": "HEADING_SCOPED_PHYSICAL_RANGE_V1",
        }
        if current.get("fingerprint_input_tuple") != expected_tuple:
            fail("CURRENT_SOURCE_FINGERPRINT_INPUT_MISMATCH", rid)
        if current.get("independently_recomputed_fingerprint") != canonical_sha(expected_tuple):
            fail("CURRENT_SOURCE_FINGERPRINT_MISMATCH", rid)
        source_statement = contract["typed_contract_ast"]["source_statement"]
        if current.get("normalized_normative_statement_sha256") != sha(source_statement.encode()):
            fail("CURRENT_SOURCE_NORMALIZED_STATEMENT_MISMATCH", rid)
        if current.get("extraction_method_version") != "HEADING_SCOPED_PHYSICAL_RANGE_V1":
            fail("CURRENT_SOURCE_EXTRACTION_METHOD_MISMATCH", rid)
    return {"retained": 9, "physical_ranges": 9, "current_fingerprints": 9}


def validate_sources_and_contracts(payload: dict, authorities: dict, check_preservation: bool = True) -> dict:
    if check_preservation:
        validate_preservation(payload, authorities)
    obligations = criteria = 0
    for _, _, contract in all_contracts(payload):
        rid = contract["requirement_id"]
        missing = REQUIRED_CONTRACT_FIELDS - set(contract)
        if missing:
            fail("REQUIRED_CONTRACT_FIELD_MISSING", f"{rid}:{sorted(missing)}")
        record = authorities["registry"].get(rid)
        if not record:
            fail("ACCEPTED_SOURCE_RECORD_MISSING", rid)
        provenance = record["provenance"]
        expected_fields = {
            "source_document": provenance["source_document"],
            "source_section": provenance["source_section"],
            "source_range": provenance["source_lines"],
            "source_fingerprint": provenance["source_fingerprint"],
            "source_statement": record["normative_statement"],
        }
        for field, expected in expected_fields.items():
            if contract.get(field) != expected:
                fail("AUTHORED_SOURCE_MISMATCH", f"{rid}:{field}")
        if sha(contract["source_statement"].encode()) != contract["source_fingerprint"]:
            fail("AUTHORED_SOURCE_FINGERPRINT_MISMATCH", rid)
        blob = git_bytes(GOVERNING, contract["source_document"])
        start, end = parse_range(contract["source_range"])
        lines = blob.decode("utf-8").splitlines(keepends=True)
        if start < 1 or end > len(lines) or start > end:
            fail("AUTHORED_PHYSICAL_SOURCE_RANGE_INVALID", rid)
        if contract["source_statement"] not in "".join(lines[start - 1:end]):
            fail("AUTHORED_STATEMENT_OUTSIDE_DECLARED_RANGE", rid)
        semantic_text = json.dumps({key: value for key, value in contract.items() if key not in {"source_statement", "semantic_anchors", "source_context_summary"}}, ensure_ascii=False).lower()
        if any(term in semantic_text for term in GENERIC):
            fail("GENERIC_ACCEPTANCE", rid)
        if contract["runtime_evidence_status"] != "NOT_EXECUTED" or contract["implementation_authorized"] is not False:
            fail("FALSE_RUNTIME_OR_IMPLEMENTATION_CLAIM", rid)
        obligation_ids = [item["obligation_id"] for item in contract["obligation_mapping"]]
        criterion_ids = [item["criterion_id"] for item in contract["acceptance_criteria"]]
        if len(obligation_ids) != len(set(obligation_ids)) or len(criterion_ids) != len(set(criterion_ids)):
            fail("DUPLICATE_OBLIGATION_OR_CRITERION", rid)
        referenced = set()
        for criterion in contract["acceptance_criteria"]:
            mapped = criterion.get("obligation_ids", [])
            if not mapped or not set(mapped) <= set(obligation_ids):
                fail("UNSUPPORTED_CRITERION", criterion.get("criterion_id", rid))
            referenced.update(mapped)
            if criterion.get("observed_evidence_authority") == criterion.get("expected_authority"):
                fail("EXPECTED_DERIVED_OBSERVATION", criterion["criterion_id"])
            if criterion.get("inference") is not False:
                fail("INFERENCE_NOT_FALSE", criterion["criterion_id"])
        for obligation in contract["obligation_mapping"]:
            mapped = obligation.get("criterion_ids", [])
            if not mapped or not set(mapped) <= set(criterion_ids) or obligation["obligation_id"] not in referenced:
                fail("UNCOVERED_OBLIGATION", obligation["obligation_id"])
        obligations += len(obligation_ids)
        criteria += len(criterion_ids)
    if (obligations, criteria) != (21, 32):
        fail("ELABORATED_ACCOUNTING_MISMATCH", f"{obligations}/{criteria}")
    return {"sources": 16, "authored_physical_ranges": 16, "obligations": obligations, "criteria": criteria}


def _text_values(value: object) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [s for item in value for s in _text_values(item)]
    if isinstance(value, dict):
        return [s for item in value.values() for s in _text_values(item)]
    return []


def validate_clauses(payload: dict, authorities: dict, check_similarity: bool = True) -> None:
    clauses = payload.get("decision_derived_acceptance_clauses")
    if not isinstance(clauses, list) or len(clauses) != 124:
        fail("DECISION_CLAUSE_COUNT_MISMATCH", str(len(clauses or [])))
    by_rule = {}
    for clause in clauses:
        rid = clause.get("authoritative_rule_id", "")
        key = f"{clause.get('decision_id')}|{rid}"
        if key in by_rule:
            fail("DECISION_CLAUSE_RULE_DUPLICATE", key)
        by_rule[key] = clause
    if set(by_rule) != set(authorities["rules"]):
        fail("DECISION_CLAUSE_RULE_SET_MISMATCH", repr(set(authorities["rules"]) ^ set(by_rule)))
    by_required: dict[str, list[dict]] = {}
    for clause in clauses:
        text = clause.get("concrete_assertion_or_prohibition", {}).get("required_observation", "")
        if text:
            by_required.setdefault(text, []).append(clause)
    for text, owners in by_required.items():
        if len(owners) > 1 and not all(
            c.get("decision_id") == DECISION_3_ID and c.get("authoritative_rule_id") in UNIFORM_POPULATION_RULES
            for c in owners
        ):
            fail("DUPLICATE_SEMANTIC_ASSERTION", text)
    authored_clauses = list(clauses)
    semantic_extractors = (
        lambda c: c["concrete_assertion_or_prohibition"]["required_observation"],
        lambda c: c["concrete_assertion_or_prohibition"]["prohibited_observation"],
        lambda c: c["observable_evidence_contract"]["probe"],
        lambda c: c["observable_evidence_contract"]["observed_state"],
    )
    if check_similarity:
        for left, right in itertools.combinations(authored_clauses, 2):
            if (
                left.get("decision_id") == DECISION_3_ID == right.get("decision_id")
                and left.get("authoritative_rule_id") in UNIFORM_POPULATION_RULES
                and right.get("authoritative_rule_id") in UNIFORM_POPULATION_RULES
            ):
                continue
            for extract in semantic_extractors:
                if difflib.SequenceMatcher(None, extract(left).lower(), extract(right).lower()).ratio() >= 0.80:
                    fail("UNEXPLAINED_SEMANTIC_SIMILARITY", f"{left['authoritative_rule_id']}/{right['authoritative_rule_id']}")
    for key in authorities["order"]:
        clause, auth = by_rule[key], authorities["rules"][key]
        rid = auth["rule_id"]
        prefix = f"{auth['prefix']}-{rid}"
        if clause.get("clause_id") != prefix:
            fail("CLAUSE_ID_MISMATCH", rid)
        checks = {
            "decision_id": auth["decision_id"], "selected_option_id": auth["option_id"],
            "authoritative_rule_fingerprint": auth["fingerprint"],
            "authority_owner": AUTHORITY_OWNER, "authority_commit": GOVERNING,
            "authority_git_path": DECISION_PATH, "authority_json_path": auth["path"],
            "runtime_evidence_status": "NOT_EXECUTED", "implementation_authorized": False,
        }
        for key, expected in checks.items():
            if clause.get(key) != expected:
                code = "DECISION_AUTHORITY_OWNER_MISMATCH" if key == "authority_owner" else "AUTHORITATIVE_RULE_FACT_MISMATCH"
                fail(code, f"{rid}:{key}")
        if clause.get("enforcement_type") not in {"ASSERTION", "PROHIBITION", "BOUNDARY", "NON_INFERENCE", "DEFERRED_TECHNICAL_CHOICE"}:
            fail("ENFORCEMENT_TYPE_INVALID", rid)
        contexts = clause.get("affected_requirement_contexts")
        applicability = clause.get("applicability", "")
        is_uniform = rid in {"NO_PUBLIC_FAILURE_REASON", "INTERNAL_REASON_AUDIT_ONLY"} or (
            auth["decision_id"] == DECISION_3_ID and rid in UNIFORM_RULES
        )
        conditional = rid.startswith("DETAIL_") and rid.endswith("_IF_DEFINED")
        if conditional and not applicability:
            fail("CONDITIONAL_APPLICABILITY_MISSING", rid)
        if not isinstance(contexts, list) or not contexts or any(c not in SLICE_REQUIREMENTS for c in contexts) or len(applicability) < 45:
            fail("UNRELATED_CONTEXT_OR_APPLICABILITY", rid)
        if any(key in clause for key in ("source_owner", "normative_requirement_owner")):
            fail("SOURCE_OWNERSHIP_MISSTATEMENT", rid)
        fixtures = clause.get("controlled_fixtures")
        if not isinstance(fixtures, list) or len(fixtures) < 2 or any(not f.get("controlled_state") or not f.get("independent_control") for f in fixtures):
            fail("CONTROLLED_FIXTURES_MISSING", rid)
        if conditional:
            states = " ".join(f["controlled_state"] for f in fixtures).lower()
            if not re.search(r"undefined|no .*field|lacks|absence|does not define", states):
                fail("CONDITIONAL_FALSE_FIXTURE_MISSING", rid)
        if is_uniform and (len({f["controlled_state"] for f in fixtures}) < 2):
            fail("UNIFORM_RESULT_FIXTURES_MISSING", rid)
        preconditions = clause.get("preconditions")
        if not isinstance(preconditions, list) or len(preconditions) < 2 or any(not p.get("required_state") or p.get("inference") is not False for p in preconditions):
            fail("CONCRETE_PRECONDITIONS_MISSING", rid)
        assertion = clause.get("concrete_assertion_or_prohibition", {})
        required = assertion.get("required_observation", "")
        prohibited = assertion.get("prohibited_observation", "")
        if rid == "LIST_BASE_PRICE_CURRENCY" and not required:
            fail("PRICE_AMOUNT_CURRENCY_PAIR_INCOMPLETE", rid)
        if not required:
            fail("CONCRETE_ENFORCEMENT_MISSING", rid)
        if not prohibited:
            fail("PROHIBITED_OUTCOME_MISSING", rid)
        if assertion.get("inference") is not False:
            fail("INFERENCE_NOT_FALSE", rid)
        combined = " ".join(_text_values(clause)).lower()
        if re.search(r"within\s+\S+.*accepted.*rule binds", combined):
            fail("TEMPLATE_RULE_WRAPPER", rid)
        if any(term in combined for term in GENERIC):
            fail("GENERIC_DECISION_CLAUSE", rid)
        lowered_required = required.lower()
        lowered_prohibited = prohibited.lower()
        if rid == "LIST_DETAIL_SLUG_EQUAL" and "may not differ" not in lowered_prohibited and "exactly equals" not in lowered_required:
            fail("LIST_DETAIL_SLUG_CONSISTENCY_WEAKENED", rid)
        if rid == "LIST_DETAIL_PRICE_EQUAL_WITHIN_SNAPSHOT" and "may not differ" not in lowered_prohibited and "exactly equal" not in lowered_required:
            fail("LIST_DETAIL_PRICE_CONSISTENCY_WEAKENED", rid)
        if rid == "NO_ATTRIBUTE_INFERENCE_FROM_PRODUCT_NAME" and not re.search(r"parsing|tokenizing|derive|infer", lowered_prohibited):
            fail("ATTRIBUTE_INFERENCE_PROHIBITION_WEAKENED", rid)
        if rid == "NO_PUBLIC_PURCHASE_COST" and not re.search(r"cost|purchase", lowered_prohibited):
            fail("SUPPLIER_COST_BOUNDARY_WEAKENED", rid)
        if rid in {"NO_PROMOTIONAL_PRICE", "NO_DISCOUNT", "NO_TAX_CALCULATION_OR_PRESENTATION"} and not re.search(r"must not|cannot|absent|no ", lowered_prohibited):
            fail("EXCLUDED_COMMERCIAL_FIELD_INTRODUCED", rid)
        if rid == "NO_CART_OR_PURCHASE_ACTION" and not re.search(r"must not|cannot|no cart|no purchase", lowered_prohibited):
            fail("PURCHASE_ACTION_INTRODUCED", rid)
        if rid == "NO_API_URL_DECISION" and re.search(r"selected|required|approved", lowered_required) and re.search(r"/[a-z]", lowered_required):
            fail("TECHNICAL_CHOICE_PREMATURELY_SELECTED", rid)
        if auth["decision_id"] == DECISION_3_ID:
            if re.search(r"\b(is|are) accepted\b|\bis allowed\b|\bmay be accepted\b|\bmay resolve\b|\bcan resolve\b|\bis permitted\b", lowered_prohibited):
                fail("DEC003_PROHIBITION_REVERSED", rid)
            if re.search(r"/[a-z].*(approved|selected|required)|(approved|selected|required).*/[a-z]", lowered_required):
                fail("TECHNICAL_CHOICE_PREMATURELY_SELECTED", rid)
            required_tokens = {
                "SLUG_LOWERCASE": ("uppercase", "lower"),
                "SLUG_ASCII": ("non-ascii", "ascii"),
                "SLUG_KEBAB_CASE": ("rewritten", "kebab"),
                "SLUG_NON_EMPTY": ("empty", "non-empty"),
                "SLUG_UNIQUE_WITHIN_STOREFRONT": ("arbitrary", "one public slug"),
                "SLUG_STABLE_FOR_PUBLISHED_PRODUCT": ("replacement", "stable"),
                "SLUG_NO_DATABASE_IDENTITY": ("internal id", "internal"),
                "SLUG_NO_SUPPLIER_REFERENCE": ("supplier", "supplier"),
                "LIST_DETAIL_SLUG_CONSISTENT": ("different slug", "identical"),
                "NO_HISTORICAL_SLUG_REDIRECT": ("redirect", "historical"),
                "NO_ALIAS_RESOLUTION": ("alias", "alias"),
                "NO_WAITLIST": ("waitlist", "waitlist"),
                "NO_REPLACEMENT_RECOMMENDATION": ("replacement", "replacement"),
            }
            if rid in required_tokens:
                prohibited_token, positive_token = required_tokens[rid]
                if prohibited_token not in lowered_prohibited or positive_token not in (lowered_required + " " + clause.get("applicability", "").lower()):
                    fail("DEC003_SEMANTIC_PROHIBITION_WEAKENED", rid)
            if rid in UNIFORM_POPULATION_RULES:
                if "404" not in required or "PRODUCT_NOT_FOUND" not in required:
                    fail("UNIFORM_NOT_FOUND_OUTCOME_MISSING", rid)
                if re.search(r"may identify|may distinguish|can reveal|may reveal", lowered_prohibited):
                    fail("UNIFORM_NOT_FOUND_DISCLOSURE_ALLOWED", rid)
                first_state = clause["controlled_fixtures"][0]["controlled_state"]
                if first_state in {c["controlled_fixtures"][0]["controlled_state"] for c in clauses if c is not clause and c.get("decision_id") == DECISION_3_ID and c.get("authoritative_rule_id") in UNIFORM_POPULATION_RULES}:
                    fail("UNIFORM_CAUSE_FIXTURE_NOT_UNIQUE", rid)
            if rid == "WRONG_STOREFRONT" and not re.search(r"must not identify|distinguish", lowered_prohibited):
                fail("WRONG_STOREFRONT_DISCLOSURE", rid)
            if rid == "MALFORMED_SLUG" and not re.search(r"must not identify|distinguish", lowered_prohibited):
                fail("MALFORMED_SLUG_DIAGNOSTIC_LEAK", rid)
        boundaries = clause.get("boundary_cases")
        if not isinstance(boundaries, list) or not boundaries:
            fail("BOUNDARY_MISSING", rid)
        boundary = boundaries[0]
        if not boundary.get("left_state") or not boundary.get("right_state") or boundary["left_state"] == boundary["right_state"] or not boundary.get("required_public_relation"):
            fail("BOUNDARY_NOT_DISTINCT", rid)
        if is_uniform and not re.search(r"identical|same|uniform|does not change|unchanged|equal", boundary["required_public_relation"], re.I):
            fail("UNIFORM_PUBLIC_RELATION_MISSING", rid)
        evidence = clause.get("observable_evidence_contract", {})
        for field in ("channel", "probe", "observed_state", "comparison", "observed_authority", "expected_authority"):
            if not evidence.get(field):
                fail("CONCRETE_EVIDENCE_MISSING", f"{rid}:{field}")
        evidence_text = " ".join(str(evidence.get(x, "")) for x in ("probe", "observed_state", "comparison"))
        if re.search(r"observe\s+subject\s+and\s+demonstrate", evidence_text, re.I) or evidence_text.strip() in {rid, f"demonstrate {rid}"}:
            fail("RULE_ID_ONLY_EVIDENCE", rid)
        if evidence["observed_authority"] == evidence["expected_authority"] or evidence["observed_state"] == required:
            fail("EXPECTED_DERIVED_EVIDENCE", rid)
        if evidence.get("runtime_status") != "PLANNED_NOT_EXECUTED":
            fail("FALSE_RUNTIME_CLAIM", rid)
        if not re.search(r"HTTP|BROWSER|QUER|PROBE|EVENT|SCHEMA|SINK|INVENTORY|OBSERVATION|MATRIX|COMPARISON|CHECK|SCAN|FIELD|MAP", evidence["channel"]):
            fail("NONOBSERVABLE_EVIDENCE_CHANNEL", rid)
        if not clause.get("failure_semantics") or not clause.get("non_inferences") or not clause.get("technical_choices_deferred"):
            fail("CLAUSE_SEMANTIC_FIELD_MISSING", rid)
        for choice in clause["technical_choices_deferred"]:
            if choice.get("owner_gate") != "PHASE_2D_VS001_IMPLEMENTATION_CONTRACT" or choice.get("business_blocker") is not False:
                fail("TECHNICAL_DEFERRAL_INVALID", rid)


def expected_metadata_projection(payload: dict) -> dict:
    return {key: payload[key] for key in (
        "candidate_id", "supersedes", "supersession_reason", "correction_pass", "status", "approval",
        "approval_ready", "next_gate", "runtime_evidence_status", "implementation_authorized",
        "governing_commit", "governing_decisions", "population", "decision_clause_authoring",
    )}


def parse_markdown(data: bytes) -> list[tuple[str, str, object]]:
    text = data.decode("utf-8")
    if not text.endswith("\n") or text.endswith("\n\n") or any(line.rstrip() != line for line in text.splitlines()):
        fail("MARKDOWN_FORMAT_INVALID", "EOF newline or trailing whitespace")
    pattern = re.compile(r"<!-- C2R2:([A-Z_]+):([^\n]+) -->\n```json\n(.*?)\n```", re.S)
    projections = []
    for match in pattern.finditer(text):
        kind, identity, raw = match.groups()
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            fail("MARKDOWN_PROJECTION_JSON_INVALID", f"{kind}:{identity}:{exc}")
        projections.append((kind, identity, value))
    if len(projections) != 152:
        fail("MARKDOWN_PROJECTION_COUNT_MISMATCH", str(len(projections)))
    return projections


def validate_markdown(payload: dict, data: bytes) -> dict:
    actual = parse_markdown(data)
    expected: list[tuple[str, str, object]] = [
        ("METADATA", payload["candidate_id"], expected_metadata_projection(payload)),
        ("RENDERING_CONTRACT", payload["independent_rendering_contract"]["contract_id"], payload["independent_rendering_contract"]),
    ]
    expected.extend(("RETAINED", record["requirement_id"], record) for record in payload["retained_contracts"])
    for batch in ("batch_1_contracts", "batch_2_contracts", "batch_3_contracts"):
        expected.extend(("SOURCE_CONTRACT", contract["requirement_id"], contract) for contract in payload[batch])
    expected.extend(("DECISION_CLAUSE", clause["clause_id"], clause) for clause in payload["decision_derived_acceptance_clauses"])
    expected.append(("NON_CLAIMS", "C2-R2", payload["non_claims"]))
    if [(kind, identity) for kind, identity, _ in actual] != [(kind, identity) for kind, identity, _ in expected]:
        fail("MARKDOWN_PROJECTION_ORDER_OR_INVENTORY_MISMATCH", "markers differ from canonical order")
    for observed, required in zip(actual, expected):
        if observed != required:
            fail("MARKDOWN_SEMANTIC_PROJECTION_MISMATCH", f"{required[0]}:{required[1]}")
    required_lines = {
        "- Status: `CANDIDATE`", "- Approval: `PENDING_HUMAN_APPROVAL`", "- Approval ready: `true`",
        "- Runtime evidence: `NOT_EXECUTED`", "- Implementation authorized: `false`",
        "- Population: `25 total / 9 retained / 16 elaborated / 21 source obligations / 3 decisions`",
        "- Decision clauses: `27 DEC-001 / 54 DEC-002 / 43 DEC-003 / 124 total / 0 pending`",
    }
    if not required_lines <= set(data.decode().splitlines()):
        fail("MARKDOWN_METADATA_FACT_MISMATCH", "candidate/accounting line missing")
    return {"projections": 152, "retained": 9, "source_contracts": 16, "decision_clauses": 124}


def aggregate(files: dict[str, bytes], paths: list[str]) -> str:
    records = [{"path": path, "sha256": sha(files[path])} for path in sorted(paths)]
    return canonical_sha(records)


def validate_manifest(manifest: dict, files: dict[str, bytes]) -> dict:
    expected_state = {
        "candidate_id": "V23-P2D-VS001-ACCEPTANCE-ELABORATION-C2-R2", "status": "CANDIDATE",
        "correction_pass": 2, "completed_decision_batches": ["DEC-001", "DEC-002", "DEC-003"],
        "decision_clauses_complete": 124, "decision_clauses_pending": 0,
        "approval": "PENDING_HUMAN_APPROVAL", "approval_ready": True,
        "next_gate": "HUMAN_PHASE_2D_VS001_ACCEPTANCE_ELABORATION_C2_R2_CANDIDATE_REVIEW",
        "runtime_evidence_status": "NOT_EXECUTED", "implementation_authorized": False,
        "staged_candidate_identity": None, "final_staged_tree": None, "final_git_content_aggregate": None,
        "gate_results_policy": "CLAIMS_ONLY; VALIDATOR_AND_TESTS_DERIVE_RESULTS_INDEPENDENTLY",
    }
    for key, expected in expected_state.items():
        if manifest.get(key) != expected:
            fail("MANIFEST_STATE_MISMATCH", key)
    if manifest.get("declared_mutation_inventory") != {
        "source_derived": 48, "retained_identity": 9, "structural": 6, "decision_derived": 124, "total": 187,
    }:
        fail("MANIFEST_MUTATION_INVENTORY_MISMATCH", "declared inventory")
    if manifest.get("actual_modified_builder_probes_required") != 10:
        fail("MANIFEST_BUILDER_PROBE_INVENTORY_MISMATCH", "10 required")
    declared = manifest.get("working_file_sha256", {})
    expected_hash_paths = set(EXPECTED_FILES) - {EXPECTED_FILES[2]}
    if set(declared) != expected_hash_paths:
        fail("MANIFEST_FILE_HASH_INVENTORY_MISMATCH", repr(set(declared)))
    for path in expected_hash_paths:
        if sha(files[path]) != declared[path]:
            fail("MANIFEST_FILE_HASH_MISMATCH", path)
    generated = aggregate(files, [EXPECTED_FILES[1], EXPECTED_FILES[0]])
    if manifest.get("working_generated_aggregate_sha256") != generated:
        fail("MANIFEST_AGGREGATE_MISMATCH", "generated payload")
    if manifest.get("self_reference_policy") != "NO_FIXED_POINT; FINAL_TREE_AND_GIT_AGGREGATE_ARE_DETACHED_HUMAN_GATE_OUTPUTS":
        fail("MANIFEST_SELF_REFERENCE_POLICY_MISMATCH", "policy")
    return {"stored_pass_trust": 0, "circular_aggregate": 0, "generated_payload_aggregate": generated}


def lifecycle_files() -> tuple[str, dict[str, bytes], str | None, str]:
    head = run("git", "rev-parse", "HEAD").decode().strip()
    status = [line for line in run("git", "status", "--porcelain=v1").decode().splitlines() if line]
    staged = set(run("git", "diff", "--cached", "--name-only").decode().splitlines())
    expected = set(EXPECTED_FILES)
    if head == GOVERNING and staged == expected:
        if set(status) != {f"A  {path}" for path in expected}:
            fail("STAGED_CANDIDATE_DIRTY_STATE", repr(status))
        files = {path: run("git", "show", f":{path}") for path in expected}
        tree = run("git", "write-tree").decode().strip()
        return "STAGED_OVER_GOVERNING_HEAD", files, tree, GOVERNING
    if head == GOVERNING and not staged:
        if set(status) != {f"?? {path}" for path in expected}:
            fail("WORKING_CANDIDATE_INVENTORY_MISMATCH", repr(status))
        return "WORKING_UNTRACKED_OVER_GOVERNING_HEAD", {path: (ROOT / path).read_bytes() for path in expected}, None, GOVERNING
    try:
        parent = run("git", "rev-parse", "HEAD^").decode().strip()
    except subprocess.CalledProcessError:
        parent = ""
    if parent == GOVERNING:
        if status:
            fail("COMMITTED_CANDIDATE_NOT_CLEAN", repr(status))
        delta = set(run("git", "diff", "--name-only", "HEAD^", "HEAD").decode().splitlines())
        if delta != expected:
            fail("COMMITTED_CANDIDATE_INVENTORY_MISMATCH", repr(delta))
        files = {path: git_bytes("HEAD", path) for path in expected}
        tree = run("git", "rev-parse", "HEAD^{tree}").decode().strip()
        return "COMMITTED_CANDIDATE_WITH_CLEAN_INDEX", files, tree, GOVERNING
    fail("CANDIDATE_LIFECYCLE_CONTEXT_INVALID", head)


def validate_payload(payload: dict, authorities: dict, check_preservation: bool = True, check_similarity: bool = True) -> dict:
    validate_metadata(payload)
    retained = validate_retained(payload, authorities)
    sources = validate_sources_and_contracts(payload, authorities, check_preservation)
    validate_clauses(payload, authorities, check_similarity=check_similarity)
    design = payload.get("builder_conformance_design", {})
    if (
        design.get("validator_imports_or_calls_builder") is not False
        or design.get("actual_modified_builder_executions_required") != 10
        or design.get("coherent_builder_markdown_manifest_update_may_authorize_defective_output") is not False
    ):
        fail("BUILDER_CONFORMANCE_DESIGN_MISMATCH", repr(design))
    if payload.get("validation_policy", {}).get("mutation_inventory", {}).get("total") != 187:
        fail("FINAL_MUTATION_POLICY_MISMATCH", "187")
    return {**retained, **sources}


def validate_all() -> dict:
    mode, files, tree, parent = lifecycle_files()
    payload = json.loads(files[EXPECTED_FILES[1]])
    manifest = json.loads(files[EXPECTED_FILES[2]])
    authorities = load_authorities()
    derived = validate_payload(payload, authorities)
    markdown = validate_markdown(payload, files[EXPECTED_FILES[0]])
    manifest_result = validate_manifest(manifest, files)
    git_aggregate = aggregate(files, EXPECTED_FILES)
    return {
        "result": "VALID_V23_P2D_VS001_ACCEPTANCE_ELABORATION_C2_R2",
        "lifecycle_mode": mode, "parent": parent, "tree": tree,
        "git_content_aggregate": git_aggregate,
        "source_fingerprints": derived["sources"] + derived["current_fingerprints"],
        "retained_git_objects": derived["retained"],
        "source_obligations": derived["obligations"], "source_criteria": derived["criteria"],
        "decision_rules": 124, "candidate_derived_authorities": 0,
        "builder_imported_or_called": 0, "stored_pass_trust": 0,
        **markdown, **manifest_result,
    }


def main() -> None:
    result = validate_all()
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    print("VALID_V23_P2D_VS001_ACCEPTANCE_ELABORATION_C2_R2")


if __name__ == "__main__":
    try:
        main()
    except ValidationError as exc:
        print(f"{exc.code}: {exc.detail}")
        raise SystemExit(1)
