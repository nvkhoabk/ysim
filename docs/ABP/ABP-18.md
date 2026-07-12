---
document_code: ABP-18
document_name: Runtime Resolution Architecture
project: YSim Platform v2.1
document_set: ABP (Architecture Blueprint)
version: 1.0
status: Draft
language: en
owner: YSim Architecture Team
last_updated: 2026-07-12
---

# ABP-18 — Runtime Resolution Architecture

---

# 1. Purpose

This document defines the Runtime Resolution Architecture of the YSim Platform.

The Runtime Resolution Architecture is responsible for transforming an incoming request into a fully resolved commercial experience by combining Experience Runtime, Business Runtime, Policy Runtime and Published Snapshots.

This document establishes the canonical runtime behavior used by all applications within the platform.

---

# 2. Objectives

The Runtime Resolution Architecture shall provide:

- Deterministic request resolution
- Experience composition
- Business capability resolution
- Policy evaluation
- Configuration inheritance
- Published snapshot consumption
- Runtime fallback
- Immutable rendering
- Runtime scalability

---

# 3. Architectural Philosophy

The Runtime Resolution Engine is an orchestration layer.

It does **not** own business logic.

It does **not** own business data.

It resolves references, composes runtime context and delegates business execution to Platform Capabilities.

```
Request

↓

Runtime Resolution

↓

Platform Capabilities

↓

Resolved Experience

↓

Rendering
```

---

# 4. Runtime Architecture

```
HTTP Request

↓

Runtime Context Resolver

↓

Experience Resolver

↓

Business Resolver

↓

Policy Resolver

↓

Snapshot Resolver

↓

Component Resolver

↓

Rendering Engine

↓

Response
```

Each resolver performs a single responsibility.

---

# 5. Runtime Context

The Runtime Context represents the complete execution context for a request.

The context may contain:

- Platform
- Organization
- Storefront
- Campaign
- Tracking
- Localization
- Identity
- Customer Segment
- Device
- Feature Flags
- Runtime Overrides

Runtime Context remains immutable during request processing.

---

# 6. Runtime Resolution Order

Runtime Resolution follows a fixed hierarchy.

```
Platform

↓

Organization

↓

Storefront

↓

Campaign

↓

Tracking

↓

User Preference

↓

Runtime Override
```

Higher levels provide defaults.

Lower levels override only explicitly configured properties.

---

# 7. Experience Runtime

The Experience Runtime resolves presentation concerns.

Responsibilities include:

- Theme
- Design Tokens
- Layout
- Navigation
- Assets
- Sections
- Components
- Localization
- Experience Profile

The Experience Runtime never evaluates business rules.

---

# 8. Business Runtime

The Business Runtime resolves platform capabilities.

Responsibilities include:

- Catalog
- Product
- Pricing
- Promotion
- Checkout
- Payment
- Customer
- Support
- Fulfillment Policy

Business Runtime delegates execution to Platform Capabilities.

---

# 9. Policy Runtime

The Policy Runtime evaluates configurable business decisions.

Responsibilities include:

- Visibility
- Pricing Eligibility
- Checkout
- Promotion
- Fraud
- Allocation
- Inventory
- Access Control

Policy Runtime never renders UI.

---

# 10. Snapshot Runtime

Only Published Snapshots participate in Runtime Resolution.

```
Draft Configuration

↓

Publish

↓

Immutable Snapshot

↓

Runtime Resolution
```

Draft configurations are never consumed directly.

---

# 11. Resolver Pipeline

```
Request

↓

Context Resolver

↓

Experience Resolver

↓

Business Resolver

↓

Policy Resolver

↓

Snapshot Resolver

↓

Asset Resolver

↓

Component Resolver

↓

Rendering
```

Resolvers execute in deterministic order.

---

# 12. Reference Resolution Principle

The Runtime Resolution Engine resolves **references**, not business logic.

Example:

```
Storefront

↓

Catalog Reference

↓

Catalog Capability

↓

Products
```

The Runtime Resolution Engine never performs:

- Product Selection
- Pricing Calculation
- Supplier Routing
- Allocation
- Settlement

These responsibilities belong to Platform Capabilities.

---

# 13. Merge Strategy

Configuration merge follows deterministic rules.

| Configuration Type | Merge Strategy |
|--------------------|----------------|
| Scalar | Replace |
| Object | Merge |
| Map | Merge |
| List | Replace |
| Ordered Collection | Replace |

No resolver may introduce custom merge behavior.

---

# 14. Runtime Cache

Published snapshots may be cached.

Typical cache key:

```
Storefront

+

Locale

+

Theme

+

Snapshot Version

+

Device
```

Cache invalidation occurs only after successful publication.

---

# 15. Runtime Fallback

If a configuration cannot be resolved, fallback is applied.

```
Runtime Override

↓

Campaign

↓

Storefront

↓

Organization

↓

Platform
```

Fallback is evaluated independently for each configuration object.

---

# 16. Error Handling

Resolution failures should degrade gracefully whenever possible.

Examples:

Missing Campaign

↓

Fallback to Storefront

Missing Theme

↓

Fallback to Organization Theme

Missing Asset

↓

Fallback to Platform Asset

Fatal runtime errors should occur only when no valid fallback exists.

---

# 17. Runtime Sequence

```
Browser

↓

Gateway

↓

Runtime Context

↓

Experience Runtime

↓

Business Runtime

↓

Policy Runtime

↓

Snapshot Runtime

↓

Rendering

↓

HTML / JSON Response
```

---

# 18. Runtime Characteristics

The Runtime Resolution Architecture shall be:

- Stateless
- Deterministic
- Idempotent
- Cache Friendly
- Snapshot Driven
- Extensible
- Multi-tenant
- Localization Aware

---

# 19. AI Implementation Guidelines

AI agents shall:

- Never bypass Runtime Resolution.
- Never consume Draft configurations.
- Never hardcode themes.
- Never hardcode storefront configuration.
- Never implement business logic inside Runtime Resolution.
- Always resolve references through Platform Capabilities.
- Always support inheritance.
- Always support fallback.
- Always consume Published Snapshots.

---

# 20. Architectural Principles

### ABP-1801

Runtime Resolution is deterministic.

---

### ABP-1802

Runtime Resolution consumes Published Snapshots only.

---

### ABP-1803

Runtime Resolution resolves references, not business logic.

---

### ABP-1804

Business execution belongs to Platform Capabilities.

---

### ABP-1805

Experience Runtime is independent from Business Runtime.

---

### ABP-1806

Policy Runtime evaluates configurable business decisions.

---

### ABP-1807

Configuration inheritance follows a fixed hierarchy.

---

### ABP-1808

Fallback is mandatory for runtime resilience.

---

### ABP-1809

Supplier systems never participate in Runtime Resolution.

---

### ABP-1810

Runtime Resolution must remain stateless and cache-friendly.

---

# 21. References

This document should be read together with:

- BRD — Business Requirements
- YADF — YSim Architecture Definition Framework
- AFM — AI Factory Model
- UXF-00 — User Experience Foundation Overview
- UXF-05 — Experience Runtime & Commerce Runtime Integration
- CAP-00 — Platform Capability Registry
- ECS-00 — Experience Configuration Schema
- PCS-00 — Platform Configuration Schema
- POL-00 — Platform Policy Framework
- DIP — Development & Implementation Principles
