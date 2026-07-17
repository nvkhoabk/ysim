#!/usr/bin/env python3
"""Unit tests for the commissioning C1 contract and deterministic builder."""

from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "docs/baselines/v2.3/phase-2d"
BUILDER = ROOT / "scripts/docs/build-phase-2d-product-implementation-commissioning-c1.py"
VALIDATOR = ROOT / "scripts/docs/validate-phase-2d-product-implementation-commissioning-c1.py"


class CommissioningContractTests(unittest.TestCase):
    def test_validator_passes(self) -> None:
        completed = subprocess.run(["python3", str(VALIDATOR)], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)

    def test_two_reproductions_are_identical(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.json"
            second = Path(directory) / "second.json"
            subprocess.check_call(["python3", str(BUILDER), "--output", str(first)], cwd=ROOT)
            subprocess.check_call(["python3", str(BUILDER), "--output", str(second)], cwd=ROOT)
            self.assertEqual(first.read_bytes(), second.read_bytes())

    def test_all_technology_choices_remain_human_pending(self) -> None:
        payload = json.loads((BASE / "product-implementation-commissioning-c1-technology-decisions.json").read_text())
        self.assertEqual(len(payload["decisions"]), 7)
        self.assertTrue(all(item["selected_option"] is None for item in payload["decisions"]))

    def test_source_and_business_paths_are_protected(self) -> None:
        policy = json.loads((BASE / "product-implementation-commissioning-c1-path-policy.json").read_text())
        self.assertIn("docs/BRD/**", policy["protected_paths"])
        self.assertIn("docs/UXF/**", policy["protected_paths"])
        self.assertIn("PRODUCT_LIST_OR_PRODUCT_DETAIL_API", policy["forbidden_content_classes"])
        self.assertIn("PRODUCT_OR_CATALOG_UI", policy["forbidden_content_classes"])


if __name__ == "__main__":
    unittest.main()
