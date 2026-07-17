#!/usr/bin/env python3
"""Tests for the Phase 2C progressive document baseline C1."""

from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "docs/baselines/v2.3/phase-2"


class ProgressiveBaselineTests(unittest.TestCase):
    def test_readiness_is_honest(self) -> None:
        registry = json.loads((BASE / "phase-2c-progressive-document-baseline-c1-registry.json").read_text())
        self.assertEqual(registry["summary"]["acceptance_gap"], 1093)
        self.assertEqual(registry["summary"]["acceptance_ready_count"], 59)

    def test_pending_has_no_acceptance_content(self) -> None:
        registry = json.loads((BASE / "phase-2c-progressive-document-baseline-c1-registry.json").read_text())
        pending = [r for r in registry["requirements"] if r.get("acceptance_status") == "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"]
        self.assertEqual(len(pending), 1093)
        self.assertTrue(all(r["acceptance_contract"]["acceptance_content"] is None for r in pending))

    def test_validators(self) -> None:
        for script in (
            "scripts/docs/validate-phase-2c-progressive-document-baseline-c1.py",
            "scripts/docs/validate-phase-2c-progressive-document-baseline-c1-roundtrip.py",
            "scripts/docs/validate-phase-2c-progressive-document-baseline-c1-regressions.py",
        ):
            subprocess.run(["python3", script], cwd=ROOT, check=True)


if __name__ == "__main__":
    unittest.main()
