---
document_code: "UXF-01"
title: "Experience Channels, Personas & Navigation"
product_baseline: "2.3"
document_revision: "2.3.0-draft.1"
lifecycle_status: "V2.3_DRAFT"
language: "en"
source_baseline: "v2.2"
generated_registry_role: "UXF_CANONICAL_SOURCE"
last_remediated_on: "2026-07-15"
---
## v2.3 requirement authority

The `YSIM:REQUIREMENT` blocks in the normative appendix are authoritative for baseline 2.3. Legacy prose is retained as context; approved v2.3 decisions and the normative blocks take precedence where wording differs.

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

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## v2.3 normative requirement appendix



<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-01-R001 — Platform Administration Portal requires authentication

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "UXF-01-R001-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Platform Administration Portal requires authentication",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "UXF-01-R001-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "UXF-01-R001-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Platform Administration Portal requires authentication",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "UXF-01-R001-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "UXF-01-R001-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Platform Administration Portal requires authentication",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "UXF-01-R001-O001"
      ],
      "when": "the violating input or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R001-AC001",
        "UXF-01-R001-AC002",
        "UXF-01-R001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R001-O001",
      "obligation_text": "Platform Administration Portal requires authentication"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-01-R001 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-01-R001 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-01-R001 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "UXF-01-R001-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-01-R001-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-01-R001 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform Administration Portal requires authentication.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-01-001",
    "previous_temporary_key": "TMP-UXF-01-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "9d5842c07d69be8e915abcecf092016795fe67c7615570a7a26053106ff5d3c5",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "9d34d98ddf35836b52bd54de3d2ac7df39ccefbc20ccf155aaada155de29c39a",
    "source_lines": "L61-L86",
    "source_section": "3. Experience Channels > 3.1 Platform Administration Portal"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-01-R001",
  "title": "Platform Administration Portal requires authentication",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-01-R002 — Organization Portal requires authentication

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "UXF-01-R002-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Organization Portal requires authentication",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "UXF-01-R002-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "UXF-01-R002-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Organization Portal requires authentication",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "UXF-01-R002-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "UXF-01-R002-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Organization Portal requires authentication",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "UXF-01-R002-O001"
      ],
      "when": "the violating input or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R002-AC001",
        "UXF-01-R002-AC002",
        "UXF-01-R002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R002-O001",
      "obligation_text": "Organization Portal requires authentication"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-01-R002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-01-R002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-01-R002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "UXF-01-R002-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-01-R002-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-01-R002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization Portal requires authentication.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-01-002",
    "previous_temporary_key": "TMP-UXF-01-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "0927f384ab3df40429ba15d50e713774ceb0b5f9d491e23a9dd4ab7a4e4a4bc1",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "f727258a7997940764558dd3d309eb97e09944899102c4db111d2dbc3780d112",
    "source_lines": "L94-L114",
    "source_section": "3. Experience Channels > 3.2 Organization Portal"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-01-R002",
  "title": "Organization Portal requires authentication",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-01-R003 — Agency Portal requires authentication

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "UXF-01-R003-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Agency Portal requires authentication",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "UXF-01-R003-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "UXF-01-R003-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Agency Portal requires authentication",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "UXF-01-R003-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "UXF-01-R003-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Agency Portal requires authentication",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "UXF-01-R003-O001"
      ],
      "when": "the violating input or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R003-AC001",
        "UXF-01-R003-AC002",
        "UXF-01-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R003-O001",
      "obligation_text": "Agency Portal requires authentication"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-01-R003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-01-R003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-01-R003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "UXF-01-R003-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-01-R003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-01-R003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Agency Portal requires authentication.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-01-003",
    "previous_temporary_key": "TMP-UXF-01-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "93ac95ee690139a1b7d867e2ccb8e6322dc668bef501ea96cc1c3f6b76305205",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "93a42713fa4942158c15b0bcd527011c2feb4b732107fc4b1980e5dc94176078",
    "source_lines": "L118-L137",
    "source_section": "3. Experience Channels > 3.3 Agency Portal"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-01-R003",
  "title": "Agency Portal requires authentication",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-01-R004 — Authentication: Optional or Required depending on Storefront Policy

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "UXF-01-R004-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Authentication: Optional or Required depending on Storefront Policy",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "UXF-01-R004-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "UXF-01-R004-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Authentication: Optional or Required depending on Storefront Policy",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "UXF-01-R004-O001"
      ],
      "when": "the protected decision or action is attempted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R004-AC001",
        "UXF-01-R004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R004-O001",
      "obligation_text": "Authentication: Optional or Required depending on Storefront Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-01-R004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-01-R004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-01-R004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "UXF-01-R004 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-01-R004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-01-R004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Authentication: Optional or Required depending on Storefront Policy",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-01-004",
    "previous_temporary_key": "TMP-UXF-01-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3.1 Platform Administration Portal",
    "source_context_sha256": "1c30f1dd76364a5a3e6d97c156112d31cb579933a69530715fd1da97004e79cd",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "759041b1f4e3a832a612494420aa9ada99d9ef1bb02dd3f24dfd5246b9028b36",
    "source_lines": "L156-L158",
    "source_section": "3. Experience Channels > 3.4 Customer Portal"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-01-R004",
  "title": "Authentication: Optional or Required depending on Storefront Policy",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-01-R005 — Customers never interact with suppliers

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-01-R005-AC001",
      "given": "a user in the applicable channel and context for Customers never interact with suppliers",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-01-R005-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-01-R005-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Customers never interact with suppliers",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-01-R005-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R005-AC001",
        "UXF-01-R005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R005-O001",
      "obligation_text": "Customers never interact with suppliers"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customers never interact with suppliers.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007",
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-01-005",
    "previous_temporary_key": "TMP-UXF-01-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Customer Journey",
    "source_context_sha256": "a79168fde7f3285acb8e0c1353d939d7892aee2d7a6e68eb91bb54d62acd290d",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "978ce06e8542f5c88b7491dc0bde61cd3e15ef12fb3a1565d127ac6fb6a4845c",
    "source_lines": "L603",
    "source_section": "10. Customer Journey"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-01-R005",
  "title": "Customers never interact with suppliers",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-01-R006 — Every experience should support: - Keyboard navigation

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "ACCESSIBILITY_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-01-R006-AC001",
      "given": "the experience state and accessibility mode governed by Every experience should support: - Keyboard navigation",
      "observable_evidence": "before/after rendered state, enabled accessibility mode, available content and actions, interaction outcome, and any accessibility conformance result declared by the source",
      "then": "the accessible rendering or interaction is available without removing required content or actions, and its outcome remains perceivable and operable",
      "verifies": [
        "UXF-01-R006-O001"
      ],
      "when": "the named accessibility capability is enabled and the same content and actions are exercised"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "ACCESSIBILITY_CONFORMANCE_FAILURE_V1",
      "criterion_id": "UXF-01-R006-AC002",
      "given": "the experience with the accessibility capability named by Every experience should support: - Keyboard navigation unavailable or producing inaccessible content or actions",
      "observable_evidence": "enabled mode, rendered state, affected content or action, interaction result, and failed accessibility conformance evidence",
      "then": "accessibility conformance fails with the unavailable capability or inaccessible element identified; the state is not reported as conforming",
      "verifies": [
        "UXF-01-R006-O001"
      ],
      "when": "the applicable accessibility mode or interaction is used"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R006-AC001",
        "UXF-01-R006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R006-O001",
      "obligation_text": "Every experience should support: - Keyboard navigation"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every experience should support: - Keyboard navigation",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-01-006",
    "previous_temporary_key": "TMP-UXF-01-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Accessibility",
    "source_context_sha256": "e687762204c9a487689b5b4220ca1696e9bc24ca97ea67b5ebdd0281c6f8c59b",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "29a32929825e070638487aa28d29a259e7c7350f60e5760b62c3789233d91597",
    "source_lines": "L624-L626",
    "source_section": "12. Accessibility"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "ACCESSIBILITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-01-R006",
  "title": "Every experience should support: - Keyboard navigation",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-01-R007 — Every experience should support: - Screen readers

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "ACCESSIBILITY_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-01-R007-AC001",
      "given": "the experience state and accessibility mode governed by Every experience should support: - Screen readers",
      "observable_evidence": "before/after rendered state, enabled accessibility mode, available content and actions, interaction outcome, and any accessibility conformance result declared by the source",
      "then": "the accessible rendering or interaction is available without removing required content or actions, and its outcome remains perceivable and operable",
      "verifies": [
        "UXF-01-R007-O001"
      ],
      "when": "the named accessibility capability is enabled and the same content and actions are exercised"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "ACCESSIBILITY_CONFORMANCE_FAILURE_V1",
      "criterion_id": "UXF-01-R007-AC002",
      "given": "the experience with the accessibility capability named by Every experience should support: - Screen readers unavailable or producing inaccessible content or actions",
      "observable_evidence": "enabled mode, rendered state, affected content or action, interaction result, and failed accessibility conformance evidence",
      "then": "accessibility conformance fails with the unavailable capability or inaccessible element identified; the state is not reported as conforming",
      "verifies": [
        "UXF-01-R007-O001"
      ],
      "when": "the applicable accessibility mode or interaction is used"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R007-AC001",
        "UXF-01-R007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R007-O001",
      "obligation_text": "Every experience should support: - Screen readers"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every experience should support: - Screen readers",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-01-007",
    "previous_temporary_key": "TMP-UXF-01-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Accessibility",
    "source_context_sha256": "e687762204c9a487689b5b4220ca1696e9bc24ca97ea67b5ebdd0281c6f8c59b",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "7eaa7a46ea96b284aea6ac8b1db7659d3c805eca1363dddc9c468bb5fe16d796",
    "source_lines": "L624-L627",
    "source_section": "12. Accessibility"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "ACCESSIBILITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-01-R007",
  "title": "Every experience should support: - Screen readers",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-01-R008 — Every experience should support: - Responsive layouts

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-01-R008-AC001",
      "given": "a user in the applicable channel and context for Every experience should support: - Responsive layouts",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-01-R008-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-01-R008-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every experience should support: - Responsive layouts",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-01-R008-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R008-AC001",
        "UXF-01-R008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R008-O001",
      "obligation_text": "Every experience should support: - Responsive layouts"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every experience should support: - Responsive layouts",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-01-008",
    "previous_temporary_key": "TMP-UXF-01-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Accessibility",
    "source_context_sha256": "e687762204c9a487689b5b4220ca1696e9bc24ca97ea67b5ebdd0281c6f8c59b",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "fdde4eb101be5365c450cb3dcb0362513eed3ebeb178989cc837a6a599e87a14",
    "source_lines": "L624-L628",
    "source_section": "12. Accessibility"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-01-R008",
  "title": "Every experience should support: - Responsive layouts",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-01-R009 — Every experience should support: - High contrast themes

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "ACCESSIBILITY_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-01-R009-AC001",
      "given": "the experience state and accessibility mode governed by Every experience should support: - High contrast themes",
      "observable_evidence": "before/after rendered state, enabled accessibility mode, available content and actions, interaction outcome, and any accessibility conformance result declared by the source",
      "then": "the accessible rendering or interaction is available without removing required content or actions, and its outcome remains perceivable and operable",
      "verifies": [
        "UXF-01-R009-O001"
      ],
      "when": "the named accessibility capability is enabled and the same content and actions are exercised"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "ACCESSIBILITY_CONFORMANCE_FAILURE_V1",
      "criterion_id": "UXF-01-R009-AC002",
      "given": "the experience with the accessibility capability named by Every experience should support: - High contrast themes unavailable or producing inaccessible content or actions",
      "observable_evidence": "enabled mode, rendered state, affected content or action, interaction result, and failed accessibility conformance evidence",
      "then": "accessibility conformance fails with the unavailable capability or inaccessible element identified; the state is not reported as conforming",
      "verifies": [
        "UXF-01-R009-O001"
      ],
      "when": "the applicable accessibility mode or interaction is used"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R009-AC001",
        "UXF-01-R009-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R009-O001",
      "obligation_text": "Every experience should support: - High contrast themes"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-029",
      "selected_disposition": "CONFIRM_HIGH"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every experience should support: - High contrast themes",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-01-009",
    "previous_temporary_key": "TMP-UXF-01-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Accessibility",
    "source_context_sha256": "e687762204c9a487689b5b4220ca1696e9bc24ca97ea67b5ebdd0281c6f8c59b",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "1aae44d5e8bd609d4707aa2911a0851dabe6d9d9212dfc7c03a94ce788dcb733",
    "source_lines": "L624-L629",
    "source_section": "12. Accessibility"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "ACCESSIBILITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-01-R009",
  "title": "Every experience should support: - High contrast themes",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-01-R010 — Every experience should support: - Touch interaction

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-01-R010-AC001",
      "given": "a user in the applicable channel and context for Every experience should support: - Touch interaction",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-01-R010-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-01-R010-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every experience should support: - Touch interaction",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-01-R010-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R010-AC001",
        "UXF-01-R010-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R010-O001",
      "obligation_text": "Every experience should support: - Touch interaction"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every experience should support: - Touch interaction",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-01-010",
    "previous_temporary_key": "TMP-UXF-01-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Accessibility",
    "source_context_sha256": "e687762204c9a487689b5b4220ca1696e9bc24ca97ea67b5ebdd0281c6f8c59b",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "562c8f28846f7997da0efe8e54d1af52d5a363a631d40964df0371d8e30c27b3",
    "source_lines": "L624-L630",
    "source_section": "12. Accessibility"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-01-R010",
  "title": "Every experience should support: - Touch interaction",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-01-R011 — Every experience should support: - Mobile-first behavior

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-01-R011-AC001",
      "given": "a user in the applicable channel and context for Every experience should support: - Mobile-first behavior",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-01-R011-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-01-R011-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every experience should support: - Mobile-first behavior",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-01-R011-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R011-AC001",
        "UXF-01-R011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R011-O001",
      "obligation_text": "Every experience should support: - Mobile-first behavior"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every experience should support: - Mobile-first behavior",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-01-011",
    "previous_temporary_key": "TMP-UXF-01-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Accessibility",
    "source_context_sha256": "e687762204c9a487689b5b4220ca1696e9bc24ca97ea67b5ebdd0281c6f8c59b",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "ff160db085b669d322b5ec49e5dadc8a688519b38bec4ceee6699d8065b6fc1d",
    "source_lines": "L624-L631",
    "source_section": "12. Accessibility"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-01-R011",
  "title": "Every experience should support: - Mobile-first behavior",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-101 — Experience is channel-specific

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-101-AC001",
      "given": "a user in the applicable channel and context for Experience is channel-specific",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-101-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-101-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Experience is channel-specific",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-101-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-101-AC001",
        "UXF-101-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-101-O001",
      "obligation_text": "Experience is channel-specific"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Experience is channel-specific.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-101",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-101",
    "source_context_sha256": "365d9f730d101074ec68f4d7bc1a1e20d4938059aa7b2d98beea17cea9ba2941",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "4020c435e933abd0323109a1bcd572708bca5a4f48a15f05a7a2e302ee1fdfec",
    "source_lines": "L679-L682",
    "source_section": "15. Experience Principles > UXF-101"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-101",
  "title": "Experience is channel-specific",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-102 — Navigation is capability-driven

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-102-AC001",
      "given": "a user in the applicable channel and context for Navigation is capability-driven",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-102-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-102-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Navigation is capability-driven",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-102-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-102-AC001",
        "UXF-102-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-102-O001",
      "obligation_text": "Navigation is capability-driven"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Navigation is capability-driven.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-102",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "Principle 2",
    "source_context_sha256": "c3247bcf792fc60b276d2c31c1d39db326510fd140d048c01143acde6e954bba",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "d8e0507dc7a95e2c6833bb1688bb560fd14ce1145e004451e07f4f7938b43af9",
    "source_lines": "L685-L688",
    "source_section": "15. Experience Principles > UXF-102"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-102",
  "title": "Navigation is capability-driven",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-103 — Menus are resolved dynamically

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-103-AC001",
      "given": "a user in the applicable channel and context for Menus are resolved dynamically",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-103-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-103-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Menus are resolved dynamically",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-103-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-103-AC001",
        "UXF-103-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-103-O001",
      "obligation_text": "Menus are resolved dynamically"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Menus are resolved dynamically.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-103",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-103",
    "source_context_sha256": "33f4d0583cfa9091a957a7b2f69f01048ad5faf9160b6e36651eae4a432029c2",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "edf75fb6f01bf5d8af47e7d6f02dacd3b2822a467bc7129ee25765602dac8aa4",
    "source_lines": "L691-L694",
    "source_section": "15. Experience Principles > UXF-103"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-103",
  "title": "Menus are resolved dynamically",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-104 — Experience inherits from parent configurations

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-104-AC001",
      "given": "a user in the applicable channel and context for Experience inherits from parent configurations",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "a missing child value resolves to the parent configuration, an explicit child override wins only at its declared scope, and the rendered result identifies the effective source",
      "verifies": [
        "UXF-104-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_INHERITANCE_FAILURE_V1",
      "criterion_id": "UXF-104-AC002",
      "given": "a child experience with no local value and an invalid or unavailable parent configuration for Experience inherits from parent configurations",
      "observable_evidence": "child and parent configuration identities, resolution trace, fallback or failure result, and rendered value",
      "then": "resolution produces the declared deterministic fallback or a visible configuration failure and never renders an unexplained value",
      "verifies": [
        "UXF-104-O001"
      ],
      "when": "the inherited value is resolved"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-104-AC001",
        "UXF-104-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-104-O001",
      "obligation_text": "Experience inherits from parent configurations"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Experience inherits from parent configurations.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-104",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-104",
    "source_context_sha256": "6f819330b9b2ef9b41955ab91c83b675835bb661d042f74bd417add1aead22e2",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "f53484556f8b8ad565d0f4cff7aed1b63c39ce9ea39757a2d22e2ea3520049b0",
    "source_lines": "L697-L700",
    "source_section": "15. Experience Principles > UXF-104"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-104",
  "title": "Experience inherits from parent configurations",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-105 — Customers never interact directly with suppliers

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-105-AC001",
      "given": "a user in the applicable channel and context for Customers never interact directly with suppliers",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-105-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-105-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Customers never interact directly with suppliers",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-105-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-105-AC001",
        "UXF-105-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-105-O001",
      "obligation_text": "Customers never interact directly with suppliers"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customers never interact directly with suppliers.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007",
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-105",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-105",
    "source_context_sha256": "2175b630cfe9d824be35203f423981afa216047c994c162a7c37c38e8f519530",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "7934f23e211e158fa65da99bae75c49374f07063f8e5445467f11e2fe746a11a",
    "source_lines": "L703-L706",
    "source_section": "15. Experience Principles > UXF-105"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-105",
  "title": "Customers never interact directly with suppliers",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-106 — Internal supplier-selection and allocation mechanics remain invisible in customer journeys; appr…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "UXF-106-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Internal supplier-selection and allocation mechanics remain invisible in customer journeys; appr…",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "UXF-106-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "UXF-106-AC002",
      "given": "a v2.3 capability, configuration, or design change governed by Internal supplier-selection and allocation mechanics remain invisible in customer journeys; appr…",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "UXF-106-O002"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "UXF-106-AC003",
      "given": "a proposed change with missing traceability or a boundary violation under Internal supplier-selection and allocation mechanics remain invisible in customer journeys; appr…",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "UXF-106-O001",
        "UXF-106-O002"
      ],
      "when": "design conformance is reviewed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-106-AC001",
        "UXF-106-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-106-O001",
      "obligation_text": "Internal supplier-selection and allocation mechanics remain invisible in customer journeys"
    },
    {
      "acceptance_criterion_references": [
        "UXF-106-AC002",
        "UXF-106-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-106-O002",
      "obligation_text": "approved provider, network, or brand disclosure is read-only and must not influence allocation"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-037",
      "selected_disposition": "ROUTE_TO_REMEDIATION"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Internal supplier-selection and allocation mechanics remain invisible in customer journeys; approved provider, network, or brand disclosure is read-only and must not influence allocation.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007",
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-106",
    "previous_temporary_key": null,
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-106",
    "source_context_sha256": "f0a770d94fc783c30180cd85445f7774897530899a5a35fa4cfe02ea2d19227b",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "0b0c49eb1de8f10b40fa45b91d42a3e70b1549d2aaa86450010f662e933ca978",
    "source_lines": "L709-L712",
    "source_section": "15. Experience Principles > UXF-106"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-106",
  "title": "Internal supplier-selection and allocation mechanics remain invisible in customer journeys; appr…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-107 — Every channel shares the same design system

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-107-AC001",
      "given": "a user in the applicable channel and context for Every channel shares the same design system",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-107-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-107-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every channel shares the same design system",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-107-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-107-AC001",
        "UXF-107-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-107-O001",
      "obligation_text": "Every channel shares the same design system"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every channel shares the same design system.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-107",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-107",
    "source_context_sha256": "39422afece56d7a0623cc7b54adb691c06ea551fa4f479ef2d3f789c13d740f0",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "d58dc3e7297dd75da84121935227229422e38db7cf9c839130dbdc06ae524c3d",
    "source_lines": "L715-L718",
    "source_section": "15. Experience Principles > UXF-107"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-107",
  "title": "Every channel shares the same design system",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-108 — Every navigation tree supports localization

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-108-AC001",
      "given": "a user in the applicable channel and context for Every navigation tree supports localization",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-108-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-108-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every navigation tree supports localization",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-108-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-108-AC001",
        "UXF-108-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-108-O001",
      "obligation_text": "Every navigation tree supports localization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every navigation tree supports localization.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-108",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-108",
    "source_context_sha256": "d8b94ab279cdb87116ab29e3375204b1ca2fb8b3356c2b2373959b6849223813",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "51fbce77cbecd33bc6a3f46f3e2647377aaccc356fef061fc0a8abae9f22abed",
    "source_lines": "L721-L724",
    "source_section": "15. Experience Principles > UXF-108"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-108",
  "title": "Every navigation tree supports localization",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-109 — Experience must remain consistent across Portal, Storefront and APIs

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "UXF-109-AC001",
      "given": "a contract interaction at the integration boundary defined by Experience must remain consistent across Portal, Storefront and APIs",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "UXF-109-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "UXF-109-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Experience must remain consistent across Portal, Storefront and APIs",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "UXF-109-O001"
      ],
      "when": "the interaction reaches the integration boundary"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-109-AC001",
        "UXF-109-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-109-O001",
      "obligation_text": "Experience must remain consistent across Portal, Storefront and APIs"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Experience must remain consistent across Portal, Storefront and APIs.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-109",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-109",
    "source_context_sha256": "34b16f7b7da92b4154f7bb4b2b7c93a94df47c83a18c1010a460e1cb02f7eab1",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
    "source_lines": "L727-L730",
    "source_section": "15. Experience Principles > UXF-109"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-109",
  "title": "Experience must remain consistent across Portal, Storefront and APIs",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-110 — Business capabilities remain independent from presentation contracts

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "UXF-110-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Business capabilities remain independent from presentation contracts",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "UXF-110-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-110-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-110-O001",
      "obligation_text": "Business capabilities remain independent from presentation contracts"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-038",
      "selected_disposition": "ROUTE_TO_REMEDIATION"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business capabilities remain independent from presentation contracts.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-110",
    "previous_temporary_key": null,
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-110",
    "source_context_sha256": "ea590f86dec88b79ce2336dbf53ed354faf5c3133298e9d7330754a0329f8aa3",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "ab52d4bb348a16d18728d2072b56b6af8bd56ed2a98aabe5e1987834f23bc863",
    "source_lines": "L733-L736",
    "source_section": "15. Experience Principles > UXF-110"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-110",
  "title": "Business capabilities remain independent from presentation contracts",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
