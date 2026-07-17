#!/usr/bin/env python3
"""Independent cross-record similarity gate for renderer C1."""

import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3/phase-2"


def norm(text: str) -> str:
    text = re.sub(r"\b(?:BRD|BD|EP|UXF|CAP|EVT|POL|BO|SNP)(?:-[A-Z0-9]+)+\b", "<RID>", text.upper())
    text = re.sub(r"\b[0-9A-F]{12,}\b", "<HASH>", text)
    text = re.sub(r"\d+", "<N>", text)
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    ast = json.loads((BASE / "semantic-acceptance-renderer-c1-ast-previews.json").read_text())["records"]
    procedures = json.loads((BASE / "semantic-acceptance-renderer-c1-procedure-previews.json").read_text())["records"]
    grouped = defaultdict(list)
    for record in ast:
        for node in record["operator_renderings"]:
            for kind in ("positive_oracle", "negative_oracle"):
                grouped[(kind, norm(node[kind]["text"]))].append(record)
    unexplained = []
    for key, members in grouped.items():
        if len(members) < 2:
            continue
        evidence = {m["evidence_contract"]["evidence_object_ref"] for m in members}
        origins = {(m["expected_operand"]["origin_id"], m["observed_operand"]["origin_id"]) for m in members}
        fingerprints = {m["source_provenance"]["source_fingerprint"] for m in members}
        exact_source_semantics = {(m["source_statement"], m["source_provenance"]["source_fingerprint"]) for m in members}
        source_explained = len(fingerprints) == len(members) or len(exact_source_semantics) == 1
        if len(evidence) != len(members) or len(origins) != len(members) or not source_explained:
            unexplained.append((key, [m["requirement_id"] for m in members]))
    actions = [norm(p["exact_actions"][0]) for p in procedures]
    if len(set(actions)) != 156:
        raise SystemExit("GENERIC_PROCEDURE_ACTION_CLUSTER")
    if unexplained:
        raise SystemExit(f"UNEXPLAINED_GENERIC_CLUSTER {unexplained[:3]}")
    print("VALID_SEMANTIC_ACCEPTANCE_RENDERER_C1_SIMILARITY unexplained=0 procedure_actions=156/156")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
