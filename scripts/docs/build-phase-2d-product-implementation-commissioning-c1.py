#!/usr/bin/env python3
"""Deterministically reproduce the commissioning-contract payload identity."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FILES = [
    "docs/baselines/v2.3/phase-2d/PRODUCT_IMPLEMENTATION_COMMISSIONING_C1.md",
    "docs/baselines/v2.3/phase-2d/PRODUCT_IMPLEMENTATION_COMMISSIONING_C1_HUMAN_APPROVAL_PACK.md",
    "docs/baselines/v2.3/phase-2d/product-implementation-commissioning-c1-evidence-plan.json",
    "docs/baselines/v2.3/phase-2d/product-implementation-commissioning-c1-execution-contract.json",
    "docs/baselines/v2.3/phase-2d/product-implementation-commissioning-c1-path-policy.json",
    "docs/baselines/v2.3/phase-2d/product-implementation-commissioning-c1-technology-decisions.json",
    "docs/baselines/v2.3/phase-2d/product-implementation-commissioning-c1-validation-matrix.json",
]


def canonical_json_bytes(path: Path) -> bytes:
    value = json.loads(path.read_text(encoding="utf-8"))
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def reproduce() -> dict[str, object]:
    aggregate = hashlib.sha256()
    hashes: dict[str, str] = {}
    for relative in FILES:
        path = ROOT / relative
        data = canonical_json_bytes(path) if path.suffix == ".json" else path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        hashes[relative] = digest
        aggregate.update(relative.encode())
        aggregate.update(b"\0")
        aggregate.update(data)
    return {
        "candidate_id": "V23-P2D-PRODUCT-IMPLEMENTATION-COMMISSIONING-C1",
        "file_sha256": hashes,
        "generated_payload_aggregate_sha256": aggregate.hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.dumps(reproduce(), ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    if args.output:
        args.output.write_text(data, encoding="utf-8", newline="\n")
    else:
        print(data, end="")


if __name__ == "__main__":
    main()
