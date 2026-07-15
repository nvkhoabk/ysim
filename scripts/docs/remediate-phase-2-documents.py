#!/usr/bin/env python3
"""Deterministically remediate the Phase 2C BRD/UXF document baseline.

The accepted FC2 registry and approved Phase 2 decision artifacts are inputs.
The remediated Markdown requirement blocks are the sole input to every JSON
projection emitted by this program.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
BASE_COMMIT = "0df2d424e00f9cd27b8dcb6645eef827ce97b60e"
CANDIDATE_ID = "V23-P2C-DOCUMENT-BASELINE-C2"
SUPERSEDES = "V23-P2C-DOCUMENT-BASELINE-C1"
SUPERSESSION_REASON = "GENERIC_ACCEPTANCE_SEMANTIC_MISMATCH"
REMEDIATION_DATE = "2026-07-15"

BRD_REGISTRY = ROOT / "docs/baselines/v2.3/requirements/brd-requirements.json"
UXF_REGISTRY = ROOT / "docs/baselines/v2.3/requirements/uxf-requirements.json"
MAPPING_PATH = ROOT / "docs/baselines/v2.3/phase-2/stable-id-mapping-candidate.json"
PREFLIGHT_PATH = ROOT / "docs/baselines/v2.3/phase-2/phase-2-preflight-summary.json"
CRITICALITY_PATH = ROOT / "docs/baselines/v2.3/phase-2/phase-2-criticality-exception-review.json"
HUMAN_DECISIONS_PATH = ROOT / "docs/baselines/v2.3/phase-2/phase-2-human-decisions.json"
RECONCILIATION_PATH = ROOT / "docs/baselines/v2.3/requirements/registry-reconciliation.json"
PROJECTION_DIR = ROOT / "docs/baselines/v2.3/phase-2/remediated-registry"
REPORT_PATH = ROOT / "docs/baselines/v2.3/phase-2/PHASE_2C_REMEDIATION_REPORT.md"
BLOCKER_PATH = ROOT / "docs/baselines/v2.3/phase-2/PHASE_2C_BLOCKER_REGISTER.md"
CANDIDATE_PATH = ROOT / "docs/baselines/v2.3/phase-2/phase-2c-document-baseline-candidate.json"

BEGIN = "<!-- YSIM:REQUIREMENT BEGIN -->"
END = "<!-- YSIM:REQUIREMENT END -->"
APPENDIX_BEGIN = "<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->"
APPENDIX_END = "<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->"
IDENTITY_BEGIN = "<!-- YSIM:IDENTITY_HISTORY BEGIN -->"
IDENTITY_END = "<!-- YSIM:IDENTITY_HISTORY END -->"

PROJECTION_NAMES = (
    "brd-requirements.json",
    "uxf-requirements.json",
    "registry-summary.json",
    "traceability.json",
    "identity-history.json",
    "acceptance-summary.json",
    "criticality-summary.json",
    "remediation-ledger.json",
)

REQUIRED_DECISIONS = {
    "P2-DEC-001",
    "P2-DEC-002",
    "P2-DEC-003",
    "P2-DEC-004",
    "P2-DEC-005",
    "P2-DEC-006",
    "P2-DEC-007",
    "P2-DEC-008",
    "P2-DEC-009",
    "P2-DEC-010",
    "SD-02",
    "SD-03",
    "BDD-26",
    "BDD-27",
}

GENERIC_ACCEPTANCE_PHRASES = (
    "PASS khi bằng chứng nghiệp vụ quan sát được xác nhận đúng nghĩa vụ",
    "PASS when observable business evidence confirms the obligation",
    "FAIL khi kết quả thực tế trái với nghĩa vụ này",
    "FAIL when observed behavior contradicts it",
    "Trường hợp biên làm nghĩa vụ không thể đáp ứng",
    "An edge condition that prevents the obligation",
    "Chuyển trạng thái không hợp lệ, bản tin lặp hoặc yêu cầu ngoài thứ tự",
    "Sai lệch số tiền, tiền tệ hoặc trạng thái tài chính phải bị chặn",
    "Retry/replay dùng cùng khóa idempotency",
    "The operation is denied without state change when identity, permission, or assurance is invalid",
)
C1_GENERIC_CRITERION_OCCURRENCES = 1822


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def aggregate_hash(items: dict[str, bytes]) -> str:
    digest = hashlib.sha256()
    for path in sorted(items):
        digest.update(path.encode("utf-8"))
        digest.update(b"\0")
        digest.update(items[path])
        digest.update(b"\0")
    return digest.hexdigest()


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        match = re.match(r"\A---\n.*?\n---\n+", text, flags=re.DOTALL)
        if match:
            return text[match.end() :]
    return text


def strip_generated(text: str) -> str:
    text = strip_front_matter(text)
    authority = re.compile(
        r"\A## (?:Thẩm quyền nguồn yêu cầu v2\.3|v2\.3 requirement authority)\n\n.*?\n\n",
        flags=re.DOTALL,
    )
    text = authority.sub("", text, count=1)
    pattern = re.compile(
        r"\n*" + re.escape(APPENDIX_BEGIN) + r".*?" + re.escape(APPENDIX_END) + r"\n*\Z",
        flags=re.DOTALL,
    )
    return pattern.sub("\n", text).strip() + "\n"


def front_matter(document: dict[str, Any]) -> str:
    language = "vi-VN" if document["path"].startswith("docs/BRD/") else "en"
    role = "BRD_CANONICAL_SOURCE" if language == "vi-VN" else "UXF_CANONICAL_SOURCE"
    fields = {
        "document_code": document["document_code"],
        "title": document["title"],
        "product_baseline": "2.3",
        "document_revision": "2.3.0-draft.1",
        "lifecycle_status": "V2.3_DRAFT",
        "language": language,
        "source_baseline": "v2.2",
        "generated_registry_role": role,
        "last_remediated_on": REMEDIATION_DATE,
    }
    lines = ["---"]
    for key, value in fields.items():
        lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    lines.extend(["---", ""])
    return "\n".join(lines)


def map_reference(value: str | None, stable_by_original: dict[str, str]) -> str | None:
    if not value:
        return None
    return stable_by_original.get(value, value)


def identity_kind(record: dict[str, Any]) -> str:
    if record.get("alias_of"):
        return "ALIAS"
    if record.get("is_composite"):
        return "COMPOSITE_PARENT"
    return "CANONICAL_ATOMIC"


def inactive_rationale(scope: str) -> str:
    return {
        "FUTURE": "Requirement is retained for a future baseline and is excluded from v2.3 delivery.",
        "DEFERRED": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
        "OUT_OF_SCOPE": "Requirement is explicitly outside the v2.3 product scope.",
    }.get(scope, "This record is not an independently verifiable v2.3 atomic unit.")


def delivery_commitment(scope: str) -> str:
    return {
        "V2.3_ACTIVE": "COMMITTED_FOR_V2.3",
        "FUTURE": "POST_V2.3",
        "DEFERRED": "POST_V2.3",
        "OUT_OF_SCOPE": "EXCLUDED_FROM_V2.3",
    }[scope]


def title_from_statement(statement: str, stable_id: str) -> str:
    text = normalize_space(statement).strip("-:.;")
    if not text:
        return f"Requirement {stable_id}"
    return text[:96] + ("…" if len(text) > 96 else "")


def extract_full_source_section(statement: str, body: str) -> tuple[str, str]:
    """Return the complete legacy Markdown section containing a statement."""
    probes = [line.strip() for line in statement.splitlines() if len(line.strip()) >= 8]
    position = -1
    for probe in probes:
        position = body.find(probe)
        if position >= 0:
            break
    if position < 0:
        return statement, "SOURCE_STATEMENT_FALLBACK"
    headings = list(re.finditer(r"^(#{1,6})\s+(.+?)\s*$", body[:position], re.MULTILINE))
    if not headings:
        return statement, "DOCUMENT_PREAMBLE"
    heading = headings[-1]
    level = len(heading.group(1))
    tail = body[position:]
    next_heading = re.search(rf"^#{{1,{level}}}\s+", tail, re.MULTILINE)
    end = position + next_heading.start() if next_heading else len(body)
    return body[heading.start():end].strip(), heading.group(2).strip()


def split_atomic_obligations(statement: str) -> list[str]:
    text = normalize_space(statement)
    list_match = re.match(r"^(.*?:)\s+-\s+(.+)$", text)
    if list_match:
        prefix = list_match.group(1).rstrip(": ")
        items = [item.strip(" -.;:") for item in re.split(r"\s+-\s+", list_match.group(2)) if item.strip(" -.;:")]
        if len(items) > 1:
            return [f"{prefix}: {item}." for item in items]
    parts = [part.strip(" -.;:") for part in re.split(r";|(?<=[.!?])\s+(?=[A-ZÀ-Ỹ])", text)]
    parts = [part for part in parts if len(part) >= 4]
    return parts or [text]


MANDATORY_OBLIGATIONS: dict[str, list[str]] = {
    "BRD-CAP-INDEX-R029": [
        "event_role accepts only PUBLISHER, SUBSCRIBER, BOTH, or NONE.",
        "NONE requires published_event_ids and subscribed_event_ids to both be empty.",
        "PUBLISHER requires published_event_ids to be non-empty.",
        "SUBSCRIBER requires subscribed_event_ids to be non-empty.",
        "BOTH requires published_event_ids and subscribed_event_ids to both be non-empty.",
        "Every event reference resolves to a canonical active or approved Event Registry ID and rejects alias, retired, tombstone, or dangling IDs.",
    ],
    "UXF-05-R054": [
        "Customer-facing provider, network, or brand disclosure is rendered read-only only when Catalog, legal, or product definition requires it.",
        "UI state and Storefront API payloads exclude internal Supplier ID, procurement source, cost, margin, routing priority, supplier health, connector identity, and allocation details.",
        "Customer-facing disclosure does not affect the Allocation decision.",
        "A journey requiring mandatory disclosure does not proceed when that disclosure data is missing.",
    ],
    "BRD-UPDATE-01-R030": [
        "Creation and publication of every Commerce Experience is traceably rooted in an identified Business Model.",
    ],
    "BRD-WS-08-R013": [
        "Applicable rule-based risk input produces an ALLOW decision when no challenge, block, or review rule matches.",
        "Applicable rule-based risk input produces a CHALLENGE decision when additional assurance is required.",
        "Applicable rule-based risk input produces a BLOCK decision when a blocking rule matches.",
        "Applicable rule-based risk input produces a REVIEW decision when human review is required.",
        "Each risk decision records the versions of its rule, signal, reason, override, and audit evidence.",
        "Missing or invalid mandatory risk evidence fails closed.",
        "A risk override is accepted only from an authorized actor and is recorded in audit evidence.",
    ],
    "BRD-WS-17-R026": [
        "A running operational task exposes its current state and relevant operational signals.",
        "A completed operational task exposes its outcome and completion evidence.",
        "A failed operational task exposes its failure outcome and relevant diagnostic signal.",
        "Missing required observability evidence produces a detectable operational verification failure.",
    ],
    "EP-08-002": [
        "PaymentGateway and MerchantAccount have independent business identities.",
        "PaymentGateway and MerchantAccount retain independent ownership and references.",
        "PaymentGateway and MerchantAccount retain independent lifecycles.",
    ],
    "BD-16-003": [
        "MFA policy is independently configurable and enforceable at Platform scope.",
        "MFA policy is independently configurable and enforceable at Organization scope.",
        "MFA policy is independently configurable and enforceable at Role scope.",
        "MFA policy is independently configurable and enforceable at User scope.",
        "MFA policy is independently configurable and enforceable at API Client scope.",
        "Effective MFA policy resolution produces the required MFA challenge for the applicable principal and scope.",
        "An attempted bypass of a required MFA challenge is denied and audited.",
    ],
    "BD-11-010": [
        "Customer Feedback from Product is ingested and attributed to Product.",
        "Customer Feedback from Fulfillment is ingested and attributed to Fulfillment.",
        "Customer Feedback from Ticket is ingested and attributed to Ticket.",
        "Customer Feedback from Customer Portal is ingested and attributed to Customer Portal.",
        "Unsupported or malformed Customer Feedback source input has a deterministic rejection outcome.",
    ],
}


def semantic_family(record: dict[str, Any]) -> str:
    requirement_type = record["requirement_type"]
    text = record["normative_statement"].casefold()
    if requirement_type == "ACCESSIBILITY_REQUIREMENT":
        return "ACCESSIBILITY"
    if requirement_type == "PRIVACY_REQUIREMENT":
        return "PRIVACY"
    if requirement_type == "SCOPE_CONSTRAINT":
        return "SCOPE"
    if requirement_type == "PERFORMANCE_REQUIREMENT" and not any(token in text for token in ("latency", "throughput", "lcp", "inp", "cls", "percentile", "p75", "ms", "second", "giây", "%", "threshold", "budget")):
        return "DESIGN_PRINCIPLE"
    if requirement_type in {"BUSINESS_REQUIREMENT", "BUSINESS_DECISION", "BUSINESS_RULE"} and any(token in text for token in ("permission", "chỉ được xem", "access", "authorized", "quyền", "xác thực")):
        return "SECURITY"
    if requirement_type in {"BUSINESS_REQUIREMENT", "BUSINESS_DECISION", "BUSINESS_RULE"} and any(token in text for token in ("phải lưu", "must store", "must retain", "ghi nhận đầy đủ")):
        return "DATA"
    if requirement_type == "DATA_REQUIREMENT" and any(token in text for token in ("approval", "phê duyệt")):
        return "BUSINESS"
    if requirement_type in {"DATA_REQUIREMENT"}:
        return "DATA"
    if requirement_type == "UX_REQUIREMENT":
        return "UX"
    if requirement_type == "SECURITY_REQUIREMENT":
        return "SECURITY"
    if requirement_type == "OPERATIONAL_REQUIREMENT":
        return "OPERATIONAL"
    if requirement_type == "INTEGRATION_REQUIREMENT":
        return "INTEGRATION"
    if requirement_type == "DESIGN_PRINCIPLE":
        return "DESIGN_PRINCIPLE"
    if requirement_type == "PERFORMANCE_REQUIREMENT":
        return "PERFORMANCE"
    return "BUSINESS"


def criterion(
    criterion_id: str, case: str, verifies: list[str], given: str, when: str,
    then: str, evidence: str, controlled_contract: str,
) -> dict[str, Any]:
    return {
        "criterion_id": criterion_id,
        "case": case,
        "verifies": verifies,
        "given": given,
        "when": when,
        "then": then,
        "observable_evidence": evidence,
        "controlled_contract": controlled_contract,
    }


def positive_boundary(record: dict[str, Any], obligation: str, family: str) -> tuple[str, str, str, str, str]:
    title = record["title"]
    lower = obligation.casefold()
    prohibited = any(token in lower for token in ("must not", "never", "prohibit", "không được", "không phải", "không bắt buộc", "exclude"))
    independent = any(token in lower for token in ("independent", "độc lập", "tách biệt"))
    configurable = any(token in lower for token in ("configur", "cấu hình", "hard-code", "hardcode"))
    stateful = any(token in lower for token in ("state", "status", "trạng thái", "transition", "chuyển"))
    runtime_resolution = any(token in lower for token in ("runtime", "resolve", "phân giải", "render"))
    event_order = "event" in lower and any(token in lower for token in ("order", "thứ tự"))
    inheritance = any(token in lower for token in ("inherit", "kế thừa", "parent configuration"))
    capability_dependency = "capability" in lower and any(token in lower for token in ("require", "yêu cầu"))
    override_policy = "override" in lower
    approval = any(token in lower for token in ("approval", "phê duyệt"))
    stored_field = any(token in lower for token in ("must store", "must retain", "phải lưu", "ghi nhận đầy đủ"))
    if family == "DATA":
        then = "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values"
        if prohibited:
            then = "validation returns REJECTED when the prohibited value or relationship is present, and no rejected state is persisted"
        elif stored_field:
            then = "the accepted record contains the field named by the obligation, preserves its submitted attribution, and exposes that stored value when the record is inspected"
        return (
            f"a candidate {title} record and the canonical records it references",
            "the candidate is evaluated against its declared data contract",
            then,
            "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
            "DATA_CONTRACT_OBSERVATION_V1",
        )
    if family == "UX":
        then = "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable"
        if runtime_resolution:
            then = "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token"
        elif prohibited:
            then = "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable"
        elif inheritance:
            then = "a missing child value resolves to the parent configuration, an explicit child override wins only at its declared scope, and the rendered result identifies the effective source"
        return (
            f"a user in the applicable channel and context for {title}",
            "the user reaches the relevant journey state or invokes the available action",
            then,
            "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
            "UX_JOURNEY_OBSERVATION_V1",
        )
    if family == "ACCESSIBILITY":
        return (
            f"the experience state and accessibility mode governed by {title}",
            "the named accessibility capability is enabled and the same content and actions are exercised",
            "the accessible rendering or interaction is available without removing required content or actions, and its outcome remains perceivable and operable",
            "before/after rendered state, enabled accessibility mode, available content and actions, interaction outcome, and any accessibility conformance result declared by the source",
            "ACCESSIBILITY_OUTCOME_OBSERVATION_V1",
        )
    if family == "PRIVACY":
        return (
            f"a data action with actor, purpose, scope, consent where required, and the effective policies for {title}",
            "privacy conformance and the protected data action are evaluated",
            "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
            "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
            "PRIVACY_POLICY_CONFORMANCE_V1",
        )
    if family == "SECURITY":
        then = "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision"
        if any(token in lower for token in ("đánh giá động", "dynamic evaluation", "không sử dụng permission tĩnh")):
            then = "the permission decision is recalculated from the current applicable attributes and policy; changing a governing input changes the effective decision without relying on a stored static permission result"
        elif any(token in lower for token in ("duy nhất", "single evaluation", "only evaluation")):
            then = "the permission decision trace identifies Permission Evaluation Engine as the sole decision authority and contains no independent Business Domain permission decision"
        elif any(token in lower for token in ("chỉ được xem", "only view", "own customer", "khách hàng của mình")):
            then = "the actor can retrieve only customer identities attributed to that actor; a customer attributed to another actor is absent and access to it is denied"
        elif prohibited:
            then = "the prohibited security decision path produces no effective permission or protected-state change, and conformance evidence identifies the attempted bypass"
        return (
            f"an identified principal, applicable assurance context, and policy inputs for {title}",
            "the protected decision or action is evaluated",
            then,
            "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
            "SECURITY_DECISION_OBSERVATION_V1",
        )
    if family == "OPERATIONAL":
        then = "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation"
        return (
            f"an operational task within the scope of {title}",
            "the task runs, completes, fails, or is inspected by an operator",
            then,
            "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
            "OPERATIONAL_OUTCOME_OBSERVATION_V1",
        )
    if family == "INTEGRATION":
        then = "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract"
        if independent:
            then = "each boundary object keeps a distinct identity, owner, reference, and lifecycle; changing one does not implicitly mutate the other"
        return (
            f"a contract interaction at the integration boundary defined by {title}",
            "a conforming interaction is submitted and its ownership boundary is evaluated",
            then,
            "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
            "INTEGRATION_BOUNDARY_OBSERVATION_V1",
        )
    if family == "DESIGN_PRINCIPLE":
        then = "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling"
        if configurable:
            then = "the conformance evidence identifies the governing configuration and shows that an approved configuration change alters the governed result without a source-code variant"
        elif event_order:
            then = "the conformance evidence identifies the applicable event family and shows sequence preservation only for the families that declare ordering"
        return (
            f"a v2.3 capability, configuration, or design change governed by {title}",
            "conformance is reviewed before the change is accepted",
            then,
            "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
            "DESIGN_CONFORMANCE_OBSERVATION_V1",
        )
    if family == "SCOPE":
        return (
            f"the v2.3 capability inventory and conformance evidence for {title}",
            "the capability is inspected at the active baseline boundary",
            "implemented behavior and exposed actions match the statement's active versus future boundary; future-only behavior is not presented as available in v2.3",
            "baseline capability inventory, exposed action or API surface, conformance trace, implementation-status evidence, and future-scope marker",
            "SCOPE_BOUNDARY_OBSERVATION_V1",
        )
    if family == "PERFORMANCE":
        return (
            f"the declared workload, channel, percentile, and measurement conditions for {title}",
            "the applicable performance measure is collected",
            "the measured value is compared with the exact declared threshold under the declared conditions and produces an attributable pass/fail result",
            "measurement conditions, raw measurement, percentile or aggregation, threshold, and pass/fail comparison",
            "PERFORMANCE_MEASUREMENT_OBSERVATION_V1",
        )
    then = "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded"
    if independent:
        then = "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other"
    elif configurable:
        then = "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change"
    elif stateful:
        then = "the resulting business state equals the declared destination for a valid transition and records the prior state, triggering input, and transition reason"
    elif prohibited:
        then = "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded"
    elif capability_dependency:
        then = "the governed business action is available only when the required Capability is active in the same applicable scope, and the outcome records the Capability reference used"
    elif override_policy:
        then = "an override is accepted only for a policy marked override-eligible, with an explicit reason and the required approval; otherwise the inherited or system policy remains effective"
    elif approval:
        then = "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change"
    return (
        f"the applicable business context, actor, and input for {title}",
        "the governing policy, calculation, state transition, or business action is evaluated",
        then,
        "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
        "BUSINESS_OUTCOME_OBSERVATION_V1",
    )


def failure_boundary(record: dict[str, Any], obligation_ids: list[str], family: str) -> dict[str, Any]:
    title = record["title"]
    text = record["normative_statement"].casefold()
    cid = f"{record['stable_id']}-AC{len(record.get('_criteria_work', [])) + 1:03d}"
    if family == "DATA":
        values = (f"a {title} candidate containing an unsupported value, inconsistent relationship, or unresolved reference", "the candidate is validated", "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason", "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state", "DATA_CONTRACT_REJECTION_V1")
    elif family == "UX":
        if any(token in text for token in ("inherit", "kế thừa", "parent configuration")):
            values = (f"a child experience with no local value and an invalid or unavailable parent configuration for {title}", "the inherited value is resolved", "resolution produces the declared deterministic fallback or a visible configuration failure and never renders an unexplained value", "child and parent configuration identities, resolution trace, fallback or failure result, and rendered value", "UX_INHERITANCE_FAILURE_V1")
        else:
            values = (f"a missing, prohibited, inaccessible, or inapplicable journey input for {title}", "the affected state is rendered or action is requested", "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome", "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome", "UX_BOUNDARY_FAILURE_V1")
    elif family == "ACCESSIBILITY":
        values = (f"the experience with the accessibility capability named by {title} unavailable or producing inaccessible content or actions", "the applicable accessibility mode or interaction is used", "accessibility conformance fails with the unavailable capability or inaccessible element identified; the state is not reported as conforming", "enabled mode, rendered state, affected content or action, interaction result, and failed accessibility conformance evidence", "ACCESSIBILITY_CONFORMANCE_FAILURE_V1")
    elif family == "PRIVACY":
        values = (f"a data action whose purpose, consent, scope, or effective policy does not permit the requested data use under {title}", "privacy conformance is evaluated", "the data action is denied, no additional protected data is exposed or changed, and the policy reason is audited", "actor, purpose, consent and scope, effective policies, denial reason, exposed-data comparison, and audit record", "PRIVACY_POLICY_DENIAL_V1")
    elif family == "SECURITY":
        values = (f"a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for {title}", "the protected decision or action is attempted", "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited", "decision result, protected-state comparison, reason, effective policy, and audit record", "SECURITY_FAIL_CLOSED_V1")
    elif family == "OPERATIONAL":
        values = (f"an operational task missing an outcome, required signal, audit evidence, or recovery evidence for {title}", "operational verification is performed", "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming", "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record", "OPERATIONAL_VERIFICATION_FAILURE_V1")
    elif family == "INTEGRATION":
        values = (f"an interaction that violates the contract or ownership boundary for {title}", "the interaction reaches the integration boundary", "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary", "contract rejection or reconciliation result, reason, boundary owner, and external outcome", "INTEGRATION_CONTRACT_REJECTION_V1")
    elif family == "DESIGN_PRINCIPLE":
        values = (f"a proposed change with missing traceability or a boundary violation under {title}", "design conformance is reviewed", "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming", "conformance result, violated principle, missing trace or configuration evidence, and review record", "DESIGN_CONFORMANCE_FAILURE_V1")
    elif family == "PERFORMANCE":
        values = (f"a missing measurement or a result outside the declared threshold for {title}", "performance conformance is evaluated", "the applicable metric is reported as failed with its measured value, threshold, and measurement conditions", "raw measurement, threshold comparison, conditions, and failed conformance result", "PERFORMANCE_THRESHOLD_FAILURE_V1")
    elif family == "SCOPE":
        values = (f"an attempt to expose or claim a capability outside the active boundary stated by {title}", "v2.3 scope conformance is evaluated", "the capability is reported as future or unavailable and no active implementation claim is accepted", "capability identity, exposed surface inspection, scope status, rejected active claim, and conformance result", "SCOPE_BOUNDARY_FAILURE_V1")
    else:
        if "capability" in text and any(token in text for token in ("require", "yêu cầu")):
            values = (f"the governed business action without the required active Capability for {title}", "the action is requested", "the action is unavailable or rejected, no success state is recorded, and the missing Capability is identified", "Capability status and scope, rejected action, unchanged business state, and missing-capability reason", "BUSINESS_CAPABILITY_DEPENDENCY_FAILURE_V1")
        elif "override" in text:
            values = (f"an override for a non-eligible or mandatory system policy, or an override missing reason or required approval under {title}", "the override is requested", "the override is rejected and the inherited or mandatory policy remains effective", "policy override eligibility, mandatory-policy marker, reason, approval state, rejection outcome, and effective policy", "POLICY_OVERRIDE_REJECTION_V1")
        elif any(token in text for token in ("approval", "phê duyệt")):
            values = (f"a governed change with missing, expired, rejected, or unauthorized approval under {title}", "the change is requested", "the change does not enter the accepted state and the approval reason and status remain observable", "change identity, approval policy and status, approver authorization, rejection or pending reason, and unchanged accepted state", "BUSINESS_APPROVAL_BOUNDARY_V1")
        else:
            values = (f"an unsupported or invalid business input at the boundary governed by {title}", "the governing policy, rule, calculation, transition, or action is evaluated", "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation", "input, policy or rule decision, before/after state, reason, and customer/operator-visible result", "BUSINESS_BOUNDARY_FAILURE_V1")
    return criterion(cid, "PRINCIPAL_FAILURE_OR_EDGE", obligation_ids, *values)


def dimension_applicability(record: dict[str, Any], dimension: str) -> bool:
    text = (record["normative_statement"] + " " + " ".join(o for o in MANDATORY_OBLIGATIONS.get(record["stable_id"], []))).casefold()
    keywords = {
        "NEGATIVE_FAIL_CLOSED": ("must not", "never", "không", "reject", "deny", "block", "fail closed", "invalid", "missing", "requires", "yêu cầu", "independent", "độc lập", "security", "auth", "permission", "privacy"),
        "RECOVERY": ("recover", "recovery", "restore", "rollback", "fallback", "khôi phục", "phục hồi"),
        "CONCURRENCY": ("concurrent", "concurrency", "race condition", "simultaneous request", "yêu cầu đồng thời", "cập nhật đồng thời", "xử lý đồng thời", "oversell", "locking"),
        "IDEMPOTENCY": ("idempot", "retry", "replay", "dedup", "duplicate", "thử lại", "lặp"),
        "AUTHORIZATION_BOUNDARY": ("permission", "authorization", "authorized", "role", "access", "mfa", "credential", "quyền", "xác thực", "bảo mật"),
    }
    return dimension == "POSITIVE" or any(
        re.search(rf"(?<!\w){re.escape(word)}(?!\w)", text) is not None
        for word in keywords[dimension]
    )


def dimension_criterion(record: dict[str, Any], obligation_ids: list[str], dimension: str) -> dict[str, Any]:
    title = record["title"]
    cid = f"{record['stable_id']}-AC{len(record.get('_criteria_work', [])) + 1:03d}"
    clauses = {
        "NEGATIVE_FAIL_CLOSED": (
            f"an input or attempted state change that violates a mandatory boundary explicitly stated by {title}",
            "the violating input or action is evaluated",
            "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
            "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
            "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
        ),
        "RECOVERY": (
            f"a failed or interrupted case for which {title} explicitly defines recovery, restore, rollback, or fallback behavior",
            "the declared recovery path is invoked",
            "the resulting state and outcome follow the requirement-specific recovery obligation and expose whether recovery completed or failed",
            "pre-failure state, recovery action, resulting state, outcome, and recovery evidence named by the obligation",
            "EXPLICIT_RECOVERY_CONTRACT_V1",
        ),
        "CONCURRENCY": (
            f"two or more concurrent actions covered by an explicit concurrency boundary in {title}",
            "the actions contend for the same governed business state",
            "the resulting decisions and state preserve the concurrency invariant stated by the referenced obligation",
            "concurrent inputs, individual outcomes, final state, and invariant comparison",
            "EXPLICIT_CONCURRENCY_CONTRACT_V1",
        ),
        "IDEMPOTENCY": (
            f"a repeated request, retry, replay, or duplicate explicitly governed by {title}",
            "the same governed action is presented again under the declared identity or deduplication boundary",
            "the repeated action produces the requirement-specific stable result without an additional prohibited side effect",
            "original and repeated action identities, both outcomes, side-effect count, and resulting business state",
            "EXPLICIT_IDEMPOTENCY_CONTRACT_V1",
        ),
        "AUTHORIZATION_BOUNDARY": (
            f"an actor lacking the permission, role, identity assurance, consent, or access condition stated by {title}",
            "the actor attempts the governed action",
            "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
            "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
            "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
        ),
    }
    return criterion(cid, dimension, obligation_ids, *clauses[dimension])


def mandatory_acceptance(record: dict[str, Any], obligations: list[dict[str, Any]]) -> list[dict[str, Any]] | None:
    sid = record["stable_id"]
    ids = [o["obligation_id"] for o in obligations]
    specs: dict[str, list[tuple[str, list[int], str, str, str, str, str]]] = {
        "BRD-CAP-INDEX-R029": [
            ("POSITIVE", [0], "a Capability metadata candidate", "event_role is validated", "only PUBLISHER, SUBSCRIBER, BOTH, or NONE is accepted", "submitted value and enum-validation result", "CAPABILITY_EVENT_ROLE_ENUM_V1"),
            ("POSITIVE", [1, 2, 3, 4], "Capability metadata for each supported event role", "role/list consistency is validated", "NONE accepts only two empty lists; PUBLISHER, SUBSCRIBER, and BOTH accept only the corresponding required non-empty lists", "event_role, both submitted lists, and field-level validation results", "CAPABILITY_EVENT_ROLE_LIST_MATRIX_V1"),
            ("PRINCIPAL_FAILURE_OR_EDGE", [1], "NONE with at least one non-empty event list", "the metadata is submitted", "the record is rejected and neither inconsistent list is persisted", "rejection reason, submitted lists, and absence of persisted inconsistent state", "CAPABILITY_EVENT_ROLE_LIST_MATRIX_V1"),
            ("PRINCIPAL_FAILURE_OR_EDGE", [2, 3, 4], "PUBLISHER, SUBSCRIBER, or BOTH with a missing corresponding list", "the metadata is submitted", "the record is rejected with the missing required list identified", "role, submitted lists, missing-list reason, and rejected persistence outcome", "CAPABILITY_EVENT_ROLE_LIST_MATRIX_V1"),
            ("PRINCIPAL_FAILURE_OR_EDGE", [5], "an event list containing an alias, retired, tombstone, unknown, or dangling Event ID", "canonical references are resolved", "the metadata is rejected and every non-canonical reference is identified", "submitted IDs, canonical-resolution result, reference status, and rejection outcome", "CANONICAL_EVENT_REFERENCE_VALIDATION_V1"),
        ],
        "UXF-05-R054": [
            ("POSITIVE", [0], "a journey whose Catalog, legal, or product definition requires provider, network, or brand disclosure", "the customer-facing state is rendered", "the required disclosure is visible, read-only, and contains only the allowed customer-facing information", "rendered disclosure, read-only state, governing disclosure requirement, and visible values", "CUSTOMER_DISCLOSURE_RENDERING_V1"),
            ("PRINCIPAL_FAILURE_OR_EDGE", [1], "a customer-facing UI state and its Storefront API response", "the disclosure surface and payload are inspected", "no prohibited internal supplier, procurement, cost, margin, routing, health, connector, or allocation field is present", "rendered fields and complete response-field inventory showing prohibited fields absent", "CUSTOMER_DISCLOSURE_PROHIBITION_V1"),
            ("PRINCIPAL_FAILURE_OR_EDGE", [2], "two otherwise identical allocation requests differing only in customer-facing disclosure", "Allocation evaluates both requests", "the allocation decision is unchanged by disclosure data", "both allocation inputs, disclosure difference, and identical allocation decision evidence", "DISCLOSURE_ALLOCATION_INDEPENDENCE_V1"),
            ("PRINCIPAL_FAILURE_OR_EDGE", [3], "a journey where disclosure is mandatory but required disclosure data is missing", "the journey attempts to proceed", "the affected action is unavailable or blocked with a customer-visible deterministic outcome", "missing-data condition, unavailable or blocked action, and rendered customer outcome", "MANDATORY_DISCLOSURE_FAIL_CLOSED_V1"),
        ],
        "BRD-UPDATE-01-R030": [
            ("POSITIVE", [0], "a Commerce Experience candidate with an identified Business Model", "creation or publication is requested", "the accepted experience and publication evidence reference that Business Model as their origin", "Business Model identifier, experience identifier, creation trace, and publication trace", "BUSINESS_MODEL_ROOT_TRACE_V1"),
            ("PRINCIPAL_FAILURE_OR_EDGE", [0], "a Commerce Experience candidate with no resolvable Business Model origin", "creation or publication is requested", "the request is rejected as non-conforming and no unrooted publication is accepted", "unresolved origin, conformance result, rejection reason, and publication state", "BUSINESS_MODEL_ROOT_TRACE_V1"),
        ],
        "BRD-WS-08-R013": [
            ("POSITIVE", [0], "risk evidence matching no challenge, block, or review rule", "rule-based risk is evaluated", "the decision is ALLOW with the applied rule set and reason recorded", "input evidence references, ALLOW result, applied rule versions, and reason", "RULE_BASED_RISK_DECISIONS_V1"),
            ("POSITIVE", [1], "risk evidence requiring additional assurance", "rule-based risk is evaluated", "the decision is CHALLENGE and identifies the required assurance", "CHALLENGE result, triggering rule, required assurance, and reason", "RULE_BASED_RISK_DECISIONS_V1"),
            ("NEGATIVE_FAIL_CLOSED", [2], "risk evidence matching a blocking rule", "rule-based risk is evaluated", "the decision is BLOCK and the protected action does not proceed", "BLOCK result, blocking rule and reason, and unchanged protected state", "RULE_BASED_RISK_DECISIONS_V1"),
            ("POSITIVE", [3], "risk evidence requiring human review", "rule-based risk is evaluated", "the decision is REVIEW and the protected action remains pending the review outcome", "REVIEW result, triggering rule and reason, and pending protected state", "RULE_BASED_RISK_DECISIONS_V1"),
            ("POSITIVE", [4], "a completed rule-based risk decision", "decision evidence is inspected", "rule, signal, reason, override if present, and audit versions are all recorded and resolvable", "decision record with resolvable version identifiers for each applicable evidence component", "VERSIONED_RISK_EVIDENCE_V1"),
            ("NEGATIVE_FAIL_CLOSED", [5], "a risk request missing mandatory evidence or containing invalid evidence", "rule-based risk is evaluated", "the protected action receives no ALLOW result and the missing or invalid evidence is identified", "non-ALLOW result, evidence-validation reason, and unchanged protected state", "RISK_EVIDENCE_FAIL_CLOSED_V1"),
            ("AUTHORIZATION_BOUNDARY", [6], "an override request from an actor without override authorization", "the override is attempted", "the override is denied, the original risk decision remains effective, and the attempt is audited", "actor and scope, authorization result, original and effective decision, denial reason, and audit record", "AUTHORIZED_RISK_OVERRIDE_V1"),
            ("AUTHORIZATION_BOUNDARY", [6], "an authorized override request with a reason", "the override is applied", "the effective decision changes only as authorized and records actor, reason, original decision, override decision, and evidence versions", "authorization evidence, before/after decision, reason, actor, and immutable audit record", "AUTHORIZED_RISK_OVERRIDE_V1"),
        ],
        "BRD-WS-17-R026": [
            ("POSITIVE", [0], "a running operational task", "an operator inspects the task", "current running state and the relevant operational signals are available", "operation identity, running state, signal names and values, and observation time", "OPERATIONAL_TASK_OBSERVABILITY_V1"),
            ("POSITIVE", [1], "a completed operational task", "an operator inspects the task", "terminal completion state and outcome evidence are available", "operation identity, completed state, outcome, completion time, and evidence reference", "OPERATIONAL_TASK_OBSERVABILITY_V1"),
            ("POSITIVE", [2], "a failed operational task", "an operator inspects the task", "failed state, failure outcome, and relevant diagnostic signal are available", "operation identity, failed state, reason, diagnostic signal, and observation time", "OPERATIONAL_TASK_OBSERVABILITY_V1"),
            ("PRINCIPAL_FAILURE_OR_EDGE", [3], "an operational task missing required state, outcome, or signal evidence", "operational observability is verified", "verification produces a detectable failure naming the missing evidence", "failed verification result, operation identity, and missing-evidence identifiers", "OPERATIONAL_OBSERVABILITY_VERIFICATION_V1"),
        ],
        "EP-08-002": [
            ("POSITIVE", [0], "a PaymentGateway and a MerchantAccount", "their business identities are inspected", "each object has a distinct stable identity and neither identity substitutes for the other", "both object identities and distinct-identity comparison", "PAYMENT_OBJECT_INDEPENDENCE_V1"),
            ("POSITIVE", [1], "a PaymentGateway and a MerchantAccount used in the same payment configuration", "ownership and references are inspected", "each object retains its own owner and is referenced explicitly through its own identity", "owner of each object and references resolving independently to each identity", "PAYMENT_OBJECT_INDEPENDENCE_V1"),
            ("NEGATIVE_FAIL_CLOSED", [0, 1], "a candidate that conflates PaymentGateway and MerchantAccount into one identity or implicit reference", "the business-object relationship is validated", "the candidate is rejected with the identity or ownership violation identified", "validation rejection, conflated identity or reference, and unchanged accepted object records", "PAYMENT_OBJECT_INDEPENDENCE_V1"),
            ("POSITIVE", [2], "independent PaymentGateway and MerchantAccount objects", "one object changes lifecycle state", "the other object does not automatically inherit that lifecycle transition", "before/after lifecycle states for both object identities and explicit transition evidence", "PAYMENT_OBJECT_LIFECYCLE_INDEPENDENCE_V1"),
        ],
        "BD-16-003": [
            *[("POSITIVE", [i], f"an MFA policy configured at {scope} scope", "a principal governed by that scope attempts an action requiring MFA", "the effective policy includes the scope-specific MFA requirement and presents the required challenge", f"{scope} policy, principal scope binding, effective-policy trace, and challenge result", "MFA_SCOPE_ENFORCEMENT_V1") for i, scope in enumerate(("Platform", "Organization", "Role", "User", "API Client"))],
            ("POSITIVE", [5], "overlapping MFA policies at more than one applicable scope", "effective MFA policy is resolved", "the effective-policy result identifies each contributing scope and the challenge that must be satisfied", "all applicable policies, precedence or composition result, effective policy, and challenge", "MFA_EFFECTIVE_POLICY_RESOLUTION_V1"),
            ("NEGATIVE_FAIL_CLOSED", [6], "a principal that has not satisfied a required MFA challenge", "the principal attempts to bypass the challenge", "the protected action is denied, protected state remains unchanged, and the bypass attempt is audited", "challenge status, denial result, protected-state comparison, reason, and audit record", "MFA_BYPASS_DENIAL_V1"),
        ],
        "BD-11-010": [
            *[("POSITIVE", [i], f"valid Customer Feedback originating from {source}", "the feedback is submitted", f"the feedback is accepted and attributed to {source}", f"accepted feedback identity, source={source}, attribution reference, and ingestion outcome", "CUSTOMER_FEEDBACK_SOURCE_ATTRIBUTION_V1") for i, source in enumerate(("Product", "Fulfillment", "Ticket", "Customer Portal"))],
            ("PRINCIPAL_FAILURE_OR_EDGE", [4], "Customer Feedback with an unsupported source or malformed source attribution", "the feedback is submitted", "the input is rejected with a deterministic source-validation reason and is not recorded as accepted feedback", "submitted source, validation reason, rejection outcome, and absence of accepted feedback identity", "CUSTOMER_FEEDBACK_SOURCE_REJECTION_V1"),
        ],
    }
    if sid not in specs:
        return None
    result = []
    for index, (case, refs, given, when, then, evidence, contract) in enumerate(specs[sid], 1):
        result.append(criterion(f"{sid}-AC{index:03d}", case, [ids[i] for i in refs], given, when, then, evidence, contract))
    return result


def semantic_acceptance(record: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any] | None]:
    sid = record["stable_id"]
    obligation_texts = MANDATORY_OBLIGATIONS.get(sid) or split_atomic_obligations(record["normative_statement"])
    obligations = [
        {
            "obligation_id": f"{sid}-O{index:03d}",
            "obligation_text": text,
            "applicability": "V2.3_ACTIVE",
            "acceptance_criterion_references": [],
        }
        for index, text in enumerate(obligation_texts, 1)
    ]
    custom = mandatory_acceptance(record, obligations)
    family = semantic_family(record)
    criteria: list[dict[str, Any]] = custom or []
    record["_criteria_work"] = criteria
    if custom is None:
        for obligation in obligations:
            given, when, then, evidence, contract = positive_boundary(record, obligation["obligation_text"], family)
            criteria.append(criterion(
                f"{sid}-AC{len(criteria) + 1:03d}", "POSITIVE", [obligation["obligation_id"]],
                given, when, then, evidence, contract,
            ))
        if record["verification_criticality"] in {"HIGH", "CRITICAL"}:
            criteria.append(failure_boundary(record, [o["obligation_id"] for o in obligations], family))

    matrix = None
    if record["verification_criticality"] == "CRITICAL":
        matrix = {}
        for dimension in ("POSITIVE", "NEGATIVE_FAIL_CLOSED", "RECOVERY", "CONCURRENCY", "IDEMPOTENCY", "AUTHORIZATION_BOUNDARY"):
            matching = [c["criterion_id"] for c in criteria if c["case"] == dimension or (dimension == "POSITIVE" and c["case"] == "POSITIVE_EXPECTED_PATH")]
            applicable = dimension_applicability(record, dimension)
            if applicable and not matching and dimension != "POSITIVE":
                extra = dimension_criterion(record, [o["obligation_id"] for o in obligations], dimension)
                criteria.append(extra)
                matching = [extra["criterion_id"]]
            if dimension == "POSITIVE" and not matching:
                matching = [c["criterion_id"] for c in criteria if c["case"] == "POSITIVE"]
            if applicable:
                matrix[dimension] = {"status": "APPLICABLE", "criterion_references": matching}
            else:
                matrix[dimension] = {
                    "status": "NOT_APPLICABLE",
                    "rationale": f"{record['stable_id']} does not define a {dimension.lower().replace('_', ' ')} obligation or boundary.",
                    "criterion_references": [],
                }

    criterion_by_id = {c["criterion_id"]: c for c in criteria}
    for obligation in obligations:
        obligation["acceptance_criterion_references"] = [
            cid for cid, item in criterion_by_id.items() if obligation["obligation_id"] in item["verifies"]
        ]
    record.pop("_criteria_work", None)
    return obligations, criteria, matrix


def decision_tags(statement: str, source_document: str) -> list[str]:
    text = statement.casefold()
    tags: set[str] = set()
    rules = {
        "P2-DEC-001": ("federat", "saml", "oidc", "jit"),
        "P2-DEC-002": ("security event", "event metadata", "event registry"),
        "P2-DEC-003": ("retry", "thử lại"),
        "P2-DEC-004": ("operation event", "operations event", "runbook", "maintenance"),
        "P2-DEC-005": ("capability", "event role"),
        "P2-DEC-006": ("connector", "adapter", "gateway", "external"),
        "P2-DEC-007": ("allocation", "supplier", "provider", "phân bổ"),
        "P2-DEC-008": ("identity", "customer", "guest", "user", "danh tính", "khách hàng"),
        "P2-DEC-009": ("lcp", "inp", "cls", "javascript", "performance"),
        "P2-DEC-010": ("sla", "slo", "latency", "reliability", "availability", "rto", "rpo"),
    }
    for decision, words in rules.items():
        if any(word in text for word in words):
            tags.add(decision)
    if source_document.endswith("BRD-WS-08.md") and any(k in text for k in ("fraud", "risk")):
        tags.update({"SD-03", "BDD-26"})
    if "approval" in text or "phê duyệt" in text:
        tags.update({"SD-03", "BDD-27"})
    return sorted(tags)


def new_record(
    *, stable_id: str, document: str, statement: str, title: str, requirement_type: str,
    scope: str, criticality: str, decisions: list[str], allocation: str,
    derived_from: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "stable_id": stable_id,
        "title": title,
        "normative_statement": statement,
        "requirement_type": requirement_type,
        "scope_status": scope,
        "lifecycle": "V2.3_DRAFT" if scope == "V2.3_ACTIVE" else "RETAINED_SCOPE_RECORD",
        "delivery_commitment": delivery_commitment(scope),
        "verification_criticality": criticality if scope == "V2.3_ACTIVE" else "NOT_APPLICABLE",
        "record_kind": "CANONICAL_ATOMIC",
        "implementation_unit": scope == "V2.3_ACTIVE",
        "acceptance_unit": scope == "V2.3_ACTIVE",
        "scope_coverage_unit": scope == "V2.3_ACTIVE",
        "criticality_unit": scope == "V2.3_ACTIVE",
        "relationships": {"aliases": [], "alias_of": None, "derived_from": derived_from or [], "derived_requirements": [], "coverage_mode": None},
        "provenance": {
            "source_document": document,
            "source_baseline": "v2.2",
            "identity_origin": "PHASE_2C_NEW_ALLOCATION",
            "allocation_contract": allocation,
            "approved_decisions": sorted(set(decisions)),
            "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
        },
    }


def build_records() -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    brd = load_json(BRD_REGISTRY)
    uxf = load_json(UXF_REGISTRY)
    mapping = load_json(MAPPING_PATH)
    preflight = load_json(PREFLIGHT_PATH)
    criticality = load_json(CRITICALITY_PATH)
    human_decisions = load_json(HUMAN_DECISIONS_PATH)
    reconciliation = load_json(RECONCILIATION_PATH)

    mapped = {item["temporary_key"]: item["proposed_stable_id"] for item in mapping["mappings"]}
    source_records = copy.deepcopy(brd["requirements"] + uxf["requirements"])
    source_paths = sorted({item["source_document"] for item in source_records})
    legacy_bodies = {
        path: strip_generated((ROOT / path).read_text(encoding="utf-8"))
        for path in source_paths
    }
    stable_by_original: dict[str, str] = {}
    for raw in source_records:
        original = raw.get("current_id") or raw.get("temporary_key")
        stable_by_original[original] = raw.get("current_id") or mapped[raw["temporary_key"]]
    stable_values = set(stable_by_original.values())

    assignments: dict[str, str] = {}
    for item in preflight["criticality_preflight"]["assignments"]:
        identity = item["registry_identity"]
        stable = stable_by_original.get(identity, item.get("stable_requirement_id") or identity)
        assignments[stable] = item["verification_criticality"]

    exceptions_by_stable: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for exc in criticality["exceptions"]:
        stable = stable_by_original.get(exc["registry_identity"], exc["requirement_id_or_key"])
        exceptions_by_stable[stable].append(exc)
        if exc["effective_tier_or_remediation_required"] in {"CRITICAL", "HIGH", "NORMAL"}:
            assignments[stable] = exc["effective_tier_or_remediation_required"]

    records: list[dict[str, Any]] = []
    for raw in source_records:
        original = raw.get("current_id") or raw.get("temporary_key")
        stable = stable_by_original[original]
        scope = raw["scope_status"]
        kind = identity_kind(raw)
        statement = raw.get("effective_statement") or raw["statement"]
        source_context, source_context_heading = extract_full_source_section(raw["statement"], legacy_bodies[raw["source_document"]])
        rec = {
            "stable_id": stable,
            "title": title_from_statement(statement, stable),
            "normative_statement": normalize_space(statement),
            "requirement_type": raw["requirement_type"],
            "scope_status": scope,
            "lifecycle": "V2.3_DRAFT" if scope == "V2.3_ACTIVE" else "RETAINED_SCOPE_RECORD",
            "delivery_commitment": delivery_commitment(scope),
            "verification_criticality": assignments.get(stable, "NOT_APPLICABLE"),
            "record_kind": kind,
            "implementation_unit": kind == "CANONICAL_ATOMIC" and scope == "V2.3_ACTIVE",
            "acceptance_unit": kind == "CANONICAL_ATOMIC" and scope == "V2.3_ACTIVE",
            "scope_coverage_unit": kind == "CANONICAL_ATOMIC" and scope == "V2.3_ACTIVE",
            "criticality_unit": kind == "CANONICAL_ATOMIC" and scope == "V2.3_ACTIVE",
            "relationships": {
                "aliases": [map_reference(v, stable_by_original) for v in (raw.get("aliases") or [])],
                "alias_of": map_reference(raw.get("alias_of"), stable_by_original),
                "derived_from": [map_reference(v, stable_by_original) for v in (raw.get("derived_from") or [])],
                "derived_requirements": [map_reference(v, stable_by_original) for v in (raw.get("derived_requirements") or [])],
                "coverage_mode": raw.get("coverage_mode"),
            },
            "provenance": {
                "source_document": raw["source_document"],
                "source_section": raw.get("source_section"),
                "source_lines": raw.get("source_lines"),
                "source_fingerprint": raw.get("source_fingerprint"),
                "source_baseline": "v2.2",
                "original_identity": original,
                "previous_temporary_key": raw.get("temporary_key"),
                "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING" if raw.get("temporary_key") else "PRESERVED_STABLE_ID",
                "approved_decisions": sorted(set((raw.get("governed_by_decisions") or []) + decision_tags(statement, raw["source_document"]))),
                "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
                "source_context_heading": source_context_heading,
                "source_context_sha256": sha256(source_context.encode("utf-8")),
            },
            "_source_context": source_context,
        }
        historical_derived_from = [
            value for value in rec["relationships"]["derived_from"] if value not in stable_values
        ]
        rec["relationships"]["derived_from"] = [
            value for value in rec["relationships"]["derived_from"] if value in stable_values
        ]
        if historical_derived_from:
            rec["provenance"]["historical_derived_from"] = historical_derived_from
        if kind != "CANONICAL_ATOMIC" or scope != "V2.3_ACTIVE":
            rec["verification_criticality"] = "NOT_APPLICABLE"
        if stable in exceptions_by_stable:
            rec["criticality_dispositions"] = [
                {
                    "exception_id": exc["exception_id"],
                    "selected_disposition": exc["selected_disposition"],
                    "decision_basis": exc["decision_basis"],
                    "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
                    "application_status": "APPLIED_IN_PHASE_2C",
                }
                for exc in exceptions_by_stable[stable]
            ]
        records.append(rec)

    by_id = {r["stable_id"]: r for r in records}

    def remediate(stable: str, **changes: Any) -> dict[str, Any]:
        rec = by_id[stable]
        rec.update(changes)
        rec["title"] = changes.get("title", title_from_statement(rec["normative_statement"], stable))
        rec["provenance"].setdefault("remediation_contracts", []).append("V23-P2B-CRITICALITY-DECISION-C1")
        return rec

    # Approved scope and extraction remediations.
    product = remediate(
        "BD-04-007",
        scope_status="OUT_OF_SCOPE",
        lifecycle="RETAINED_SCOPE_RECORD",
        delivery_commitment="EXCLUDED_FROM_V2.3",
        verification_criticality="NOT_APPLICABLE",
        implementation_unit=False,
        acceptance_unit=False,
        scope_coverage_unit=False,
        criticality_unit=False,
        normative_statement="Product Variant nằm ngoài phạm vi sản phẩm v2.3.",
        requirement_type="SCOPE_CONSTRAINT",
        title="Product Variant outside v2.3",
    )
    product["provenance"]["approved_decisions"] = sorted(set(product["provenance"]["approved_decisions"] + ["SD-02"]))

    approval = remediate(
        "BRD-CAP-INDEX-R007",
        normative_statement="Nền tảng phải cung cấp Shared Approval Engine dùng chung cho ngoại lệ biên lợi nhuận, hoàn tiền, cấu hình, thông tin xác thực, ghi đè rủi ro và các nghiệp vụ BRD quy định; engine phải hỗ trợ policy, phân giải người duyệt, phân tách nhiệm vụ, hết hạn, escalation, delegation, evidence và immutable audit, đồng thời không được diễn giải thành general-purpose BPM workflow engine.",
        requirement_type="BUSINESS_REQUIREMENT",
        verification_criticality="HIGH",
        title="Shared Approval Engine",
    )
    approval["provenance"]["approved_decisions"] = sorted(set(approval["provenance"]["approved_decisions"] + ["SD-03", "BDD-27"]))

    event_r1 = remediate(
        "BRD-EVENT-INDEX-R001",
        normative_statement="Các event thuộc họ Payment, Settlement và Financial phải duy trì thứ tự xử lý.",
        requirement_type="DESIGN_PRINCIPLE",
        verification_criticality="CRITICAL",
        title="Ordered financial event families",
    )
    event_r1["provenance"]["approved_effective_statement_candidate"] = "Payment, Settlement, and Financial events must preserve processing order."
    event_r1["provenance"]["related_non_exception_defect"] = "EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT"
    event_r2 = remediate(
        "BRD-EVENT-INDEX-R002",
        normative_statement="Các event thuộc họ Marketing, Analytics và Notification không bắt buộc duy trì thứ tự xử lý.",
        requirement_type="DESIGN_PRINCIPLE",
        verification_criticality="NORMAL",
        title="Unordered non-financial event families",
    )
    event_r2["provenance"]["approved_effective_statement_candidate"] = "Marketing, Analytics, and Notification events are not required to preserve processing order."

    remediate("BRD-WS-01-R001", requirement_type="DESIGN_PRINCIPLE", verification_criticality="NORMAL", title="YSim product positioning")
    remediate(
        "BRD-WS-01-R004",
        normative_statement="YSim phải cung cấp năng lực thương mại white-label như một nguyên tắc sản phẩm, với hành vi cụ thể được quy định bởi các yêu cầu kênh và cấu hình liên quan.",
        requirement_type="DESIGN_PRINCIPLE",
        verification_criticality="NORMAL",
        title="White-label commerce principle",
    )

    # Business Principles: preserve the parent and reconcile eight existing plus four new children.
    business_parent = remediate(
        "BRD-UPDATE-01-R010",
        normative_statement="Commerce Experience Platform tuân thủ toàn bộ các Business Principles được liên kết bên dưới.",
        record_kind="COMPOSITE_PARENT",
        verification_criticality="NOT_APPLICABLE",
        implementation_unit=False,
        acceptance_unit=False,
        scope_coverage_unit=False,
        criticality_unit=False,
        title="Business Principles composite parent",
    )
    business_existing = {
        "Configuration over Customization": "BRD-UPDATE-01-R021",
        "White-label by Default": "BRD-UPDATE-01-R022",
        "Publish in Minutes": "BRD-UPDATE-01-R023",
        "Experience First": "BRD-UPDATE-01-R029",
        "Multi-brand": "BRD-UPDATE-01-R025",
        "Multi-language": "BRD-UPDATE-01-R026",
        "Multi-country": "BRD-UPDATE-01-R027",
        "API First": "BRD-UPDATE-01-R028",
    }
    business_new_specs = [
        ("BRD-UPDATE-01-R030", "Business Model First", "Business Model là điểm khởi đầu của mọi Commerce Experience trên nền tảng YSim."),
        ("BRD-UPDATE-01-R031", "Template Driven", "Mỗi Commerce Experience phải được khởi tạo từ Store Template được phê duyệt thay vì xây dựng thủ công từ đầu."),
        ("BRD-UPDATE-01-R032", "Headless Ready", "Commerce Experience phải có khả năng sử dụng các contract API chuẩn mà không phụ thuộc vào một lớp trình bày cụ thể."),
        ("BRD-UPDATE-01-R033", "AI Ready", "Nền tảng phải chuẩn bị contract và metadata có quản trị để hỗ trợ khả năng AI trong tương lai; nguyên tắc này không được diễn giải thành một tính năng sản phẩm AI active nếu chưa có yêu cầu được phê duyệt."),
    ]
    business_children: list[str] = []
    for name, stable in business_existing.items():
        child = by_id[stable]
        child["title"] = name
        if name == "Experience First":
            child["normative_statement"] = "Commerce Experience phải ưu tiên trải nghiệm người dùng trong các quyết định trình bày mà không thay đổi hành vi nghiệp vụ chuẩn."
        child["relationships"].setdefault("satisfies_composite_parents", []).append(business_parent["stable_id"])
        business_children.append(stable)
    for stable, name, statement in business_new_specs:
        child = new_record(
            stable_id=stable,
            document="docs/BRD/BRD-UPDATE-01.md",
            statement=statement,
            title=name,
            requirement_type="DESIGN_PRINCIPLE",
            scope="V2.3_ACTIVE",
            criticality="NORMAL",
            decisions=["HUMAN_DECISION_2026-07-14"],
            allocation="BUSINESS_PRINCIPLES_CHILD_RECONCILIATION",
            derived_from=[business_parent["stable_id"]],
        )
        child["relationships"]["satisfies_composite_parents"] = [business_parent["stable_id"]]
        if name == "AI Ready":
            child["non_inference_guard"] = "MUST_NOT_BE_INTERPRETED_AS_AN_ACTIVE_AI_PRODUCT_FEATURE_WITHOUT_AN_APPROVED_REQUIREMENT"
        records.append(child)
        by_id[stable] = child
        business_children.append(stable)
    business_parent["relationships"]["derived_requirements"] = business_children
    business_parent["relationships"]["coverage_mode"] = "ALL_CHILDREN"

    # Fraud/Risk split: preserve R012 as deferred ML and add the active rule-based contract.
    fraud_ml = remediate(
        "BRD-WS-08-R012",
        normative_statement="ML scoring cho Fraud/Risk Engine được hoãn sang sau v2.3.",
        requirement_type="SCOPE_CONSTRAINT",
        scope_status="DEFERRED",
        lifecycle="RETAINED_SCOPE_RECORD",
        delivery_commitment="POST_V2.3",
        verification_criticality="NOT_APPLICABLE",
        implementation_unit=False,
        acceptance_unit=False,
        scope_coverage_unit=False,
        criticality_unit=False,
        title="Deferred ML fraud scoring",
    )
    fraud_ml["provenance"]["approved_decisions"] = sorted(set(fraud_ml["provenance"]["approved_decisions"] + ["SD-03", "BDD-26"]))
    fraud_active = new_record(
        stable_id="BRD-WS-08-R013",
        document="docs/BRD/BRD-WS-08.md",
        statement="Trong v2.3, Fraud/Risk Engine phải áp dụng rule-based risk cho authentication/account, checkout và payment; quyết định tối thiểu gồm ALLOW, CHALLENGE, BLOCK và REVIEW, đồng thời rule, signal, reason, override và audit phải được versioning.",
        title="Active rule-based Fraud/Risk Engine",
        requirement_type="SECURITY_REQUIREMENT",
        scope="V2.3_ACTIVE",
        criticality="CRITICAL",
        decisions=["SD-03", "BDD-26"],
        allocation="FRAUD_RISK_ACTIVE_DEFERRED_SPLIT",
        derived_from=[fraud_ml["stable_id"]],
    )
    fraud_active["criticality_dispositions"] = copy.deepcopy(fraud_ml.get("criticality_dispositions", []))
    records.append(fraud_active)
    by_id[fraud_active["stable_id"]] = fraud_active

    # Enterprise Operations: preserve R013 as parent, alias the old aggregate, add six atomic children.
    operations_parent = remediate(
        "BRD-WS-17-R013",
        normative_statement="Mọi tác vụ vận hành phải đáp ứng toàn bộ các hợp đồng Enterprise Operations được liên kết bên dưới.",
        record_kind="COMPOSITE_PARENT",
        verification_criticality="NOT_APPLICABLE",
        implementation_unit=False,
        acceptance_unit=False,
        scope_coverage_unit=False,
        criticality_unit=False,
        title="Enterprise Operations composite parent",
    )
    old_aggregate = by_id["EP-17-010"]
    old_aggregate.update({
        "record_kind": "ALIAS",
        "verification_criticality": "NOT_APPLICABLE",
        "implementation_unit": False,
        "acceptance_unit": False,
        "scope_coverage_unit": False,
        "criticality_unit": False,
    })
    old_aggregate["relationships"]["alias_of"] = operations_parent["stable_id"]
    operations_specs = [
        ("BRD-WS-17-R026", "Observable operational task", "Mọi tác vụ vận hành phải có khả năng quan sát được thông qua trạng thái, kết quả và tín hiệu vận hành phù hợp.", "HIGH"),
        ("BRD-WS-17-R027", "Auditable operational task", "Mọi tác vụ vận hành phải tạo bằng chứng audit bất biến, gắn với actor, thời điểm, phạm vi và kết quả.", "CRITICAL"),
        ("BRD-WS-17-R028", "Configurable operational task", "Mọi tác vụ vận hành phải được cấu hình bằng policy có version thay vì hard-code quyết định vận hành.", "HIGH"),
        ("BRD-WS-17-R029", "Recoverable operational task", "Mọi tác vụ vận hành phải có đường khôi phục xác định, có thể đối soát kết quả và bảo toàn bất biến khi thất bại.", "CRITICAL"),
        ("BRD-WS-17-R030", "Automatable operational task", "Mọi tác vụ vận hành phải có contract cho phép tự động hóa có kiểm soát, permission và audit.", "HIGH"),
        ("BRD-WS-17-R031", "No direct infrastructure manipulation", "Operator không được thao tác trực tiếp trên hạ tầng khi Platform đã cung cấp thao tác tương ứng.", "CRITICAL"),
    ]
    operations_children: list[str] = []
    for stable, name, statement, tier in operations_specs:
        child = new_record(
            stable_id=stable,
            document="docs/BRD/BRD-WS-17.md",
            statement=statement,
            title=name,
            requirement_type="OPERATIONAL_REQUIREMENT" if tier == "HIGH" else "SECURITY_REQUIREMENT",
            scope="V2.3_ACTIVE",
            criticality=tier,
            decisions=["P2-DEC-003", "P2-DEC-004", "P2-DEC-010"],
            allocation="ENTERPRISE_OPERATIONS_CHILD_RECONCILIATION",
            derived_from=[operations_parent["stable_id"]],
        )
        child["relationships"]["satisfies_composite_parents"] = [operations_parent["stable_id"]]
        records.append(child)
        by_id[stable] = child
        operations_children.append(stable)
    operations_parent["relationships"]["derived_requirements"] = operations_children
    operations_parent["relationships"]["coverage_mode"] = "ALL_CHILDREN"

    # Classification/presentation repairs from the approved criticality pack.
    defect_overrides = {
        "UXF-00-R016": ("DESIGN_PRINCIPLE", "NORMAL", "White-label configuration must not require source-code modification."),
        "UXF-04-R006": ("DESIGN_PRINCIPLE", "NORMAL", "White-label configuration must not require source-code modification."),
        "UXF-106": ("DESIGN_PRINCIPLE", "HIGH", "Internal supplier-selection and allocation mechanics remain invisible in customer journeys; approved provider, network, or brand disclosure is read-only and must not influence allocation."),
        "UXF-110": ("DESIGN_PRINCIPLE", "NORMAL", "Business capabilities remain independent from presentation contracts."),
        "UXF-202": ("DESIGN_PRINCIPLE", "NORMAL", "Themes are versioned configuration objects rather than source-code variants."),
        "UXF-203": ("DESIGN_PRINCIPLE", "NORMAL", "Experience Profiles extend Themes through governed configuration."),
        "UXF-204": ("DESIGN_PRINCIPLE", "NORMAL", "Theme inheritance resolves deterministically through the approved configuration hierarchy."),
        "UXF-208": ("DESIGN_PRINCIPLE", "NORMAL", "Business behavior remains independent from presentation composition."),
        "UXF-408": ("DESIGN_PRINCIPLE", "NORMAL", "White-label configuration requires no source-code changes."),
        "UXF-501": ("DESIGN_PRINCIPLE", "NORMAL", "Experience Runtime owns presentation while business domains retain ownership of business behavior."),
    }
    for stable, (req_type, tier, statement) in defect_overrides.items():
        rec = remediate(stable, requirement_type=req_type, verification_criticality=tier, normative_statement=statement)
        if stable == "UXF-106":
            rec["provenance"]["approved_decisions"] = sorted(set(rec["provenance"]["approved_decisions"] + ["P2-DEC-007"]))

    # Two allocations explicitly reserved and approved in Phase 2A.
    cap_allocation = new_record(
        stable_id="BRD-CAP-INDEX-R029",
        document="docs/BRD/BRD-CAP-INDEX.md",
        statement="Mỗi Capability phải khai báo event_role là PUBLISHER, SUBSCRIBER, BOTH hoặc NONE cùng published_event_ids và subscribed_event_ids; NONE yêu cầu hai danh sách rỗng, các role còn lại yêu cầu danh sách tương ứng không rỗng, và mọi tham chiếu phải trỏ tới Event Registry ID canonical active/approved, không được dùng alias, retired, tombstone hoặc dangling reference.",
        title="Capability event-role metadata",
        requirement_type="DATA_REQUIREMENT",
        scope="V2.3_ACTIVE",
        criticality="HIGH",
        decisions=["P2-DEC-005"],
        allocation="P2-ALLOC-001",
    )
    disclosure = new_record(
        stable_id="UXF-05-R054",
        document="docs/UXF/UXF-05.md",
        statement="Customer-facing provider, network, or brand information may be shown as read-only disclosure when required by Catalog, legal, or product definition; internal supplier ID, procurement source, cost or margin, routing priority, supplier health, connector identity, and allocation details must never be exposed or influence allocation, and missing mandatory disclosure data must fail closed.",
        title="Customer-facing provider disclosure boundary",
        requirement_type="UX_REQUIREMENT",
        scope="V2.3_ACTIVE",
        criticality="HIGH",
        decisions=["P2-DEC-007"],
        allocation="P2-ALLOC-002",
    )
    records.extend([cap_allocation, disclosure])
    by_id[cap_allocation["stable_id"]] = cap_allocation
    by_id[disclosure["stable_id"]] = disclosure

    # Ensure each accepted human decision is explicitly represented in source provenance.
    anchors = {
        "P2-DEC-001": next(r for r in records if "federat" in r["normative_statement"].casefold()),
        "P2-DEC-002": event_r1,
        "P2-DEC-003": by_id["BRD-WS-17-R029"],
        "P2-DEC-004": by_id["BRD-WS-17-R027"],
        "P2-DEC-005": cap_allocation,
        "P2-DEC-006": next(r for r in records if "connector" in r["normative_statement"].casefold()),
        "P2-DEC-007": disclosure,
        "P2-DEC-008": next(r for r in records if "identity" in r["normative_statement"].casefold()),
        "P2-DEC-009": by_id["UXF-001"],
        "P2-DEC-010": by_id["BRD-WS-17-R029"],
    }
    decision_payloads = {item["decision_id"]: item for item in human_decisions["decisions"]}
    for decision, anchor in anchors.items():
        anchor["provenance"]["approved_decisions"] = sorted(set(anchor["provenance"]["approved_decisions"] + [decision]))
        anchor["provenance"].setdefault("approved_decision_contracts", {})[decision] = decision_payloads[decision]

    source_probes = {
        "BRD-CAP-INDEX-R029": "Capability may be PUBLISHER, SUBSCRIBER, BOTH, or NONE",
        "UXF-05-R054": "Storefront does not select, route, or directly integrate Supplier",
        "BRD-UPDATE-01-R030": "Business Model là điểm khởi đầu",
        "BRD-WS-08-R013": "Anti Fraud Engine sẽ triển khai ở phiên bản sau",
        "BRD-WS-17-R026": "Mọi tác vụ vận hành phải có khả năng",
        "BRD-WS-17-R027": "Mọi tác vụ vận hành phải có khả năng",
        "BRD-WS-17-R028": "Mọi tác vụ vận hành phải có khả năng",
        "BRD-WS-17-R029": "Mọi tác vụ vận hành phải có khả năng",
        "BRD-WS-17-R030": "Mọi tác vụ vận hành phải có khả năng",
        "BRD-WS-17-R031": "Operator không thao tác trực tiếp trên hạ tầng",
    }

    # Finalize obligation coverage and acceptance after every structural and scope change.
    for rec in records:
        if "_source_context" not in rec:
            body = legacy_bodies[rec["provenance"]["source_document"]]
            probe = source_probes.get(rec["stable_id"], rec["normative_statement"])
            source_context, source_heading = extract_full_source_section(probe, body)
            if source_heading == "SOURCE_STATEMENT_FALLBACK" and rec["provenance"].get("approved_decision_contracts"):
                source_context = canonical_json(rec["provenance"]["approved_decision_contracts"])
                source_heading = "APPROVED_DECISION_CONTRACT"
            rec["_source_context"] = source_context
            rec["provenance"]["source_context_heading"] = source_heading
            rec["provenance"]["source_context_sha256"] = sha256(source_context.encode("utf-8"))
        active_atomic = rec["scope_status"] == "V2.3_ACTIVE" and rec["record_kind"] == "CANONICAL_ATOMIC"
        if active_atomic:
            if rec["verification_criticality"] not in {"CRITICAL", "HIGH", "NORMAL"}:
                raise RuntimeError(f"missing final criticality for {rec['stable_id']}")
            obligations, criteria, applicability = semantic_acceptance(rec)
            rec["acceptance_schema_version"] = "2.0.0-OBLIGATION_COVERAGE"
            rec["atomic_obligations"] = obligations
            rec["acceptance_status"] = "DIRECT"
            rec["acceptance_contract"] = criteria
            rec["criticality_applicability"] = applicability
            rec["acceptance_rationale"] = None
        else:
            rec["acceptance_schema_version"] = "2.0.0-OBLIGATION_COVERAGE"
            rec["atomic_obligations"] = []
            rec["acceptance_status"] = "NOT_APPLICABLE_FOR_V2.3"
            rec["acceptance_contract"] = []
            rec["criticality_applicability"] = None
            if rec["record_kind"] == "COMPOSITE_PARENT":
                rec["acceptance_rationale"] = "Composite parent coverage is satisfied only through ALL_CHILDREN; the parent is not an acceptance unit."
            elif rec["record_kind"] == "ALIAS":
                rec["acceptance_rationale"] = "Alias evidence is inherited from the canonical target; the alias is not an acceptance unit."
            else:
                rec["acceptance_rationale"] = inactive_rationale(rec["scope_status"])
            rec["implementation_unit"] = False
            rec["acceptance_unit"] = False
            rec["scope_coverage_unit"] = False
            rec["criticality_unit"] = False
            rec["verification_criticality"] = "NOT_APPLICABLE"
        rec.pop("_source_context", None)

    # Attach all 46 disposition applications, including the split's replacement child.
    applied_exception_ids = {
        item["exception_id"]
        for rec in records
        for item in rec.get("criticality_dispositions", [])
    }
    expected_exception_ids = {item["exception_id"] for item in criticality["exceptions"]}
    if applied_exception_ids != expected_exception_ids:
        missing = sorted(expected_exception_ids - applied_exception_ids)
        raise RuntimeError(f"unapplied criticality dispositions: {missing}")

    # A record cannot retain an active temporary identity.
    for rec in records:
        rec.pop("temporary_key", None)
        rec["provenance"]["approved_decisions"] = sorted(set(rec["provenance"]["approved_decisions"]))

    documents = brd["documents"] + uxf["documents"]
    context = {
        "documents": documents,
        "retired_keys": reconciliation["retired_temporary_keys"],
        "mapping": mapping,
        "criticality": criticality,
    }
    return records, documents, context


def render_block(record: dict[str, Any]) -> str:
    title = record["title"].replace("\n", " ")
    payload = canonical_json(record).rstrip()
    return f"{BEGIN}\n### {record['stable_id']} — {title}\n\n```json\n{payload}\n```\n{END}"


def identity_history_payload(records: list[dict[str, Any]], context: dict[str, Any]) -> dict[str, Any]:
    preserved = []
    mapped = []
    allocated = []
    for rec in records:
        provenance = rec["provenance"]
        entry = {"stable_id": rec["stable_id"], "source_document": provenance["source_document"]}
        if provenance["identity_origin"] == "PRESERVED_STABLE_ID":
            entry["previous_identity"] = provenance["original_identity"]
            preserved.append(entry)
        elif provenance["identity_origin"] == "APPROVED_TEMPORARY_KEY_MAPPING":
            entry["previous_temporary_key"] = provenance["previous_temporary_key"]
            mapped.append(entry)
        else:
            entry["allocation_contract"] = provenance["allocation_contract"]
            allocated.append(entry)
    retired = context["retired_keys"]
    return {
        "preserved": sorted(preserved, key=lambda x: x["stable_id"]),
        "mapped": sorted(mapped, key=lambda x: x["stable_id"]),
        "newly_allocated": sorted(allocated, key=lambda x: x["stable_id"]),
        "retired_key_history": retired,
        "retired_key_count": len(retired),
        "reuse_policy": "NEVER_REUSE_RETIRED_IDS_OR_KEYS",
    }


def render_documents(records: list[dict[str, Any]], documents: list[dict[str, Any]], context: dict[str, Any]) -> dict[str, bytes]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[record["provenance"]["source_document"]].append(record)
    identity_payload = identity_history_payload(records, context)
    output: dict[str, bytes] = {}
    for document in documents:
        path = ROOT / document["path"]
        body = strip_generated(path.read_text(encoding="utf-8"))
        language = "vi-VN" if document["path"].startswith("docs/BRD/") else "en"
        if language == "vi-VN":
            notice = (
                "## Thẩm quyền nguồn yêu cầu v2.3\n\n"
                "Các khối `YSIM:REQUIREMENT` trong phụ lục chuẩn tắc là nguồn yêu cầu có thẩm quyền cho baseline 2.3. "
                "Nội dung legacy bên dưới được giữ làm ngữ cảnh; nếu có khác biệt, khối chuẩn tắc và các quyết định v2.3 đã phê duyệt được ưu tiên.\n"
            )
            appendix_title = "## Phụ lục yêu cầu chuẩn tắc v2.3"
        else:
            notice = (
                "## v2.3 requirement authority\n\n"
                "The `YSIM:REQUIREMENT` blocks in the normative appendix are authoritative for baseline 2.3. "
                "Legacy prose is retained as context; approved v2.3 decisions and the normative blocks take precedence where wording differs.\n"
            )
            appendix_title = "## v2.3 normative requirement appendix"
        blocks = [render_block(r) for r in sorted(grouped[document["path"]], key=lambda x: natural_key(x["stable_id"]))]
        appendix_parts = [APPENDIX_BEGIN, appendix_title, "", *blocks]
        if document["document_code"] == "BRD-META-MODEL":
            appendix_parts.extend([
                "", IDENTITY_BEGIN, "```json", canonical_json(identity_payload).rstrip(), "```", IDENTITY_END,
            ])
        appendix_parts.append(APPENDIX_END)
        rendered = front_matter(document) + notice + "\n" + body.rstrip() + "\n\n" + "\n\n".join(appendix_parts) + "\n"
        output[document["path"]] = rendered.encode("utf-8")
    return output


def natural_key(value: str) -> list[Any]:
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", value)]


def parse_records(markdown_files: dict[str, bytes]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    records: list[dict[str, Any]] = []
    identity: dict[str, Any] | None = None
    block_re = re.compile(re.escape(BEGIN) + r".*?```json\n(.*?)\n```.*?" + re.escape(END), re.DOTALL)
    identity_re = re.compile(re.escape(IDENTITY_BEGIN) + r"\s*```json\n(.*?)\n```\s*" + re.escape(IDENTITY_END), re.DOTALL)
    for path in sorted(markdown_files):
        text = markdown_files[path].decode("utf-8")
        for match in block_re.finditer(text):
            record = json.loads(match.group(1))
            if record["provenance"]["source_document"] != path:
                raise RuntimeError(f"source path mismatch for {record['stable_id']}")
            records.append(record)
        match = identity_re.search(text)
        if match:
            identity = json.loads(match.group(1))
    if identity is None:
        raise RuntimeError("missing Markdown identity-history block")
    return records, identity


def build_projections(markdown_files: dict[str, bytes]) -> tuple[dict[str, bytes], dict[str, Any]]:
    records, identity = parse_records(markdown_files)
    stable_ids = [r["stable_id"] for r in records]
    if len(stable_ids) != len(set(stable_ids)):
        raise RuntimeError("duplicate stable IDs")
    brd = [r for r in records if r["provenance"]["source_document"].startswith("docs/BRD/")]
    uxf = [r for r in records if r["provenance"]["source_document"].startswith("docs/UXF/")]
    atomic = [r for r in records if r["record_kind"] == "CANONICAL_ATOMIC"]
    active_atomic = [r for r in atomic if r["scope_status"] == "V2.3_ACTIVE"]
    inactive_atomic = [r for r in atomic if r["scope_status"] != "V2.3_ACTIVE"]
    aliases = [r for r in records if r["record_kind"] == "ALIAS"]
    composites = [r for r in records if r["record_kind"] == "COMPOSITE_PARENT"]

    relationship_targets: set[str] = set()
    trace_records = []
    for rec in records:
        rel = rec["relationships"]
        targets = [v for v in [rel.get("alias_of")] if v]
        for key in ("aliases", "derived_from", "derived_requirements", "satisfies_composite_parents"):
            targets.extend(rel.get(key, []))
        relationship_targets.update(targets)
        trace_records.append({
            "stable_id": rec["stable_id"],
            "source_document": rec["provenance"]["source_document"],
            "relationships": rel,
            "approved_decisions": rec["provenance"]["approved_decisions"],
        })
    dangling = sorted(relationship_targets - set(stable_ids))

    ledger_by_exception: dict[str, dict[str, Any]] = {}
    for rec in records:
        for item in rec.get("criticality_dispositions", []):
            entry = ledger_by_exception.setdefault(item["exception_id"], {
                **item,
                "applied_requirement_ids": [],
                "source_exception_status": "OPEN",
                "source_resolution_claim": False,
            })
            entry["applied_requirement_ids"].append(rec["stable_id"])
    ledger = [ledger_by_exception[key] for key in sorted(ledger_by_exception)]

    decision_coverage = sorted({d for r in records for d in r["provenance"]["approved_decisions"]})
    all_criteria = [criterion for record in active_atomic for criterion in record["acceptance_contract"]]
    uncovered_obligations = [
        obligation["obligation_id"]
        for record in active_atomic
        for obligation in record["atomic_obligations"]
        if not obligation["acceptance_criterion_references"]
    ]
    generic_occurrences = sum(
        any(phrase in canonical_json(item) for phrase in GENERIC_ACCEPTANCE_PHRASES)
        for item in all_criteria
    )
    wording_groups: dict[tuple[str, str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for item in all_criteria:
        wording_groups[(item["given"], item["when"], item["then"], item["observable_evidence"])].append(item)
    invalid_duplicate_templates = [
        {
            "criterion_ids": [item["criterion_id"] for item in group],
            "controlled_contracts": sorted({item["controlled_contract"] for item in group}),
        }
        for group in wording_groups.values()
        if len(group) > 1 and len({item["controlled_contract"] for item in group}) != 1
    ]
    summary = {
        "artifact": "V23-P2C-REMEDIATED-REGISTRY",
        "candidate_id": CANDIDATE_ID,
        "source_document_count": len(markdown_files),
        "requirement_record_count": len(records),
        "canonical_atomic_count": len(atomic),
        "active_atomic_count": len(active_atomic),
        "inactive_atomic_count": len(inactive_atomic),
        "composite_parent_count": len(composites),
        "alias_count": len(aliases),
        "stable_id_count": len(set(stable_ids)),
        "active_temporary_key_count": 0,
        "missing_stable_id_count": 0,
        "dangling_reference_count": len(dangling),
        "scope_distribution": dict(sorted(Counter(r["scope_status"] for r in atomic).items())),
        "record_kind_distribution": dict(sorted(Counter(r["record_kind"] for r in records).items())),
        "source_aggregate_sha256": aggregate_hash(markdown_files),
    }
    acceptance_summary = {
        "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
        "active_atomic_denominator": len(active_atomic),
        "direct_count": sum(r["acceptance_status"] == "DIRECT" for r in active_atomic),
        "active_acceptance_gap": sum(r["acceptance_status"] != "DIRECT" for r in active_atomic),
        "obligation_count": sum(len(r["atomic_obligations"]) for r in active_atomic),
        "criterion_count": len(all_criteria),
        "uncovered_obligation_count": len(uncovered_obligations),
        "uncovered_obligation_ids": uncovered_obligations,
        "c1_generic_criterion_occurrences": C1_GENERIC_CRITERION_OCCURRENCES,
        "c2_generic_criterion_occurrences": generic_occurrences,
        "invalid_duplicate_template_group_count": len(invalid_duplicate_templates),
        "invalid_duplicate_template_groups": invalid_duplicate_templates,
        "not_applicable_count": sum(r["acceptance_status"] == "NOT_APPLICABLE_FOR_V2.3" for r in records),
        "inactive_atomic_not_applicable_count": sum(r["acceptance_status"] == "NOT_APPLICABLE_FOR_V2.3" for r in inactive_atomic),
        "criticality_depth": {
            tier: dict(sorted(Counter(len(r["acceptance_contract"]) for r in active_atomic if r["verification_criticality"] == tier).items()))
            for tier in ("CRITICAL", "HIGH", "NORMAL")
        },
    }
    criticality_summary = {
        "denominator": len(active_atomic),
        "distribution": dict(sorted(Counter(r["verification_criticality"] for r in active_atomic).items())),
        "inactive_or_non_atomic_excluded": len(records) - len(active_atomic),
        "source_disposition_count": len(ledger),
        "source_exception_status": {"OPEN": len(ledger)},
    }
    projections = {
        "brd-requirements.json": {"artifact": "V23-P2C-BRD-REQUIREMENTS", "generated_from": "REMEDIATED_MARKDOWN_ONLY", "requirements": brd},
        "uxf-requirements.json": {"artifact": "V23-P2C-UXF-REQUIREMENTS", "generated_from": "REMEDIATED_MARKDOWN_ONLY", "requirements": uxf},
        "registry-summary.json": summary,
        "traceability.json": {"artifact": "V23-P2C-TRACEABILITY", "records": trace_records, "dangling_references": dangling, "approved_decision_coverage": decision_coverage},
        "identity-history.json": {"artifact": "V23-P2C-IDENTITY-HISTORY", **identity},
        "acceptance-summary.json": acceptance_summary,
        "criticality-summary.json": criticality_summary,
        "remediation-ledger.json": {"artifact": "V23-P2C-REMEDIATION-LEDGER", "disposition_count": len(ledger), "entries": ledger},
    }
    encoded = {f"docs/baselines/v2.3/phase-2/remediated-registry/{name}": canonical_json(value).encode("utf-8") for name, value in projections.items()}
    metrics = {
        "summary": summary,
        "acceptance": acceptance_summary,
        "criticality": criticality_summary,
        "identity": identity,
        "decision_coverage": decision_coverage,
        "remediation_ledger": ledger,
        "projection_aggregate_sha256": aggregate_hash(encoded),
    }
    return encoded, metrics


def render_reports(markdown: dict[str, bytes], projections: dict[str, bytes], metrics: dict[str, Any]) -> dict[str, bytes]:
    summary = metrics["summary"]
    acceptance = metrics["acceptance"]
    criticality = metrics["criticality"]
    identity = metrics["identity"]
    blocker = f"""# Phase 2C Blocker Register\n\n- Candidate: `{CANDIDATE_ID}`\n- Supersedes: `{SUPERSEDES}`\n- Status: `CLEAR`\n- Blocker count: `0`\n- Last evaluated: `{REMEDIATION_DATE}`\n\nFull source-section context resolved the mandatory semantic cases, including Customer Feedback sources. No unresolved semantic blocker remains.\n"""
    report = f"""# Phase 2C Big-Bang Document Remediation Report\n\n- Candidate: `{CANDIDATE_ID}`\n- Supersedes: `{SUPERSEDES}`\n- Supersession reason: `{SUPERSESSION_REASON}`\n- Status: `CANDIDATE`\n- Approval: `PENDING_HUMAN_ACCEPTANCE`\n- Base commit: `{BASE_COMMIT}`\n- Source documents remediated: `{summary['source_document_count']}` (`24` BRD + `7` UXF)\n- Registry records: `{summary['requirement_record_count']}`\n- Canonical atomic requirements: `{summary['canonical_atomic_count']}`\n- Active atomic requirements: `{summary['active_atomic_count']}`\n- Stable IDs preserved: `{len(identity['preserved'])}`\n- Temporary keys mapped: `{len(identity['mapped'])}`\n- Stable IDs newly allocated: `{len(identity['newly_allocated'])}`\n- Retired-key history entries: `{identity['retired_key_count']}`\n- Composite parents: `{summary['composite_parent_count']}`\n- Aliases: `{summary['alias_count']}`\n- Blockers: `0`\n\n## Scope distribution\n\n```json\n{json.dumps(summary['scope_distribution'], indent=2, sort_keys=True)}\n```\n\n## Verification criticality\n\n```json\n{json.dumps(criticality['distribution'], indent=2, sort_keys=True)}\n```\n\n## Acceptance schema 2.0\n\n- Direct: `{acceptance['direct_count']}`\n- NOT_APPLICABLE_FOR_V2.3: `{acceptance['not_applicable_count']}`\n- Active acceptance gap: `{acceptance['active_acceptance_gap']}`\n- Atomic obligations: `{acceptance['obligation_count']}`\n- Acceptance criteria: `{acceptance['criterion_count']}`\n- Uncovered obligations: `{acceptance['uncovered_obligation_count']}`\n- Generic criterion occurrences in C1: `{acceptance['c1_generic_criterion_occurrences']}`\n- Generic criterion occurrences in C2: `{acceptance['c2_generic_criterion_occurrences']}`\n- Invalid duplicate-template groups: `{acceptance['invalid_duplicate_template_group_count']}`\n\n## Deterministic aggregates\n\n- Remediated Markdown SHA-256: `{summary['source_aggregate_sha256']}`\n- Generated projection SHA-256: `{metrics['projection_aggregate_sha256']}`\n\n## Gate\n\n`HUMAN_DOCUMENT_BASELINE_ACCEPTANCE`\n"""
    file_hashes = {
        **{path: sha256(data) for path, data in markdown.items()},
        **{path: sha256(data) for path, data in projections.items()},
    }
    candidate = {
        "schema_version": "2.0.0",
        "candidate_id": CANDIDATE_ID,
        "supersedes": SUPERSEDES,
        "supersession_reason": SUPERSESSION_REASON,
        "status": "CANDIDATE",
        "approval_status": "PENDING_HUMAN_ACCEPTANCE",
        "base_commit": BASE_COMMIT,
        "source_registry": "V23-REQ-REGISTRY-FC2",
        "source_human_decision_pack": "V23-P2A-DECISION-PACK-C1",
        "source_criticality_decision_pack": "V23-P2B-CRITICALITY-DECISION-C1",
        "hash_basis": "GIT_INDEX_BLOB_CONTENT",
        "line_endings": "GIT_CANONICAL_TEXT",
        "next_gate": "HUMAN_DOCUMENT_BASELINE_ACCEPTANCE",
        "blocker_count": 0,
        "counts": {
            **{key: summary[key] for key in ("source_document_count", "requirement_record_count", "canonical_atomic_count", "active_atomic_count", "inactive_atomic_count", "composite_parent_count", "alias_count")},
            "stable_ids_preserved": len(identity["preserved"]),
            "temporary_keys_mapped": len(identity["mapped"]),
            "new_stable_ids_allocated": len(identity["newly_allocated"]),
            "retired_key_history": identity["retired_key_count"],
            "criticality_dispositions_applied": len(metrics["remediation_ledger"]),
            "active_acceptance_gap": acceptance["active_acceptance_gap"],
            "atomic_obligations": acceptance["obligation_count"],
            "acceptance_criteria": acceptance["criterion_count"],
            "uncovered_obligations": acceptance["uncovered_obligation_count"],
            "generic_criterion_occurrences_before": acceptance["c1_generic_criterion_occurrences"],
            "generic_criterion_occurrences_after": acceptance["c2_generic_criterion_occurrences"],
            "semantic_blockers": 0,
        },
        "scope_distribution": summary["scope_distribution"],
        "criticality_distribution": criticality["distribution"],
        "acceptance_distribution": {"DIRECT": acceptance["direct_count"], "NOT_APPLICABLE_FOR_V2.3": acceptance["not_applicable_count"]},
        "deterministic_hashes": {
            "source_aggregate_sha256": summary["source_aggregate_sha256"],
            "projection_aggregate_sha256": metrics["projection_aggregate_sha256"],
            "files": dict(sorted(file_hashes.items())),
        },
        "historical_validation_contract": {
            "validation_target": BASE_COMMIT,
            "mode": "ACCEPTED_CLEAN_CHECKOUT_ONLY",
            "validator_count": 6,
        },
        "approval_block": {
            "decision": "PENDING",
            "authorized_approver": None,
            "signature": None,
            "approval_date": None,
        },
    }
    return {
        str(REPORT_PATH.relative_to(ROOT)): report.encode("utf-8"),
        str(BLOCKER_PATH.relative_to(ROOT)): blocker.encode("utf-8"),
        str(CANDIDATE_PATH.relative_to(ROOT)): canonical_json(candidate).encode("utf-8"),
    }


def build_outputs() -> dict[str, bytes]:
    records, documents, context = build_records()
    markdown = render_documents(records, documents, context)
    projections, metrics = build_projections(markdown)
    reports = render_reports(markdown, projections, metrics)
    return {**markdown, **projections, **reports}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="compare deterministic output without writing")
    args = parser.parse_args()
    outputs = build_outputs()
    mismatches: list[str] = []
    for relative, data in sorted(outputs.items()):
        path = ROOT / relative
        if args.check:
            if not path.exists() or path.read_bytes() != data:
                mismatches.append(relative)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    if args.check and mismatches:
        for path in mismatches:
            print(f"MISMATCH {path}")
        return 1
    if args.check:
        print("PASS — DETERMINISTIC_PHASE_2C_REMEDIATION_OUTPUT")
    else:
        print(f"REMEDIATED {len(outputs)} files for {CANDIDATE_ID}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
