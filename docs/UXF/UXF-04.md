---
document_code: UXF-04
document_name: White-label, Localization & Runtime Context Resolution
project: YSim Platform v2.1
document_set: UXF (User Experience Foundation)
version: 1.0
status: Draft
language: en
owner: YSim Architecture Team
last_updated: 2026-07-12
---

# UXF-04 — White-label, Localization & Runtime Context Resolution

---

# 1. Purpose

This document defines the runtime resolution engine responsible for generating every customer experience within the YSim Platform.

Rather than rendering static websites, YSim dynamically resolves runtime contexts and composes the final commercial experience.

The Runtime Resolution Engine determines:

- Branding
- Storefront
- Theme
- Navigation
- Localization
- Catalog
- Pricing
- Payment
- Checkout
- Support
- Content
- Runtime Policies

before rendering any user interface.

---

# 2. Runtime Resolution Philosophy

The YSim Platform never renders pages directly.

Instead, every request is resolved through a sequence of independent context providers.

```
Incoming Request

↓

Context Resolution

↓

Experience Resolution

↓

Business Resolution

↓

Commercial Resolution

↓

Rendered Experience
```

Every rendered storefront is therefore generated dynamically.

---

# 3. Runtime Context Providers

The Runtime Resolution Engine collects information from multiple providers.

```
Platform Context

↓

Organization Context

↓

Storefront Context

↓

Domain Context

↓

Campaign Context

↓

Tracking Context

↓

Localization Context

↓

Identity Context

↓

Device Context

↓

Feature Flag Context

↓

User Preference Context

↓

Runtime Experience
```

Each provider contributes part of the final experience.

---

# 4. Domain Resolution

The first runtime context is Domain.

Example:

```
ysim.vn

↓

Platform Storefront
```

```
travel.partner.com

↓

Partner Storefront
```

```
agency-a.ysim.vn

↓

Agency Storefront
```

Domains determine:

- Organization
- Default Storefront
- Branding
- Default Locale
- Default Currency

---

# 5. URL Resolution

URL paths further refine the experience.

Example:

```
/japan

↓

Destination

↓

Japan Catalog
```

```
/campaign/summer

↓

Campaign Storefront
```

URL Resolution never bypasses Storefront configuration.

---

# 6. Tracking Resolution

Tracking identifiers participate in runtime resolution.

Examples:

```
tracking-id

affiliate-id

agency-id

campaign-id

qr-id
```

Tracking may influence:

- Promotion
- Hero Banner
- Featured Products
- CTA
- Commission Attribution
- Analytics
- Support Contact

Tracking must never bypass business policies.

---

# 7. Organization Resolution

Organizations define business defaults.

Examples:

- Branding
- Themes
- Navigation
- Supported Locales
- Payment Profiles
- Storefront Templates

Organizations inherit Platform defaults.

---

# 8. Storefront Resolution

Storefronts define commercial experiences.

Each storefront references:

- Experience Profile
- Theme
- Template
- Business Bindings
- Localization
- Runtime Policies

Storefronts inherit Organization configuration.

---

# 9. Localization Resolution

Localization extends beyond language translation.

Localization may resolve:

- Language
- Currency
- Date Format
- Number Format
- Timezone
- Support Information
- FAQ
- Legal Content
- Email Templates
- SMS Templates
- Payment Methods
- Promotions

Localization produces a localized commercial experience.

---

# 10. Device Resolution

Supported device categories:

- Mobile
- Tablet
- Laptop
- Desktop
- Kiosk

Device context affects:

- Layout
- Navigation
- Hero
- Grid
- CTA Position

Business behavior remains identical.

---

# 11. Identity Resolution

Identity context includes:

- Anonymous Visitor
- Customer
- Agency User
- Organization User
- Platform User

Identity affects:

- Navigation
- Available Capabilities
- Checkout
- Customer Portal
- Personalization

Identity never changes published business rules.

---

# 12. Feature Flag Resolution

Feature Flags support progressive rollout.

Flags may enable:

- Components
- Sections
- Pages
- Promotions
- Checkout Variants
- Payment Methods

Feature Flags never replace authorization.

---

# 13. User Preference Resolution

Runtime preferences may include:

- Preferred Language
- Preferred Currency
- Theme Preference
- Accessibility Settings

User Preferences override only permitted properties.

---

# 14. Runtime Resolution Order

The platform resolves contexts in the following order.

```
Platform

↓

Organization

↓

Storefront

↓

Domain

↓

Campaign

↓

Tracking

↓

Localization

↓

Identity

↓

Device

↓

Feature Flags

↓

User Preference

↓

Runtime Overrides

↓

Final Experience
```

---

# 15. Experience Inheritance

Every context supports inheritance.

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

Only overridden properties are replaced.

---

# 16. Runtime Fallback

Missing configurations fall back automatically.

Example:

```
Tracking

↓

Campaign

↓

Storefront

↓

Organization

↓

Platform
```

Fallback applies independently to:

- Theme
- Assets
- Navigation
- Localization
- Support
- Payment
- Catalog
- Checkout

---

# 17. White-label Architecture

Every organization may own multiple storefronts.

Each storefront may configure:

- Domain
- Branding
- Theme
- Logo
- Assets
- Localization
- Navigation
- Catalog
- Payment Profile
- Checkout Flow
- Support Profile

White-label customization never requires code modification.

---

# 18. Multi-domain Support

One organization may expose multiple domains.

Example:

```
ysim.vn

travel.partner.com

agency-a.com

holiday-esim.jp
```

Each domain may resolve a different storefront.

---

# 19. Multi-storefront Support

One organization may own multiple storefronts.

Examples:

- Retail Storefront
- Agency Storefront
- Campaign Storefront
- Partner Storefront
- Embedded Commerce

Each storefront is independently configurable.

---

# 20. Runtime Policies

Policies may influence runtime rendering.

Examples:

- Guest Checkout
- Mandatory Login
- Country Restrictions
- Product Visibility
- Promotion Eligibility
- Payment Availability

Policies are evaluated before rendering.

---

# 21. Runtime Caching

Runtime Resolution may cache published snapshots.

Cache keys may include:

- Storefront
- Domain
- Locale
- Theme
- Device

Editable configurations are never cached directly.

---

# 22. Runtime Security

The Runtime Resolution Engine must:

- validate domain ownership
- validate organization ownership
- validate storefront publication status
- validate localization
- validate feature flags
- validate runtime policies

before rendering.

---

# 23. AI Implementation Guidelines

AI agents shall:

- Never hardcode domains.
- Never hardcode storefronts.
- Never hardcode localization.
- Never bypass Runtime Resolution.
- Never resolve suppliers directly.
- Always use inheritance.
- Always support fallback.
- Always resolve published configurations.
- Separate runtime resolution from rendering.

---

# 24. Architectural Principles

### UXF-401

Every request is resolved through Runtime Context Resolution.

---

### UXF-402

Domains determine storefront identity.

---

### UXF-403

Tracking participates in runtime experience generation.

---

### UXF-404

Localization defines commercial experience.

---

### UXF-405

Storefronts inherit Organization configuration.

---

### UXF-406

Organizations inherit Platform configuration.

---

### UXF-407

Every configuration supports fallback.

---

### UXF-408

White-label customization requires no source code changes.

---

### UXF-409

Only published configurations participate in runtime rendering.

---

### UXF-410

Supplier systems never participate in Experience Resolution.

---

# 25. References

This document should be read together with:

- UXF-00 — User Experience Foundation Overview
- UXF-01 — Experience Channels, Personas & Navigation
- UXF-02 — Design System, Theme & Experience Inheritance
- UXF-03 — Storefront Template & Page Composition
- UXF-05 — Storefront Runtime Architecture & Business Binding

- BRD
- ABP
- AFM
- YADF
- DIP