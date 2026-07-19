#!/usr/bin/env python3
"""Build the authority-bound VS001 implementation-contract C1-R2 candidate."""
from __future__ import annotations
import hashlib,json,os,subprocess
from pathlib import Path

ROOT=Path(os.environ.get("C1_R2_ROOT_OVERRIDE",Path(__file__).resolve().parents[2]));GIT_ROOT=Path(os.environ.get("C1_R2_GIT_ROOT",ROOT));BASE=ROOT/"docs/baselines/v2.3/phase-2d"
JSON_PATH=BASE/"vs001-implementation-contract-c1-r2.json";MD_PATH=BASE/"VS001_IMPLEMENTATION_CONTRACT_C1_R2_CANDIDATE.md";MANIFEST_PATH=BASE/"vs001-implementation-contract-c1-r2-manifest.json"
BUILDER=ROOT/"scripts/docs/build-phase-2d-vs001-implementation-contract-c1-r2.py";VALIDATOR=ROOT/"scripts/docs/validate-phase-2d-vs001-implementation-contract-c1-r2.py";TESTS=ROOT/"scripts/docs/tests/test-phase-2d-vs001-implementation-contract-c1-r2.py"
FILES=[str(x.relative_to(ROOT)) for x in (MD_PATH,JSON_PATH,MANIFEST_PATH,BUILDER,VALIDATOR,TESTS)]
HEAD="f67422a19fb91a03f3e7c8336268724262c696e7";ACCEPTANCE="5780bf5e89c66103980fd4cda7c2b294fdc23f20";APATH="docs/baselines/v2.3/phase-2d/vs001-acceptance-elaboration-c2-r2.json"
RENDERER="120184748c70543b86220fb4f3f3089e99d175dc";RPATH="docs/baselines/v2.3/phase-2/semantic-acceptance-renderer-c2-reference-good-contracts.json"
IMPL_DEC="51857c222509b058067589d8d2dab42cd0593dff";IPATH="docs/baselines/v2.3/phase-2d/vs001-implementation-decision-c1.json"
CONT_DEC="711c9e5a388a811df4f66bd0525a1568b0f431ea";CPATH="docs/baselines/v2.3/phase-2d/vs001-implementation-contract-continuity-decision-c1.json"

def git_json(c,p):return json.loads(subprocess.check_output(["git","show",f"{c}:{p}"],cwd=GIT_ROOT))
def canonical(v):return (json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode()
def digest(v):return hashlib.sha256(canonical(v)).hexdigest()
def sha(b):return hashlib.sha256(b).hexdigest()

ALLOWED=["database/config/schema.prisma","database/migrations/20260719000000_vs001_public_catalog/migration.sql","database/seed-mechanism/vs001-fixtures.ts","packages/contracts/src/index.ts","packages/contracts/src/vs001/public-catalog.ts","apps/api/src/app.module.ts","apps/api/src/vs001/public-catalog.module.ts","apps/api/src/vs001/public-catalog.controller.ts","apps/api/src/vs001/public-catalog.service.ts","apps/api/src/vs001/public-catalog.repository.ts","apps/api/src/vs001/eligibility-resolver.ts","apps/api/src/vs001/price-resolver.ts","apps/api/src/vs001/public-catalog-audit.ts","apps/web/app/catalog/page.tsx","apps/web/app/catalog/loading.tsx","apps/web/app/catalog/error.tsx","apps/web/app/catalog/[public_slug]/page.tsx","apps/web/app/catalog/[public_slug]/loading.tsx","apps/web/app/catalog/[public_slug]/error.tsx","apps/web/app/catalog/[public_slug]/not-found.tsx","apps/web/src/vs001/public-catalog-client.ts","apps/web/src/vs001/public-catalog-view.tsx","tests/vs001/api/public-catalog.integration.test.ts","tests/vs001/browser/public-catalog.spec.ts","tests/vs001/data/public-catalog-integrity.test.ts","tests/vs001/security/public-catalog-disclosure.test.ts","scripts/vs001/fixtures.mjs","scripts/vs001/cleanup.mjs","scripts/vs001/validate-evidence.mjs","scripts/vs001/bootstrap-clean-checkout.mjs","configs/local/vs001.env.example","package.json"]
PROTECTED=["docs/BRD/**","docs/UXF/**","accepted docs/baselines artifacts","scripts/commissioning/**","runtime/**","infrastructure/**","YADF/**","deployment/**",".github/**","pnpm-lock.yaml","all application/package/database/config paths not explicitly listed"]
FOCUSED=["vs001:db:migrate","vs001:fixtures:load","vs001:fixtures:cleanup","vs001:test:api","vs001:test:web","vs001:test:not-found","vs001:audit:disclosure","vs001:test:consistency","vs001:test:db-integrity","vs001:audit:docker","vs001:evidence:validate","vs001:bootstrap:clean-checkout"]
MIGRATION_MAPPING_IDS={
 "ACL-DEC001-STOREFRONT_CATALOG_CONTEXT_VALID","ACL-DEC001-PUBLICATION_ACTIVE",
 "ACL-DEC002-PRICE_STOREFRONT_SCOPED","ACL-DEC003-SLUG_UNIQUE_WITHIN_STOREFRONT",
 "ACL-DEC003-RESPONSE_HAS_OPAQUE_CANONICAL_IDENTITY",
 "IMPL-V23-P2D-VS001-IMPLEMENTATION-DEC-005","IMPL-V23-P2D-VS001-IMPLEMENTATION-DEC-006",
 "IMPL-V23-P2D-VS001-IMPLEMENTATION-DEC-007","IMPL-V23-P2D-VS001-IMPLEMENTATION-DEC-008"
}
BINDING_EXECUTION={
 "V23-P2D-VS001-IMPLEMENTATION-DEC-001":{"commands":["vs001:test:api","vs001:test:not-found","vs001:evidence:validate","vs001:bootstrap:clean-checkout"],"batches":["B2","B4","B6","B7"]},
 "V23-P2D-VS001-IMPLEMENTATION-DEC-002":{"commands":["vs001:test:api","vs001:test:web","vs001:test:consistency","vs001:evidence:validate"],"batches":["B2","B4","B5","B6"]},
 "V23-P2D-VS001-IMPLEMENTATION-DEC-003":{"commands":["vs001:test:api","vs001:test:consistency","vs001:test:db-integrity","vs001:evidence:validate"],"batches":["B2","B3","B4","B6"]},
 "V23-P2D-VS001-IMPLEMENTATION-DEC-004":{"commands":["vs001:test:api","vs001:test:web","vs001:test:not-found","vs001:audit:disclosure","vs001:evidence:validate"],"batches":["B2","B4","B5","B6"]},
 "V23-P2D-VS001-IMPLEMENTATION-DEC-005":{"commands":["vs001:db:migrate","vs001:test:db-integrity","vs001:test:api","vs001:test:consistency","vs001:evidence:validate"],"batches":["B1","B2","B3","B4","B6"]},
 "V23-P2D-VS001-IMPLEMENTATION-DEC-006":{"commands":["vs001:db:migrate","vs001:fixtures:load","vs001:fixtures:cleanup","vs001:test:db-integrity","vs001:evidence:validate"],"batches":["B1","B3","B6"]},
 "V23-P2D-VS001-IMPLEMENTATION-DEC-007":{"commands":["vs001:db:migrate","vs001:fixtures:load","vs001:fixtures:cleanup","vs001:test:db-integrity","vs001:audit:docker","vs001:bootstrap:clean-checkout"],"batches":["B1","B6","B7"]},
 "V23-P2D-VS001-IMPLEMENTATION-DEC-008":{"commands":["vs001:db:migrate","vs001:test:db-integrity","vs001:test:api","vs001:test:not-found","vs001:test:consistency","vs001:evidence:validate"],"batches":["B1","B3","B4","B6"]},
 "V23-P2D-VS001-IMPLEMENTATION-DEC-009":{"commands":["vs001:test:api","vs001:audit:disclosure","vs001:evidence:validate"],"batches":["B2","B4","B6"]},
 "V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-001":{"commands":["vs001:test:api","vs001:test:web","vs001:test:consistency","vs001:evidence:validate"],"batches":["B2","B4","B5","B6"]},
 "V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-002":{"commands":["vs001:db:migrate","vs001:test:db-integrity","vs001:test:api","vs001:test:consistency","vs001:evidence:validate","vs001:bootstrap:clean-checkout"],"batches":["B1","B3","B4","B6","B7"]}
}

def text(v):return json.dumps(v,ensure_ascii=False,sort_keys=True)
def profile(mid,rid,rule,semantic,mtype):
    s=(rule+" "+rid+" "+text(semantic)).upper(); owners=[]
    def add(*xs):
        for x in xs:
            if x not in owners:owners.append(x)
    if any(k in s for k in ["MIGRATION","JSONB","RELATIONAL","UUIDV7","UNIQUE_WITHIN","VERSION","REFERENCE","CATALOG","PUBLICATION","REVISION"]):add("database/config/schema.prisma","apps/api/src/vs001/public-catalog.repository.ts","tests/vs001/data/public-catalog-integrity.test.ts")
    if any(k in s for k in ["ELIGIB","ACTIVE","WINDOW","VALIDATION_PASS","SCOPE","EXCLUDE_FROM_PUBLIC_LIST"]):add("apps/api/src/vs001/eligibility-resolver.ts","apps/api/src/vs001/public-catalog.repository.ts","tests/vs001/api/public-catalog.integration.test.ts")
    if any(k in s for k in ["PRICE","CURRENCY","COST","MARGIN"]):add("apps/api/src/vs001/price-resolver.ts","tests/vs001/data/public-catalog-integrity.test.ts")
    if any(k in s for k in ["SLUG","NOT_FOUND","404","UNKNOWN","MALFORMED","WRONG_STOREFRONT","HEADER"]):add("packages/contracts/src/vs001/public-catalog.ts","apps/api/src/vs001/public-catalog.controller.ts","tests/vs001/api/public-catalog.integration.test.ts")
    if any(k in s for k in ["LIST_","DETAIL_","LOCALIZED","IMAGE","DISPLAY","UI","ACCESSIB","LOADING","EMPTY"]):add("packages/contracts/src/vs001/public-catalog.ts","apps/web/src/vs001/public-catalog-view.tsx","tests/vs001/browser/public-catalog.spec.ts")
    if any(k in s for k in ["SUPPLIER","INTERNAL","DISCLOS","CREDENTIAL","REASON","AUDIT","CORRELATION"]):add("apps/api/src/vs001/public-catalog-audit.ts","tests/vs001/security/public-catalog-disclosure.test.ts")
    if not owners:add("apps/api/src/vs001/public-catalog.service.ts","tests/vs001/api/public-catalog.integration.test.ts")
    if mid=="ACL-DEC002-NO_DATABASE_SCHEMA_DECISION":
        owners=["packages/contracts/src/vs001/public-catalog.ts","tests/vs001/data/public-catalog-integrity.test.ts"]
    # One primary closure batch per mapping.  The selection is semantic rather
    # than prefix-only: retained cross-layer contracts close in clean checkout;
    # disclosure/consistency rules close in evidence; UI presentation closes in
    # browser work; transport/slug rules close in API; persistence rules close
    # in data; and public schema rules close in contracts.
    if mid in MIGRATION_MAPPING_IDS:batch="B1"
    elif mid=="ACL-DEC002-NO_DATABASE_SCHEMA_DECISION":batch="B2"
    elif mtype=="retained_requirement":batch="B7"
    elif any(k in s for k in ["SUPPLIER","DISCLOS","CREDENTIAL","COST","MARGIN","LIST_DETAIL","CONSISTEN","NO_PROMOTION","NO_DISCOUNT","NO_TAX","NO_CART"]):batch="B6"
    elif any(k in s for k in ["ACCESSIB","LOADING","EMPTY","BROWSER","UI STATE","PUBLIC IMAGE","ALT TEXT"]):batch="B5"
    elif any(k in s for k in ["NOT_FOUND","404","UNKNOWN_SLUG","MALFORMED_SLUG","WRONG_STOREFRONT","ROUTE","HTTP","SLUG"]):batch="B4"
    elif any(k in s for k in ["ELIGIB","ACTIVE","WINDOW","VALIDATION_PASS","SCOPE","PRICE_RESOL","EVALUATION","SNAPSHOT"]):batch="B3"
    elif any(k in s for k in ["DTO","SCHEMA","LIST_","DETAIL_","LOCALIZED","DISPLAY","CURRENCY"]):batch="B2"
    elif any("database/" in x for x in owners):batch="B1"
    else:batch="B6"
    commands=["vs001:fixtures:load","vs001:fixtures:cleanup","vs001:evidence:validate","vs001:audit:docker","vs001:bootstrap:clean-checkout"]
    if any("database/" in x or "repository" in x or "resolver" in x for x in owners):commands+= ["vs001:test:db-integrity"]
    if any("controller" in x or "service.ts" in x for x in owners):commands+=["vs001:test:api"]
    if any("apps/web" in x for x in owners):commands+=["vs001:test:web"]
    if any(k in s for k in ["NOT_FOUND","404","UNKNOWN","MALFORMED","WRONG_STOREFRONT","UNPUBLISHED","INACTIVE"]):commands+=["vs001:test:not-found"]
    if any(k in s for k in ["LIST_DETAIL","CONSISTEN","SNAPSHOT","REVISION","CURSOR"]):commands+=["vs001:test:consistency"]
    if any(k in s for k in ["SUPPLIER","INTERNAL","DISCLOS","CREDENTIAL","REASON","COST","MARGIN"]):commands+=["vs001:audit:disclosure"]
    if mid in MIGRATION_MAPPING_IDS:commands+=["vs001:db:migrate"]
    if mid=="ACL-DEC002-NO_DATABASE_SCHEMA_DECISION":commands=[x for x in commands if x not in ["vs001:db:migrate","vs001:test:web"]]
    return owners,list(dict.fromkeys(commands)),batch

def make_mapping(mid,mtype,authority,rid,semantic,fixture_source,precondition,action,observation,expected,prohibited,boundary):
    rule=authority.get("rule_id","");owners,commands,batch=profile(mid,rid,rule,semantic,mtype)
    fixture={"fixture_id":"FX-"+mid,"semantic_state":fixture_source,"ownership_token":"vs001-${RUN_ID}-"+mid,"isolation":"dedicated rows in disposable PostgreSQL; never shared production or commissioning data","state_authority":"fixture loader receipt plus independent PostgreSQL query","runtime_status":"PLANNED_NOT_EXECUTED"}
    channels=[];resources=[]
    if any(x.startswith("database/") or "repository" in x or "resolver" in x for x in owners):channels.append("independent PostgreSQL as-of query over rows bearing "+fixture["ownership_token"]);resources.append("versioned PostgreSQL fixture rows for "+mid)
    if any(x.startswith("apps/api/") or x.startswith("packages/contracts/") for x in owners):channels.append("raw black-box HTTP status/header/body captured for "+mid);resources.append("run-owned API process and correlation records for "+mid)
    if any(x.startswith("apps/web/") for x in owners):channels.append("browser DOM/accessibility-tree and network capture for "+mid);resources.append("isolated browser context for "+mid)
    if any("security" in x or "audit" in x for x in owners):channels.append("raw disclosure/redaction scan of public response and protected audit record for "+mid);resources.append("redacted audit evidence owned by "+mid)
    obs={"observed_subject":rid+" / "+(rule or mtype),"channel":channels,"independent_source":observation,"expected_authority":"accepted Git object at "+authority["fingerprint"],"observed_authority":"real process bytes plus independently queried state bearing "+fixture["ownership_token"],"comparison":"mapping "+mid+" compares the channel observations to its authority assertion while forbidding expected-value replay","failure_condition":"any channel disagrees, leaks a prohibited value, lacks correlation, or cannot be reproduced from the owned fixture","expected_derived":False}
    cleanup={"cleanup_id":"CLEAN-"+mid,"resources":resources,"success":"for "+mid+", delete owned rows in FK-safe order, close its browser/API handles, then query every listed resource class and verify zero owned residue","failure":"for "+mid+", execute the same idempotent resource-specific cleanup in finally and preserve only the redacted evidence index","prohibited":"for "+mid+", never retain controlled fixtures, delete shared commissioning resources, or treat residual resources as PASS"}
    return {"mapping_id":mid,"mapping_type":mtype,"authority":authority,"semantic_assertion":semantic,"owner_paths":owners,"controlled_fixture":fixture,"preconditions":precondition,"action":action,"independent_observation":obs,"expected_outcome":expected,"prohibited_outcome":prohibited,"boundary_negative_case":boundary,"evidence_contract":{"evidence_id":"EVID-"+mid,"artifacts":["owned fixture receipt for "+mid,*channels,"independent comparison result for "+mid,"resource-specific cleanup receipt for "+mid],"correlation":"server correlation UUID plus fixture ownership token "+fixture["ownership_token"],"runtime_status":"PLANNED_NOT_EXECUTED"},"cleanup_contract":cleanup,"validation_command_ids":commands,"implementation_batch_ids":[batch],"runtime_evidence_status":"NOT_EXECUTED","implementation_authorized":False}

def mappings(a,r):
    out=[];rb={x["requirement_id"]:x for x in r["records"]}
    for x in a["retained_contracts"]:
        rid=x["requirement_id"];rec=rb[rid];c=rec["acceptance_contract"];auth={"lifecycle":"RENDERER_C2_ACCEPTED","commit":x["signed_legacy_contract_provenance"]["renderer_accepted_commit"],"git_path":x["signed_legacy_contract_provenance"]["repository_path"],"json_path":x["signed_legacy_contract_provenance"]["canonical_json_path"],"fingerprint":rec["contract_sha256"]}
        out.append(make_mapping("REQ-"+rid,"retained_requirement",auth,rid,c,c.get("fixture_contract",c.get("typed_contract_ast",{})),c.get("preconditions",c.get("typed_contract_ast",{})),c.get("action",c.get("typed_contract_ast",{})),c.get("required_evidence",c),c.get("positive_oracle",c),c.get("negative_oracle",c),c.get("boundary_oracle",c)))
    contracts=a["batch_1_contracts"]+a["batch_2_contracts"]+a["batch_3_contracts"]
    for c in contracts:
        rid=c["requirement_id"];base={"lifecycle":"ACCEPTANCE_ELABORATION_C2_R2_ACCEPTED","commit":"4a0ff5700554023b30d9a6dba01d80d1dbc78867","git_path":APATH,"json_path":"contracts/"+rid,"fingerprint":c["source_fingerprint"]}
        out.append(make_mapping("REQ-"+rid,"elaborated_requirement",base,rid,c["source_statement"],c["controlled_fixtures"],c["preconditions"],[x["trigger_action"] for x in c["acceptance_criteria"]],[x["observed_evidence_authority"] for x in c["acceptance_criteria"]],c["positive_outcomes"],c["prohibited_outcomes"],c["boundary_cases"]))
        for i,o in enumerate(c["obligation_mapping"]):
            auth={**base,"json_path":f"contracts/{rid}/obligation_mapping/{i}","fingerprint":digest(o)};criteria=[x for x in c["acceptance_criteria"] if x["criterion_id"] in o["criterion_ids"]]
            out.append(make_mapping(f"OBL-{rid}-{o['obligation_id']}","source_obligation",auth,rid,o["source_obligation"],c["controlled_fixtures"],c["preconditions"],o["source_obligation"],[x["observed_evidence_authority"] for x in criteria],[x["expected_semantic_outcome"] for x in criteria],[x["prohibited_outcome"] for x in criteria],c["boundary_cases"]))
        for i,k in enumerate(c["acceptance_criteria"]):
            auth={**base,"json_path":f"contracts/{rid}/acceptance_criteria/{i}","fingerprint":digest(k)}
            out.append(make_mapping(f"CRT-{rid}-{k['criterion_id']}","source_criterion",auth,rid,k["expected_semantic_outcome"],k["evidence_references"],k["actor_context"],k["trigger_action"],k["observed_evidence_authority"],k["expected_semantic_outcome"],k["prohibited_outcome"],{"left":k["left_boundary"],"right":k["right_boundary"],"negative":k["negative_case"]}))
    for i,c in enumerate(a["decision_derived_acceptance_clauses"]):
        rid=c["affected_requirement_contexts"][0];auth={"lifecycle":"ACCEPTANCE_DECISION_C1_ACCEPTED","commit":c["authority_commit"],"git_path":c["authority_git_path"],"json_path":c["authority_json_path"],"fingerprint":c["authoritative_rule_fingerprint"],"rule_id":c["authoritative_rule_id"],"selected_option_id":c["selected_option_id"]}
        out.append(make_mapping("ACL-"+c["clause_id"],"decision_clause",auth,rid,c["concrete_assertion_or_prohibition"],c["controlled_fixtures"],c["preconditions"],c["concrete_assertion_or_prohibition"],c["observable_evidence_contract"],c["concrete_assertion_or_prohibition"],c["failure_semantics"],c["boundary_cases"]))
    return out

IMPL_SELECTED={"V23-P2D-VS001-IMPLEMENTATION-DEC-001":"OPT-V1-STOREFRONT-RESOURCE-HIERARCHY","V23-P2D-VS001-IMPLEMENTATION-DEC-002":"OPT-BCP47-REQUEST-THEN-STOREFRONT-DEFAULT","V23-P2D-VS001-IMPLEMENTATION-DEC-003":"OPT-OPAQUE-CURSOR-SLUG-IDENTITY-ORDER","V23-P2D-VS001-IMPLEMENTATION-DEC-004":"OPT-EXPLICIT-DATA-META-DTO","V23-P2D-VS001-IMPLEMENTATION-DEC-005":"OPT-STOREFRONT-ENTRY-SLUG-UUIDV7-PUBLIC-ID","V23-P2D-VS001-IMPLEMENTATION-DEC-006":"OPT-HYBRID-RELATIONAL-CORE-JSONB-SPECIFICATION","V23-P2D-VS001-IMPLEMENTATION-DEC-007":"OPT-FORWARD-MIGRATION-SEPARATE-FIXTURE-LOADER","V23-P2D-VS001-IMPLEMENTATION-DEC-008":"OPT-REQUEST-TIMESTAMP-REPEATABLE-READ-SNAPSHOT","V23-P2D-VS001-IMPLEMENTATION-DEC-009":"OPT-SERVER-CORRELATION-ID-ALLOWLISTED-AUDIT"}
CONT_SELECTED={"V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-001":"OPT-QORDER-EXACT-THEN-STOREFRONT-DEFAULT","V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-002":"OPT-STATELESS-LOGICAL-REVISION-CURSOR"}

def binding(did,oid,option,authority,kind):
    n=did[-3:]; owners={"001":["packages/contracts/src/vs001/public-catalog.ts","apps/api/src/vs001/public-catalog.controller.ts","apps/web/src/vs001/public-catalog-client.ts","tests/vs001/api/public-catalog.integration.test.ts","tests/vs001/browser/public-catalog.spec.ts"],"002":["packages/contracts/src/vs001/public-catalog.ts","apps/api/src/vs001/public-catalog.service.ts","apps/web/src/vs001/public-catalog-client.ts","tests/vs001/api/public-catalog.integration.test.ts","tests/vs001/browser/public-catalog.spec.ts"],"003":["packages/contracts/src/vs001/public-catalog.ts","apps/api/src/vs001/public-catalog.repository.ts","apps/api/src/vs001/public-catalog.service.ts","tests/vs001/api/public-catalog.integration.test.ts","tests/vs001/data/public-catalog-integrity.test.ts"],"004":["packages/contracts/src/vs001/public-catalog.ts","apps/api/src/vs001/public-catalog.controller.ts","apps/web/src/vs001/public-catalog-view.tsx","tests/vs001/security/public-catalog-disclosure.test.ts"],"005":["database/config/schema.prisma","apps/api/src/vs001/public-catalog.repository.ts","packages/contracts/src/vs001/public-catalog.ts","tests/vs001/data/public-catalog-integrity.test.ts"],"006":["database/config/schema.prisma","database/migrations/20260719000000_vs001_public_catalog/migration.sql","apps/api/src/vs001/public-catalog.repository.ts","tests/vs001/data/public-catalog-integrity.test.ts"],"007":["database/migrations/20260719000000_vs001_public_catalog/migration.sql","database/seed-mechanism/vs001-fixtures.ts","scripts/vs001/fixtures.mjs","scripts/vs001/cleanup.mjs","tests/vs001/data/public-catalog-integrity.test.ts"],"008":["database/config/schema.prisma","apps/api/src/vs001/public-catalog.repository.ts","apps/api/src/vs001/eligibility-resolver.ts","apps/api/src/vs001/price-resolver.ts","tests/vs001/data/public-catalog-integrity.test.ts","tests/vs001/api/public-catalog.integration.test.ts"],"009":["packages/contracts/src/vs001/public-catalog.ts","apps/api/src/vs001/public-catalog.controller.ts","apps/api/src/vs001/public-catalog-audit.ts","tests/vs001/security/public-catalog-disclosure.test.ts","scripts/vs001/validate-evidence.mjs"]}[n]
    if kind=="continuity" and did.endswith("001"):owners=["packages/contracts/src/vs001/public-catalog.ts","apps/api/src/vs001/public-catalog.service.ts","apps/web/src/vs001/public-catalog-client.ts","tests/vs001/api/public-catalog.integration.test.ts","tests/vs001/browser/public-catalog.spec.ts"]
    if kind=="continuity" and did.endswith("002"):owners=["database/config/schema.prisma","database/migrations/20260719000000_vs001_public_catalog/migration.sql","apps/api/src/vs001/public-catalog.repository.ts","apps/api/src/vs001/public-catalog.service.ts","tests/vs001/data/public-catalog-integrity.test.ts","tests/vs001/api/public-catalog.integration.test.ts","scripts/vs001/cleanup.mjs"]
    observation={
      "V23-P2D-VS001-IMPLEMENTATION-DEC-001":"Issue versioned Storefront-scoped list/detail requests and compare route parameters, response identities and uniform negative routes.",
      "V23-P2D-VS001-IMPLEMENTATION-DEC-002":"Send ordered Accept-Language fixtures and compare Content-Language plus localized list/detail fields to independently queried Storefront locale support.",
      "V23-P2D-VS001-IMPLEMENTATION-DEC-003":"Traverse opaque cursors while querying the slug/public-identity order tuple independently and probing malformed or context-reused cursors.",
      "V23-P2D-VS001-IMPLEMENTATION-DEC-004":"Capture raw success/error DTO and media fields, then scan schema and bytes for absent internal fields and undeclared envelope members.",
      "V23-P2D-VS001-IMPLEMENTATION-DEC-005":"Query UUIDv7 and Storefront-scoped slug constraints independently, then compare only the approved opaque public identity and slug at API/UI boundaries.",
      "V23-P2D-VS001-IMPLEMENTATION-DEC-006":"Inspect migration history, relational keys and validated JSONB specification while proving lifecycle, price and identity facts are not hidden in JSONB.",
      "V23-P2D-VS001-IMPLEMENTATION-DEC-007":"Run forward migration and separate owned fixture loader/cleanup, proving production seed behavior never owns acceptance fixtures.",
      "V23-P2D-VS001-IMPLEMENTATION-DEC-008":"Hold an injected UTC evaluation instant inside each request-local repeatable-read transaction and compare eligibility/price facts under concurrent changes.",
      "V23-P2D-VS001-IMPLEMENTATION-DEC-009":"Probe caller correlation spoofing, DTO allowlist, public body/header redaction and protected audit correlation without exposing internal causes.",
      "V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-001":"Exercise q-order, equal-q header order, exact support, wildcard, q=0, malformed members and Storefront default across list/detail responses.",
      "V23-P2D-VS001-IMPLEMENTATION-CONTRACT-CONTINUITY-DEC-002":"Page across inserts, updates, publication/price changes and retirement using a tamper-protected Storefront-bound logical-revision cursor in new request transactions."
    }[did]
    selected=option["selected_option"]
    fixture={"fixture_id":"FX-BIND-"+did,"positive_authority_state":selected.get("contract",selected.get("algorithm",{})),"negative_state":"one controlled violation of "+oid+" plus an unchanged control fixture","boundary_state":selected.get("boundaries",selected.get("non_inferences",option.get("non_inferences",[]))),"ownership_token":"vs001-${RUN_ID}-BIND-"+did,"independent_control":"owned fixture receipt and distinct PostgreSQL/API/browser observation channels for "+did,"runtime_status":"PLANNED_NOT_EXECUTED"}
    execution=BINDING_EXECUTION[did]
    return {"binding_id":"BIND-"+did,"decision_id":did,"selected_option_id":oid,"authority":authority,"authority_owner":"ACCEPTED_DECISION_GIT_OBJECT","canonical_option_payload":option,"owner_paths":owners,"controlled_fixtures":fixture,"preconditions":["accepted option and detached selection resolve from Git objects","all named cross-layer owners remain planned and absent in contract authoring"],"positive_observation":observation,"expected_outcome":"Every canonical selected-option rule is observed through the named owners and exact command subset for "+did,"negative_boundaries":"For "+did+", compare the owned positive fixture with its option-specific prohibited state and boundary while keeping unrelated controls unchanged.","prohibited_outcomes":["canonical option weakened or extended","single irrelevant owner substitutes for cross-layer enforcement","expected authority is replayed as observation","runtime PASS or implementation appears before approval"],"commands":execution["commands"],"batches":execution["batches"],"cleanup":{"owned_rows":"delete rows carrying vs001-${RUN_ID}-BIND-"+did,"processes":"stop only API/browser handles opened for "+did,"docker":"remove only resources labeled for "+did+" and compare before/after inventory","prohibited":"retain this binding's fixtures or delete shared commissioning resources"},"implementation_authorized":False,"runtime_evidence_status":"NOT_EXECUTED"}

def decision_bindings(impl,cont):
    out=[]
    for d in impl["decisions"]:
        oid=IMPL_SELECTED[d["decision_id"]];o=next(x for x in d["options"] if x["option_id"]==oid);payload={"decision_id":d["decision_id"],"selected_option":o,"non_inferences":d["non_inferences"]}
        out.append(binding(d["decision_id"],oid,payload,{"lifecycle":"IMPLEMENTATION_DECISION_C1_ACCEPTED","commit":"5b4159cdec2b93e94a65690314624518d1ddc94e","git_path":IPATH,"fingerprint":digest(payload)},"implementation"))
    for d in cont["decisions"]:
        oid=CONT_SELECTED[d["decision_id"]];o=next(x for x in d["options"] if x["option_id"]==oid);payload={"decision_id":d["decision_id"],"selected_option":o}
        out.append(binding(d["decision_id"],oid,payload,{"lifecycle":"CONTINUITY_DECISION_C1_ACCEPTED","commit":HEAD,"git_path":CPATH,"fingerprint":digest(payload)},"continuity"))
    return out

def locale_fixtures():
    def case(fid,header,supported,default,expected,behavior):
        return {"fixture_id":fid,"raw_accept_language":header,"supported_locales":supported,"storefront_default":default,"expected_resolved_locale":expected,"expected_behavior":behavior,"api_observation":"raw Content-Language plus localized list/detail body under vs001:test:api","ui_observation":"browser network response and rendered locale under vs001:test:web","command_ids":["vs001:test:api","vs001:test:web","vs001:test:consistency"],"isolation_cleanup":"locale catalog rows carry "+fid+" ownership token and are deleted after list/detail comparison","runtime_status":"PLANNED_NOT_EXECUTED"}
    return [
      case("LOC-DUP-DIFFERENT-Q","fr-CA;q=0.4, fr-CA;q=0.9, en-US;q=0.8",["fr-CA","en-US"],"en-US","fr-CA","higher-q duplicate wins; duplicate presence does not create ambiguity"),
      case("LOC-DUP-EQUAL-Q","fr-CA;q=0.8, fr-CA;q=0.8, en-US;q=0.7",["fr-CA","en-US"],"en-US","fr-CA","equal duplicate retains original order and resolves the same exact tag"),
      case("LOC-EQUAL-Q-ORDER","fr-CA;q=0.8, en-US;q=0.8",["fr-CA","en-US"],"en-US","fr-CA","original header order breaks equal-q tie"),
      case("LOC-MALFORMED-Q","fr-CA;q=bogus, en-US;q=0.7",["fr-CA","en-US"],"fr-CA","en-US","malformed member is ignored; next acceptable exact range wins"),
      case("LOC-OUT-OF-RANGE-Q","fr-CA;q=1.5",["fr-CA","en-US"],"en-US","en-US","out-of-range q makes the member malformed, so Storefront default wins"),
      case("LOC-Q-ZERO","fr-CA;q=0, en-US;q=0.5",["fr-CA","en-US"],"fr-CA","en-US","q=0 is never selectable"),
      case("LOC-WILDCARD","*;q=1",["fr-CA","en-US"],"en-US","en-US","wildcard never chooses an arbitrary locale; Storefront default wins"),
      case("LOC-UNSUPPORTED","zz-ZZ;q=1",["fr-CA","en-US"],"en-US","en-US","unsupported exact range falls back to Storefront default"),
      case("LOC-MISSING-HEADER",None,["fr-CA","en-US"],"fr-CA","fr-CA","missing header uses Storefront default"),
      case("LOC-NO-SUBTAG-FALLBACK","en;q=1",["en-US","fr-CA"],"fr-CA","fr-CA","en does not match en-US; no language-subtag fallback"),
      case("LOC-LIST-DETAIL-CONSISTENCY","fr-CA;q=1",["fr-CA","en-US"],"en-US","fr-CA","list and detail expose identical Content-Language and localized values")
    ]

def design(cont):
    loc=next(o for d in cont["decisions"] if d["decision_id"].endswith("001") for o in d["options"] if o["option_id"]==CONT_SELECTED[d["decision_id"]])
    cur=next(o for d in cont["decisions"] if d["decision_id"].endswith("002") for o in d["options"] if o["option_id"]==CONT_SELECTED[d["decision_id"]])
    return {"api":{"routes":["GET /api/v1/storefronts/{storefront_slug}/products","GET /api/v1/storefronts/{storefront_slug}/products/{public_slug}"],"list_envelope":"{data:[PublicProductListItem],meta:{page:{next_cursor,limit,snapshot_id}}}","detail_envelope":"{data:PublicProductDetail}","not_found":{"status":404,"body":{"error":{"code":"PRODUCT_NOT_FOUND","message":"Product not found"}}},"invalid_cursor":{"status":400,"body":{"error":{"code":"INVALID_CURSOR","message":"Invalid cursor"}}},"correlation":"server UUID in X-Correlation-Id; never trust caller value"},
      "data":{"tables":["product","product_version","storefront","catalog","catalog_entry","product_publication","publication_validation","product_price","product_localization","product_media","catalog_revision"],"identity":"immutable UUIDv7 public_product_id; unique(storefront_id,public_slug); internal/Supplier IDs never public","jsonb":"schema-versioned validated public specification only; identity/lifecycle/publication/price remain relational","revision_invariants":["monotonic logical catalog_revision allocated transactionally for public-affecting changes","versioned facts carry valid_from_revision inclusive and valid_to_revision exclusive","retirement/deletion uses retained tombstone/version history through cursor expiry","as-of query uses revision plus evaluation timestamp for publication/price/effective predicates","each page opens its own request-local REPEATABLE READ transaction; no PostgreSQL snapshot spans requests"],"migration":"forward-only schema migration; no fixture rows or production seed coupling"},
      "ui":{"routes":["/catalog","/catalog/[public_slug]"],"states":["loading","success","empty","uniform unavailable","non-disclosing error"],"contract":"render allowlisted DTO only; Content-Language, identity, slug and price consistent with API snapshot","prohibited":["cart/purchase","inventory","promotion/tax","recommendation/waitlist","admin publishing","internal diagnostics"]},
      "security_observability":{"projection":"explicit DTO allowlist; never serialize persistence objects","redaction":["Supplier identity/reference","cost/margin","credentials/secrets","internal IDs/storage paths","internal failure reason from public body/headers"],"audit":"protected correlation/operation/Storefront public identity/internal reason only","cursor_integrity":"authenticated opaque cursor; tampered, expired, wrong-context and unavailable revision share INVALID_CURSOR"},
      "locale":{"selected_option":loc,"list_detail_consistency":"one resolved locale per request; Content-Language exposes it on list, detail and uniform not-found; list/detail evidence compares same requested context","fixtures":locale_fixtures()},
      "cursor_continuity":{"selected_option":cur,"cursor_fields":["version","storefront public identity","resolved locale","page limit","public_slug","opaque public_product_id","UTC evaluation instant","logical catalog revision","15-minute expiry","integrity tag"],"concurrent_fixtures":["insert after revision excluded","update after revision returns prior version","publication change after revision uses prior publication","price change after revision uses prior price","retirement/deletion after revision retains prior as-of state until expiry","cross-Storefront reuse returns uniform INVALID_CURSOR"],"request_boundary":"new PostgreSQL REPEATABLE READ transaction per page; logical revision and evaluation instant provide continuity"},
      "path_policy":{"allowed":ALLOWED,"protected":PROTECTED,"shared_file_rule":"app.module.ts, contracts index, schema.prisma and package.json permit only VS001-scoped additions; commissioning behavior must remain byte/behavior compatible"}}

def commands(maps,binds):
    inherited=[
      ("commissioning:lint","corepack pnpm lint","eslint --config scripts/commissioning/eslint.config.mjs scripts/commissioning/*.mjs && node scripts/commissioning/audit-boundaries.mjs"),
      ("commissioning:typecheck","corepack pnpm typecheck","corepack pnpm --filter @ysim/contracts build && corepack pnpm -r --if-present typecheck && tsc -p database/config/tsconfig.json --noEmit"),
      ("commissioning:test","corepack pnpm test","vitest run tests/commissioning"),
      ("commissioning:build","corepack pnpm build","corepack pnpm -r --if-present build"),
      ("commissioning:smoke:api","corepack pnpm smoke:api","node scripts/commissioning/smoke-api.mjs"),
      ("commissioning:smoke:web","corepack pnpm smoke:web","node scripts/commissioning/smoke-web.mjs"),
      ("commissioning:db:migrate:verify","corepack pnpm db:migrate:verify","node scripts/commissioning/db-migrate-verify.mjs"),
      ("commissioning:bootstrap:clean-checkout","corepack pnpm bootstrap:clean-checkout","node scripts/commissioning/bootstrap-clean-checkout.mjs"),
      ("commissioning:audit:versions","corepack pnpm audit:versions","node scripts/commissioning/audit-versions.mjs"),
      ("commissioning:audit:boundaries","corepack pnpm audit:boundaries","node scripts/commissioning/audit-boundaries.mjs")]
    required={
      "commissioning:lint":["B2","B4","B5","B6","B7"],"commissioning:typecheck":["B2","B3","B4","B5","B6","B7"],
      "commissioning:test":["B3","B4","B5","B6","B7"],"commissioning:build":["B4","B5","B7"],
      "commissioning:smoke:api":["B4","B6","B7"],"commissioning:smoke:web":["B5","B6","B7"],
      "commissioning:db:migrate:verify":["B1","B6","B7"],"commissioning:bootstrap:clean-checkout":["B7"],
      "commissioning:audit:versions":["B1","B7"],"commissioning:audit:boundaries":["B1","B2","B3","B4","B5","B6","B7"]}
    out=[{"command_id":i,"command":c,"command_class":"INHERITED_COMMISSIONING_FOUNDATION_GATE","authority":{"accepted_commit":"f7f2aeca3c1643996f77dec1b0b5caae22363ddc","git_path":"package.json","script_name":i.split(":",1)[1],"accepted_script_definition":definition},"foundation_gate_ids":["I1-R1-"+i.split(":",1)[1].upper().replace(":","-")],"foundation_purpose":"Preserve accepted commissioning "+i+" behavior; this command alone does not prove a VS001 acceptance mapping.","acceptance_evidence":False,"required_by_batches":required[i],"real_process":True,"success_exit":0,"evidence_output":"accepted commissioning foundation evidence for "+i,"failure":"nonzero on any failed foundation assertion","cleanup":"accepted commissioning owned-resource cleanup; no VS001 fixture ownership"} for i,c,definition in inherited]
    focused_contract={
      "vs001:db:migrate":("B1","apply the forward-only VS001 migration to owned PostgreSQL 18.4 and query migration history plus declared constraints","migration history, PostgreSQL constraint/index inventory and schema diff for the owned database","drop only the disposable database or schema created for migration verification; never retain fixture rows or roll back shared migrations"),
      "vs001:fixtures:load":("B1","load deterministic run-owned Product, Catalog, Storefront, revision, publication and price fixtures through the separate fixture loader","fixture receipt plus independent PostgreSQL count and ownership-token query","delete only rows bearing the run ownership token in foreign-key-safe order"),
      "vs001:fixtures:cleanup":("B1","execute idempotent cleanup for every run-owned fixture and process resource","before/after PostgreSQL, process, browser and Docker inventory proving zero owned residue","repeat resource-specific cleanup on failure; never delete shared commissioning resources"),
      "vs001:test:api":("B4","start the real API and issue black-box list/detail requests against owned PostgreSQL fixtures","raw HTTP status, headers, bodies and correlation identities compared with independent database state","stop only the run-owned API process and remove its fixture rows"),
      "vs001:test:web":("B5","start the real web application and browser against the black-box API","browser DOM, accessibility tree, screenshots and network capture","close only the run-owned browser context and web process, then remove its fixture rows"),
      "vs001:test:not-found":("B4","probe every governed unknown, malformed and unavailable slug population","raw 404 PRODUCT_NOT_FOUND status/body/header uniformity matrix plus independent internal-cause fixture query","remove each not-found fixture and its correlation records without preserving diagnostic public output"),
      "vs001:audit:disclosure":("B6","scan public API, browser output, headers and protected audit records for allowlist/redaction boundaries","raw disclosure scan proving Supplier, cost, margin, internal identity and internal reason absence","delete run-owned audit records after retaining only the redacted evidence index"),
      "vs001:test:consistency":("B6","compare list/detail identity, slug, locale and price at one logical revision and evaluation timestamp","independent API-to-API, API-to-browser and API-to-database comparison receipt","remove revision-scoped fixtures and close request/browser handles"),
      "vs001:test:db-integrity":("B3","query real PostgreSQL constraints, as-of revision rows, publication windows and price/currency integrity","SQL assertion output separated from expected contract values","remove owned relational/JSONB/revision fixtures in foreign-key-safe order"),
      "vs001:audit:docker":("B6","compare Docker resources before and after VS001 evidence execution","container, network, volume and image inventory delta proving commissioning resources preserved","remove only resources labeled with the run ownership token"),
      "vs001:evidence:validate":("B6","independently validate every mapping and binding evidence index against raw artifacts","signed evidence-index validation report with missing, conflicting and expected-derived counts","remove transient validation workspace while preserving only the approved redacted evidence bundle"),
      "vs001:bootstrap:clean-checkout":("B7","bootstrap a committed clean checkout and execute the approved implementation-validation command graph","clean-checkout commit/tree, toolchain, command exits and final clean Git status","remove temporary worktree and unreferenced commit resources; preserve no branch or tag")}
    for cid in FOCUSED:
        mids=[m["mapping_id"] for m in maps if cid in m["validation_command_ids"]]
        dbids=[b["binding_id"] for b in binds if cid in b["commands"]]
        owning=sorted({m["implementation_batch_ids"][0] for m in maps if m["mapping_id"] in mids}|{x for b in binds if b["binding_id"] in dbids for x in b["batches"]})
        primary,process,evidence,cleanup=focused_contract[cid]
        out.append({"command_id":cid,"command":"corepack pnpm "+cid,"command_class":"FOCUSED_VS001_TRACEABILITY_COMMAND","mapping_ids":mids,"decision_binding_ids":dbids,"primary_batch_id":primary,"owning_batches":owning,"prerequisites":["approved C1-R2","real PostgreSQL/API/browser as applicable","owned fixture token"],"acceptance_evidence":True,"real_process":True,"process_contract":process,"success_exit":0,"evidence_output":evidence,"failure":"nonzero for missing process/evidence, semantic mismatch, leakage or residual owned resource","cleanup":cleanup,"lifecycle":"approved implementation committed clean checkout"})
    return out

def batches(maps,binds,cmds):
    names={"B1":"Database migration and controlled fixtures","B2":"Public contracts and schemas","B3":"Persistence, eligibility, price and audit resolution","B4":"Public list/detail API","B5":"Web list/detail UI","B6":"Cross-layer evidence and negative tests","B7":"Committed clean-checkout reproduction"}
    pathsets={"B1":[p for p in ALLOWED if p.startswith("database/") or p in ["scripts/vs001/fixtures.mjs","scripts/vs001/cleanup.mjs"]],"B2":[p for p in ALLOWED if p.startswith("packages/contracts/")],"B3":[p for p in ALLOWED if p.startswith("apps/api/src/vs001/") and not p.endswith(("controller.ts","service.ts","module.ts"))],"B4":[p for p in ALLOWED if p in ["apps/api/src/app.module.ts","apps/api/src/vs001/public-catalog.module.ts","apps/api/src/vs001/public-catalog.controller.ts","apps/api/src/vs001/public-catalog.service.ts"]],"B5":[p for p in ALLOWED if p.startswith("apps/web/")],"B6":[p for p in ALLOWED if p.startswith("tests/") or p in ["scripts/vs001/validate-evidence.mjs","configs/local/vs001.env.example","package.json"]],"B7":["scripts/vs001/bootstrap-clean-checkout.mjs"]}
    out=[]
    for n,bid in enumerate(names,1):
        mids=[m["mapping_id"] for m in maps if m["implementation_batch_ids"]==[bid]]
        binding_ids=[b["binding_id"] for b in binds if bid in b["batches"]]
        focused_ids=[c["command_id"] for c in cmds if c["command_class"]=="FOCUSED_VS001_TRACEABILITY_COMMAND" and bid in c["owning_batches"]]
        inherited_ids=[c["command_id"] for c in cmds if c["command_class"]=="INHERITED_COMMISSIONING_FOUNDATION_GATE" and bid in c["required_by_batches"]]
        out.append({"batch_id":bid,"order":n,"name":names[bid],"prerequisite_batch_ids":[f"B{x}" for x in range(1,n)],"downstream_batch_ids":[f"B{x}" for x in range(n+1,8)],"allowed_paths":sorted(set(pathsets[bid])),"mapping_ids":mids,"decision_binding_ids":binding_ids,"focused_command_ids":focused_ids,"inherited_foundation_gate_ids":inherited_ids,"completion_gates":{"mapping_gates":[{"mapping_id":mid,"required_commands":next(m["validation_command_ids"] for m in maps if m["mapping_id"]==mid),"required_evidence":"EVID-"+mid} for mid in mids],"decision_binding_gates":[{"binding_id":x,"required_commands":next(b["commands"] for b in binds if b["binding_id"]==x)} for x in binding_ids]},"cleanup":"execute each listed mapping and binding cleanup; verify zero owned residue; no destructive migration rollback","maximum_correction_passes":2,"implementation_authorized":False})
    return out

def render(p):
    sections=[("metadata",{k:p[k] for k in ["candidate_id","status","approval","runtime_evidence_status","implementation_authorized","next_gate","accounting"]}),("api",p["design"]["api"]),("data",p["design"]["data"]),("ui",p["design"]["ui"]),("security_observability",p["design"]["security_observability"]),("locale",p["design"]["locale"]),("cursor_continuity",p["design"]["cursor_continuity"]),("path_policy",p["design"]["path_policy"]),("decision_bindings",p["decision_bindings"]),("traceability_summary",p["traceability_summary"]),("traceability_catalog",p["traceability_mappings"]),("batches",p["implementation_batches"]),("commands",p["commands"]),("non_claims",p["non_claims"])]
    lines=["# VS001 Implementation Contract C1-R2 Candidate",""]
    for name,value in sections:lines += [f"<!-- C1_R2_SECTION:{name} -->",f"## {name}","","```json",json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2),"```",""]
    return "\n".join(lines).rstrip()+"\n"

def build():
    a=git_json(ACCEPTANCE,APATH);r=git_json(RENDERER,RPATH);i=git_json(IMPL_DEC,IPATH);c=git_json(CONT_DEC,CPATH);maps=mappings(a,r)
    if len(maps)!=202:raise RuntimeError(f"acceptance mapping population {len(maps)} != 202")
    # Nine implementation-decision traceability records complete the explicit 211 union.
    binds=decision_bindings(i,c)
    for b in binds[:9]:
        mid="IMPL-"+b["decision_id"];auth=b["authority"]
        maps.append(make_mapping(mid,"implementation_decision",auth,b["decision_id"],b["canonical_option_payload"],b["controlled_fixtures"],b["preconditions"],b["canonical_option_payload"],b["positive_observation"],b["canonical_option_payload"],b["prohibited_outcomes"],b["negative_boundaries"]))
    maps.sort(key=lambda x:x["mapping_id"])
    cmds=commands(maps,binds);bs=batches(maps,binds,cmds);d=design(c)
    p={"candidate_id":"V23-P2D-VS001-IMPLEMENTATION-CONTRACT-C1-R2","supersedes":"V23-P2D-VS001-IMPLEMENTATION-CONTRACT-C1-R1","correction_pass":2,"correction_reason":"EXECUTABLE_COMMAND_AND_BATCH_BINDING_RELEVANCE_GAPS","status":"CANDIDATE","approval":"PENDING_HUMAN_APPROVAL","runtime_evidence_status":"NOT_EXECUTED","implementation_authorized":False,"next_gate":"HUMAN_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_C1_R2_CANDIDATE_REVIEW","governing_head":HEAD,"blocked_candidate_preservation":{"r1":{"ref":"refs/ysim-backups/v2.3/phase-2d-vs001-implementation-contract-c1-r1-final-audit-blocked","object":"9c5733d4927c5eadd359b53fb1cb1bcb7d726a43","tree":"85bea890e4287c5c6926960f9d9d4dd23216375c","recovery":"6/6_BYTE_IDENTICAL","rejection":"EXECUTABLE_COMMAND_AND_BATCH_BINDING_RELEVANCE_GAPS"},"c1":{"ref":"refs/ysim-backups/v2.3/phase-2d-vs001-implementation-contract-c1-final-audit-blocked","object":"7cd340caa03e619de306f17c34aa067c117e437e","tree":"771a8292a5a381a50b963c36a30e55137d1789fb"}},"accounting":{"requirements":25,"retained":9,"elaborated":16,"source_obligations":21,"source_criteria":32,"acceptance_clauses":124,"implementation_decisions":9,"continuity_decisions":2,"traceability_mappings":211,"decision_bindings":11,"focused_commands":12,"inherited_commands":10,"classified_inherited_foundation_gates":10,"unexplained_empty_bindings":0,"floating_focused_commands":0,"commands_falsely_claimed_as_acceptance_evidence":0,"locale_controlled_cases":11,"batches":7,"implementation_changes":0,"runtime_evidence_executed":0},"authorities":{"commissioning":"VALID_APPROVED_PHASE_2D_PRODUCT_IMPLEMENTATION_COMMISSIONING_I1_R1","acceptance_decision":"VALID_APPROVED_PHASE_2D_VS001_ACCEPTANCE_DECISION_C1","acceptance_elaboration":"VALID_APPROVED_PHASE_2D_VS001_ACCEPTANCE_ELABORATION_C2_R2","implementation_decision":"VALID_APPROVED_PHASE_2D_VS001_IMPLEMENTATION_DECISION_C1","continuity_decision":"VALID_APPROVED_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_CONTINUITY_DECISION_C1"},"design":d,"decision_bindings":binds,"traceability_mappings":maps,"traceability_summary":{"mapping_ids":[m["mapping_id"] for m in maps],"mapping_semantic_sha256":{m["mapping_id"]:digest(m) for m in maps},"uncovered":0,"duplicate":0,"generic":0},"commands":cmds,"implementation_batches":bs,"batch_distribution":{"previous":[19,29,30,49,6,69,9],"current":[len(x["mapping_ids"]) for x in bs],"change_reason":"migration-owning mappings move to B1; technology-neutral non-inference remains B2; all other mappings retain semantic primary ownership"},"correction_policy":{"maximum_passes":2,"external_blockers_consume_pass":False,"validator_weakening":False,"scope_expansion":False,"after_pass_2":"new candidate or human decision"},"non_claims":["NOT_VS001_IMPLEMENTATION","NOT_RUNTIME_EVIDENCE","NOT_RUNTIME_ACCEPTANCE","NOT_MIGRATION_OR_FIXTURE_EXECUTION","NOT_API_UI_DATABASE_CHANGE","NOT_BRD_UXF_COMMISSIONING_CHANGE","NOT_YADF_DEPLOYMENT_PRODUCTION_WORK"]}
    return p

def main():
    p=build();JSON_PATH.write_bytes(canonical(p));MD_PATH.write_text(render(p),encoding="utf-8",newline="\n")
    hashes={str(x.relative_to(ROOT)):sha(x.read_bytes()) for x in (MD_PATH,JSON_PATH,BUILDER,VALIDATOR,TESTS)}
    gen=[str(MD_PATH.relative_to(ROOT)),str(JSON_PATH.relative_to(ROOT))];manifest={"candidate_id":p["candidate_id"],"status":"CANDIDATE","approval":"PENDING_HUMAN_APPROVAL","runtime_evidence_status":"NOT_EXECUTED","implementation_authorized":False,"inventory":FILES,"file_sha256_excluding_manifest":hashes,"generated_payload_aggregate":digest([{"path":x,"sha256":hashes[x]} for x in sorted(gen)]),"mapping_catalog_root":digest(p["traceability_summary"]["mapping_semantic_sha256"]),"decision_binding_root":digest({b["binding_id"]:digest(b) for b in p["decision_bindings"]}),"command_catalog_root":digest({c["command_id"]:digest(c) for c in p["commands"]}),"batch_catalog_root":digest({b["batch_id"]:digest(b) for b in p["implementation_batches"]}),"staged_tree":"DETACHED_HUMAN_GATE_VALUE","git_content_aggregate":"DETACHED_HUMAN_GATE_VALUE","self_reference_policy":"manifest excluded from its own per-file domain; staged tree and Git-content aggregate are detached human-gate values"};MANIFEST_PATH.write_bytes(canonical(manifest));print("BUILT_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_C1_R2")
if __name__=="__main__":main()
