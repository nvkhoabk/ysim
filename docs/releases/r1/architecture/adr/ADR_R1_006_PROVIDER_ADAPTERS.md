# ADR-R1-006 — Payment and Supplier Provider Adapters

## Status

PROPOSED

## Context

Release 1 integrates:

- GPay.
- OnePay.
- Gigago.
- uMoney in R1.1.

The twelve-month target is approximately six suppliers. Sandbox and production contracts may differ. Provider payloads, HTTP methods, signatures, state names and retry behavior must not leak into core domains.

## Decision

All payment and supplier integrations will use provider adapters behind stable internal contracts.

Provider adapters translate between provider-specific protocols and normalized internal commands, results and events.

## Payment provider contract

The normalized payment contract supports:

- Create payment.
- Interpret customer action or redirect.
- Verify callback.
- Verify webhook.
- Query transaction.
- Reconcile unknown outcome.
- Request full refund where supported.
- Normalize provider status.
- Classify temporary and permanent errors.

## Supplier gateway contract

The normalized supplier contract supports:

- Validate availability or procurement.
- Create supplier order.
- Query supplier order.
- Interpret webhook.
- Recover pending order.
- Normalize delivered eSIM data.
- Cancel where supported.
- Classify temporary and permanent errors.

## Configuration

Provider behavior is selected through environment-specific configuration:

- Provider environment.
- Base URL.
- Credential reference.
- Signature or certificate reference.
- HTTP method where contract differences require it.
- Timeout.
- Retry policy.
- Webhook URL.
- Enabled capabilities.

Production behavior must be probed and confirmed before activation. Sandbox observations are not assumed to apply to production.

## Ownership boundaries

Adapters may:

- Perform provider HTTP calls.
- Verify provider signatures.
- Normalize provider payloads.
- Emit provider results to the owning context.

Adapters may not:

- Write arbitrary domain tables.
- Decide canonical business state.
- Create commission.
- Modify orders directly.
- Store plaintext secrets.
- Bypass inbox or idempotency handling.

## Error classification

Adapters return normalized classes:

- Validation.
- Authentication.
- Signature failure.
- Rate limit.
- Timeout.
- Temporary provider failure.
- Permanent provider rejection.
- Unknown outcome.
- Contract mismatch.

Unknown outcomes require reconciliation.

## Raw payloads

Raw payloads are stored through secure references when operationally required.

Logs use masked and normalized data.

## Testing

Each adapter requires:

- Contract tests.
- Signature-verification tests.
- Duplicate-event tests.
- Timeout tests.
- Unknown-outcome tests.
- Sandbox evidence.
- Production contract probe before activation.
- Fixture replay without live provider dependency.

## Consequences

### Positive

- Supports provider growth.
- Isolates protocol differences.
- Enables provider-specific recovery.
- Protects core domains from vendor coupling.

### Negative

- Requires normalized contracts that may not expose every provider feature.
- Adapter test maintenance grows with providers.
- Production probing must be operationally controlled.

## Rejected alternatives

### Provider calls directly from checkout or order services

Rejected because it couples business state to provider protocols and makes retries unsafe.

### One universal untyped provider client

Rejected because payment and supplier semantics differ materially.
