from __future__ import annotations

from ysf.integration_boundary import (
    FAILURE_DISPOSITION,
    IntegrationGateway,
    build_adapter_profile,
    build_canonical_request,
    build_operator_failure_projection,
)


def test_synthetic_request_pipeline_has_bounded_operator_visibility_and_zero_effects() -> None:
    profile = build_adapter_profile(
        adapter_id="ADAPTER.SYNTHETIC.NOTIFICATION",
        capability_id="CAPABILITY.SYNTHETIC.NOTIFICATION",
        enabled=False,
        interaction_modes=["EVENT", "QUEUE"],
        contract_versions=["v1"],
        scenario_ids=["SCENARIO.SYNTHETIC.NOTIFICATION.FAILURE"],
        owner="Platform Integration",
        timeout_policy_ref="POLICY.TIMEOUT.SYNTHETIC",
        retry_policy_ref="POLICY.RETRY.NONE",
    )
    gateway = IntegrationGateway(
        allowed_adapter_ids=["ADAPTER.SYNTHETIC.NOTIFICATION"], profiles=[profile]
    )
    request = build_canonical_request(
        {
            "contract_version": "v1",
            "capability_id": "CAPABILITY.SYNTHETIC.NOTIFICATION",
            "scenario_id": "SCENARIO.SYNTHETIC.NOTIFICATION.FAILURE",
            "idempotency_key": "IDEM-SYNTHETIC-NOTIFICATION-001",
            "correlation_id": "SYN-NOTIFICATION-FAILURE-001",
            "interaction_mode": "EVENT",
            "adapter_id": "ADAPTER.SYNTHETIC.NOTIFICATION",
            "owner": "Platform Integration",
            "timeout_policy_ref": "POLICY.TIMEOUT.SYNTHETIC",
            "retry_policy_ref": "POLICY.RETRY.NONE",
            "diagnostic_context": {
                "ATTEMPT": 1,
                "CLASSIFICATION": "SYNTHETIC_FAILURE",
            },
        }
    )
    result = gateway.submit(request)
    projection = build_operator_failure_projection(result)

    assert result.disposition == FAILURE_DISPOSITION
    assert result.exception_classification == "ADAPTER_DISABLED"
    assert result.adapter_invocation_count == 0
    assert result.network_call_count == 0
    assert gateway.adapter_invocation_count == 0
    assert gateway.network_call_count == 0
    assert projection.correlation_id == request.correlation_id
    assert projection.current_state == "SYNTHETIC_FAILURE"
    assert projection.reconciliation_eligible is True
    assert projection.alert_eligible is True
    assert projection.safe_manual_action == "REVIEW_SYNTHETIC_POLICY"
