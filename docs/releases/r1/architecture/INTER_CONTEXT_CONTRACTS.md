R1A-02 — Inter-Context Contracts
1. Purpose

This document defines how Release 1 bounded contexts communicate without violating ownership boundaries.

2. Contract types
2.1. Synchronous query

Used when the caller needs an immediate answer and no business state is changed.

Examples:

Checkout queries a Pricing Quote.
Checkout resolves a Reference Artifact.
Procurement reads a Supplier Plan Mapping.
Customer Portal queries an authorized order view.

Requirements:

Explicit request and response schema.
Organization and authorization context.
Correlation ID.
Timeout.
No hidden write side effect.
2.2. Synchronous command

Used when one context requests the owning context to perform a state transition.

Examples:

Checkout requests Order creation.
Operations requests manual eSIM replacement.
Finance requests commission marked as paid.
Customer Experience requests email resend.

Requirements:

Idempotency key where repeat delivery is possible.
Owning-context authorization.
Validation by the owner.
Explicit success and failure contract.
Audit metadata for privileged actions.
2.3. Domain event

Used to announce a completed business fact.

Examples:

SalesOrderCreated
PaymentSucceeded
ProcurementSucceeded
FulfillmentSucceeded
RefundCompleted

Requirements:

Immutable event ID.
Event type and version.
Occurred timestamp.
Aggregate ID.
Organization context.
Correlation ID.
Causation ID.
Idempotent consumer behavior.
2.4. Integration event

Used when communicating with another process, worker, repository or external channel.

Integration events are published through the transactional outbox.

Domain events may be translated into integration events.

Provider webhooks are external events and enter through a provider-specific inbox.

3. Event envelope

Every cross-context event must contain:

event_id
event_type
event_version
occurred_at
producer_context
aggregate_type
aggregate_id
organization_id
correlation_id
causation_id
payload
metadata

Sensitive data must not be placed in events unless required.

QR payload and activation code must never be included in general-purpose events.

Events may contain secure references to an eSIM Asset.

4. Core event contracts
Organization events
OrganizationCreated
OrganizationActivated
OrganizationSuspended
MembershipGranted
MembershipRevoked

Primary consumers:

IAM projections.
Agency Portal.
Operations.
Audit.
Catalog events
ProductOfferPublished
ProductOfferSuspended
ProductLocalizationChanged

Primary consumers:

Storefront projection.
Pricing validation.
Agency Offer validation.
Operations.
Pricing events
PriceEntryPublished
PricingQuoteIssued
PricingQuoteExpired

Primary consumers:

Checkout.
Order snapshotting.
Operations.
Agency Commerce events
AgencyOfferVersionPublished
ReferenceArtifactIssued
ReferenceArtifactRevoked
ReferenceArtifactExpired

Primary consumers:

Agency Portal.
Checkout.
Operations.
Audit.
Checkout events
CheckoutConfirmed
CheckoutSessionExpired

Primary consumers:

Order process.
Operations analytics.
Order events
SalesOrderCreated
SalesOrderCancelled
OrderStatusProjectionChanged

Primary consumers:

Payment orchestration.
Customer Experience.
Agency reporting.
Operations.
Payment events
PaymentSucceeded
PaymentFailed
PaymentExpired
PaymentReconciliationRequired
RefundCompleted
RefundFailed

Primary consumers:

Order projection.
Procurement orchestration.
Commission.
Customer Experience.
Operations.
Procurement events
ProcurementRequested
SupplierOrderSubmitted
SupplierOrderProcessing
ProcurementSucceeded
ProcurementFailed
ProcurementRecoveryRequired

Primary consumers:

Fulfillment orchestration.
Operations.
Order projection.
Fulfillment events
EsimAssetAssigned
EsimAssetReplaced
FulfillmentSucceeded
FulfillmentFailed

Primary consumers:

Delivery.
Commission.
Customer Experience.
Operations.
Audit.
Delivery events
DeliverySucceeded
DeliveryFailed
DeliveryRetryScheduled

Primary consumers:

Customer Experience.
Operations.
Order projection.
Commission events
CommissionAttributed
CommissionAccrued
CommissionEligible
CommissionReversed
CommissionMarkedPaid

Primary consumers:

Agency reporting.
Finance reporting.
Operations.
5. Core synchronous contracts
Resolve Reference Artifact

Caller:

Checkout.

Owner:

Agency Commerce.

Input:

Signed token.
Market.
Request timestamp.

Output:

Agency Offer Version ID.
Agency ID.
Product Offer ID.
Price and currency.
Payment-provider restriction.
Locale.
Commission rule reference.
Validity result.
Issue Pricing Quote

Caller:

Checkout.

Owner:

Pricing.

Input:

Product Offer ID.
Market.
Currency.
Agency Offer Version, when applicable.
Request timestamp.

Output:

Pricing Quote ID.
Selling price.
Currency.
Supplier-cost reference.
Effective-until timestamp.
Price snapshot hash.
Create Sales Order

Caller:

Checkout.

Owner:

Order.

Input:

Confirmed Checkout Session.
Pricing Quote.
Product snapshot.
Customer snapshot.
Agency attribution snapshot.

Output:

Sales Order ID.
Public order reference.
PENDING_PAYMENT state.
Start Payment

Caller:

Commerce orchestration.

Owner:

Payment.

Input:

Sales Order ID.
Amount.
Currency.
Payment provider.
Customer return context.
Idempotency key.

Output:

Payment Intent ID.
Provider action or redirect.
Expiration.
Request Procurement

Caller:

Payment Fulfillment Process.

Owner:

Procurement.

Input:

Sales Order ID.
Order Item ID.
Supplier Plan Mapping snapshot.
Idempotency key.

Output:

Procurement Request ID.
Initial procurement state.
Assign eSIM Asset

Caller:

Fulfillment orchestration.

Owner:

Fulfillment.

Input:

Order Item ID.
Procurement result reference.
Normalized supplier result.
Idempotency key.

Output:

Fulfillment ID.
Secure eSIM Asset reference.
Request Delivery

Caller:

Payment Fulfillment Process.

Owner:

Delivery.

Input:

Order ID.
Customer contact snapshot.
Secure eSIM Asset reference.
Locale.
Delivery idempotency key.

Output:

Delivery Request ID.
Initial delivery state.
Replace eSIM Asset

Caller:

Operations.

Owner:

Fulfillment.

Input:

Fulfillment ID.
Replacement asset.
Operator identity.
Reason.
Idempotency key.

Output:

Updated asset reference.
Previous asset reference.
Audit correlation ID.
6. Process-manager ownership

Process managers belong to the application orchestration layer.

They are not aggregate roots in Order, Payment, Procurement or Fulfillment.

Required process managers:

OrderPaymentProcess
PaymentFulfillmentProcess
RefundCompensationProcess
DeliveryRecoveryProcess

Each process manager stores:

Process ID.
Current orchestration step.
Correlation ID.
Last processed event.
Retry state.
Completion state.
Failure reason.

A process manager must not duplicate the canonical status of another context.

7. Idempotency

Required idempotency scopes:

Operation	Idempotency key scope
Create Sales Order	Checkout Session
Start Payment	Sales Order plus provider
Provider webhook	Provider plus external event ID
Confirm payment	Payment Intent plus provider transaction
Request procurement	Order Item plus fulfillment requirement
Create Supplier Order	Procurement Request
Assign eSIM Asset	Fulfillment plus supplier result
Request delivery	Fulfillment plus channel
Resend delivery	Delivery Request plus resend request
Create commission entry	Order plus commission transition
Refund	Payment Intent plus refund request

Idempotency records must include:

Key.
Operation.
Request hash.
Result reference.
Status.
Expiration or retention.
Correlation ID.

The same key with a different request hash must be rejected.

8. Provider inbox and outbox
Provider inbox

Each provider adapter must persist external events before business processing.

Inbox records include:

Provider.
External event ID.
Received timestamp.
Signature-verification result.
Raw-payload secure reference.
Processing status.
Processing attempts.
Related Payment or Supplier Order.
Failure reason.
Transactional outbox

Business state transition and outbox publication must commit atomically.

Outbox records include:

Event envelope.
Publication status.
Attempt count.
Next-attempt timestamp.
Last error.
9. Failure contracts

Every synchronous command must classify failures as:

Validation failure.
Authorization failure.
Conflict.
Idempotency mismatch.
Temporary dependency failure.
Permanent provider failure.
Not found.
Already completed.
Internal failure.

Temporary failures may be retried.

Permanent failures require a deterministic response or Operations Case.

Unknown provider outcomes must enter reconciliation rather than being treated as failed.

10. Forbidden interactions

The following are prohibited:

Checkout writing directly to Order tables.
Order writing directly to Payment records.
Payment writing directly to Procurement records.
Procurement creating eSIM Asset records.
Fulfillment sending email directly.
Delivery changing Fulfillment status.
Commission changing Sales Order data.
Operations updating foreign-context tables.
Provider adapters querying arbitrary business repositories.
Storefront sending trusted price or commission values.
Reference QR exposing unsigned mutable commercial fields.
Cross-context imports of repository implementations.
11. Read-model projections

Required projections include:

Storefront catalog view.
Customer order view.
Agency order and revenue view.
Agency commission view.
Operations transaction timeline.
Finance payment and commission view.

Projection rules:

Projections are rebuildable.
Projection failures do not change canonical business state.
Projection lag must be observable.
Projection access remains organization-scoped.
Projection data cannot authorize a write without owner validation.
12. Contract versioning

Published contracts use explicit versions.

Backward-incompatible changes require:

New contract version.
Consumer-impact analysis.
Migration period.
Compatibility tests.
Deprecation date.
Removal approval.

Provider contracts are versioned separately from internal domain contracts.
