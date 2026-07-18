#!/usr/bin/env python3
"""Independent validator for the focused continuity decision pack."""
from __future__ import annotations
import argparse,hashlib,json,re,subprocess,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
JSON_REL="docs/baselines/v2.3/phase-2d/vs001-implementation-contract-continuity-decision-c1.json"
MD_REL="docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_CONTRACT_CONTINUITY_DECISION_C1_CANDIDATE.md"
MANIFEST_REL="docs/baselines/v2.3/phase-2d/vs001-implementation-contract-continuity-decision-c1-manifest.json"
BUILDER_REL="scripts/docs/build-phase-2d-vs001-implementation-contract-continuity-decision-c1.py"
VALIDATOR_REL="scripts/docs/validate-phase-2d-vs001-implementation-contract-continuity-decision-c1.py"
TEST_REL="scripts/docs/tests/test-phase-2d-vs001-implementation-contract-continuity-decision-c1.py"
FILES=[MD_REL,JSON_REL,MANIFEST_REL,BUILDER_REL,VALIDATOR_REL,TEST_REL]
HEAD="5b4159cdec2b93e94a65690314624518d1ddc94e"
DECISION_COMMIT="51857c222509b058067589d8d2dab42cd0593dff"
DECISION_PATH="docs/baselines/v2.3/phase-2d/vs001-implementation-decision-c1.json"
APPROVAL_PATH="docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_DECISION_C1_APPROVAL.md"
EXPECTED_AUTH_SHA="08c22be8b5ff29e0d8b8dbd3aa3ddeeed74533fe866848d5ad051f832d7df705"
EXPECTED_APPROVAL_SHA="ae2af135c888dff312a8ba2f263f45eb7c9be7ba88ff1eb4b6dc98db96a5e000"
EXPECTED_FP={
 "V23-P2D-VS001-IMPLEMENTATION-DEC-002":"924e38fc32d48bb5d02e8a9178256da9871d3a949bfad66613c2eb3cc4dbe96f",
 "V23-P2D-VS001-IMPLEMENTATION-DEC-003":"74178064c2a7b1a40b8a9d1ac14ae5bd7a96eb87869b0353286a2f7c9555e441",
 "V23-P2D-VS001-IMPLEMENTATION-DEC-008":"ebae50e1d8828d3091335271ff722f5c348e29c73c3198a40125ce1b9ad5b748"}

class DecisionError(Exception):pass
def fail(code,detail=""):raise DecisionError(code+(":"+detail if detail else ""))
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(v):return (json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode()
def run(*a):return subprocess.check_output(a,cwd=ROOT)

def validate_authority(p):
    raw=run("git","show",f"{DECISION_COMMIT}:{DECISION_PATH}"); approval=run("git","show",f"{HEAD}:{APPROVAL_PATH}")
    if sha(raw)!=EXPECTED_AUTH_SHA or sha(approval)!=EXPECTED_APPROVAL_SHA:fail("SIGNED_AUTHORITY_BLOB_MISMATCH")
    if run("git","rev-parse",f"{HEAD}^").decode().strip()!=DECISION_COMMIT:fail("SIGNED_AUTHORITY_CHAIN_MISMATCH")
    auth=json.loads(raw); selections=dict(re.findall(rb"`(V23-P2D-VS001-IMPLEMENTATION-DEC-\d{3})`\s+\xe2\x86\x92\s+`([^`]+)`",approval))
    selections={k.decode():v.decode() for k,v in selections.items()}
    wanted={"V23-P2D-VS001-IMPLEMENTATION-DEC-002":"OPT-BCP47-REQUEST-THEN-STOREFRONT-DEFAULT",
            "V23-P2D-VS001-IMPLEMENTATION-DEC-003":"OPT-OPAQUE-CURSOR-SLUG-IDENTITY-ORDER",
            "V23-P2D-VS001-IMPLEMENTATION-DEC-008":"OPT-REQUEST-TIMESTAMP-REPEATABLE-READ-SNAPSHOT"}
    for did,oid in wanted.items():
        d=next(x for x in auth["decisions"] if x["decision_id"]==did); o=next(x for x in d["options"] if x["option_id"]==oid)
        fp=sha(canonical({"decision_id":did,"selected_option":o,"non_inferences":d["non_inferences"]}))
        if selections.get(did)!=oid or fp!=EXPECTED_FP[did] or p["authority"]["governing_option_fingerprints"].get(did)!=fp:fail("GOVERNING_OPTION_AUTHORITY_MISMATCH",did)
    if p["authority"]["canonical_blob_sha256"]!=EXPECTED_AUTH_SHA or p["authority"]["approval_blob_sha256"]!=EXPECTED_APPROVAL_SHA:fail("DECLARED_AUTHORITY_HASH_MISMATCH")

def validate_semantics(p):
    if p.get("candidate_id")!="V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DECISION-C1" or p.get("status")!="CANDIDATE" or p.get("approval")!="PENDING_HUMAN_APPROVAL":fail("CANDIDATE_STATE_MISMATCH")
    if p.get("implementation_authorized") is not False or p.get("runtime_evidence_status")!="NOT_EXECUTED":fail("FALSE_AUTHORIZATION_OR_RUNTIME_CLAIM")
    if p.get("next_gate")!="HUMAN_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_CONTINUITY_DECISION_REQUIRED":fail("NEXT_GATE_MISMATCH")
    if p["blocked_c1_preservation"]!={"backup_ref":"refs/ysim-backups/v2.3/phase-2d-vs001-implementation-contract-c1-final-audit-blocked","backup_object":"7cd340caa03e619de306f17c34aa067c117e437e","tree":"771a8292a5a381a50b963c36a30e55137d1789fb","git_content_aggregate":"be0842c892096c2d16c35011423f6457a20ab801d759ca5ad135059605d583b9","inventory":6,"recovery":"6/6_BYTE_IDENTICAL","rejection_reason":"SYSTEMIC_SEMANTIC_MAPPING_VALIDATION_AND_EXECUTABLE_BINDING_GAPS"}:fail("BLOCKED_C1_PRESERVATION_MISMATCH")
    if run("git","rev-parse",p["blocked_c1_preservation"]["backup_ref"]).decode().strip()!=p["blocked_c1_preservation"]["backup_object"]:fail("BLOCKED_C1_BACKUP_REF_MISMATCH")
    ds=p.get("decisions",[])
    if len(ds)!=2 or {d["decision_id"] for d in ds}!={"V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-001","V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-002"}:fail("DECISION_INVENTORY_MISMATCH")
    if any(d.get("selected_option") is not None for d in ds):fail("HUMAN_SELECTION_NOT_NULL")
    expected={
      "V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-001":({"OPT-QORDER-EXACT-THEN-STOREFRONT-DEFAULT","OPT-SINGLE-HIGHEST-QUALITY-THEN-DEFAULT","OPT-QORDER-WITH-BASIC-LANGUAGE-FALLBACK"},"OPT-QORDER-EXACT-THEN-STOREFRONT-DEFAULT"),
      "V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-002":({"OPT-STATELESS-LOGICAL-REVISION-CURSOR","OPT-SERVER-HELD-POSTGRES-SNAPSHOT-CURSOR","OPT-REQUEST-LOCAL-SNAPSHOT-FAIL-CLOSED"},"OPT-STATELESS-LOGICAL-REVISION-CURSOR")}
    for d in ds:
        ids=[o["option_id"] for o in d.get("options",[])]
        if len(ids)!=3 or set(ids)!=expected[d["decision_id"]][0] or d.get("recommended_option")!=expected[d["decision_id"]][1]:fail("OPTION_INVENTORY_OR_RECOMMENDATION_MISMATCH",d["decision_id"])
    loc=next(d for d in ds if d["decision_id"].endswith("001")); alg=next(o for o in loc["options"] if o["option_id"]==loc["recommended_option"])["algorithm"]
    required={"parse","priority","q_zero","malformed","wildcard","matching","resolved_locale_output","mandatory_content_failure"}
    if set(alg)!=required:fail("LOCALE_ALGORITHM_INCOMPLETE")
    checks={"priority":["descending q-value","header order"],"q_zero":["never selected"],"matching":["exact","no language-subtag"],"resolved_locale_output":["Content-Language"]}
    for field,terms in checks.items():
        if not all(t.lower() in alg[field].lower() for t in terms):fail("LOCALE_SEMANTIC_MISMATCH",field)
    snap=next(d for d in ds if d["decision_id"].endswith("002")); rec=next(o for o in snap["options"] if o["option_id"]==snap["recommended_option"])["contract"]
    if set(rec)!={"request_snapshot","cursor","concurrent_change","invalid_or_expired","cleanup"}:fail("SNAPSHOT_CONTINUITY_CONTRACT_INCOMPLETE")
    for term in ("its own PostgreSQL repeatable-read transaction","logical catalog revision","15-minute expiry","HTTP 400","INVALID_CURSOR","No server-held snapshot"):
        if term.lower() not in json.dumps(rec,ensure_ascii=False).lower():fail("SNAPSHOT_CONTINUITY_SEMANTIC_MISMATCH",term)
    if p["decision_accounting"]!={"decisions":2,"options_per_decision":3,"selected_options":0,"unresolved_authority_gaps":2,"implementation_changes":0,"runtime_evidence_executed":0}:fail("DECISION_ACCOUNTING_MISMATCH")

def validate_markdown(p,root):
    text=(root/MD_REL).read_text()
    if not text.endswith("\n") or text.endswith("\n\n"):fail("MARKDOWN_EOF_MISMATCH")
    blocks=[json.loads(x) for x in re.findall(r"```json\n(.*?)\n```",text,re.S)]
    for gap in p["authority_gap_findings"]:
        if gap not in blocks:fail("MARKDOWN_GAP_PROJECTION_MISSING",gap["finding_id"])
    for d in p["decisions"]:
        if f"- Selected option: `{d['selected_option']}`" not in text:fail("MARKDOWN_SELECTION_PROJECTION_MISMATCH",d["decision_id"])
        for o in d["options"]:
            if o not in blocks:fail("MARKDOWN_OPTION_PROJECTION_MISSING",o["option_id"])

def validate_manifest(root):
    m=json.loads((root/MANIFEST_REL).read_bytes())
    if m["inventory"]!=FILES:fail("MANIFEST_INVENTORY_MISMATCH")
    for path,h in m["file_sha256_excluding_manifest"].items():
        if sha((root/path).read_bytes())!=h:fail("MANIFEST_FILE_HASH_MISMATCH",path)
    domain=[MD_REL,JSON_REL]; agg=sha(canonical([{"path":x,"sha256":m["file_sha256_excluding_manifest"][x]} for x in sorted(domain)]))
    if agg!=m["generated_payload_aggregate"]:fail("GENERATED_AGGREGATE_MISMATCH")

def validate(p,root=ROOT,check_files=True):
    validate_authority(p);validate_semantics(p)
    if check_files:validate_markdown(p,root);validate_manifest(root)
    return {"authority_options":3,"decisions":2,"selected_options":0,"implementation_changes":0}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--root",type=Path,default=ROOT);args=ap.parse_args()
    try:
        p=json.loads((args.root/JSON_REL).read_bytes());r=validate(p,args.root,True);print("VALID_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_CONTINUITY_DECISION_C1",json.dumps(r,sort_keys=True));return 0
    except (DecisionError,KeyError,TypeError,ValueError,subprocess.CalledProcessError) as e:
        print("INVALID_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_CONTINUITY_DECISION_C1",e,file=sys.stderr);return 1
if __name__=="__main__":raise SystemExit(main())
