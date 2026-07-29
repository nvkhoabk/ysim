# R1A-02 — Domain Context Map

## 1. Purpose

This document defines the bounded contexts and dependency direction for YSim Global eSIM Commerce & Distribution Platform Release 1.

It establishes:

* Business ownership boundaries.
* Aggregate ownership.
* Permitted dependencies.
* Cross-context workflow boundaries.
* Separation between business domains and provider integrations.
* Rules for modular-monolith implementation.

This document does not define physical database tables or final API schemas.

---

## 2. Architecture style

Release 1 uses a modular monolith.

Each bounded context must have its own:

* Domain model.
* Application services.
* Repository interfaces.
* Authorization policies.
* Published contracts.
* Domain events.
* Tests.
* Runtime evidence.

A context must not access another context's repository or tables directly.

Cross-context workflows are coordinated through:

* Published application contracts.
* Domain events.
* Transactional outbox.
* Process managers.
* Read-model projections.

Provider-specific code must remain behind adapter interfaces.

---

## 3. Bounded contexts

### 3.1. Identity and Access Context

Identifier:

```text
IAM
```

Responsibilities:

* Global identity.
* Authentication.
* Authenticated sessions.
* Role assignment.
* Permission evaluation.
* Organization-context selection.
* Customer magic-link authentication.
* Access-token verification.
* Privileged-access enforcement.

Aggregate roots:

* `Identity`
* `AuthenticationSession`
* `AccessGrant`
* `MagicLinkGrant`

Does not own:

* Agency profile.
* Sales Order.
* Customer order history.
* Commission.
* Support case.

Published capabilities:

* Authenticate principal.
* Validate session.
* Resolve active organization.
* Evaluate permission.
* Issue and verify magic-link access.

---

### 3.2. Organization and Agency Context

Identifier:

```text
ORG
```

Responsibilities:

* Organization lifecycle.
* Agency profile.
* Organization membership.
* Agency status.
* Organization-scoped access metadata.
* Agency product eligibility reference.
* Organization market configuration.

Aggregate roots:

* `Organization`
* `OrganizationMembership`
* `AgencyProfile`

Organization types:

* `PLATFORM`
* `AGENCY`

Initial organizations:

* YSim platform organization.
* Pilot agency organizations.

Does not own:

* Authentication credentials.
* Product pricing.
* Agency Offer.
* Commission ledger.
* Agency-attributed orders.

Published events:

* `OrganizationCreated`
* `OrganizationActivated`
* `OrganizationSuspended`
* `AgencyProfileCreated`
* `MembershipGranted`
* `MembershipRevoked`

---

### 3.3. Catalog Context

Identifier:

```text
CAT
```

Responsibilities:

* Destination.
* Region.
* Canonical Product.
* Product Offer.
* Data allowance.
* Package validity.
* Activation policy.
* Supported network/operator metadata.
* Product localization metadata.
* WooCommerce content reference.
* Product publication lifecycle.

Aggregate roots:

* `Destination`
* `Region`
* `Product`
* `ProductOffer`

The Catalog Context owns the commercial identity of a product independently of supplier-specific plan structures.

Does not own:

* Selling price.
* Supplier cost.
* Supplier fulfillment status.
* Inventory allocation.
* Marketing page rendering.

Published events:

* `ProductCreated`
* `ProductOfferCreated`
* `ProductOfferPublished`
* `ProductOfferSuspended`
* `ProductLocalizationChanged`

---

### 3.4. Supplier Management Context

Identifier:

```text
SUP
```

Responsibilities:

* Supplier registry.
* Supplier status.
* Supplier Plan normalization.
* Product Offer to Supplier Plan mapping.
* Supplier contract profile.
* Supplier environment configuration reference.
* Supplier health diagnostics.
* Supplier adapter selection.

Aggregate roots:

* `Supplier`
* `SupplierPlan`
* `SupplierPlanMapping`
* `SupplierContractProfile`

The context stores credential references, not plaintext secrets.

Does not own:

* Sales Order.
* Procurement lifecycle.
* eSIM Asset.
* Customer delivery.
* Product selling price.

Published events:

* `SupplierRegistered`
* `SupplierActivated`
* `SupplierPlanImported`
* `SupplierPlanMappingCreated`
* `SupplierContractProfileChanged`

---

### 3.5. Pricing Context

Identifier:

```text
PRI
```

Responsibilities:

* Price Book.
* Price Entry.
* Market-specific pricing.
* Currency-specific pricing.
* Effective periods.
* Pricing Quote.
* Supplier-cost snapshot.
* Selling-price snapshot.
* Internal FX reference for reporting.

Aggregate roots:

* `PriceBook`
* `PriceEntry`
* `PricingQuote`

Supported currencies:

* VND.
* LAK.
* USD.

Selling prices are independently approved per currency.

Real-time FX rates do not directly determine checkout prices.

Does not own:

* Product definition.
* Agency commission.
* Checkout Session.
* Sales Order.

Published events:

* `PriceBookCreated`
* `PriceEntryPublished`
* `PriceEntryExpired`
* `PricingQuoteIssued`
* `PricingQuoteExpired`

---

### 3.6. Agency Commerce Context

Identifier:

```text
AOF
```

Responsibilities:

* Agency Product entitlement.
* Agency Offer.
* Agency Offer Version.
* Commission rule assigned to an offer.
* Reference Link.
* Reference QR.
* Signed Reference Token.
* Reference expiry.
* Reference revocation.
* Attribution resolution.

Aggregate roots:

* `AgencyOffer`
* `AgencyOfferVersion`
* `ReferenceArtifact`

Value objects:

* `CommissionRule`
* `SignedReferenceToken`
* `AttributionContext`

Agency Offer Version is immutable after publication.

Reference parameters cannot override:

* Agency.
* Product Offer.
* Price.
* Currency.
* Payment provider.
* Commission rule.

Does not own:

* Agency organization lifecycle.
* Payment.
* Sales Order.
* Commission ledger.

Published events:

* `AgencyOfferCreated`
* `AgencyOfferVersionPublished`
* `ReferenceArtifactIssued`
* `ReferenceArtifactRevoked`
* `ReferenceArtifactExpired`

---

### 3.7. Checkout Context

Identifier:

```text
CHK
```

Responsibilities:

* Guest Checkout Session.
* Checkout validation.
* Customer contact capture.
* Market, locale and currency context.
* Invoice-information capture.
* Pricing Quote validation.
* Agency attribution validation.
* Checkout expiry.
* Conversion into a Sales Order request.

Aggregate root:

* `CheckoutSession`

Checkout stores temporary customer and transaction information.

The final immutable customer and commercial snapshots are owned by the Order Context.

Does not own:

* Payment lifecycle.
* Fulfillment.
* Commission ledger.
* Customer authentication.

Published events:

* `CheckoutSessionCreated`
* `CheckoutSessionValidated`
* `CheckoutSessionExpired`
* `CheckoutConfirmed`

---

### 3.8. Order Context

Identifier:

```text
ORD
```

Responsibilities:

* Sales Order.
* Order Item.
* Order commercial snapshots.
* Customer snapshot.
* Product snapshot.
* Price snapshot.
* Market and locale snapshot.
* Agency attribution snapshot.
* Supplier-mapping snapshot.
* Derived overall order status.

Aggregate root:

* `SalesOrder`

Entities:

* `OrderItem`

Initial status:

```text
PENDING_PAYMENT
```

Order does not directly execute payment or procurement.

Overall order status is derived from published Payment, Procurement, Fulfillment, Delivery and Refund states.

Published events:

* `SalesOrderCreated`
* `SalesOrderCancelled`
* `OrderCommercialSnapshotStored`
* `OrderStatusProjectionChanged`

---

### 3.9. Payment Context

Identifier:

```text
PAY
```

Responsibilities:

* Payment Intent.
* Payment Attempt.
* Provider transaction.
* Webhook inbox.
* Signature verification.
* Payment expiration.
* Payment retry.
* Payment reconciliation.
* Full refund.
* Provider adapter invocation.

Aggregate roots:

* `PaymentIntent`
* `Refund`

Entities:

* `PaymentAttempt`
* `ProviderTransaction`
* `PaymentWebhookEvent`
* `PaymentReconciliationCase`

Providers:

* GPay.
* OnePay.
* uMoney in R1.1.

Payment success must be determined by trusted server-side evidence.

Browser redirect alone cannot confirm payment.

Published events:

* `PaymentIntentCreated`
* `PaymentAttemptStarted`
* `PaymentSucceeded`
* `PaymentFailed`
* `PaymentExpired`
* `PaymentReconciliationRequired`
* `RefundRequested`
* `RefundCompleted`
* `RefundFailed`

---

### 3.10. Procurement Context

Identifier:

```text
PRO
```

Responsibilities:

* Procurement validation.
* Supplier-order request.
* Supplier request correlation.
* Supplier Order lifecycle.
* Supplier retry.
* Supplier polling.
* Supplier webhook interpretation.
* Procurement recovery.

Aggregate roots:

* `ProcurementRequest`
* `SupplierOrder`

Procurement invokes Supplier Gateway contracts published by Supplier Management.

Procurement must prevent duplicate supplier purchases for the same fulfillment requirement.

Does not own:

* eSIM Asset.
* Customer delivery.
* Supplier credential plaintext.
* Payment status.

Published events:

* `ProcurementRequested`
* `SupplierOrderSubmitted`
* `SupplierOrderProcessing`
* `ProcurementSucceeded`
* `ProcurementFailed`
* `ProcurementRecoveryRequired`

---

### 3.11. Fulfillment Context

Identifier:

```text
FUL
```

Responsibilities:

* Fulfillment lifecycle.
* eSIM Asset.
* ICCID.
* QR payload.
* Activation code.
* Secure eSIM storage.
* Asset assignment.
* Duplicate-assignment prevention.
* Manual eSIM replacement.
* Fulfillment recovery status.

Aggregate roots:

* `Fulfillment`
* `EsimAsset`

Sensitive values must be encrypted or stored through a secure storage abstraction.

Does not own:

* Supplier-order communication.
* Payment.
* Email delivery.
* Commission.

Published events:

* `FulfillmentStarted`
* `EsimAssetCreated`
* `EsimAssetAssigned`
* `EsimAssetReplaced`
* `FulfillmentSucceeded`
* `FulfillmentFailed`

---

### 3.12. Delivery Context

Identifier:

```text
DEL
```

Responsibilities:

* Delivery request.
* Delivery attempt.
* Email delivery.
* Delivery retry.
* Resend.
* Delivery status.
* Localized transactional templates.
* Delivery failure recovery.

Aggregate root:

* `DeliveryRequest`

Entities:

* `DeliveryAttempt`

Delivery references an eSIM Asset but does not own its sensitive source data.

Published events:

* `DeliveryRequested`
* `DeliveryAttemptStarted`
* `DeliverySucceeded`
* `DeliveryFailed`
* `DeliveryRetryScheduled`

---

### 3.13. Commission Context

Identifier:

```text
COM
```

Responsibilities:

* Commission snapshot.
* Commission lifecycle.
* Commission ledger.
* Commission statement.
* Reversal.
* External-payment marking.
* Agency commission reporting.

Aggregate roots:

* `CommissionLedger`
* `CommissionStatement`

Commission states:

* `ATTRIBUTED`
* `ACCRUED`
* `ELIGIBLE`
* `REVERSED`
* `PAID`

Commission becomes eligible only after fulfillment succeeds.

Refund reverses the applicable commission.

Published events:

* `CommissionAttributed`
* `CommissionAccrued`
* `CommissionEligible`
* `CommissionReversed`
* `CommissionMarkedPaid`
* `CommissionStatementGenerated`

---

### 3.14. Customer Experience Context

Identifier:

```text
CXP
```

Responsibilities:

* Customer Portal use cases.
* Customer order-view projection.
* Secure QR presentation.
* Activation-code presentation.
* Installation-guide selection.
* Resend request.
* Customer support-request intake.

Aggregate root:

* `CustomerSupportRequest`

Read models:

* `CustomerOrderView`
* `CustomerEsimView`

Customer Experience does not own canonical Order, Payment or eSIM Asset data.

It consumes authorized projections from owning contexts.

Published events:

* `CustomerSupportRequested`
* `CustomerResendRequested`

---

### 3.15. Operations Context

Identifier:

```text
OPS
```

Responsibilities:

* Operations Case.
* Payment-exception queue.
* Supplier-timeout queue.
* Fulfillment-failure queue.
* Webhook-failure queue.
* Delivery-failure queue.
* Refund queue.
* Manual-resolution workflow.
* Cross-context transaction timeline.
* Operational search projections.

Aggregate root:

* `OperationsCase`

Operations does not directly mutate another domain's tables.

Manual actions are issued through the owning context's application commands.

Published events:

* `OperationsCaseOpened`
* `OperationsCaseAssigned`
* `ManualResolutionRequested`
* `OperationsCaseResolved`

---

### 3.16. Audit Context

Identifier:

```text
AUD
```

Responsibilities:

* Immutable Audit Event.
* Sensitive-data access audit.
* Administrative-action audit.
* Manual-replacement audit.
* Organization-context audit.
* Correlation timeline.
* Retention enforcement.

Aggregate root:

* `AuditEvent`

Audit records:

* Actor.
* Organization.
* Action.
* Subject.
* Timestamp.
* Correlation ID.
* Session or request context.
* Before and after metadata when applicable.

Audit events are append-only.

Business contexts must not update or delete Audit Events.

---

## 4. Dependency direction

Permitted high-level direction:

```text
IAM
  ↓
ORG
  ↓
CAT ──→ SUP
  ↓       ↓
PRI     PRO
  ↓       ↓
AOF     FUL
  ↓       ↓
CHK → ORD → PAY
          ↓
         PRO → FUL → DEL
          ↓     ↓
         COM   CXP
           \   /
            OPS
             ↓
            AUD
```

This diagram represents logical dependencies, not direct database calls.

Important corrections:

* Order does not invoke Payment directly.
* Payment does not invoke Procurement directly.
* Fulfillment does not invoke Delivery directly.
* Commission does not modify Order.
* Operations does not bypass owning contexts.

Application process managers coordinate the workflow.

---

## 5. Core process managers

### 5.1. Order Payment Process

Starts from:

* `SalesOrderCreated`

Coordinates:

* Payment Intent creation.
* Payment expiration.
* Order cancellation after payment expiry.

Consumes:

* `PaymentSucceeded`
* `PaymentFailed`
* `PaymentExpired`

### 5.2. Payment Fulfillment Process

Starts from:

* `PaymentSucceeded`

Coordinates:

* Procurement request.
* Fulfillment start.
* Delivery request.
* Commission progression.

Consumes:

* `ProcurementSucceeded`
* `ProcurementFailed`
* `FulfillmentSucceeded`
* `FulfillmentFailed`
* `DeliverySucceeded`
* `DeliveryFailed`

### 5.3. Refund Compensation Process

Starts from:

* `RefundRequested`

Coordinates:

* Provider refund.
* Order-state projection.
* Commission reversal.
* Operations exception creation.

Consumes:

* `RefundCompleted`
* `RefundFailed`

Process managers do not own business state already owned by a bounded context.

They only own orchestration progress and idempotency state.

---

## 6. Cross-context invariants

1. A Sales Order references exactly one accepted Pricing Quote snapshot.
2. Agency attribution cannot be changed after Sales Order creation.
3. A Payment Intent belongs to exactly one Sales Order.
4. Payment success is idempotent.
5. One fulfillment requirement cannot create more than one active supplier purchase.
6. An eSIM Asset cannot be assigned to more than one fulfilled Order Item unless explicitly supported by product policy.
7. Commission cannot become eligible before Fulfillment succeeds.
8. Refund completion triggers commission reversal.
9. Delivery failure does not reverse successful fulfillment.
10. Operations actions must use owning-context commands.
11. Sensitive eSIM access must produce an Audit Event.
12. Organization-scoped records must never be exposed across organization boundaries.

---

## 7. Physical implementation constraints

Release 1 may use one PostgreSQL database, but logical ownership remains strict.

Required rules:

* Each table has one owning context.
* Repository code remains inside its owning module.
* Cross-context repository imports are prohibited.
* Cross-context ORM navigation is prohibited.
* Context references use stable identifiers.
* Read-model projections may combine data from multiple contexts.
* Projection tables must be clearly marked as non-canonical.
* Business updates must go through owning application services.
* Provider adapters cannot write directly to domain tables.
* Secrets are resolved through environment-specific secret references.

Database-level foreign keys across contexts require an explicit architecture decision.

They must not create lifecycle ownership by accident.

---

## 8. Acceptance conditions

The Domain Context Map is accepted when:

1. Every Release 1 capability belongs to one owning context.
2. Aggregate ownership is unambiguous.
3. Payment, Procurement, Fulfillment and Delivery remain separate.
4. Agency Offer and Commission remain separate.
5. Operations cannot directly mutate foreign contexts.
6. Provider-specific code is isolated behind adapters.
7. Cross-context workflows use process managers and events.
8. Sensitive eSIM ownership and access rules are explicit.
9. Multi-organization boundaries are explicit.
10. No runtime or database implementation is included in R1A-02.
