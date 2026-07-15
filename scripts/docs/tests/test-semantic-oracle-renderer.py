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


RENDERER = module("semantic_oracle_renderer_test", ROOT / "scripts/docs/render-semantic-oracle-contract.py")


class RendererTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = json.loads((P2 / "oracle-operator-catalog.json").read_text())
        cls.references = json.loads((P2 / "semantic-oracle-reference-contracts.json").read_text())

    def test_all_retained_reference_renderings_are_concrete(self) -> None:
        for reference in self.references["contracts"]:
            if reference["semantic_status"] != "RETAINED_EXECUTABLE":
                continue
            for rendered in reference["rendered_oracles"]:
                with self.subTest(reference=reference["reference_id"], operator=rendered["operator_id"]):
                    RENDERER.validate_rendered_contract(rendered)

    def test_unknown_operator_fails_closed(self) -> None:
        with self.assertRaisesRegex(RENDERER.RenderError, "HUMAN_OPERATOR_MAPPING_REVIEW"):
            RENDERER.render("UNKNOWN", {"x":"y"}, ["evidence"], self.catalog)

    def test_generic_paraphrases_fail_completeness(self) -> None:
        for text in ("The operation produces the intended result.", "Invalid input is dealt with in a suitable manner.", "Evidence demonstrates that behavior remains acceptable."):
            with self.subTest(text=text), self.assertRaises(RENDERER.RenderError):
                RENDERER.validate_rendered_contract({"operator_id":"CAPABILITY_AVAILABLE","bindings":{},"positive":text,"negative":text+" N","boundary":text+" B","evidence_fields":[]})


if __name__ == "__main__":
    unittest.main()
