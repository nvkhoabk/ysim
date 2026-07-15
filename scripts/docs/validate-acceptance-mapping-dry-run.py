#!/usr/bin/env python3
"""Validate full-corpus hybrid acceptance mapping and rendered semantic audit."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PHASE2 = ROOT / "docs/baselines/v2.3/phase-2"
REGISTRY = PHASE2 / "remediated-registry"
MAPPING_PATH = PHASE2 / "acceptance-mapping-dry-run.json"
CATALOG_PATH = PHASE2 / "acceptance-profile-catalog.json"
SCHEMA_PATH = PHASE2 / "schemas/acceptance-mapping-dry-run.schema.json"
MANIFEST_PATH = PHASE2 / "acceptance-model-candidate-manifest.json"
GENERATOR = ROOT / "scripts/docs/generate-acceptance-model-candidate.py"
MECHANISMS = {"PROFILE_BINDING_HIGH_CONFIDENCE", "INLINE_CONTRACT_REQUIRED", "HUMAN_MAPPING_REVIEW", "INVALID_OR_BLOCKED"}
COMPLEX_TERMS = ("fraud", "risk engine", "payment", "thanh toán", "pricing", "promotion", "procurement", "allocation", "fulfillment", "refund", "reconciliation", "đối soát", "workflow", "state machine")
BANNED = (
    "works as expected", "is handled correctly", "appropriate error is returned",
    "requirement is satisfied", "verify the business rule", "system remains consistent",
    "todo", "tbd", "placeholder", "inferred_only",
)


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def load_source() -> dict[str, dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for name in ("brd-requirements.json", "uxf-requirements.json"):
        records.extend(json.loads((REGISTRY / name).read_text(encoding="utf-8"))["requirements"])
    return {r["stable_id"]: r for r in records if r["record_kind"] == "CANONICAL_ATOMIC" and r["scope_status"] == "V2.3_ACTIVE"}


def rendered(profile: dict[str, Any], bindings: dict[str, Any]) -> dict[str, str]:
    values = {key: ", ".join(value) if isinstance(value, list) else str(value) for key, value in bindings.items()}
    return {name: template.format(**values) for name, template in profile["oracle_templates"].items()}


def concrete(value: Any) -> bool:
    if value in (None, "", []): return False
    text = json.dumps(value, ensure_ascii=False).casefold()
    return not any(term in text for term in BANNED) and not re.search(r"\b(?:value|thing|something|generic|unknown)\b", text)


def validate_mapping(item: dict[str, Any], source: dict[str, dict[str, Any]], profiles: dict[str, dict[str, Any]]) -> None:
    sid = item["requirement_id"]
    require(sid in source, f"mapping references non-active or missing requirement: {sid}")
    record = source[sid]
    require(item["statement_fingerprint"] == hashlib.sha256(record["normative_statement"].encode()).hexdigest(), f"statement fingerprint mismatch: {sid}")
    require((item["requirement_type"], item["scope"], item["criticality"]) == (record["requirement_type"], "V2.3_ACTIVE", record["verification_criticality"]), f"source metadata mismatch: {sid}")
    require(item["proposed_mechanism"] in MECHANISMS, f"invalid mechanism: {sid}")
    require(item["rationale"].strip() and item["source_and_decision_provenance"]["source_document"] == record["provenance"]["source_document"], f"missing rationale/provenance: {sid}")
    mechanism = item["proposed_mechanism"]
    if mechanism == "PROFILE_BINDING_HIGH_CONFIDENCE":
        require(item["profile_id"] in profiles, f"unknown profile: {sid}")
        profile = profiles[item["profile_id"]]
        require(item["profile_version"] == profile["version"], f"profile version mismatch: {sid}")
        require(record["requirement_type"] in profile["supported_requirement_types"], f"incompatible profile type: {sid}")
        require(record["verification_criticality"] in profile["criticality_compatibility"], f"incompatible profile criticality: {sid}")
        required = {binding["name"] for binding in profile["required_bindings"]}
        require(set(item["concrete_bindings"]) == required, f"missing or unused concrete bindings: {sid}")
        require(all(concrete(value) for value in item["concrete_bindings"].values()), f"placeholder/generic binding: {sid}")
        expected = rendered(profile, item["concrete_bindings"])
        require(item["rendered_contract"] == expected, f"rendered contract mismatch: {sid}")
        statement_normal = re.sub(r"\W+", " ", item["normative_statement"].casefold()).strip()
        for oracle, text in expected.items():
            lower = text.casefold()
            require(not any(term in lower for term in BANNED), f"generic rendered oracle: {sid}/{oracle}")
            require("{" not in text, f"unmaterialized oracle binding: {sid}/{oracle}")
            require(any(str(value).casefold() in lower for value in item["concrete_bindings"].values() if not isinstance(value, list)) or any(str(v).casefold() in lower for value in item["concrete_bindings"].values() if isinstance(value, list) for v in value), f"oracle does not reference concrete binding: {sid}/{oracle}")
            oracle_normal = re.sub(r"\W+", " ", lower).strip()
            require(statement_normal != oracle_normal, f"tautological oracle repeats statement: {sid}/{oracle}")
        require(not any(term in item["normative_statement"].casefold() for term in COMPLEX_TERMS), f"complex requirement forced into simple profile: {sid}")
        require(not item["semantic_risks"] and item["confidence"] == "HIGH", f"high-confidence profile carries unresolved risk: {sid}")
    elif mechanism == "INLINE_CONTRACT_REQUIRED":
        require(item["profile_id"] is None and item["inline_category"], f"inline routing metadata missing: {sid}")
        outline = item["inline_authoring_contract"]
        required_fields = {"obligations","preconditions","action_trigger","expected_observable_outcomes","prohibited_outcomes","negative_cases","boundary_failure_cases","evidence","traceability","authoring_status"}
        require(set(outline) == required_fields and outline["obligations"], f"incomplete inline authoring contract: {sid}")
        require(outline["authoring_status"] == "REQUIRED_AFTER_ACCEPTANCE_MODEL_APPROVAL", f"inline authoring improperly claimed complete: {sid}")
        require(item["rendered_contract"] is None, f"dry run fabricated inline contract: {sid}")
    elif mechanism == "HUMAN_MAPPING_REVIEW":
        require(item["profile_id"] is None and item["rendered_contract"] is None, f"review record contains fabricated contract: {sid}")
        require(item["review_reason"] and item["semantic_risks"], f"review reason/risk missing: {sid}")
        require(item["confidence"] == "UNRESOLVED", f"review record confidence mismatch: {sid}")
    else:
        require(item["review_reason"] and item["semantic_risks"], f"blocked record lacks reason: {sid}")


def validate_identical_contracts(mappings: list[dict[str, Any]]) -> None:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in mappings:
        if item["rendered_contract"]:
            key = json.dumps(item["rendered_contract"], ensure_ascii=False, sort_keys=True)
            groups[key].append(item)
    for items in groups.values():
        fingerprints = {item["statement_fingerprint"] for item in items}
        require(len(items) == 1 or len(fingerprints) == 1, "identical rendered contracts used for semantically different requirements: " + ", ".join(i["requirement_id"] for i in items))


def validate_sample(artifact: dict[str, Any], mappings: list[dict[str, Any]]) -> None:
    sample = artifact["stratified_semantic_sample"]
    sample_ids = {item["requirement_id"] for item in sample}
    by_id = {item["requirement_id"]: item for item in mappings}
    profile_counts = Counter(item["profile_id"] for item in mappings if item["profile_id"])
    for profile_id, count in profile_counts.items():
        sampled = sum(1 for sid in sample_ids if by_id[sid]["profile_id"] == profile_id)
        require(sampled >= min(2, count), f"sample under-covers profile: {profile_id}")
        if count < 5: require(sampled == count, f"sample omits low-volume profile mapping: {profile_id}")
    for tier, minimum in (("CRITICAL",10),("HIGH",10),("NORMAL",5)):
        require(sum(1 for sid in sample_ids if by_id[sid]["criticality"] == tier) >= minimum, f"sample under-covers {tier}")
    all_categories = {item["inline_category"] for item in mappings if item["inline_category"]}
    sample_categories = {by_id[sid]["inline_category"] for sid in sample_ids if by_id[sid]["inline_category"]}
    require(all_categories <= sample_categories, "sample omits inline category")
    risk_ids = {item["requirement_id"] for item in mappings if item["semantic_risks"]}
    require(risk_ids <= sample_ids, "sample omits classifier semantic risk")
    for item in sample:
        source = by_id[item["requirement_id"]]
        require(item["rendered_contract"] == source["rendered_contract"], f"sample rendered contract mismatch: {item['requirement_id']}")
        require(item["sample_audit_result"] == "PASS", f"semantic sample failure: {item['requirement_id']}")
    require(artifact["sample_result"] == "PASS", "stratified semantic sample did not pass")


def validate_manifest(artifact: dict[str, Any]) -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    require(manifest["candidate_id"] == "V23-P2C-ACCEPTANCE-MODEL-C1", "candidate identity mismatch")
    require(manifest["status"] == "CANDIDATE" and manifest["approval_status"] == "PENDING_HUMAN_APPROVAL", "candidate state mismatch")
    require(manifest["next_gate"] == "HUMAN_ACCEPTANCE_MODEL_APPROVAL", "candidate gate mismatch")
    require(manifest["final_document_baseline"] is False and manifest["yadf_authorization"] is False and manifest["source_documents_regenerated"] is False, "candidate overclaims authority")
    require(manifest["mapping_summary"] == artifact["summary"], "manifest mapping summary mismatch")
    require(manifest["stratified_sample_result"] == "PASS", "manifest sample is not pass")
    require(manifest["approval_block"] == {"decision":"PENDING","approver":None,"signature":None,"date":None,"revision":None}, "approval block is not wholly pending")


def main() -> int:
    try:
        artifact = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
        source = load_source()
        require(schema["$schema"] == "https://json-schema.org/draft/2020-12/schema", "mapping schema draft mismatch")
        require(all(key in artifact for key in schema["required"]), "mapping JSON/schema shape mismatch")
        require(artifact["candidate_id"] == "V23-P2C-ACCEPTANCE-MODEL-C1" and artifact["source_denominator"] == 1076, "mapping candidate identity/denominator mismatch")
        mappings = artifact["mappings"]
        require(len(source) == len(mappings) == 1076, "mapping denominator mismatch")
        ids = [item["requirement_id"] for item in mappings]
        require(len(ids) == len(set(ids)) and set(ids) == set(source), "mapping coverage is not exhaustive/disjoint")
        profiles = {profile["profile_id"]: profile for profile in catalog["profiles"]}
        for item in mappings: validate_mapping(item, source, profiles)
        counts = Counter(item["proposed_mechanism"] for item in mappings)
        require(artifact["summary"]["disposition_counts"] == {key: counts.get(key,0) for key in ("PROFILE_BINDING_HIGH_CONFIDENCE","INLINE_CONTRACT_REQUIRED","HUMAN_MAPPING_REVIEW","INVALID_OR_BLOCKED")}, "disposition accounting mismatch")
        require(counts["INVALID_OR_BLOCKED"] == 0, "invalid/blocked mappings remain")
        validate_identical_contracts(mappings)
        validate_sample(artifact, mappings)
        validate_manifest(artifact)
        generated = subprocess.run([sys.executable, str(GENERATOR), "--check"], cwd=ROOT, text=True, capture_output=True, check=False)
        require(generated.returncode == 0, f"dry-run generation is not deterministic: {generated.stdout}{generated.stderr}")
    except (ValidationError, KeyError, ValueError, json.JSONDecodeError) as error:
        print(f"FAIL — {error}", file=sys.stderr)
        return 1
    print("PASS — VALID_ACCEPTANCE_MAPPING_DRY_RUN_CANDIDATE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
