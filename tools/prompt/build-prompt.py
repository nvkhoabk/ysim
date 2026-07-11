#!/usr/bin/env python3
from pathlib import Path
import argparse,json
from datetime import datetime
p=argparse.ArgumentParser()
p.add_argument('--repo-root',required=True)
p.add_argument('--manifest',required=True)
a=p.parse_args()
repo=Path(a.repo_root)
mf=repo/a.manifest if not Path(a.manifest).is_absolute() else Path(a.manifest)
cfg={}
for line in mf.read_text(encoding='utf-8-sig').splitlines():
    if ':' in line and not line.lstrip().startswith('#'):
        k,v=line.split(':',1);cfg[k.strip()]=v.strip().strip('"')
ctx=repo/cfg.get('context','factory/contexts/generated/s00')
cj=json.loads((ctx/'context.json').read_text())
od=repo/cfg.get('output','factory/prompts/generated/s00/t00'); od.mkdir(parents=True,exist_ok=True)
docs='\n'.join(f"- {d.get('documentCode')} ({d.get('path')})" for d in cj['documents'])
(repo/cfg.get('output','factory/prompts/generated/s00/t00')/'prompt.md').write_text(f'# ROLE\nYou are Codex.\n\n# CONTEXT\n{docs}\n')
(od/'prompt.json').write_text(json.dumps({'generatedAt':datetime.now().isoformat(),'documentCount':cj['documentCount']},indent=2))
(od/'manifest.json').write_text(json.dumps({'sourceManifest':str(mf.relative_to(repo))},indent=2))
print('PASS')
