#!/usr/bin/env python3
"""Unit tests for Phase 2C semantic infrastructure amendment A1."""

from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts/docs"))
import semantic_infrastructure_amendment_a1 as core


def load_builder():
    path = ROOT / "scripts/docs/build-phase-2c-semantic-infrastructure-amendment-a1.py"
    spec = importlib.util.spec_from_file_location("amendment_a1_builder_tests", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class AmendmentA1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.builder = load_builder()
        cls.types = cls.builder.type_amendment()
        cls.example = cls.builder.example()

    def test_valid_reference_example(self):
        core.validate_generic_set_contract(self.example, self.types)

    def test_all_three_operator_signatures(self):
        self.assertEqual(
            [item["type_signature"] for item in self.types["operators"]],
            ["SET_EQUALS<T>", "SET_CONTAINS<T>", "SET_EXCLUDES<T>"],
        )

    def test_generic_type_catalog_is_not_example_limited(self):
        accepted = json.loads((ROOT / "docs/baselines/v2.3/phase-2/operator-binding-semantic-types.json").read_text())
        self.assertEqual(self.types["allowed_type_parameters"], sorted(accepted["types"]))
        self.assertIn("CONFIGURATION_KEY", self.types["reference_target_types"])
        self.assertIn("CAPABILITY_ID", self.types["reference_target_types"])
        self.assertIn("ENTITY_ID", self.types["reference_target_types"])

    def test_adversarial_matrix(self):
        rows = core.adversarial_results(self.types, self.example)
        self.assertEqual(len(rows), 30)
        self.assertTrue(all(item["result"] == "PASS" for item in rows))

    def test_alias_regression(self):
        row = core.alias_regression()
        self.assertEqual(row["isolated_hash"], "23f0cd102050f812c1da9aae80b21421d17b1ae146f2f557ba1182bfc194ca00")
        self.assertEqual(row["aliased_hash"], "e9aa0328aced18ee1d6c181b6a0b1039423764202aaedb92488955a82fea6711")
        self.assertTrue(row["aliased_result_rejected"])

    def test_impact_accounting(self):
        impact = core.impact_audit()
        self.assertEqual(impact["vulnerable_hash_count"], 354)
        self.assertEqual(impact["reproduced_hash_count"], 177)

    def test_unknown_mutation_rejected(self):
        fixture = core.backup_json("docs/baselines/v2.3/phase-2/semantic-completion-c4-fixtures.json")["fixtures"][0]
        mutation = {"mutation_kind": "UNKNOWN", "target": "/validation_fixture/comparison/observed"}
        with self.assertRaisesRegex(core.AmendmentError, "UNKNOWN_MUTATION"):
            core.apply_isolated_mutation(core.canonical(fixture), mutation)

    def test_missing_mutation_target_rejected(self):
        fixture = core.backup_json("docs/baselines/v2.3/phase-2/semantic-completion-c4-fixtures.json")["fixtures"][0]
        mutation = {"mutation_kind": "SEMANTIC_DIFFERENCE", "target": "/validation_fixture/missing"}
        with self.assertRaisesRegex(core.AmendmentError, "MISSING_MUTATION_TARGET"):
            core.apply_isolated_mutation(core.canonical(fixture), mutation)

    def test_noncanonical_input_rejected(self):
        fixture = core.backup_json("docs/baselines/v2.3/phase-2/semantic-completion-c4-fixtures.json")["fixtures"][0]
        noncanonical = json.dumps(fixture, ensure_ascii=False, indent=2).encode()
        mutation = {"mutation_kind": "SEMANTIC_DIFFERENCE", "target": "/validation_fixture/comparison/observed"}
        with self.assertRaisesRegex(core.AmendmentError, "NONCANONICAL_FIXTURE_INPUT"):
            core.apply_isolated_mutation(noncanonical, mutation)

    def test_no_c4_write_target(self):
        self.assertFalse(any("semantic-completion-c4" in path for path in self.builder.OUTPUTS))

    def test_two_builds_identical(self):
        self.assertEqual(self.builder.build(), self.builder.build())


if __name__ == "__main__":
    unittest.main(verbosity=2)
