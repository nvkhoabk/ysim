#!/usr/bin/env python3
"""Independent business-semantic binding type checker.

This module validates first-class typed values, origins, resolvers and operand
independence.  It deliberately does not import the candidate generator.
"""

from __future__ import annotations

import re
from typing import Any


class TypeModelError(ValueError):
    pass


SYMBOL = re.compile(r"^[A-Z][A-Z0-9_.:-]*$")
ORIGINS = {
    "SOURCE_LITERAL", "APPROVED_DECISION", "CANONICAL_REGISTRY",
    "VERSIONED_POLICY", "VERSIONED_CONFIGURATION", "RUNTIME_OBSERVED",
    "EVIDENCE_OBJECT", "SYNTHETIC_MODEL_FIXTURE",
}
REFERENCE_FIELDS = {
    "namespace", "identifier", "semantic_type", "authoritative_source",
    "resolver_contract", "lifecycle", "origin", "provenance", "inference",
}
PRIMITIVES = {"BOOLEAN": bool, "INTEGER": int, "DECIMAL": (int, float), "TIMESTAMP": str, "DURATION": int}


def fail(code: str, detail: str) -> None:
    raise TypeModelError(f"{code}:{detail}")


def _validate_origin(value: dict[str, Any], allowed: list[str], path: str) -> None:
    origin = value.get("origin")
    if not isinstance(origin, dict) or set(origin) != {"origin_type", "origin_id"}:
        fail("INVALID_ORIGIN", path)
    if origin["origin_type"] not in ORIGINS or origin["origin_type"] not in allowed:
        fail("ORIGIN_NOT_ALLOWED", f"{path}:{origin.get('origin_type')}")
    if not isinstance(origin["origin_id"], str) or not SYMBOL.fullmatch(origin["origin_id"]):
        fail("INVALID_ORIGIN_ID", path)
    provenance = value.get("provenance")
    if not isinstance(provenance, dict) or provenance.get("inference") is not False or not provenance.get("source_fingerprint"):
        fail("INVALID_PROVENANCE", path)


def _generic_inner(semantic_type: str) -> tuple[str, str] | None:
    for prefix in ("SET_OF", "CANONICAL_SET_REF", "RUNTIME_SET_REF"):
        marker = prefix + "<"
        if semantic_type.startswith(marker) and semantic_type.endswith(">"):
            return prefix, semantic_type[len(marker):-1]
    return None


def validate_value(value: Any, expected_type: str, allowed_origins: list[str], catalog: dict[str, Any], path: str) -> None:
    if not isinstance(value, dict):
        fail("UNTYPED_OR_PROSE_VALUE", path)
    if value.get("semantic_type") != expected_type:
        fail("SEMANTIC_TYPE_MISMATCH", f"{path}:{value.get('semantic_type')}!={expected_type}")
    _validate_origin(value, allowed_origins, path)
    generic = _generic_inner(expected_type)
    if generic:
        kind, inner = generic
        if kind == "SET_OF":
            members = value.get("members")
            if not isinstance(members, list) or not members:
                fail("INVALID_SET_CARDINALITY", path)
            for index, member in enumerate(members):
                validate_value(member, inner, allowed_origins, catalog, f"{path}/members/{index}")
        else:
            _validate_reference(value, expected_type, catalog, path)
            if value["resolver_contract"].get("output_type") != f"SET_OF<{inner}>":
                fail("RESOLVER_TYPE_MISMATCH", path)
        return
    if expected_type in PRIMITIVES:
        pytype = PRIMITIVES[expected_type]
        raw = value.get("value")
        if expected_type in {"INTEGER", "DECIMAL"} and isinstance(raw, bool):
            fail("PRIMITIVE_TYPE_MISMATCH", path)
        if not isinstance(raw, pytype):
            fail("PRIMITIVE_TYPE_MISMATCH", path)
        return
    if expected_type not in catalog["types"]:
        fail("UNKNOWN_SEMANTIC_TYPE", expected_type)
    _validate_reference(value, expected_type, catalog, path)


def _validate_reference(value: dict[str, Any], expected_type: str, catalog: dict[str, Any], path: str) -> None:
    if not REFERENCE_FIELDS <= set(value):
        fail("INCOMPLETE_SYMBOLIC_REFERENCE", path)
    if value.get("inference") is not False:
        fail("INFERRED_SYMBOLIC_REFERENCE", path)
    if not isinstance(value["namespace"], str) or not SYMBOL.fullmatch(value["namespace"]):
        fail("INVALID_NAMESPACE", path)
    if not isinstance(value["identifier"], str) or not SYMBOL.fullmatch(value["identifier"]):
        fail("PREDICATE_OR_LABEL_IDENTIFIER", path)
    source = value["authoritative_source"]
    if not isinstance(source, dict) or not {"source_type", "source_id", "version"} <= set(source):
        fail("MISSING_AUTHORITATIVE_SOURCE", path)
    if source["source_type"] not in ORIGINS - {"RUNTIME_OBSERVED", "EVIDENCE_OBJECT", "SYNTHETIC_MODEL_FIXTURE"}:
        fail("INVALID_AUTHORITATIVE_SOURCE", path)
    resolver = value["resolver_contract"]
    if not isinstance(resolver, dict) or not {"resolver_id", "version", "input_types", "output_type", "deterministic"} <= set(resolver):
        fail("MISSING_RESOLVER", path)
    generic = _generic_inner(expected_type)
    resolver_output_type = f"SET_OF<{generic[1]}>" if generic and generic[0] in {"CANONICAL_SET_REF", "RUNTIME_SET_REF"} else expected_type
    if resolver["output_type"] != resolver_output_type or resolver["deterministic"] is not True:
        fail("RESOLVER_TYPE_MISMATCH", path)
    if expected_type in {"STATE_ID", "CANONICAL_ENUM_VALUE", "CANONICAL_OUTCOME"}:
        allowed = source.get("allowed_identifiers")
        if not isinstance(allowed, list) or value["identifier"] not in allowed:
            fail("NONCANONICAL_ENUM_OR_STATE", path)


def scalar_value(semantic_type: str, identifier: str, origin_type: str, origin_id: str, *, allowed: list[str] | None = None) -> dict[str, Any]:
    if semantic_type in PRIMITIVES:
        defaults: dict[str, Any] = {"BOOLEAN": True, "INTEGER": 1, "DECIMAL": 1, "TIMESTAMP": "2026-07-15T00:00:00+07:00", "DURATION": 1}
        return {
            "semantic_type": semantic_type, "value": defaults[semantic_type],
            "origin": {"origin_type": origin_type, "origin_id": origin_id},
            "provenance": {"source_fingerprint": "A" * 64, "inference": False},
        }
    return {
        "namespace": "YSIM.MODEL", "identifier": identifier, "semantic_type": semantic_type,
        "authoritative_source": {
            "source_type": "CANONICAL_REGISTRY", "source_id": "V23-SEMANTIC-TYPE-CATALOG",
            "version": "1.0.0", **({"allowed_identifiers": allowed or [identifier]} if semantic_type in {"STATE_ID", "CANONICAL_ENUM_VALUE", "CANONICAL_OUTCOME"} else {}),
        },
        "resolver_contract": {"resolver_id": f"RESOLVE.{semantic_type}", "version": "1.0.0", "input_types": [], "output_type": semantic_type, "deterministic": True},
        "lifecycle": {"status": "ACTIVE", "version": "1.0.0"},
        "origin": {"origin_type": origin_type, "origin_id": origin_id},
        "provenance": {"source_fingerprint": "A" * 64, "inference": False},
        "inference": False,
    }


def typed_value(semantic_type: str, origin_type: str, origin_id: str, *, identifier: str = "VALUE.1") -> dict[str, Any]:
    generic = _generic_inner(semantic_type)
    if generic:
        kind, inner = generic
        if kind == "SET_OF":
            member = scalar_value(inner, "MEMBER.1", origin_type, origin_id + ".MEMBER")
            return {
                "semantic_type": semantic_type, "members": [member],
                "origin": {"origin_type": origin_type, "origin_id": origin_id},
                "provenance": {"source_fingerprint": "A" * 64, "inference": False},
            }
        value = scalar_value(semantic_type, identifier, origin_type, origin_id)
        value["resolver_contract"]["output_type"] = f"SET_OF<{inner}>"
        return value
    return scalar_value(semantic_type, identifier, origin_type, origin_id)


def validate_fixture(fixture: dict[str, Any], schema: dict[str, Any], catalog: dict[str, Any]) -> None:
    if fixture.get("operator_id") != schema["operator_id"]:
        fail("OPERATOR_SCHEMA_MISMATCH", fixture.get("operator_id", "MISSING"))
    definitions = {item["name"]: item for item in schema["bindings"]}
    if set(fixture.get("bindings", {})) != set(definitions):
        fail("BINDING_SET_MISMATCH", schema["operator_id"])
    for name, definition in definitions.items():
        validate_value(fixture["bindings"][name], definition["semantic_type"], definition["allowed_origins"], catalog, f"bindings/{name}")
    comparison = fixture.get("comparison", {})
    expected_type = schema["comparison_contract"]["semantic_type"]
    validate_value(comparison.get("expected"), expected_type, schema["origin_constraints"]["expected_allowed"], catalog, "comparison/expected")
    validate_value(comparison.get("observed"), expected_type, schema["origin_constraints"]["observed_allowed"], catalog, "comparison/observed")
    if comparison["expected"]["origin"]["origin_id"] == comparison["observed"]["origin"]["origin_id"]:
        fail("NON_INDEPENDENT_ORIGIN", schema["operator_id"])
    expected_resolver = comparison["expected"].get("resolver_contract", {}).get("resolver_id")
    observed_resolver = comparison["observed"].get("resolver_contract", {}).get("resolver_id")
    if expected_resolver is not None and expected_resolver == observed_resolver:
        fail("NON_INDEPENDENT_RESOLVER", schema["operator_id"])
    evidence = fixture.get("evidence_object")
    validate_value(evidence, "EVIDENCE_OBJECT_REF", ["EVIDENCE_OBJECT", "SYNTHETIC_MODEL_FIXTURE"], catalog, "evidence_object")
    if not schema.get("evaluator_consumes_all_bindings"):
        fail("EVALUATOR_BINDING_CONSUMPTION_NOT_REQUIRED", schema["operator_id"])


def semantic_equal(left: dict[str, Any], right: dict[str, Any]) -> bool:
    if left.get("semantic_type") != right.get("semantic_type"):
        return False
    generic = _generic_inner(left["semantic_type"])
    if generic and generic[0] == "SET_OF":
        return {item["identifier"] for item in left["members"]} == {item["identifier"] for item in right["members"]}
    if left["semantic_type"] in PRIMITIVES:
        return left["value"] == right["value"]
    return left["namespace"] == right["namespace"] and left["identifier"] == right["identifier"]


def evaluate_fixture(fixture: dict[str, Any], schema: dict[str, Any], catalog: dict[str, Any]) -> bool:
    validate_fixture(fixture, schema, catalog)
    return semantic_equal(fixture["comparison"]["expected"], fixture["comparison"]["observed"])
