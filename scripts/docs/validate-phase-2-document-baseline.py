#!/usr/bin/env python3
"""Validate the Phase 2C remediated BRD/UXF document-baseline candidate."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
BASE = "0df2d424e00f9cd27b8dcb6645eef827ce97b60e"
CANDIDATE_ID = "V23-P2C-DOCUMENT-BASELINE-C2"
SUPERSEDES = "V23-P2C-DOCUMENT-BASELINE-C1"
SUPERSESSION_REASON = "GENERIC_ACCEPTANCE_SEMANTIC_MISMATCH"
PHASE2 = ROOT / "docs/baselines/v2.3/phase-2"
PROJECTIONS = PHASE2 / "remediated-registry"
REMEDIATOR = ROOT / "scripts/docs/remediate-phase-2-documents.py"
REGISTER = PHASE2 / "PHASE_2_CRITICALITY_EXCEPTION_REGISTER.md"
CANDIDATE = PHASE2 / "phase-2c-document-baseline-candidate.json"

BEGIN = "<!-- YSIM:REQUIREMENT BEGIN -->"
END = "<!-- YSIM:REQUIREMENT END -->"
REQUIRED_FRONT_MATTER = {
    "document_code",
    "title",
    "product_baseline",
    "document_revision",
    "lifecycle_status",
    "language",
    "source_baseline",
    "generated_registry_role",
    "last_remediated_on",
}
REQUIRED_DECISIONS = {f"P2-DEC-{number:03d}" for number in range(1, 11)} | {"SD-02", "SD-03", "BDD-26", "BDD-27"}
ALLOWED_PATHS = (
    "docs/BRD/",
    "docs/UXF/",
    "docs/baselines/v2.3/phase-2/PHASE_2C_REMEDIATION_REPORT.md",
    "docs/baselines/v2.3/phase-2/PHASE_2C_BLOCKER_REGISTER.md",
    "docs/baselines/v2.3/phase-2/phase-2c-document-baseline-candidate.json",
    "docs/baselines/v2.3/phase-2/remediated-registry/",
    "scripts/docs/remediate-phase-2-documents.py",
    "scripts/docs/validate-phase-2-document-baseline.py",
)
GENERIC_PHRASES = (
    "pass khi bằng chứng nghiệp vụ quan sát được xác nhận đúng nghĩa vụ",
    "pass when observable business evidence confirms the obligation",
    "fail khi kết quả thực tế trái với nghĩa vụ này",
    "fail when observed behavior contradicts it",
    "trường hợp biên làm nghĩa vụ không thể đáp ứng",
    "an edge condition that prevents the obligation",
    "chuyển trạng thái không hợp lệ, bản tin lặp hoặc yêu cầu ngoài thứ tự",
    "sai lệch số tiền, tiền tệ hoặc trạng thái tài chính phải bị chặn",
    "retry/replay dùng cùng khóa idempotency",
    "the operation is denied without state change when identity, permission, or assurance is invalid",
)
CRITICAL_DIMENSIONS = (
    "POSITIVE", "NEGATIVE_FAIL_CLOSED", "RECOVERY", "CONCURRENCY",
    "IDEMPOTENCY", "AUTHORIZATION_BOUNDARY",
)
STOPWORDS = {
    "the", "and", "or", "a", "an", "is", "are", "to", "of", "for", "from", "with", "when", "that",
    "must", "shall", "every", "each", "be", "in", "on", "its", "as", "by", "only", "not",
    "và", "hoặc", "là", "của", "cho", "từ", "với", "khi", "phải", "mọi", "mỗi", "được", "trong",
    "không", "có", "các", "một", "theo", "này", "đó", "tại", "thuộc",
}


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=check)


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def index_blob(path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f":{path}"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(result.returncode == 0, f"missing Git-index blob: {path}")
    return result.stdout


def aggregate_hash(items: dict[str, bytes]) -> str:
    digest = hashlib.sha256()
    for path in sorted(items):
        digest.update(path.encode("utf-8"))
        digest.update(b"\0")
        digest.update(items[path])
        digest.update(b"\0")
    return digest.hexdigest()


def source_documents() -> list[Path]:
    return sorted((ROOT / "docs/BRD").glob("*.md")) + sorted((ROOT / "docs/UXF").glob("*.md"))


def parse_front_matter(text: str, path: Path) -> dict[str, Any]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    require(match is not None, f"missing YAML front matter: {path}")
    result: dict[str, Any] = {}
    for line in match.group(1).splitlines():
        key, separator, raw = line.partition(":")
        require(bool(separator), f"malformed front matter line in {path}: {line}")
        result[key.strip()] = json.loads(raw.strip())
    return result


def parse_records() -> list[dict[str, Any]]:
    docs = source_documents()
    require(len(docs) == 31, f"expected 31 source documents, found {len(docs)}")
    require(sum("/BRD/" in str(path) for path in docs) == 24, "expected 24 BRD documents")
    require(sum("/UXF/" in str(path) for path in docs) == 7, "expected 7 UXF documents")
    block_re = re.compile(re.escape(BEGIN) + r".*?```json\n(.*?)\n```.*?" + re.escape(END), re.DOTALL)
    records: list[dict[str, Any]] = []
    for path in docs:
        text = path.read_text(encoding="utf-8")
        front = parse_front_matter(text, path)
        require(REQUIRED_FRONT_MATTER <= set(front), f"incomplete front matter: {path}")
        require(front["product_baseline"] == "2.3", f"wrong baseline: {path}")
        require(front["lifecycle_status"] == "V2.3_DRAFT", f"wrong lifecycle: {path}")
        require(front["last_remediated_on"] == "2026-07-15", f"wrong remediation date: {path}")
        expected_language = "vi-VN" if "/BRD/" in str(path) else "en"
        require(front["language"] == expected_language, f"wrong canonical language: {path}")
        relative = str(path.relative_to(ROOT))
        for match in block_re.finditer(text):
            record = json.loads(match.group(1))
            require(record["provenance"]["source_document"] == relative, f"source mismatch: {record['stable_id']}")
            records.append(record)
    return records


def validate_git_boundary() -> None:
    require(run("git", "cat-file", "-e", f"{BASE}^{{commit}}", check=False).returncode == 0, "base commit does not exist")
    require(run("git", "merge-base", "--is-ancestor", BASE, "HEAD", check=False).returncode == 0, "validation HEAD is not based on approved Phase 2B commit")
    changed = run("git", "diff", "--name-only", BASE).stdout.splitlines()
    staged = run("git", "diff", "--cached", "--name-only", BASE).stdout.splitlines()
    untracked = run("git", "ls-files", "--others", "--exclude-standard").stdout.splitlines()
    candidates = sorted(set(changed + staged + untracked))
    unauthorized = [path for path in candidates if not any(path == prefix or path.startswith(prefix) for prefix in ALLOWED_PATHS)]
    require(not unauthorized, f"unauthorized paths changed since approved base: {unauthorized}")
    protected = [
        "docs/baselines/v2.3/requirements",
        "docs/baselines/v2.3/phase-2/PHASE_2_CRITICALITY_EXCEPTION_REGISTER.md",
        "docs/baselines/v2.3/phase-2/PHASE_2_CRITICALITY_EXCEPTION_REVIEW_PACK.md",
        "docs/baselines/v2.3/phase-2/phase-2-criticality-exception-review.json",
        "docs/baselines/v2.3/phase-2/PHASE_2_HUMAN_DECISION_PACK.md",
        "docs/baselines/v2.3/phase-2/phase-2-human-decisions.json",
        "docs/baselines/v2.3/phase-2/stable-id-mapping-candidate.json",
    ]
    for path in protected:
        require(run("git", "diff", "--quiet", BASE, "--", path, check=False).returncode == 0, f"signed/protected artifact changed: {path}")


def semantic_tokens(text: str) -> set[str]:
    return {
        token for token in re.findall(r"[A-Za-zÀ-ỹ0-9_]+", text.casefold())
        if len(token) >= 3 and token not in STOPWORDS
    }


def criterion_text(item: dict[str, Any]) -> str:
    return " ".join(str(item[field]) for field in ("given", "when", "then", "observable_evidence"))


def validate_acceptance_record(record: dict[str, Any]) -> None:
    sid = record["stable_id"]
    require(record.get("acceptance_schema_version") == "2.0.0-OBLIGATION_COVERAGE", f"wrong acceptance schema: {sid}")
    obligations = record.get("atomic_obligations")
    criteria = record.get("acceptance_contract")
    require(isinstance(obligations, list) and obligations, f"missing atomic obligations: {sid}")
    require(isinstance(criteria, list) and criteria, f"missing acceptance criteria: {sid}")
    obligation_ids = [item.get("obligation_id") for item in obligations]
    criterion_ids = [item.get("criterion_id") for item in criteria]
    require(all(obligation_ids) and len(obligation_ids) == len(set(obligation_ids)), f"invalid obligation IDs: {sid}")
    require(all(criterion_ids) and len(criterion_ids) == len(set(criterion_ids)), f"invalid criterion IDs: {sid}")
    obligation_by_id = {item["obligation_id"]: item for item in obligations}
    criterion_by_id = {item["criterion_id"]: item for item in criteria}
    required_criterion_fields = {"criterion_id", "case", "verifies", "given", "when", "then", "observable_evidence", "controlled_contract"}

    for obligation in obligations:
        require(set(obligation) >= {"obligation_id", "obligation_text", "applicability", "acceptance_criterion_references"}, f"incomplete obligation: {obligation['obligation_id']}")
        require(obligation["applicability"] == "V2.3_ACTIVE", f"wrong obligation applicability: {obligation['obligation_id']}")
        refs = obligation["acceptance_criterion_references"]
        require(refs and set(refs) <= set(criterion_ids), f"uncovered obligation: {obligation['obligation_id']}")
        require(all(obligation["obligation_id"] in criterion_by_id[ref]["verifies"] for ref in refs), f"obligation back-reference mismatch: {obligation['obligation_id']}")

    record_semantics = " ".join([record["title"], record["normative_statement"]] + [item["obligation_text"] for item in obligations])
    record_tokens = semantic_tokens(record_semantics)
    for item in criteria:
        require(set(item) >= required_criterion_fields, f"incomplete acceptance criterion: {sid}")
        require(item["verifies"] and set(item["verifies"]) <= set(obligation_ids), f"criterion verifies unknown obligation: {item['criterion_id']}")
        require(all(isinstance(item[field], str) and len(item[field].strip()) >= 8 for field in ("given", "when", "then", "observable_evidence")), f"non-concrete criterion field: {item['criterion_id']}")
        text = criterion_text(item)
        lower = text.casefold()
        require(not any(phrase in lower for phrase in GENERIC_PHRASES), f"generic acceptance template: {item['criterion_id']}")
        require(not re.search(r"\b(?:TODO|TBD|PLACEHOLDER|INFERRED_ONLY)\b", text, re.IGNORECASE), f"placeholder acceptance: {item['criterion_id']}")
        require("requirement passes" not in lower and "nghĩa vụ được đáp ứng" not in lower, f"tautological acceptance: {item['criterion_id']}")
        for oid in item["verifies"]:
            obligation_norm = re.sub(r"\W+", " ", obligation_by_id[oid]["obligation_text"].casefold()).strip()
            then_norm = re.sub(r"\W+", " ", item["then"].casefold()).strip()
            require(len(obligation_norm) < 24 or obligation_norm not in then_norm, f"criterion merely restates obligation: {item['criterion_id']}")
        verified_tokens = set().union(*(semantic_tokens(obligation_by_id[oid]["obligation_text"]) for oid in item["verifies"]))
        require(bool((semantic_tokens(text) & (verified_tokens | record_tokens)) - {"result", "state", "evidence", "outcome"}), f"criterion unrelated to obligation: {item['criterion_id']}")
        require(len(semantic_tokens(item["observable_evidence"])) >= 3, f"non-observable evidence: {item['criterion_id']}")
        for leaked in ("database", "framework", "message queue"):
            require(leaked not in lower or leaked in record_semantics.casefold(), f"solution-design leakage in {item['criterion_id']}: {leaked}")
        if any(term in lower for term in ("amount mismatch", "currency mismatch", "sai lệch số tiền", "sai lệch tiền tệ")):
            require(any(term in record_semantics.casefold() for term in ("amount", "currency", "số tiền", "tiền tệ")), f"unrelated financial criterion: {item['criterion_id']}")
        if any(term in lower for term in ("idempot", "retry", "replay", "duplicate side effect")):
            require(any(term in record_semantics.casefold() for term in ("idempot", "retry", "replay", "dedup", "duplicate", "thử lại", "lặp")), f"unconditional retry/idempotency criterion: {item['criterion_id']}")
        if item["case"] == "AUTHORIZATION_BOUNDARY" or item["controlled_contract"].startswith("SECURITY_"):
            require(any(term in record_semantics.casefold() for term in ("permission", "authoriz", "access", "role", "mfa", "credential", "quyền", "được xem", "chỉ được", "xác thực", "bảo mật")) or record["requirement_type"] in {"SECURITY_REQUIREMENT", "PRIVACY_REQUIREMENT"}, f"unrelated security criterion: {item['criterion_id']}")

    tier = record["verification_criticality"]
    cases = {item["case"] for item in criteria}
    require("POSITIVE" in cases, f"missing statement-specific positive criterion: {sid}")
    if tier == "HIGH":
        require("PRINCIPAL_FAILURE_OR_EDGE" in cases, f"HIGH missing principal failure/boundary criterion: {sid}")
    if tier == "CRITICAL":
        matrix = record.get("criticality_applicability")
        require(isinstance(matrix, dict) and set(matrix) == set(CRITICAL_DIMENSIONS), f"invalid CRITICAL applicability matrix: {sid}")
        for dimension in CRITICAL_DIMENSIONS:
            entry = matrix[dimension]
            require(entry.get("status") in {"APPLICABLE", "NOT_APPLICABLE"}, f"invalid applicability status: {sid}/{dimension}")
            refs = entry.get("criterion_references", [])
            require(set(refs) <= set(criterion_ids), f"unknown matrix criterion: {sid}/{dimension}")
            if entry["status"] == "APPLICABLE":
                require(refs, f"applicable dimension lacks criteria: {sid}/{dimension}")
                expected_cases = {dimension} if dimension != "POSITIVE" else {"POSITIVE"}
                require(all(criterion_by_id[ref]["case"] in expected_cases for ref in refs), f"matrix/case mismatch: {sid}/{dimension}")
            else:
                require(not refs and sid in entry.get("rationale", "") and dimension.casefold().replace("_", " ") in entry.get("rationale", "").casefold(), f"non-specific N/A rationale: {sid}/{dimension}")
    else:
        require(record.get("criticality_applicability") is None, f"non-CRITICAL record has critical matrix: {sid}")


def validate_duplicate_templates(records: list[dict[str, Any]]) -> None:
    groups: dict[tuple[str, str, str, str], list[dict[str, Any]]] = {}
    for record in records:
        for item in record.get("acceptance_contract", []):
            key = tuple(item[field] for field in ("given", "when", "then", "observable_evidence"))
            groups.setdefault(key, []).append(item)
    for group in groups.values():
        if len(group) < 2:
            continue
        contracts = {item.get("controlled_contract") for item in group}
        require(len(contracts) == 1 and None not in contracts and "" not in contracts, f"uncontrolled copied acceptance template: {[item['criterion_id'] for item in group]}")


def validate_records(records: list[dict[str, Any]]) -> None:
    require(len(records) == 1198, f"expected 1198 records, found {len(records)}")
    ids = [record.get("stable_id") for record in records]
    require(all(ids), "missing stable ID")
    require(len(ids) == len(set(ids)), "duplicate or reused stable ID")
    require(all("temporary_key" not in record for record in records), "active temporary-key field remains")
    by_id = {record["stable_id"]: record for record in records}
    require(len([r for r in records if r["record_kind"] == "CANONICAL_ATOMIC"]) == 1184, "canonical atomic count mismatch")
    require(len([r for r in records if r["record_kind"] == "COMPOSITE_PARENT"]) == 4, "composite count mismatch")
    require(len([r for r in records if r["record_kind"] == "ALIAS"]) == 10, "alias count mismatch")

    relationship_targets: set[str] = set()
    for record in records:
        relationships = record["relationships"]
        if relationships.get("alias_of"):
            relationship_targets.add(relationships["alias_of"])
        for key in ("aliases", "derived_from", "derived_requirements", "satisfies_composite_parents"):
            relationship_targets.update(relationships.get(key, []))
        require(re.fullmatch(r"[0-9a-f]{64}", record["provenance"].get("source_context_sha256", "")) is not None, f"missing full-source-section context hash: {record['stable_id']}")
        require(bool(record["provenance"].get("source_context_heading")), f"missing full-source-section heading: {record['stable_id']}")
        active_atomic = record["scope_status"] == "V2.3_ACTIVE" and record["record_kind"] == "CANONICAL_ATOMIC"
        if active_atomic:
            require(record["acceptance_status"] == "DIRECT", f"active acceptance gap: {record['stable_id']}")
            require(record["acceptance_unit"] and record["criticality_unit"], f"active atomic flags missing: {record['stable_id']}")
            tier = record["verification_criticality"]
            require(tier in {"CRITICAL", "HIGH", "NORMAL"}, f"invalid criticality: {record['stable_id']}")
            validate_acceptance_record(record)
        else:
            require(record["acceptance_status"] == "NOT_APPLICABLE_FOR_V2.3", f"non-atomic/inactive acceptance status: {record['stable_id']}")
            require(not any(record[key] for key in ("implementation_unit", "acceptance_unit", "scope_coverage_unit", "criticality_unit")), f"forbidden unit flag: {record['stable_id']}")
            require(record["verification_criticality"] == "NOT_APPLICABLE", f"false inactive/non-atomic tier: {record['stable_id']}")
            require(record.get("atomic_obligations") == [] and record.get("acceptance_contract") == [] and record.get("criticality_applicability") is None, f"non-unit record carries runtime acceptance: {record['stable_id']}")
        payload = json.dumps(record, ensure_ascii=False)
        require(not re.search(r"\b(?:TODO|TBD|PLACEHOLDER|INFERRED_ONLY)\b", payload, re.IGNORECASE), f"placeholder/inferred content: {record['stable_id']}")
    require(not (relationship_targets - set(ids)), f"dangling references: {sorted(relationship_targets - set(ids))}")

    active_atomic = [r for r in records if r["scope_status"] == "V2.3_ACTIVE" and r["record_kind"] == "CANONICAL_ATOMIC"]
    require(len(active_atomic) == 1076, "active atomic denominator mismatch")
    require(Counter(r["scope_status"] for r in records if r["record_kind"] == "CANONICAL_ATOMIC") == Counter({"V2.3_ACTIVE": 1076, "FUTURE": 74, "DEFERRED": 16, "OUT_OF_SCOPE": 18}), "scope distribution mismatch")
    require(Counter(r["verification_criticality"] for r in active_atomic) == Counter({"CRITICAL": 316, "HIGH": 394, "NORMAL": 366}), "criticality distribution mismatch")
    validate_duplicate_templates(active_atomic)

    # Approved structural and semantic contracts.
    require(by_id["BD-04-007"]["scope_status"] == "OUT_OF_SCOPE", "Product Variant must remain outside v2.3")
    require("Shared Approval Engine" in by_id["BRD-CAP-INDEX-R007"]["normative_statement"], "Shared Approval Engine remediation missing")
    require(by_id["BRD-WS-08-R012"]["scope_status"] == "DEFERRED" and by_id["BRD-WS-08-R013"]["scope_status"] == "V2.3_ACTIVE", "Fraud/Risk split missing")
    require(all(word in by_id["BRD-EVENT-INDEX-R001"]["normative_statement"] for word in ("Payment", "Settlement", "Financial")), "R001 event subjects missing")
    require(all(word in by_id["BRD-EVENT-INDEX-R002"]["normative_statement"] for word in ("Marketing", "Analytics", "Notification")), "R002 event subjects missing")
    business = by_id["BRD-UPDATE-01-R010"]
    require(business["record_kind"] == "COMPOSITE_PARENT" and business["relationships"]["coverage_mode"] == "ALL_CHILDREN", "Business Principles parent invalid")
    require(len(business["relationships"]["derived_requirements"]) == 12, "Business Principles must have 12 reconciled children")
    require("Business Model là điểm khởi đầu" in by_id["BRD-UPDATE-01-R030"]["normative_statement"], "Business Model First explanation missing")
    require(by_id["BRD-UPDATE-01-R033"].get("non_inference_guard") == "MUST_NOT_BE_INTERPRETED_AS_AN_ACTIVE_AI_PRODUCT_FEATURE_WITHOUT_AN_APPROVED_REQUIREMENT", "AI Ready non-inference guard missing")
    operations = by_id["BRD-WS-17-R013"]
    require(operations["record_kind"] == "COMPOSITE_PARENT" and operations["relationships"]["coverage_mode"] == "ALL_CHILDREN", "Operations parent invalid")
    require(len(operations["relationships"]["derived_requirements"]) == 6, "Operations parent must have six children")
    require(by_id["EP-17-010"]["relationships"]["alias_of"] == "BRD-WS-17-R013", "old operations aggregate must be alias")
    require({"BRD-CAP-INDEX-R029", "UXF-05-R054"} <= set(ids), "approved allocations missing")

    # Mandatory C2 semantic repairs.
    cap = by_id["BRD-CAP-INDEX-R029"]
    cap_text = json.dumps({"obligations": cap["atomic_obligations"], "criteria": cap["acceptance_contract"]}, ensure_ascii=False)
    require(all(token in cap_text for token in ("PUBLISHER", "SUBSCRIBER", "BOTH", "NONE", "alias", "retired", "tombstone", "dangling")), "Capability event-role acceptance is incomplete")
    disclosure = by_id["UXF-05-R054"]
    disclosure_text = json.dumps({"obligations": disclosure["atomic_obligations"], "criteria": disclosure["acceptance_contract"]}, ensure_ascii=False).casefold()
    require(all(token in disclosure_text for token in ("read-only", "api payload", "allocation", "missing", "fail")), "disclosure acceptance is incomplete")
    model_first = by_id["BRD-UPDATE-01-R030"]
    require(all(token in json.dumps(model_first["acceptance_contract"], ensure_ascii=False).casefold() for token in ("business model identifier", "experience identifier", "creation trace", "publication trace")), "Business Model First lacks observable trace evidence")
    fraud = by_id["BRD-WS-08-R013"]
    fraud_text = json.dumps({"obligations": fraud["atomic_obligations"], "criteria": fraud["acceptance_contract"]}, ensure_ascii=False)
    require(all(token in fraud_text for token in ("ALLOW", "CHALLENGE", "BLOCK", "REVIEW", "rule", "signal", "reason", "override", "audit")), "Fraud/Risk decision coverage incomplete")
    require(fraud["criticality_applicability"]["CONCURRENCY"]["status"] == "NOT_APPLICABLE" and fraud["criticality_applicability"]["IDEMPOTENCY"]["status"] == "NOT_APPLICABLE", "Fraud/Risk has fabricated concurrency/idempotency coverage")
    observable = by_id["BRD-WS-17-R026"]
    observable_text = json.dumps({"obligations": observable["atomic_obligations"], "criteria": observable["acceptance_contract"]}, ensure_ascii=False).casefold()
    require(all(token in observable_text for token in ("running", "completed", "failed", "signal", "detectable")) and "duplicate side effect" not in observable_text, "operations observability acceptance mismatch")
    objects = by_id["EP-08-002"]
    objects_text = json.dumps({"obligations": objects["atomic_obligations"], "criteria": objects["acceptance_contract"]}, ensure_ascii=False).casefold()
    require(all(token in objects_text for token in ("distinct stable identity", "owner", "reference", "lifecycle")) and not any(token in objects_text for token in ("amount", "currency", "retry", "idempot")), "PaymentGateway/MerchantAccount independence acceptance mismatch")
    mfa = by_id["BD-16-003"]
    mfa_text = json.dumps({"obligations": mfa["atomic_obligations"], "criteria": mfa["acceptance_contract"]}, ensure_ascii=False)
    require(all(token in mfa_text for token in ("Platform scope", "Organization scope", "Role scope", "User scope", "API Client scope", "effective MFA policy", "bypass", "audited")), "MFA scope acceptance incomplete")
    feedback = by_id["BD-11-010"]
    feedback_text = json.dumps({"obligations": feedback["atomic_obligations"], "criteria": feedback["acceptance_contract"]}, ensure_ascii=False)
    require(all(token in feedback_text for token in ("Product", "Fulfillment", "Ticket", "Customer Portal", "unsupported", "malformed", "rejected")), "Customer Feedback source acceptance incomplete")

    covered_decisions = {decision for record in records for decision in record["provenance"]["approved_decisions"]}
    require(REQUIRED_DECISIONS <= covered_decisions, f"approved decisions missing: {sorted(REQUIRED_DECISIONS - covered_decisions)}")
    contracts = {decision for record in records for decision in record["provenance"].get("approved_decision_contracts", {})}
    require({f"P2-DEC-{number:03d}" for number in range(1, 11)} <= contracts, "not all Phase 2A human decision contracts are embedded")

    dispositions = {item["exception_id"] for record in records for item in record.get("criticality_dispositions", [])}
    require(dispositions == {f"P2-CRIT-EXC-{number:03d}" for number in range(1, 47)}, "not all 46 criticality dispositions applied")


def validate_projections(records: list[dict[str, Any]]) -> None:
    expected_names = {
        "brd-requirements.json", "uxf-requirements.json", "registry-summary.json", "traceability.json",
        "identity-history.json", "acceptance-summary.json", "criticality-summary.json", "remediation-ledger.json",
    }
    require({path.name for path in PROJECTIONS.glob("*.json")} == expected_names, "projection file set mismatch")
    projected = load(PROJECTIONS / "brd-requirements.json")["requirements"] + load(PROJECTIONS / "uxf-requirements.json")["requirements"]
    require(projected == records, "generated JSON does not exactly match Markdown source order/content")
    summary = load(PROJECTIONS / "registry-summary.json")
    require(summary["dangling_reference_count"] == 0 and summary["active_temporary_key_count"] == 0 and summary["missing_stable_id_count"] == 0, "registry summary invariant failed")
    acceptance = load(PROJECTIONS / "acceptance-summary.json")
    require(acceptance["active_acceptance_gap"] == 0 and acceptance["direct_count"] == 1076, "acceptance summary mismatch")
    require(acceptance["acceptance_schema_version"] == "2.0.0-OBLIGATION_COVERAGE", "wrong projected acceptance schema")
    require(acceptance["obligation_count"] > 1076 and acceptance["criterion_count"] >= acceptance["obligation_count"], "obligation/criterion accounting invalid")
    require(acceptance["uncovered_obligation_count"] == 0, "projected uncovered obligations remain")
    require(acceptance["c1_generic_criterion_occurrences"] == 1822 and acceptance["c2_generic_criterion_occurrences"] == 0, "generic-template occurrence accounting invalid")
    require(acceptance["invalid_duplicate_template_group_count"] == 0, "invalid duplicate acceptance templates remain")
    ledger = load(PROJECTIONS / "remediation-ledger.json")
    require(ledger["disposition_count"] == 46 and all(not entry["source_resolution_claim"] and entry["source_exception_status"] == "OPEN" for entry in ledger["entries"]), "remediation ledger source-status violation")
    identity = load(PROJECTIONS / "identity-history.json")
    require((len(identity["preserved"]), len(identity["mapped"]), len(identity["newly_allocated"]), identity["retired_key_count"]) == (576, 609, 13, 157), "identity-history accounting mismatch")
    require(not ({item["stable_id"] for item in identity["newly_allocated"]} & set(identity["retired_key_history"])), "retired identity reused")


def validate_candidate() -> None:
    candidate = load(CANDIDATE)
    require(candidate["candidate_id"] == CANDIDATE_ID, "candidate identity mismatch")
    require(candidate["supersedes"] == SUPERSEDES and candidate["supersession_reason"] == SUPERSESSION_REASON, "C2 supersession metadata mismatch")
    require(candidate["status"] == "CANDIDATE", "candidate state must remain CANDIDATE")
    require(candidate["approval_status"] == "PENDING_HUMAN_ACCEPTANCE", "approval must remain pending")
    require(candidate["base_commit"] == BASE, "candidate base mismatch")
    require(candidate["hash_basis"] == "GIT_INDEX_BLOB_CONTENT" and candidate["line_endings"] == "GIT_CANONICAL_TEXT", "candidate hash contract mismatch")
    require(candidate["next_gate"] == "HUMAN_DOCUMENT_BASELINE_ACCEPTANCE", "wrong next gate")
    require(candidate["blocker_count"] == 0, "candidate has blockers")
    require(all(value is None for key, value in candidate["approval_block"].items() if key != "decision") and candidate["approval_block"]["decision"] == "PENDING", "candidate approval block is not wholly pending")
    manifest = candidate["deterministic_hashes"]["files"]
    blobs = {path: index_blob(path) for path in manifest}
    for path, expected in manifest.items():
        require(hashlib.sha256(blobs[path]).hexdigest() == expected, f"Git-index SHA-256 mismatch: {path}")
    source_blobs = {path: data for path, data in blobs.items() if path.startswith("docs/BRD/") or path.startswith("docs/UXF/")}
    projection_blobs = {path: data for path, data in blobs.items() if path.startswith("docs/baselines/v2.3/phase-2/remediated-registry/")}
    require(aggregate_hash(source_blobs) == candidate["deterministic_hashes"]["source_aggregate_sha256"], "Git-index source aggregate mismatch")
    require(aggregate_hash(projection_blobs) == candidate["deterministic_hashes"]["projection_aggregate_sha256"], "Git-index projection aggregate mismatch")


def validate_source_register() -> None:
    text = REGISTER.read_text(encoding="utf-8")
    rows = re.findall(r"^\| P2-CRIT-EXC-\d{3} .*?\| `OPEN` \|$", text, re.MULTILINE)
    require(len(rows) == 46, f"source exception register must remain 46 OPEN, found {len(rows)}")


def validate_determinism() -> None:
    for pass_number in (1, 2):
        result = run(sys.executable, str(REMEDIATOR), "--check", check=False)
        require(result.returncode == 0, f"deterministic regeneration pass {pass_number} failed:\n{result.stdout}{result.stderr}")
        require(result.stdout.strip() == "PASS — DETERMINISTIC_PHASE_2C_REMEDIATION_OUTPUT", f"unexpected regeneration output on pass {pass_number}")


def main() -> int:
    try:
        validate_git_boundary()
        records = parse_records()
        validate_records(records)
        validate_projections(records)
        validate_candidate()
        validate_source_register()
        validate_determinism()
    except (ValidationError, KeyError, ValueError, json.JSONDecodeError) as error:
        print(f"FAIL — {error}", file=sys.stderr)
        return 1
    print("PASS — VALID_PHASE_2C_DOCUMENT_BASELINE_CANDIDATE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
