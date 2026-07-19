#!/usr/bin/env python3
"""Build the VS001 execution-boundary governance amendment A2."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
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


def canonical(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_bytes(commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=GIT_ROOT)


def schedule() -> dict[str, dict[str, object]]:
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


def supporting_paths(batch_id: str) -> dict[str, object]:
    batch = batch_id.lower()
    tests = {
        "B1": ["tests/vs001/data/b1-public-catalog-integrity.test.ts"],
        "B2": ["tests/vs001/contracts/b2-public-catalog-contract.test.ts"],
        "B3": ["tests/vs001/data/b3-public-catalog-persistence.test.ts"],
        "B4": ["tests/vs001/api/public-catalog.integration.test.ts", "tests/vs001/api/public-catalog-not-found.test.ts"],
        "B5": ["tests/vs001/browser/public-catalog.spec.ts"],
        "B6": ["tests/vs001/api/public-catalog.integration.test.ts", "tests/vs001/browser/public-catalog.spec.ts", "tests/vs001/data/public-catalog-integrity.test.ts", "tests/vs001/security/public-catalog-disclosure.test.ts"],
        "B7": ["tests/vs001/governance/full-clean-checkout.test.mjs"],
    }[batch_id]
    command = {
        "B1": ["package.json", "scripts/vs001/db-migrate.mjs", "scripts/vs001/test-db-integrity.mjs", "scripts/vs001/audit-docker.mjs", "scripts/vs001/validate-batch.mjs", "scripts/vs001/bootstrap-batch-clean-checkout.mjs"],
        "B2": [], "B3": [],
        "B4": ["package.json", "scripts/vs001/test-api.mjs", "scripts/vs001/test-not-found.mjs"],
        "B5": ["package.json", "scripts/vs001/test-web.mjs"],
        "B6": ["package.json", "scripts/vs001/audit-disclosure.mjs", "scripts/vs001/test-consistency.mjs", "scripts/vs001/validate-evidence.mjs"],
        "B7": ["package.json", "scripts/vs001/bootstrap-clean-checkout.mjs"],
    }[batch_id]
    keys = {
        "B1": ["vs001:db:migrate", "vs001:fixtures:load", "vs001:fixtures:cleanup", "vs001:test:db-integrity", "vs001:audit:docker", "vs001:batch:validate", "vs001:batch:clean-checkout"],
        "B2": [], "B3": [], "B4": ["vs001:test:api", "vs001:test:not-found"], "B5": ["vs001:test:web"],
        "B6": ["vs001:audit:disclosure", "vs001:test:consistency", "vs001:evidence:validate"], "B7": ["vs001:bootstrap:clean-checkout"],
    }[batch_id]
    evidence = [f"artifacts/vs001/{batch}/{name}" for name in ("implementation-report.json", "mapping-evidence.json", "command-results.json", "database-evidence.json", "boundary-audit.json", "docker-preservation.json", "cleanup-proof.json", "candidate-manifest.json")]
    if batch_id == "B7":
        evidence.append("artifacts/vs001/b7/final-evidence.json")
    return {"TEST_AND_VALIDATION_PATH": tests, "COMMAND_REGISTRATION_PATH": command, "package_json_exact_script_keys": keys, "package_json_dependency_or_version_changes_authorized": False, "pnpm_lock_change_authorized": False, "EVIDENCE_OUTPUT_PATH": evidence, "MANIFEST_AND_INDEPENDENT_VALIDATOR_PATH": [f"scripts/vs001/validate-{batch}-candidate.mjs", f"tests/vs001/governance/{batch}-candidate.test.mjs"]}


def channels(mapping: dict[str, object]) -> list[str]:
    raw = mapping["independent_observation"]["channel"]
    values = raw if isinstance(raw, list) else [raw]
    text = " ".join(str(x).lower() for x in values)
    result = []
    for name, tokens in (("DATA", ("postgres", "database", "migration")), ("API", ("http", "api")), ("UI", ("browser", "dom", "accessibility")), ("SECURITY", ("disclosure", "redaction", "audit record"))):
        if any(token in text for token in tokens):
            result.append(name)
    return result or ["PROCESS"]


def evidence_batches(mapping: dict[str, object], observed: list[str]) -> list[str]:
    owner = mapping["implementation_batch_ids"][0]
    owner_i = int(owner[1:])
    channel_batch = {"DATA": "B1" if owner == "B1" else "B3", "API": "B4", "UI": "B5", "SECURITY": "B6", "PROCESS": owner}
    batches = {owner, "B6"}
    for channel in observed:
        candidate = channel_batch[channel]
        batches.add(candidate if int(candidate[1:]) >= owner_i else "B6")
    return sorted(batches, key=lambda x: int(x[1:]))


def closure(mapping: dict[str, object], plan: dict[str, dict[str, object]]) -> dict[str, object]:
    owner = mapping["implementation_batch_ids"][0]
    observed = channels(mapping)
    provisional = [bid for bid in evidence_batches(mapping, observed) if bid != "B7"]
    executable = [cid for cid in mapping["validation_command_ids"] if int(plan[cid]["earliest_executable_batch"][1:]) <= int(owner[1:])]
    channel_batch = {"DATA": "B1" if owner == "B1" else "B3", "API": "B4", "UI": "B5", "SECURITY": "B6", "PROCESS": owner}
    pending = [channel for channel in observed if int(channel_batch[channel][1:]) > int(owner[1:])] + ["SLICE_WIDE_CLEAN_CHECKOUT"]
    return {
        "mapping_id": mapping["mapping_id"], "authority_fingerprint": mapping["authority"]["fingerprint"],
        "accepted_semantic_assertion_sha256": sha256(canonical(mapping["semantic_assertion"])),
        "implementation_owner_batch": owner, "implementation_state": "PENDING_IMPLEMENTATION",
        "controlled_fixture": mapping["controlled_fixture"], "required_observation_channels": observed,
        "provisional_evidence_batches": provisional, "final_closure_batch": "B7",
        "final_acceptance_state": "PENDING_RUNTIME_EVIDENCE", "commands_executable_at_implementation_batch": executable,
        "commands_deferred_until_registered": [cid for cid in mapping["validation_command_ids"] if cid not in executable],
        "pending_downstream_observations": pending,
        "provisional_evidence_contract": {"action": mapping["action"], "independent_observation": mapping["independent_observation"], "evidence_artifacts": mapping["evidence_contract"]["artifacts"], "rule": "preserve content-addressed observed evidence; expected values and stored PASS never substitute for an observation"},
        "cleanup_contract": mapping["cleanup_contract"],
    }


def product_paths(batch_id: str, accepted_batch: dict[str, object]) -> list[str]:
    if batch_id == "B6":
        return [p for p in accepted_batch["allowed_paths"] if p.startswith("configs/")]
    if batch_id == "B7":
        return []
    return accepted_batch["allowed_paths"]


def path_authorization(contract: dict[str, object]) -> list[dict[str, object]]:
    accepted = {b["batch_id"]: b for b in contract["implementation_batches"]}
    immutable_forbidden = ["pnpm-lock.yaml", "scripts/commissioning/**", "docs/BRD/**", "docs/UXF/**", "docs/baselines/v2.3/**/*APPROVAL*", "factory/**", "knowledge/**", "runtime/**", "tools/ysf/**", "integrations/**", "infrastructure/**", ".git/**"]
    result = []
    for bid in BATCHES:
        support = supporting_paths(bid)
        product = product_paths(bid, accepted[bid])
        exact = sorted(set(product + support["TEST_AND_VALIDATION_PATH"] + support["COMMAND_REGISTRATION_PATH"] + support["EVIDENCE_OUTPUT_PATH"] + support["MANIFEST_AND_INDEPENDENT_VALIDATOR_PATH"]))
        result.append({"batch_id": bid, "accepted_protected_paths": contract["design"]["path_policy"]["protected"], "immutable_amendment_forbidden_paths": immutable_forbidden, "PRODUCT_IMPLEMENTATION_PATH": product, **support, "exact_authorized_paths": exact, "wildcard_authorization": False})
    return result


def ids_for_command(command_id: str, b1_ids: set[str], commands: dict[str, dict[str, object]]) -> list[str]:
    if command_id in commands:
        return sorted(b1_ids & set(commands[command_id]["mapping_ids"]))
    return sorted(b1_ids)


def b1_path_matrix(contract: dict[str, object], auth: list[dict[str, object]]) -> list[dict[str, object]]:
    commands = {c["command_id"]: c for c in contract["commands"]}
    b1 = next(b for b in contract["implementation_batches"] if b["batch_id"] == "B1")
    b1_ids = set(b1["mapping_ids"])
    db_ids = ids_for_command("vs001:db:migrate", b1_ids, commands)
    fixture_ids = sorted(b1_ids)
    definitions = {
        "database/config/schema.prisma": ("PRODUCT_IMPLEMENTATION_PATH", "relational schema and integrity declarations", ["vs001:db:migrate", "vs001:test:db-integrity"], db_ids, False),
        "database/migrations/20260719000000_vs001_public_catalog/migration.sql": ("PRODUCT_IMPLEMENTATION_PATH", "forward-only VS001 migration", ["vs001:db:migrate", "vs001:test:db-integrity"], db_ids, False),
        "database/seed-mechanism/vs001-fixtures.ts": ("PRODUCT_IMPLEMENTATION_PATH", "controlled fixture definitions separated from production seed", ["vs001:fixtures:load", "vs001:fixtures:cleanup", "vs001:test:db-integrity"], fixture_ids, False),
        "scripts/vs001/cleanup.mjs": ("PRODUCT_IMPLEMENTATION_PATH", "owned fixture cleanup orchestration", ["vs001:fixtures:cleanup"], fixture_ids, False),
        "scripts/vs001/fixtures.mjs": ("PRODUCT_IMPLEMENTATION_PATH", "owned fixture load orchestration", ["vs001:fixtures:load"], fixture_ids, False),
        "tests/vs001/data/b1-public-catalog-integrity.test.ts": ("TEST_AND_VALIDATION_PATH", "real PostgreSQL B1 integrity behavior", ["vs001:test:db-integrity"], fixture_ids, False),
        "package.json": ("COMMAND_REGISTRATION_PATH", "only seven exact VS001 B1 script registrations", ["vs001:db:migrate", "vs001:fixtures:load", "vs001:fixtures:cleanup", "vs001:test:db-integrity", "vs001:audit:docker", "vs001:batch:validate", "vs001:batch:clean-checkout"], fixture_ids, False),
        "scripts/vs001/db-migrate.mjs": ("COMMAND_REGISTRATION_PATH", "migration command implementation", ["vs001:db:migrate"], db_ids, False),
        "scripts/vs001/test-db-integrity.mjs": ("COMMAND_REGISTRATION_PATH", "database integrity test runner", ["vs001:test:db-integrity"], fixture_ids, False),
        "scripts/vs001/audit-docker.mjs": ("COMMAND_REGISTRATION_PATH", "owned Docker before/after preservation audit", ["vs001:audit:docker"], fixture_ids, False),
        "scripts/vs001/validate-batch.mjs": ("COMMAND_REGISTRATION_PATH", "batch-scoped evidence and boundary validation", ["vs001:batch:validate"], fixture_ids, False),
        "scripts/vs001/bootstrap-batch-clean-checkout.mjs": ("COMMAND_REGISTRATION_PATH", "B1-only clean-checkout orchestration", ["vs001:batch:clean-checkout"], fixture_ids, False),
    }
    evidence_owners = {
        "implementation-report.json": ["vs001:batch:validate"],
        "mapping-evidence.json": ["vs001:test:db-integrity"],
        "command-results.json": ["vs001:batch:validate"],
        "database-evidence.json": ["vs001:db:migrate"],
        "boundary-audit.json": ["vs001:batch:validate"], "docker-preservation.json": ["vs001:audit:docker"],
        "cleanup-proof.json": ["vs001:batch:clean-checkout"],
        "candidate-manifest.json": ["vs001:batch:validate"],
    }
    for name, owners in evidence_owners.items():
        definitions[f"artifacts/vs001/b1/{name}"] = ("EVIDENCE_OUTPUT_PATH", f"content-addressed B1 {name.removesuffix('.json').replace('-', ' ')}", owners, fixture_ids, True)
    definitions["scripts/vs001/validate-b1-candidate.mjs"] = ("MANIFEST_AND_INDEPENDENT_VALIDATOR_PATH", "independent B1 evidence and Git-object validator", ["vs001:batch:validate", "vs001:batch:clean-checkout"], fixture_ids, False)
    definitions["tests/vs001/governance/b1-candidate.test.mjs"] = ("MANIFEST_AND_INDEPENDENT_VALIDATOR_PATH", "B1 governance mutation and clean-checkout tests", ["vs001:batch:validate", "vs001:batch:clean-checkout"], fixture_ids, False)
    bindings = b1["decision_binding_ids"]
    return [{"path": path, "path_category": spec[0], "semantic_purpose": spec[1], "owning_command_ids": spec[2], "mapping_ids": spec[3], "decision_binding_ids": bindings, "implementation_batch": "B1", "evidence_batch": "B1", "generated": spec[4], "mutation_and_cleanup_responsibility": "producer writes atomically under run identity; cleanup removes only run-owned resources and evidence remains immutable once candidate is signed"} for path, spec in sorted(definitions.items())]


def later_command_paths() -> dict[str, list[str]]:
    return {
        "vs001:test:api": ["package.json", "scripts/vs001/test-api.mjs", "tests/vs001/api/public-catalog.integration.test.ts", "artifacts/vs001/b4/mapping-evidence.json", "artifacts/vs001/b4/command-results.json", "artifacts/vs001/b4/boundary-audit.json"],
        "vs001:test:not-found": ["package.json", "scripts/vs001/test-not-found.mjs", "tests/vs001/api/public-catalog-not-found.test.ts", "artifacts/vs001/b4/mapping-evidence.json", "artifacts/vs001/b4/command-results.json", "artifacts/vs001/b4/boundary-audit.json"],
        "vs001:test:web": ["package.json", "scripts/vs001/test-web.mjs", "tests/vs001/browser/public-catalog.spec.ts", "artifacts/vs001/b5/mapping-evidence.json", "artifacts/vs001/b5/command-results.json", "artifacts/vs001/b5/boundary-audit.json"],
        "vs001:audit:disclosure": ["package.json", "scripts/vs001/audit-disclosure.mjs", "tests/vs001/security/public-catalog-disclosure.test.ts", "artifacts/vs001/b6/mapping-evidence.json", "artifacts/vs001/b6/command-results.json", "artifacts/vs001/b6/boundary-audit.json"],
        "vs001:test:consistency": ["package.json", "scripts/vs001/test-consistency.mjs", "tests/vs001/api/public-catalog.integration.test.ts", "tests/vs001/browser/public-catalog.spec.ts", "tests/vs001/data/public-catalog-integrity.test.ts", "artifacts/vs001/b6/mapping-evidence.json", "artifacts/vs001/b6/command-results.json", "artifacts/vs001/b6/database-evidence.json"],
        "vs001:evidence:validate": ["package.json", "scripts/vs001/validate-evidence.mjs", "scripts/vs001/validate-b6-candidate.mjs", "tests/vs001/governance/b6-candidate.test.mjs", "artifacts/vs001/b7/final-evidence.json"] + [f"artifacts/vs001/b6/{name}" for name in ("implementation-report.json", "mapping-evidence.json", "command-results.json", "database-evidence.json", "boundary-audit.json", "docker-preservation.json", "cleanup-proof.json", "candidate-manifest.json")],
        "vs001:bootstrap:clean-checkout": ["package.json", "scripts/vs001/bootstrap-clean-checkout.mjs", "tests/vs001/governance/full-clean-checkout.test.mjs", "scripts/vs001/validate-b7-candidate.mjs", "tests/vs001/governance/b7-candidate.test.mjs"] + [f"artifacts/vs001/b7/{name}" for name in ("implementation-report.json", "mapping-evidence.json", "command-results.json", "database-evidence.json", "boundary-audit.json", "docker-preservation.json", "cleanup-proof.json", "candidate-manifest.json")],
    }


def command_rows(contract: dict[str, object], matrix: list[dict[str, object]]) -> list[dict[str, object]]:
    accepted = {c["command_id"]: c for c in contract["commands"]}
    plan = schedule()
    owners = {}
    for row in matrix:
        for cid in row["owning_command_ids"]:
            owners.setdefault(cid, []).append(row["path"])
    result = []
    for cid in sorted(plan):
        row = accepted[cid]
        allowed = sorted(owners.get(cid, [])) if plan[cid]["implementation_owner_batch"] == "B1" else sorted(later_command_paths()[cid])
        result.append({"command_id": cid, **plan[cid], "exact_mapping_ids": row["mapping_ids"], "exact_decision_binding_ids": row["decision_binding_ids"], "process_contract": row["process_contract"], "evidence_output": row["evidence_output"], "cleanup": row["cleanup"], "failure": row["failure"], "allowed_paths": allowed})
    return result


def package_script_bindings() -> list[dict[str, object]]:
    rows = [
        ("vs001:db:migrate", "node scripts/vs001/db-migrate.mjs", "scripts/vs001/db-migrate.mjs", []),
        ("vs001:fixtures:load", "node scripts/vs001/fixtures.mjs load", "scripts/vs001/fixtures.mjs", ["load"]),
        ("vs001:fixtures:cleanup", "node scripts/vs001/cleanup.mjs", "scripts/vs001/cleanup.mjs", []),
        ("vs001:test:db-integrity", "node scripts/vs001/test-db-integrity.mjs", "scripts/vs001/test-db-integrity.mjs", []),
        ("vs001:audit:docker", "node scripts/vs001/audit-docker.mjs", "scripts/vs001/audit-docker.mjs", []),
        ("vs001:batch:validate", "node scripts/vs001/validate-batch.mjs", "scripts/vs001/validate-batch.mjs", []),
        ("vs001:batch:clean-checkout", "node scripts/vs001/bootstrap-batch-clean-checkout.mjs", "scripts/vs001/bootstrap-batch-clean-checkout.mjs", []),
    ]
    return [{
        "package_json_key": key, "exact_command_string": command, "target_executable_file": target,
        "owning_command_id": key, "implementation_batch": "B1", "allowed_arguments": args,
        "allowed_environment_behavior": "inherit only accepted commissioning environment plus run-scoped VS001 identifiers; no secrets embedded",
        "may_invoke_another_script": False, "forbidden_shell_expansion": ["&&", "||", ";", "|", ">", "<", "$(", "`"],
    } for key, command, target, args in rows]


def producer_command_catalog() -> list[dict[str, object]]:
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
    channels_by_command = {
        "vs001:db:migrate": ["DATA"],
        "vs001:test:db-integrity": ["DATA"], "vs001:test:api": ["API"], "vs001:test:not-found": ["API"],
        "vs001:test:web": ["UI"], "vs001:audit:disclosure": ["SECURITY"],
        "vs001:test:consistency": ["DATA", "API", "UI"],
        "vs001:evidence:validate": ["DATA", "API", "UI", "SECURITY", "PROCESS", "COMPOSITE_REVALIDATION"],
        "vs001:batch:validate": ["PROCESS"], "vs001:batch:clean-checkout": ["PROCESS"],
    }
    plan = schedule()
    rows = []
    for command_id in sorted(writes):
        if command_id in plan:
            authority = {"kind": "ACCEPTED_C1_R2_FOCUSED_COMMAND", "earliest_executable_batch": plan[command_id]["earliest_executable_batch"], "required_evidence_batches": plan[command_id]["required_evidence_batches"]}
        else:
            authority = {"kind": "A2_BATCH_SCOPED_COMMAND", "registration_batch": "B1", "scheduled_batches": BATCHES if command_id.endswith("clean-checkout") else BATCHES[:-1]}
        authority_fingerprint = sha256(canonical(authority))
        rows.append({
            "command_id": command_id, "schedule_authority": authority,
            "schedule_authority_fingerprint": authority_fingerprint,
            "scheduled_batches": sorted(writes[command_id], key=lambda x: int(x[1:])),
            "write_authorized_paths_by_batch": writes[command_id],
            "supported_observation_channels": channels_by_command[command_id],
            "path_authorization_identities": {bid: "CPA-" + sha256(canonical([command_id, bid, path]))[:24] for bid, path in writes[command_id].items()},
        })
    return rows


def choose_producer(mapping: dict[str, object], row: dict[str, object], bid: str) -> tuple[str, str]:
    required = row["required_observation_channels"]
    commands = set(mapping["validation_command_ids"])
    if bid == "B1" and "vs001:db:migrate" in commands:
        return "vs001:db:migrate", "DATA"
    if bid in ("B1", "B3") and "DATA" in required and "vs001:test:db-integrity" in commands:
        return "vs001:test:db-integrity", "DATA"
    if bid == "B4" and "API" in required:
        not_found_tokens = ("NOT_FOUND", "UNKNOWN", "MALFORMED", "UNAVAILABLE", "INACTIVE", "UNPUBLISHED", "WRONG_STOREFRONT")
        if "vs001:test:not-found" in commands and any(token in row["mapping_id"] for token in not_found_tokens):
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


def fixture_identity(mapping: dict[str, object]) -> tuple[str, dict[str, object]]:
    fixture = mapping["controlled_fixture"]
    fixture_id = fixture.get("fixture_id") if isinstance(fixture, dict) else None
    if not fixture_id:
        fixture_id = "FIX-" + sha256(canonical(fixture))[:16]
    return fixture_id, {"authority_fingerprint": mapping["authority"]["fingerprint"], "available_from_batch": mapping["implementation_batch_ids"][0], "fixture_sha256": sha256(canonical(fixture))}


def lineage_records(closures: list[dict[str, object]], accepted_mappings: dict[str, dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    catalog = {row["command_id"]: row for row in producer_command_catalog()}
    cleanup = []
    for bid in BATCHES:
        command = catalog["vs001:batch:clean-checkout"]
        cleanup.append({
            "cleanup_evidence_record_id": f"CLEANUP-{bid}", "producer_batch": bid,
            "producer_command_id": "vs001:batch:clean-checkout", "evidence_file_path": command["write_authorized_paths_by_batch"][bid],
            "evidence_record_pointer": f"/cleanup/CLEANUP-{bid}", "resource_scope": f"only run-owned VS001 {bid} resources",
            "proof_requirement": "independent before/after resource observation plus nonzero forced-failure cleanup verification",
        })
    records = []
    by_mapping: dict[str, list[str]] = {}
    for row in closures:
        mapping = accepted_mappings[row["mapping_id"]]
        fixture_id, fixture_authority = fixture_identity(mapping)
        fixture_authority["available_from_batch"] = min([mapping["implementation_batch_ids"][0], *row["provisional_evidence_batches"]], key=lambda x: int(x[1:]))
        provisional_ids = [f"ELR-{row['mapping_id']}-{bid}-PROVISIONAL" for bid in row["provisional_evidence_batches"]]
        final_id = f"ELR-{row['mapping_id']}-B7-FINAL-REVALIDATION"
        by_mapping[row["mapping_id"]] = provisional_ids
        for index, bid in enumerate(row["provisional_evidence_batches"]):
            record_id = provisional_ids[index]
            producer, channel = choose_producer(mapping, row, bid)
            command = catalog[producer]
            next_ids = provisional_ids[index + 1:index + 2] or [final_id]
            records.append({
                "evidence_record_id": record_id, "mapping_id": row["mapping_id"], "record_kind": "PROVISIONAL_OBSERVATION",
                "producer_batch": bid, "producer_command_id": producer,
                "producer_command_schedule_authority": command["schedule_authority_fingerprint"],
                "evidence_file_path": command["write_authorized_paths_by_batch"][bid],
                "evidence_record_pointer": f"/records/{record_id}",
                "exact_command_path_authorization_identity": command["path_authorization_identities"][bid],
                "observation_channel": channel, "controlled_fixture_id": fixture_id, "fixture_authority": fixture_authority,
                "expected_toolchain_environment_identity": {"node": "v24.18.0", "pnpm": "11.13.1", "corepack": True, "postgresql": "18.4 when DATA/API/UI/SECURITY runtime is required", "accepted_commissioning_environment": True},
                "implementation_candidate_commit_tree_requirement": "signed accepted implementation-batch candidate commit and tree required at execution",
                "content_hash_or_git_blob_requirement": "SHA-256 plus Git blob identity required; stored PASS is insufficient",
                "cleanup_evidence_record_id": f"CLEANUP-{bid}", "downstream_dependency_record_ids": next_ids,
                "input_evidence_record_ids": [], "final_revalidation_record_id": final_id,
                "runtime_status": "NOT_EXECUTED",
            })
        final_command = catalog["vs001:evidence:validate"]
        records.append({
            "evidence_record_id": final_id, "mapping_id": row["mapping_id"], "record_kind": "FINAL_REVALIDATION",
            "producer_batch": "B7", "producer_command_id": "vs001:evidence:validate",
            "producer_command_schedule_authority": final_command["schedule_authority_fingerprint"],
            "evidence_file_path": "artifacts/vs001/b7/final-evidence.json", "evidence_record_pointer": f"/records/{final_id}",
            "exact_command_path_authorization_identity": final_command["path_authorization_identities"]["B7"],
            "observation_channel": "COMPOSITE_REVALIDATION", "controlled_fixture_id": fixture_id, "fixture_authority": fixture_authority,
            "expected_toolchain_environment_identity": {"node": "v24.18.0", "pnpm": "11.13.1", "corepack": True, "postgresql": "18.4 when runtime revalidation is required", "accepted_commissioning_environment": True},
            "implementation_candidate_commit_tree_requirement": "resolve every accepted batch commit/tree and final candidate tree",
            "content_hash_or_git_blob_requirement": "resolve content and recompute SHA-256/Git blob; count or stored hash alone is insufficient",
            "cleanup_evidence_record_id": "CLEANUP-B7", "downstream_dependency_record_ids": [],
            "input_evidence_record_ids": provisional_ids, "final_revalidation_record_id": final_id,
            "runtime_status": "NOT_EXECUTED",
        })
    files: dict[tuple[str, str, str], list[str]] = {}
    for record in records:
        key = (record["producer_batch"], record["producer_command_id"], record["evidence_file_path"])
        files.setdefault(key, []).append(record["evidence_record_id"])
    for record in cleanup:
        key = (record["producer_batch"], record["producer_command_id"], record["evidence_file_path"])
        files.setdefault(key, []).append(record["cleanup_evidence_record_id"])
    file_catalog = [{
        "evidence_file_id": "EFILE-" + sha256(canonical([bid, command, path]))[:20], "path": path, "owning_command_id": command,
        "producer_batch": bid, "contained_record_ids": sorted(ids), "allowed_record_pointer_namespace": "/records/" if not all(x.startswith("CLEANUP-") for x in ids) else "/cleanup/",
        "schema": "VS001_EVIDENCE_FILE_V1", "authored_or_generated": "GENERATED_BY_REAL_EXECUTION",
        "content_addressing_rule": "signed candidate Git blob plus independently recomputed SHA-256",
        "cleanup_retention_responsibility": "runtime resources are cleaned; signed evidence bytes are immutable and retained",
        "downstream_consumers": ["vs001:evidence:validate", "vs001:bootstrap:clean-checkout"] if bid != "B7" else ["vs001:bootstrap:clean-checkout"],
    } for (bid, command, path), ids in sorted(files.items())]
    existing = {(x["producer_batch"], x["path"]): x for x in file_catalog}
    plan = schedule()
    for bid in BATCHES:
        focused = sorted(cid for cid, spec in plan.items() if bid in spec["required_evidence_batches"] and int(spec["earliest_executable_batch"][1:]) <= int(bid[1:]))
        for path in supporting_paths(bid)["EVIDENCE_OUTPUT_PATH"]:
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
    for row in file_catalog:
        row.setdefault("source_command_ids", [row["owning_command_id"]])
        row.setdefault("support_record_ids", [f"CMDREC-{row['producer_batch']}-{row['owning_command_id'].replace(':', '-')}"])
        row.setdefault("aggregator_authority", "NO_CROSS_COMMAND_AGGREGATION")
    file_catalog.sort(key=lambda x: (int(x["producer_batch"][1:]), x["path"], x["owning_command_id"]))
    artifacts, support_records, support_revalidations, cleanup_support = freeze_support_artifacts(records, file_catalog)
    return records, support_records, support_revalidations, artifacts, cleanup_support


def command_schedule_authority(command_id: str) -> dict[str, object]:
    plan = schedule()
    if command_id in plan:
        return {
            "authority_kind": "ACCEPTED_C1_R2_FOCUSED_COMMAND",
            "command_id": command_id,
            "earliest_executable_batch": plan[command_id]["earliest_executable_batch"],
            "required_evidence_batches": plan[command_id]["required_evidence_batches"],
        }
    if command_id == "vs001:batch:validate":
        return {"authority_kind": "A2_BATCH_SCOPED_COMMAND", "command_id": command_id, "scheduled_batches": BATCHES[:-1]}
    if command_id == "vs001:batch:clean-checkout":
        return {"authority_kind": "A2_BATCH_SCOPED_COMMAND", "command_id": command_id, "scheduled_batches": BATCHES}
    raise RuntimeError(f"unknown executable support command: {command_id}")


def command_is_scheduled(command_id: str, batch_id: str) -> bool:
    authority = command_schedule_authority(command_id)
    if "scheduled_batches" in authority:
        return batch_id in authority["scheduled_batches"]
    return batch_id in authority["required_evidence_batches"] and int(batch_id[1:]) >= int(authority["earliest_executable_batch"][1:])


def support_kind(path: str) -> str:
    name = Path(path).name
    return {
        "candidate-manifest.json": "CANDIDATE_MANIFEST",
        "implementation-report.json": "IMPLEMENTATION_INVENTORY_AND_REPORT",
        "command-results.json": "COMMAND_RESULT_AND_EXIT_IDENTITY",
        "boundary-audit.json": "PROTECTED_BOUNDARY_AUDIT",
        "docker-preservation.json": "DOCKER_BEFORE_AFTER_PRESERVATION",
        "cleanup-proof.json": "RESOURCE_CLEANUP_AND_RETENTION_PROOF",
        "database-evidence.json": "DATABASE_EXECUTION_SUPPORT",
        "mapping-evidence.json": "MAPPING_EVIDENCE_CONTAINER_SUPPORT",
        "final-evidence.json": "FINAL_DUAL_UNION_CONTAINER_SUPPORT",
    }[name]


def freeze_support_artifacts(
    lineage: list[dict[str, object]], legacy_files: list[dict[str, object]]
) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    """Turn every operational file/reference into file-bound immutable records.

    Mapping evidence remains the 767-record population. Operational support is
    a disjoint catalog; no support record claims direct acceptance evidence.
    """
    lineage_ids = {row["evidence_record_id"] for row in lineage}
    final_by_mapping = {
        row["mapping_id"]: row["evidence_record_id"]
        for row in lineage
        if row["record_kind"] == "FINAL_REVALIDATION"
    }
    provisional_by_batch: dict[str, set[str]] = {bid: set() for bid in BATCHES}
    for row in lineage:
        if row["record_kind"] == "PROVISIONAL_OBSERVATION":
            provisional_by_batch[row["producer_batch"]].add(final_by_mapping[row["mapping_id"]])

    artifacts: list[dict[str, object]] = []
    support_records: list[dict[str, object]] = []
    support_by_batch: dict[str, list[dict[str, object]]] = {bid: [] for bid in BATCHES}
    cleanup_support_by_batch: dict[str, str] = {}

    for legacy in legacy_files:
        batch_id = legacy["producer_batch"]
        mapping_ids = sorted(record_id for record_id in legacy["contained_record_ids"] if record_id in lineage_ids)
        cleanup_ids = sorted(record_id for record_id in legacy["contained_record_ids"] if record_id.startswith("CLEANUP-"))
        category = "MAPPING_EVIDENCE_ARTIFACT" if mapping_ids else "EXECUTION_SUPPORT_ARTIFACT"
        source_commands = sorted(set(legacy["source_command_ids"]))
        artifact_id = "ART-" + sha256(canonical([batch_id, legacy["path"], category]))[:24]
        contained_support_ids: list[str] = []

        if category == "EXECUTION_SUPPORT_ARTIFACT":
            for command_id in source_commands:
                if not command_is_scheduled(command_id, batch_id):
                    raise RuntimeError(f"support producer {command_id} is not scheduled in {batch_id}")
                support_id = "SUP-" + sha256(canonical([batch_id, legacy["path"], command_id]))[:28]
                revalidation_id = "SUPREVAL-" + support_id.removeprefix("SUP-")
                schedule_authority = command_schedule_authority(command_id)
                required_mapping_finals = sorted(provisional_by_batch[batch_id]) if batch_id != "B7" else sorted(final_by_mapping.values())
                record = {
                    "support_record_id": support_id,
                    "artifact_file_path": legacy["path"],
                    "record_pointer": f"/support_records/{support_id}",
                    "support_kind": support_kind(legacy["path"]),
                    "producer_batch": batch_id,
                    "producer_command_id": command_id,
                    "command_schedule_authority": schedule_authority,
                    "command_schedule_authority_fingerprint": sha256(canonical(schedule_authority)),
                    "exact_command_path_relation_identity": "CPR-" + sha256(canonical([command_id, batch_id, legacy["path"], "SUPPORT_RECORD_V1"]))[:28],
                    "schema_identifier": "VS001_EXECUTION_SUPPORT_RECORD",
                    "schema_version": "1.0.0",
                    "implementation_candidate_commit_tree_requirement": "signed accepted implementation-batch candidate commit and tree required at execution",
                    "content_sha256_or_git_blob_requirement": "resolve the exact artifact bytes and pointer payload, recompute SHA-256 and Git blob; stored PASS and aggregate count are insufficient",
                    "expected_toolchain_environment_identity": {"node": "v24.18.0", "pnpm": "11.13.1", "corepack": True, "accepted_commissioning_environment": True, "postgresql": "18.4 only when the command contract requires PostgreSQL"},
                    "resource_ownership": f"only run-owned VS001 {batch_id} resources and the file-bound {support_id} record",
                    "cleanup_retention_proof": "runtime resources are removed by the batch cleanup record; signed support bytes remain immutable and addressable",
                    "cleanup_evidence_record_id": None,
                    "downstream_consumer_record_ids": [revalidation_id],
                    "b7_support_revalidation_record_id": revalidation_id,
                    "required_by_mapping_final_revalidation_record_ids": required_mapping_finals,
                    "direct_acceptance_evidence": False,
                    "runtime_status": "NOT_EXECUTED",
                }
                support_records.append(record)
                support_by_batch[batch_id].append(record)
                contained_support_ids.append(support_id)
                if cleanup_ids and command_id == "vs001:batch:clean-checkout":
                    cleanup_support_by_batch[batch_id] = support_id

        artifacts.append({
            "artifact_file_id": artifact_id,
            "path": legacy["path"],
            "artifact_category": category,
            "primary_owning_command_id": legacy["owning_command_id"],
            "producer_batch": batch_id,
            "producer_command_ids": source_commands if category == "EXECUTION_SUPPORT_ARTIFACT" else sorted({row["producer_command_id"] for row in lineage if row["evidence_record_id"] in mapping_ids}),
            "contained_mapping_lineage_record_ids": mapping_ids,
            "contained_support_record_ids": sorted(contained_support_ids),
            "contained_support_revalidation_record_ids": [],
            "allowed_pointer_namespaces": ["/records/"] if category == "MAPPING_EVIDENCE_ARTIFACT" else ["/support_records/"],
            "schema": "VS001_MAPPING_EVIDENCE_FILE_V1" if category == "MAPPING_EVIDENCE_ARTIFACT" else "VS001_EXECUTION_SUPPORT_FILE_V1",
            "authored_or_generated": legacy["authored_or_generated"],
            "content_addressing_rule": legacy["content_addressing_rule"],
            "cleanup_retention_responsibility": legacy["cleanup_retention_responsibility"],
            "downstream_consumers": legacy["downstream_consumers"],
            "category_change_requires_new_signed_authority": True,
            "direct_acceptance_closure_claimed": category == "MAPPING_EVIDENCE_ARTIFACT",
        })

    if set(cleanup_support_by_batch) != set(BATCHES):
        raise RuntimeError(f"missing cleanup support records: {sorted(set(BATCHES) - set(cleanup_support_by_batch))}")
    for record in support_records:
        record["cleanup_evidence_record_id"] = cleanup_support_by_batch[record["producer_batch"]]
    for record in lineage:
        record["cleanup_evidence_record_id"] = cleanup_support_by_batch[record["producer_batch"]]

    support_revalidations: list[dict[str, object]] = []
    final_artifact = next(row for row in artifacts if row["path"] == "artifacts/vs001/b7/final-evidence.json")
    for source in sorted(support_records, key=lambda row: row["support_record_id"]):
        revalidation_id = source["b7_support_revalidation_record_id"]
        support_revalidations.append({
            "support_revalidation_record_id": revalidation_id,
            "source_support_record_id": source["support_record_id"],
            "producer_batch": "B7",
            "producer_command_id": "vs001:evidence:validate",
            "artifact_file_path": "artifacts/vs001/b7/final-evidence.json",
            "record_pointer": f"/support_revalidation/{revalidation_id}",
            "required_source_resolution": {"artifact_file_path": source["artifact_file_path"], "record_pointer": source["record_pointer"], "candidate_commit_tree": True, "content_sha256_or_git_blob": True, "toolchain_environment": True, "cleanup_proof": True},
            "stored_pass_sufficient": False,
            "runtime_status": "NOT_EXECUTED",
        })
    final_artifact["contained_support_revalidation_record_ids"] = sorted(row["support_revalidation_record_id"] for row in support_revalidations)
    final_artifact["allowed_pointer_namespaces"] = ["/records/", "/support_revalidation/"]
    final_artifact["producer_command_ids"] = sorted(set(final_artifact["producer_command_ids"] + ["vs001:evidence:validate"]))

    artifacts.sort(key=lambda row: (int(row["producer_batch"][1:]), row["path"]))
    support_records.sort(key=lambda row: row["support_record_id"])
    return artifacts, support_records, support_revalidations, [record for record in support_records if record["support_kind"] == "RESOURCE_CLEANUP_AND_RETENTION_PROOF"]


def command_path_record_closure(
    lineage: list[dict[str, object]],
    support_records: list[dict[str, object]],
    support_revalidations: list[dict[str, object]],
    artifacts: list[dict[str, object]],
) -> list[dict[str, object]]:
    command_ids = sorted(set(schedule()) | {"vs001:batch:validate", "vs001:batch:clean-checkout"})
    result = []
    for cid in command_ids:
        mapping_records = sorted(x["evidence_record_id"] for x in lineage if x["producer_command_id"] == cid)
        produced_support = sorted(x["support_record_id"] for x in support_records if x["producer_command_id"] == cid)
        produced_revalidations = sorted(x["support_revalidation_record_id"] for x in support_revalidations if x["producer_command_id"] == cid)
        paths = sorted({x["artifact_file_path"] for x in support_records if x["producer_command_id"] == cid} | {x["evidence_file_path"] for x in lineage if x["producer_command_id"] == cid} | {x["artifact_file_path"] for x in support_revalidations if x["producer_command_id"] == cid})
        artifact_ids = sorted(x["artifact_file_id"] for x in artifacts if x["path"] in paths)
        role = "FINAL_ORCHESTRATOR" if cid == "vs001:bootstrap:clean-checkout" else ("MAPPING_AND_SUPPORT_PRODUCER" if mapping_records and produced_support else ("MAPPING_RECORD_PRODUCER" if mapping_records else "EXECUTION_SUPPORT_RECORD_PRODUCER"))
        result.append({
            "command_id": cid,
            "relation_role": role,
            "authorized_artifact_file_ids": artifact_ids,
            "authorized_artifact_paths": paths,
            "mapping_lineage_record_ids_produced": mapping_records,
            "support_record_ids_produced": produced_support,
            "support_revalidation_record_ids_produced": produced_revalidations,
            "executable_record_count": len(mapping_records) + len(produced_support) + len(produced_revalidations),
            "direct_acceptance_evidence": bool(mapping_records),
            "orphan": not bool(mapping_records or produced_support or produced_revalidations),
        })
    return result


def batch_matrix(contract: dict[str, object], closures: list[dict[str, object]], auth: list[dict[str, object]], plan: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    accepted = {b["batch_id"]: b for b in contract["implementation_batches"]}
    all_ids = sorted(x["mapping_id"] for x in closures)
    retained: set[str] = set()
    closed: set[str] = set()
    result = []
    for index, bid in enumerate(BATCHES, 1):
        provisional = sorted(x["mapping_id"] for x in closures if bid in x["provisional_evidence_batches"])
        retained.update(provisional)
        newly_closed = all_ids if bid == "B7" else []
        closed.update(newly_closed)
        paths = next(x for x in auth if x["batch_id"] == bid)
        executable = sorted(cid for cid, row in plan.items() if bid in row["required_evidence_batches"] and int(row["earliest_executable_batch"][1:]) <= index)
        result.append({"batch_id": bid, "order": index, "prerequisite_batch_ids": accepted[bid]["prerequisite_batch_ids"], "newly_implemented_mapping_ids": accepted[bid]["mapping_ids"], "per_batch_provisional_evidence_mapping_ids": provisional, "cumulative_retained_evidence_mapping_ids": sorted(retained), "newly_final_closed_mapping_ids": newly_closed, "cumulative_final_closed_mapping_ids": sorted(closed), "decision_binding_ids": accepted[bid]["decision_binding_ids"], "executable_focused_command_ids": executable, "deferred_focused_command_ids": sorted(cid for cid, row in plan.items() if int(row["earliest_executable_batch"][1:]) > index), "inherited_foundation_gate_ids": accepted[bid]["inherited_foundation_gate_ids"], "authorized_paths": paths["exact_authorized_paths"], "completion_gate": "implement assigned artifacts and preserve content-addressed provisional evidence; no final closure" if bid != "B7" else "resolve and revalidate the complete immutable 211-mapping retained-evidence union before one final closure per mapping", "cleanup": "remove only batch-owned runtime resources; signed evidence objects remain immutable and addressable", "evidence_count_semantics": "per_batch_provisional_evidence_mapping_ids is NOT cumulative; cumulative_retained_evidence_mapping_ids is the union of all provisional evidence available through this batch"})
    return result


def render(payload: dict[str, object]) -> str:
    names = ("identity", "authority_blocker", "closure_model", "artifact_taxonomy", "evidence_lineage_contract", "support_record_contract", "lineage_producer_command_catalog", "evidence_file_catalog", "support_record_catalog", "support_revalidation_catalog", "command_path_record_closure", "cleanup_evidence_catalog", "b7_dual_revalidation_contract", "package_script_bindings", "protected_path_policy", "batch_scoped_validation_interface", "inherited_foundation_gate_classification", "b1_path_purpose_owner_matrix", "command_schedule", "path_authorization", "seven_batch_matrix", "non_claims")
    identity = {k: payload[k] for k in ("candidate_id", "supersedes", "purpose", "status", "approval", "next_gate", "runtime_evidence_status", "implementation_authorized")}
    lines = ["# VS001 Implementation Contract Execution-Boundary Amendment A2 Candidate", "", "A2 is a new governance amendment, not A1 correction pass 3. Mapping evidence and execution-support artifacts are disjoint primary categories. Per-batch provisional evidence counts are not cumulative; the cumulative retained set is independently derived.", ""]
    for name in names:
        value = identity if name == "identity" else payload[name]
        lines += [f"<!-- EXEC_BOUNDARY_A2_SECTION:{name} -->", f"## {name}", "", "```json", json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2), "```", ""]
    lines += ["<!-- EXEC_BOUNDARY_A2_CANONICAL_PROJECTION -->", "## canonical_projection", "", "```json", json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")), "```", ""]
    return "\n".join(lines).rstrip() + "\n"


def build_payload() -> dict[str, object]:
    raw = git_bytes(GOVERNING_HEAD, CONTRACT_PATH)
    contract = json.loads(raw)
    mappings = {m["mapping_id"]: m for m in contract["traceability_mappings"]}
    batches = {b["batch_id"]: b for b in contract["implementation_batches"]}
    bindings = {b["binding_id"]: b for b in contract["decision_bindings"]}
    plan = schedule()
    closures = [closure(mappings[mid], plan) for mid in sorted(mappings)]
    auth = path_authorization(contract)
    matrix = b1_path_matrix(contract, auth)
    batch_rows = batch_matrix(contract, closures, auth, plan)
    expected_counts = [(28, 28, 28, 0, 0), (28, 28, 56, 0, 0), (26, 54, 82, 0, 0), (48, 130, 130, 0, 0), (6, 105, 136, 0, 0), (66, 211, 211, 0, 0), (9, 0, 211, 211, 211)]
    actual_counts = [(len(r["newly_implemented_mapping_ids"]), len(r["per_batch_provisional_evidence_mapping_ids"]), len(r["cumulative_retained_evidence_mapping_ids"]), len(r["newly_final_closed_mapping_ids"]), len(r["cumulative_final_closed_mapping_ids"])) for r in batch_rows]
    if actual_counts != expected_counts:
        raise RuntimeError(f"independent batch accounting mismatch: {actual_counts}")
    lineage, support_records, support_revalidations, evidence_files, cleanup_catalog = lineage_records(closures, mappings)
    producer_catalog = producer_command_catalog()
    category_counts = {category: sum(row["artifact_category"] == category for row in evidence_files) for category in ("MAPPING_EVIDENCE_ARTIFACT", "EXECUTION_SUPPORT_ARTIFACT")}
    if sum(category_counts.values()) != 57 or any(not row["contained_mapping_lineage_record_ids"] and not row["contained_support_record_ids"] and not row["contained_support_revalidation_record_ids"] for row in evidence_files):
        raise RuntimeError("artifact taxonomy is not closed")
    command_closure = command_path_record_closure(lineage, support_records, support_revalidations, evidence_files)
    if any(row["orphan"] or row["executable_record_count"] == 0 for row in command_closure):
        raise RuntimeError("command executable-record closure is incomplete")
    return {
        "candidate_id": CANDIDATE_ID, "supersedes": "V23-P2D-VS001-IMPLEMENTATION-CONTRACT-EXECUTION-BOUNDARY-AMENDMENT-A1-R2",
        "rejection_reason_closed": "UNFROZEN_SUPPORT_ARTIFACT_LINEAGE_AND_INCOMPLETE_COMMAND_PATH_RECORD_CLOSURE", "purpose": "BATCH_SCOPED_IMPLEMENTATION_AND_PROGRESSIVE_EVIDENCE_CLOSURE",
        "status": "CANDIDATE", "approval": "PENDING_HUMAN_APPROVAL", "next_gate": "HUMAN_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_EXECUTION_BOUNDARY_AMENDMENT_A2_CANDIDATE_REVIEW",
        "governing_head": GOVERNING_HEAD, "runtime_evidence_status": "NOT_EXECUTED", "implementation_authorized": False, "implementation_correction_passes_consumed": 0,
        "accepted_contract_authority": {"accepted_commit": GOVERNING_HEAD, "git_path": CONTRACT_PATH, "sha256": sha256(raw), "detached_validator_result": "VALID_APPROVED_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_C1_R2"},
        "authorities": contract["authorities"], "frozen_input_accounting": {"batches": 7, "mappings": 211, "decision_bindings": 11, "inherited_foundation_gates": 10, "focused_commands": 12, "batch_distribution": [28, 28, 26, 48, 6, 66, 9], "runtime_evidence_executed": 0},
        "authority_blocker": {"result": "PHASE_2D_VS001_IMPLEMENTATION_B1_AUTHORITY_BLOCKED", "resolution": "exact supporting paths plus independently derived progressive evidence closure; no accepted semantic change"},
        "closure_model": {"states": ["PENDING_IMPLEMENTATION", "BATCH_IMPLEMENTATION_COMPLETE", "PROVISIONAL_EVIDENCE_COMPLETE", "FINAL_ACCEPTANCE_CLOSED"], "per_batch_semantics": "per_batch_provisional_evidence_mapping_ids contains routes produced or exercised in that batch and is not cumulative", "cumulative_semantics": "cumulative_retained_evidence_mapping_ids is the monotonic union of all mapping evidence available through the batch", "final_semantics": "B7 resolves immutable evidence identities, recomputes provenance/hashes/observations, and closes exactly 211 mappings once", "stored_pass_sufficient": False},
        "artifact_taxonomy": {"primary_categories": ["MAPPING_EVIDENCE_ARTIFACT", "EXECUTION_SUPPORT_ARTIFACT"], "exactly_one_primary_category_per_file": True, "artifact_file_count": len(evidence_files), "category_counts": category_counts, "mapping_artifact_rule": "contained_mapping_lineage_record_ids is nonempty and only frozen mapping-lineage records can claim direct acceptance evidence", "support_artifact_rule": "contained_support_record_ids is nonempty; support does not directly close acceptance", "empty_containment_allowed": False, "category_change_requires_new_signed_authority": True},
        "evidence_lineage_contract": {"schema_version": "VS001-EVIDENCE-LINEAGE-2", "content_addressed": True, "overwrite_same_identity_forbidden": True, "accepted_batch_git_object_required": True, "b7_complete_union_required": True, "b7_recomputes": ["Git object provenance", "evidence SHA-256/blob and underlying content", "toolchain/environment identity", "required observation", "cleanup evidence", "producer schedule/path/channel/fixture authority"], "runtime_records_currently_exist": False, "provisional_record_count": 556, "final_revalidation_record_count": 211, "record_count": len(lineage), "filesystem_path_and_json_pointer_are_distinct": True},
        "support_record_contract": {"schema_version": "VS001-EXECUTION-SUPPORT-LINEAGE-1", "support_record_count": len(support_records), "support_revalidation_record_count": len(support_revalidations), "globally_unique_file_bound_identity": True, "unfrozen_cmdrec_identity_count": 0, "direct_acceptance_evidence": False, "stored_pass_sufficient": False, "runtime_records_currently_exist": False},
        "evidence_lineage_requirements": lineage,
        "lineage_producer_command_catalog": producer_catalog,
        "evidence_file_catalog": evidence_files,
        "support_record_catalog": support_records,
        "support_revalidation_catalog": support_revalidations,
        "command_path_record_closure": command_closure,
        "cleanup_evidence_catalog": cleanup_catalog,
        "b7_dual_revalidation_contract": {"final_evidence_path": "artifacts/vs001/b7/final-evidence.json", "mapping_record_namespace": "/records/", "support_revalidation_namespace": "/support_revalidation/", "producer_command_id": "vs001:evidence:validate", "producer_batch": "B7", "bootstrap_consumer_orchestrator_command_id": "vs001:bootstrap:clean-checkout", "producer_and_orchestrator_are_distinct": True, "acceptance_evidence_union": {"signed_provisional_mapping_record_ids": sorted(x["evidence_record_id"] for x in lineage if x["record_kind"] == "PROVISIONAL_OBSERVATION"), "final_mapping_revalidation_record_ids": sorted(x["evidence_record_id"] for x in lineage if x["record_kind"] == "FINAL_REVALIDATION"), "mapping_ids": sorted(mappings)}, "execution_support_union": {"source_support_record_ids": sorted(x["support_record_id"] for x in support_records), "support_revalidation_record_ids": sorted(x["support_revalidation_record_id"] for x in support_revalidations), "support_artifact_file_ids": sorted(x["artifact_file_id"] for x in evidence_files if x["artifact_category"] == "EXECUTION_SUPPORT_ARTIFACT")}, "required_revalidations": ["resolve accepted batch commits and trees", "resolve every mapping and support artifact blob and recompute content hashes", "verify producer command, path, pointer, toolchain and environment identity", "inspect or rerun required mapping observations", "verify cleanup and Docker preservation support content", "reject missing, altered, unsigned, superseded or stored-PASS support"], "final_mapping_closure_requires_complete_support_union": True, "runtime_status": "NOT_EXECUTED"},
        "package_script_bindings": package_script_bindings(),
        "protected_path_policy": {"authority_layers": ["accepted protected paths resolved from signed C1-R2", "immutable amendment forbidden paths", "exact future authorized paths"], "stored_policy_booleans_are_authority": False, "package_json_rule": {"batch": "B1", "exact_script_keys": supporting_paths("B1")["package_json_exact_script_keys"], "exact_script_bindings": package_script_bindings(), "all_other_fields_forbidden": True, "dependency_devDependency_version_packageManager_engines_changes_forbidden": True}, "pnpm_lock_yaml_forbidden": True},
        "batch_scoped_validation_interface": {"validate_command": "corepack pnpm vs001:batch:validate -- --batch <B1..B7>", "clean_checkout_command": "corepack pnpm vs001:batch:clean-checkout -- --batch <B1..B7>", "registration_batch": "B1", "implementation_paths": ["scripts/vs001/validate-batch.mjs", "scripts/vs001/bootstrap-batch-clean-checkout.mjs"], "semantics": "validate only artifacts implemented through the named batch, preserve immutable provisional evidence, and fail closed on pending downstream observations", "full_slice_command_reserved": "vs001:bootstrap:clean-checkout at B7"},
        "inherited_foundation_gate_classification": [{"command_id": c["command_id"], "authority": c["authority"], "acceptance_evidence": False, "required_by_batches": c["required_by_batches"], "foundation_purpose": c["foundation_purpose"]} for c in sorted(contract["commands"], key=lambda x: x["command_id"]) if c["command_class"] == "INHERITED_COMMISSIONING_FOUNDATION_GATE"],
        "path_authorization": auth, "b1_path_purpose_owner_matrix": matrix, "command_schedule": command_rows(contract, matrix), "mapping_closure_catalog": closures,
        "b1_mapping_reclassification": [next(x for x in closures if x["mapping_id"] == mid) for mid in batches["B1"]["mapping_ids"]], "seven_batch_matrix": batch_rows,
        "decision_binding_progression": [{"binding_id": bid, "authority_fingerprint": bindings[bid]["authority"]["fingerprint"], "implementation_batches": bindings[bid]["batches"], "final_closure_batch": "B7", "state": "NOT_IMPLEMENTED"} for bid in sorted(bindings)],
        "validation_contract": {"stored_pass_trusted": False, "candidate_builder_is_validator_oracle": False, "candidate_generated_catalog_is_authority": False, "independent_lineage_authority_catalog": True, "independent_support_authority_catalog": True, "future_batch_leakage_error_code": "A2_B1_FUTURE_BATCH_PRODUCT_PATH_LEAKAGE", "required_builder_probe_families": ["empty-artifact-containment", "unfrozen-cmdrec", "support-id-reuse", "support-record-removed", "zero-command-records", "incomplete-b7-support-union", "wrong-docker-support-producer", "missing-cleanup-support", "missing-manifest-support", "coherent-category-change", "stored-support-pass", "mapping-closure-without-support"]},
        "non_claims": ["NOT_B1_IMPLEMENTATION", "NOT_RUNTIME_EVIDENCE", "NOT_ACCEPTANCE_SEMANTIC_CHANGE", "NOT_C1_R2_MODIFICATION", "NOT_POSTGRESQL_OR_DOCKER_EXECUTION", "NOT_BRD_UXF_COMMISSIONING_YADF_DEPLOYMENT_PRODUCTION_WORK"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=ROOT)
    args = parser.parse_args()
    out = args.output_root
    payload = build_payload()
    json_path, md_path, manifest_path = out / JSON_REL, out / MD_REL, out / MANIFEST_REL
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_bytes(canonical(payload))
    md_path.write_text(render(payload), encoding="utf-8", newline="\n")
    hashes = {str(path): sha256((out / path).read_bytes() if (out / path).exists() else (ROOT / path).read_bytes()) for path in (MD_REL, JSON_REL, BUILDER_REL, VALIDATOR_REL, TEST_REL)}
    generated = [str(MD_REL), str(JSON_REL)]
    roots = {
        "mapping_closure_root": sha256(canonical({x["mapping_id"]: sha256(canonical(x)) for x in payload["mapping_closure_catalog"]})),
        "command_schedule_root": sha256(canonical({x["command_id"]: sha256(canonical(x)) for x in payload["command_schedule"]})),
        "seven_batch_root": sha256(canonical({x["batch_id"]: sha256(canonical(x)) for x in payload["seven_batch_matrix"]})),
        "evidence_lineage_root": sha256(canonical({x["evidence_record_id"]: sha256(canonical(x)) for x in payload["evidence_lineage_requirements"]})),
        "b1_path_matrix_root": sha256(canonical({x["path"]: sha256(canonical(x)) for x in payload["b1_path_purpose_owner_matrix"]})),
        "lineage_producer_root": sha256(canonical({x["command_id"]: sha256(canonical(x)) for x in payload["lineage_producer_command_catalog"]})),
        "evidence_file_catalog_root": sha256(canonical({x["artifact_file_id"]: sha256(canonical(x)) for x in payload["evidence_file_catalog"]})),
        "support_record_catalog_root": sha256(canonical({x["support_record_id"]: sha256(canonical(x)) for x in payload["support_record_catalog"]})),
        "support_revalidation_root": sha256(canonical({x["support_revalidation_record_id"]: sha256(canonical(x)) for x in payload["support_revalidation_catalog"]})),
        "package_script_binding_root": sha256(canonical({x["package_json_key"]: sha256(canonical(x)) for x in payload["package_script_bindings"]})),
        "command_path_record_root": sha256(canonical({x["command_id"]: sha256(canonical(x)) for x in payload["command_path_record_closure"]})),
    }
    manifest = {"candidate_id": CANDIDATE_ID, "status": "CANDIDATE", "approval": "PENDING_HUMAN_APPROVAL", "runtime_evidence_status": "NOT_EXECUTED", "implementation_authorized": False, "inventory": INVENTORY, "file_sha256_excluding_manifest": hashes, "generated_payload_aggregate": sha256(canonical([{"path": p, "sha256": hashes[p]} for p in sorted(generated)])), **roots, "staged_tree": "DETACHED_HUMAN_GATE_VALUE", "git_content_aggregate": "DETACHED_HUMAN_GATE_VALUE", "self_reference_policy": "manifest excluded from its own hash domain; staged tree and Git-content aggregate are detached human-gate values"}
    manifest_path.write_bytes(canonical(manifest))
    print("BUILT_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_EXECUTION_BOUNDARY_AMENDMENT_A2")


if __name__ == "__main__":
    main()
