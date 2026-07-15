#!/usr/bin/env python3
"""Validate the Phase 2C versioned acceptance-profile catalog candidate."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PHASE2 = ROOT / "docs/baselines/v2.3/phase-2"
CATALOG_PATH = PHASE2 / "acceptance-profile-catalog.json"
SCHEMA_PATH = PHASE2 / "schemas/acceptance-profile-catalog.schema.json"
GENERATOR = ROOT / "scripts/docs/generate-acceptance-model-candidate.py"
REQUIRED_PROFILE_FIELDS = {
    "profile_id", "version", "title", "semantic_intent", "supported_requirement_types",
    "applicability_rules", "prohibited_uses", "required_bindings", "optional_bindings",
    "observable_verification_contract", "oracle_templates", "evidence_requirements",
    "failure_semantics", "criticality_compatibility", "deterministic_validation_rules",
    "valid_examples", "counterexamples", "matcher_contract",
}
BANNED = (
    "works as expected", "is handled correctly", "appropriate error is returned",
    "requirement is satisfied", "verify the business rule", "system remains consistent",
    "todo", "tbd", "placeholder", "inferred_only",
)


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def binding_tokens(text: str) -> set[str]:
    return set(re.findall(r"\{([a-z][a-z0-9_]*)\}", text))


def validate_schema_shape(schema: dict[str, Any], catalog: dict[str, Any]) -> None:
    require(schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema", "catalog schema draft mismatch")
    for key in schema["required"]:
        require(key in catalog, f"catalog schema required property absent: {key}")
    require(schema["properties"]["status"]["const"] == catalog["status"], "catalog schema status const mismatch")


def validate_profile(profile: dict[str, Any]) -> None:
    pid = profile.get("profile_id", "<missing>")
    require(set(profile) >= REQUIRED_PROFILE_FIELDS, f"incomplete profile: {pid}")
    require(re.fullmatch(r"ACP-[A-Z][A-Z0-9_]+", pid) is not None, f"invalid profile ID: {pid}")
    require(re.fullmatch(r"\d+\.\d+\.\d+", profile["version"]) is not None, f"invalid profile version: {pid}")
    require(profile["supported_requirement_types"], f"profile supports no requirement types: {pid}")
    require(len(profile["applicability_rules"]) >= 3 and len(profile["prohibited_uses"]) >= 3, f"weak applicability boundary: {pid}")
    require(profile["observable_verification_contract"].strip(), f"missing observable verification contract: {pid}")
    require(set(profile["oracle_templates"]) == {"positive", "negative", "edge_boundary"}, f"missing profile oracle: {pid}")
    required = {item["name"] for item in profile["required_bindings"]}
    optional = {item["name"] for item in profile["optional_bindings"]}
    require(required and not (required & optional), f"invalid binding declarations: {pid}")
    require(len(required) == len(profile["required_bindings"]), f"duplicate required binding: {pid}")
    oracle_text = " ".join(profile["oracle_templates"].values())
    used = binding_tokens(oracle_text)
    require(required <= used, f"unused required profile bindings: {pid}: {sorted(required-used)}")
    require(used <= required | optional, f"undeclared oracle bindings: {pid}: {sorted(used-required-optional)}")
    require(not any(term in oracle_text.casefold() for term in BANNED), f"generic/placeholder oracle: {pid}")
    for oracle, text in profile["oracle_templates"].items():
        require(binding_tokens(text), f"oracle has no concrete binding token: {pid}/{oracle}")
        require(len(text.split()) >= 12, f"oracle is non-observable or underspecified: {pid}/{oracle}")
    require(len(profile["evidence_requirements"]) >= 3, f"insufficient evidence requirements: {pid}")
    require(profile["failure_semantics"].strip(), f"missing failure semantics: {pid}")
    require(set(profile["criticality_compatibility"]) <= {"CRITICAL", "HIGH", "NORMAL"}, f"invalid criticality compatibility: {pid}")
    require(len(profile["valid_examples"]) >= 2 and len(profile["counterexamples"]) >= 1, f"missing examples/counterexample: {pid}")
    for example in profile["valid_examples"]:
        bindings = example["bindings"]
        require(set(bindings) == required, f"example binding mismatch: {example['example_id']}")
        require(all(value not in (None, "", []) for value in bindings.values()), f"empty example binding: {example['example_id']}")
        rendered = oracle_text.format(**{key: ", ".join(value) if isinstance(value, list) else value for key, value in bindings.items()})
        require("{" not in rendered and not any(term in rendered.casefold() for term in BANNED), f"invalid rendered example: {example['example_id']}")
    require(profile["matcher_contract"]["requires_type_compatibility"] is True, f"matcher omits type compatibility: {pid}")
    require(profile["matcher_contract"]["requires_structural_binding_extraction"] is True, f"matcher omits binding extraction: {pid}")
    require(profile["matcher_contract"]["keyword_only_match_forbidden"] is True, f"keyword-only matcher allowed: {pid}")


def main() -> int:
    try:
        catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        validate_schema_shape(schema, catalog)
        require(catalog["artifact"] == "V23-P2C-ACCEPTANCE-PROFILE-CATALOG-C1", "catalog artifact mismatch")
        require(catalog["model"] == "HYBRID_ACCEPTANCE_PROFILES_AND_INLINE_CONTRACTS", "catalog model mismatch")
        require(catalog["status"] == "CANDIDATE", "catalog must remain candidate")
        profiles = catalog["profiles"]
        require(catalog["profile_count"] == len(profiles) and len(profiles) >= 20, "catalog profile count mismatch")
        ids = [profile["profile_id"] for profile in profiles]
        require(len(ids) == len(set(ids)), "duplicate stable profile ID")
        for profile in profiles:
            validate_profile(profile)
        require(len(catalog["removed_or_split_profiles"]) >= 4, "profile split decisions not recorded")
        generated = subprocess.run([sys.executable, str(GENERATOR), "--check"], cwd=ROOT, text=True, capture_output=True, check=False)
        require(generated.returncode == 0, f"catalog generation is not deterministic: {generated.stdout}{generated.stderr}")
    except (ValidationError, KeyError, ValueError, json.JSONDecodeError) as error:
        print(f"FAIL — {error}", file=sys.stderr)
        return 1
    print("PASS — VALID_ACCEPTANCE_PROFILE_CATALOG_CANDIDATE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
