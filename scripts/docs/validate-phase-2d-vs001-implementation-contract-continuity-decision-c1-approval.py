#!/usr/bin/env python3
"""Validate detached approval for the VS001 continuity decision pack."""
from __future__ import annotations
import hashlib,json,re,subprocess,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BASE="5b4159cdec2b93e94a65690314624518d1ddc94e"
CANDIDATE="711c9e5a388a811df4f66bd0525a1568b0f431ea"
TREE="87a9d3300b317504dcdf89399c75c6ec82b6488f"
JSON_PATH="docs/baselines/v2.3/phase-2d/vs001-implementation-contract-continuity-decision-c1.json"
APPROVAL_PATH="docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_CONTRACT_CONTINUITY_DECISION_C1_APPROVAL.md"
VALIDATOR_PATH="scripts/docs/validate-phase-2d-vs001-implementation-contract-continuity-decision-c1-approval.py"
APPROVAL_FILES=[APPROVAL_PATH,VALIDATOR_PATH]
CANDIDATE_FILES=[
 "docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_CONTRACT_CONTINUITY_DECISION_C1_CANDIDATE.md",
 JSON_PATH,
 "docs/baselines/v2.3/phase-2d/vs001-implementation-contract-continuity-decision-c1-manifest.json",
 "scripts/docs/build-phase-2d-vs001-implementation-contract-continuity-decision-c1.py",
 "scripts/docs/validate-phase-2d-vs001-implementation-contract-continuity-decision-c1.py",
 "scripts/docs/tests/test-phase-2d-vs001-implementation-contract-continuity-decision-c1.py"]
HASHES={
 CANDIDATE_FILES[0]:"a3839d0b085ae03328aa9d902abdfe817b10f3b0bfbd173386c1eb76371cb02a",
 CANDIDATE_FILES[1]:"aa932cafae91861cf083103839577e7e7e9041c4106d04c5636e4c9d16a9a09e",
 CANDIDATE_FILES[2]:"5f0401dca04c1a5f32b1cf5a628db37a10ff3891704314ee2329259f2229b1c0",
 CANDIDATE_FILES[3]:"8f6da80a4c561ed6717d45738b726e1a076f6b44eae3f69cf7eccae2063aad66",
 CANDIDATE_FILES[4]:"3d4ac4ba78b0c5ff8033c10aff397f499fd7e18f1c03a70cde0a9527b006bc31",
 CANDIDATE_FILES[5]:"23c42f94d323181f752b5b2aa7f1274b1528c8d9a5b55418a2680086748a8b98"}
EXPECTED={
 "V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-001":"OPT-QORDER-EXACT-THEN-STOREFRONT-DEFAULT",
 "V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-002":"OPT-STATELESS-LOGICAL-REVISION-CURSOR"}

class ApprovalError(Exception):pass
def fail(c,d=""):raise ApprovalError(c+(":"+d if d else ""))
def git(*a):return subprocess.check_output(["git",*a],cwd=ROOT)
def sha(b):return hashlib.sha256(b).hexdigest()

def lifecycle():
    head=git("rev-parse","HEAD").decode().strip(); staged=git("diff","--cached","--name-only").decode().splitlines()
    if head==CANDIDATE and set(staged)==set(APPROVAL_FILES):return "STAGED_APPROVAL_OVER_CANDIDATE",lambda p:git("show",f":{p}")
    if git("rev-parse","HEAD^").decode().strip()==CANDIDATE and not staged:return "COMMITTED_ACCEPTED",lambda p:git("show",f"HEAD:{p}")
    fail("APPROVAL_LIFECYCLE_MISMATCH",head)

def main():
  try:
    mode,read_approval=lifecycle()
    if git("rev-parse",f"{CANDIDATE}^").decode().strip()!=BASE or git("rev-parse",f"{CANDIDATE}^{{tree}}").decode().strip()!=TREE:fail("CANDIDATE_CHAIN_OR_TREE_MISMATCH")
    delta=git("diff-tree","--no-commit-id","--name-only","-r",BASE,CANDIDATE).decode().splitlines()
    if sorted(delta)!=sorted(CANDIDATE_FILES):fail("CANDIDATE_INVENTORY_MISMATCH")
    for p,h in HASHES.items():
      if sha(git("show",f"{CANDIDATE}:{p}"))!=h:fail("SIGNED_CANDIDATE_BLOB_MISMATCH",p)
    payload=json.loads(git("show",f"{CANDIDATE}:{JSON_PATH}"))
    if payload["candidate_id"]!="V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DECISION-C1" or payload["status"]!="CANDIDATE" or payload["approval"]!="PENDING_HUMAN_APPROVAL":fail("CANDIDATE_STATE_MISMATCH")
    if any(d["selected_option"] is not None for d in payload["decisions"]):fail("CANDIDATE_SELECTION_NOT_NULL")
    if payload["implementation_authorized"] is not False or payload["runtime_evidence_status"]!="NOT_EXECUTED":fail("FALSE_IMPLEMENTATION_OR_RUNTIME_CLAIM")
    text=read_approval(APPROVAL_PATH).decode(); selections=dict(re.findall(r"`(V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-\d{3})`\s+→\s+`([^`]+)`",text))
    if selections!=EXPECTED:fail("DETACHED_SELECTION_MISMATCH")
    for did,oid in EXPECTED.items():
      d=next(x for x in payload["decisions"] if x["decision_id"]==did)
      if oid not in {o["option_id"] for o in d["options"]}:fail("SELECTED_OPTION_NOT_IN_CANDIDATE",oid)
    required=["Authorized approver: `Khoa, Nguyen`","Approval date: `2026-07-19`","Approval scope: `PHASE_2D_VS001_LOCALE_NEGOTIATION_AND_CROSS_REQUEST_SNAPSHOT_CONTINUITY_ONLY`",
      "Candidate tree: `87a9d3300b317504dcdf89399c75c6ec82b6488f`","Canonical JSON SHA-256: `aa932cafae91861cf083103839577e7e7e9041c4106d04c5636e4c9d16a9a09e`"]
    if not all(x in text for x in required):fail("APPROVAL_IDENTITY_OR_SCOPE_MISMATCH")
    if mode=="COMMITTED_ACCEPTED":
      adelta=git("diff-tree","--no-commit-id","--name-only","-r",CANDIDATE,"HEAD").decode().splitlines()
      if sorted(adelta)!=sorted(APPROVAL_FILES):fail("ACCEPTED_DIFF_NOT_EXACT_TWO_FILES")
    all_delta=set(git("diff","--name-only",BASE,"HEAD").decode().splitlines())|set(git("diff","--cached","--name-only").decode().splitlines())
    if any(p.startswith(("apps/","packages/","database/","configs/","docs/BRD/","docs/UXF/","scripts/commissioning/","runtime/","infrastructure/")) for p in all_delta):fail("PROTECTED_OR_IMPLEMENTATION_CHANGE")
    if any("IMPLEMENTATION_CONTRACT_C1_R1" in p for p in all_delta):fail("C1_R1_CREATED_IN_PERSISTENCE_TURN")
    print(json.dumps({"result":"VALID_APPROVED_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_CONTINUITY_DECISION_C1","lifecycle_mode":mode,"candidate_commit":CANDIDATE,"candidate_tree":TREE,"candidate_files":6,"approval_files":2,"effective_selections":2,"candidate_selected_options":0,"implementation_authorized":False},sort_keys=True))
    print("VALID_APPROVED_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_CONTINUITY_DECISION_C1");return 0
  except (ApprovalError,KeyError,TypeError,ValueError,subprocess.CalledProcessError) as e:
    print("INVALID_APPROVED_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_CONTINUITY_DECISION_C1",e,file=sys.stderr);return 1
if __name__=="__main__":raise SystemExit(main())
