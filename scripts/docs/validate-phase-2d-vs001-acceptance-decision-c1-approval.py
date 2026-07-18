#!/usr/bin/env python3
import subprocess,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; C='f003eca82512887a616c4ee83ed4ab8da4432b8a'; P='f7f2aeca3c1643996f77dec1b0b5caae22363ddc'; A=['docs/baselines/v2.3/phase-2d/VS001_ACCEPTANCE_DECISION_C1_APPROVAL.md','scripts/docs/validate-phase-2d-vs001-acceptance-decision-c1-approval.py']
g=lambda *x:subprocess.check_output(['git',*x],cwd=R,text=True).strip()
assert g('rev-parse',C+'^')==P and g('rev-parse','HEAD^')==C and sorted(g('diff','--name-only',C,'HEAD').splitlines())==A
d=json.loads(subprocess.check_output(['git','show',C+':docs/baselines/v2.3/phase-2d/vs001-acceptance-decision-c1.json'],cwd=R)); assert all(x['selected_option'] is None for x in d['decisions'])
text=(R/A[0]).read_text(); assert all(x in text for x in ['Khoa, Nguyen','OPT-PUBLISHED-STOREFRONT-ELIGIBLE','OPT-MINIMUM-COMMERCIAL-DISPLAY-WITH-PRICE','OPT-STABLE-SLUG-UNIFORM-NOT-FOUND'])
print('VALID_APPROVED_PHASE_2D_VS001_ACCEPTANCE_DECISION_C1')
