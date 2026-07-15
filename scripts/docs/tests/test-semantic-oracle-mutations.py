#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
P2 = ROOT / "docs/baselines/v2.3/phase-2"


def module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    assert spec.loader
    spec.loader.exec_module(value)
    return value


ENGINE = module("semantic_oracle_engine_test", ROOT / "scripts/docs/semantic-oracle-engine.py")


class MutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = json.loads((P2 / "oracle-operator-catalog.json").read_text())

    def test_each_operator_executes_direct_conformance_suite(self) -> None:
        result = ENGINE.run_operator_conformance(self.catalog)
        self.assertEqual(result["operator_count"], 40)
        self.assertEqual(result["passed"], 40)
        self.assertEqual({row["operator_id"] for row in result["rows"]}, {item["operator_id"] for item in self.catalog["operators"]})
        for row in result["rows"]:
            with self.subTest(operator=row["operator_id"]):
                self.assertTrue(all(item["actual_detection"] == "KILLED" for item in row["execution_records"]))
                self.assertTrue(all(item["original_sha256"] != item["mutant_sha256"] for item in row["execution_records"]))

    def test_ten_adversarial_cases_fail_closed(self) -> None:
        result = ENGINE.run_adversarial(self.catalog)
        self.assertEqual((result["passed"], result["total"]), (10, 10))

    def test_independent_challenges_are_execution_derived(self) -> None:
        result = ENGINE.run_independent_challenges(self.catalog)
        self.assertEqual((result["killed"], result["generated"], result["survived"]), (42, 42, 0))
        self.assertEqual(len({item["operator_id"] for item in result["rows"]}), 40)


if __name__ == "__main__":
    unittest.main()
