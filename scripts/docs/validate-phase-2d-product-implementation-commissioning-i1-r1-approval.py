#!/usr/bin/env python3
import hashlib, json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CANDIDATE='5e4f373619140f575d061436ab3a08368f63c55a'; PARENT='c3429e79b2e80ac050b21dd9dc5844dd64029ce0'; TREE='420c7c120a3c04ceb086e42d5de42db6b62c6558'
APPROVAL=['docs/baselines/v2.3/phase-2d/PRODUCT_IMPLEMENTATION_COMMISSIONING_I1_R1_APPROVAL.md','scripts/docs/validate-phase-2d-product-implementation-commissioning-i1-r1-approval.py']
def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(ref,p): return subprocess.check_output(['git','show',f'{ref}:{p}'],cwd=ROOT)
def need(ok,msg):
 if not ok: raise SystemExit('INVALID_APPROVED_PHASE_2D_PRODUCT_IMPLEMENTATION_COMMISSIONING_I1_R1: '+msg)
def main():
 head=git('rev-parse','HEAD'); need(git('rev-parse',CANDIDATE+'^')==PARENT,'candidate parent'); need(git('rev-parse',CANDIDATE+'^{tree}')==TREE,'tree'); need(git('rev-parse','HEAD^')==CANDIDATE,'accepted parent'); need(sorted(git('diff','--name-only',CANDIDATE,head).splitlines())==APPROVAL,'approval diff')
 mpath='scripts/commissioning/evidence/commissioning-i1-manifest.json'; mbytes=blob(CANDIDATE,mpath); m=json.loads(mbytes); need(len(git('diff','--name-only',PARENT,CANDIDATE).splitlines())==62,'inventory'); need(m['candidate_id']=='V23-P2D-PRODUCT-IMPLEMENTATION-COMMISSIONING-I1-R1' and m['status']=='CANDIDATE' and m['acceptance']=='PENDING_HUMAN_ACCEPTANCE','candidate state'); need(hashlib.sha256(mbytes).hexdigest()=='33643b27f53ea6ac5bf12d913bde63721ae87c3577cf331749619cf89512df92','manifest');
 for p,h in m['per_file_sha256'].items(): need(hashlib.sha256(blob(CANDIDATE,p)).hexdigest()==h and blob(CANDIDATE,p)==blob(head,p),'signed blob '+p)
 text=(ROOT/APPROVAL[0]).read_text();
 for s in ['Khoa, Nguyen','2026-07-18','PRODUCT_IMPLEMENTATION_COMMISSIONING_INFRASTRUCTURE_ONLY',CANDIDATE,PARENT,TREE,'NOT_VS001_BUSINESS_IMPLEMENTATION']: need(s in text,'approval field '+s)
 need(not git('diff','--name-only',PARENT,CANDIDATE,'--','docs/BRD','docs/UXF'),'BRD UXF'); print('VALID_APPROVED_PHASE_2D_PRODUCT_IMPLEMENTATION_COMMISSIONING_I1_R1')
if __name__=='__main__': main()
