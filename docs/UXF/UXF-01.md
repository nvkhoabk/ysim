---
document_code: UXF-01
document_name: Experience Channels, Personas & Navigation
project: YSim Platform v2.1
document_set: UXF (User Experience Foundation)
version: 1.0
status: Draft
language: en
owner: YSim Architecture Team
last_updated: 2026-07-12
---

# UXF-01 — Experience Channels, Personas & Navigation

---

# 1. Purpose

This document defines the primary user experience channels of the YSim Platform.

The objective is to standardize how different users interact with the platform while maintaining a unified architecture, consistent navigation model, and reusable design system.

This document does not define visual layouts. It defines the experience model used by all YSim applications.

---

# 2. Experience Philosophy

YSim is a multi-channel digital commerce platform.

Different users access different experiences, but all experiences are generated from the same platform capabilities.

```
                    YSim Platform

                           │

        ┌──────────────────┼──────────────────┐

        ▼                  ▼                  ▼

    Portal UI         Storefront UI      Public APIs

        │                  │                  │

        ▼                  ▼                  ▼

   Different Experiences sharing the same Business Capabilities
```

Every channel consumes the same platform services.

Only the presentation and permissions differ.

---

# 3. Experience Channels

The platform currently defines the following primary channels.

## 3.1 Platform Administration Portal

Primary users:

- Platform Administrator
- Platform Operator
- Finance
- Customer Care
- Product Manager
- Operations Team

Objectives:

- Platform administration
- Organization management
- Product management
- Pricing management
- Allocation management
- Supplier management
- Settlement
- Monitoring
- Reporting

Authentication:

Required

Theme:

Platform Default

---

## 3.2 Organization Portal

Primary users:

- Organization Administrator
- Brand Administrator

Objectives:

- Organization configuration
- Branding
- Theme selection
- Domain management
- Storefront management
- Users & Roles
- Payment configuration
- Business policies

Authentication:

Required

---

## 3.3 Agency Portal

Primary users:

- Agency
- Distributor
- Sales Team

Objectives:

- Order creation
- Customer assignment
- Sales reporting
- Commission
- Inventory visibility
- Customer support

Authentication:

Required

---

## 3.4 Customer Portal

Primary users:

- End Customer

Objectives:

- View purchased eSIMs
- Activation guide
- QR download
- Purchase history
- Support
- Profile management

Authentication:

Optional or Required depending on Storefront Policy

---

## 3.5 White-label Storefront

Primary users:

- Public Visitors
- Travelers
- Guests

Objectives:

- Browse products
- Purchase eSIM
- Complete payment
- Receive delivery
- View activation instructions

Authentication:

Guest by default

---

## 3.6 Campaign Landing

Primary users:

- Campaign Visitors
- Affiliate Customers
- QR Visitors

Objectives:

- Fast purchase
- Limited campaign products
- Promotion conversion

Authentication:

Guest

---

## 3.7 Embedded Commerce

Primary users:

External Partner Customers

Examples:

- Banking App
- Travel Website
- OTA
- Super App
- Mobile App

YSim provides commerce capabilities through APIs and SDKs.

---

# 4. Personas

YSim defines several personas.

## Platform Personas

- Platform Owner
- Platform Administrator
- Finance Officer
- Customer Support
- Product Manager
- Marketing Manager

---

## Organization Personas

- Organization Owner
- Organization Administrator
- Storefront Manager
- Brand Manager

---

## Commerce Personas

- Agency
- Distributor
- Sales Representative
- Affiliate

---

## Customer Personas

- Anonymous Visitor
- Returning Customer
- Registered Customer
- Business Customer

---

# 5. Experience Context

Every experience is generated from runtime context.

```
User

↓

Identity Context

↓

Organization Context

↓

Storefront Context

↓

Localization Context

↓

Tracking Context

↓

Experience Context

↓

Rendered UI
```

Navigation is therefore contextual rather than static.

---

# 6. Navigation Principles

Navigation follows several principles.

## Principle 1

Navigation is role-driven.

Different roles see different navigation trees.

---

## Principle 2

Navigation is capability-driven.

Menus expose business capabilities rather than technical modules.

Example:

Preferred:

```
Products

Orders

Pricing

Customers
```

Avoid:

```
Product Module

Pricing Service

Catalog Repository
```

---

## Principle 3

Navigation supports inheritance.

Organizations may extend or hide menus without modifying the platform.

---

## Principle 4

Navigation supports localization.

Labels, ordering and visibility may differ by locale.

---

# 7. Portal Navigation Model

Platform Portal

```
Dashboard

Organizations

Users

Products

Pricing

Orders

Allocation

Inventory

Payments

Finance

Reports

Monitoring

Settings
```

---

Organization Portal

```
Dashboard

Storefronts

Domains

Branding

Themes

Localization

Catalogs

Pricing

Promotions

Payments

Support

Users

Reports

Settings
```

---

Agency Portal

```
Dashboard

Orders

Customers

Products

Campaigns

Commissions

Reports

Support
```

---

Customer Portal

```
Home

My eSIM

Orders

Activation

Support

Profile
```

---

Storefront

```
Home

Destinations

Packages

Cart

Checkout

Support

FAQ
```

---

# 8. Navigation Inheritance

Navigation follows inheritance rules.

```
Platform Navigation

↓

Organization Navigation

↓

Storefront Navigation

↓

Campaign Navigation

↓

Runtime Navigation
```

Each level may:

- Add items
- Remove items
- Reorder items
- Override labels

without modifying source code.

---

# 9. Runtime Navigation Resolution

The final navigation is generated dynamically.

```
Default Navigation

↓

Role Policy

↓

Organization Policy

↓

Storefront Policy

↓

Localization

↓

Feature Flags

↓

Runtime Navigation
```

---

# 10. Customer Journey

Typical storefront journey.

```
Landing

↓

Destination

↓

Product

↓

Checkout

↓

Payment

↓

Allocation

↓

Delivery

↓

Activation

↓

Support
```

Allocation remains invisible to customers.

Customers never interact with suppliers.

---

# 11. Experience Consistency

All channels share:

- Design Tokens
- Theme Engine
- Component Library
- Typography
- Iconography
- Accessibility Standards

This guarantees a consistent platform experience.

---

# 12. Accessibility

Every experience should support:

- Keyboard navigation
- Screen readers
- Responsive layouts
- High contrast themes
- Touch interaction
- Mobile-first behavior

Accessibility is considered a platform capability.

---

# 13. Responsive Strategy

Supported layouts:

- Mobile
- Tablet
- Laptop
- Desktop
- Large Display

Layout adapts without changing business functionality.

---

# 14. Cross-channel Consistency

Business capabilities remain identical across channels.

Examples:

```
Product

↓

Portal

↓

Storefront

↓

API
```

All represent the same business capability through different user experiences.

---

# 15. Experience Principles

### UXF-101

Experience is channel-specific.

---

### UXF-102

Navigation is capability-driven.

---

### UXF-103

Menus are resolved dynamically.

---

### UXF-104

Experience inherits from parent configurations.

---

### UXF-105

Customers never interact directly with suppliers.

---

### UXF-106

Allocation remains invisible within customer journeys.

---

### UXF-107

Every channel shares the same design system.

---

### UXF-108

Every navigation tree supports localization.

---

### UXF-109

Experience must remain consistent across Portal, Storefront and APIs.

---

### UXF-110

Business capabilities are independent from presentation.

---

# 16. References

This document should be read together with:

- UXF-00 — User Experience Foundation Overview
- UXF-02 — Design System, Theme & Experience Inheritance
- UXF-03 — Storefront Template & Page Composition
- UXF-04 — White-label, Localization & Runtime Context Resolution
- UXF-05 — Storefront Runtime Architecture & Business Binding

- BRD
- ABP
- AFM
- YADF
- DIP