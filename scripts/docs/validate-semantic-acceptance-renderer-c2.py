#!/usr/bin/env python3
"""Validate Renderer C2 inventory, hash locks, scope and accounting."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3/phase-2"


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def comparison_failures(value, path=""):
    failures = []
    if isinstance(value, dict):
        if isinstance(value.get("actual_set"), dict):
            actual = value["actual_set"]
            for expected_name in ("expected_set", "required_members", "prohibited_members"):
                expected = value.get(expected_name)
                if not isinstance(expected, dict):
                    continue
                ao = actual.get("origin", {}).get("origin_id")
                eo = expected.get("origin", {}).get("origin_id")
                ar = actual.get("resolver_contract", {}).get("resolver_id")
                er = expected.get("resolver_contract", {}).get("resolver_id")
                if not ao or not eo or ao == eo:
                    failures.append(f"{path}: non-independent origins")
                if not ar or not er or ar == er:
                    failures.append(f"{path}: non-independent resolvers")
        for key, item in value.items():
            failures.extend(comparison_failures(item, f"{path}/{key}"))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            failures.extend(comparison_failures(item, f"{path}/{index}"))
    return failures


def main() -> int:
    manifest = json.loads((BASE / "semantic-acceptance-renderer-c2-manifest.json").read_text())
    reference = json.loads((BASE / "semantic-acceptance-renderer-c2-reference-good-contracts.json").read_text())
    supersession = json.loads((BASE / "semantic-acceptance-renderer-c2-contract-supersession.json").read_text())
    audit = json.loads((BASE / "semantic-acceptance-renderer-c2-semantic-audit.json").read_text())
    c1 = json.loads((BASE / "semantic-acceptance-renderer-c1-reference-good-contracts.json").read_text())
    c1_ast = json.loads((BASE / "semantic-acceptance-renderer-c1-ast-previews.json").read_text())["records"]
    c1_dec = json.loads((BASE / "semantic-acceptance-renderer-c1-decision-previews.json").read_text())["records"]
    c1_proc = json.loads((BASE / "semantic-acceptance-renderer-c1-procedure-previews.json").read_text())["records"]
    if manifest["candidate_id"] != "V23-P2C-SEMANTIC-ACCEPTANCE-RENDERER-C2" or manifest["status"] != "CANDIDATE" or manifest["approval_status"] != "PENDING_HUMAN_APPROVAL":
        raise SystemExit("candidate lifecycle mismatch")
    if (reference["count"], reference["unchanged_count"], reference["superseded_count"]) != (59, 48, 11):
        raise SystemExit("custom population mismatch")
    if supersession["record_count"] != 11 or len(supersession["records"]) != 11:
        raise SystemExit("supersession count mismatch")
    old = {r["requirement_id"]: r for r in c1["records"]}
    changed = 0
    for row in reference["records"]:
        rid = row["requirement_id"]
        digest = sha(canonical(row["acceptance_contract"]))
        if digest != row["contract_sha256"]:
            raise SystemExit(f"contract hash mismatch {rid}")
        if digest != old[rid]["contract_sha256"]:
            changed += 1
    if changed != 11:
        raise SystemExit(f"changed contract count {changed}")
    corrected_ids = {row["requirement_id"] for row in supersession["records"]}
    for row in supersession["records"]:
        if any(not item["path"].endswith("/origin/origin_id") for item in row["changed_paths"]):
            raise SystemExit(f"non-origin correction {row['requirement_id']}")
        for item in row["changed_paths"]:
            upper = item["new"].upper()
            if any(token in upper for token in ("SEMANTIC_IDENTIFIER", "EXPECTED_SET", "ACTUAL_SET", "YSIM.C5.", "YSIM.C6.")):
                raise SystemExit(f"opaque replacement {row['requirement_id']}")
        for item in row["normalizations"]:
            if not all(item.get(key) for key in ("corrected_identifier", "semantic_type", "namespace", "authority", "resolver", "origin", "provenance")):
                raise SystemExit(f"incomplete normalization {row['requirement_id']}")
            if item["provenance"].get("inference") is not False:
                raise SystemExit(f"inferred normalization {row['requirement_id']}")
    by_new = {row["requirement_id"]: row for row in reference["records"]}
    independence = []
    for rid in corrected_ids:
        independence.extend(f"{rid}{failure}" for failure in comparison_failures(by_new[rid]["acceptance_contract"]))
    if independence:
        raise SystemExit("\n".join(independence))
    expected = {"ast_operator_aware_pass": "937/937", "human_procedures_pass": "156/156", "typed_custom_pass": "59/59"}
    if any(audit["results"].get(k) != v for k, v in expected.items()):
        raise SystemExit("dry-run population failure")
    zeros = ["lost_obligations", "unsupported_obligations", "opaque_identifiers", "schema_derived_identifiers", "whole_statement_identifiers", "same_origin_violations", "missing_resolvers", "missing_evidence_contracts", "invalid_or_blocked", "unexplained_generic_similarity_clusters"]
    if any(audit["results"].get(k) != 0 for k in zeros):
        raise SystemExit("semantic audit nonzero")
    expected_ast_locks = [{"requirement_id": r["requirement_id"], "sha256": sha(canonical(r))} for r in c1_ast + c1_dec]
    expected_proc_locks = [{"requirement_id": r["requirement_id"], "sha256": sha(canonical(r))} for r in c1_proc]
    if audit["hash_locks"]["ast_and_decision"] != expected_ast_locks:
        raise SystemExit("937 AST/decision byte locks differ from C1")
    if audit["hash_locks"]["procedures"] != expected_proc_locks:
        raise SystemExit("156 procedure byte locks differ from C1")
    for path, digest in manifest["per_file_sha256_excluding_manifest"].items():
        if sha((ROOT / path).read_bytes()) != digest:
            raise SystemExit(f"file hash mismatch {path}")
    if len(manifest["exact_inventory"]) != 12:
        raise SystemExit("candidate inventory != 12")
    if subprocess.run(["git", "diff", "--name-only", "--", "docs/BRD", "docs/UXF"], cwd=ROOT, stdout=subprocess.PIPE, check=True).stdout:
        raise SystemExit("BRD/UXF changed")
    print("VALID_SEMANTIC_ACCEPTANCE_RENDERER_C2 1152/1152")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
