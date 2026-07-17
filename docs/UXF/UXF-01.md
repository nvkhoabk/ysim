---
document_code: "UXF-01"
document_id: "UXF-01"
title: "Experience Channels, Personas & Navigation"
version: "2.3.0-draft.3"
document_revision: "2.3.0-draft.3"
status: "V2.3_DRAFT"
lifecycle_status: "V2.3_DRAFT"
language: "en"
baseline: "2.3"
product_baseline: "2.3"
source_lineage: "v2.2 + approved Phase 1/2A/2B + accepted Acceptance Model C1 + accepted Mapping C3"
source_baseline: "v2.2"
last_reviewed_date: "2026-07-15"
last_remediated_on: "2026-07-17"
applicable_scope: "V2.3_ACTIVE_AND_RETAINED_SCOPE_RECORDS"
generated_registry_role: "UXF_CANONICAL_SOURCE"
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

## v2.3 normative requirement appendix — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-01-R001 — Platform Administration Portal requires authentication

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-01-R001",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "9d5842c07d69be8e915abcecf092016795fe67c7615570a7a26053106ff5d3c5"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R001 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R001 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R001 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-01-R001-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-01-R001-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R001 does not define a recovery obligation."
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
    "source_fingerprint": "9d5842c07d69be8e915abcecf092016795fe67c7615570a7a26053106ff5d3c5",
    "source_lines": "L771-L879",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-01-R001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-01-R002",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "0927f384ab3df40429ba15d50e713774ceb0b5f9d491e23a9dd4ab7a4e4a4bc1"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R002 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-01-R002-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-01-R002-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R002 does not define a recovery obligation."
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
    "source_fingerprint": "0927f384ab3df40429ba15d50e713774ceb0b5f9d491e23a9dd4ab7a4e4a4bc1",
    "source_lines": "L881-L989",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-01-R002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-01-R003",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "93ac95ee690139a1b7d867e2ccb8e6322dc668bef501ea96cc1c3f6b76305205"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R003 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-01-R003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-01-R003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R003 does not define a recovery obligation."
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
    "source_fingerprint": "93ac95ee690139a1b7d867e2ccb8e6322dc668bef501ea96cc1c3f6b76305205",
    "source_lines": "L991-L1099",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-01-R003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-01-R004",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "759041b1f4e3a832a612494420aa9ada99d9ef1bb02dd3f24dfd5246b9028b36"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R004-AC001",
        "UXF-01-R004-AC002",
        "UXF-01-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R004-O001",
      "obligation_text": "Authentication: Optional or Required depending on Storefront Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R004 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-01-R004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-01-R004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-01-R004 does not define a recovery obligation."
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
    "source_lines": "L1101-L1209",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-01-R004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007",
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-01-R005",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "978ce06e8542f5c88b7491dc0bde61cd3e15ef12fb3a1565d127ac6fb6a4845c"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R005-AC001",
        "UXF-01-R005-AC002",
        "UXF-01-R005-AC003"
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
    "source_lines": "L1211-L1292",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-01-R005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-01-R006",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "29a32929825e070638487aa28d29a259e7c7350f60e5760b62c3789233d91597"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R006-AC001",
        "UXF-01-R006-AC002",
        "UXF-01-R006-AC003"
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
    "source_lines": "L1294-L1369",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-01-R006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-01-R007",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "a55cdba50a7b87694513e11448649496ad895a9a0c0a44b0b6240e5998a110e6"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R007-AC001",
        "UXF-01-R007-AC002",
        "UXF-01-R007-AC003"
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
    "source_fingerprint": "a55cdba50a7b87694513e11448649496ad895a9a0c0a44b0b6240e5998a110e6",
    "source_lines": "L1371-L1446",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-01-R007"
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
### UXF-01-R008 — Every V2.3_ACTIVE experience channel must use responsive layouts that preserve usable navigation…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-01-R008",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "17cf17817605343e900e1e39c28fcde24d8414578762208d763dc95fa701f13b"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R008-AC001",
        "UXF-01-R008-AC003",
        "UXF-01-R008-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R008-O001",
      "obligation_text": "Every V2.3_ACTIVE experience channel must use responsive layouts that preserve usable navigation, actions, content, and critical workflows on supported browser, mobile, and WebView viewport ranges"
    },
    {
      "acceptance_criterion_references": [
        "UXF-01-R008-AC002",
        "UXF-01-R008-AC003",
        "UXF-01-R008-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R008-O002",
      "obligation_text": "Partner Portal remains outside active scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every V2.3_ACTIVE experience channel must use responsive layouts that preserve usable navigation, actions, content, and critical workflows on supported browser, mobile, and WebView viewport ranges; Partner Portal remains outside active scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-01-008",
    "phase_2c_c3_actions": [
      "C3_APPROVED_SEMANTIC_DIRECTIVE"
    ],
    "previous_temporary_key": "TMP-UXF-01-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Accessibility",
    "source_context_sha256": "e687762204c9a487689b5b4220ca1696e9bc24ca97ea67b5ebdd0281c6f8c59b",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "17cf17817605343e900e1e39c28fcde24d8414578762208d763dc95fa701f13b",
    "source_fingerprint_before_c3": "fdde4eb101be5365c450cb3dcb0362513eed3ebeb178989cc837a6a599e87a14",
    "source_lines": "L1448-L1543",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-01-R008"
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
  "title": "Every V2.3_ACTIVE experience channel must use responsive layouts that preserve usable navigation…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-01-R009 — Every experience should support: - High contrast themes

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-01-R009",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "873b70e52ef5b209ad51667f7adc9d3f0fd52c1b3bb353beea6de9a57548c9e6"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R009-AC001",
        "UXF-01-R009-AC002",
        "UXF-01-R009-AC003"
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
    "source_fingerprint": "873b70e52ef5b209ad51667f7adc9d3f0fd52c1b3bb353beea6de9a57548c9e6",
    "source_lines": "L1545-L1629",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-01-R009"
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
### UXF-01-R010 — Every V2.3_ACTIVE experience channel on supported browsers, mobile devices, and WebViews must pr…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-01-R010",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "80ed1b9407c3e793caf599e66b6a41b1a1f53fa417039c144896985c08b03bf9"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R010-AC001",
        "UXF-01-R010-AC004",
        "UXF-01-R010-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R010-O001",
      "obligation_text": "Every V2.3_ACTIVE experience channel on supported browsers, mobile devices, and WebViews must provide touch-usable navigation, actions, and critical workflows"
    },
    {
      "acceptance_criterion_references": [
        "UXF-01-R010-AC002",
        "UXF-01-R010-AC004",
        "UXF-01-R010-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R010-O002",
      "obligation_text": "no required interaction may depend on hover alone"
    },
    {
      "acceptance_criterion_references": [
        "UXF-01-R010-AC003",
        "UXF-01-R010-AC004",
        "UXF-01-R010-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R010-O003",
      "obligation_text": "Partner Portal is excluded until activated by an approved scope requirement"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every V2.3_ACTIVE experience channel on supported browsers, mobile devices, and WebViews must provide touch-usable navigation, actions, and critical workflows; no required interaction may depend on hover alone. Partner Portal is excluded until activated by an approved scope requirement.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-01-010",
    "phase_2c_c3_actions": [
      "C3_APPROVED_SEMANTIC_DIRECTIVE"
    ],
    "previous_temporary_key": "TMP-UXF-01-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Accessibility",
    "source_context_sha256": "e687762204c9a487689b5b4220ca1696e9bc24ca97ea67b5ebdd0281c6f8c59b",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "80ed1b9407c3e793caf599e66b6a41b1a1f53fa417039c144896985c08b03bf9",
    "source_fingerprint_before_c3": "562c8f28846f7997da0efe8e54d1af52d5a363a631d40964df0371d8e30c27b3",
    "source_lines": "L1631-L1736",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-01-R010"
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
  "title": "Every V2.3_ACTIVE experience channel on supported browsers, mobile devices, and WebViews must pr…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-01-R011 — Every V2.3_ACTIVE experience channel must provide mobile-first behavior on supported touch-capab…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-01-R011",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "25b194eda2617952c3ecdc381eaa3dafc81e7279ec2fcc45a22a20a8993cf040"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-01-R011-AC001",
        "UXF-01-R011-AC003",
        "UXF-01-R011-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R011-O001",
      "obligation_text": "Every V2.3_ACTIVE experience channel must provide mobile-first behavior on supported touch-capable mobile and WebView devices without requiring hover-only interaction"
    },
    {
      "acceptance_criterion_references": [
        "UXF-01-R011-AC002",
        "UXF-01-R011-AC003",
        "UXF-01-R011-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-01-R011-O002",
      "obligation_text": "Partner Portal remains outside active scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every V2.3_ACTIVE experience channel must provide mobile-first behavior on supported touch-capable mobile and WebView devices without requiring hover-only interaction; Partner Portal remains outside active scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-01-011",
    "phase_2c_c3_actions": [
      "C3_APPROVED_SEMANTIC_DIRECTIVE"
    ],
    "previous_temporary_key": "TMP-UXF-01-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Accessibility",
    "source_context_sha256": "e687762204c9a487689b5b4220ca1696e9bc24ca97ea67b5ebdd0281c6f8c59b",
    "source_document": "docs/UXF/UXF-01.md",
    "source_fingerprint": "25b194eda2617952c3ecdc381eaa3dafc81e7279ec2fcc45a22a20a8993cf040",
    "source_fingerprint_before_c3": "ff160db085b669d322b5ec49e5dadc8a688519b38bec4ceee6699d8065b6fc1d",
    "source_lines": "L1738-L1833",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-01-R011"
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
  "title": "Every V2.3_ACTIVE experience channel must provide mobile-first behavior on supported touch-capab…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-101 — Experience is channel-specific

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-101",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "bbc5cd35b9af00cffde722fe59c070c4bfd8ecd525f8a10af27f970535acdaa2"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-101-AC001",
        "UXF-101-AC002",
        "UXF-101-AC003"
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
    "source_fingerprint": "bbc5cd35b9af00cffde722fe59c070c4bfd8ecd525f8a10af27f970535acdaa2",
    "source_lines": "L1835-L1910",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-101"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-102",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "cb9765cf2d0613e144c1b1ea3197626db2cd127b965fbd885f0b46bc0f3a8e0a"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-102-AC001",
        "UXF-102-AC002",
        "UXF-102-AC003"
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
    "source_fingerprint": "cb9765cf2d0613e144c1b1ea3197626db2cd127b965fbd885f0b46bc0f3a8e0a",
    "source_lines": "L1912-L1991",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-102"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-103",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "6078e875b60f6d932a6572c0d89d2c89f098ff8050562ef9c07c622476bb02d5"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-103-AC001",
        "UXF-103-AC002",
        "UXF-103-AC003"
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
    "source_fingerprint": "6078e875b60f6d932a6572c0d89d2c89f098ff8050562ef9c07c622476bb02d5",
    "source_lines": "L1993-L2068",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-103"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-104",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "dc69fdbb553ddf2ac5b20bda15c25906f45c84ebea17b066b1a67ec1237d9a84"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-104-AC001",
        "UXF-104-AC002",
        "UXF-104-AC003"
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
    "source_fingerprint": "dc69fdbb553ddf2ac5b20bda15c25906f45c84ebea17b066b1a67ec1237d9a84",
    "source_lines": "L2070-L2145",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-104"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007",
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-105",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "890358db24fe9a33e7a87baa01276ba4cbb6c871d67f94f786af0f66017034d7"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-105-AC001",
        "UXF-105-AC002",
        "UXF-105-AC003"
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
    "source_fingerprint": "890358db24fe9a33e7a87baa01276ba4cbb6c871d67f94f786af0f66017034d7",
    "source_lines": "L2147-L2228",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-105"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007",
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-106",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "6fdbb4f01ebfb494857e932b2865404f0fc718f18366576f5960946986c931d5"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-106-AC001",
        "UXF-106-AC003",
        "UXF-106-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-106-O001",
      "obligation_text": "Internal supplier-selection and allocation mechanics remain invisible in customer journeys"
    },
    {
      "acceptance_criterion_references": [
        "UXF-106-AC002",
        "UXF-106-AC003",
        "UXF-106-AC004"
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
    "source_fingerprint": "6fdbb4f01ebfb494857e932b2865404f0fc718f18366576f5960946986c931d5",
    "source_lines": "L2230-L2333",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-106"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-107",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "32774b30a97625cc01abb8e6a4ba50d52567d923474707e7860742e2b5297062"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-107-AC001",
        "UXF-107-AC002",
        "UXF-107-AC003"
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
    "source_fingerprint": "32774b30a97625cc01abb8e6a4ba50d52567d923474707e7860742e2b5297062",
    "source_lines": "L2335-L2410",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-107"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-108",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "c4b307a0bddaa5f8cdb0587925a2d392085517e835294469053488cd9bf085e0"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-108-AC001",
        "UXF-108-AC002",
        "UXF-108-AC003"
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
    "source_fingerprint": "c4b307a0bddaa5f8cdb0587925a2d392085517e835294469053488cd9bf085e0",
    "source_lines": "L2412-L2487",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-108"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "Presentation and interaction may differ while canonical business outcome remains equivalent"
    ],
    "concrete_bindings": [
      {
        "expected_outcome": {
          "authoritative_source": {
            "allowed_identifiers": [
              "UXF-109.POLICY.OUTCOME.CONFORMING"
            ],
            "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
            "source_type": "SOURCE_LITERAL",
            "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
          },
          "identifier": "UXF-109.POLICY.OUTCOME.CONFORMING",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-01.md",
            "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
            "source_lines": "L727-L730",
            "source_section": "15. Experience Principles > UXF-109"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_OUTCOME",
            "resolver_id": "RESOLVE.UXF-109.UXF-109.POLICY.OUTCOME.CONFORMING",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_OUTCOME"
        },
        "policy": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
            "source_type": "SOURCE_LITERAL",
            "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
          },
          "identifier": "UXF-109.POLICY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-01.md",
            "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
            "source_lines": "L727-L730",
            "source_section": "15. Experience Principles > UXF-109"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.UXF-109.UXF-109.POLICY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "policy_inputs": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
            "source_type": "SOURCE_LITERAL",
            "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
          },
          "identifier": "UXF-109.POLICY_INPUTS",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-01.md",
            "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
            "source_lines": "L727-L730",
            "source_section": "15. Experience Principles > UXF-109"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "RESOLVE.UXF-109.UXF-109.POLICY_INPUTS",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "policy_version": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
            "source_type": "SOURCE_LITERAL",
            "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
          },
          "identifier": "UXF-109.POLICY_VERSION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-01.md",
            "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
            "source_lines": "L727-L730",
            "source_section": "15. Experience Principles > UXF-109"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_VERSION",
            "resolver_id": "RESOLVE.UXF-109.UXF-109.POLICY_VERSION",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_VERSION"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.UXF-109",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "A channel changes canonical pricing, policy, authorization or state semantics"
    ],
    "operator_composition": [
      "POLICY_OUTCOME_EQUALS"
    ],
    "positive_oracle": [
      "Portal, Storefront and API produce equivalent canonical business outcomes"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
      "source_lines": "L727-L730",
      "source_section": "15. Experience Principles > UXF-109"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
          "source_type": "SOURCE_LITERAL",
          "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
        },
        "identifier": "UXF-109.UXF-109.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "UXF-109.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/UXF/UXF-01.md",
          "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
          "source_lines": "L727-L730",
          "source_section": "15. Experience Principles > UXF-109"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.UXF-109.UXF-109.UXF-109.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "UXF-109.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.OPERATION_ID",
        "FIELD.CHANNEL",
        "FIELD.POLICY_VERSION",
        "FIELD.CANONICAL_OBJECT_ID",
        "FIELD.BUSINESS_OUTCOME",
        "FIELD.COMPARISON_RESULT"
      ],
      "producer": "UXF-109.EVIDENCE.PRODUCER",
      "required_collection_origin": "UXF-109.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.OPERATION_ID",
        "FIELD.CHANNEL",
        "FIELD.POLICY_VERSION",
        "FIELD.CANONICAL_OBJECT_ID",
        "FIELD.BUSINESS_OUTCOME",
        "FIELD.COMPARISON_RESULT"
      ],
      "required_values_or_hashes": [
        "UXF-109.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "UXF-109.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "UXF-109.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "UXF-109-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS",
          "evaluator_consumed_bindings": [
            "expected_outcome",
            "policy",
            "policy_inputs",
            "policy_version"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
              "source_type": "SOURCE_LITERAL",
              "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
            },
            "identifier": "UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/UXF/UXF-01.md",
              "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
              "source_lines": "L727-L730",
              "source_section": "15. Experience Principles > UXF-109"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.UXF-109.UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
              "source_type": "SOURCE_LITERAL",
              "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
            },
            "identifier": "UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/UXF/UXF-01.md",
              "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
              "source_lines": "L727-L730",
              "source_section": "15. Experience Principles > UXF-109"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "RESOLVE.UXF-109.UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_OUTCOME"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "expected_outcome": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "UXF-109.POLICY.OUTCOME.CONFORMING"
                  ],
                  "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
                  "source_type": "SOURCE_LITERAL",
                  "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
                },
                "identifier": "UXF-109.POLICY.OUTCOME.CONFORMING",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-01.md",
                  "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
                  "source_lines": "L727-L730",
                  "source_section": "15. Experience Principles > UXF-109"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.UXF-109.UXF-109.POLICY.OUTCOME.CONFORMING",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "policy": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
                  "source_type": "SOURCE_LITERAL",
                  "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
                },
                "identifier": "UXF-109.POLICY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-01.md",
                  "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
                  "source_lines": "L727-L730",
                  "source_section": "15. Experience Principles > UXF-109"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.UXF-109.UXF-109.POLICY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "policy_inputs": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
                  "source_type": "SOURCE_LITERAL",
                  "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
                },
                "identifier": "UXF-109.POLICY_INPUTS",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-01.md",
                  "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
                  "source_lines": "L727-L730",
                  "source_section": "15. Experience Principles > UXF-109"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.UXF-109.UXF-109.POLICY_INPUTS",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "policy_version": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
                  "source_type": "SOURCE_LITERAL",
                  "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
                },
                "identifier": "UXF-109.POLICY_VERSION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-01.md",
                  "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
                  "source_lines": "L727-L730",
                  "source_section": "15. Experience Principles > UXF-109"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_VERSION",
                  "resolver_id": "RESOLVE.UXF-109.UXF-109.POLICY_VERSION",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_VERSION"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
                  "source_type": "SOURCE_LITERAL",
                  "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
                },
                "identifier": "UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-01.md",
                  "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
                  "source_lines": "L727-L730",
                  "source_section": "15. Experience Principles > UXF-109"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.UXF-109.UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
                  "source_type": "SOURCE_LITERAL",
                  "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
                },
                "identifier": "UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-01.md",
                  "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
                  "source_lines": "L727-L730",
                  "source_section": "15. Experience Principles > UXF-109"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "OBSERVE.UXF-109.UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
                "source_type": "SOURCE_LITERAL",
                "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
              },
              "identifier": "UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-01.md",
                "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
                "source_lines": "L727-L730",
                "source_section": "15. Experience Principles > UXF-109"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.UXF-109.UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "POLICY_OUTCOME_EQUALS"
          },
          "obligation_id": "UXF-109-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
              "source_type": "SOURCE_LITERAL",
              "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
            },
            "identifier": "UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/UXF/UXF-01.md",
              "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
              "source_lines": "L727-L730",
              "source_section": "15. Experience Principles > UXF-109"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "OBSERVE.UXF-109.UXF-109.UXF-109.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_OUTCOME"
          },
          "operator_id": "POLICY_OUTCOME_EQUALS",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "expected_outcome": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "UXF-109.POLICY.OUTCOME.CONFORMING"
                ],
                "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
                "source_type": "SOURCE_LITERAL",
                "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
              },
              "identifier": "UXF-109.POLICY.OUTCOME.CONFORMING",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-01.md",
                "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
                "source_lines": "L727-L730",
                "source_section": "15. Experience Principles > UXF-109"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_OUTCOME",
                "resolver_id": "RESOLVE.UXF-109.UXF-109.POLICY.OUTCOME.CONFORMING",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_OUTCOME"
            },
            "policy": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
                "source_type": "SOURCE_LITERAL",
                "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
              },
              "identifier": "UXF-109.POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-01.md",
                "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
                "source_lines": "L727-L730",
                "source_section": "15. Experience Principles > UXF-109"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.UXF-109.UXF-109.POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "policy_inputs": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
                "source_type": "SOURCE_LITERAL",
                "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
              },
              "identifier": "UXF-109.POLICY_INPUTS",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-01.md",
                "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
                "source_lines": "L727-L730",
                "source_section": "15. Experience Principles > UXF-109"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "RESOLVE.UXF-109.UXF-109.POLICY_INPUTS",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "policy_version": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
                "source_type": "SOURCE_LITERAL",
                "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
              },
              "identifier": "UXF-109.POLICY_VERSION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-109.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-01.md",
                "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
                "source_lines": "L727-L730",
                "source_section": "15. Experience Principles > UXF-109"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_VERSION",
                "resolver_id": "RESOLVE.UXF-109.UXF-109.POLICY_VERSION",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_VERSION"
            }
          }
        }
      ],
      "boundary_cases": [
        "Presentation and interaction may differ while canonical business outcome remains equivalent"
      ],
      "contract_ast_sha256": "c93fdbea5fdda055a99f41cf7f69ef16d8b34d6e62e90267c5f7ae9b566527f5",
      "contract_id": "P2C.C4.CONTRACT.UXF-109",
      "criticality": "HIGH",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-01.md#15. Experience Principles > UXF-109",
            "source_type": "SOURCE_LITERAL",
            "version": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d"
          },
          "identifier": "UXF-109.UXF-109.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-109.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-01.md",
            "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
            "source_lines": "L727-L730",
            "source_section": "15. Experience Principles > UXF-109"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.UXF-109.UXF-109.UXF-109.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "UXF-109.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.OPERATION_ID",
          "FIELD.CHANNEL",
          "FIELD.POLICY_VERSION",
          "FIELD.CANONICAL_OBJECT_ID",
          "FIELD.BUSINESS_OUTCOME",
          "FIELD.COMPARISON_RESULT"
        ],
        "producer": "UXF-109.EVIDENCE.PRODUCER",
        "required_collection_origin": "UXF-109.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.OPERATION_ID",
          "FIELD.CHANNEL",
          "FIELD.POLICY_VERSION",
          "FIELD.CANONICAL_OBJECT_ID",
          "FIELD.BUSINESS_OUTCOME",
          "FIELD.COMPARISON_RESULT"
        ],
        "required_values_or_hashes": [
          "UXF-109.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "UXF-109.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "UXF-109.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-EC730FC188B790B463DD",
        "P2C-C4-FX-B84EBBF44FC848C2EDE7",
        "P2C-C4-FX-413582DE7CCCACD1C660"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "A channel changes canonical pricing, policy, authorization or state semantics"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "UXF-109-O001",
          "obligation_text": "Experience must remain consistent across Portal, Storefront and APIs"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "UXF-109.O1.1.POLICY_OUTCOME_EQUALS"
          ],
          "coverage_count": 1,
          "obligation_id": "UXF-109-O001"
        }
      ],
      "operator_composition": [
        "POLICY_OUTCOME_EQUALS"
      ],
      "positive_oracles": [
        "Portal, Storefront and API produce equivalent canonical business outcomes"
      ],
      "preconditions": [
        "Channels reference the same canonical business policy and object identity"
      ],
      "prohibitions": [
        "A channel changes canonical pricing, policy, authorization or state semantics"
      ],
      "requirement_id": "UXF-109",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/UXF/UXF-01.md",
        "source_fingerprint": "4b24c0c308560c53f4fc8d0e074f28384fb7f843ba9dcf8257f900aa3ebd997d",
        "source_lines": "L727-L730",
        "source_section": "15. Experience Principles > UXF-109"
      },
      "source_statement": "Experience must remain consistent across Portal, Storefront and APIs.",
      "surrounding_source_context": "### UXF-109\n\nExperience must remain consistent across Portal, Storefront and APIs.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.UXF-109",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "SEMANTIC_ACCEPTANCE_RENDERER_C2",
    "runtime_status": "RUNTIME_ADAPTER_PENDING"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "ACCEPTANCE_READY",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-109-AC001",
        "UXF-109-AC002",
        "UXF-109-AC003"
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
    "source_fingerprint": "5882ce3c943ce883c7571df999582e8e1a126d66e5dd3d2b7024a5316ef94da9",
    "source_lines": "L2489-L3434",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-109"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-110",
      "source_document": "docs/UXF/UXF-01.md",
      "source_fingerprint": "ad84aa4103c9c2bce36e8756c0f64446fb4bea00a898af9e63805be2e7587d03"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-110-AC001",
        "UXF-110-AC002",
        "UXF-110-AC003"
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
    "source_fingerprint": "ad84aa4103c9c2bce36e8756c0f64446fb4bea00a898af9e63805be2e7587d03",
    "source_lines": "L3436-L3523",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-110"
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
