from __future__ import annotations

from dataclasses import FrozenInstanceError, replace
from typing import Any

import pytest

from ysf.integration_boundary import (
    FAILURE_DISPOSITION,
    FAILURE_STATE,
    SUCCESS_DISPOSITION,
    SUPPORTED_INTERACTION_MODES,
    IntegrationGateway,
    assert_owned_integration_dependencies,
    build_adapter_profile,
    build_canonical_request,
    build_operator_failure_projection,
    service,
)
from ysf.secure_factory.models import FactoryFailure


def request_values(**updates: object) -> dict[str, object]:
    values: dict[str, object] = {
        "contract_version": "v1",
        "capability_id": "CAPABILITY.SYNTHETIC.ORDER",
        "scenario_id": "SCENARIO.SYNTHETIC.PILOT",
        "idempotency_key": "IDEM-SYNTHETIC-000001",
        "correlation_id": "SYN-CORRELATION-000001",
        "interaction_mode": "REST",
        "adapter_id": "ADAPTER.SYNTHETIC.DISABLED",
        "owner": "Platform Integration",
        "timeout_policy_ref": "POLICY.TIMEOUT.SYNTHETIC",
        "retry_policy_ref": "POLICY.RETRY.NONE",
        "diagnostic_context": {"ATTEMPT": 1, "CLASSIFICATION": "SYNTHETIC"},
    }
    values.update(updates)
    return values


def profile(**updates: Any) -> Any:
    values: dict[str, Any] = {
        "adapter_id": "ADAPTER.SYNTHETIC.DISABLED",
        "capability_id": "CAPABILITY.SYNTHETIC.ORDER",
        "enabled": False,
        "interaction_modes": ["REST"],
        "contract_versions": ["v1"],
        "scenario_ids": ["SCENARIO.SYNTHETIC.PILOT"],
        "owner": "Platform Integration",
        "timeout_policy_ref": "POLICY.TIMEOUT.SYNTHETIC",
        "retry_policy_ref": "POLICY.RETRY.NONE",
    }
    values.update(updates)
    return build_adapter_profile(**values)


def assert_failure(code: str, action: Any) -> None:
    with pytest.raises(FactoryFailure) as captured:
        action()
    assert captured.value.code == code


def test_supported_interaction_schema_is_exact_and_does_not_enable_modes() -> None:
    assert SUPPORTED_INTERACTION_MODES == {"REST", "WEBHOOK", "EVENT", "QUEUE", "BATCH"}
    gateway = IntegrationGateway(allowed_adapter_ids=[])
    assert gateway.profiles == ()
    assert gateway.adapter_invocation_count == 0
    assert gateway.network_call_count == 0


def test_request_is_canonical_immutable_and_digest_is_deterministic() -> None:
    first = build_canonical_request(request_values())
    second_values = request_values(
        diagnostic_context={"CLASSIFICATION": "SYNTHETIC", "ATTEMPT": 1}
    )
    second = build_canonical_request(second_values)
    assert first == second
    assert len(first.request_digest) == 64
    assert dict(first.diagnostics) == {"ATTEMPT": 1, "CLASSIFICATION": "SYNTHETIC"}
    with pytest.raises(FrozenInstanceError):
        first.adapter_id = "ADAPTER.OTHER"  # type: ignore[misc]
    with pytest.raises(TypeError):
        first.diagnostics["ATTEMPT"] = 2  # type: ignore[index]


@pytest.mark.parametrize(
    ("updates", "code"),
    [
        ({"contract_version": "1"}, "FAIL_INTEGRATION_VERSION"),
        ({"capability_id": "bad"}, "FAIL_INTEGRATION_CAPABILITY"),
        ({"scenario_id": "bad"}, "FAIL_INTEGRATION_SCENARIO"),
        ({"adapter_id": "bad"}, "FAIL_ADAPTER_IDENTITY"),
        ({"owner": "x"}, "FAIL_INTEGRATION_OWNER"),
        ({"correlation_id": "bad"}, "FAIL_CORRELATION_ID"),
        ({"idempotency_key": "bad"}, "FAIL_IDEMPOTENCY_KEY"),
        ({"interaction_mode": "SOAP"}, "FAIL_INTERACTION_MODE"),
        ({"timeout_policy_ref": "bad"}, "FAIL_POLICY_REFERENCE"),
        ({"retry_policy_ref": "bad"}, "FAIL_POLICY_REFERENCE"),
    ],
)
def test_request_identity_and_policy_fields_fail_closed(
    updates: dict[str, object], code: str
) -> None:
    assert_failure(code, lambda: build_canonical_request(request_values(**updates)))


def test_request_exact_key_boundary_rejects_missing_and_extra() -> None:
    missing = request_values()
    missing.pop("owner")
    assert_failure("FAIL_INTEGRATION_SCHEMA", lambda: build_canonical_request(missing))
    extra = request_values(extra="value")
    assert_failure("FAIL_INTEGRATION_SCHEMA", lambda: build_canonical_request(extra))


@pytest.mark.parametrize(
    "diagnostics",
    [
        [],
        {"token": "REDACTED"},
        {"CUSTOMER": "SYNTHETIC"},
        {"SAFE": ["nested"]},
        {"bad-key": "value"},
        {f"KEY{index}": index for index in range(17)},
    ],
)
def test_diagnostic_context_rejects_unbounded_or_sensitive_shapes(diagnostics: object) -> None:
    assert_failure(
        "FAIL_DIAGNOSTIC_CONTEXT",
        lambda: build_canonical_request(request_values(diagnostic_context=diagnostics)),
    )


def test_sensitive_diagnostic_value_is_rejected_before_gateway_state() -> None:
    prohibited = "api_" + "key=" + "abcdefghijklmnop"
    assert_failure(
        "FAIL_SENSITIVE_VALUE",
        lambda: build_canonical_request(
            request_values(diagnostic_context={"CLASSIFICATION": prohibited})
        ),
    )


def test_disabled_profile_is_allowlisted_but_denied_before_invocation() -> None:
    gateway = IntegrationGateway(
        allowed_adapter_ids=["ADAPTER.SYNTHETIC.DISABLED"], profiles=[profile()]
    )
    result = gateway.submit(build_canonical_request(request_values()))
    assert result.current_state == FAILURE_STATE
    assert result.disposition == FAILURE_DISPOSITION
    assert result.exception_classification == "ADAPTER_DISABLED"
    assert result.adapter_invocation_count == 0
    assert result.network_call_count == 0
    assert gateway.adapter_invocation_count == 0
    assert gateway.network_call_count == 0


@pytest.mark.parametrize(
    ("gateway", "expected"),
    [
        (IntegrationGateway(allowed_adapter_ids=[]), "ADAPTER_NOT_ALLOWLISTED"),
        (
            IntegrationGateway(allowed_adapter_ids=["ADAPTER.SYNTHETIC.DISABLED"]),
            "ADAPTER_ABSENT",
        ),
    ],
)
def test_unallowlisted_and_absent_adapters_fail_closed(
    gateway: IntegrationGateway, expected: str
) -> None:
    result = gateway.submit(build_canonical_request(request_values()))
    assert result.exception_classification == expected
    assert result.disposition == FAILURE_DISPOSITION
    assert (result.adapter_invocation_count, result.network_call_count) == (0, 0)


def test_enabled_synthetic_profile_is_fully_bound_and_still_has_no_effect() -> None:
    enabled = profile(enabled=True)
    gateway = IntegrationGateway(
        allowed_adapter_ids=["ADAPTER.SYNTHETIC.DISABLED"], profiles=[enabled]
    )
    result = gateway.submit(build_canonical_request(request_values()))
    assert result.disposition == SUCCESS_DISPOSITION
    assert result.current_state == "SYNTHETIC_ACCEPTED"
    assert result.exception_classification == "NONE"
    assert (result.adapter_invocation_count, result.network_call_count) == (0, 0)


@pytest.mark.parametrize(
    ("request_update", "classification"),
    [
        ({"capability_id": "CAPABILITY.SYNTHETIC.OTHER"}, "CAPABILITY_POLICY_MISMATCH"),
        ({"interaction_mode": "QUEUE"}, "INTERACTION_MODE_DISABLED"),
        ({"contract_version": "v2"}, "CONTRACT_VERSION_DISABLED"),
        ({"scenario_id": "SCENARIO.SYNTHETIC.OTHER"}, "SCENARIO_DISABLED"),
        ({"owner": "Reliability Operations"}, "OWNER_POLICY_MISMATCH"),
        ({"timeout_policy_ref": "POLICY.TIMEOUT.OTHER"}, "TIMEOUT_POLICY_MISMATCH"),
        ({"retry_policy_ref": "POLICY.RETRY.OTHER"}, "RETRY_POLICY_MISMATCH"),
    ],
)
def test_enabled_profile_rejects_every_binding_mismatch(
    request_update: dict[str, object], classification: str
) -> None:
    gateway = IntegrationGateway(
        allowed_adapter_ids=["ADAPTER.SYNTHETIC.DISABLED"], profiles=[profile(enabled=True)]
    )
    result = gateway.submit(build_canonical_request(request_values(**request_update)))
    assert result.exception_classification == classification
    assert result.disposition == FAILURE_DISPOSITION
    assert (result.adapter_invocation_count, result.network_call_count) == (0, 0)


@pytest.mark.parametrize("field", ["interaction_modes", "contract_versions", "scenario_ids"])
def test_enabled_profile_requires_mode_version_scenario_bindings(field: str) -> None:
    assert_failure("FAIL_ADAPTER_POLICY", lambda: profile(enabled=True, **{field: []}))


def test_profile_allowlist_integrity_and_ambiguity_fail_closed() -> None:
    assert_failure(
        "FAIL_ADAPTER_ALLOWLIST",
        lambda: IntegrationGateway(allowed_adapter_ids=["bad"]),
    )
    unallowed = profile()
    assert_failure(
        "FAIL_ADAPTER_ALLOWLIST",
        lambda: IntegrationGateway(allowed_adapter_ids=["ADAPTER.OTHER"], profiles=[unallowed]),
    )
    forged = replace(unallowed, profile_digest="0" * 64)
    assert_failure(
        "FAIL_ADAPTER_INTEGRITY",
        lambda: IntegrationGateway(
            allowed_adapter_ids=["ADAPTER.SYNTHETIC.DISABLED"], profiles=[forged]
        ),
    )
    gateway = IntegrationGateway(allowed_adapter_ids=["ADAPTER.SYNTHETIC.DISABLED"])
    gateway.register(unallowed)
    changed = profile(owner="Reliability Operations")
    assert_failure("FAIL_ADAPTER_AMBIGUITY", lambda: gateway.register(changed))


def test_replay_is_deterministic_and_digest_mismatch_fails_closed() -> None:
    gateway = IntegrationGateway(
        allowed_adapter_ids=["ADAPTER.SYNTHETIC.DISABLED"], profiles=[profile(enabled=True)]
    )
    original = build_canonical_request(request_values())
    assert gateway.submit(original).disposition == SUCCESS_DISPOSITION
    assert gateway.submit(original).disposition == SUCCESS_DISPOSITION
    changed = build_canonical_request(
        request_values(diagnostic_context={"ATTEMPT": 2, "CLASSIFICATION": "SYNTHETIC"})
    )
    replay = gateway.submit(changed)
    assert replay.exception_classification == "IDEMPOTENCY_REPLAY_MISMATCH"
    forged = replace(original, request_digest="0" * 64)
    assert_failure("FAIL_REQUEST_INTEGRITY", lambda: gateway.submit(forged))


def test_operator_projection_is_failure_only_read_only_and_redacted() -> None:
    gateway = IntegrationGateway(allowed_adapter_ids=[])
    failure = gateway.submit(build_canonical_request(request_values()))
    projection = build_operator_failure_projection(failure)
    assert projection.correlation_id == failure.correlation_id
    assert projection.exception_classification == "ADAPTER_NOT_ALLOWLISTED"
    assert projection.safe_manual_action == "REVIEW_SYNTHETIC_POLICY"
    assert len(projection.projection_digest) == 64
    with pytest.raises(FrozenInstanceError):
        projection.current_state = "MUTATED"  # type: ignore[misc]
    with pytest.raises(TypeError):
        projection.diagnostics["ATTEMPT"] = 9  # type: ignore[index]

    enabled = IntegrationGateway(
        allowed_adapter_ids=["ADAPTER.SYNTHETIC.DISABLED"], profiles=[profile(enabled=True)]
    )
    success = enabled.submit(build_canonical_request(request_values()))
    assert_failure("FAIL_OPERATOR_SCOPE", lambda: build_operator_failure_projection(success))
    forged = replace(failure, network_call_count=1)
    assert_failure("FAIL_OPERATOR_INTEGRITY", lambda: build_operator_failure_projection(forged))


@pytest.mark.parametrize(
    "module",
    ["requests", "httpx", "socket", "urllib.request", "ysf.execution.providers.codex"],
)
def test_business_and_ui_direct_provider_imports_are_rejected(module: str) -> None:
    sources = {"src/business/order.py": f"import {module}\n"}
    assert_failure(
        "FAIL_DIRECT_PROVIDER_DEPENDENCY",
        lambda: assert_owned_integration_dependencies(sources),
    )
    sources = {"src/ui/order.py": f"from {module} import client\n"}
    assert_failure(
        "FAIL_DIRECT_PROVIDER_DEPENDENCY",
        lambda: assert_owned_integration_dependencies(sources),
    )


def test_dependency_check_accepts_owned_boundary_and_non_python_files() -> None:
    assert_owned_integration_dependencies(
        {
            "src/business/order.py": (
                "from ysf.integration_boundary import IntegrationGateway\n"
            ),
            "src/presentation/readme.txt": "import requests",
            "src/integration/adapter.py": "import socket\n",
        }
    )


def test_dependency_check_rejects_malformed_business_source() -> None:
    assert_failure(
        "FAIL_DEPENDENCY_SOURCE",
        lambda: assert_owned_integration_dependencies({"src/business/broken.py": "if"}),
    )


def test_defensive_encoding_and_adapter_profile_branches_fail_closed() -> None:
    assert_failure(
        "FAIL_INTEGRATION_SCHEMA",
        lambda: service._canonical_json({"UNSUPPORTED": {object()}}),
    )
    assert_failure("FAIL_ADAPTER_POLICY", lambda: profile(enabled=1))
    assert_failure("FAIL_INTERACTION_MODE", lambda: profile(interaction_modes=["SOAP"]))
    assert_failure("FAIL_INTEGRATION_VERSION", lambda: profile(contract_versions=["1"]))
    assert_failure("FAIL_INTEGRATION_SCENARIO", lambda: profile(scenario_ids=["bad"]))


def test_result_diagnostics_and_forged_registered_profile_fail_closed() -> None:
    enabled = profile(enabled=True)
    gateway = IntegrationGateway(
        allowed_adapter_ids=["ADAPTER.SYNTHETIC.DISABLED"], profiles=[enabled]
    )
    gateway._profiles[enabled.adapter_id] = replace(enabled, profile_digest="0" * 64)
    result = gateway.submit(build_canonical_request(request_values()))
    assert result.exception_classification == "ADAPTER_PROFILE_INTEGRITY_FAILURE"
    assert dict(result.diagnostics) == {"ATTEMPT": 1, "CLASSIFICATION": "SYNTHETIC"}
