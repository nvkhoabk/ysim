"""Deterministic, non-operational configuration and access controls for S03."""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any, NoReturn, TypeAlias

from ysf.secure_factory.models import FactoryFailure
from ysf.secure_factory.sensitive import scan_text

Scalar: TypeAlias = str | int | bool | None

SCOPES = ("GLOBAL", "ORGANIZATION", "DEPARTMENT", "STOREFRONT", "USER")
SCOPE_RANK = {scope: rank for rank, scope in enumerate(SCOPES)}
AUTHENTICATION_METHODS = frozenset({"SERVICE_ASSERTION", "SYNTHETIC_OTP", "SYNTHETIC_PASSWORD"})
ASSURANCE_REQUIREMENTS = frozenset({"SYNTHETIC_ASSURANCE_LEVEL_1", "SYNTHETIC_ASSURANCE_LEVEL_2"})
SESSION_RULES = frozenset({"SOURCE_ONLY_NO_SESSION", "SYNTHETIC_SINGLE_OPERATION"})
FAILURE_BEHAVIORS = frozenset({"DENY_BEFORE_PROVIDER_OR_DELIVERY"})
_POLICY_RULE_KEYS = frozenset(
    {"role", "method", "assurance_requirement", "session_rule", "failure_behavior"}
)
_IDENTIFIER = re.compile(r"^[A-Z0-9][A-Z0-9_.:-]{2,127}$")
_TENANT = re.compile(r"^TENANT:[A-Z0-9][A-Z0-9_.-]{2,63}$")
_OWNER = re.compile(r"^[A-Za-z][A-Za-z0-9 ._-]{2,79}$")
_CORRELATION = re.compile(r"^SYN-[A-Z0-9-]{6,64}$")
_REDACT_KEYS = frozenset(
    {"authorization", "credential", "email", "private_key", "proof", "secret", "token"}
)


def _fail(code: str, message: str, **details: object) -> NoReturn:
    raise FactoryFailure(code, message, details=dict(details))


def _canonical_json(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value)).hexdigest()


def _canonical_values(values: Mapping[str, Scalar]) -> bytes:
    return _canonical_json(dict(values))


def _parse_utc(value: str) -> datetime:
    if not value.endswith("Z"):
        _fail("FAIL_CONFIG_INTERVAL", "Effective interval must use UTC Z form.")
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        _fail("FAIL_CONFIG_INTERVAL", "Effective interval is malformed.")
    return parsed


def _require_safe_text(value: str, code: str) -> None:
    if scan_text(value, location="synthetic-input"):
        _fail(code, "Sensitive input was rejected before state mutation.")


@dataclass(frozen=True)
class ConfigurationSchema:
    """Exact schema and override boundary for one configuration family."""

    version: str
    fields: tuple[tuple[str, str], ...]
    required_fields: frozenset[str]
    overridable_fields: frozenset[str]

    @classmethod
    def create(
        cls,
        *,
        version: str,
        fields: Mapping[str, str],
        required_fields: Iterable[str],
        overridable_fields: Iterable[str],
    ) -> ConfigurationSchema:
        if _IDENTIFIER.fullmatch(version) is None:
            _fail("FAIL_CONFIG_SCHEMA", "Schema version is malformed.")
        ordered = tuple(sorted(fields.items()))
        allowed_types = {"boolean", "integer", "null", "string"}
        if not ordered or any(
            _IDENTIFIER.fullmatch(name) is None or kind not in allowed_types
            for name, kind in ordered
        ):
            _fail("FAIL_CONFIG_SCHEMA", "Schema fields are malformed.")
        names = {name for name, _ in ordered}
        required = frozenset(required_fields)
        overridable = frozenset(overridable_fields)
        if not required <= names or not overridable <= names:
            _fail("FAIL_CONFIG_SCHEMA", "Schema field sets exceed declared fields.")
        return cls(version, ordered, required, overridable)

    @property
    def field_types(self) -> dict[str, str]:
        return dict(self.fields)


@dataclass(frozen=True)
class ConfigurationRecord:
    """Immutable configuration identity/version and canonical record binding."""

    identity: str
    version: int
    schema_version: str
    scope: str
    tenant_id: str | None
    owner: str
    effective_from: str
    effective_until: str
    parent_identity: str | None
    values: tuple[tuple[str, Scalar], ...]
    audit_metadata: tuple[tuple[str, str], ...]
    value_digest: str
    record_digest: str

    @property
    def value_map(self) -> dict[str, Scalar]:
        return dict(self.values)

    def is_effective(self, at: str) -> bool:
        point = _parse_utc(at)
        return _parse_utc(self.effective_from) <= point < _parse_utc(self.effective_until)


def build_configuration_record(
    *,
    identity: str,
    version: int,
    schema: ConfigurationSchema,
    scope: str,
    tenant_id: str | None,
    owner: str,
    effective_from: str,
    effective_until: str,
    values: Mapping[str, Scalar],
    audit_metadata: Mapping[str, str],
    parent_identity: str | None = None,
) -> ConfigurationRecord:
    """Validate completely and then return immutable canonical state."""

    if _IDENTIFIER.fullmatch(identity) is None or type(version) is not int or version < 1:
        _fail("FAIL_CONFIG_IDENTITY", "Configuration identity/version is invalid.")
    if scope not in SCOPE_RANK or _OWNER.fullmatch(owner) is None:
        _fail("FAIL_CONFIG_SCOPE_OWNER", "Configuration scope/owner is invalid.")
    if (scope == "GLOBAL" and tenant_id is not None) or (
        scope != "GLOBAL"
        and (not isinstance(tenant_id, str) or _TENANT.fullmatch(tenant_id) is None)
    ):
        _fail("FAIL_CONFIG_TENANT", "Configuration tenant binding is missing or malformed.")
    start = _parse_utc(effective_from)
    end = _parse_utc(effective_until)
    if start >= end:
        _fail("FAIL_CONFIG_INTERVAL", "Effective interval must be non-empty.")
    if parent_identity is not None and _IDENTIFIER.fullmatch(parent_identity) is None:
        _fail("FAIL_CONFIG_PARENT", "Parent identity is malformed.")
    declared = schema.field_types
    if not schema.required_fields <= set(values) or not set(values) <= set(declared):
        _fail("FAIL_CONFIG_SCHEMA", "Configuration keys differ from the schema.")
    python_types: dict[str, type[object]] = {
        "boolean": bool,
        "integer": int,
        "null": type(None),
        "string": str,
    }
    for key, value in values.items():
        if type(value) is not python_types[declared[key]]:
            _fail("FAIL_CONFIG_SCHEMA", "Configuration value type is incorrect.", key=key)
    encoded_values = _canonical_values(values)
    _require_safe_text(encoded_values.decode("utf-8"), "FAIL_CONFIG_SENSITIVE")
    if not audit_metadata or any(
        _IDENTIFIER.fullmatch(key) is None or not isinstance(value, str) or not value
        for key, value in audit_metadata.items()
    ):
        _fail("FAIL_CONFIG_AUDIT", "Audit metadata is incomplete or malformed.")
    _require_safe_text(json.dumps(dict(audit_metadata), sort_keys=True), "FAIL_CONFIG_SENSITIVE")
    value_digest = hashlib.sha256(encoded_values).hexdigest()
    record_binding = {
        "audit_metadata": dict(sorted(audit_metadata.items())),
        "effective_from": effective_from,
        "effective_until": effective_until,
        "identity": identity,
        "owner": owner,
        "parent_identity": parent_identity,
        "schema_version": schema.version,
        "scope": scope,
        "tenant_id": tenant_id,
        "value_digest": value_digest,
        "version": version,
    }
    return ConfigurationRecord(
        identity=identity,
        version=version,
        schema_version=schema.version,
        scope=scope,
        tenant_id=tenant_id,
        owner=owner,
        effective_from=effective_from,
        effective_until=effective_until,
        parent_identity=parent_identity,
        values=tuple(sorted(values.items())),
        audit_metadata=tuple(sorted(audit_metadata.items())),
        value_digest=value_digest,
        record_digest=_digest(record_binding),
    )


class ConfigurationRegistry:
    """In-memory source reference that rejects ambiguous immutable versions."""

    def __init__(self) -> None:
        self._records: dict[tuple[str, int], ConfigurationRecord] = {}

    def add(self, record: ConfigurationRecord) -> None:
        key = (record.identity, record.version)
        existing = self._records.get(key)
        if existing is not None and existing != record:
            _fail(
                "FAIL_CONFIG_AMBIGUITY",
                "The same configuration identity/version binds different bytes.",
            )
        self._records.setdefault(key, record)

    def remove(self, identity: str, version: int) -> ConfigurationRecord:
        try:
            return self._records.pop((identity, version))
        except KeyError:
            _fail("FAIL_CONFIG_MISSING", "Configuration record does not exist.")

    @property
    def records(self) -> tuple[ConfigurationRecord, ...]:
        return tuple(sorted(self._records.values(), key=lambda item: (item.identity, item.version)))


@dataclass(frozen=True)
class EffectiveConfiguration:
    tenant_id: str | None
    values: tuple[tuple[str, Scalar], ...]
    source_records: tuple[tuple[str, str], ...]
    resolution_digest: str


def _record_binding(record: ConfigurationRecord) -> dict[str, object]:
    return {
        "audit_metadata": dict(record.audit_metadata),
        "effective_from": record.effective_from,
        "effective_until": record.effective_until,
        "identity": record.identity,
        "owner": record.owner,
        "parent_identity": record.parent_identity,
        "schema_version": record.schema_version,
        "scope": record.scope,
        "tenant_id": record.tenant_id,
        "value_digest": record.value_digest,
        "version": record.version,
    }


def _validate_record_integrity(record: ConfigurationRecord) -> None:
    expected_value_digest = hashlib.sha256(_canonical_values(record.value_map)).hexdigest()
    if expected_value_digest != record.value_digest or _digest(_record_binding(record)) != (
        record.record_digest
    ):
        _fail("FAIL_CONFIG_INTEGRITY", "Configuration record binding is incorrect.")


def _validate_tenant_edge(child: ConfigurationRecord, parent: ConfigurationRecord) -> None:
    if parent.scope == "GLOBAL":
        if parent.tenant_id is not None:
            _fail("FAIL_CONFIG_TENANT", "Global parent must be tenant-neutral.")
        return
    if child.tenant_id is None or child.tenant_id != parent.tenant_id:
        _fail("FAIL_CONFIG_TENANT", "Cross-tenant configuration inheritance is forbidden.")


def resolve_effective_configuration(
    records: Iterable[ConfigurationRecord],
    schema: ConfigurationSchema,
    *,
    at: str,
) -> EffectiveConfiguration:
    """Resolve one explicit tenant-safe chain from the highest active scope."""

    active = tuple(record for record in records if record.is_effective(at))
    if not active:
        _fail("FAIL_CONFIG_MISSING", "No effective configuration exists.")
    by_identity: dict[str, ConfigurationRecord] = {}
    for record in active:
        _validate_record_integrity(record)
        if record.schema_version != schema.version:
            _fail("FAIL_CONFIG_SCHEMA", "Configuration schema versions differ.")
        if record.identity in by_identity:
            _fail("FAIL_CONFIG_AMBIGUITY", "Multiple active versions are ambiguous.")
        by_identity[record.identity] = record
    highest = max(SCOPE_RANK[record.scope] for record in active)
    leaves = [record for record in active if SCOPE_RANK[record.scope] == highest]
    if len(leaves) != 1:
        _fail("FAIL_CONFIG_AMBIGUITY", "Effective configuration has multiple leaves.")
    selected_tenant = leaves[0].tenant_id
    if any(record.scope != "GLOBAL" and record.tenant_id != selected_tenant for record in active):
        _fail("FAIL_CONFIG_TENANT", "Resolution input contains ambiguous tenant bindings.")
    for record in active:
        path: set[str] = set()
        current_record = record
        while current_record.parent_identity is not None:
            if current_record.identity in path:
                _fail("FAIL_CONFIG_CYCLE", "Configuration inheritance contains a cycle.")
            path.add(current_record.identity)
            parent = by_identity.get(current_record.parent_identity)
            if parent is None:
                _fail("FAIL_CONFIG_PARENT", "Configuration parent is missing.")
            current_record = parent
    for record in active:
        if record.parent_identity is None:
            continue
        parent = by_identity[record.parent_identity]
        _validate_tenant_edge(record, parent)
        if SCOPE_RANK[parent.scope] >= SCOPE_RANK[record.scope]:
            _fail("FAIL_CONFIG_SCOPE", "Configuration scope precedence is invalid.")
    chain: list[ConfigurationRecord] = []
    current = leaves[0]
    while True:
        chain.append(current)
        if current.parent_identity is None:
            break
        current = by_identity[current.parent_identity]
    merged: dict[str, Scalar] = {}
    sources: dict[str, str] = {}
    for record in reversed(chain):
        for key, value in record.values:
            if key in merged and merged[key] != value and key not in schema.overridable_fields:
                _fail("FAIL_CONFIG_OVERRIDE", "Configuration override is unauthorized.")
            if key in merged and merged[key] == value:
                continue
            merged[key] = value
            tenant_binding = record.tenant_id or "TENANT:NEUTRAL"
            sources[key] = (
                f"{tenant_binding}|{record.identity}:{record.version}|{record.record_digest}"
            )
    canonical_values: dict[str, Scalar] = dict(sorted(merged.items()))
    canonical_sources = dict(sorted(sources.items()))
    return EffectiveConfiguration(
        tenant_id=selected_tenant,
        values=tuple(canonical_values.items()),
        source_records=tuple(canonical_sources.items()),
        resolution_digest=_digest(
            {
                "tenant_id": selected_tenant,
                "sources": canonical_sources,
                "values": canonical_values,
            }
        ),
    )


@dataclass(frozen=True)
class AuthenticationRule:
    actor_class: str
    role: str
    method: str
    assurance_requirement: str
    session_rule: str
    failure_behavior: str


@dataclass(frozen=True)
class AuthenticationPolicy:
    rules: tuple[AuthenticationRule, ...]
    policy_digest: str

    @classmethod
    def create(cls, actor_rules: Mapping[str, Mapping[str, str]]) -> AuthenticationPolicy:
        if not actor_rules:
            _fail("FAIL_AUTH_POLICY", "Authentication policy is empty.")
        rules: list[AuthenticationRule] = []
        for actor_class, raw_rule in actor_rules.items():
            if not isinstance(raw_rule, Mapping) or set(raw_rule) != _POLICY_RULE_KEYS:
                _fail("FAIL_AUTH_POLICY", "Authentication rule keys are incomplete or extra.")
            if not all(isinstance(value, str) for value in raw_rule.values()):
                _fail("FAIL_AUTH_POLICY", "Authentication rule values must be strings.")
            rule = AuthenticationRule(actor_class=actor_class, **dict(raw_rule))
            if (
                _IDENTIFIER.fullmatch(rule.actor_class) is None
                or _IDENTIFIER.fullmatch(rule.role) is None
                or rule.method not in AUTHENTICATION_METHODS
                or rule.assurance_requirement not in ASSURANCE_REQUIREMENTS
                or rule.session_rule not in SESSION_RULES
                or rule.failure_behavior not in FAILURE_BEHAVIORS
            ):
                _fail("FAIL_AUTH_POLICY", "Authentication rule is malformed.")
            rules.append(rule)
        ordered = tuple(sorted(rules, key=lambda item: item.actor_class))
        return cls(ordered, _digest([asdict(rule) for rule in ordered]))

    def rule_for(self, actor_class: str) -> AuthenticationRule:
        if not self.rules or len({rule.actor_class for rule in self.rules}) != len(self.rules):
            _fail("FAIL_AUTH_POLICY", "Authentication policy actors are empty or duplicated.")
        for rule in self.rules:
            if type(rule) is not AuthenticationRule:
                _fail("FAIL_AUTH_POLICY", "Authentication policy rule type is invalid.")
            if (
                _IDENTIFIER.fullmatch(rule.actor_class) is None
                or _IDENTIFIER.fullmatch(rule.role) is None
                or rule.method not in AUTHENTICATION_METHODS
                or rule.assurance_requirement not in ASSURANCE_REQUIREMENTS
                or rule.session_rule not in SESSION_RULES
                or rule.failure_behavior not in FAILURE_BEHAVIORS
            ):
                _fail("FAIL_AUTH_POLICY", "Authentication policy contains an invalid rule.")
        selected = [rule for rule in self.rules if rule.actor_class == actor_class]
        if len(selected) != 1:
            _fail("FAIL_AUTH_POLICY", "Actor class is unknown or ambiguous.")
        expected_digest = _digest([asdict(rule) for rule in self.rules])
        if expected_digest != self.policy_digest:
            _fail("FAIL_AUTH_POLICY", "Authentication policy digest is incorrect.")
        return selected[0]


@dataclass(frozen=True)
class AuthenticationDecision:
    result: str
    actor_class: str
    role: str
    method: str
    assurance_requirement: str
    assurance_result: str
    session_rule: str
    session_rule_result: str
    failure_behavior: str
    policy_digest: str
    evidence_digest: str


def _authentication_evidence_payload(
    *,
    result: str,
    rule: AuthenticationRule,
    assurance_result: str,
    session_rule_result: str,
    policy_digest: str,
) -> dict[str, str]:
    return {
        "actor_class": rule.actor_class,
        "assurance_requirement": rule.assurance_requirement,
        "assurance_result": assurance_result,
        "failure_behavior": rule.failure_behavior,
        "method": rule.method,
        "policy_digest": policy_digest,
        "result": result,
        "role": rule.role,
        "session_rule": rule.session_rule,
        "session_rule_result": session_rule_result,
    }


def authenticate(
    policy: AuthenticationPolicy,
    *,
    actor_class: str,
    role: str,
    method: str,
    synthetic_proof: str,
    assurance_result: str,
    session_rule_result: str,
) -> AuthenticationDecision:
    if type(policy) is not AuthenticationPolicy:
        _fail("FAIL_AUTH_POLICY", "Authentication policy type is invalid.")
    if _IDENTIFIER.fullmatch(actor_class) is None or _IDENTIFIER.fullmatch(role) is None:
        _fail("FAIL_AUTHENTICATION_METHOD", "Authentication identity is malformed.")
    rule = policy.rule_for(actor_class)
    if role != rule.role or method != rule.method or method not in AUTHENTICATION_METHODS:
        _fail("FAIL_AUTHENTICATION_METHOD", "Actor role or method is not allowlisted.")
    if assurance_result != rule.assurance_requirement:
        _fail("FAIL_AUTHENTICATION_ASSURANCE", "Authentication assurance did not match policy.")
    if session_rule_result != rule.session_rule:
        _fail("FAIL_AUTHENTICATION_SESSION", "Authentication session rule did not match policy.")
    if rule.failure_behavior != "DENY_BEFORE_PROVIDER_OR_DELIVERY":
        _fail("FAIL_AUTH_POLICY", "Authentication failure behavior is not fail-closed.")
    if synthetic_proof not in {"SYNTHETIC_REJECTED", "SYNTHETIC_VERIFIED"}:
        _fail("FAIL_AUTHENTICATION_PROOF", "Only synthetic proof status is accepted.")
    result = "PASS" if synthetic_proof == "SYNTHETIC_VERIFIED" else "FAIL"
    payload = _authentication_evidence_payload(
        result=result,
        rule=rule,
        assurance_result=assurance_result,
        session_rule_result=session_rule_result,
        policy_digest=policy.policy_digest,
    )
    return AuthenticationDecision(**payload, evidence_digest=_digest(payload))


@dataclass(frozen=True)
class AccessGrant:
    actor_class: str
    role: str
    action: str
    resource: str
    data_scope: str


@dataclass(frozen=True)
class AccessRequest:
    subject: str
    actor_class: str
    role: str
    action: str
    resource: str
    data_scope: str
    correlation_id: str


@dataclass(frozen=True)
class AccessDecision:
    result: str
    policy_digest: str
    authentication_evidence_digest: str
    request_digest: str
    grant_digest: str
    decision_digest: str
    audit_record: tuple[tuple[str, str], ...]


def _validate_access_text(value: str) -> None:
    if _IDENTIFIER.fullmatch(value) is None:
        _fail("FAIL_AUTHORIZATION_INPUT", "Access-control input is malformed.")
    _require_safe_text(value, "FAIL_AUTHORIZATION_SENSITIVE")


def _request_payload(request: AccessRequest) -> dict[str, str]:
    if type(request) is not AccessRequest:
        _fail("FAIL_AUTHORIZATION_INPUT", "Access request type is invalid.")
    for value in (
        request.subject,
        request.actor_class,
        request.role,
        request.action,
        request.resource,
        request.data_scope,
    ):
        _validate_access_text(value)
    if _CORRELATION.fullmatch(request.correlation_id) is None:
        _fail("FAIL_AUTHORIZATION_INPUT", "Audit correlation identifier is malformed.")
    return asdict(request)


def _grant_payload(grants: Iterable[AccessGrant]) -> list[dict[str, str]]:
    materialized = tuple(grants)
    for grant in materialized:
        if type(grant) is not AccessGrant:
            _fail("FAIL_AUTHORIZATION_INPUT", "Access grant type is invalid.")
        for value in asdict(grant).values():
            _validate_access_text(value)
    return sorted((asdict(grant) for grant in materialized), key=_canonical_json)


def _validate_authentication_decision(
    policy: AuthenticationPolicy, decision: AuthenticationDecision
) -> AuthenticationRule:
    rule = policy.rule_for(decision.actor_class)
    payload = _authentication_evidence_payload(
        result=decision.result,
        rule=rule,
        assurance_result=decision.assurance_result,
        session_rule_result=decision.session_rule_result,
        policy_digest=policy.policy_digest,
    )
    expected = AuthenticationDecision(**payload, evidence_digest=_digest(payload))
    if decision != expected:
        _fail("FAIL_AUTHENTICATION_EVIDENCE", "Authentication evidence is forged or mismatched.")
    return rule


def authorize(
    policy: AuthenticationPolicy,
    authentication: AuthenticationDecision,
    request: AccessRequest,
    grants: Iterable[AccessGrant],
) -> AccessDecision:
    if type(authentication) is not AuthenticationDecision:
        _fail("FAIL_AUTHENTICATION_EVIDENCE", "Authentication evidence type is invalid.")
    rule = _validate_authentication_decision(policy, authentication)
    request_payload = _request_payload(request)
    grant_payload = _grant_payload(grants)
    request_digest = _digest(request_payload)
    grant_digest = _digest(grant_payload)
    expected_grant = asdict(
        AccessGrant(
            request.actor_class,
            request.role,
            request.action,
            request.resource,
            request.data_scope,
        )
    )
    if (
        authentication.result != "PASS"
        or authentication.actor_class != request.actor_class
        or authentication.role != request.role
        or rule.role != request.role
    ):
        result = "DENY"
    else:
        result = "ALLOW" if expected_grant in grant_payload else "DENY"
    subject_digest = hashlib.sha256(request.subject.encode()).hexdigest()
    correlation_digest = hashlib.sha256(request.correlation_id.encode()).hexdigest()
    audit = {
        "action": request.action,
        "actor_class": request.actor_class,
        "assurance_result": authentication.assurance_result,
        "authentication_method": authentication.method,
        "authorization_result": result,
        "correlation_digest": correlation_digest,
        "data_scope": request.data_scope,
        "resource": request.resource,
        "role": request.role,
        "session_rule_result": authentication.session_rule_result,
        "subject_digest": subject_digest,
    }
    decision_payload = {
        "audit": audit,
        "authentication_evidence_digest": authentication.evidence_digest,
        "grant_digest": grant_digest,
        "policy_digest": policy.policy_digest,
        "request_digest": request_digest,
    }
    return AccessDecision(
        result=result,
        policy_digest=policy.policy_digest,
        authentication_evidence_digest=authentication.evidence_digest,
        request_digest=request_digest,
        grant_digest=grant_digest,
        decision_digest=_digest(decision_payload),
        audit_record=tuple(sorted(audit.items())),
    )


def redact_for_output(fields: Mapping[str, str]) -> tuple[tuple[str, str], ...]:
    redacted: dict[str, str] = {}
    for key, value in fields.items():
        if key.casefold() in _REDACT_KEYS or scan_text(value, location="output"):
            redacted[key] = "<REDACTED>"
        else:
            redacted[key] = value
    return tuple(sorted(redacted.items()))


@dataclass(frozen=True)
class PreExecutionAccess:
    result: str
    provider_invoked: bool
    delivery_performed: bool
    decision_digest: str


def assert_pre_execution_access(
    policy: AuthenticationPolicy,
    request: AccessRequest,
    grants: Iterable[AccessGrant],
    *,
    method: str,
    synthetic_proof: str,
    assurance_result: str,
    session_rule_result: str,
) -> PreExecutionAccess:
    """Re-run authn/authz from immutable inputs; never trust caller decisions."""

    if type(policy) is not AuthenticationPolicy or type(request) is not AccessRequest:
        _fail(
            "FAIL_PRE_EXECUTION_INPUT",
            "Pre-execution boundary requires immutable policy and request inputs.",
        )
    authentication = authenticate(
        policy,
        actor_class=request.actor_class,
        role=request.role,
        method=method,
        synthetic_proof=synthetic_proof,
        assurance_result=assurance_result,
        session_rule_result=session_rule_result,
    )
    if authentication.result != "PASS":
        _fail("FAIL_PRE_EXECUTION_AUTHENTICATION", "Authentication did not pass.")
    authorization = authorize(policy, authentication, request, grants)
    if authorization.result != "ALLOW":
        _fail("FAIL_PRE_EXECUTION_AUTHORIZATION", "Authorization did not allow access.")
    return PreExecutionAccess(
        result="PASS",
        provider_invoked=False,
        delivery_performed=False,
        decision_digest=authorization.decision_digest,
    )
