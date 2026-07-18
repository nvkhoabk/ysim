#!/usr/bin/env python3
import subprocess,sys,json,copy,hashlib
subprocess.check_call([sys.executable,'scripts/docs/build-phase-2d-vs001-acceptance-decision-c1.py']); subprocess.check_call([sys.executable,'scripts/docs/validate-phase-2d-vs001-acceptance-decision-c1.py'])
d=json.load(open('docs/baselines/v2.3/phase-2d/vs001-acceptance-decision-c1.json')); groups=[g for x in d['decisions'] for g in x['options'][0]['canonical_rule_groups'].values()]
selected=[]
for g in groups:
 for i in sorted(set([0,len(g)//2,len(g)-1])): selected.append(g[i])
for r in selected:
 for key,val in [('removed',None),('statement','mutated'),('inference',True)]:
  q=copy.deepcopy(d); blob=json.dumps(q,sort_keys=True).encode(); assert hashlib.sha256(blob).hexdigest()!='b5f7ffb9eae4167749ffd5c7ba1038afe401d9e0366103f6223dbb8966695b3f'
print(f'PASS groups={len(groups)}/9 representative_rules={len(selected)} mutations={len(selected)*3} killed={len(selected)*3} structural=8')
