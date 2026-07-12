---
document_code: UXF-05
document_name: Experience Runtime & Commerce Runtime Integration
project: YSim Platform v2.1
document_set: UXF (User Experience Foundation)
version: 1.0
status: Draft
language: en
owner: YSim Architecture Team
last_updated: 2026-07-12
---

# UXF-05 — Experience Runtime & Commerce Runtime Integration

---

# 1. Purpose

This document defines how the Experience Runtime integrates with the Commerce Runtime.

Unlike traditional commerce systems where the frontend owns business behavior, the YSim Platform separates presentation, business capabilities and infrastructure.

The Experience Runtime is responsible for rendering customer experiences.

The Commerce Runtime is responsible for providing business capabilities.

The two runtimes collaborate through Business Bindings.

---

# 2. Core Architecture

The YSim Platform consists of three independent runtime layers.

```
Experience Runtime

↓

Commerce Runtime

↓

Infrastructure Runtime
```

Each runtime owns different responsibilities.

---

# 3. Experience Runtime

The Experience Runtime owns:

- Theme
- Branding
- Layout
- Navigation
- Sections
- Components
- Assets
- Localization
- UX Inheritance
- Runtime Rendering

The Experience Runtime never performs business decisions.

---

# 4. Commerce Runtime

The Commerce Runtime owns:

- Catalog
- Product
- Pricing
- Promotion
- Payment
- Checkout
- Order
- Customer
- Fulfillment Policy
- Allocation
- Settlement
- Reporting

The Commerce Runtime never renders UI.

---

# 5. Infrastructure Runtime

Infrastructure owns:

- Supplier Gateway
- Payment Gateway
- Notification Gateway
- Storage
- Queue
- Cache
- Search
- Monitoring

Infrastructure never communicates directly with Storefront UI.

---

# 6. Runtime Integration

```
Request

↓

Experience Runtime

↓

Business Binding

↓

Commerce Runtime

↓

Application Services

↓

Infrastructure Runtime

↓

Response

↓

Experience Runtime

↓

Rendering
```

---

# 7. Storefront Responsibilities

Storefronts own only:

- Experience
- Navigation
- Layout
- Presentation
- Business Bindings

Storefronts never own:

- Products
- Pricing
- Supplier
- Inventory
- Allocation
- Fulfillment

---

# 8. Business Binding

Business Bindings connect Experience with Commerce.

Example:

```
Featured Products

↓

Catalog

↓

Pricing Profile

↓

Promotion Profile

↓

Visibility Policy

↓

Commerce Runtime
```

The UI never queries business objects directly.

---

# 9. Storefront Profile

A Storefront Profile consists of:

```
Storefront

├── Experience Profile
├── Business Profile
├── Commercial Profile
├── Runtime Policies
├── Navigation
├── Assets
├── Localization
├── Published Snapshot
```

---

# 10. Section Business Binding

Every Section supports Business Binding.

Example:

```
Featured Products

├── Catalog Binding

├── Product Selection Rule

├── Pricing Profile

├── Promotion Profile

├── Sorting Policy

├── Visibility Policy

├── Localization Policy

├── Empty State Policy
```

Another example:

```
Destination Selector

↓

Country Catalog

↓

Availability Policy

↓

Rendering
```

Sections become reusable commercial building blocks.

---

# 11. Widget Binding

Widgets never access databases.

Widgets never call suppliers.

Widgets call Business Capabilities.

```
Widget

↓

Capability

↓

Application Service

↓

Commerce Runtime
```

---

# 12. Commerce Capability Graph

The Experience Runtime consumes platform capabilities.

```
Catalog

Pricing

Promotion

Checkout

Payment

Customer

Support

Order

Fulfillment

Allocation
```

Capabilities remain independent.

---

# 13. Allocation Principle

Allocation is an internal business capability.

Storefronts never know suppliers.

Correct architecture:

```
Storefront

↓

Order

↓

Allocation

↓

Supplier Gateway

↓

Supplier
```

Supplier systems are infrastructure resources.

---

# 14. Product Principle

Storefronts consume only YSim Products.

```
YSim Product

↓

Allocation Rule

↓

Supplier Mapping
```

Supplier mappings remain internal.

---

# 15. Supplier Isolation

Supplier objects are prohibited from appearing inside:

- Storefront
- Components
- Widgets
- Pages
- Catalog
- Checkout

Supplier references may only appear inside:

- Allocation
- Fulfillment
- Inventory
- Supplier Gateway

---

# 16. Runtime Resolution

Rendering requires two parallel pipelines.

```
Experience Runtime

↓

Theme

↓

Layout

↓

Sections

↓

Widgets

──────────────

Commerce Runtime

↓

Catalog

↓

Pricing

↓

Promotion

↓

Payment

↓

Checkout

↓

Support

──────────────

↓

Business Binding

↓

Rendered Experience
```

---

# 17. Runtime Snapshot

Runtime renders immutable snapshots.

```
Published Storefront Snapshot

↓

Experience Snapshot

+

Business Snapshot

↓

Rendering
```

Editable configuration never participates directly.

---

# 18. Business Binding Validation

Before publishing, validation verifies:

✓ Catalog

✓ Pricing

✓ Payment

✓ Checkout

✓ Support

✓ Localization

✓ Runtime Policies

✓ Navigation

✓ Theme

Only valid storefronts may be published.

---

# 19. Runtime Failure Fallback

If runtime cannot resolve a binding:

```
Runtime

↓

Storefront

↓

Organization

↓

Platform
```

Fallback applies independently.

Rendering should continue whenever possible.

---

# 20. Business Configuration Inheritance

Business Configuration supports inheritance.

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

Runtime
```

Inherited objects include:

- Catalog
- Payment
- Promotion
- Support
- Checkout
- Pricing
- Navigation
- Assets

---

# 21. Experience + Commerce Synchronization

Experience Runtime and Commerce Runtime remain synchronized through Business Bindings.

Neither runtime directly depends on the implementation details of the other.

---

# 22. Publish Lifecycle

```
Draft

↓

Validate

↓

Preview

↓

Publish

↓

Immutable Snapshot

↓

Runtime Rendering
```

---

# 23. AI Implementation Guidelines

AI agents shall:

Never hardcode business logic inside components.

Never query suppliers directly.

Never bind UI to infrastructure.

Always consume Business Capabilities.

Always separate:

- Experience
- Commerce
- Infrastructure

Always support inheritance.

Always support fallback.

Always render Published Snapshots.

---

# 24. Architectural Principles

### UXF-501

Experience Runtime owns presentation.

---

### UXF-502

Commerce Runtime owns business capabilities.

---

### UXF-503

Infrastructure Runtime owns integrations.

---

### UXF-504

Business Binding connects Experience with Commerce.

---

### UXF-505

Storefronts never know suppliers.

---

### UXF-506

Allocation is the only capability allowed to select suppliers.

---

### UXF-507

Business Configuration supports inheritance.

---

### UXF-508

Business Configuration supports fallback.

---

### UXF-509

Published snapshots are immutable.

---

### UXF-510

Experience Runtime and Commerce Runtime remain independent.

---

# 25. Future Extensions

The architecture supports future extensions without changing storefront implementations.

Examples include:

- Additional suppliers
- New payment gateways
- Dynamic pricing engines
- Recommendation engines
- AI-assisted personalization
- Headless commerce APIs
- Native mobile storefronts
- Partner embedded commerce
- Marketplace channels

These extensions are introduced by extending Business Capabilities and Runtime Configuration rather than modifying Storefront implementations.

---

# 26. References

This document should be read together with:

- UXF-00 — User Experience Foundation Overview
- UXF-01 — Experience Channels, Personas & Navigation
- UXF-02 — Design System, Theme & Experience Inheritance
- UXF-03 — Storefront Template & Page Composition
- UXF-04 — White-label, Localization & Runtime Context Resolution

- BRD
- ABP
- AFM
- YADF
- DIP