from __future__ import annotations

import dataclasses
from collections.abc import Mapping
from typing import Any, cast

import pytest

from ysf.configuration_access_control.controls import (
    AccessDecision,
    AccessGrant,
    AccessRequest,
    AuthenticationPolicy,
    AuthenticationRule,
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
    tenant_id: str | None = "TENANT:PILOT",
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
        tenant_id=None if scope == "GLOBAL" else tenant_id,
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
        "tenant_id": None,
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
    assert "TENANT:PILOT|CONFIG:ORG:1|" in dict(resolved.source_records)["FEATURE"]
    assert resolved.tenant_id == "TENANT:PILOT"
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
    bad_parent = record("CONFIG:P", "DEPARTMENT")
    bad_child = record("CONFIG:C", "ORGANIZATION", parent="CONFIG:P")
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


def test_tenant_binding_is_immutable_and_part_of_resolution_evidence() -> None:
    selected = schema()
    parent = record("CONFIG:GLOBAL", "GLOBAL", selected_schema=selected)
    child = record(
        "CONFIG:ORG",
        "ORGANIZATION",
        parent="CONFIG:GLOBAL",
        tenant_id="TENANT:PILOT",
        selected_schema=selected,
    )
    resolved = resolve_effective_configuration((parent, child), selected, at="2026-06-01T00:00:00Z")
    assert resolved.tenant_id == "TENANT:PILOT"
    assert all("TENANT:" in source for _, source in resolved.source_records)
    changed_tenant = dataclasses.replace(child, tenant_id="TENANT:OTHER")
    assert changed_tenant.record_digest == child.record_digest
    failure_code(
        lambda: resolve_effective_configuration(
            (parent, changed_tenant), selected, at="2026-06-01T00:00:00Z"
        ),
        "FAIL_CONFIG_INTEGRITY",
    )


def test_direct_and_multilevel_cross_tenant_inheritance_fail_closed() -> None:
    selected = schema()
    tenant_a = record(
        "CONFIG:TENANT-A", "ORGANIZATION", tenant_id="TENANT:ALPHA", selected_schema=selected
    )
    tenant_b = record(
        "CONFIG:TENANT-B",
        "DEPARTMENT",
        parent="CONFIG:TENANT-A",
        tenant_id="TENANT:BRAVO",
        selected_schema=selected,
    )
    failure_code(
        lambda: resolve_effective_configuration(
            (tenant_a, tenant_b), selected, at="2026-06-01T00:00:00Z"
        ),
        "FAIL_CONFIG_TENANT",
    )
    middle = record(
        "CONFIG:MIDDLE",
        "DEPARTMENT",
        parent="CONFIG:TENANT-A",
        tenant_id="TENANT:ALPHA",
        selected_schema=selected,
    )
    leaf = record(
        "CONFIG:LEAF",
        "STOREFRONT",
        parent="CONFIG:MIDDLE",
        tenant_id="TENANT:BRAVO",
        selected_schema=selected,
    )
    failure_code(
        lambda: resolve_effective_configuration(
            (tenant_a, middle, leaf), selected, at="2026-06-01T00:00:00Z"
        ),
        "FAIL_CONFIG_TENANT",
    )


def test_tenant_neutral_global_and_same_tenant_chain_pass() -> None:
    selected = schema()
    global_parent = record("CONFIG:GLOBAL", "GLOBAL", selected_schema=selected)
    organization = record(
        "CONFIG:ORG",
        "ORGANIZATION",
        parent="CONFIG:GLOBAL",
        tenant_id="TENANT:PILOT",
        selected_schema=selected,
    )
    department = record(
        "CONFIG:DEPT",
        "DEPARTMENT",
        parent="CONFIG:ORG",
        tenant_id="TENANT:PILOT",
        selected_schema=selected,
    )
    result = resolve_effective_configuration(
        (global_parent, organization, department), selected, at="2026-06-01T00:00:00Z"
    )
    assert result.tenant_id == "TENANT:PILOT"


def test_missing_malformed_and_ambiguous_tenant_fail_closed() -> None:
    selected = schema()
    for tenant in (None, "OTHER", "TENANT:x"):
        failure_code(
            lambda tenant=tenant: build_configuration_record(
                identity="CONFIG:ORG",
                version=1,
                schema=selected,
                scope="ORGANIZATION",
                tenant_id=tenant,
                owner="Platform Operations",
                effective_from="2026-01-01T00:00:00Z",
                effective_until="2027-01-01T00:00:00Z",
                values={"FEATURE": False, "REGION": "PILOT"},
                audit_metadata={"CHANGE_ID": "SYN-CHANGE-001"},
            ),
            "FAIL_CONFIG_TENANT",
        )
    failure_code(
        lambda: build_configuration_record(
            identity="CONFIG:GLOBAL",
            version=1,
            schema=selected,
            scope="GLOBAL",
            tenant_id="TENANT:PILOT",
            owner="Platform Operations",
            effective_from="2026-01-01T00:00:00Z",
            effective_until="2027-01-01T00:00:00Z",
            values={"FEATURE": False, "REGION": "PILOT"},
            audit_metadata={"CHANGE_ID": "SYN-CHANGE-001"},
        ),
        "FAIL_CONFIG_TENANT",
    )


def policy() -> AuthenticationPolicy:
    return AuthenticationPolicy.create(
        {
            "ACTOR:OPERATOR": {
                "role": "ROLE:OPERATOR",
                "method": "SYNTHETIC_PASSWORD",
                "assurance_requirement": "SYNTHETIC_ASSURANCE_LEVEL_2",
                "session_rule": "SYNTHETIC_SINGLE_OPERATION",
                "failure_behavior": "DENY_BEFORE_PROVIDER_OR_DELIVERY",
            },
            "ACTOR:SERVICE": {
                "role": "ROLE:SERVICE",
                "method": "SERVICE_ASSERTION",
                "assurance_requirement": "SYNTHETIC_ASSURANCE_LEVEL_1",
                "session_rule": "SOURCE_ONLY_NO_SESSION",
                "failure_behavior": "DENY_BEFORE_PROVIDER_OR_DELIVERY",
            },
        }
    )


def request() -> AccessRequest:
    return AccessRequest(
        subject="SUBJECT:SYNTHETIC-001",
        actor_class="ACTOR:OPERATOR",
        role="ROLE:OPERATOR",
        action="CONFIG:READ",
        resource="CONFIG:PILOT",
        data_scope="ORG:SYNTHETIC",
        correlation_id="SYN-CORRELATION-001",
    )


def valid_authentication():
    return authenticate(
        policy(),
        actor_class="ACTOR:OPERATOR",
        role="ROLE:OPERATOR",
        method="SYNTHETIC_PASSWORD",
        synthetic_proof="SYNTHETIC_VERIFIED",
        assurance_result="SYNTHETIC_ASSURANCE_LEVEL_2",
        session_rule_result="SYNTHETIC_SINGLE_OPERATION",
    )


@pytest.mark.parametrize(
    "case",
    (
        "non_string_rule_value",
        "empty_policy",
        "invalid_rule_value",
        "unknown_actor",
        "wrong_policy_digest",
        "wrong_policy_type",
        "wrong_request_type",
        "wrong_grant_type",
        "wrong_authentication_type",
    ),
)
def test_defensive_authentication_and_authorization_branches_fail_closed(case: str) -> None:
    valid_rule: dict[str, Any] = {
        "role": "ROLE:OPERATOR",
        "method": "SYNTHETIC_PASSWORD",
        "assurance_requirement": "SYNTHETIC_ASSURANCE_LEVEL_2",
        "session_rule": "SYNTHETIC_SINGLE_OPERATION",
        "failure_behavior": "DENY_BEFORE_PROVIDER_OR_DELIVERY",
    }
    invalid_rule = AuthenticationRule(
        actor_class="ACTOR:OPERATOR",
        role="ROLE:OPERATOR",
        method="UNLISTED",
        assurance_requirement="SYNTHETIC_ASSURANCE_LEVEL_2",
        session_rule="SYNTHETIC_SINGLE_OPERATION",
        failure_behavior="DENY_BEFORE_PROVIDER_OR_DELIVERY",
    )
    calls = {
        "non_string_rule_value": (
            lambda: AuthenticationPolicy.create(
                {"ACTOR:OPERATOR": {**valid_rule, "role": cast(Any, 7)}}
            ),
            "FAIL_AUTH_POLICY",
        ),
        "empty_policy": (
            lambda: AuthenticationPolicy((), "0" * 64).rule_for("ACTOR:OPERATOR"),
            "FAIL_AUTH_POLICY",
        ),
        "invalid_rule_value": (
            lambda: AuthenticationPolicy((invalid_rule,), "0" * 64).rule_for("ACTOR:OPERATOR"),
            "FAIL_AUTH_POLICY",
        ),
        "unknown_actor": (
            lambda: policy().rule_for("ACTOR:UNKNOWN"),
            "FAIL_AUTH_POLICY",
        ),
        "wrong_policy_digest": (
            lambda: dataclasses.replace(policy(), policy_digest="0" * 64).rule_for(
                "ACTOR:OPERATOR"
            ),
            "FAIL_AUTH_POLICY",
        ),
        "wrong_policy_type": (
            lambda: authenticate(
                cast(Any, object()),
                actor_class="ACTOR:OPERATOR",
                role="ROLE:OPERATOR",
                method="SYNTHETIC_PASSWORD",
                synthetic_proof="SYNTHETIC_VERIFIED",
                assurance_result="SYNTHETIC_ASSURANCE_LEVEL_2",
                session_rule_result="SYNTHETIC_SINGLE_OPERATION",
            ),
            "FAIL_AUTH_POLICY",
        ),
        "wrong_request_type": (
            lambda: authorize(policy(), valid_authentication(), cast(Any, object()), ()),
            "FAIL_AUTHORIZATION_INPUT",
        ),
        "wrong_grant_type": (
            lambda: authorize(policy(), valid_authentication(), request(), (cast(Any, object()),)),
            "FAIL_AUTHORIZATION_INPUT",
        ),
        "wrong_authentication_type": (
            lambda: authorize(policy(), cast(Any, object()), request(), ()),
            "FAIL_AUTHENTICATION_EVIDENCE",
        ),
    }
    call, expected_code = calls[case]
    failure_code(call, expected_code)


def test_malformed_utc_timestamp_reaches_interval_boundary() -> None:
    failure_code(
        lambda: record(
            "CONFIG:GLOBAL",
            "GLOBAL",
            effective_from="not-a-timestampZ",
        ),
        "FAIL_CONFIG_INTERVAL",
    )


def test_allowlisted_authentication_and_access_allow_path() -> None:
    authentication = authenticate(
        policy(),
        actor_class="ACTOR:OPERATOR",
        role="ROLE:OPERATOR",
        method="SYNTHETIC_PASSWORD",
        synthetic_proof="SYNTHETIC_VERIFIED",
        assurance_result="SYNTHETIC_ASSURANCE_LEVEL_2",
        session_rule_result="SYNTHETIC_SINGLE_OPERATION",
    )
    grant = AccessGrant(
        "ACTOR:OPERATOR", "ROLE:OPERATOR", "CONFIG:READ", "CONFIG:PILOT", "ORG:SYNTHETIC"
    )
    decision = authorize(policy(), authentication, request(), (grant,))
    assert authentication.result == "PASS"
    assert decision.result == "ALLOW"
    assert request().subject not in json_values(decision.audit_record)
    gate = assert_pre_execution_access(
        policy(),
        request(),
        (grant,),
        method="SYNTHETIC_PASSWORD",
        synthetic_proof="SYNTHETIC_VERIFIED",
        assurance_result="SYNTHETIC_ASSURANCE_LEVEL_2",
        session_rule_result="SYNTHETIC_SINGLE_OPERATION",
    )
    assert gate.result == "PASS"
    assert gate.provider_invoked is False
    assert gate.delivery_performed is False


def json_values(items: tuple[tuple[str, str], ...]) -> str:
    return "|".join(value for _, value in items)


@pytest.mark.parametrize(
    ("actor", "role", "method", "proof", "code"),
    [
        (
            "ACTOR:OPERATOR",
            "ROLE:OPERATOR",
            "UNLISTED",
            "SYNTHETIC_VERIFIED",
            "FAIL_AUTHENTICATION_METHOD",
        ),
        (
            "ACTOR:SERVICE",
            "ROLE:SERVICE",
            "SYNTHETIC_PASSWORD",
            "SYNTHETIC_VERIFIED",
            "FAIL_AUTHENTICATION_METHOD",
        ),
        (
            "bad actor",
            "ROLE:OPERATOR",
            "SYNTHETIC_PASSWORD",
            "SYNTHETIC_VERIFIED",
            "FAIL_AUTHENTICATION_METHOD",
        ),
        (
            "ACTOR:OPERATOR",
            "ROLE:OTHER",
            "SYNTHETIC_PASSWORD",
            "SYNTHETIC_VERIFIED",
            "FAIL_AUTHENTICATION_METHOD",
        ),
        (
            "ACTOR:OPERATOR",
            "ROLE:OPERATOR",
            "SYNTHETIC_PASSWORD",
            "RAW_PROOF",
            "FAIL_AUTHENTICATION_PROOF",
        ),
    ],
)
def test_authentication_negative_matrix(
    actor: str, role: str, method: str, proof: str, code: str
) -> None:
    failure_code(
        lambda: authenticate(
            policy(),
            actor_class=actor,
            role=role,
            method=method,
            synthetic_proof=proof,
            assurance_result="SYNTHETIC_ASSURANCE_LEVEL_2",
            session_rule_result="SYNTHETIC_SINGLE_OPERATION",
        ),
        code,
    )


def test_authentication_policy_and_failed_proof_fail_closed() -> None:
    failure_code(lambda: AuthenticationPolicy.create({}), "FAIL_AUTH_POLICY")
    failure_code(
        lambda: AuthenticationPolicy.create(
            {
                "bad actor": {
                    "role": "ROLE:OPERATOR",
                    "method": "SYNTHETIC_PASSWORD",
                    "assurance_requirement": "SYNTHETIC_ASSURANCE_LEVEL_2",
                    "session_rule": "SYNTHETIC_SINGLE_OPERATION",
                    "failure_behavior": "DENY_BEFORE_PROVIDER_OR_DELIVERY",
                }
            }
        ),
        "FAIL_AUTH_POLICY",
    )
    failed = authenticate(
        policy(),
        actor_class="ACTOR:OPERATOR",
        role="ROLE:OPERATOR",
        method="SYNTHETIC_PASSWORD",
        synthetic_proof="SYNTHETIC_REJECTED",
        assurance_result="SYNTHETIC_ASSURANCE_LEVEL_2",
        session_rule_result="SYNTHETIC_SINGLE_OPERATION",
    )
    decision = authorize(policy(), failed, request(), ())
    assert decision.result == "DENY"
    failure_code(
        lambda: assert_pre_execution_access(
            policy(),
            request(),
            (),
            method="SYNTHETIC_PASSWORD",
            synthetic_proof="SYNTHETIC_REJECTED",
            assurance_result="SYNTHETIC_ASSURANCE_LEVEL_2",
            session_rule_result="SYNTHETIC_SINGLE_OPERATION",
        ),
        "FAIL_PRE_EXECUTION_AUTHENTICATION",
    )


def test_authorization_denies_wrong_action_scope_and_missing_grant() -> None:
    authentication = authenticate(
        policy(),
        actor_class="ACTOR:OPERATOR",
        role="ROLE:OPERATOR",
        method="SYNTHETIC_PASSWORD",
        synthetic_proof="SYNTHETIC_VERIFIED",
        assurance_result="SYNTHETIC_ASSURANCE_LEVEL_2",
        session_rule_result="SYNTHETIC_SINGLE_OPERATION",
    )
    decision = authorize(policy(), authentication, request(), ())
    assert decision.result == "DENY"
    failure_code(
        lambda: assert_pre_execution_access(
            policy(),
            request(),
            (),
            method="SYNTHETIC_PASSWORD",
            synthetic_proof="SYNTHETIC_VERIFIED",
            assurance_result="SYNTHETIC_ASSURANCE_LEVEL_2",
            session_rule_result="SYNTHETIC_SINGLE_OPERATION",
        ),
        "FAIL_PRE_EXECUTION_AUTHORIZATION",
    )
    wrong = AccessGrant(
        "ACTOR:OPERATOR", "ROLE:OPERATOR", "CONFIG:WRITE", "CONFIG:PILOT", "ORG:OTHER"
    )
    assert authorize(policy(), authentication, request(), (wrong,)).result == "DENY"


def test_authorization_rejects_malformed_sensitive_and_bad_correlation() -> None:
    authentication = authenticate(
        policy(),
        actor_class="ACTOR:OPERATOR",
        role="ROLE:OPERATOR",
        method="SYNTHETIC_PASSWORD",
        synthetic_proof="SYNTHETIC_VERIFIED",
        assurance_result="SYNTHETIC_ASSURANCE_LEVEL_2",
        session_rule_result="SYNTHETIC_SINGLE_OPERATION",
    )
    malformed = dataclasses.replace(request(), action="bad action")
    failure_code(
        lambda: authorize(policy(), authentication, malformed, ()),
        "FAIL_AUTHORIZATION_INPUT",
    )
    sensitive = dataclasses.replace(request(), subject="user" + "@" + "outside.invalid")
    failure_code(
        lambda: authorize(policy(), authentication, sensitive, ()),
        "FAIL_AUTHORIZATION_INPUT",
    )
    correlation = dataclasses.replace(request(), correlation_id="raw")
    failure_code(
        lambda: authorize(policy(), authentication, correlation, ()),
        "FAIL_AUTHORIZATION_INPUT",
    )


def test_assurance_session_and_policy_schema_fail_closed() -> None:
    common = {
        "policy": policy(),
        "actor_class": "ACTOR:OPERATOR",
        "role": "ROLE:OPERATOR",
        "method": "SYNTHETIC_PASSWORD",
        "synthetic_proof": "SYNTHETIC_VERIFIED",
        "assurance_result": "SYNTHETIC_ASSURANCE_LEVEL_2",
        "session_rule_result": "SYNTHETIC_SINGLE_OPERATION",
    }
    failure_code(
        lambda: authenticate(**{**common, "assurance_result": "SYNTHETIC_ASSURANCE_LEVEL_1"}),
        "FAIL_AUTHENTICATION_ASSURANCE",
    )
    failure_code(
        lambda: authenticate(**{**common, "session_rule_result": "SOURCE_ONLY_NO_SESSION"}),
        "FAIL_AUTHENTICATION_SESSION",
    )
    base_rule = {
        "role": "ROLE:OPERATOR",
        "method": "SYNTHETIC_PASSWORD",
        "assurance_requirement": "SYNTHETIC_ASSURANCE_LEVEL_2",
        "session_rule": "SYNTHETIC_SINGLE_OPERATION",
        "failure_behavior": "DENY_BEFORE_PROVIDER_OR_DELIVERY",
    }
    for mutation in (
        {key: value for key, value in base_rule.items() if key != "failure_behavior"},
        {**base_rule, "extra": "DENY"},
        {**base_rule, "failure_behavior": "ALLOW"},
    ):
        failure_code(
            lambda mutation=mutation: AuthenticationPolicy.create({"ACTOR:OPERATOR": mutation}),
            "FAIL_AUTH_POLICY",
        )


def test_forged_decisions_replay_and_digest_mismatch_are_rejected() -> None:
    selected_policy = policy()
    authentication = authenticate(
        selected_policy,
        actor_class="ACTOR:OPERATOR",
        role="ROLE:OPERATOR",
        method="SYNTHETIC_PASSWORD",
        synthetic_proof="SYNTHETIC_VERIFIED",
        assurance_result="SYNTHETIC_ASSURANCE_LEVEL_2",
        session_rule_result="SYNTHETIC_SINGLE_OPERATION",
    )
    forged_auth = dataclasses.replace(authentication, evidence_digest="0" * 64)
    grant = AccessGrant(
        "ACTOR:OPERATOR", "ROLE:OPERATOR", "CONFIG:READ", "CONFIG:PILOT", "ORG:SYNTHETIC"
    )
    failure_code(
        lambda: authorize(selected_policy, forged_auth, request(), (grant,)),
        "FAIL_AUTHENTICATION_EVIDENCE",
    )
    decision = authorize(selected_policy, authentication, request(), (grant,))
    forged_access = AccessDecision(
        result="ALLOW",
        policy_digest=selected_policy.policy_digest,
        authentication_evidence_digest=authentication.evidence_digest,
        request_digest="0" * 64,
        grant_digest="0" * 64,
        decision_digest="0" * 64,
        audit_record=(("authorization_result", "ALLOW"),),
    )
    assert forged_access != decision
    common = {
        "grants": (grant,),
        "method": "SYNTHETIC_PASSWORD",
        "synthetic_proof": "SYNTHETIC_VERIFIED",
        "assurance_result": "SYNTHETIC_ASSURANCE_LEVEL_2",
        "session_rule_result": "SYNTHETIC_SINGLE_OPERATION",
    }
    failure_code(
        lambda: assert_pre_execution_access(
            forged_auth,
            request(),
            **common,  # type: ignore[arg-type]
        ),
        "FAIL_PRE_EXECUTION_INPUT",
    )
    failure_code(
        lambda: assert_pre_execution_access(
            selected_policy,
            forged_access,
            **common,  # type: ignore[arg-type]
        ),
        "FAIL_PRE_EXECUTION_INPUT",
    )
    replay = dataclasses.replace(request(), resource="CONFIG:OTHER")
    replay_decision = authorize(selected_policy, authentication, replay, (grant,))
    assert replay_decision.result == "DENY"
    assert replay_decision.request_digest != decision.request_digest


def test_audit_binds_actor_role_and_redacts_subject_and_correlation() -> None:
    selected_policy = policy()
    authentication = authenticate(
        selected_policy,
        actor_class="ACTOR:OPERATOR",
        role="ROLE:OPERATOR",
        method="SYNTHETIC_PASSWORD",
        synthetic_proof="SYNTHETIC_VERIFIED",
        assurance_result="SYNTHETIC_ASSURANCE_LEVEL_2",
        session_rule_result="SYNTHETIC_SINGLE_OPERATION",
    )
    grant = AccessGrant(
        "ACTOR:OPERATOR", "ROLE:OPERATOR", "CONFIG:READ", "CONFIG:PILOT", "ORG:SYNTHETIC"
    )
    audit = dict(authorize(selected_policy, authentication, request(), (grant,)).audit_record)
    assert audit["actor_class"] == "ACTOR:OPERATOR"
    assert audit["role"] == "ROLE:OPERATOR"
    assert audit["authentication_method"] == "SYNTHETIC_PASSWORD"
    assert audit["assurance_result"] == "SYNTHETIC_ASSURANCE_LEVEL_2"
    assert audit["session_rule_result"] == "SYNTHETIC_SINGLE_OPERATION"
    assert request().subject not in json_values(tuple(audit.items()))
    assert request().correlation_id not in json_values(tuple(audit.items()))


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
