#!/usr/bin/env python3
"""Independent validator for VS001 execution-boundary amendment A2."""
from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GIT_ROOT = Path(os.environ.get("A2_GIT_ROOT", ROOT))
GOVERNING_HEAD = "77c25755ece698088820447f92b094594e9e21c4"
CONTRACT_PATH = "docs/baselines/v2.3/phase-2d/vs001-implementation-contract-c1-r2.json"
CANDIDATE_ID = "V23-P2D-VS001-IMPLEMENTATION-CONTRACT-EXECUTION-BOUNDARY-AMENDMENT-A2"
BASE = Path("docs/baselines/v2.3/phase-2d")
JSON_REL = BASE / "vs001-implementation-contract-execution-boundary-amendment-a2.json"
MD_REL = BASE / "VS001_IMPLEMENTATION_CONTRACT_EXECUTION_BOUNDARY_AMENDMENT_A2_CANDIDATE.md"
MANIFEST_REL = BASE / "vs001-implementation-contract-execution-boundary-amendment-a2-manifest.json"
BUILDER_REL = Path("scripts/docs/build-phase-2d-vs001-implementation-contract-execution-boundary-amendment-a2.py")
VALIDATOR_REL = Path("scripts/docs/validate-phase-2d-vs001-implementation-contract-execution-boundary-amendment-a2.py")
TEST_REL = Path("scripts/docs/tests/test-phase-2d-vs001-implementation-contract-execution-boundary-amendment-a2.py")
INVENTORY = [str(x) for x in (MD_REL, JSON_REL, MANIFEST_REL, BUILDER_REL, VALIDATOR_REL, TEST_REL)]
BATCHES = [f"B{i}" for i in range(1, 8)]
EXPECTED_COUNTS = [(28, 28, 28, 0, 0), (28, 28, 56, 0, 0), (26, 54, 82, 0, 0), (48, 130, 130, 0, 0), (6, 105, 136, 0, 0), (66, 211, 211, 0, 0), (9, 0, 211, 211, 211)]
IMMUTABLE_FORBIDDEN = ["pnpm-lock.yaml", "scripts/commissioning/**", "docs/BRD/**", "docs/UXF/**", "docs/baselines/v2.3/**/*APPROVAL*", "factory/**", "knowledge/**", "runtime/**", "tools/ysf/**", "integrations/**", "infrastructure/**", ".git/**"]
B1_KEYS = ["vs001:db:migrate", "vs001:fixtures:load", "vs001:fixtures:cleanup", "vs001:test:db-integrity", "vs001:audit:docker", "vs001:batch:validate", "vs001:batch:clean-checkout"]


class AmendmentError(Exception):
    def __init__(self, code: str, detail: str):
        self.code = code
        self.detail = detail
        super().__init__(f"{code}: {detail}")


def require(condition: bool, code: str, detail: str) -> None:
    if not condition:
        raise AmendmentError(code, detail)


def canonical(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_bytes(commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=GIT_ROOT)


def accepted_contract() -> tuple[dict[str, object], bytes]:
    raw = git_bytes(GOVERNING_HEAD, CONTRACT_PATH)
    return json.loads(raw), raw


def frozen_schedule() -> dict[str, dict[str, object]]:
    return {
        "vs001:db:migrate": {"implementation_owner_batch": "B1", "registration_batch": "B1", "earliest_executable_batch": "B1", "required_evidence_batches": ["B1", "B3", "B6", "B7"], "final_closure_batch": "B7", "prerequisite_commands": ["commissioning:db:migrate:verify"]},
        "vs001:fixtures:load": {"implementation_owner_batch": "B1", "registration_batch": "B1", "earliest_executable_batch": "B1", "required_evidence_batches": ["B1", "B3", "B4", "B5", "B6", "B7"], "final_closure_batch": "B7", "prerequisite_commands": ["vs001:db:migrate"]},
        "vs001:fixtures:cleanup": {"implementation_owner_batch": "B1", "registration_batch": "B1", "earliest_executable_batch": "B1", "required_evidence_batches": ["B1", "B3", "B4", "B5", "B6", "B7"], "final_closure_batch": "B7", "prerequisite_commands": ["vs001:fixtures:load"]},
        "vs001:test:db-integrity": {"implementation_owner_batch": "B1", "registration_batch": "B1", "earliest_executable_batch": "B1", "required_evidence_batches": ["B1", "B3", "B6", "B7"], "final_closure_batch": "B7", "prerequisite_commands": ["vs001:db:migrate", "vs001:fixtures:load"]},
        "vs001:audit:docker": {"implementation_owner_batch": "B1", "registration_batch": "B1", "earliest_executable_batch": "B1", "required_evidence_batches": BATCHES, "final_closure_batch": "B7", "prerequisite_commands": []},
        "vs001:test:api": {"implementation_owner_batch": "B4", "registration_batch": "B4", "earliest_executable_batch": "B4", "required_evidence_batches": ["B4", "B5", "B6", "B7"], "final_closure_batch": "B7", "prerequisite_commands": ["vs001:test:db-integrity"]},
        "vs001:test:not-found": {"implementation_owner_batch": "B4", "registration_batch": "B4", "earliest_executable_batch": "B4", "required_evidence_batches": ["B4", "B6", "B7"], "final_closure_batch": "B7", "prerequisite_commands": ["vs001:test:api"]},
        "vs001:test:web": {"implementation_owner_batch": "B5", "registration_batch": "B5", "earliest_executable_batch": "B5", "required_evidence_batches": ["B5", "B6", "B7"], "final_closure_batch": "B7", "prerequisite_commands": ["vs001:test:api"]},
        "vs001:audit:disclosure": {"implementation_owner_batch": "B6", "registration_batch": "B6", "earliest_executable_batch": "B6", "required_evidence_batches": ["B6", "B7"], "final_closure_batch": "B7", "prerequisite_commands": ["vs001:test:api", "vs001:test:web"]},
        "vs001:test:consistency": {"implementation_owner_batch": "B6", "registration_batch": "B6", "earliest_executable_batch": "B6", "required_evidence_batches": ["B6", "B7"], "final_closure_batch": "B7", "prerequisite_commands": ["vs001:test:api", "vs001:test:web", "vs001:test:db-integrity"]},
        "vs001:evidence:validate": {"implementation_owner_batch": "B6", "registration_batch": "B6", "earliest_executable_batch": "B6", "required_evidence_batches": ["B6", "B7"], "final_closure_batch": "B7", "prerequisite_commands": ["vs001:audit:disclosure", "vs001:test:consistency"]},
        "vs001:bootstrap:clean-checkout": {"implementation_owner_batch": "B7", "registration_batch": "B7", "earliest_executable_batch": "B7", "required_evidence_batches": ["B7"], "final_closure_batch": "B7", "prerequisite_commands": ["vs001:evidence:validate"]},
    }


def frozen_support(batch_id: str) -> dict[str, object]:
    batch = batch_id.lower()
    tests = {"B1": ["tests/vs001/data/b1-public-catalog-integrity.test.ts"], "B2": ["tests/vs001/contracts/b2-public-catalog-contract.test.ts"], "B3": ["tests/vs001/data/b3-public-catalog-persistence.test.ts"], "B4": ["tests/vs001/api/public-catalog.integration.test.ts", "tests/vs001/api/public-catalog-not-found.test.ts"], "B5": ["tests/vs001/browser/public-catalog.spec.ts"], "B6": ["tests/vs001/api/public-catalog.integration.test.ts", "tests/vs001/browser/public-catalog.spec.ts", "tests/vs001/data/public-catalog-integrity.test.ts", "tests/vs001/security/public-catalog-disclosure.test.ts"], "B7": ["tests/vs001/governance/full-clean-checkout.test.mjs"]}[batch_id]
    command = {"B1": ["package.json", "scripts/vs001/db-migrate.mjs", "scripts/vs001/test-db-integrity.mjs", "scripts/vs001/audit-docker.mjs", "scripts/vs001/validate-batch.mjs", "scripts/vs001/bootstrap-batch-clean-checkout.mjs"], "B2": [], "B3": [], "B4": ["package.json", "scripts/vs001/test-api.mjs", "scripts/vs001/test-not-found.mjs"], "B5": ["package.json", "scripts/vs001/test-web.mjs"], "B6": ["package.json", "scripts/vs001/audit-disclosure.mjs", "scripts/vs001/test-consistency.mjs", "scripts/vs001/validate-evidence.mjs"], "B7": ["package.json", "scripts/vs001/bootstrap-clean-checkout.mjs"]}[batch_id]
    keys = {"B1": B1_KEYS, "B2": [], "B3": [], "B4": ["vs001:test:api", "vs001:test:not-found"], "B5": ["vs001:test:web"], "B6": ["vs001:audit:disclosure", "vs001:test:consistency", "vs001:evidence:validate"], "B7": ["vs001:bootstrap:clean-checkout"]}[batch_id]
    evidence = [f"artifacts/vs001/{batch}/{name}" for name in ("implementation-report.json", "mapping-evidence.json", "command-results.json", "database-evidence.json", "boundary-audit.json", "docker-preservation.json", "cleanup-proof.json", "candidate-manifest.json")]
    if batch_id == "B7":
        evidence.append("artifacts/vs001/b7/final-evidence.json")
    return {"TEST_AND_VALIDATION_PATH": tests, "COMMAND_REGISTRATION_PATH": command, "package_json_exact_script_keys": keys, "package_json_dependency_or_version_changes_authorized": False, "pnpm_lock_change_authorized": False, "EVIDENCE_OUTPUT_PATH": evidence, "MANIFEST_AND_INDEPENDENT_VALIDATOR_PATH": [f"scripts/vs001/validate-{batch}-candidate.mjs", f"tests/vs001/governance/{batch}-candidate.test.mjs"]}


def product_paths(batch_id: str, accepted: dict[str, object]) -> list[str]:
    if batch_id == "B6":
        return [p for p in accepted["allowed_paths"] if p.startswith("configs/")]
    return [] if batch_id == "B7" else accepted["allowed_paths"]


def observed_channels(mapping: dict[str, object]) -> list[str]:
    raw = mapping["independent_observation"]["channel"]
    values = raw if isinstance(raw, list) else [raw]
    text = " ".join(str(x).lower() for x in values)
    result = []
    for name, tokens in (("DATA", ("postgres", "database", "migration")), ("API", ("http", "api")), ("UI", ("browser", "dom", "accessibility")), ("SECURITY", ("disclosure", "redaction", "audit record"))):
        if any(token in text for token in tokens):
            result.append(name)
    return result or ["PROCESS"]


def derived_evidence_batches(mapping: dict[str, object], channels: list[str]) -> list[str]:
    owner = mapping["implementation_batch_ids"][0]
    lookup = {"DATA": "B1" if owner == "B1" else "B3", "API": "B4", "UI": "B5", "SECURITY": "B6", "PROCESS": owner}
    values = {owner, "B6"}
    for channel in channels:
        candidate = lookup[channel]
        values.add(candidate if int(candidate[1:]) >= int(owner[1:]) else "B6")
    return sorted(values, key=lambda x: int(x[1:]))


def expected_closures(contract: dict[str, object]) -> dict[str, dict[str, object]]:
    plan = frozen_schedule()
    result = {}
    for mapping in contract["traceability_mappings"]:
        owner = mapping["implementation_batch_ids"][0]
        channels = observed_channels(mapping)
        executable = [cid for cid in mapping["validation_command_ids"] if int(plan[cid]["earliest_executable_batch"][1:]) <= int(owner[1:])]
        lookup = {"DATA": "B1" if owner == "B1" else "B3", "API": "B4", "UI": "B5", "SECURITY": "B6", "PROCESS": owner}
        pending = [channel for channel in channels if int(lookup[channel][1:]) > int(owner[1:])] + ["SLICE_WIDE_CLEAN_CHECKOUT"]
        result[mapping["mapping_id"]] = {"mapping_id": mapping["mapping_id"], "authority_fingerprint": mapping["authority"]["fingerprint"], "accepted_semantic_assertion_sha256": sha256(canonical(mapping["semantic_assertion"])), "implementation_owner_batch": owner, "implementation_state": "PENDING_IMPLEMENTATION", "controlled_fixture": mapping["controlled_fixture"], "required_observation_channels": channels, "provisional_evidence_batches": [bid for bid in derived_evidence_batches(mapping, channels) if bid != "B7"], "final_closure_batch": "B7", "final_acceptance_state": "PENDING_RUNTIME_EVIDENCE", "commands_executable_at_implementation_batch": executable, "commands_deferred_until_registered": [cid for cid in mapping["validation_command_ids"] if cid not in executable], "pending_downstream_observations": pending}
    return result


def path_is_immutable_forbidden(path: str) -> bool:
    if path == "pnpm-lock.yaml":
        return True
    return any(fnmatch.fnmatchcase(path, pattern) for pattern in IMMUTABLE_FORBIDDEN if pattern != "pnpm-lock.yaml")


def expected_path_authorization(contract: dict[str, object]) -> dict[str, dict[str, object]]:
    batches = {b["batch_id"]: b for b in contract["implementation_batches"]}
    result = {}
    for bid in BATCHES:
        support = frozen_support(bid)
        product = product_paths(bid, batches[bid])
        exact = sorted(set(product + support["TEST_AND_VALIDATION_PATH"] + support["COMMAND_REGISTRATION_PATH"] + support["EVIDENCE_OUTPUT_PATH"] + support["MANIFEST_AND_INDEPENDENT_VALIDATOR_PATH"]))
        result[bid] = {"batch_id": bid, "accepted_protected_paths": contract["design"]["path_policy"]["protected"], "immutable_amendment_forbidden_paths": IMMUTABLE_FORBIDDEN, "PRODUCT_IMPLEMENTATION_PATH": product, **support, "exact_authorized_paths": exact, "wildcard_authorization": False}
    return result


def command_mapping_ids(command_id: str, b1_ids: set[str], commands: dict[str, dict[str, object]]) -> list[str]:
    return sorted(b1_ids & set(commands[command_id]["mapping_ids"])) if command_id in commands else sorted(b1_ids)


def frozen_later_command_paths() -> dict[str, list[str]]:
    return {
        "vs001:test:api": ["package.json", "scripts/vs001/test-api.mjs", "tests/vs001/api/public-catalog.integration.test.ts", "artifacts/vs001/b4/mapping-evidence.json", "artifacts/vs001/b4/command-results.json", "artifacts/vs001/b4/boundary-audit.json"],
        "vs001:test:not-found": ["package.json", "scripts/vs001/test-not-found.mjs", "tests/vs001/api/public-catalog-not-found.test.ts", "artifacts/vs001/b4/mapping-evidence.json", "artifacts/vs001/b4/command-results.json", "artifacts/vs001/b4/boundary-audit.json"],
        "vs001:test:web": ["package.json", "scripts/vs001/test-web.mjs", "tests/vs001/browser/public-catalog.spec.ts", "artifacts/vs001/b5/mapping-evidence.json", "artifacts/vs001/b5/command-results.json", "artifacts/vs001/b5/boundary-audit.json"],
        "vs001:audit:disclosure": ["package.json", "scripts/vs001/audit-disclosure.mjs", "tests/vs001/security/public-catalog-disclosure.test.ts", "artifacts/vs001/b6/mapping-evidence.json", "artifacts/vs001/b6/command-results.json", "artifacts/vs001/b6/boundary-audit.json"],
        "vs001:test:consistency": ["package.json", "scripts/vs001/test-consistency.mjs", "tests/vs001/api/public-catalog.integration.test.ts", "tests/vs001/browser/public-catalog.spec.ts", "tests/vs001/data/public-catalog-integrity.test.ts", "artifacts/vs001/b6/mapping-evidence.json", "artifacts/vs001/b6/command-results.json", "artifacts/vs001/b6/database-evidence.json"],
        "vs001:evidence:validate": ["package.json", "scripts/vs001/validate-evidence.mjs", "scripts/vs001/validate-b6-candidate.mjs", "tests/vs001/governance/b6-candidate.test.mjs", "artifacts/vs001/b7/final-evidence.json"] + [f"artifacts/vs001/b6/{name}" for name in ("implementation-report.json", "mapping-evidence.json", "command-results.json", "database-evidence.json", "boundary-audit.json", "docker-preservation.json", "cleanup-proof.json", "candidate-manifest.json")],
        "vs001:bootstrap:clean-checkout": ["package.json", "scripts/vs001/bootstrap-clean-checkout.mjs", "tests/vs001/governance/full-clean-checkout.test.mjs", "scripts/vs001/validate-b7-candidate.mjs", "tests/vs001/governance/b7-candidate.test.mjs"] + [f"artifacts/vs001/b7/{name}" for name in ("implementation-report.json", "mapping-evidence.json", "command-results.json", "database-evidence.json", "boundary-audit.json", "docker-preservation.json", "cleanup-proof.json", "candidate-manifest.json")],
    }


def expected_b1_matrix(contract: dict[str, object]) -> dict[str, dict[str, object]]:
    commands = {c["command_id"]: c for c in contract["commands"]}
    batch = next(b for b in contract["implementation_batches"] if b["batch_id"] == "B1")
    b1_ids = set(batch["mapping_ids"])
    db_ids = command_mapping_ids("vs001:db:migrate", b1_ids, commands)
    all_ids = sorted(b1_ids)
    definitions = {
        "database/config/schema.prisma": ("PRODUCT_IMPLEMENTATION_PATH", "relational schema and integrity declarations", ["vs001:db:migrate", "vs001:test:db-integrity"], db_ids, False),
        "database/migrations/20260719000000_vs001_public_catalog/migration.sql": ("PRODUCT_IMPLEMENTATION_PATH", "forward-only VS001 migration", ["vs001:db:migrate", "vs001:test:db-integrity"], db_ids, False),
        "database/seed-mechanism/vs001-fixtures.ts": ("PRODUCT_IMPLEMENTATION_PATH", "controlled fixture definitions separated from production seed", ["vs001:fixtures:load", "vs001:fixtures:cleanup", "vs001:test:db-integrity"], all_ids, False),
        "scripts/vs001/cleanup.mjs": ("PRODUCT_IMPLEMENTATION_PATH", "owned fixture cleanup orchestration", ["vs001:fixtures:cleanup"], all_ids, False),
        "scripts/vs001/fixtures.mjs": ("PRODUCT_IMPLEMENTATION_PATH", "owned fixture load orchestration", ["vs001:fixtures:load"], all_ids, False),
        "tests/vs001/data/b1-public-catalog-integrity.test.ts": ("TEST_AND_VALIDATION_PATH", "real PostgreSQL B1 integrity behavior", ["vs001:test:db-integrity"], all_ids, False),
        "package.json": ("COMMAND_REGISTRATION_PATH", "only seven exact VS001 B1 script registrations", B1_KEYS, all_ids, False),
        "scripts/vs001/db-migrate.mjs": ("COMMAND_REGISTRATION_PATH", "migration command implementation", ["vs001:db:migrate"], db_ids, False),
        "scripts/vs001/test-db-integrity.mjs": ("COMMAND_REGISTRATION_PATH", "database integrity test runner", ["vs001:test:db-integrity"], all_ids, False),
        "scripts/vs001/audit-docker.mjs": ("COMMAND_REGISTRATION_PATH", "owned Docker before/after preservation audit", ["vs001:audit:docker"], all_ids, False),
        "scripts/vs001/validate-batch.mjs": ("COMMAND_REGISTRATION_PATH", "batch-scoped evidence and boundary validation", ["vs001:batch:validate"], all_ids, False),
        "scripts/vs001/bootstrap-batch-clean-checkout.mjs": ("COMMAND_REGISTRATION_PATH", "B1-only clean-checkout orchestration", ["vs001:batch:clean-checkout"], all_ids, False),
    }
    evidence_owners = {"implementation-report.json": ["vs001:batch:validate"], "mapping-evidence.json": ["vs001:test:db-integrity"], "command-results.json": ["vs001:batch:validate"], "database-evidence.json": ["vs001:db:migrate"], "boundary-audit.json": ["vs001:batch:validate"], "docker-preservation.json": ["vs001:audit:docker"], "cleanup-proof.json": ["vs001:batch:clean-checkout"], "candidate-manifest.json": ["vs001:batch:validate"]}
    for name, owners in evidence_owners.items():
        definitions[f"artifacts/vs001/b1/{name}"] = ("EVIDENCE_OUTPUT_PATH", f"content-addressed B1 {name.removesuffix('.json').replace('-', ' ')}", owners, all_ids, True)
    definitions["scripts/vs001/validate-b1-candidate.mjs"] = ("MANIFEST_AND_INDEPENDENT_VALIDATOR_PATH", "independent B1 evidence and Git-object validator", ["vs001:batch:validate", "vs001:batch:clean-checkout"], all_ids, False)
    definitions["tests/vs001/governance/b1-candidate.test.mjs"] = ("MANIFEST_AND_INDEPENDENT_VALIDATOR_PATH", "B1 governance mutation and clean-checkout tests", ["vs001:batch:validate", "vs001:batch:clean-checkout"], all_ids, False)
    result = {}
    for path, spec in definitions.items():
        result[path] = {"path": path, "path_category": spec[0], "semantic_purpose": spec[1], "owning_command_ids": spec[2], "mapping_ids": spec[3], "decision_binding_ids": batch["decision_binding_ids"], "implementation_batch": "B1", "evidence_batch": "B1", "generated": spec[4], "mutation_and_cleanup_responsibility": "producer writes atomically under run identity; cleanup removes only run-owned resources and evidence remains immutable once candidate is signed"}
    return result


def frozen_package_script_bindings() -> list[dict[str, object]]:
    specs = [
        ("vs001:db:migrate", "node scripts/vs001/db-migrate.mjs", "scripts/vs001/db-migrate.mjs", []),
        ("vs001:fixtures:load", "node scripts/vs001/fixtures.mjs load", "scripts/vs001/fixtures.mjs", ["load"]),
        ("vs001:fixtures:cleanup", "node scripts/vs001/cleanup.mjs", "scripts/vs001/cleanup.mjs", []),
        ("vs001:test:db-integrity", "node scripts/vs001/test-db-integrity.mjs", "scripts/vs001/test-db-integrity.mjs", []),
        ("vs001:audit:docker", "node scripts/vs001/audit-docker.mjs", "scripts/vs001/audit-docker.mjs", []),
        ("vs001:batch:validate", "node scripts/vs001/validate-batch.mjs", "scripts/vs001/validate-batch.mjs", []),
        ("vs001:batch:clean-checkout", "node scripts/vs001/bootstrap-batch-clean-checkout.mjs", "scripts/vs001/bootstrap-batch-clean-checkout.mjs", []),
    ]
    return [{"package_json_key": key, "exact_command_string": command, "target_executable_file": target, "owning_command_id": key, "implementation_batch": "B1", "allowed_arguments": args, "allowed_environment_behavior": "inherit only accepted commissioning environment plus run-scoped VS001 identifiers; no secrets embedded", "may_invoke_another_script": False, "forbidden_shell_expansion": ["&&", "||", ";", "|", ">", "<", "$(", "`"]} for key, command, target, args in specs]


def frozen_producer_catalog() -> dict[str, dict[str, object]]:
    writes = {
        "vs001:db:migrate": {"B1": "artifacts/vs001/b1/database-evidence.json"},
        "vs001:test:db-integrity": {"B1": "artifacts/vs001/b1/mapping-evidence.json", "B3": "artifacts/vs001/b3/database-evidence.json"},
        "vs001:test:api": {"B4": "artifacts/vs001/b4/mapping-evidence.json"},
        "vs001:test:not-found": {"B4": "artifacts/vs001/b4/boundary-audit.json"},
        "vs001:test:web": {"B5": "artifacts/vs001/b5/mapping-evidence.json"},
        "vs001:audit:disclosure": {"B6": "artifacts/vs001/b6/boundary-audit.json"},
        "vs001:test:consistency": {"B6": "artifacts/vs001/b6/mapping-evidence.json"},
        "vs001:evidence:validate": {"B6": "artifacts/vs001/b6/candidate-manifest.json", "B7": "artifacts/vs001/b7/final-evidence.json"},
        "vs001:batch:validate": {"B1": "artifacts/vs001/b1/boundary-audit.json", "B2": "artifacts/vs001/b2/mapping-evidence.json", "B3": "artifacts/vs001/b3/mapping-evidence.json", "B4": "artifacts/vs001/b4/command-results.json", "B5": "artifacts/vs001/b5/boundary-audit.json", "B6": "artifacts/vs001/b6/command-results.json"},
        "vs001:batch:clean-checkout": {bid: f"artifacts/vs001/{bid.lower()}/cleanup-proof.json" for bid in BATCHES},
    }
    channel_map = {"vs001:db:migrate": ["DATA"], "vs001:test:db-integrity": ["DATA"], "vs001:test:api": ["API"], "vs001:test:not-found": ["API"], "vs001:test:web": ["UI"], "vs001:audit:disclosure": ["SECURITY"], "vs001:test:consistency": ["DATA", "API", "UI"], "vs001:evidence:validate": ["DATA", "API", "UI", "SECURITY", "PROCESS", "COMPOSITE_REVALIDATION"], "vs001:batch:validate": ["PROCESS"], "vs001:batch:clean-checkout": ["PROCESS"]}
    plan = frozen_schedule()
    result = {}
    for cid in sorted(writes):
        authority = ({"kind": "ACCEPTED_C1_R2_FOCUSED_COMMAND", "earliest_executable_batch": plan[cid]["earliest_executable_batch"], "required_evidence_batches": plan[cid]["required_evidence_batches"]} if cid in plan else {"kind": "A2_BATCH_SCOPED_COMMAND", "registration_batch": "B1", "scheduled_batches": BATCHES if cid.endswith("clean-checkout") else BATCHES[:-1]})
        result[cid] = {"command_id": cid, "schedule_authority": authority, "schedule_authority_fingerprint": sha256(canonical(authority)), "scheduled_batches": sorted(writes[cid], key=lambda x: int(x[1:])), "write_authorized_paths_by_batch": writes[cid], "supported_observation_channels": channel_map[cid], "path_authorization_identities": {bid: "CPA-" + sha256(canonical([cid, bid, path]))[:24] for bid, path in writes[cid].items()}}
    return result


def frozen_choose_producer(mapping: dict[str, object], closure: dict[str, object], bid: str) -> tuple[str, str]:
    required = closure["required_observation_channels"]
    commands = set(mapping["validation_command_ids"])
    if bid == "B1" and "vs001:db:migrate" in commands:
        return "vs001:db:migrate", "DATA"
    if bid in ("B1", "B3") and "DATA" in required and "vs001:test:db-integrity" in commands:
        return "vs001:test:db-integrity", "DATA"
    if bid == "B4" and "API" in required:
        tokens = ("NOT_FOUND", "UNKNOWN", "MALFORMED", "UNAVAILABLE", "INACTIVE", "UNPUBLISHED", "WRONG_STOREFRONT")
        if "vs001:test:not-found" in commands and any(token in closure["mapping_id"] for token in tokens):
            return "vs001:test:not-found", "API"
        if "vs001:test:api" in commands:
            return "vs001:test:api", "API"
    if bid == "B5" and "UI" in required and "vs001:test:web" in commands:
        return "vs001:test:web", "UI"
    if bid == "B6":
        if "SECURITY" in required and "vs001:audit:disclosure" in commands:
            return "vs001:audit:disclosure", "SECURITY"
        if "vs001:test:consistency" in commands:
            for channel in ("API", "UI", "DATA"):
                if channel in required:
                    return "vs001:test:consistency", channel
        if "vs001:evidence:validate" in commands:
            return "vs001:evidence:validate", required[0]
    return "vs001:batch:validate", "PROCESS"


def frozen_fixture(mapping: dict[str, object]) -> tuple[str, dict[str, object]]:
    fixture = mapping["controlled_fixture"]
    fixture_id = fixture.get("fixture_id") if isinstance(fixture, dict) else None
    if not fixture_id:
        fixture_id = "FIX-" + sha256(canonical(fixture))[:16]
    return fixture_id, {"authority_fingerprint": mapping["authority"]["fingerprint"], "available_from_batch": mapping["implementation_batch_ids"][0], "fixture_sha256": sha256(canonical(fixture))}


def expected_lineage_catalog(contract: dict[str, object], closures: dict[str, dict[str, object]]) -> tuple[dict[str, dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    mappings = {m["mapping_id"]: m for m in contract["traceability_mappings"]}
    producers = frozen_producer_catalog()
    cleanup = [{"cleanup_evidence_record_id": f"CLEANUP-{bid}", "producer_batch": bid, "producer_command_id": "vs001:batch:clean-checkout", "evidence_file_path": producers["vs001:batch:clean-checkout"]["write_authorized_paths_by_batch"][bid], "evidence_record_pointer": f"/cleanup/CLEANUP-{bid}", "resource_scope": f"only run-owned VS001 {bid} resources", "proof_requirement": "independent before/after resource observation plus nonzero forced-failure cleanup verification"} for bid in BATCHES]
    result = {}
    for mid in sorted(closures):
        closure = closures[mid]
        mapping = mappings[mid]
        fixture_id, fixture_authority = frozen_fixture(mapping)
        fixture_authority["available_from_batch"] = min([mapping["implementation_batch_ids"][0], *closure["provisional_evidence_batches"]], key=lambda x: int(x[1:]))
        provisional_ids = [f"ELR-{mid}-{bid}-PROVISIONAL" for bid in closure["provisional_evidence_batches"]]
        final_id = f"ELR-{mid}-B7-FINAL-REVALIDATION"
        for index, bid in enumerate(closure["provisional_evidence_batches"]):
            rid = provisional_ids[index]
            cid, channel = frozen_choose_producer(mapping, closure, bid)
            command = producers[cid]
            result[rid] = {"evidence_record_id": rid, "mapping_id": mid, "record_kind": "PROVISIONAL_OBSERVATION", "producer_batch": bid, "producer_command_id": cid, "producer_command_schedule_authority": command["schedule_authority_fingerprint"], "evidence_file_path": command["write_authorized_paths_by_batch"][bid], "evidence_record_pointer": f"/records/{rid}", "exact_command_path_authorization_identity": command["path_authorization_identities"][bid], "observation_channel": channel, "controlled_fixture_id": fixture_id, "fixture_authority": fixture_authority, "expected_toolchain_environment_identity": {"node": "v24.18.0", "pnpm": "11.13.1", "corepack": True, "postgresql": "18.4 when DATA/API/UI/SECURITY runtime is required", "accepted_commissioning_environment": True}, "implementation_candidate_commit_tree_requirement": "signed accepted implementation-batch candidate commit and tree required at execution", "content_hash_or_git_blob_requirement": "SHA-256 plus Git blob identity required; stored PASS is insufficient", "cleanup_evidence_record_id": f"CLEANUP-{bid}", "downstream_dependency_record_ids": provisional_ids[index + 1:index + 2] or [final_id], "input_evidence_record_ids": [], "final_revalidation_record_id": final_id, "runtime_status": "NOT_EXECUTED"}
        cid = "vs001:evidence:validate"
        command = producers[cid]
        result[final_id] = {"evidence_record_id": final_id, "mapping_id": mid, "record_kind": "FINAL_REVALIDATION", "producer_batch": "B7", "producer_command_id": cid, "producer_command_schedule_authority": command["schedule_authority_fingerprint"], "evidence_file_path": "artifacts/vs001/b7/final-evidence.json", "evidence_record_pointer": f"/records/{final_id}", "exact_command_path_authorization_identity": command["path_authorization_identities"]["B7"], "observation_channel": "COMPOSITE_REVALIDATION", "controlled_fixture_id": fixture_id, "fixture_authority": fixture_authority, "expected_toolchain_environment_identity": {"node": "v24.18.0", "pnpm": "11.13.1", "corepack": True, "postgresql": "18.4 when runtime revalidation is required", "accepted_commissioning_environment": True}, "implementation_candidate_commit_tree_requirement": "resolve every accepted batch commit/tree and final candidate tree", "content_hash_or_git_blob_requirement": "resolve content and recompute SHA-256/Git blob; count or stored hash alone is insufficient", "cleanup_evidence_record_id": "CLEANUP-B7", "downstream_dependency_record_ids": [], "input_evidence_record_ids": provisional_ids, "final_revalidation_record_id": final_id, "runtime_status": "NOT_EXECUTED"}
    files: dict[tuple[str, str, str], list[str]] = {}
    for record in result.values():
        files.setdefault((record["producer_batch"], record["producer_command_id"], record["evidence_file_path"]), []).append(record["evidence_record_id"])
    for record in cleanup:
        files.setdefault((record["producer_batch"], record["producer_command_id"], record["evidence_file_path"]), []).append(record["cleanup_evidence_record_id"])
    file_catalog = [{"evidence_file_id": "EFILE-" + sha256(canonical([bid, cid, path]))[:20], "path": path, "owning_command_id": cid, "producer_batch": bid, "contained_record_ids": sorted(ids), "allowed_record_pointer_namespace": "/records/" if not all(x.startswith("CLEANUP-") for x in ids) else "/cleanup/", "schema": "VS001_EVIDENCE_FILE_V1", "authored_or_generated": "GENERATED_BY_REAL_EXECUTION", "content_addressing_rule": "signed candidate Git blob plus independently recomputed SHA-256", "cleanup_retention_responsibility": "runtime resources are cleaned; signed evidence bytes are immutable and retained", "downstream_consumers": ["vs001:evidence:validate", "vs001:bootstrap:clean-checkout"] if bid != "B7" else ["vs001:bootstrap:clean-checkout"]} for (bid, cid, path), ids in sorted(files.items())]
    existing = {(x["producer_batch"], x["path"]): x for x in file_catalog}
    plan = frozen_schedule()
    for bid in BATCHES:
        focused = sorted(cid for cid, spec in plan.items() if bid in spec["required_evidence_batches"] and int(spec["earliest_executable_batch"][1:]) <= int(bid[1:]))
        for path in frozen_support(bid)["EVIDENCE_OUTPUT_PATH"]:
            name = Path(path).name
            if (bid, path) in existing:
                row = existing[(bid, path)]
                sources = [row["owning_command_id"]]
            else:
                if name == "cleanup-proof.json": owner = "vs001:batch:clean-checkout"
                elif name == "docker-preservation.json": owner = "vs001:audit:docker"
                elif name == "final-evidence.json": owner = "vs001:evidence:validate"
                elif bid == "B7": owner = "vs001:evidence:validate" if name in ("mapping-evidence.json", "database-evidence.json", "boundary-audit.json") else "vs001:bootstrap:clean-checkout"
                elif name == "database-evidence.json" and bid == "B1": owner = "vs001:db:migrate"
                elif name == "database-evidence.json" and bid == "B3": owner = "vs001:test:db-integrity"
                elif name == "boundary-audit.json" and bid == "B4": owner = "vs001:test:not-found"
                elif name == "boundary-audit.json" and bid == "B6": owner = "vs001:audit:disclosure"
                elif name == "mapping-evidence.json" and bid == "B4": owner = "vs001:test:api"
                elif name == "mapping-evidence.json" and bid == "B5": owner = "vs001:test:web"
                elif name == "mapping-evidence.json" and bid == "B6": owner = "vs001:test:consistency"
                elif name == "candidate-manifest.json" and bid == "B6": owner = "vs001:evidence:validate"
                else: owner = "vs001:batch:validate"
                row = {"evidence_file_id": "EFILE-" + sha256(canonical([bid, owner, path]))[:20], "path": path, "owning_command_id": owner, "producer_batch": bid, "contained_record_ids": [], "allowed_record_pointer_namespace": "/command_records/", "schema": "VS001_EVIDENCE_FILE_V1", "authored_or_generated": "GENERATED_BY_REAL_EXECUTION", "content_addressing_rule": "signed candidate Git blob plus independently recomputed SHA-256", "cleanup_retention_responsibility": "runtime resources are cleaned; signed evidence bytes are immutable and retained", "downstream_consumers": ["vs001:evidence:validate", "vs001:bootstrap:clean-checkout"] if bid != "B7" else ["vs001:bootstrap:clean-checkout"]}
                file_catalog.append(row)
                existing[(bid, path)] = row
                sources = [owner]
            if name in ("command-results.json", "implementation-report.json", "candidate-manifest.json"):
                sources = sorted(set(sources + focused + (["vs001:batch:validate"] if bid != "B7" else ["vs001:bootstrap:clean-checkout"])))
            elif name == "cleanup-proof.json" and "vs001:fixtures:cleanup" in focused:
                sources = sorted(set(sources + ["vs001:fixtures:cleanup"]))
            row["source_command_ids"] = sources
            row["support_record_ids"] = [f"CMDREC-{bid}-{cid.replace(':', '-')}" for cid in sources]
            row["aggregator_authority"] = "owning command may aggregate the listed source-command results but must resolve their content-addressed records" if len(sources) > 1 else "NO_CROSS_COMMAND_AGGREGATION"
    file_catalog.sort(key=lambda x: (int(x["producer_batch"][1:]), x["path"], x["owning_command_id"]))
    artifacts, support_records, support_revalidations, cleanup_support = freeze_expected_support(result, file_catalog)
    return result, support_records, support_revalidations, artifacts, cleanup_support


def frozen_command_schedule_authority(command_id: str) -> dict[str, object]:
    plan = frozen_schedule()
    if command_id in plan:
        return {"authority_kind": "ACCEPTED_C1_R2_FOCUSED_COMMAND", "command_id": command_id, "earliest_executable_batch": plan[command_id]["earliest_executable_batch"], "required_evidence_batches": plan[command_id]["required_evidence_batches"]}
    if command_id == "vs001:batch:validate":
        return {"authority_kind": "A2_BATCH_SCOPED_COMMAND", "command_id": command_id, "scheduled_batches": BATCHES[:-1]}
    if command_id == "vs001:batch:clean-checkout":
        return {"authority_kind": "A2_BATCH_SCOPED_COMMAND", "command_id": command_id, "scheduled_batches": BATCHES}
    raise AmendmentError("A2_SUPPORT_PRODUCER_UNKNOWN", command_id)


def frozen_command_is_scheduled(command_id: str, batch_id: str) -> bool:
    authority = frozen_command_schedule_authority(command_id)
    return batch_id in authority.get("scheduled_batches", authority.get("required_evidence_batches", [])) and ("earliest_executable_batch" not in authority or int(batch_id[1:]) >= int(authority["earliest_executable_batch"][1:]))


def frozen_support_kind(path: str) -> str:
    return {"candidate-manifest.json": "CANDIDATE_MANIFEST", "implementation-report.json": "IMPLEMENTATION_INVENTORY_AND_REPORT", "command-results.json": "COMMAND_RESULT_AND_EXIT_IDENTITY", "boundary-audit.json": "PROTECTED_BOUNDARY_AUDIT", "docker-preservation.json": "DOCKER_BEFORE_AFTER_PRESERVATION", "cleanup-proof.json": "RESOURCE_CLEANUP_AND_RETENTION_PROOF", "database-evidence.json": "DATABASE_EXECUTION_SUPPORT", "mapping-evidence.json": "MAPPING_EVIDENCE_CONTAINER_SUPPORT", "final-evidence.json": "FINAL_DUAL_UNION_CONTAINER_SUPPORT"}[Path(path).name]


def freeze_expected_support(
    lineage: dict[str, dict[str, object]], legacy_files: list[dict[str, object]]
) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    lineage_ids = set(lineage)
    final_by_mapping = {row["mapping_id"]: row["evidence_record_id"] for row in lineage.values() if row["record_kind"] == "FINAL_REVALIDATION"}
    provisional_by_batch = {bid: set() for bid in BATCHES}
    for row in lineage.values():
        if row["record_kind"] == "PROVISIONAL_OBSERVATION":
            provisional_by_batch[row["producer_batch"]].add(final_by_mapping[row["mapping_id"]])
    artifacts, supports = [], []
    cleanup_by_batch: dict[str, str] = {}
    for legacy in legacy_files:
        bid, path = legacy["producer_batch"], legacy["path"]
        mapping_ids = sorted(x for x in legacy["contained_record_ids"] if x in lineage_ids)
        cleanup_ids = [x for x in legacy["contained_record_ids"] if x.startswith("CLEANUP-")]
        category = "MAPPING_EVIDENCE_ARTIFACT" if mapping_ids else "EXECUTION_SUPPORT_ARTIFACT"
        source_commands = sorted(set(legacy["source_command_ids"]))
        contained_support = []
        if category == "EXECUTION_SUPPORT_ARTIFACT":
            for cid in source_commands:
                require(frozen_command_is_scheduled(cid, bid), "A2_SUPPORT_PRODUCER_UNSCHEDULED", f"{cid}:{bid}")
                support_id = "SUP-" + sha256(canonical([bid, path, cid]))[:28]
                revalidation_id = "SUPREVAL-" + support_id.removeprefix("SUP-")
                authority = frozen_command_schedule_authority(cid)
                record = {"support_record_id": support_id, "artifact_file_path": path, "record_pointer": f"/support_records/{support_id}", "support_kind": frozen_support_kind(path), "producer_batch": bid, "producer_command_id": cid, "command_schedule_authority": authority, "command_schedule_authority_fingerprint": sha256(canonical(authority)), "exact_command_path_relation_identity": "CPR-" + sha256(canonical([cid, bid, path, "SUPPORT_RECORD_V1"]))[:28], "schema_identifier": "VS001_EXECUTION_SUPPORT_RECORD", "schema_version": "1.0.0", "implementation_candidate_commit_tree_requirement": "signed accepted implementation-batch candidate commit and tree required at execution", "content_sha256_or_git_blob_requirement": "resolve the exact artifact bytes and pointer payload, recompute SHA-256 and Git blob; stored PASS and aggregate count are insufficient", "expected_toolchain_environment_identity": {"node": "v24.18.0", "pnpm": "11.13.1", "corepack": True, "accepted_commissioning_environment": True, "postgresql": "18.4 only when the command contract requires PostgreSQL"}, "resource_ownership": f"only run-owned VS001 {bid} resources and the file-bound {support_id} record", "cleanup_retention_proof": "runtime resources are removed by the batch cleanup record; signed support bytes remain immutable and addressable", "cleanup_evidence_record_id": None, "downstream_consumer_record_ids": [revalidation_id], "b7_support_revalidation_record_id": revalidation_id, "required_by_mapping_final_revalidation_record_ids": sorted(provisional_by_batch[bid]) if bid != "B7" else sorted(final_by_mapping.values()), "direct_acceptance_evidence": False, "runtime_status": "NOT_EXECUTED"}
                supports.append(record); contained_support.append(support_id)
                if cleanup_ids and cid == "vs001:batch:clean-checkout": cleanup_by_batch[bid] = support_id
        artifacts.append({"artifact_file_id": "ART-" + sha256(canonical([bid, path, category]))[:24], "path": path, "artifact_category": category, "primary_owning_command_id": legacy["owning_command_id"], "producer_batch": bid, "producer_command_ids": source_commands if category == "EXECUTION_SUPPORT_ARTIFACT" else sorted({row["producer_command_id"] for row in lineage.values() if row["evidence_record_id"] in mapping_ids}), "contained_mapping_lineage_record_ids": mapping_ids, "contained_support_record_ids": sorted(contained_support), "contained_support_revalidation_record_ids": [], "allowed_pointer_namespaces": ["/records/"] if category == "MAPPING_EVIDENCE_ARTIFACT" else ["/support_records/"], "schema": "VS001_MAPPING_EVIDENCE_FILE_V1" if category == "MAPPING_EVIDENCE_ARTIFACT" else "VS001_EXECUTION_SUPPORT_FILE_V1", "authored_or_generated": legacy["authored_or_generated"], "content_addressing_rule": legacy["content_addressing_rule"], "cleanup_retention_responsibility": legacy["cleanup_retention_responsibility"], "downstream_consumers": legacy["downstream_consumers"], "category_change_requires_new_signed_authority": True, "direct_acceptance_closure_claimed": category == "MAPPING_EVIDENCE_ARTIFACT"})
    require(set(cleanup_by_batch) == set(BATCHES), "A2_SUPPORT_CLEANUP_MISSING", "seven cleanup support records")
    for row in supports: row["cleanup_evidence_record_id"] = cleanup_by_batch[row["producer_batch"]]
    for row in lineage.values(): row["cleanup_evidence_record_id"] = cleanup_by_batch[row["producer_batch"]]
    revalidations = []
    final_artifact = next(x for x in artifacts if x["path"] == "artifacts/vs001/b7/final-evidence.json")
    for source in sorted(supports, key=lambda x: x["support_record_id"]):
        rid = source["b7_support_revalidation_record_id"]
        revalidations.append({"support_revalidation_record_id": rid, "source_support_record_id": source["support_record_id"], "producer_batch": "B7", "producer_command_id": "vs001:evidence:validate", "artifact_file_path": "artifacts/vs001/b7/final-evidence.json", "record_pointer": f"/support_revalidation/{rid}", "required_source_resolution": {"artifact_file_path": source["artifact_file_path"], "record_pointer": source["record_pointer"], "candidate_commit_tree": True, "content_sha256_or_git_blob": True, "toolchain_environment": True, "cleanup_proof": True}, "stored_pass_sufficient": False, "runtime_status": "NOT_EXECUTED"})
    final_artifact["contained_support_revalidation_record_ids"] = sorted(x["support_revalidation_record_id"] for x in revalidations)
    final_artifact["allowed_pointer_namespaces"] = ["/records/", "/support_revalidation/"]
    final_artifact["producer_command_ids"] = sorted(set(final_artifact["producer_command_ids"] + ["vs001:evidence:validate"]))
    artifacts.sort(key=lambda x: (int(x["producer_batch"][1:]), x["path"])); supports.sort(key=lambda x: x["support_record_id"])
    return artifacts, supports, revalidations, [x for x in supports if x["support_kind"] == "RESOURCE_CLEANUP_AND_RETENTION_PROOF"]


def expected_command_path_record_closure(lineage: dict[str, dict[str, object]], supports: list[dict[str, object]], revalidations: list[dict[str, object]], files: list[dict[str, object]]) -> list[dict[str, object]]:
    command_ids = sorted(set(frozen_schedule()) | {"vs001:batch:validate", "vs001:batch:clean-checkout"})
    result = []
    for cid in command_ids:
        mapping_records = sorted(x["evidence_record_id"] for x in lineage.values() if x["producer_command_id"] == cid)
        produced_support = sorted(x["support_record_id"] for x in supports if x["producer_command_id"] == cid)
        produced_revalidations = sorted(x["support_revalidation_record_id"] for x in revalidations if x["producer_command_id"] == cid)
        paths = sorted({x["artifact_file_path"] for x in supports if x["producer_command_id"] == cid} | {x["evidence_file_path"] for x in lineage.values() if x["producer_command_id"] == cid} | {x["artifact_file_path"] for x in revalidations if x["producer_command_id"] == cid})
        role = "FINAL_ORCHESTRATOR" if cid == "vs001:bootstrap:clean-checkout" else ("MAPPING_AND_SUPPORT_PRODUCER" if mapping_records and produced_support else ("MAPPING_RECORD_PRODUCER" if mapping_records else "EXECUTION_SUPPORT_RECORD_PRODUCER"))
        result.append({"command_id": cid, "relation_role": role, "authorized_artifact_file_ids": sorted(x["artifact_file_id"] for x in files if x["path"] in paths), "authorized_artifact_paths": paths, "mapping_lineage_record_ids_produced": mapping_records, "support_record_ids_produced": produced_support, "support_revalidation_record_ids_produced": produced_revalidations, "executable_record_count": len(mapping_records)+len(produced_support)+len(produced_revalidations), "direct_acceptance_evidence": bool(mapping_records), "orphan": not bool(mapping_records or produced_support or produced_revalidations)})
    return result


def extract_markdown(text: str) -> tuple[dict[str, object], dict[str, object]]:
    require(text.endswith("\n") and not text.endswith("\n\n"), "A2_MARKDOWN_FORMAT", "single EOF newline")
    require(all(not line.endswith((" ", "\t")) for line in text.splitlines()), "A2_MARKDOWN_FORMAT", "trailing whitespace")
    require("Per-batch provisional evidence counts are not cumulative" in text, "A2_AMBIGUOUS_COUNT_SEMANTICS", "explicit non-cumulative statement missing")
    pattern = re.compile(r"<!-- EXEC_BOUNDARY_A2_SECTION:([^>]+) -->\n## [^\n]+\n\n```json\n(.*?)\n```", re.S)
    sections = {name: json.loads(raw) for name, raw in pattern.findall(text)}
    match = re.search(r"<!-- EXEC_BOUNDARY_A2_CANONICAL_PROJECTION -->\n## canonical_projection\n\n```json\n(.*?)\n```", text, re.S)
    require(match is not None, "A2_MARKDOWN_PROJECTION", "canonical projection missing")
    return json.loads(match.group(1)), sections


def validate_payload(payload: dict[str, object], contract: dict[str, object]) -> dict[str, object]:
    require(payload["candidate_id"] == CANDIDATE_ID and payload["supersedes"] == "V23-P2D-VS001-IMPLEMENTATION-CONTRACT-EXECUTION-BOUNDARY-AMENDMENT-A1-R2" and "correction_pass" not in payload, "A2_IDENTITY", "new amendment identity, not A1 correction pass 3")
    require(payload["status"] == "CANDIDATE" and payload["approval"] == "PENDING_HUMAN_APPROVAL", "A2_IDENTITY", "candidate lifecycle")
    require(payload["runtime_evidence_status"] == "NOT_EXECUTED" and payload["implementation_authorized"] is False, "A2_RUNTIME_CLAIM", "nonauthorization")
    require(not payload.get("stored_results"), "A2_STORED_PASS_REPLAY", "stored PASS/result fields cannot prove a gate")
    require(payload["protected_path_policy"]["stored_policy_booleans_are_authority"] is False, "A2_STORED_POLICY_TRUST", "stored policy trust")
    require(payload["protected_path_policy"]["pnpm_lock_yaml_forbidden"] is True, "A2_LOCKFILE_FORBIDDEN", "lockfile policy")
    expected_package_rule = {"batch": "B1", "exact_script_keys": B1_KEYS, "exact_script_bindings": frozen_package_script_bindings(), "all_other_fields_forbidden": True, "dependency_devDependency_version_packageManager_engines_changes_forbidden": True}
    package_bindings = payload.get("package_script_bindings", [])
    require(len(package_bindings) == 7, "A2_PACKAGE_SCRIPT_POPULATION", "seven exact package script bindings")
    for actual, expected in zip(package_bindings, frozen_package_script_bindings()):
        require(actual.get("package_json_key") == expected["package_json_key"], "A2_PACKAGE_SCRIPT_KEY", str(actual.get("package_json_key")))
        require(actual.get("exact_command_string") == expected["exact_command_string"] and actual.get("target_executable_file") == expected["target_executable_file"], "A2_PACKAGE_SCRIPT_TARGET", expected["package_json_key"])
        require(actual == expected, "A2_PACKAGE_SCRIPT_SEMANTICS", expected["package_json_key"])
    require(payload["protected_path_policy"]["package_json_rule"] == expected_package_rule, "A2_PACKAGE_JSON_SCOPE", "only seven exact script keys and no package metadata changes")
    require(payload["closure_model"]["per_batch_semantics"].endswith("is not cumulative"), "A2_AMBIGUOUS_COUNT_SEMANTICS", "per-batch semantics")
    require("monotonic union" in payload["closure_model"]["cumulative_semantics"], "A2_AMBIGUOUS_COUNT_SEMANTICS", "cumulative semantics")
    require(payload["artifact_taxonomy"]["artifact_file_count"] == 57 and payload["artifact_taxonomy"]["empty_containment_allowed"] is False, "A2_ARTIFACT_TAXONOMY", "57 closed artifact contracts")
    require(payload["support_record_contract"]["unfrozen_cmdrec_identity_count"] == 0 and payload["support_record_contract"]["direct_acceptance_evidence"] is False, "A2_UNFROZEN_CMDREC", "support catalog policy")
    require(payload["frozen_input_accounting"] == {"batches": 7, "mappings": 211, "decision_bindings": 11, "inherited_foundation_gates": 10, "focused_commands": 12, "batch_distribution": [28, 28, 26, 48, 6, 66, 9], "runtime_evidence_executed": 0}, "A2_ACCOUNTING", "frozen accounting")

    accepted_mappings = {m["mapping_id"]: m for m in contract["traceability_mappings"]}
    accepted_batches = {b["batch_id"]: b for b in contract["implementation_batches"]}
    expected_closure = expected_closures(contract)
    actual_closure = {x["mapping_id"]: x for x in payload["mapping_closure_catalog"]}
    require(len(actual_closure) == len(payload["mapping_closure_catalog"]) == 211 and set(actual_closure) == set(expected_closure), "A2_MAPPING_POPULATION", "211 closure records")
    for mid, expected in expected_closure.items():
        row = actual_closure[mid]
        for key, value in expected.items():
            code = "A2_MAPPING_CLOSURE"
            if key == "pending_downstream_observations":
                code = "A2_DOWNSTREAM_ROUTE_MISSING"
            elif key == "final_closure_batch":
                code = "A2_FINAL_ROUTE_MISSING"
            require(row.get(key) == value, code, f"{mid}:{key}")
        require(row["provisional_evidence_contract"]["independent_observation"] == accepted_mappings[mid]["independent_observation"], "A2_STORED_PASS_REPLAY", mid)
        require("content-addressed" in row["provisional_evidence_contract"]["rule"], "A2_EVIDENCE_IDENTITY", mid)

    expected_paths = expected_path_authorization(contract)
    actual_paths = {x["batch_id"]: x for x in payload["path_authorization"]}
    require(set(actual_paths) == set(expected_paths), "A2_PATH_POPULATION", "batch path population")
    future_product_paths = {path for bid in BATCHES[1:] for category in ("PRODUCT_IMPLEMENTATION_PATH", "TEST_AND_VALIDATION_PATH") for path in expected_paths[bid][category]}
    for path in actual_paths["B1"]["exact_authorized_paths"]:
        require(path not in future_product_paths, "A2_B1_FUTURE_BATCH_PRODUCT_PATH_LEAKAGE", path)
    for bid, expected in expected_paths.items():
        row = actual_paths[bid]
        require(row["immutable_amendment_forbidden_paths"] == IMMUTABLE_FORBIDDEN, "A2_PROTECTED_PATH", bid)
        for path in row["exact_authorized_paths"]:
            require(not path_is_immutable_forbidden(path), "A2_PROTECTED_PATH", f"{bid}:{path}")
            require("*" not in path, "A2_BROAD_PATH", f"{bid}:{path}")
        require("pnpm-lock.yaml" not in row["exact_authorized_paths"], "A2_LOCKFILE_FORBIDDEN", bid)
        require(row["package_json_dependency_or_version_changes_authorized"] is False, "A2_PACKAGE_JSON_SCOPE", bid)
        require(row == expected, "A2_PATH_POPULATION", f"{bid} exact independently frozen authorization")

    expected_matrix = expected_b1_matrix(contract)
    actual_matrix = {x["path"]: x for x in payload["b1_path_purpose_owner_matrix"]}
    require(len(actual_matrix) == len(payload["b1_path_purpose_owner_matrix"]) == 22 and set(actual_matrix) == set(expected_matrix), "A2_B1_INVENTORY", "22 exact B1 paths")
    category_counts = {}
    for path, expected in expected_matrix.items():
        row = actual_matrix[path]
        require(row == expected, "A2_PATH_PURPOSE_OWNER", path)
        require(row["owning_command_ids"] and row["mapping_ids"] and row["semantic_purpose"], "A2_PATH_OWNER_MISSING", path)
        category_counts[row["path_category"]] = category_counts.get(row["path_category"], 0) + 1
    require(category_counts == {"PRODUCT_IMPLEMENTATION_PATH": 5, "TEST_AND_VALIDATION_PATH": 1, "COMMAND_REGISTRATION_PATH": 6, "EVIDENCE_OUTPUT_PATH": 8, "MANIFEST_AND_INDEPENDENT_VALIDATOR_PATH": 2}, "A2_B1_INVENTORY", str(category_counts))

    commands = {c["command_id"]: c for c in contract["commands"]}
    plan = frozen_schedule()
    rows = {x["command_id"]: x for x in payload["command_schedule"]}
    require(set(rows) == set(plan) and len(rows) == 12, "A2_COMMAND_POPULATION", "12 focused commands")
    for cid, frozen in plan.items():
        row = rows[cid]
        for key, value in frozen.items():
            require(row[key] == value, "A2_COMMAND_SCHEDULE", f"{cid}:{key}")
        require(row["exact_mapping_ids"] == commands[cid]["mapping_ids"] and row["exact_decision_binding_ids"] == commands[cid]["decision_binding_ids"], "A2_COMMAND_AUTHORITY", cid)
        expected_allowed = sorted(path for path, entry in expected_matrix.items() if cid in entry["owning_command_ids"]) if frozen["implementation_owner_batch"] == "B1" else sorted(frozen_later_command_paths()[cid])
        require(row["allowed_paths"] == expected_allowed, "A2_COMMAND_PATH_RELEVANCE", cid)
        require(all(any(path in expected_paths[bid]["exact_authorized_paths"] for bid in BATCHES) for path in expected_allowed), "A2_COMMAND_PATH_RELEVANCE", f"{cid}:authorized subset")
    require("apps/api/src/vs001/public-catalog.controller.ts" not in rows["vs001:audit:docker"]["allowed_paths"], "A2_COMMAND_PATH_RELEVANCE", "docker/API mismatch")

    accepted_commands = {c["command_id"]: c for c in contract["commands"]}
    inherited_expected = [{"command_id": cid, "authority": accepted_commands[cid]["authority"], "acceptance_evidence": False, "required_by_batches": accepted_commands[cid]["required_by_batches"], "foundation_purpose": accepted_commands[cid]["foundation_purpose"]} for cid in sorted(accepted_commands) if accepted_commands[cid]["command_class"] == "INHERITED_COMMISSIONING_FOUNDATION_GATE"]
    require(payload["inherited_foundation_gate_classification"] == inherited_expected and len(inherited_expected) == 10, "A2_INHERITED_GATE_CLASSIFICATION", "10 signed foundation gates")
    require(payload["batch_scoped_validation_interface"]["full_slice_command_reserved"] == "vs001:bootstrap:clean-checkout at B7", "A2_B7_BOOTSTRAP_PREMATURE", "full-slice command reservation")

    batch_rows = payload["seven_batch_matrix"]
    require([r["batch_id"] for r in batch_rows] == BATCHES, "A2_BATCH_POPULATION", "batch order")
    retained: set[str] = set()
    closed: set[str] = set()
    implemented_union = []
    actual_counts = []
    for index, row in enumerate(batch_rows, 1):
        bid = f"B{index}"
        expected_impl = accepted_batches[bid]["mapping_ids"]
        expected_provisional = sorted(mid for mid, closure_row in expected_closure.items() if bid in closure_row["provisional_evidence_batches"])
        retained.update(expected_provisional)
        expected_new_closed = sorted(expected_closure) if bid == "B7" else []
        closed.update(expected_new_closed)
        require(row["newly_implemented_mapping_ids"] == expected_impl, "A2_IMPLEMENTATION_PROJECTION", bid)
        require(row["per_batch_provisional_evidence_mapping_ids"] == expected_provisional, "A2_BATCH_PROVISIONAL_MISMATCH", bid)
        require(row["cumulative_retained_evidence_mapping_ids"] == sorted(retained), "A2_CUMULATIVE_RETAINED_MISMATCH", bid)
        require(row["newly_final_closed_mapping_ids"] == expected_new_closed, "A2_FINAL_UNION_MISMATCH", bid)
        require(row["cumulative_final_closed_mapping_ids"] == sorted(closed), "A2_FINAL_UNION_MISMATCH", bid)
        require("NOT cumulative" in row["evidence_count_semantics"], "A2_AMBIGUOUS_COUNT_SEMANTICS", bid)
        require(row["prerequisite_batch_ids"] == accepted_batches[bid]["prerequisite_batch_ids"] and all(int(x[1:]) < index for x in row["prerequisite_batch_ids"]), "A2_BATCH_CYCLE", bid)
        require(row["decision_binding_ids"] == accepted_batches[bid]["decision_binding_ids"], "A2_BATCH_BINDINGS", bid)
        require(row["inherited_foundation_gate_ids"] == accepted_batches[bid]["inherited_foundation_gate_ids"], "A2_INHERITED_GATE_CLASSIFICATION", bid)
        expected_executable = sorted(cid for cid, command in plan.items() if bid in command["required_evidence_batches"] and int(command["earliest_executable_batch"][1:]) <= index)
        expected_deferred = sorted(cid for cid, command in plan.items() if int(command["earliest_executable_batch"][1:]) > index)
        require(row["executable_focused_command_ids"] == expected_executable, "A2_COMMAND_BEFORE_REGISTRATION", bid)
        require(row["deferred_focused_command_ids"] == expected_deferred, "A2_COMMAND_BEFORE_REGISTRATION", f"{bid}:deferred")
        require(row["authorized_paths"] == expected_paths[bid]["exact_authorized_paths"], "A2_PATH_POPULATION", f"{bid}:batch projection")
        implemented_union.extend(expected_impl)
        actual_counts.append((len(expected_impl), len(expected_provisional), len(retained), len(expected_new_closed), len(closed)))
    require(actual_counts == EXPECTED_COUNTS, "A2_STORED_COUNT_MISMATCH", str(actual_counts))
    require(len(implemented_union) == len(set(implemented_union)) == 211, "A2_IMPLEMENTATION_PROJECTION", "implementation partition")
    b1_ids = accepted_batches["B1"]["mapping_ids"]
    require([x["mapping_id"] for x in payload["b1_mapping_reclassification"]] == b1_ids, "A2_B1_MAPPING_POPULATION", "28 B1 mappings")
    for row in payload["b1_mapping_reclassification"]:
        require("vs001:test:api" not in row["commands_executable_at_implementation_batch"], "A2_API_BEFORE_IMPLEMENTATION", row["mapping_id"])
        require("vs001:test:web" not in row["commands_executable_at_implementation_batch"], "A2_BROWSER_BEFORE_IMPLEMENTATION", row["mapping_id"])
        require("vs001:bootstrap:clean-checkout" not in row["commands_executable_at_implementation_batch"], "A2_B7_BOOTSTRAP_PREMATURE", row["mapping_id"])

    accepted_bindings = {b["binding_id"]: b for b in contract["decision_bindings"]}
    progression = {x["binding_id"]: x for x in payload["decision_binding_progression"]}
    require(len(progression) == 11 and set(progression) == set(accepted_bindings), "A2_BINDING_POPULATION", "11 decision bindings")
    for bid, binding in accepted_bindings.items():
        require(progression[bid] == {"binding_id": bid, "authority_fingerprint": binding["authority"]["fingerprint"], "implementation_batches": binding["batches"], "final_closure_batch": "B7", "state": "NOT_IMPLEMENTED"}, "A2_BINDING_POPULATION", bid)

    expected_lineage, expected_support, expected_support_revalidation, expected_files, expected_cleanup = expected_lineage_catalog(contract, expected_closure)
    lineage = payload["evidence_lineage_requirements"]
    lineage_by_id = {x.get("evidence_record_id"): x for x in lineage}
    require(len(lineage_by_id) == len(lineage) and set(lineage_by_id) == set(expected_lineage), "A2_LINEAGE_POPULATION", "767 exact lineage identities")
    field_codes = {
        "mapping_id": "A2_LINEAGE_MAPPING", "record_kind": "A2_LINEAGE_KIND", "producer_batch": "A2_LINEAGE_PRODUCER_SCHEDULE",
        "producer_command_id": "A2_LINEAGE_PRODUCER", "producer_command_schedule_authority": "A2_LINEAGE_PRODUCER_SCHEDULE",
        "evidence_file_path": "A2_LINEAGE_EVIDENCE_PATH", "evidence_record_pointer": "A2_LINEAGE_RECORD_POINTER",
        "exact_command_path_authorization_identity": "A2_LINEAGE_PATH_AUTHORITY", "observation_channel": "A2_LINEAGE_CHANNEL",
        "controlled_fixture_id": "A2_LINEAGE_FIXTURE", "fixture_authority": "A2_LINEAGE_FIXTURE",
        "expected_toolchain_environment_identity": "A2_LINEAGE_TOOLCHAIN_ENVIRONMENT",
        "implementation_candidate_commit_tree_requirement": "A2_LINEAGE_CONTENT_IDENTITY",
        "content_hash_or_git_blob_requirement": "A2_LINEAGE_CONTENT_IDENTITY",
        "cleanup_evidence_record_id": "A2_LINEAGE_CLEANUP", "downstream_dependency_record_ids": "A2_LINEAGE_DEPENDENCY",
        "input_evidence_record_ids": "A2_LINEAGE_INPUT_UNION", "final_revalidation_record_id": "A2_LINEAGE_FINAL_ROUTE",
        "runtime_status": "A2_STORED_PASS_REPLAY",
    }
    for rid, expected in expected_lineage.items():
        actual = lineage_by_id[rid]
        require(actual.get("evidence_record_id") == rid, "A2_EVIDENCE_IDENTITY", rid)
        require(rid not in actual.get("downstream_dependency_record_ids", []), "A2_LINEAGE_DEPENDENCY_CYCLE", rid)
        for field, expected_value in expected.items():
            if field == "evidence_record_id":
                continue
            require(actual.get(field) == expected_value, field_codes[field], f"{rid}:{field}")
        require("#" not in actual["evidence_file_path"] and actual["evidence_record_pointer"].startswith("/records/"), "A2_LINEAGE_RECORD_POINTER", rid)

    producer_expected = frozen_producer_catalog()
    producer_actual = {x["command_id"]: x for x in payload.get("lineage_producer_command_catalog", [])}
    require(set(producer_actual) == set(producer_expected), "A2_PRODUCER_CATALOG_POPULATION", "producer catalog")
    for cid, expected in producer_expected.items():
        require(producer_actual[cid] == expected, "A2_PRODUCER_CATALOG_SEMANTICS", cid)
    actual_files_by_id = {x.get("artifact_file_id"): x for x in payload.get("evidence_file_catalog", [])}
    expected_files_by_id = {x["artifact_file_id"]: x for x in expected_files}
    require(len(actual_files_by_id) == len(payload.get("evidence_file_catalog", [])) == 57 and set(actual_files_by_id) == set(expected_files_by_id), "A2_ARTIFACT_CATALOG", "57 unique artifact identities")
    actual_support_by_id = {x.get("support_record_id"): x for x in payload.get("support_record_catalog", [])}
    expected_support_by_id = {x["support_record_id"]: x for x in expected_support}
    manifest_support_ids = {x["support_record_id"] for x in expected_support if Path(x["artifact_file_path"]).name == "candidate-manifest.json"}
    require(manifest_support_ids <= set(actual_support_by_id), "A2_MANIFEST_SUPPORT_LINEAGE_MISSING", "all batch candidate manifests require support lineage")
    require(len(actual_support_by_id) == len(payload.get("support_record_catalog", [])) and set(actual_support_by_id) == set(expected_support_by_id), "A2_SUPPORT_CATALOG_POPULATION", "unique file-bound support identities")
    actual_revalidation_by_id = {x.get("support_revalidation_record_id"): x for x in payload.get("support_revalidation_catalog", [])}
    expected_revalidation_by_id = {x["support_revalidation_record_id"]: x for x in expected_support_revalidation}
    require(len(actual_revalidation_by_id) == len(payload.get("support_revalidation_catalog", [])) and set(actual_revalidation_by_id) == set(expected_revalidation_by_id), "A2_SUPPORT_REVALIDATION_POPULATION", "B7 support identities")
    expected_relation = expected_command_path_record_closure(expected_lineage, expected_support, expected_support_revalidation, expected_files)
    actual_relation_rows = payload.get("command_path_record_closure", [])
    actual_relation = {x.get("command_id"): x for x in actual_relation_rows}
    require(len(actual_relation) == len(actual_relation_rows) == 14 and all(x.get("executable_record_count", 0) > 0 and not x.get("orphan", True) for x in actual_relation.values()), "A2_COMMAND_ZERO_EXECUTABLE_RECORDS", "every command produces mapping or support records")
    require(all(not x["orphan"] and x["executable_record_count"] > 0 for x in expected_relation), "A2_COMMAND_ZERO_EXECUTABLE_RECORDS", "command relation")
    authorized_evidence = {(bid, path) for bid in BATCHES for path in expected_paths[bid]["EVIDENCE_OUTPUT_PATH"]}
    catalog_evidence = {(x["producer_batch"], x["path"]) for x in expected_files}
    require(catalog_evidence == authorized_evidence, "A2_EVIDENCE_FILE_ORPHAN", "every exact evidence path has one catalog owner")
    all_commands = set(frozen_schedule()) | {"vs001:batch:validate", "vs001:batch:clean-checkout"}
    support_by_id = actual_support_by_id
    revalidation_by_id = actual_revalidation_by_id
    require(not any("CMDREC-" in json.dumps(x, sort_keys=True) for x in (payload,)), "A2_UNFROZEN_CMDREC", "unfrozen support substitution")
    containment_counts: dict[str, int] = {}
    for artifact in actual_files_by_id.values():
        require(bool(artifact.get("contained_mapping_lineage_record_ids") or artifact.get("contained_support_record_ids") or artifact.get("contained_support_revalidation_record_ids")), "A2_ARTIFACT_EMPTY_CONTAINMENT", str(artifact.get("path")))
        for sid in artifact.get("contained_support_record_ids", []):
            require(sid in support_by_id, "A2_SUPPORT_UNKNOWN_ID", f"{artifact.get('path')}:{sid}")
            containment_counts[sid] = containment_counts.get(sid, 0) + 1
    require(all(containment_counts.get(sid, 0) == 1 for sid in support_by_id), "A2_SUPPORT_ID_REUSED", "each support identity belongs to exactly one artifact")
    category_counts = {category: sum(x["artifact_category"] == category for x in expected_files) for category in ("MAPPING_EVIDENCE_ARTIFACT", "EXECUTION_SUPPORT_ARTIFACT")}
    require(category_counts == {"MAPPING_EVIDENCE_ARTIFACT": 13, "EXECUTION_SUPPORT_ARTIFACT": 44}, "A2_ARTIFACT_CATEGORY", str(category_counts))
    for artifact_id, expected_file in expected_files_by_id.items():
        file_row = actual_files_by_id[artifact_id]
        require(file_row.get("path") == expected_file["path"] and file_row.get("producer_batch") == expected_file["producer_batch"], "A2_ARTIFACT_PATH_IDENTITY", artifact_id)
        require(file_row.get("artifact_category") == expected_file["artifact_category"], "A2_ARTIFACT_CATEGORY", expected_file["path"])
        for field in ("primary_owning_command_id", "producer_command_ids", "allowed_pointer_namespaces", "schema", "authored_or_generated", "content_addressing_rule", "cleanup_retention_responsibility", "downstream_consumers", "category_change_requires_new_signed_authority", "direct_acceptance_closure_claimed"):
            require(file_row.get(field) == expected_file[field], "A2_ARTIFACT_SEMANTICS", f"{expected_file['path']}:{field}")
        mapping_ids, support_ids, revalidation_ids = file_row["contained_mapping_lineage_record_ids"], file_row["contained_support_record_ids"], file_row["contained_support_revalidation_record_ids"]
        require(bool(mapping_ids or support_ids or revalidation_ids), "A2_ARTIFACT_EMPTY_CONTAINMENT", file_row["path"])
        require(mapping_ids == expected_file["contained_mapping_lineage_record_ids"], "A2_ARTIFACT_MAPPING_CONTAINMENT", expected_file["path"])
        require(support_ids == expected_file["contained_support_record_ids"], "A2_ARTIFACT_SUPPORT_CONTAINMENT", expected_file["path"])
        require(revalidation_ids == expected_file["contained_support_revalidation_record_ids"], "A2_ARTIFACT_SUPPORT_REVALIDATION_CONTAINMENT", expected_file["path"])
        if file_row["artifact_category"] == "MAPPING_EVIDENCE_ARTIFACT":
            require(bool(mapping_ids), "A2_MAPPING_ARTIFACT_EMPTY", file_row["path"])
        else:
            require(bool(support_ids) and not mapping_ids and file_row["direct_acceptance_closure_claimed"] is False, "A2_SUPPORT_ARTIFACT_FALSE_ACCEPTANCE", file_row["path"])
        require(set(revalidation_ids) <= set(revalidation_by_id), "A2_SUPPORT_REVALIDATION_UNKNOWN_ID", file_row["path"])
        require(set(file_row["producer_command_ids"]) <= all_commands, "A2_ARTIFACT_PRODUCER", file_row["path"])

    file_by_path = {x["path"]: x for x in actual_files_by_id.values()}
    used_producers = set()
    for rid, record in lineage_by_id.items():
        command = producer_expected[record["producer_command_id"]]
        used_producers.add(record["producer_command_id"])
        require(record["producer_batch"] in command["scheduled_batches"], "A2_LINEAGE_PRODUCER_SCHEDULE", rid)
        require(command["write_authorized_paths_by_batch"].get(record["producer_batch"]) == record["evidence_file_path"], "A2_LINEAGE_EVIDENCE_PATH", rid)
        require(record["observation_channel"] in command["supported_observation_channels"], "A2_LINEAGE_CHANNEL", rid)
        require(int(record["fixture_authority"]["available_from_batch"][1:]) <= int(record["producer_batch"][1:]), "A2_LINEAGE_FIXTURE", f"{rid}:availability")
        require(record["evidence_file_path"] in expected_paths[record["producer_batch"]]["exact_authorized_paths"], "A2_LINEAGE_EVIDENCE_PATH", f"{rid}:batch authorization")
        file_row = file_by_path[record["evidence_file_path"]]
        require(rid in file_row["contained_mapping_lineage_record_ids"] and any(record["evidence_record_pointer"].startswith(ns) for ns in file_row["allowed_pointer_namespaces"]), "A2_LINEAGE_RECORD_POINTER", rid)
    used_producers.update(x["producer_command_id"] for x in expected_cleanup)
    require(set(producer_expected) <= used_producers, "A2_COMMAND_PATH_RECORD_ORPHAN", f"unused mapping producers={sorted(set(producer_expected)-used_producers)}")

    cleanup_ids = {x["support_record_id"] for x in expected_cleanup}
    graph = {rid: row["downstream_dependency_record_ids"] for rid, row in lineage_by_id.items()}
    require(all(row["cleanup_evidence_record_id"] in cleanup_ids for row in lineage), "A2_LINEAGE_CLEANUP", "cleanup identity existence")
    require(all(dep in lineage_by_id for deps in graph.values() for dep in deps), "A2_LINEAGE_DEPENDENCY", "dependency existence")
    state: dict[str, int] = {}
    def visit(node: str) -> None:
        require(state.get(node, 0) != 1, "A2_LINEAGE_DEPENDENCY_CYCLE", node)
        if state.get(node, 0) == 2:
            return
        state[node] = 1
        for dep in graph[node]:
            visit(dep)
        state[node] = 2
    for rid in sorted(graph):
        visit(rid)

    # Frozen support records are file-bound, executable, content-addressed and revalidated exactly once at B7.
    seen_file_bound: set[tuple[str, str]] = set()
    support_field_codes = {
        "artifact_file_path": "A2_SUPPORT_WRONG_FILE", "record_pointer": "A2_SUPPORT_POINTER_NAMESPACE",
        "producer_batch": "A2_SUPPORT_PRODUCER_UNSCHEDULED", "producer_command_id": "A2_SUPPORT_PRODUCER_UNSCHEDULED",
        "command_schedule_authority": "A2_SUPPORT_PRODUCER_UNSCHEDULED", "command_schedule_authority_fingerprint": "A2_SUPPORT_PRODUCER_UNSCHEDULED",
        "exact_command_path_relation_identity": "A2_SUPPORT_PATH_UNAUTHORIZED", "content_sha256_or_git_blob_requirement": "A2_SUPPORT_CONTENT_IDENTITY",
        "implementation_candidate_commit_tree_requirement": "A2_SUPPORT_CONTENT_IDENTITY", "cleanup_evidence_record_id": "A2_SUPPORT_CLEANUP_MISSING",
        "cleanup_retention_proof": "A2_SUPPORT_CLEANUP_MISSING", "b7_support_revalidation_record_id": "A2_SUPPORT_B7_ROUTE_MISSING",
        "downstream_consumer_record_ids": "A2_SUPPORT_B7_ROUTE_MISSING", "runtime_status": "A2_SUPPORT_STORED_PASS_REPLAY",
        "direct_acceptance_evidence": "A2_SUPPORT_ONLY_FALSE_ACCEPTANCE", "expected_toolchain_environment_identity": "A2_SUPPORT_TOOLCHAIN_ENVIRONMENT",
    }
    for sid, expected_record in expected_support_by_id.items():
        record = support_by_id[sid]
        path, pointer = record.get("artifact_file_path"), record.get("record_pointer")
        if expected_record["support_kind"] == "DOCKER_BEFORE_AFTER_PRESERVATION":
            require(record.get("producer_command_id") == "vs001:audit:docker", "A2_DOCKER_SUPPORT_PRODUCER", sid)
        for field, expected_value in expected_record.items():
            if field == "support_record_id": continue
            code = support_field_codes.get(field, "A2_SUPPORT_SEMANTICS")
            if field == "artifact_file_path" and record.get(field) not in expected_paths[expected_record["producer_batch"]]["EVIDENCE_OUTPUT_PATH"]:
                code = "A2_SUPPORT_PATH_UNAUTHORIZED"
            require(record.get(field) == expected_value, code, f"{sid}:{field}")
        require((path, pointer) not in seen_file_bound, "A2_SUPPORT_ID_REUSED", sid); seen_file_bound.add((path, pointer))
        require(path in file_by_path and sid in file_by_path[path]["contained_support_record_ids"], "A2_SUPPORT_WRONG_FILE", sid)
        require(any(pointer.startswith(ns) for ns in file_by_path[path]["allowed_pointer_namespaces"]), "A2_SUPPORT_POINTER_NAMESPACE", sid)
        require(frozen_command_is_scheduled(record["producer_command_id"], record["producer_batch"]), "A2_SUPPORT_PRODUCER_UNSCHEDULED", sid)
        require(path in expected_paths[record["producer_batch"]]["EVIDENCE_OUTPUT_PATH"], "A2_SUPPORT_PATH_UNAUTHORIZED", sid)
        require(record["content_sha256_or_git_blob_requirement"] and record["implementation_candidate_commit_tree_requirement"], "A2_SUPPORT_CONTENT_IDENTITY", sid)
        require(record["cleanup_evidence_record_id"] in cleanup_ids and record["cleanup_retention_proof"], "A2_SUPPORT_CLEANUP_MISSING", sid)
        require(record["b7_support_revalidation_record_id"] in revalidation_by_id, "A2_SUPPORT_B7_ROUTE_MISSING", sid)
        require(record["runtime_status"] == "NOT_EXECUTED" and record["direct_acceptance_evidence"] is False, "A2_SUPPORT_STORED_PASS_REPLAY", sid)
    for rid, expected_record in expected_revalidation_by_id.items():
        record = revalidation_by_id[rid]
        for field, expected_value in expected_record.items():
            if field == "support_revalidation_record_id": continue
            code = "A2_SUPPORT_REVALIDATION_SEMANTICS"
            if field == "source_support_record_id": code = "A2_SUPPORT_REVALIDATION_SOURCE_MISSING"
            elif field in ("artifact_file_path", "record_pointer"): code = "A2_SUPPORT_REVALIDATION_POINTER"
            elif field in ("stored_pass_sufficient", "runtime_status"): code = "A2_SUPPORT_STORED_PASS_REPLAY"
            require(record.get(field) == expected_value, code, f"{rid}:{field}")
        source = support_by_id.get(record["source_support_record_id"])
        require(source is not None, "A2_SUPPORT_REVALIDATION_SOURCE_MISSING", rid)
        require(record["artifact_file_path"] == "artifacts/vs001/b7/final-evidence.json" and record["record_pointer"].startswith("/support_revalidation/"), "A2_SUPPORT_REVALIDATION_POINTER", rid)
        require(record["stored_pass_sufficient"] is False and record["runtime_status"] == "NOT_EXECUTED", "A2_SUPPORT_STORED_PASS_REPLAY", rid)
    require(payload.get("cleanup_evidence_catalog") == expected_cleanup, "A2_SUPPORT_CLEANUP_CATALOG", "seven exact file-bound cleanup support records")
    require(payload.get("command_path_record_closure") == expected_relation, "A2_COMMAND_PATH_RECORD_CLOSURE", "14 exact command/path/executable-record relations")

    b7 = payload.get("b7_dual_revalidation_contract", {})
    require(b7.get("final_evidence_path") == "artifacts/vs001/b7/final-evidence.json", "A2_B7_FINAL_PATH", "exact final evidence path")
    require(b7.get("producer_command_id") == "vs001:evidence:validate" and b7.get("producer_batch") == "B7", "A2_B7_FINAL_PRODUCER", "final producer")
    require(b7.get("bootstrap_consumer_orchestrator_command_id") == "vs001:bootstrap:clean-checkout" and b7.get("producer_and_orchestrator_are_distinct") is True, "A2_B7_ORCHESTRATOR_RELATION", "producer/orchestrator separation")
    expected_inputs = sorted(rid for rid, row in expected_lineage.items() if row["record_kind"] == "PROVISIONAL_OBSERVATION")
    expected_finals = sorted(rid for rid, row in expected_lineage.items() if row["record_kind"] == "FINAL_REVALIDATION")
    acceptance_union = b7.get("acceptance_evidence_union", {})
    support_union = b7.get("execution_support_union", {})
    require(acceptance_union.get("signed_provisional_mapping_record_ids") == expected_inputs and acceptance_union.get("final_mapping_revalidation_record_ids") == expected_finals and acceptance_union.get("mapping_ids") == sorted(expected_closure), "A2_B7_MAPPING_UNION", "556/211/211")
    require(support_union.get("source_support_record_ids") == sorted(support_by_id) and support_union.get("support_revalidation_record_ids") == sorted(revalidation_by_id), "A2_B7_SUPPORT_UNION_INCOMPLETE", "complete support union")
    require(support_union.get("support_artifact_file_ids") == sorted(x["artifact_file_id"] for x in expected_files if x["artifact_category"] == "EXECUTION_SUPPORT_ARTIFACT"), "A2_B7_SUPPORT_ARTIFACT_UNION", "44 support artifacts")
    require(b7.get("mapping_record_namespace") == "/records/" and b7.get("support_revalidation_namespace") == "/support_revalidation/", "A2_B7_NAMESPACE_COLLISION", "disjoint namespaces")
    require(b7.get("final_mapping_closure_requires_complete_support_union") is True, "A2_B7_MAPPING_WITHOUT_SUPPORT", "support required for final mapping closure")
    require(any("stored-PASS" in text for text in b7.get("required_revalidations", [])), "A2_SUPPORT_STORED_PASS_REPLAY", "B7 support revalidation")
    require(b7.get("runtime_status") == "NOT_EXECUTED", "A2_RUNTIME_CLAIM", "B7")
    expected_lineage_count = sum(len(x["provisional_evidence_batches"]) + 1 for x in expected_closure.values())
    require(len(lineage) == expected_lineage_count == 767 == payload["evidence_lineage_contract"]["record_count"], "A2_LINEAGE_POPULATION", str(len(lineage)))
    require(payload["evidence_lineage_contract"]["provisional_record_count"] == 556 and payload["evidence_lineage_contract"]["final_revalidation_record_count"] == 211, "A2_LINEAGE_POPULATION", "556+211")
    require(payload["evidence_lineage_contract"]["b7_complete_union_required"] is True and payload["evidence_lineage_contract"]["runtime_records_currently_exist"] is False, "A2_FINAL_WITHOUT_LINEAGE", "lineage contract")
    return {"mappings": 211, "b1_paths": 22, "lineage_records": len(lineage), "provisional_records": 556, "final_records": 211, "artifact_files": len(expected_files), "mapping_artifacts": category_counts["MAPPING_EVIDENCE_ARTIFACT"], "support_artifacts": category_counts["EXECUTION_SUPPORT_ARTIFACT"], "support_records": len(expected_support), "support_revalidations": len(expected_support_revalidation), "commands": 12, "batches": 7}


def validate_files(root: Path, check_git: bool = False) -> dict[str, object]:
    contract, raw = accepted_contract()
    payload = json.loads((root / JSON_REL).read_bytes())
    require(payload["accepted_contract_authority"]["sha256"] == sha256(raw), "A2_ACCEPTED_CONTRACT_HASH", "accepted C1-R2 bytes")
    counts = validate_payload(payload, contract)
    projected, sections = extract_markdown((root / MD_REL).read_text(encoding="utf-8"))
    require(projected == payload, "A2_MARKDOWN_PROJECTION", "canonical projection divergence")
    for name in ("closure_model", "artifact_taxonomy", "evidence_lineage_contract", "support_record_contract", "lineage_producer_command_catalog", "evidence_file_catalog", "support_record_catalog", "support_revalidation_catalog", "command_path_record_closure", "cleanup_evidence_catalog", "b7_dual_revalidation_contract", "package_script_bindings", "protected_path_policy", "batch_scoped_validation_interface", "inherited_foundation_gate_classification", "b1_path_purpose_owner_matrix", "command_schedule", "path_authorization", "seven_batch_matrix", "non_claims"):
        require(sections.get(name) == payload[name], "A2_MARKDOWN_SECTION", name)
    manifest = json.loads((root / MANIFEST_REL).read_bytes())
    require(manifest["inventory"] == INVENTORY, "A2_INVENTORY", "manifest inventory")
    require(manifest["runtime_evidence_status"] == "NOT_EXECUTED" and manifest["implementation_authorized"] is False, "A2_RUNTIME_CLAIM", "manifest")
    for rel, expected in manifest["file_sha256_excluding_manifest"].items():
        require(sha256((root / rel).read_bytes()) == expected, "A2_FILE_HASH", rel)
    generated = [str(MD_REL), str(JSON_REL)]
    aggregate = sha256(canonical([{"path": p, "sha256": manifest["file_sha256_excluding_manifest"][p]} for p in sorted(generated)]))
    require(manifest["generated_payload_aggregate"] == aggregate, "A2_GENERATED_AGGREGATE", "generated domain")
    roots = {"mapping_closure_root": {x["mapping_id"]: sha256(canonical(x)) for x in payload["mapping_closure_catalog"]}, "command_schedule_root": {x["command_id"]: sha256(canonical(x)) for x in payload["command_schedule"]}, "seven_batch_root": {x["batch_id"]: sha256(canonical(x)) for x in payload["seven_batch_matrix"]}, "evidence_lineage_root": {x["evidence_record_id"]: sha256(canonical(x)) for x in payload["evidence_lineage_requirements"]}, "b1_path_matrix_root": {x["path"]: sha256(canonical(x)) for x in payload["b1_path_purpose_owner_matrix"]}, "lineage_producer_root": {x["command_id"]: sha256(canonical(x)) for x in payload["lineage_producer_command_catalog"]}, "evidence_file_catalog_root": {x["artifact_file_id"]: sha256(canonical(x)) for x in payload["evidence_file_catalog"]}, "support_record_catalog_root": {x["support_record_id"]: sha256(canonical(x)) for x in payload["support_record_catalog"]}, "support_revalidation_root": {x["support_revalidation_record_id"]: sha256(canonical(x)) for x in payload["support_revalidation_catalog"]}, "package_script_binding_root": {x["package_json_key"]: sha256(canonical(x)) for x in payload["package_script_bindings"]}, "command_path_record_root": {x["command_id"]: sha256(canonical(x)) for x in payload["command_path_record_closure"]}}
    for key, domain in roots.items():
        require(manifest[key] == sha256(canonical(domain)), "A2_ROOT_MISMATCH", key)
    if check_git:
        staged = subprocess.check_output(["git", "diff", "--cached", "--name-only"], cwd=root, text=True).splitlines()
        unstaged = subprocess.check_output(["git", "diff", "--name-only"], cwd=root, text=True).splitlines()
        untracked = subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard"], cwd=root, text=True).splitlines()
        changed = sorted(set(staged + unstaged + untracked))
        if not changed:
            changed = sorted(subprocess.check_output(["git", "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD^", "HEAD"], cwd=root, text=True).splitlines())
        require(changed == sorted(INVENTORY), "A2_INVENTORY", str(changed))
    return {"result": "VALID_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_EXECUTION_BOUNDARY_AMENDMENT_A2", **counts, "generated_payload_aggregate": aggregate}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check-git", action="store_true")
    args = parser.parse_args()
    try:
        result = validate_files(args.root, args.check_git)
    except AmendmentError as exc:
        print(f"INVALID_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_EXECUTION_BOUNDARY_AMENDMENT_A2: {exc}")
        raise SystemExit(1)
    print(json.dumps(result, sort_keys=True))
    print("VALID_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_EXECUTION_BOUNDARY_AMENDMENT_A2")


if __name__ == "__main__":
    main()
