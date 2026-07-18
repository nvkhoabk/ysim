#!/usr/bin/env python3
"""Render the focused VS001 implementation-contract continuity decision pack."""
from __future__ import annotations
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/"docs/baselines/v2.3/phase-2d"
JSON_PATH=BASE/"vs001-implementation-contract-continuity-decision-c1.json"
MD_PATH=BASE/"VS001_IMPLEMENTATION_CONTRACT_CONTINUITY_DECISION_C1_CANDIDATE.md"
MANIFEST_PATH=BASE/"vs001-implementation-contract-continuity-decision-c1-manifest.json"
BUILDER=ROOT/"scripts/docs/build-phase-2d-vs001-implementation-contract-continuity-decision-c1.py"
VALIDATOR=ROOT/"scripts/docs/validate-phase-2d-vs001-implementation-contract-continuity-decision-c1.py"
TESTS=ROOT/"scripts/docs/tests/test-phase-2d-vs001-implementation-contract-continuity-decision-c1.py"
INVENTORY=[str(p.relative_to(ROOT)) for p in (MD_PATH,JSON_PATH,MANIFEST_PATH,BUILDER,VALIDATOR,TESTS)]

def canonical(v): return (json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode()
def sha(b): return hashlib.sha256(b).hexdigest()

def render(p):
    lines=["# VS001 Implementation Contract Continuity Decision C1", "",
      f"- Candidate: `{p['candidate_id']}`",f"- Status: `{p['status']}`",f"- Approval: `{p['approval']}`",
      "- Implementation authorized: `false`","- Runtime evidence: `NOT_EXECUTED`",f"- Next gate: `{p['next_gate']}`","",
      "## Authority gap findings",""]
    for g in p["authority_gap_findings"]:
        lines += [f"### {g['finding_id']}","","```json",json.dumps(g,ensure_ascii=False,sort_keys=True,indent=2),"```",""]
    lines += ["## Decisions",""]
    for d in p["decisions"]:
        lines += [f"### {d['decision_id']} — {d['title']}","",f"- Selected option: `{d['selected_option']}`",f"- Recommended: `{d['recommended_option']}`",""]
        for o in d["options"]:
            lines += [f"#### {o['option_id']}","","```json",json.dumps(o,ensure_ascii=False,sort_keys=True,indent=2),"```",""]
        lines += ["Recommendation rationale:","",d["recommendation_rationale"],""]
    lines += ["## Non-claims",""]+[f"- `{x}`" for x in p["non_claims"]]
    return "\n".join(lines).rstrip()+"\n"

def main():
    p=json.loads(JSON_PATH.read_bytes())
    MD_PATH.write_text(render(p),encoding="utf-8",newline="\n")
    hashes={str(x.relative_to(ROOT)):sha(x.read_bytes()) for x in (MD_PATH,JSON_PATH,BUILDER,VALIDATOR,TESTS)}
    generated=[str(MD_PATH.relative_to(ROOT)),str(JSON_PATH.relative_to(ROOT))]
    aggregate=sha(canonical([{"path":x,"sha256":hashes[x]} for x in sorted(generated)]))
    m={"candidate_id":p["candidate_id"],"status":"CANDIDATE","approval":"PENDING_HUMAN_APPROVAL",
       "implementation_authorized":False,"runtime_evidence_status":"NOT_EXECUTED","inventory":INVENTORY,
       "file_sha256_excluding_manifest":hashes,"generated_payload_aggregate":aggregate,
       "hash_domain":"canonical SHA-256 of sorted path/file-SHA records; manifest excluded from itself",
       "staged_tree":"DETACHED_HUMAN_GATE_VALUE","git_content_aggregate":"DETACHED_HUMAN_GATE_VALUE"}
    MANIFEST_PATH.write_bytes(canonical(m))
    print("BUILT_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_CONTINUITY_DECISION_C1")

if __name__=="__main__":main()
