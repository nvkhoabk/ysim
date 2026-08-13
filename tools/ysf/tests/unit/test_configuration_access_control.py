from __future__ import annotations

import dataclasses
from collections.abc import Mapping

import pytest

from ysf.configuration_access_control.controls import (
    AccessGrant,
    AccessRequest,
    AuthenticationPolicy,
    ConfigurationRecord,
    ConfigurationRegistry,
    ConfigurationSchema,
    assert_pre_execution_access,
    authenticate,
    authorize,
    build_configuration_record,
    redact_for_output,
    resolve_effective_configuration,
)
from ysf.secure_factory.models import FactoryFailure


def schema(*, overridable: tuple[str, ...] = ("FEATURE",)) -> ConfigurationSchema:
    return ConfigurationSchema.create(
        version="SCHEMA:1",
        fields={"FEATURE": "boolean", "REGION": "string"},
        required_fields=("FEATURE", "REGION"),
        overridable_fields=overridable,
    )


def record(
    identity: str,
    scope: str,
    *,
    parent: str | None = None,
    version: int = 1,
    values: Mapping[str, str | int | bool | None] | None = None,
    selected_schema: ConfigurationSchema | None = None,
    effective_from: str = "2026-01-01T00:00:00Z",
    effective_until: str = "2027-01-01T00:00:00Z",
) -> ConfigurationRecord:
    return build_configuration_record(
        identity=identity,
        version=version,
        schema=selected_schema or schema(),
        scope=scope,
        owner="Platform Operations",
        effective_from=effective_from,
        effective_until=effective_until,
        parent_identity=parent,
        values=values or {"FEATURE": False, "REGION": "PILOT"},
        audit_metadata={"CHANGE_ID": "SYN-CHANGE-001", "ACTOR": "SYNTHETIC-OPS"},
    )


def failure_code(callable_: object, code: str) -> None:
    assert callable(callable_)
    with pytest.raises(FactoryFailure) as captured:
        callable_()  # type: ignore[operator]
    assert captured.value.code == code


def test_configuration_record_is_immutable_and_digest_is_canonical() -> None:
    first = record(
        "CONFIG:GLOBAL",
        "GLOBAL",
        values={"REGION": "PILOT", "FEATURE": False},
    )
    second = record(
        "CONFIG:GLOBAL",
        "GLOBAL",
        values={"FEATURE": False, "REGION": "PILOT"},
    )
    assert first == second
    assert first.value_digest == second.value_digest
    assert first.value_map == {"FEATURE": False, "REGION": "PILOT"}
    with pytest.raises(dataclasses.FrozenInstanceError):
        first.version = 2  # type: ignore[misc]


@pytest.mark.parametrize(
    ("kwargs", "code"),
    [
        ({"version": "bad version"}, "FAIL_CONFIG_SCHEMA"),
        ({"fields": {}}, "FAIL_CONFIG_SCHEMA"),
        ({"fields": {"FIELD": "float"}}, "FAIL_CONFIG_SCHEMA"),
        ({"required_fields": ("MISSING",)}, "FAIL_CONFIG_SCHEMA"),
        ({"overridable_fields": ("MISSING",)}, "FAIL_CONFIG_SCHEMA"),
    ],
)
def test_schema_fail_closed(kwargs: dict[str, object], code: str) -> None:
    values: dict[str, object] = {
        "version": "SCHEMA:1",
        "fields": {"FIELD": "string"},
        "required_fields": ("FIELD",),
        "overridable_fields": ("FIELD",),
    }
    values.update(kwargs)
    failure_code(lambda: ConfigurationSchema.create(**values), code)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("kwargs", "code"),
    [
        ({"identity": "x"}, "FAIL_CONFIG_IDENTITY"),
        ({"version": 0}, "FAIL_CONFIG_IDENTITY"),
        ({"scope": "TENANT"}, "FAIL_CONFIG_SCOPE_OWNER"),
        ({"owner": "x"}, "FAIL_CONFIG_SCOPE_OWNER"),
        ({"effective_from": "2026-01-01"}, "FAIL_CONFIG_INTERVAL"),
        ({"effective_until": "2025-01-01T00:00:00Z"}, "FAIL_CONFIG_INTERVAL"),
        ({"parent_identity": "x"}, "FAIL_CONFIG_PARENT"),
        ({"values": {"FEATURE": False}}, "FAIL_CONFIG_SCHEMA"),
        ({"values": {"FEATURE": 1, "REGION": "PILOT"}}, "FAIL_CONFIG_SCHEMA"),
        ({"audit_metadata": {}}, "FAIL_CONFIG_AUDIT"),
    ],
)
def test_record_validation_fail_closed(kwargs: dict[str, object], code: str) -> None:
    values: dict[str, object] = {
        "identity": "CONFIG:GLOBAL",
        "version": 1,
        "schema": schema(),
        "scope": "GLOBAL",
        "owner": "Platform Operations",
        "effective_from": "2026-01-01T00:00:00Z",
        "effective_until": "2027-01-01T00:00:00Z",
        "values": {"FEATURE": False, "REGION": "PILOT"},
        "audit_metadata": {"CHANGE_ID": "SYN-CHANGE-001"},
        "parent_identity": None,
    }
    values.update(kwargs)
    failure_code(lambda: build_configuration_record(**values), code)  # type: ignore[arg-type]


def test_sensitive_configuration_is_rejected_before_registry_mutation() -> None:
    registry = ConfigurationRegistry()
    prohibited = "api_" + "key=" + "abcdefghijklmnop"
    failure_code(
        lambda: record(
            "CONFIG:GLOBAL",
            "GLOBAL",
            values={"FEATURE": False, "REGION": prohibited},
        ),
        "FAIL_CONFIG_SENSITIVE",
    )
    assert registry.records == ()


def test_registry_rejects_same_identity_version_with_different_values() -> None:
    registry = ConfigurationRegistry()
    registry.add(record("CONFIG:GLOBAL", "GLOBAL"))
    registry.add(record("CONFIG:GLOBAL", "GLOBAL"))
    failure_code(
        lambda: registry.add(
            record(
                "CONFIG:GLOBAL",
                "GLOBAL",
                values={"FEATURE": True, "REGION": "PILOT"},
            )
        ),
        "FAIL_CONFIG_AMBIGUITY",
    )
    assert len(registry.records) == 1
    assert registry.remove("CONFIG:GLOBAL", 1).identity == "CONFIG:GLOBAL"
    failure_code(lambda: registry.remove("CONFIG:GLOBAL", 1), "FAIL_CONFIG_MISSING")


def test_deterministic_inheritance_override_and_removal() -> None:
    selected = schema()
    parent = record("CONFIG:GLOBAL", "GLOBAL", selected_schema=selected)
    child = record(
        "CONFIG:ORG",
        "ORGANIZATION",
        parent="CONFIG:GLOBAL",
        values={"FEATURE": True, "REGION": "PILOT"},
        selected_schema=selected,
    )
    resolved = resolve_effective_configuration((child, parent), selected, at="2026-06-01T00:00:00Z")
    assert resolved.values == (("FEATURE", True), ("REGION", "PILOT"))
    assert dict(resolved.source_records)["FEATURE"] == "CONFIG:ORG:1"
    inherited = resolve_effective_configuration((parent,), selected, at="2026-06-01T00:00:00Z")
    assert inherited.values == (("FEATURE", False), ("REGION", "PILOT"))
    assert parent.value_map["FEATURE"] is False


def test_unauthorized_override_fails_closed() -> None:
    selected = schema(overridable=())
    parent = record("CONFIG:GLOBAL", "GLOBAL", selected_schema=selected)
    child = record(
        "CONFIG:ORG",
        "ORGANIZATION",
        parent="CONFIG:GLOBAL",
        values={"FEATURE": True, "REGION": "PILOT"},
        selected_schema=selected,
    )
    failure_code(
        lambda: resolve_effective_configuration(
            (parent, child), selected, at="2026-06-01T00:00:00Z"
        ),
        "FAIL_CONFIG_OVERRIDE",
    )


def test_missing_parent_cycle_scope_and_ambiguity_fail_closed() -> None:
    selected = schema()
    missing = record("CONFIG:ORG", "ORGANIZATION", parent="CONFIG:MISSING")
    failure_code(
        lambda: resolve_effective_configuration((missing,), selected, at="2026-06-01T00:00:00Z"),
        "FAIL_CONFIG_PARENT",
    )
    first = record("CONFIG:A", "GLOBAL", parent="CONFIG:B")
    second = record("CONFIG:B", "ORGANIZATION", parent="CONFIG:A")
    failure_code(
        lambda: resolve_effective_configuration(
            (first, second), selected, at="2026-06-01T00:00:00Z"
        ),
        "FAIL_CONFIG_CYCLE",
    )
    bad_parent = record("CONFIG:P", "ORGANIZATION")
    bad_child = record("CONFIG:C", "GLOBAL", parent="CONFIG:P")
    failure_code(
        lambda: resolve_effective_configuration(
            (bad_parent, bad_child), selected, at="2026-06-01T00:00:00Z"
        ),
        "FAIL_CONFIG_SCOPE",
    )
    one = record("CONFIG:ONE", "ORGANIZATION")
    two = record("CONFIG:TWO", "ORGANIZATION")
    failure_code(
        lambda: resolve_effective_configuration((one, two), selected, at="2026-06-01T00:00:00Z"),
        "FAIL_CONFIG_AMBIGUITY",
    )


def test_active_version_schema_and_empty_resolution_fail_closed() -> None:
    selected = schema()
    one = record("CONFIG:GLOBAL", "GLOBAL", version=1)
    two = record("CONFIG:GLOBAL", "GLOBAL", version=2)
    failure_code(
        lambda: resolve_effective_configuration((one, two), selected, at="2026-06-01T00:00:00Z"),
        "FAIL_CONFIG_AMBIGUITY",
    )
    other_schema = ConfigurationSchema.create(
        version="SCHEMA:2",
        fields={"FEATURE": "boolean", "REGION": "string"},
        required_fields=("FEATURE", "REGION"),
        overridable_fields=("FEATURE",),
    )
    other = record("CONFIG:GLOBAL", "GLOBAL", selected_schema=other_schema)
    failure_code(
        lambda: resolve_effective_configuration((other,), selected, at="2026-06-01T00:00:00Z"),
        "FAIL_CONFIG_SCHEMA",
    )
    expired = record(
        "CONFIG:GLOBAL",
        "GLOBAL",
        effective_until="2026-02-01T00:00:00Z",
    )
    failure_code(
        lambda: resolve_effective_configuration((expired,), selected, at="2026-06-01T00:00:00Z"),
        "FAIL_CONFIG_MISSING",
    )


def policy() -> AuthenticationPolicy:
    return AuthenticationPolicy.create(
        {
            "ACTOR:OPERATOR": ("SYNTHETIC_PASSWORD",),
            "ACTOR:SERVICE": ("SERVICE_ASSERTION",),
        }
    )


def request() -> AccessRequest:
    return AccessRequest(
        subject="SUBJECT:SYNTHETIC-001",
        actor_class="ACTOR:OPERATOR",
        action="CONFIG:READ",
        resource="CONFIG:PILOT",
        data_scope="ORG:SYNTHETIC",
        correlation_id="SYN-CORRELATION-001",
    )


def test_allowlisted_authentication_and_access_allow_path() -> None:
    authentication = authenticate(
        policy(),
        actor_class="ACTOR:OPERATOR",
        method="SYNTHETIC_PASSWORD",
        synthetic_proof="SYNTHETIC_VERIFIED",
    )
    grant = AccessGrant("ACTOR:OPERATOR", "CONFIG:READ", "CONFIG:PILOT", "ORG:SYNTHETIC")
    decision = authorize(authentication, request(), (grant,))
    assert authentication.result == "PASS"
    assert decision.result == "ALLOW"
    assert request().subject not in json_values(decision.audit_record)
    gate = assert_pre_execution_access(authentication, decision)
    assert gate.result == "PASS"
    assert gate.provider_invoked is False
    assert gate.delivery_performed is False


def json_values(items: tuple[tuple[str, str], ...]) -> str:
    return "|".join(value for _, value in items)


@pytest.mark.parametrize(
    ("actor", "method", "proof", "code"),
    [
        ("ACTOR:OPERATOR", "UNLISTED", "SYNTHETIC_VERIFIED", "FAIL_AUTHENTICATION_METHOD"),
        ("ACTOR:SERVICE", "SYNTHETIC_PASSWORD", "SYNTHETIC_VERIFIED", "FAIL_AUTHENTICATION_METHOD"),
        ("bad actor", "SYNTHETIC_PASSWORD", "SYNTHETIC_VERIFIED", "FAIL_AUTHENTICATION_METHOD"),
        ("ACTOR:OPERATOR", "SYNTHETIC_PASSWORD", "RAW_PROOF", "FAIL_AUTHENTICATION_PROOF"),
    ],
)
def test_authentication_negative_matrix(actor: str, method: str, proof: str, code: str) -> None:
    failure_code(
        lambda: authenticate(policy(), actor_class=actor, method=method, synthetic_proof=proof),
        code,
    )


def test_authentication_policy_and_failed_proof_fail_closed() -> None:
    failure_code(lambda: AuthenticationPolicy.create({}), "FAIL_AUTH_POLICY")
    failure_code(
        lambda: AuthenticationPolicy.create({"bad actor": ("SYNTHETIC_PASSWORD",)}),
        "FAIL_AUTH_POLICY",
    )
    failed = authenticate(
        policy(),
        actor_class="ACTOR:OPERATOR",
        method="SYNTHETIC_PASSWORD",
        synthetic_proof="SYNTHETIC_REJECTED",
    )
    decision = authorize(failed, request(), ())
    assert decision.result == "DENY"
    failure_code(
        lambda: assert_pre_execution_access(failed, decision),
        "FAIL_PRE_EXECUTION_AUTHENTICATION",
    )


def test_authorization_denies_wrong_action_scope_and_missing_grant() -> None:
    authentication = authenticate(
        policy(),
        actor_class="ACTOR:OPERATOR",
        method="SYNTHETIC_PASSWORD",
        synthetic_proof="SYNTHETIC_VERIFIED",
    )
    decision = authorize(authentication, request(), ())
    assert decision.result == "DENY"
    failure_code(
        lambda: assert_pre_execution_access(authentication, decision),
        "FAIL_PRE_EXECUTION_AUTHORIZATION",
    )
    wrong = AccessGrant("ACTOR:OPERATOR", "CONFIG:WRITE", "CONFIG:PILOT", "ORG:OTHER")
    assert authorize(authentication, request(), (wrong,)).result == "DENY"


def test_authorization_rejects_malformed_sensitive_and_bad_correlation() -> None:
    authentication = authenticate(
        policy(),
        actor_class="ACTOR:OPERATOR",
        method="SYNTHETIC_PASSWORD",
        synthetic_proof="SYNTHETIC_VERIFIED",
    )
    malformed = dataclasses.replace(request(), action="bad action")
    failure_code(lambda: authorize(authentication, malformed, ()), "FAIL_AUTHORIZATION_INPUT")
    sensitive = dataclasses.replace(request(), subject="user" + "@" + "outside.invalid")
    failure_code(
        lambda: authorize(authentication, sensitive, ()),
        "FAIL_AUTHORIZATION_INPUT",
    )
    correlation = dataclasses.replace(request(), correlation_id="raw")
    failure_code(lambda: authorize(authentication, correlation, ()), "FAIL_AUTHORIZATION_INPUT")


def test_redaction_happens_before_output() -> None:
    fields = {
        "status": "PASS",
        "token": "synthetic-value",
        "contact": "user" + "@" + "outside.invalid",
    }
    redacted = dict(redact_for_output(fields))
    assert redacted == {
        "contact": "<REDACTED>",
        "status": "PASS",
        "token": "<REDACTED>",
    }
