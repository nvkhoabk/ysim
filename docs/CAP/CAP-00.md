---
document_code: CAP-00
document_name: Platform Capability Registry
project: YSim Platform v2.1
document_set: CAP (Capability Architecture)
version: 1.0
status: Draft
language: en
owner: YSim Architecture Team
last_updated: 2026-07-12
---

# CAP-00 — Platform Capability Registry

---

# 1. Purpose

This document defines the canonical Business Capability Registry of the YSim Platform.

The registry establishes a single source of truth for all platform capabilities used throughout:

- Business Requirements
- Architecture
- Domain Models
- APIs
- AI Factory
- Runtime
- Documentation
- Sprint Planning

A Capability represents **what the platform is able to do**, independent of implementation technology.

Capabilities are stable architectural concepts and should evolve much slower than services or applications.

---

# 2. Capability Philosophy

The YSim Platform is capability-driven.

Applications do not own business logic.

Applications consume Platform Capabilities.

```
Portal

Storefront

Embedded Commerce

Public APIs

↓

Business Capability

↓

Application Services

↓

Infrastructure
```

Capabilities remain independent from presentation.

---

# 3. Capability Definition

A Capability describes:

- Business Responsibility
- Business Ownership
- Business Rules
- Domain Boundaries
- Events
- APIs
- Permissions

A Capability never describes:

- UI
- Database Tables
- Frameworks
- Programming Languages
- External Suppliers

---

# 4. Capability Hierarchy

The platform organizes capabilities hierarchically.

```
Platform

↓

Business Domain

↓

Capability

↓

Application Service

↓

Infrastructure
```

Capabilities are implementation-independent.

---

# 5. Capability Classification

Capabilities are grouped into five categories.

## Foundation

Core platform capabilities.

Examples:

- Identity
- Organization
- Configuration
- Localization
- Branding

---

## Commerce

Commercial capabilities.

Examples:

- Catalog
- Product
- Pricing
- Promotion
- Checkout
- Order

---

## Fulfillment

Delivery capabilities.

Examples:

- Allocation
- Fulfillment
- Inventory
- Delivery

---

## Operations

Operational capabilities.

Examples:

- Monitoring
- Reporting
- Notification
- Scheduler

---

## Integration

External connectivity.

Examples:

- Supplier Gateway
- Payment Gateway
- Notification Gateway
- Webhooks

---

# 6. Canonical Capability Registry

The following capabilities are defined for YSim v2.1.

---

## Foundation

- Identity
- Access Control
- Organization
- User Management
- Branding
- Theme
- Localization
- Configuration
- Storefront
- Asset Management
- Domain Management
- Feature Flags

---

## Commerce

- Catalog
- Product
- Pricing
- Promotion
- Shopping Cart
- Checkout
- Order
- Customer
- Payment
- Refund
- Voucher

---

## Fulfillment

- Allocation
- Inventory
- Fulfillment
- Delivery
- Activation
- Replacement

---

## Finance

- Settlement
- Ledger
- Commission
- Billing
- Invoice
- Revenue

---

## Support

- Customer Care
- Knowledge Base
- Ticketing
- Feedback

---

## Platform Operations

- Reporting
- Analytics
- Monitoring
- Scheduler
- Audit
- Logging

---

## Integration

- Supplier Gateway
- Payment Gateway
- Notification Gateway
- Authentication Gateway
- External APIs

---

# 7. Capability Dependency

Capabilities may depend on other capabilities.

Example:

```
Checkout

↓

Pricing

↓

Catalog

↓

Product
```

Another example:

```
Order

↓

Allocation

↓

Fulfillment

↓

Delivery
```

Dependencies always point downward.

Circular dependencies are prohibited.

---

# 8. Capability Exposure

Capabilities are exposed through different channels.

Examples:

```
Portal

↓

Capability
```

```
Storefront

↓

Capability
```

```
Public API

↓

Capability
```

```
Background Jobs

↓

Capability
```

Capabilities remain channel independent.

---

# 9. Capability Ownership

Each capability has one business owner.

Example:

| Capability | Owner |
|------------|-------|
| Catalog | Commerce Domain |
| Pricing | Commerce Domain |
| Allocation | Fulfillment Domain |
| Settlement | Finance Domain |
| Branding | Foundation Domain |

Ownership prevents duplicated business logic.

---

# 10. Capability Lifecycle

Capabilities evolve independently.

Lifecycle:

```
Planned

↓

Draft

↓

Active

↓

Deprecated

↓

Retired
```

Deprecated capabilities remain backward compatible until retired.

---

# 11. Capability Contracts

Capabilities expose contracts.

Contracts include:

- APIs
- Events
- Commands
- Queries
- Permissions

Consumers communicate only through contracts.

---

# 12. Capability Boundaries

Capabilities never access each other's internal models.

Interaction occurs through:

- Commands
- Queries
- Events

Direct database access across capabilities is prohibited.

---

# 13. Experience Integration

Experience Runtime consumes capabilities.

Example:

```
Featured Products Widget

↓

Catalog Capability

↓

Pricing Capability

↓

Promotion Capability
```

Widgets never access infrastructure directly.

---

# 14. Commerce Runtime

Commerce Runtime consists of:

- Catalog
- Product
- Pricing
- Promotion
- Checkout
- Payment
- Customer
- Order

These capabilities define commercial behavior.

---

# 15. Allocation Capability

Allocation is a first-class capability.

Responsibilities:

- Inventory Reservation
- Supplier Routing
- Cost Optimization
- Fulfillment Selection
- Retry
- Replacement

Allocation is the only capability allowed to determine which supplier provides an eSIM.

---

# 16. Supplier Isolation

Supplier systems are not capabilities.

Supplier systems are infrastructure resources.

Correct architecture:

```
Capability

↓

Supplier Gateway

↓

Supplier
```

Storefronts never consume suppliers.

Commerce Runtime never exposes supplier objects.

---

# 17. Capability Matrix

| Capability | Portal | Storefront | API | Background |
|------------|--------|------------|-----|------------|
| Catalog | ✓ | ✓ | ✓ | - |
| Pricing | ✓ | ✓ | ✓ | - |
| Checkout | - | ✓ | ✓ | - |
| Allocation | ✓ | - | Internal | ✓ |
| Fulfillment | ✓ | - | Internal | ✓ |
| Settlement | ✓ | - | Internal | ✓ |
| Monitoring | ✓ | - | Internal | ✓ |

---

# 18. AI Implementation Rules

AI agents shall:

- Treat Capabilities as architectural boundaries.
- Never merge unrelated capabilities.
- Never expose infrastructure through capabilities.
- Never expose suppliers to storefronts.
- Always communicate through capability contracts.
- Keep business rules inside capabilities.
- Keep UI independent from capability implementation.

---

# 19. Architectural Principles

### CAP-001

Capabilities define business responsibilities.

---

### CAP-002

Capabilities are independent from implementation.

---

### CAP-003

Capabilities expose contracts.

---

### CAP-004

Capabilities own business rules.

---

### CAP-005

Capabilities never expose infrastructure.

---

### CAP-006

Suppliers are infrastructure resources.

---

### CAP-007

Allocation owns supplier selection.

---

### CAP-008

Storefronts consume capabilities only.

---

### CAP-009

Capabilities communicate through contracts.

---

### CAP-010

Business ownership is unique.

---

# 20. References

This document should be read together with:

- BRD — Business Requirements
- ABP — Architecture Blueprint
- YADF — YSim Architecture Definition Framework
- AFM — AI Factory Model
- UXF-00 ~ UXF-05
- DIP — Development & Implementation Principles