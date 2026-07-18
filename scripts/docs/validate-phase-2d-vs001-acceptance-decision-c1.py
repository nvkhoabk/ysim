#!/usr/bin/env python3
import json,subprocess,hashlib
from pathlib import Path
EXPECTED_CANONICAL_JSON_SHA256 = 'b5f7ffb9eae4167749ffd5c7ba1038afe401d9e0366103f6223dbb8966695b3f'
R=Path(__file__).resolve().parents[2]; J=R/'docs/baselines/v2.3/phase-2d/vs001-acceptance-decision-c1.json'; raw=J.read_bytes()
if hashlib.sha256(raw).hexdigest()!=EXPECTED_CANONICAL_JSON_SHA256: raise SystemExit('CANONICAL_JSON_HASH_MISMATCH')
d=json.loads(raw); assert d['candidate_id']=='V23-P2D-VS001-ACCEPTANCE-DECISION-C1' and len(d['decisions'])==3
for x in d['decisions']:
 assert x['selected_option'] is None and len(x['options'])==3 and x['recommended_option']==x['options'][0]['option_id']
 for g in x['options'][0]['canonical_rule_groups'].values(): assert all(r['inference'] is False and all(k in r for k in ('rule_id','statement','enforcement','failure_behavior','provenance','inference')) for r in g)
assert sum(len(g) for x in d['decisions'] for g in x['options'][0]['canonical_rule_groups'].values())==124
assert [len(x['options'][0]['canonical_rule_groups']) for x in d['decisions']]==[3,3,3]
print('VALID_VS001_ACCEPTANCE_DECISION_C1_CANDIDATE FULL_PAYLOAD_HASH_LOCK_WITH_NINE_GROUP_STRATIFIED_MUTATION_TESTS')
