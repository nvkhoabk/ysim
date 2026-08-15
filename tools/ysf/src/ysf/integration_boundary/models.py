"""Immutable source-only records for the S04 integration boundary."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import TypeAlias

DiagnosticScalar: TypeAlias = str | int | bool | None


@dataclass(frozen=True)
class CanonicalIntegrationRequest:
    """Versioned synthetic request captured before routing decisions."""

    contract_version: str
    capability_id: str
    scenario_id: str
    idempotency_key: str
    correlation_id: str
    interaction_mode: str
    adapter_id: str
    owner: str
    timeout_policy_ref: str
    retry_policy_ref: str
    diagnostic_context: tuple[tuple[str, DiagnosticScalar], ...]
    request_digest: str

    @property
    def diagnostics(self) -> MappingProxyType[str, DiagnosticScalar]:
        return MappingProxyType(dict(self.diagnostic_context))


@dataclass(frozen=True)
class CanonicalIntegrationResult:
    """Deterministic result with no provider or transport side effect."""

    contract_version: str
    request_digest: str
    capability_id: str
    scenario_id: str
    correlation_id: str
    interaction_mode: str
    adapter_id: str
    owner: str
    current_state: str
    disposition: str
    exception_classification: str
    reconciliation_eligible: bool
    alert_eligible: bool
    safe_manual_action: str
    diagnostic_context: tuple[tuple[str, DiagnosticScalar], ...]
    adapter_invocation_count: int
    network_call_count: int
    result_digest: str

    @property
    def diagnostics(self) -> MappingProxyType[str, DiagnosticScalar]:
        return MappingProxyType(dict(self.diagnostic_context))


@dataclass(frozen=True)
class AdapterProfile:
    """Explicit source policy for one replaceable synthetic adapter."""

    adapter_id: str
    capability_id: str
    enabled: bool
    interaction_modes: tuple[str, ...]
    contract_versions: tuple[str, ...]
    scenario_ids: tuple[str, ...]
    owner: str
    timeout_policy_ref: str
    retry_policy_ref: str
    profile_digest: str


@dataclass(frozen=True)
class OperatorFailureProjection:
    """Bounded read-only projection over one synthetic failure result."""

    correlation_id: str
    current_state: str
    adapter_id: str
    capability_id: str
    exception_classification: str
    reconciliation_eligible: bool
    alert_eligible: bool
    safe_manual_action: str
    diagnostic_context: tuple[tuple[str, DiagnosticScalar], ...]
    source_result_digest: str
    projection_digest: str

    @property
    def diagnostics(self) -> MappingProxyType[str, DiagnosticScalar]:
        return MappingProxyType(dict(self.diagnostic_context))
