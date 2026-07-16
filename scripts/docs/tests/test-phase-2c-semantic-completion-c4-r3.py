#!/usr/bin/env python3
import json,subprocess,unittest
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];P2=ROOT/"docs/baselines/v2.3/phase-2"
class R3(unittest.TestCase):
 @classmethod
 def setUpClass(cls): cls.d=json.loads((P2/"semantic-completion-c4-r3-decision-contract-options.json").read_text())
 def test_count(self): self.assertEqual(len(self.d["decisions"]),27)
 def test_pending(self): self.assertTrue(all(x["selected_option"] is None and x["status"]=="PENDING_HUMAN_APPROVAL" for x in self.d["decisions"]))
 def test_distribution(self): self.assertEqual(Counter(x["audit_result"] for x in self.d["decisions"]),Counter({"SAFE_TO_APPROVE_RECOMMENDED_OPTION":25,"BUSINESS_DECISION_OPTION_READY":2}))
 def test_business_choices(self):
  for suffix in ("004","013"):
   x=next(x for x in self.d["decisions"] if x["decision_id"].endswith(suffix));self.assertEqual(len(x["available_options"]),3)
 def test_storefront_dependencies(self):
  ids=["021","022","026","027"];rows=[next(x for x in self.d["decisions"] if x["decision_id"].endswith(i)) for i in ids];self.assertEqual([len(x["dependencies"]) for x in rows],[0,1,2,3])
 def test_wcag(self):
  for suffix in ("024","025"):
   x=next(x for x in self.d["decisions"] if x["decision_id"].endswith(suffix));self.assertIn("UXD-07",x["source_provenance"]["approved_decision_ids"])
 def test_no_generic_false_claim(self): self.assertNotIn("concrete bindings are recorded in the decision",json.dumps(self.d).lower())
 def test_r2_ref(self): self.assertEqual(subprocess.check_output(["git","rev-parse","refs/ysim-backups/v2.3/phase-2c-semantic-completion-c4-r2-decision-incomplete"],cwd=ROOT,text=True).strip(),"24d72df1e1eba625b89983e80b6fad32a973bbb5")
if __name__=="__main__": unittest.main()
