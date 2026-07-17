#!/usr/bin/env python3

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "docs/baselines/v2.3/phase-2"


class SemanticAcceptanceRendererC1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ast = json.loads((BASE / "semantic-acceptance-renderer-c1-ast-previews.json").read_text())["records"]
        cls.procedures = json.loads((BASE / "semantic-acceptance-renderer-c1-procedure-previews.json").read_text())["records"]
        cls.decisions = json.loads((BASE / "semantic-acceptance-renderer-c1-decision-previews.json").read_text())["records"]
        cls.schemas = json.loads((BASE / "semantic-acceptance-renderer-c1-operator-schemas.json").read_text())["operators"]

    def test_population(self):
        self.assertEqual((len(self.ast), len(self.procedures), len(self.decisions)), (910, 156, 27))

    def test_operator_registry_closed(self):
        used = {node["operator_id"] for record in self.ast for node in record["operator_renderings"]}
        used |= {operator for record in self.decisions for operator in record["operator_composition"]}
        self.assertEqual(used, set(self.schemas))

    def test_concrete_negative(self):
        for record in self.ast:
            for node in record["operator_renderings"]:
                self.assertIn(record["bound_subject"]["display_value"], node["negative_oracle"]["text"])
                self.assertIn(record["expected_operand"]["display_value"], node["negative_oracle"]["text"])

    def test_distinct_boundaries(self):
        for record in self.ast:
            for node in record["operator_renderings"]:
                self.assertNotEqual(node["boundary_oracle"]["left"], node["boundary_oracle"]["right"])

    def test_independent_origins(self):
        for record in self.ast:
            self.assertNotEqual(record["expected_operand"]["origin_id"], record["observed_operand"]["origin_id"])

    def test_evidence_specific(self):
        for record in self.ast:
            self.assertGreaterEqual(len(record["evidence_contract"]["field_ids"]), 4)
            self.assertGreaterEqual(len(record["evidence_contract"]["resolver_ids"]), 2)

    def test_procedure_actors(self):
        for procedure in self.procedures:
            self.assertNotIn("reviewer", procedure["authoritative_actor"].lower())
            self.assertFalse(procedure["actor_provenance"]["inference"])

    def test_procedure_actions_unique(self):
        self.assertEqual(len({p["exact_actions"][0] for p in self.procedures}), 156)

    def test_decision_obligations_visible(self):
        for decision in self.decisions:
            for obligation in decision["approved_obligations"]:
                self.assertIn(obligation["text"], decision["positive_oracle"])

    def test_no_runtime_claim(self):
        self.assertTrue(all(r["runtime_status"] == "RUNTIME_ADAPTER_PENDING" for r in self.ast + self.decisions))
        self.assertTrue(all(r["runtime_status"] == "HUMAN_VERIFICATION_REQUIRED" for r in self.procedures))

    def test_operator_adversarial_shapes(self):
        for operator, schema in self.schemas.items():
            with self.subTest(operator=operator):
                self.assertEqual(set(schema["adversarial_examples"].values()), {"REJECT"})
                self.assertEqual(len(schema["adversarial_examples"]), 5)


if __name__ == "__main__":
    unittest.main()
