#!/usr/bin/env python3
"""Unit tests for the independent operator-binding type checker."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/"scripts/docs"))
import operator_binding_type_checker as checker


class TypeCheckerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog=json.loads((ROOT/"docs/baselines/v2.3/phase-2/operator-binding-semantic-types.json").read_text())
        cls.schemas=json.loads((ROOT/"docs/baselines/v2.3/phase-2/operator-binding-schemas.json").read_text())["schemas"]

    def test_all_40_schemas_have_complete_bindings(self):
        accepted=json.loads(subprocess.check_output(["git","show","77d10a8c3ccb2e7795724fd1c82cdbea36c54e2e:docs/baselines/v2.3/phase-2/oracle-operator-catalog.json"],cwd=ROOT))
        required={item["operator_id"]:set(item["required_bindings"]) for item in accepted["operators"]}
        self.assertEqual(40,len(self.schemas))
        for schema in self.schemas:
            with self.subTest(operator=schema["operator_id"]):
                self.assertTrue(required[schema["operator_id"]]<={item["name"] for item in schema["bindings"]})

    def test_raw_sentence_is_never_a_typed_value(self):
        for semantic_type in self.catalog["types"]:
            with self.subTest(semantic_type=semantic_type),self.assertRaises(checker.TypeModelError):
                checker.validate_value("The requirement is satisfied.",semantic_type,["SOURCE_LITERAL"],self.catalog,"value")

    def test_same_origin_is_not_independent(self):
        expected=checker.typed_value("ENTITY_ID","CANONICAL_REGISTRY","SAME.ORIGIN",identifier="ENTITY.1")
        observed=checker.typed_value("ENTITY_ID","RUNTIME_OBSERVED","SAME.ORIGIN",identifier="ENTITY.1")
        observed["resolver_contract"]["resolver_id"]="OBSERVE.ENTITY_ID"
        schema={"operator_id":"TEST","bindings":[],"comparison_contract":{"semantic_type":"ENTITY_ID"},"origin_constraints":{"expected_allowed":["CANONICAL_REGISTRY"],"observed_allowed":["RUNTIME_OBSERVED"]},"evaluator_consumes_all_bindings":True}
        fixture={"operator_id":"TEST","bindings":{},"comparison":{"expected":expected,"observed":observed},"evidence_object":checker.typed_value("EVIDENCE_OBJECT_REF","EVIDENCE_OBJECT","EVIDENCE.1")}
        with self.assertRaises(checker.TypeModelError):checker.validate_fixture(fixture,schema,self.catalog)


if __name__=="__main__":unittest.main(verbosity=2)
