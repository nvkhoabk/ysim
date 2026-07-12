---
document_code: ECS-00
document_name: Experience Configuration Schema
project: YSim Platform v2.1
document_set: ECS (Experience Configuration Schema)
version: 1.0
status: Draft
language: en
owner: YSim Architecture Team
last_updated: 2026-07-12
---

# ECS-00 — Experience Configuration Schema

---

# 1. Purpose

This document defines the canonical configuration schema used by the YSim Experience Runtime.

The schema standardizes how runtime configurations are represented, validated, inherited, published and consumed across the platform.

All runtime configuration must conform to the ECS specification.

This document applies to:

- Experience Profiles
- Storefront Profiles
- Themes
- Templates
- Sections
- Widgets
- Business Bindings
- Runtime Policies
- Published Snapshots

---

# 2. Design Goals

The ECS model follows several principles.

- Human readable
- Machine readable
- Version controlled
- Inheritable
- Immutable after publishing
- AI friendly
- Schema validated
- Backward compatible

---

# 3. Configuration Hierarchy

Configuration follows a hierarchical model.

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

Runtime Override
```

Each layer overrides only necessary properties.

---

# 4. Configuration Object

Every ECS object shares the same metadata.

```yaml
id:
code:
name:
description:

schemaVersion:

status:

owner:

createdAt:

updatedAt:

inherits:

tags:

metadata:
```

---

# 5. Experience Profile

Experience Profile defines presentation behavior.

Example

```yaml
experienceProfile:

  id: EXP-DEFAULT

  theme: YSIM-GREEN

  navigation: NAV-DEFAULT

  layout: LAYOUT-TRAVEL

  assets: ASSET-DEFAULT

  localization: LOC-GLOBAL

  runtimePolicies:

    - POLICY-001

    - POLICY-002
```

---

# 6. Theme Configuration

```yaml
theme:

  preset: ysim-green

  colors:

    primary: "#2BA84A"

    secondary: "#6D6F72"

    success: "#00B050"

    warning: "#F5A623"

    danger: "#E53935"

  typography:

    heading: Inter

    body: Inter

  radius:

    default: 12

  spacing:

    scale: default

  icons:

    provider: heroicons
```

---

# 7. Storefront Profile

A Storefront Profile combines Experience and Commerce.

```yaml
storefront:

  storefrontId: STOREFRONT-JP

  experienceProfile: EXP-JAPAN

  businessProfile: BUS-JAPAN

  catalog: CAT-JAPAN

  pricingProfile: PRICE-JP

  paymentProfile: PAYMENT-JP

  checkoutFlow: CHECKOUT-DEFAULT

  supportProfile: SUPPORT-JP

  localization: JA-JP
```

---

# 8. Business Profile

Business Profile references platform capabilities.

```yaml
businessProfile:

  catalog:

    reference: CAT-JAPAN

  pricing:

    reference: PRICE-JAPAN

  promotion:

    reference: PROMO-SUMMER

  payment:

    reference: PAYMENT-JP

  checkout:

    reference: CHECKOUT-DEFAULT

  support:

    reference: SUPPORT-JP

  fulfillment:

    reference: FULFILLMENT-STANDARD
```

Business Profiles never reference suppliers.

---

# 9. Section Configuration

Each section is independently configurable.

```yaml
section:

  type: featured-products

  enabled: true

  order: 20

  layout:

    columns: 4

  businessBinding:

    catalog: CAT-JAPAN

    pricing: PRICE-JAPAN

    promotion: PROMO-JP

  rendering:

    card: PACKAGE-CARD

    style: default
```

---

# 10. Widget Configuration

Widgets are presentation components.

```yaml
widget:

  type: package-card

  component: PACKAGE_CARD

  datasource:

    capability: Catalog

  properties:

    showPrice: true

    showCoverage: true

    showPromotion: true
```

Widgets never access databases directly.

---

# 11. Business Binding

Business Binding connects UI with Platform Capabilities.

```yaml
businessBinding:

  capability: Catalog

  bindingType: reference

  referenceId: CAT-JAPAN

  fallback: inherit
```

Another example

```yaml
businessBinding:

  capability: Pricing

  referenceId: PRICE-JAPAN
```

---

# 12. Runtime Policy

Runtime Policies define dynamic behavior.

```yaml
runtimePolicy:

  guestCheckout: true

  requireOtp: false

  allowGuestPurchase: true

  enablePromotion: true

  enableRecommendations: false
```

---

# 13. Localization Profile

```yaml
localization:

  locale: ja-JP

  currency: JPY

  timezone: Asia/Tokyo

  paymentProfile: PAYMENT-JP

  supportProfile: SUPPORT-JP

  terms: TERMS-JP
```

---

# 14. Asset Profile

```yaml
assets:

  logo: LOGO-JAPAN

  favicon: ICON-JAPAN

  hero: HERO-JAPAN

  footer: FOOTER-JAPAN
```

---

# 15. Navigation Profile

```yaml
navigation:

  profile: NAV-DEFAULT

  items:

    - Home

    - Packages

    - Coverage

    - FAQ

    - Support
```

---

# 16. Inheritance

Objects inherit from parents.

```yaml
inherits:

  from: STORE-DEFAULT

  strategy: merge
```

Supported strategies:

- merge
- replace
- append
- remove

---

# 17. Merge Rules

Configuration merge follows deterministic rules.

| Type | Strategy |
|------|----------|
| Scalar | Replace |
| Object | Merge |
| List | Replace by default |
| Ordered List | Replace |
| Map | Merge |

Platform implementations must not invent merge rules.

---

# 18. Validation

Every configuration must pass validation.

Examples:

- Required fields
- Existing references
- Circular inheritance detection
- Invalid capability references
- Invalid localization
- Invalid payment profile

Invalid configurations cannot be published.

---

# 19. Published Snapshot

Published snapshots are immutable.

```yaml
snapshot:

  version: 5

  storefront: STOREFRONT-JP

  experienceProfile: EXP-JP

  businessProfile: BUS-JP

  checksum: SHA256

  publishedAt: 2026-07-12T08:00:00Z
```

Runtime always consumes snapshots.

---

# 20. Versioning

Every configuration is versioned.

```
Draft

↓

Revision

↓

Published

↓

Archived
```

Previous versions remain available for rollback.

---

# 21. AI Implementation Guidelines

AI agents shall:

- Never invent configuration fields.
- Always follow ECS schema.
- Keep Experience and Business configurations separate.
- Use references instead of embedding duplicated objects.
- Validate references before publishing.
- Support inheritance.
- Support fallback.
- Support immutable snapshots.

---

# 22. Architectural Principles

### ECS-001

Every runtime configuration follows ECS.

---

### ECS-002

Every object is versioned.

---

### ECS-003

Every object supports inheritance.

---

### ECS-004

Every object supports validation.

---

### ECS-005

Published configurations are immutable.

---

### ECS-006

Experience configuration is independent from business configuration.

---

### ECS-007

Business configuration references Capabilities.

---

### ECS-008

Business configuration never references Suppliers.

---

### ECS-009

Configuration merge is deterministic.

---

### ECS-010

Runtime consumes Published Snapshots only.

---

# 23. References

This document should be read together with:

- UXF-00 ~ UXF-05
- CAP-00
- BRD
- ABP
- AFM
- YADF
- DIP