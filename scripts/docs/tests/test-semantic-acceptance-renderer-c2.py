#!/usr/bin/env python3
"""Unit tests for Renderer C2 origin normalization."""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("nested", ROOT / "scripts/docs/validate-semantic-acceptance-renderer-c2-nested.py")
NESTED = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(NESTED)


class RendererC2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = ROOT / "docs/baselines/v2.3/phase-2"
        cls.reference = json.loads((base / "semantic-acceptance-renderer-c2-reference-good-contracts.json").read_text())
        cls.supersession = json.loads((base / "semantic-acceptance-renderer-c2-contract-supersession.json").read_text())

    def test_exact_supersession_population(self):
        self.assertEqual(11, len(self.supersession["records"]))

    def test_other_custom_contracts_unchanged(self):
        self.assertEqual(48, self.reference["unchanged_count"])

    def test_nested_contracts_are_clean(self):
        for row in self.reference["records"]:
            self.assertEqual([], NESTED.inspect(row["acceptance_contract"]), row["requirement_id"])

    def test_candidate_prefix_renaming_is_rejected(self):
        for prefix in ("C5", "C6", "C99"):
            fixture = {"origin_id": f"YSIM.{prefix}.RID.SEMANTIC_IDENTIFIER.DEADBEEF", "origin_type": "RUNTIME_OBSERVED"}
            self.assertTrue(NESTED.inspect(fixture))

    def test_schema_identifier_rejected(self):
        fixture = {"semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>", "identifier": "EXPECTED_SET", "namespace": "YSIM.TEST", "authoritative_source": {"source_id": "x"}, "resolver_contract": {"resolver_id": "x"}, "lifecycle": {"version": "1"}, "origin": {"origin_id": "x"}, "provenance": {"inference": False}, "inference": False}
        self.assertTrue(NESTED.inspect(fixture))

    def test_all_corrected_origins_are_distinct_and_concrete(self):
        for row in self.supersession["records"]:
            for change in row["changed_paths"]:
                self.assertNotEqual(change["old"], change["new"])
                self.assertNotIn("SEMANTIC_IDENTIFIER", change["new"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
