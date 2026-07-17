#!/usr/bin/env python3
"""Independent structural and semantic audit for renderer C1.

This module intentionally does not import the builder or renderer.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3/phase-2"
REF = "refs/ysim-backups/v2.3/phase-2c-document-baseline-c5-generic-rendering-rejected^2"
REGISTRY = "docs/baselines/v2.3/phase-2/phase-2c-document-baseline-c5-registry.json"
BANNED = (
    "does not conform", "violates the obligation", "mutation fails",
    "operator returns false", "boundary input", "adjacent case",
    "near-valid value", "the requirement is not satisfied",
    "evidence demonstrates conformance", "evaluate the requirement",
    "verify conformance", "inspect applicable evidence",
    "Authorized Phase 2C semantic reviewer", "YSIM.C5.",
    "SEMANTIC_IDENTIFIER", "NO_EXPLICIT_", "EXPECTED_OUTCOME",
)


def load(name: str) -> dict[str, Any]:
    return json.loads((BASE / name).read_text())


def canonical(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def git_registry() -> dict[str, Any]:
    raw = subprocess.run(["git", "show", f"{REF}:{REGISTRY}"], cwd=ROOT, check=True, stdout=subprocess.PIPE).stdout
    return json.loads(raw)


def text_values(value: Any):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from text_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from text_values(child)


def validate_ast(records: list[dict[str, Any]], source: dict[str, dict[str, Any]]) -> Counter:
    results = Counter()
    require(len(records) == 910, "AST population must be 910")
    for record in records:
        rid = record["requirement_id"]
        require(rid in source, f"unknown AST requirement {rid}")
        require(record["source_statement"] == source[rid]["normative_statement"].rstrip(".") or record["source_statement"] == source[rid]["normative_statement"], f"source statement mismatch {rid}")
        subject = record["bound_subject"]["display_value"]
        expected = record["expected_operand"]["display_value"]
        require(subject and expected, f"missing concrete operand {rid}")
        require(expected.strip(" .") != record["source_statement"].strip(" ."), f"whole statement used as expected binding {rid}")
        require(record["expected_operand"]["origin_id"] != record["observed_operand"]["origin_id"], f"same origin {rid}")
        require(record["expected_operand"]["resolver_id"].startswith("RESOLVE."), f"missing expected resolver {rid}")
        require(record["observed_operand"]["resolver_id"].startswith("OBSERVE."), f"missing observed resolver {rid}")
        evidence = record["evidence_contract"]
        require(len(evidence["field_ids"]) >= 4 and len(evidence["resolver_ids"]) >= 2, f"incomplete evidence {rid}")
        require(evidence["expected_origin_id"] != evidence["observed_origin_id"], f"evidence origin collision {rid}")
        require(record["runtime_status"] == "RUNTIME_ADAPTER_PENDING", f"runtime claim {rid}")
        for rendered in record["operator_renderings"]:
            for key in ("positive_oracle", "negative_oracle"):
                text = rendered[key]["text"]
                require(subject in text and expected in text, f"{key} does not consume subject/expected {rid} {rendered['operator_id']}")
                require(not any(token.lower() in text.lower() for token in BANNED), f"banned generic text {rid}: {text}")
            boundary = rendered["boundary_oracle"]
            require(boundary["left"] != boundary["right"], f"identical boundary {rid}")
            require(subject in boundary["left"] and subject in boundary["right"] and expected in boundary["left"] and expected in boundary["right"], f"boundary binding omission {rid}")
            results[rendered["operator_id"]] += 1
        require(set(record["critical_bindings_consumed"]) == {"subject", "expected_operand", "observed_operand", "trigger_or_scope", "evidence_contract"}, f"unconsumed bindings {rid}")
        require(record["inference"] is False, f"inference {rid}")
    return results


def validate_procedures(records: list[dict[str, Any]], source: dict[str, dict[str, Any]]) -> Counter:
    actors = Counter()
    require(len(records) == 156, "procedure population must be 156")
    action_texts = []
    for procedure in records:
        rid = procedure["requirement_id"]
        require(rid in source, f"unknown procedure {rid}")
        actor = procedure["authoritative_actor"]
        actors[actor] += 1
        require(actor and "reviewer" not in actor.lower(), f"generic actor {rid}: {actor}")
        provenance = procedure["actor_provenance"]
        require(provenance["basis"] and provenance["source_document"] == source[rid]["provenance"]["source_document"], f"actor provenance {rid}")
        require(provenance["inference"] is False, f"actor inference {rid}")
        require(procedure["authorization"] and procedure["prerequisites"] and procedure["concrete_setup_data"], f"procedure setup {rid}")
        require(len(procedure["exact_actions"]) >= 1, f"missing action {rid}")
        action = " ".join(procedure["exact_actions"])
        action_texts.append(action)
        require(not any(token.lower() in action.lower() for token in BANNED), f"generic procedure action {rid}")
        require(procedure["concrete_setup_data"]["subject"] in action or procedure["concrete_setup_data"]["source_required_outcome"] in action, f"action loses obligation {rid}")
        require(procedure["expected_result"] != procedure["prohibited_result"], f"tautological result {rid}")
        boundary = procedure["boundary_case"]
        require(boundary["left"] != boundary["right"] and boundary["distinction"], f"invalid boundary {rid}")
        evidence = procedure["required_evidence"]
        require(evidence["evidence_object_ref"] and len(evidence["field_ids"]) >= 4 and evidence["correlation_id_required"], f"procedure evidence {rid}")
        require(procedure["failure_handling"] and procedure["cleanup_reset"], f"procedure failure/cleanup {rid}")
        require(procedure["runtime_status"] == "HUMAN_VERIFICATION_REQUIRED" and procedure["inference"] is False, f"procedure claim {rid}")
    require(len(set(action_texts)) == 156, "procedure actions are not record-specific")
    return actors


def validate_decisions(records: list[dict[str, Any]]) -> Counter:
    operators = Counter()
    require(len(records) == 27, "decision population must be 27")
    require(len({r["decision_id"] for r in records}) == 27, "duplicate decisions")
    for record in records:
        require(record["approved_obligations"], f"missing obligations {record['decision_id']}")
        target = "; ".join(x["text"] for x in record["approved_obligations"])
        require(target in record["positive_oracle"] and target in record["negative_oracle"], f"decision obligation not visible {record['decision_id']}")
        require(record["positive_oracle"] != record["negative_oracle"], f"decision tautology {record['decision_id']}")
        require(record["boundary_oracle"]["sides"], f"decision boundary {record['decision_id']}")
        require(record["expected_resolver_ids"] and record["observed_resolver_ids"] and record["evidence_fields"], f"decision evidence {record['decision_id']}")
        require(set(record["expected_resolver_ids"]).isdisjoint(record["observed_resolver_ids"]), f"decision same resolver {record['decision_id']}")
        require(record["runtime_status"] == "RUNTIME_ADAPTER_PENDING" and record["inference"] is False, f"decision runtime/inference {record['decision_id']}")
        operators.update(record["operator_composition"])
    mandatory = {r["decision_id"]: r for r in records}
    checks = {
        "P2C-SC-C1-DEC-001": ("Supplier", "Master", "Sales", "Storefront"),
        "P2C-SC-C1-DEC-002": ("more than one Purchase Order", "Sales Order"),
        "P2C-SC-C1-DEC-003": ("only after Delivery succeeds", "prohibited"),
        "P2C-SC-C1-DEC-004": ("Security", "event"),
        "P2C-SC-C1-DEC-007": ("QR Code", "ICCID", "Current Owner", "Inventory Status"),
        "P2C-SC-C1-DEC-011": ("Dashboard", "Workspace", "Admin Portal", "Organization Portal", "Customer Portal"),
        "P2C-SC-C1-DEC-013": ("addressable", "not overwritten"),
        "P2C-SC-C1-DEC-016": ("recovery", "reconciled", "invariants"),
        "P2C-SC-C1-DEC-018": ("Dashboard", "drill-down", "permission"),
        "P2C-SC-C1-DEC-024": ("WCAG 2.2 AA", "Themes"),
        "P2C-SC-C1-DEC-025": ("WCAG 2.2 AA", "mandatory"),
    }
    for decision_id, terms in checks.items():
        text = json.dumps(mandatory[decision_id], ensure_ascii=False)
        require(all(term.lower() in text.lower() for term in terms), f"mandatory decision semantics {decision_id}")
    return operators


def validate_reference(records: list[dict[str, Any]], source: dict[str, dict[str, Any]]) -> None:
    require(len(records) == 59, "reference population must be 59")
    for item in records:
        rid = item["requirement_id"]
        require(rid in source, f"unknown reference {rid}")
        require(item["contract_sha256"] == sha(item["acceptance_contract"]), f"reference hash {rid}")
        require(item["acceptance_contract"] == source[rid]["acceptance_contract"], f"reference changed {rid}")


def validate_manifest() -> None:
    manifest = load("semantic-acceptance-renderer-c1-manifest.json")
    require(manifest["candidate_id"] == "V23-P2C-SEMANTIC-ACCEPTANCE-RENDERER-C1", "candidate id")
    require(manifest["status"] == "CANDIDATE" and manifest["approval_status"] == "PENDING_HUMAN_APPROVAL", "candidate state")
    require(manifest["next_gate"] == "HUMAN_PHASE_2C_SEMANTIC_ACCEPTANCE_RENDERER_C1_APPROVAL", "next gate")
    require(manifest["counts"] == {"active": 1152, "renderer_correction": 1093, "operator_rendered": 937, "profile_archetype_unique": 910, "procedures": 156, "approved_decisions": 27, "reference_good": 59}, "manifest counts")
    for path, digest in manifest["per_file_sha256_excluding_manifest"].items():
        require(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, f"manifest file hash {path}")
    aggregate = sha([{"path": path, "sha256": digest} for path, digest in sorted(manifest["per_file_sha256_excluding_manifest"].items())])
    require(aggregate == manifest["generated_payload_aggregate_sha256"], "generated aggregate")


def main() -> int:
    registry = git_registry()
    source = {r["stable_id"]: r for r in registry["requirements"]}
    ast = load("semantic-acceptance-renderer-c1-ast-previews.json")["records"]
    procedures = load("semantic-acceptance-renderer-c1-procedure-previews.json")["records"]
    decisions = load("semantic-acceptance-renderer-c1-decision-previews.json")["records"]
    references = load("semantic-acceptance-renderer-c1-reference-good-contracts.json")["records"]
    ast_ops = validate_ast(ast, source)
    actors = validate_procedures(procedures, source)
    decision_ops = validate_decisions(decisions)
    validate_reference(references, source)
    schemas = load("semantic-acceptance-renderer-c1-operator-schemas.json")
    used = set(ast_ops) | set(decision_ops)
    require(set(schemas["operators"]) == used, "operator registry coverage")
    require(all(len(schema["adversarial_examples"]) == 5 for schema in schemas["operators"].values()), "operator adversarial coverage")
    generic = load("semantic-acceptance-renderer-c1-generic-equivalence.json")
    require(generic["unexplained_generic_clusters"] == 0, "unexplained generic cluster")
    require(generic["generic_actor_without_provenance"] == 0 and generic["generated_procedure_actions"] == 0, "generic procedure")
    regression = load("semantic-acceptance-renderer-c1-false-pass-regressions.json")
    require(regression["count"] == 35 and all(x["rejected_c5_result"].startswith("FAIL") and x["c1_result"].startswith("PASS") for x in regression["results"]), "false-pass regressions")
    audit = load("semantic-acceptance-renderer-c1-semantic-audit.json")
    require(all(value in (0, "937/937", "156/156", "59/59") for value in audit["results"].values()), "audit result")
    validate_manifest()
    print(f"VALID_PHASE_2C_SEMANTIC_ACCEPTANCE_RENDERER_C1 operators={len(used)} ast_nodes={sum(ast_ops.values())} actors={len(actors)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
