#!/usr/bin/env python3
"""Validate rejected-C5 false-pass regression fixtures."""

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3/phase-2"
REF = "refs/ysim-backups/v2.3/phase-2c-document-baseline-c5-generic-rendering-rejected^2"
REGISTRY = "docs/baselines/v2.3/phase-2/phase-2c-document-baseline-c5-registry.json"


def main() -> int:
    report = json.loads((BASE / "semantic-acceptance-renderer-c1-false-pass-regressions.json").read_text())
    raw = subprocess.run(["git", "show", f"{REF}:{REGISTRY}"], cwd=ROOT, check=True, stdout=subprocess.PIPE).stdout
    rejected = {r["stable_id"]: r["acceptance_contract"] for r in json.loads(raw)["requirements"]}
    if report["count"] != 35 or len(report["results"]) != 35:
        raise SystemExit("INVALID_FALSE_PASS_REGRESSION_POPULATION")
    required = {"BRD-BO-INDEX-R004", "BD-02-001", "BD-03-012", "UXF-05-R056", "BD-04-001"}
    ids = {item["requirement_id"] for item in report["results"]}
    if not required <= ids:
        raise SystemExit("MISSING_MANDATORY_FALSE_PASS_REGRESSION")
    for item in report["results"]:
        old = rejected[item["requirement_id"]]
        expected_excerpt = {
            "positive_oracle": old.get("positive_oracle"),
            "negative_oracle": old.get("negative_oracle"),
            "boundary_oracle": old.get("boundary_oracle"),
            "required_evidence": old.get("required_evidence"),
            "procedure_action": (old.get("human_verification_procedure") or {}).get("exact_action"),
        }
        if item["rejected_c5_excerpt"] != expected_excerpt:
            raise SystemExit(f"REJECTED_C5_EXCERPT_NOT_INDEPENDENT {item['requirement_id']}")
        if item["rejected_c5_result"] != "FAIL_SEMANTICALLY_GENERIC":
            raise SystemExit(f"REJECTED_C5_FALSE_PASS_NOT_DETECTED {item['requirement_id']}")
        if item["c1_result"] != "PASS_OBLIGATION_SPECIFIC" or not all(item[key] for key in ("semantic_obligation_visible", "concrete_negative", "distinct_boundary", "obligation_specific_evidence")):
            raise SystemExit(f"CORRECTED_RENDERING_NOT_SPECIFIC {item['requirement_id']}")
    print("VALID_SEMANTIC_ACCEPTANCE_RENDERER_C1_FALSE_PASS_REGRESSIONS 35/35")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
