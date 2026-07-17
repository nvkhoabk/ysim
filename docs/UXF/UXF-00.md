---
document_code: "UXF-00"
document_id: "UXF-00"
title: "User Experience Foundation Overview"
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

# UXF-00 — User Experience Foundation Overview

---

# 1. Purpose

This document defines the **User Experience Foundation (UXF)** for the YSim Platform.

Unlike traditional UI guideline documents, UXF defines the architectural principles that govern how every Portal, Storefront and Customer Experience is designed, rendered and operated.

UXF serves as the authoritative reference for:

- Business Architecture
- Frontend Architecture
- White-label Architecture
- Storefront Runtime
- Portal Design
- Theme Engine
- Localization Engine
- Experience Runtime
- AI (YSF / Codex) generated frontend implementations

UXF is considered the **Source of Truth** for every frontend application within the YSim Platform.

---

# 2. Vision

YSim is **NOT** a website.

YSim is **NOT** an online shop.

YSim is an **Experience Platform** capable of rendering different commercial experiences according to runtime business context.

The same URL may produce completely different user experiences depending on:

- Organization
- Storefront
- Domain
- Campaign
- Tracking ID
- Customer Segment
- Device
- Localization
- Currency
- Runtime Policies

Therefore,

> Every rendered page is the result of runtime context resolution rather than static page implementation.

---

# 3. Experience First Principle

Traditional commerce systems generally follow:

```
Website

↓

Page

↓

Product

↓

Checkout
```

YSim follows a different philosophy.

```
Request

↓

Runtime Context Resolution

↓

Experience Resolution

↓

Business Resolution

↓

Commercial Resolution

↓

Localization Resolution

↓

Storefront Runtime

↓

Rendered Experience
```

The UI is therefore an output of the platform, not a hardcoded implementation.

---

# 4. User Experience Architecture

Every customer interaction is rendered by resolving multiple independent contexts.

```
Incoming Request

        │

        ▼

Platform Context

        │

        ▼

Organization Context

        │

        ▼

Storefront Context

        │

        ▼

Campaign Context

        │

        ▼

Tracking Context

        │

        ▼

Localization Context

        │

        ▼

Business Context

        │

        ▼

Commerce Experience

        │

        ▼

Rendered UI
```

No individual module independently determines the final interface.

---

# 5. Runtime Experience Resolution

Experience Resolution consists of several independent engines.

```
Experience Runtime

├── Theme Resolver

├── Template Resolver

├── Asset Resolver

├── Navigation Resolver

├── Layout Resolver

├── Localization Resolver

├── Business Binding Resolver

├── Payment Resolver

├── Catalog Resolver

├── Promotion Resolver

├── Checkout Resolver

├── Support Resolver

└── Runtime Policy Resolver
```

Each resolver contributes part of the final rendered experience.

---

# 6. Storefront Definition

A Storefront is **NOT** a website template.

A Storefront is a complete commercial experience configuration.

A Storefront contains:

- Experience Configuration
- Business Configuration
- Commercial Configuration
- Operational Configuration
- Runtime Policies

A Storefront is therefore an independent business entity.

---

# 7. Business Binding Principle

Every Storefront must be connected to business capabilities.

Examples include:

- Product Catalog
- Pricing Policy
- Promotion Policy
- Payment Profile
- Checkout Flow
- Fulfillment Policy
- Customer Policy
- Support Profile
- Legal Profile

Without valid business bindings a Storefront **cannot be published**.

---

# 8. Supplier Isolation Principle

Supplier systems are internal infrastructure.

Storefronts never communicate with suppliers directly.

The correct architecture is:

```
Storefront

↓

Order

↓

Allocation Engine

↓

Supplier Gateway

↓

Supplier
```

Storefronts only understand YSim Products.

Supplier Products are hidden behind the Allocation Engine.

This architecture guarantees:

- supplier independence
- routing flexibility
- cost optimization
- failover capability
- future supplier replacement

without changing storefront implementations.

---

# 9. Allocation Principle

Allocation is a core business capability of YSim.

Allocation is responsible for:

- Supplier Routing
- Inventory Reservation
- Inventory Release
- Fulfillment
- Retry
- Replacement
- Cost Optimization
- Availability Decision

Allocation is the only business component allowed to determine which supplier provides an eSIM.

---

# 10. Product Principle

Storefronts expose only YSim Products.

```
YSim Product

↓

Allocation Rule

↓

Supplier Mapping
```

Supplier products are never exposed to:

- Storefront
- Portal
- Customer
- Agency
- Reseller

Supplier Mapping remains internal configuration.

---

# 11. Experience Inheritance

Every experience supports hierarchical inheritance.

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

Each level only overrides the required configuration.

All unspecified properties inherit from their parent.

---

# 12. Fallback Experience

Every runtime configuration must support fallback.

Fallback applies to every configurable aspect.

Examples:

- Theme
- Catalog
- Payment
- Promotion
- Checkout
- Support
- Localization
- Assets
- Navigation

If a configuration cannot be resolved, the runtime automatically falls back to the nearest valid parent configuration.

No runtime request should fail solely because a child configuration is incomplete.

---

# 13. Localization Principle

Localization extends beyond language translation.

Localization defines the complete customer experience for a specific market.

Localization may affect:

- Language
- Currency
- Date Format
- Number Format
- Timezone
- Payment Methods
- Promotions
- Hero Banner
- Product Recommendations
- Support Information
- FAQ
- Legal Documents
- Checkout Flow
- Email Templates
- SMS Templates
- Notifications

Localization therefore represents a localized commercial experience.

---

# 14. Tracking Context

Tracking identifiers are part of runtime experience resolution.

Tracking may influence:

- Landing Page
- Campaign
- Promotion
- Banner
- CTA
- Product Visibility
- Pricing
- Commission
- Affiliate Attribution
- Support Channel
- Analytics

Tracking is not limited to reporting.

Tracking participates in experience generation.

---

# 15. Page Composition

Pages are dynamically composed.

A page consists of Sections.

Each Section consists of Components.

```
Page

↓

Sections

↓

Components

↓

Business Data

↓

Rendered Experience
```

Sections may be:

- enabled
- disabled
- reordered
- replaced

without modifying application code.

---

# 16. Design System Principle

All portals share a unified Design System.

Applications include:

- Platform Portal
- Administration Portal
- Agency Portal
- Partner Portal
- Customer Portal
- White-label Storefront

All applications must reuse the same component library.

UI duplication is prohibited.

---

# 17. White-label Principle

Every tenant may own multiple storefronts.

Each storefront may have:

- Domain
- Branding
- Theme
- Assets
- Localization
- Catalog
- Payment Profile
- Checkout Policy
- Support Profile

White-label customization must never require source code modification.

---

# 18. Published Experience Snapshot

Runtime rendering must use immutable published configurations.

Lifecycle:

```
Draft

↓

Preview

↓

Validation

↓

Publish

↓

Published Snapshot

↓

Runtime Rendering
```

The runtime never renders directly from editable configurations.

---

# 19. Experience Runtime Goals

The Experience Runtime must provide:

- Dynamic Rendering
- White-label Support
- Multi-tenant Isolation
- Localization
- Runtime Resolution
- Experience Inheritance
- Safe Fallback
- Versioning
- Preview
- Publish
- Rollback
- Auditability

---

# 20. Architectural Principles

The following principles are mandatory.

### UXF-001

Experience is resolved at runtime.

---

### UXF-002

Storefronts represent commercial experiences rather than websites.

---

### UXF-003

Storefronts consume YSim Products only.

---

### UXF-004

Supplier systems are internal infrastructure.

---

### UXF-005

Allocation is the only capability allowed to select suppliers.

---

### UXF-006

Every runtime configuration supports inheritance.

---

### UXF-007

Every runtime configuration supports fallback.

---

### UXF-008

Localization defines customer experience, not only language.

---

### UXF-009

Tracking participates in experience generation.

---

### UXF-010

Every published storefront must pass business binding validation.

---

### UXF-011

Runtime rendering must use published snapshots.

---

### UXF-012

Design System components are shared across every portal.

---

# 21. References

This document should be read together with:

- BRD — Business Requirements
- AFM — AI Factory Model
- YADF — YSim Architecture Definition Framework
- ABP — Architecture Blueprint
- DIP — Development & Implementation Principles
- UXF-01 — Channels, Personas & Navigation
- UXF-02 — Design System, Theme & Experience Inheritance
- UXF-03 — Storefront Template & Page Composition
- UXF-04 — White-label, Localization & Runtime Context Resolution
- UXF-05 — Storefront Runtime Architecture & Business Binding

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## v2.3 normative requirement appendix — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R001 — Every Storefront must be connected to business capabilities

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
      "requirement_id": "UXF-00-R001",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "92d1f71588a560b49a45176ad1114fd76b9b1dd1e1ecb9286de6f41127f98a8d"
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
        "UXF-00-R001-AC001",
        "UXF-00-R001-AC002",
        "UXF-00-R001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R001-O001",
      "obligation_text": "Every Storefront must be connected to business capabilities"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every Storefront must be connected to business capabilities.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-001",
    "previous_temporary_key": "TMP-UXF-00-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Business Binding Principle",
    "source_context_sha256": "56080338734e3d9860464e1deffabe913bece6ac6e254fcf2b4e4f26b95f508a",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "92d1f71588a560b49a45176ad1114fd76b9b1dd1e1ecb9286de6f41127f98a8d",
    "source_lines": "L706-L784",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R001"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R001",
  "title": "Every Storefront must be connected to business capabilities",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R002 — Without valid business bindings a Storefront **cannot be published**

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
      "requirement_id": "UXF-00-R002",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "0b75aafa06ab5d1b39d4b0ccc17488c6729743e32c0f8497163caba57f165d32"
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
        "UXF-00-R002-AC001",
        "UXF-00-R002-AC002",
        "UXF-00-R002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R002-O001",
      "obligation_text": "Without valid business bindings a Storefront **cannot be published**"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Without valid business bindings a Storefront **cannot be published**.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-002",
    "previous_temporary_key": "TMP-UXF-00-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Business Binding Principle",
    "source_context_sha256": "56080338734e3d9860464e1deffabe913bece6ac6e254fcf2b4e4f26b95f508a",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "0b75aafa06ab5d1b39d4b0ccc17488c6729743e32c0f8497163caba57f165d32",
    "source_lines": "L786-L864",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R002"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R002",
  "title": "Without valid business bindings a Storefront **cannot be published**",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R003 — Storefronts never communicate with suppliers directly

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-00-R003",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "37167209c7832f685b7dfbf2d9f00dadd658e9d6d31f30e8f22eb04bad29ee00"
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
        "UXF-00-R003-AC001",
        "UXF-00-R003-AC002",
        "UXF-00-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R003-O001",
      "obligation_text": "Storefronts never communicate with suppliers directly"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Storefronts never communicate with suppliers directly.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-003",
    "previous_temporary_key": "TMP-UXF-00-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Supplier Isolation Principle",
    "source_context_sha256": "4f0bd9a2fc1905a2811a2245e10e7624900db78efcdb96c9c2294c049d8d9679",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "37167209c7832f685b7dfbf2d9f00dadd658e9d6d31f30e8f22eb04bad29ee00",
    "source_lines": "L866-L948",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R003"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R003",
  "title": "Storefronts never communicate with suppliers directly",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R004 —  future supplier replacement

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "UXF-00-R004",
    "scope_status": "FUTURE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is retained for a future baseline and is excluded from v2.3 delivery.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "- future supplier replacement",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-004",
    "previous_temporary_key": "TMP-UXF-00-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Supplier Isolation Principle",
    "source_context_sha256": "4f0bd9a2fc1905a2811a2245e10e7624900db78efcdb96c9c2294c049d8d9679",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "012189671efdafabfc3a1b921170acd4d693c649e86cbd8ef1b2cfb336ea8ad9",
    "source_lines": "L950-L1013",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R004"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "FUTURE",
  "stable_id": "UXF-00-R004",
  "title": " future supplier replacement",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R005 — Supplier products are never exposed to: - Storefront

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-00-R005",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "b2f5844d197139710bc0e03bbc90b9f878e62ff8c3620951bbf8a6a9e6eff722"
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
        "UXF-00-R005-AC001",
        "UXF-00-R005-AC002",
        "UXF-00-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R005-O001",
      "obligation_text": "Supplier products are never exposed to: - Storefront"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier products are never exposed to: - Storefront",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-005",
    "previous_temporary_key": "TMP-UXF-00-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Product Principle",
    "source_context_sha256": "b37a243bf303f8bdba0991929cc073ad86c42ae0e4fcf819802c90fd8baed315",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "b2f5844d197139710bc0e03bbc90b9f878e62ff8c3620951bbf8a6a9e6eff722",
    "source_lines": "L1015-L1097",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R005"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R005",
  "title": "Supplier products are never exposed to: - Storefront",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R006 — Supplier products are never exposed to: - Portal

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-00-R006",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "8e141203b0a47da600ecea30933256281f6e5d43147cbd987c187f6d4f25b329"
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
        "UXF-00-R006-AC001",
        "UXF-00-R006-AC002",
        "UXF-00-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R006-O001",
      "obligation_text": "Supplier products are never exposed to: - Portal"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier products are never exposed to: - Portal",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-006",
    "previous_temporary_key": "TMP-UXF-00-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Product Principle",
    "source_context_sha256": "b37a243bf303f8bdba0991929cc073ad86c42ae0e4fcf819802c90fd8baed315",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "8e141203b0a47da600ecea30933256281f6e5d43147cbd987c187f6d4f25b329",
    "source_lines": "L1099-L1181",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R006"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R006",
  "title": "Supplier products are never exposed to: - Portal",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R007 — Supplier products are never exposed to: - Customer

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
      "requirement_id": "UXF-00-R007",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "fdc72831c7e4038f97728192b7c087d6768bcae29b46c9e6fe5a5798e64fa247"
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
        "UXF-00-R007-AC001",
        "UXF-00-R007-AC002",
        "UXF-00-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R007-O001",
      "obligation_text": "Supplier products are never exposed to: - Customer"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier products are never exposed to: - Customer",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007",
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-007",
    "previous_temporary_key": "TMP-UXF-00-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Product Principle",
    "source_context_sha256": "b37a243bf303f8bdba0991929cc073ad86c42ae0e4fcf819802c90fd8baed315",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "fdc72831c7e4038f97728192b7c087d6768bcae29b46c9e6fe5a5798e64fa247",
    "source_lines": "L1183-L1267",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R007"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R007",
  "title": "Supplier products are never exposed to: - Customer",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R008 — Supplier products are never exposed to: - Agency

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-00-R008",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "541aef09996088e61faf7178231daef69d5352708330dceaf47cb1f09b6f7f68"
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
        "UXF-00-R008-AC001",
        "UXF-00-R008-AC002",
        "UXF-00-R008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R008-O001",
      "obligation_text": "Supplier products are never exposed to: - Agency"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier products are never exposed to: - Agency",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-008",
    "previous_temporary_key": "TMP-UXF-00-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Product Principle",
    "source_context_sha256": "b37a243bf303f8bdba0991929cc073ad86c42ae0e4fcf819802c90fd8baed315",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "541aef09996088e61faf7178231daef69d5352708330dceaf47cb1f09b6f7f68",
    "source_lines": "L1269-L1351",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R008"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R008",
  "title": "Supplier products are never exposed to: - Agency",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R009 — Supplier products are never exposed to: - Reseller

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-00-R009",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "af434f8496d265fadd59ea1bac17adf49abca75a25b4ecce5f0a01f5057b9bdc"
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
        "UXF-00-R009-AC001",
        "UXF-00-R009-AC002",
        "UXF-00-R009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R009-O001",
      "obligation_text": "Supplier products are never exposed to: - Reseller"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier products are never exposed to: - Reseller",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-009",
    "previous_temporary_key": "TMP-UXF-00-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Product Principle",
    "source_context_sha256": "b37a243bf303f8bdba0991929cc073ad86c42ae0e4fcf819802c90fd8baed315",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "af434f8496d265fadd59ea1bac17adf49abca75a25b4ecce5f0a01f5057b9bdc",
    "source_lines": "L1353-L1435",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R009"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R009",
  "title": "Supplier products are never exposed to: - Reseller",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R010 — Each level only overrides the required configuration

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
      "requirement_id": "UXF-00-R010",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "4e8368f5affb418a03d8a7bf14c437aa1786deb3ac46c145f4c3542a5043a653"
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
        "UXF-00-R010-AC001",
        "UXF-00-R010-AC002",
        "UXF-00-R010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R010-O001",
      "obligation_text": "Each level only overrides the required configuration"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Each level only overrides the required configuration.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-010",
    "previous_temporary_key": "TMP-UXF-00-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Experience Inheritance",
    "source_context_sha256": "a613298c65e637ea8a830828d79cd26f1cf6ad4abcf01870d1deecf22ded0d41",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "4e8368f5affb418a03d8a7bf14c437aa1786deb3ac46c145f4c3542a5043a653",
    "source_lines": "L1437-L1515",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R010"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R010",
  "title": "Each level only overrides the required configuration",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R011 — Every runtime configuration must support fallback

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
      "requirement_id": "UXF-00-R011",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "adfa8e3e62d09fe0a726043a0a990459cf09ab14b48936c9f06fca537d31e419"
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
        "UXF-00-R011-AC001",
        "UXF-00-R011-AC002",
        "UXF-00-R011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R011-O001",
      "obligation_text": "Every runtime configuration must support fallback"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every runtime configuration must support fallback.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-011",
    "previous_temporary_key": "TMP-UXF-00-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Fallback Experience",
    "source_context_sha256": "60b4a5e34a152d8e66574e8461c34a0296b318eea1631ec5ff334805aa9c22c3",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "adfa8e3e62d09fe0a726043a0a990459cf09ab14b48936c9f06fca537d31e419",
    "source_lines": "L1517-L1595",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R011"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R011",
  "title": "Every runtime configuration must support fallback",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R012 — If a configuration cannot be resolved, the runtime automatically falls back to the nearest valid…

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
      "requirement_id": "UXF-00-R012",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "b0b90b345be44d6c45b4319085bd2a17f76c0a7670829a321d6d86ddd083f3b3"
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
        "UXF-00-R012-AC001",
        "UXF-00-R012-AC002",
        "UXF-00-R012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R012-O001",
      "obligation_text": "If a configuration cannot be resolved, the runtime automatically falls back to the nearest valid parent configuration"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "If a configuration cannot be resolved, the runtime automatically falls back to the nearest valid parent configuration.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-012",
    "previous_temporary_key": "TMP-UXF-00-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Fallback Experience",
    "source_context_sha256": "60b4a5e34a152d8e66574e8461c34a0296b318eea1631ec5ff334805aa9c22c3",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "b0b90b345be44d6c45b4319085bd2a17f76c0a7670829a321d6d86ddd083f3b3",
    "source_lines": "L1597-L1675",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R012"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R012",
  "title": "If a configuration cannot be resolved, the runtime automatically falls back to the nearest valid…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R013 — A missing or invalid business-critical configuration must fail closed: checkout, payment, alloca…

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
      "requirement_id": "UXF-00-R013",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "acc952dfd45e0eeff27343f8c3d28b0434c678cf748e15279ae69423a736e87f"
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
        "UXF-00-R013-AC001",
        "UXF-00-R013-AC004",
        "UXF-00-R013-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R013-O001",
      "obligation_text": "Missing or invalid business-critical configuration fails closed"
    },
    {
      "acceptance_criterion_references": [
        "UXF-00-R013-AC002",
        "UXF-00-R013-AC004",
        "UXF-00-R013-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R013-O002",
      "obligation_text": "Checkout, payment, allocation, fulfillment, authorization, and security flows do not continue with inferred unsafe defaults"
    },
    {
      "acceptance_criterion_references": [
        "UXF-00-R013-AC003",
        "UXF-00-R013-AC004",
        "UXF-00-R013-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R013-O003",
      "obligation_text": "The failure exposes actionable recovery information"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "A missing or invalid business-critical configuration must fail closed: checkout, payment, allocation, fulfillment, authorization, and security flows must not continue with inferred unsafe defaults, and the failure must expose actionable recovery information.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-013",
    "phase_2c_c3_actions": [
      "C3_APPROVED_SEMANTIC_DIRECTIVE"
    ],
    "previous_temporary_key": "TMP-UXF-00-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Fallback Experience",
    "source_context_sha256": "60b4a5e34a152d8e66574e8461c34a0296b318eea1631ec5ff334805aa9c22c3",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "acc952dfd45e0eeff27343f8c3d28b0434c678cf748e15279ae69423a736e87f",
    "source_fingerprint_before_c3": "1796ccb7f406176950afb115a8cf25040721fd9b6a72488039a96d92c5eadadc",
    "source_lines": "L1677-L1785",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R013"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R013",
  "title": "A missing or invalid business-critical configuration must fail closed: checkout, payment, alloca…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R014 — All applications must reuse the same component library

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
      "requirement_id": "UXF-00-R014",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "eaa91ef8121d1a90ba037df4326fc1cbd8d9bd14a48d2fa9c4f2d0c440aa3bc1"
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
        "UXF-00-R014-AC001",
        "UXF-00-R014-AC002",
        "UXF-00-R014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R014-O001",
      "obligation_text": "All applications must reuse the same component library"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "All applications must reuse the same component library.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-014",
    "previous_temporary_key": "TMP-UXF-00-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Design System Principle",
    "source_context_sha256": "61598e6603bdf638c801c93c93688445670b4d69998c2f2884a9ac45dc770622",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "eaa91ef8121d1a90ba037df4326fc1cbd8d9bd14a48d2fa9c4f2d0c440aa3bc1",
    "source_lines": "L1787-L1865",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R014"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R014",
  "title": "All applications must reuse the same component library",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R015 — UI duplication is prohibited

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
      "requirement_id": "UXF-00-R015",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "8962a5e90181b99fd96bf6b16bc9b38e461a918ffa667966b29c4b1837a5fadd"
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
        "UXF-00-R015-AC001",
        "UXF-00-R015-AC002",
        "UXF-00-R015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R015-O001",
      "obligation_text": "UI duplication is prohibited"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "UI duplication is prohibited.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-015",
    "previous_temporary_key": "TMP-UXF-00-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Design System Principle",
    "source_context_sha256": "61598e6603bdf638c801c93c93688445670b4d69998c2f2884a9ac45dc770622",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "8962a5e90181b99fd96bf6b16bc9b38e461a918ffa667966b29c4b1837a5fadd",
    "source_lines": "L1867-L1945",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R015"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R015",
  "title": "UI duplication is prohibited",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R016 — White-label configuration must not require source-code modification

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
      "requirement_id": "UXF-00-R016",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "c1d29364303d17973a158aaaf1005c8a91f12502f035c1ac39088c8b3c84770f"
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
        "UXF-00-R016-AC001",
        "UXF-00-R016-AC002",
        "UXF-00-R016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R016-O001",
      "obligation_text": "White-label configuration must not require source-code modification"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-024",
      "selected_disposition": "ROUTE_TO_REMEDIATION"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "White-label configuration must not require source-code modification.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-016",
    "previous_temporary_key": "TMP-UXF-00-016",
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. White-label Principle",
    "source_context_sha256": "6a058263fda34ad832842c30d4c6a5b75122da35cbb2fa3f1f5a7efa062d0236",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "c1d29364303d17973a158aaaf1005c8a91f12502f035c1ac39088c8b3c84770f",
    "source_lines": "L1947-L2037",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R016"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R016",
  "title": "White-label configuration must not require source-code modification",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R017 — Runtime rendering must use immutable published configurations

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
      "requirement_id": "UXF-00-R017",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "d3de627d24a1d705c0184609fb63ab03a5cce88d6a9574bd0d16b44330f0f1c4"
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
        "UXF-00-R017-AC001",
        "UXF-00-R017-AC002",
        "UXF-00-R017-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R017-O001",
      "obligation_text": "Runtime rendering must use immutable published configurations"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-00-R017 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-00-R017 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-00-R017 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-00-R017-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-00-R017-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-00-R017 does not define a recovery obligation."
    }
  },
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-025",
      "selected_disposition": "CONFIRM_CRITICAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Runtime rendering must use immutable published configurations.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-017",
    "previous_temporary_key": "TMP-UXF-00-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Published Experience Snapshot",
    "source_context_sha256": "5a9bf72c0ba863c7bf431087e49e707e8fc0598f76e6e142f7d8ba0e09f8fd68",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "d3de627d24a1d705c0184609fb63ab03a5cce88d6a9574bd0d16b44330f0f1c4",
    "source_lines": "L2039-L2159",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R017"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R017",
  "title": "Runtime rendering must use immutable published configurations",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R018 — The runtime never renders directly from editable configurations

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
      "requirement_id": "UXF-00-R018",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "cb34abacfb3ea60573b337a95f0bbe841e0da2bd9b4ff135e173e4eb1e56a6d4"
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
        "UXF-00-R018-AC001",
        "UXF-00-R018-AC002",
        "UXF-00-R018-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R018-O001",
      "obligation_text": "The runtime never renders directly from editable configurations"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The runtime never renders directly from editable configurations.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-018",
    "previous_temporary_key": "TMP-UXF-00-018",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Published Experience Snapshot",
    "source_context_sha256": "5a9bf72c0ba863c7bf431087e49e707e8fc0598f76e6e142f7d8ba0e09f8fd68",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "cb34abacfb3ea60573b337a95f0bbe841e0da2bd9b4ff135e173e4eb1e56a6d4",
    "source_lines": "L2161-L2239",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R018"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R018",
  "title": "The runtime never renders directly from editable configurations",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R019 — The Experience Runtime must provide: - Dynamic Rendering

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
      "requirement_id": "UXF-00-R019",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "bc0a95136e071663ec73def373042c7bf2b9b6734d920e9149ee9877926818af"
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
        "UXF-00-R019-AC001",
        "UXF-00-R019-AC002",
        "UXF-00-R019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R019-O001",
      "obligation_text": "The Experience Runtime must provide: - Dynamic Rendering"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Experience Runtime must provide: - Dynamic Rendering",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-019",
    "previous_temporary_key": "TMP-UXF-00-019",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Experience Runtime Goals",
    "source_context_sha256": "76f7626abb86825c0f22537f994b3c1b8a3de86ed7ccb239ae54c9d44f1cef71",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "bc0a95136e071663ec73def373042c7bf2b9b6734d920e9149ee9877926818af",
    "source_lines": "L2241-L2319",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R019"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R019",
  "title": "The Experience Runtime must provide: - Dynamic Rendering",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R020 — The Experience Runtime must provide: - White-label Support

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
      "requirement_id": "UXF-00-R020",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "e6250521ed732a508e7a9c9c2c02df6eff9a08fd32f02d300704a10c208ee7d3"
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
        "UXF-00-R020-AC001",
        "UXF-00-R020-AC002",
        "UXF-00-R020-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R020-O001",
      "obligation_text": "The Experience Runtime must provide: - White-label Support"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-026",
      "selected_disposition": "CONFIRM_HIGH"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Experience Runtime must provide: - White-label Support",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-020",
    "previous_temporary_key": "TMP-UXF-00-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Experience Runtime Goals",
    "source_context_sha256": "76f7626abb86825c0f22537f994b3c1b8a3de86ed7ccb239ae54c9d44f1cef71",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "e6250521ed732a508e7a9c9c2c02df6eff9a08fd32f02d300704a10c208ee7d3",
    "source_lines": "L2321-L2408",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R020"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R020",
  "title": "The Experience Runtime must provide: - White-label Support",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R021 — The Experience Runtime must provide: - Multi-tenant Isolation

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
      "requirement_id": "UXF-00-R021",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "bd00945eaa84d8b84256ad935b55e374bed6f425aec373041b4631c9694ec2b1"
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
        "UXF-00-R021-AC001",
        "UXF-00-R021-AC002",
        "UXF-00-R021-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R021-O001",
      "obligation_text": "The Experience Runtime must provide: - Multi-tenant Isolation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-00-R021 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-00-R021 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-00-R021 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-00-R021-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-00-R021-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-00-R021 does not define a recovery obligation."
    }
  },
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-027",
      "selected_disposition": "CONFIRM_CRITICAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Experience Runtime must provide: - Multi-tenant Isolation",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-021",
    "previous_temporary_key": "TMP-UXF-00-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Experience Runtime Goals",
    "source_context_sha256": "76f7626abb86825c0f22537f994b3c1b8a3de86ed7ccb239ae54c9d44f1cef71",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "bd00945eaa84d8b84256ad935b55e374bed6f425aec373041b4631c9694ec2b1",
    "source_lines": "L2410-L2531",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R021"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031",
      "BRD-UPDATE-01-R024"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R021",
  "title": "The Experience Runtime must provide: - Multi-tenant Isolation",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R022 — The Experience Runtime must provide: - Localization

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
      "requirement_id": "UXF-00-R022",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "2f5845f11f6e5495c83d8a8ccb096e9e2fbd5487ff56d0ec59a138b3f99ee091"
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
        "UXF-00-R022-AC001",
        "UXF-00-R022-AC002",
        "UXF-00-R022-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R022-O001",
      "obligation_text": "The Experience Runtime must provide: - Localization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Experience Runtime must provide: - Localization",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-022",
    "previous_temporary_key": "TMP-UXF-00-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Experience Runtime Goals",
    "source_context_sha256": "76f7626abb86825c0f22537f994b3c1b8a3de86ed7ccb239ae54c9d44f1cef71",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "2f5845f11f6e5495c83d8a8ccb096e9e2fbd5487ff56d0ec59a138b3f99ee091",
    "source_lines": "L2533-L2611",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R022"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R022",
  "title": "The Experience Runtime must provide: - Localization",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R023 — The Experience Runtime must provide: - Runtime Resolution

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
      "requirement_id": "UXF-00-R023",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "d7c4e37de17e0807232e69d047381fc2438a79cd6b5cad5931fc3558aff83a9a"
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
        "UXF-00-R023-AC001",
        "UXF-00-R023-AC002",
        "UXF-00-R023-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R023-O001",
      "obligation_text": "The Experience Runtime must provide: - Runtime Resolution"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Experience Runtime must provide: - Runtime Resolution",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-023",
    "previous_temporary_key": "TMP-UXF-00-023",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Experience Runtime Goals",
    "source_context_sha256": "76f7626abb86825c0f22537f994b3c1b8a3de86ed7ccb239ae54c9d44f1cef71",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "d7c4e37de17e0807232e69d047381fc2438a79cd6b5cad5931fc3558aff83a9a",
    "source_lines": "L2613-L2691",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R023"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R023",
  "title": "The Experience Runtime must provide: - Runtime Resolution",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R024 — The Experience Runtime must provide: - Experience Inheritance

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
      "requirement_id": "UXF-00-R024",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "63a76e3f5e2cc7f52b47ab37f76608ff388fe6fa1f5d14ae8995ba2064490128"
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
        "UXF-00-R024-AC001",
        "UXF-00-R024-AC002",
        "UXF-00-R024-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R024-O001",
      "obligation_text": "The Experience Runtime must provide: - Experience Inheritance"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Experience Runtime must provide: - Experience Inheritance",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-024",
    "previous_temporary_key": "TMP-UXF-00-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Experience Runtime Goals",
    "source_context_sha256": "76f7626abb86825c0f22537f994b3c1b8a3de86ed7ccb239ae54c9d44f1cef71",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "63a76e3f5e2cc7f52b47ab37f76608ff388fe6fa1f5d14ae8995ba2064490128",
    "source_lines": "L2693-L2771",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R024"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R024",
  "title": "The Experience Runtime must provide: - Experience Inheritance",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R025 — The Experience Runtime must provide: - Safe Fallback

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
      "requirement_id": "UXF-00-R025",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "c932e030f4a15c6892039c5a0084d56433f27947b0eece118186f55ba13b62b0"
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
        "UXF-00-R025-AC001",
        "UXF-00-R025-AC002",
        "UXF-00-R025-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R025-O001",
      "obligation_text": "The Experience Runtime must provide: - Safe Fallback"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Experience Runtime must provide: - Safe Fallback",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-025",
    "previous_temporary_key": "TMP-UXF-00-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Experience Runtime Goals",
    "source_context_sha256": "76f7626abb86825c0f22537f994b3c1b8a3de86ed7ccb239ae54c9d44f1cef71",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "c932e030f4a15c6892039c5a0084d56433f27947b0eece118186f55ba13b62b0",
    "source_lines": "L2773-L2851",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R025"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R025",
  "title": "The Experience Runtime must provide: - Safe Fallback",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R026 — The Experience Runtime must provide: - Versioning

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
      "requirement_id": "UXF-00-R026",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "17c48a0414e49698fa82a54715952a883b8fcb401bd4223ef59a1b592ff7e338"
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
        "UXF-00-R026-AC001",
        "UXF-00-R026-AC002",
        "UXF-00-R026-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R026-O001",
      "obligation_text": "The Experience Runtime must provide: - Versioning"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Experience Runtime must provide: - Versioning",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-026",
    "previous_temporary_key": "TMP-UXF-00-026",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Experience Runtime Goals",
    "source_context_sha256": "76f7626abb86825c0f22537f994b3c1b8a3de86ed7ccb239ae54c9d44f1cef71",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "17c48a0414e49698fa82a54715952a883b8fcb401bd4223ef59a1b592ff7e338",
    "source_lines": "L2853-L2931",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R026"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R026",
  "title": "The Experience Runtime must provide: - Versioning",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R027 — The Experience Runtime must provide: - Preview

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
      "requirement_id": "UXF-00-R027",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "a9b848028c0c51e159a6de8ff022397631b19e4011af5bb127a0a51e668e4977"
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
        "UXF-00-R027-AC001",
        "UXF-00-R027-AC002",
        "UXF-00-R027-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R027-O001",
      "obligation_text": "The Experience Runtime must provide: - Preview"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Experience Runtime must provide: - Preview",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-027",
    "previous_temporary_key": "TMP-UXF-00-027",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Experience Runtime Goals",
    "source_context_sha256": "76f7626abb86825c0f22537f994b3c1b8a3de86ed7ccb239ae54c9d44f1cef71",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "a9b848028c0c51e159a6de8ff022397631b19e4011af5bb127a0a51e668e4977",
    "source_lines": "L2933-L3011",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R027"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R027",
  "title": "The Experience Runtime must provide: - Preview",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R028 — The Experience Runtime must provide: - Publish

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
      "requirement_id": "UXF-00-R028",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "9ea0b70f81f91cc804291d962c9bdba6ec1178bd588348aed4265b006cab9c69"
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
        "UXF-00-R028-AC001",
        "UXF-00-R028-AC002",
        "UXF-00-R028-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R028-O001",
      "obligation_text": "The Experience Runtime must provide: - Publish"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Experience Runtime must provide: - Publish",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-028",
    "previous_temporary_key": "TMP-UXF-00-028",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Experience Runtime Goals",
    "source_context_sha256": "76f7626abb86825c0f22537f994b3c1b8a3de86ed7ccb239ae54c9d44f1cef71",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "9ea0b70f81f91cc804291d962c9bdba6ec1178bd588348aed4265b006cab9c69",
    "source_lines": "L3013-L3091",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R028"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R028",
  "title": "The Experience Runtime must provide: - Publish",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R029 — The Experience Runtime must provide: - Rollback

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
      "requirement_id": "UXF-00-R029",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "8df9c94f00419f46f0ad47e4d9cc884af4b1d20b699c4bc6654062c52f51d242"
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
        "UXF-00-R029-AC001",
        "UXF-00-R029-AC002",
        "UXF-00-R029-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R029-O001",
      "obligation_text": "The Experience Runtime must provide: - Rollback"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Experience Runtime must provide: - Rollback",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-029",
    "previous_temporary_key": "TMP-UXF-00-029",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Experience Runtime Goals",
    "source_context_sha256": "76f7626abb86825c0f22537f994b3c1b8a3de86ed7ccb239ae54c9d44f1cef71",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "8df9c94f00419f46f0ad47e4d9cc884af4b1d20b699c4bc6654062c52f51d242",
    "source_lines": "L3093-L3171",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R029"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R029",
  "title": "The Experience Runtime must provide: - Rollback",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R030 — The Experience Runtime must provide: - Auditability

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
      "requirement_id": "UXF-00-R030",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "aab19848d2bc46bf37e8db5a857fbed3a07d5d52033143822cc1f9bb1b203964"
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
        "UXF-00-R030-AC001",
        "UXF-00-R030-AC002",
        "UXF-00-R030-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R030-O001",
      "obligation_text": "The Experience Runtime must provide: - Auditability"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-00-R030 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-00-R030 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-00-R030 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-00-R030-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-00-R030-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-00-R030 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Experience Runtime must provide: - Auditability",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-030",
    "previous_temporary_key": "TMP-UXF-00-030",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Experience Runtime Goals",
    "source_context_sha256": "76f7626abb86825c0f22537f994b3c1b8a3de86ed7ccb239ae54c9d44f1cef71",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "aab19848d2bc46bf37e8db5a857fbed3a07d5d52033143822cc1f9bb1b203964",
    "source_lines": "L3173-L3284",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R030"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "UXF-00-R031"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R030",
  "title": "The Experience Runtime must provide: - Auditability",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R031 — The Architectural Principles heading is a composite parent covering the named UXF principle chil…

```json
{
  "acceptance_contract": null,
  "acceptance_mechanism": null,
  "acceptance_rationale": "Composite parent coverage is satisfied only through ALL_CHILDREN; the parent is not an implementation, acceptance, scope-coverage, or criticality unit.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "STRUCTURAL_RECORD",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Architectural Principles heading is a composite parent covering the named UXF principle children and is not an atomic acceptance unit.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/UXF/UXF-00.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "20. Architectural Principles"
    },
    "deterministic_transformation": "EXPAND_RANGE_AND_CONVERT_TO_COMPOSITE_PARENT",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-031",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION",
      "C3_SOURCE_NORMALIZATION_TO_COMPOSITE"
    ],
    "previous_temporary_key": "TMP-UXF-00-031",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Architectural Principles",
    "source_context_sha256": "71d192fa479ef3e344cf99e4aefe5b668c34e24ae250df91f95329e121c994a7",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "1643d9dc2d20e8f2d8e5cd335a2b164d4104d9871e9339e0e04b093523dd8303",
    "source_fingerprint_before_c3": "1643d9dc2d20e8f2d8e5cd335a2b164d4104d9871e9339e0e04b093523dd8303",
    "source_lines": "L3286-L3385",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/UXF/UXF-00.md",
      "lines": "L601",
      "section": "20. Architectural Principles"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-00-R031"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "UXF-00-R001",
      "UXF-00-R002",
      "UXF-00-R003",
      "UXF-00-R004",
      "UXF-00-R005",
      "UXF-00-R006",
      "UXF-00-R007",
      "UXF-00-R008",
      "UXF-00-R009",
      "UXF-00-R010",
      "UXF-00-R011",
      "UXF-00-R012",
      "UXF-00-R013",
      "UXF-00-R014",
      "UXF-00-R015",
      "UXF-00-R016",
      "UXF-00-R017",
      "UXF-00-R018",
      "UXF-00-R019",
      "UXF-00-R020",
      "UXF-00-R021",
      "UXF-00-R022",
      "UXF-00-R023",
      "UXF-00-R024",
      "UXF-00-R025",
      "UXF-00-R026",
      "UXF-00-R027",
      "UXF-00-R028",
      "UXF-00-R029",
      "UXF-00-R030"
    ]
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-00-R031",
  "title": "The Architectural Principles heading is a composite parent covering the named UXF principle chil…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-001 — Experience is resolved at runtime

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-009"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-001",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "a3c5ac633024f619f3b4d92970f6532dfe1a3138c93284d8fcd1a78945661dd6"
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
        "UXF-001-AC001",
        "UXF-001-AC002",
        "UXF-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-001-O001",
      "obligation_text": "Experience is resolved at runtime"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Experience is resolved at runtime.",
  "provenance": {
    "approved_decision_contracts": {
      "P2-DEC-009": {
        "decision_id": "P2-DEC-009",
        "sections": [
          {
            "heading": "Authority and percentile",
            "items": [
              "The shared authoritative matrix belongs in UXF-00.",
              "Field/RUM thresholds use p75."
            ]
          },
          {
            "heading": "Channel budgets",
            "items": [
              "Storefront: LCP 2.5s, INP 200ms, CLS 0.10, initial JavaScript 200 KiB, initial route 800 KiB.",
              "Customer Portal: LCP 2.5s, INP 200ms, CLS 0.10, initial JavaScript 250 KiB, initial route 900 KiB.",
              "Platform Admin, Organization, and Agency Portal: LCP 2.5s, INP 200ms, CLS 0.10, initial JavaScript 300 KiB, initial route 1000 KiB.",
              "Builder: shell LCP 2.5s, ready-state INP 200ms, CLS 0.10, initial JavaScript 300 KiB with lazy editor modules, initial route 1000 KiB.",
              "Embedded SDK: host LCP regression 100ms, host INP regression 50ms, CLS contribution 0.05, SDK 75 KiB, widget 150 KiB, route transfer 300 KiB.",
              "Embedded WebView: LCP 2.5s, INP 200ms, CLS 0.10, initial JavaScript 200 KiB, initial route 800 KiB.",
              "Partner Portal is NOT_APPLICABLE_FOR_V2.3."
            ]
          },
          {
            "heading": "Measurement and governance",
            "items": [
              "Transfer budgets are compressed production transfer.",
              "Initial route includes HTML, CSS, JavaScript, font, and critical media.",
              "Default LCP asset maximum is 250 KiB.",
              "Default critical-route third-party maximum is 100 KiB unless approved.",
              "Dynamic composition cannot bypass the budget.",
              "Missing measurement is failure.",
              "RUM uses rolling 28-day p75 segmented by channel, route, mobile, desktop, and WebView.",
              "Lab uses production build, cold cache, representative data, mobile 150ms latency, 1.6Mbps down, 750Kbps up, and calibrated mid-tier CPU.",
              "At least five lab runs are required and raw evidence is stored.",
              "Critical journeys are listed per channel.",
              "An exception records metric, current/requested value, reason, expiry, owner, and approval.",
              "API latency references P2-DEC-010."
            ]
          },
          {
            "heading": "References",
            "items": [
              "https://web.dev/articles/vitals",
              "https://github.com/GoogleChrome/lighthouse/blob/main/docs/throttling.md"
            ]
          }
        ],
        "selected_option": 1,
        "status": "DECIDED_PENDING_PACK_APPROVAL",
        "title": "Authoritative UX performance budgets"
      }
    },
    "approved_decisions": [
      "P2-DEC-009"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-001",
    "source_context_sha256": "021be5ae21231270a667ec286bef8624733b0268a88e1d9cc2ebb3e052e44394",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "a3c5ac633024f619f3b4d92970f6532dfe1a3138c93284d8fcd1a78945661dd6",
    "source_lines": "L3387-L3519",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-001"
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
  "stable_id": "UXF-001",
  "title": "Experience is resolved at runtime",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-002 — Storefronts represent commercial experiences rather than websites

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-021",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-002",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "63505fce07882b456fbbf0d6175c3cc44ae84444b1a7a8991943795a2edf8010"
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
        "UXF-002-AC001",
        "UXF-002-AC002",
        "UXF-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-002-O001",
      "obligation_text": "Storefronts represent commercial experiences rather than websites"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Storefronts represent commercial experiences rather than websites.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-002",
    "source_context_sha256": "c8a0aa5aed237e84f7c13f941f079f890bfd9c94a79f61e2c3d3669411245f59",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "63505fce07882b456fbbf0d6175c3cc44ae84444b1a7a8991943795a2edf8010",
    "source_lines": "L3521-L3600",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-002"
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
  "stable_id": "UXF-002",
  "title": "Storefronts represent commercial experiences rather than websites",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-003 — Storefronts consume YSim Products only

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-022",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-003",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "9f11c5eb650f6180f4a17d61fd8ebb58355ed223202048c7907a5410988bb149"
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
        "UXF-003-AC001",
        "UXF-003-AC002",
        "UXF-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-003-O001",
      "obligation_text": "Storefronts consume YSim Products only"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Storefronts consume YSim Products only.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-003",
    "source_context_sha256": "6940e25ff97d8630368d2207bae3291461afe75f8490653294ec4bd7af010e6e",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "9f11c5eb650f6180f4a17d61fd8ebb58355ed223202048c7907a5410988bb149",
    "source_lines": "L3602-L3681",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-003"
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
  "stable_id": "UXF-003",
  "title": "Storefronts consume YSim Products only",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-004 — Supplier systems are internal infrastructure

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-004",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "2307b70f87304132274fdeef32aa28f27852aed794677f52b21c8a2ee81f0e46"
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
        "UXF-004-AC001",
        "UXF-004-AC002",
        "UXF-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-004-O001",
      "obligation_text": "Supplier systems are internal infrastructure"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier systems are internal infrastructure.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Supplier Isolation Principle",
    "source_context_sha256": "4f0bd9a2fc1905a2811a2245e10e7624900db78efcdb96c9c2294c049d8d9679",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "2307b70f87304132274fdeef32aa28f27852aed794677f52b21c8a2ee81f0e46",
    "source_lines": "L3683-L3762",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-004"
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
  "stable_id": "UXF-004",
  "title": "Supplier systems are internal infrastructure",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-005 — Allocation is the only capability allowed to select suppliers

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005",
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-005",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "ae6d804b21bd1d2fd7e5d3bb6db3c34a0458aa63d869c239b2e74626f0245e01"
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
        "UXF-005-AC001",
        "UXF-005-AC002",
        "UXF-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-005-O001",
      "obligation_text": "Allocation is the only capability allowed to select suppliers"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-005 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-005 does not define a recovery obligation."
    }
  },
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-028",
      "selected_disposition": "CONFIRM_CRITICAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Allocation is the only capability allowed to select suppliers.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-005",
    "source_context_sha256": "f66fac7050e3c3157876b4471cf1fa2040136c1fbf408dee24ed1c46d0a9a510",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "ae6d804b21bd1d2fd7e5d3bb6db3c34a0458aa63d869c239b2e74626f0245e01",
    "source_lines": "L3764-L3887",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-005"
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
  "stable_id": "UXF-005",
  "title": "Allocation is the only capability allowed to select suppliers",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-006 — Every runtime configuration supports inheritance

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
      "requirement_id": "UXF-006",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "65e18d2ddebf538013ffa818a6a230b60c85ed24716030cb84d14e1f457b7d59"
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
        "UXF-006-AC001",
        "UXF-006-AC002",
        "UXF-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-006-O001",
      "obligation_text": "Every runtime configuration supports inheritance"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every runtime configuration supports inheritance.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-006",
    "source_context_sha256": "80e70b5aa5c0b30d3c6cc430abd63daba1ab06103ff418dec9e3855a15a31a69",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "65e18d2ddebf538013ffa818a6a230b60c85ed24716030cb84d14e1f457b7d59",
    "source_lines": "L3889-L3964",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-006"
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
  "stable_id": "UXF-006",
  "title": "Every runtime configuration supports inheritance",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-007 — Every runtime configuration supports fallback

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
      "requirement_id": "UXF-007",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "1f70d81d70cb57b7481189cdaac2a240eaa8ce2542d35f57ad3de9b446105624"
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
        "UXF-007-AC001",
        "UXF-007-AC002",
        "UXF-007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-007-O001",
      "obligation_text": "Every runtime configuration supports fallback"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every runtime configuration supports fallback.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-007",
    "source_context_sha256": "f8ed2e693bb1e04a4ca033eb938dcfc31576565f9a7d4f950750bff0cb02a30c",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "1f70d81d70cb57b7481189cdaac2a240eaa8ce2542d35f57ad3de9b446105624",
    "source_lines": "L3966-L4041",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-007"
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
  "stable_id": "UXF-007",
  "title": "Every runtime configuration supports fallback",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-008 — Localization defines customer experience, not only language

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008"
      ],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-023",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-008",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "86cce49bd9292f723ecdbc9439e9a1169feadf2721b502d51281d32bd855586f"
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
        "UXF-008-AC001",
        "UXF-008-AC002",
        "UXF-008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-008-O001",
      "obligation_text": "Localization defines customer experience, not only language"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Localization defines customer experience, not only language.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-008",
    "source_context_sha256": "abd7673b8343b2428339e25d6cf0102b3fdfaa6f8913613413fd5ce6366f185e",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "86cce49bd9292f723ecdbc9439e9a1169feadf2721b502d51281d32bd855586f",
    "source_lines": "L4043-L4126",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-008"
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
  "stable_id": "UXF-008",
  "title": "Localization defines customer experience, not only language",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-009 — Tracking participates in experience generation

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
      "requirement_id": "UXF-009",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "6dc52f0e0722d4adb04c226f286eb265417f38a2832e013eaf031bafb671c415"
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
        "UXF-009-AC001",
        "UXF-009-AC002",
        "UXF-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-009-O001",
      "obligation_text": "Tracking participates in experience generation"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Tracking participates in experience generation.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "14. Tracking Context",
    "source_context_sha256": "54cd724c09d3481deab71ae3d4e2a735a3647620e0f884d2f1d5778dd32b84ef",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "6dc52f0e0722d4adb04c226f286eb265417f38a2832e013eaf031bafb671c415",
    "source_lines": "L4128-L4203",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-009"
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
  "stable_id": "UXF-009",
  "title": "Tracking participates in experience generation",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-010 — Every published storefront must pass business binding validation

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Draft preview may expose incomplete bindings but cannot become published"
    ],
    "concrete_bindings": [
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "UXF-010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                "source_type": "SOURCE_LITERAL",
                "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
              },
              "identifier": "UXF-010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                "source_lines": "L657-L660",
                "source_section": "20. Architectural Principles > UXF-010"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.UXF-010.UXF-010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
            "source_lines": "L657-L660",
            "source_section": "20. Architectural Principles > UXF-010"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "UXF-010.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                "source_type": "SOURCE_LITERAL",
                "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
              },
              "identifier": "UXF-010.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                "source_lines": "L657-L660",
                "source_section": "20. Architectural Principles > UXF-010"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.UXF-010.UXF-010.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
            "source_lines": "L657-L660",
            "source_section": "20. Architectural Principles > UXF-010"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
            "source_type": "SOURCE_LITERAL",
            "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
          },
          "identifier": "UXF-010.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
            "source_lines": "L657-L660",
            "source_section": "20. Architectural Principles > UXF-010"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.UXF-010.UXF-010.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
            "source_type": "SOURCE_LITERAL",
            "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
          },
          "identifier": "UXF-010.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
            "source_lines": "L657-L660",
            "source_section": "20. Architectural Principles > UXF-010"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.UXF-010.UXF-010.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
            "source_type": "SOURCE_LITERAL",
            "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
          },
          "identifier": "UXF-010.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
            "source_lines": "L657-L660",
            "source_section": "20. Architectural Principles > UXF-010"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.UXF-010.UXF-010.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
            "source_type": "SOURCE_LITERAL",
            "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
          },
          "identifier": "UXF-010.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
            "source_lines": "L657-L660",
            "source_section": "20. Architectural Principles > UXF-010"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.UXF-010.UXF-010.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
            "source_type": "SOURCE_LITERAL",
            "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
          },
          "identifier": "UXF-010.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
            "source_lines": "L657-L660",
            "source_section": "20. Architectural Principles > UXF-010"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.UXF-010.UXF-010.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.UXF-010",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Storefront publishes with a missing, dangling or invalid required binding"
    ],
    "operator_composition": [
      "REFERENCE_TARGET_VALID"
    ],
    "positive_oracle": [
      "Publication succeeds only after all required business bindings validate"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
      "source_lines": "L657-L660",
      "source_section": "20. Architectural Principles > UXF-010"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
          "source_type": "SOURCE_LITERAL",
          "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
        },
        "identifier": "UXF-010.UXF-010.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "UXF-010.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/UXF/UXF-00.md",
          "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
          "source_lines": "L657-L660",
          "source_section": "20. Architectural Principles > UXF-010"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.UXF-010.UXF-010.UXF-010.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "UXF-010.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.STOREFRONT_ID",
        "FIELD.BINDING_IDS",
        "FIELD.BINDING_VALIDATION_RESULTS",
        "FIELD.PUBLISH_STATE",
        "FIELD.PUBLISH_AUDIT"
      ],
      "producer": "UXF-010.EVIDENCE.PRODUCER",
      "required_collection_origin": "UXF-010.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.STOREFRONT_ID",
        "FIELD.BINDING_IDS",
        "FIELD.BINDING_VALIDATION_RESULTS",
        "FIELD.PUBLISH_STATE",
        "FIELD.PUBLISH_AUDIT"
      ],
      "required_values_or_hashes": [
        "UXF-010.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "UXF-010.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "UXF-010.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "UXF-010-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID",
          "evaluator_consumed_bindings": [
            "allowed_lifecycle_states",
            "allowed_states",
            "reference",
            "registry",
            "registry_source",
            "target_id",
            "target_type"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
              "source_type": "SOURCE_LITERAL",
              "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
            },
            "identifier": "UXF-010.UXF-010.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/UXF/UXF-00.md",
              "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
              "source_lines": "L657-L660",
              "source_section": "20. Architectural Principles > UXF-010"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.UXF-010.UXF-010.UXF-010.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
              "source_type": "SOURCE_LITERAL",
              "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
            },
            "identifier": "UXF-010.UXF-010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/UXF/UXF-00.md",
              "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
              "source_lines": "L657-L660",
              "source_section": "20. Architectural Principles > UXF-010"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.UXF-010.UXF-010.UXF-010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "REFERENCE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "allowed_lifecycle_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "UXF-010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                      "source_type": "SOURCE_LITERAL",
                      "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
                    },
                    "identifier": "UXF-010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/UXF/UXF-00.md",
                      "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                      "source_lines": "L657-L660",
                      "source_section": "20. Architectural Principles > UXF-010"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.UXF-010.UXF-010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                  "source_lines": "L657-L660",
                  "source_section": "20. Architectural Principles > UXF-010"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "UXF-010.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                      "source_type": "SOURCE_LITERAL",
                      "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
                    },
                    "identifier": "UXF-010.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/UXF/UXF-00.md",
                      "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                      "source_lines": "L657-L660",
                      "source_section": "20. Architectural Principles > UXF-010"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.UXF-010.UXF-010.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                  "source_lines": "L657-L660",
                  "source_section": "20. Architectural Principles > UXF-010"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
                },
                "identifier": "UXF-010.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                  "source_lines": "L657-L660",
                  "source_section": "20. Architectural Principles > UXF-010"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.UXF-010.UXF-010.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
                },
                "identifier": "UXF-010.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                  "source_lines": "L657-L660",
                  "source_section": "20. Architectural Principles > UXF-010"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.UXF-010.UXF-010.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
                },
                "identifier": "UXF-010.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                  "source_lines": "L657-L660",
                  "source_section": "20. Architectural Principles > UXF-010"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.UXF-010.UXF-010.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
                },
                "identifier": "UXF-010.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                  "source_lines": "L657-L660",
                  "source_section": "20. Architectural Principles > UXF-010"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.UXF-010.UXF-010.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
                },
                "identifier": "UXF-010.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                  "source_lines": "L657-L660",
                  "source_section": "20. Architectural Principles > UXF-010"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.UXF-010.UXF-010.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
                },
                "identifier": "UXF-010.UXF-010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                  "source_lines": "L657-L660",
                  "source_section": "20. Architectural Principles > UXF-010"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.UXF-010.UXF-010.UXF-010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
                },
                "identifier": "UXF-010.UXF-010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                  "source_lines": "L657-L660",
                  "source_section": "20. Architectural Principles > UXF-010"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.UXF-010.UXF-010.UXF-010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                "source_type": "SOURCE_LITERAL",
                "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
              },
              "identifier": "UXF-010.UXF-010.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                "source_lines": "L657-L660",
                "source_section": "20. Architectural Principles > UXF-010"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.UXF-010.UXF-010.UXF-010.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "UXF-010-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
              "source_type": "SOURCE_LITERAL",
              "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
            },
            "identifier": "UXF-010.UXF-010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/UXF/UXF-00.md",
              "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
              "source_lines": "L657-L660",
              "source_section": "20. Architectural Principles > UXF-010"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.UXF-010.UXF-010.UXF-010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "REFERENCE_ID"
          },
          "operator_id": "REFERENCE_TARGET_VALID",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "allowed_lifecycle_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "UXF-010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                    "source_type": "SOURCE_LITERAL",
                    "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
                  },
                  "identifier": "UXF-010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/UXF/UXF-00.md",
                    "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                    "source_lines": "L657-L660",
                    "source_section": "20. Architectural Principles > UXF-010"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.UXF-010.UXF-010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                "source_lines": "L657-L660",
                "source_section": "20. Architectural Principles > UXF-010"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "UXF-010.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                    "source_type": "SOURCE_LITERAL",
                    "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
                  },
                  "identifier": "UXF-010.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/UXF/UXF-00.md",
                    "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                    "source_lines": "L657-L660",
                    "source_section": "20. Architectural Principles > UXF-010"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.UXF-010.UXF-010.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                "source_lines": "L657-L660",
                "source_section": "20. Architectural Principles > UXF-010"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                "source_type": "SOURCE_LITERAL",
                "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
              },
              "identifier": "UXF-010.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                "source_lines": "L657-L660",
                "source_section": "20. Architectural Principles > UXF-010"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.UXF-010.UXF-010.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                "source_type": "SOURCE_LITERAL",
                "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
              },
              "identifier": "UXF-010.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                "source_lines": "L657-L660",
                "source_section": "20. Architectural Principles > UXF-010"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.UXF-010.UXF-010.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                "source_type": "SOURCE_LITERAL",
                "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
              },
              "identifier": "UXF-010.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                "source_lines": "L657-L660",
                "source_section": "20. Architectural Principles > UXF-010"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.UXF-010.UXF-010.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                "source_type": "SOURCE_LITERAL",
                "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
              },
              "identifier": "UXF-010.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                "source_lines": "L657-L660",
                "source_section": "20. Architectural Principles > UXF-010"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.UXF-010.UXF-010.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
                "source_type": "SOURCE_LITERAL",
                "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
              },
              "identifier": "UXF-010.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-010.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
                "source_lines": "L657-L660",
                "source_section": "20. Architectural Principles > UXF-010"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.UXF-010.UXF-010.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        }
      ],
      "boundary_cases": [
        "Draft preview may expose incomplete bindings but cannot become published"
      ],
      "contract_ast_sha256": "a72fcd0d8c02220d8c303df6bc7b6e2aa70c283ffba08a8740c4731345f26806",
      "contract_id": "P2C.C4.CONTRACT.UXF-010",
      "criticality": "HIGH",
      "disposition": "OPERATOR_REMAP_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-010",
            "source_type": "SOURCE_LITERAL",
            "version": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc"
          },
          "identifier": "UXF-010.UXF-010.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-010.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
            "source_lines": "L657-L660",
            "source_section": "20. Architectural Principles > UXF-010"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.UXF-010.UXF-010.UXF-010.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "UXF-010.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.STOREFRONT_ID",
          "FIELD.BINDING_IDS",
          "FIELD.BINDING_VALIDATION_RESULTS",
          "FIELD.PUBLISH_STATE",
          "FIELD.PUBLISH_AUDIT"
        ],
        "producer": "UXF-010.EVIDENCE.PRODUCER",
        "required_collection_origin": "UXF-010.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.STOREFRONT_ID",
          "FIELD.BINDING_IDS",
          "FIELD.BINDING_VALIDATION_RESULTS",
          "FIELD.PUBLISH_STATE",
          "FIELD.PUBLISH_AUDIT"
        ],
        "required_values_or_hashes": [
          "UXF-010.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "UXF-010.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "UXF-010.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-8AB32E29CBB360F60B81",
        "P2C-C4-FX-9FEF0F3B6B1740C1AABF",
        "P2C-C4-FX-32B14AF861DCC2F2E211"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Storefront publishes with a missing, dangling or invalid required binding"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "UXF-010-O001",
          "obligation_text": "Every published storefront must pass business binding validation"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "UXF-010.O1.1.REFERENCE_TARGET_VALID"
          ],
          "coverage_count": 1,
          "obligation_id": "UXF-010-O001"
        }
      ],
      "operator_composition": [
        "REFERENCE_TARGET_VALID"
      ],
      "positive_oracles": [
        "Publication succeeds only after all required business bindings validate"
      ],
      "preconditions": [
        "Required business bindings and referenced canonical objects exist"
      ],
      "prohibitions": [
        "Storefront publishes with a missing, dangling or invalid required binding"
      ],
      "requirement_id": "UXF-010",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/UXF/UXF-00.md",
        "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
        "source_lines": "L657-L660",
        "source_section": "20. Architectural Principles > UXF-010"
      },
      "source_statement": "Every published storefront must pass business binding validation.",
      "surrounding_source_context": "### UXF-010\n\nEvery published storefront must pass business binding validation.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.UXF-010",
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
        "UXF-010-AC001",
        "UXF-010-AC002",
        "UXF-010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-010-O001",
      "obligation_text": "Every published storefront must pass business binding validation"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every published storefront must pass business binding validation.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-010",
    "source_context_sha256": "ed38d445deb7190118fc9f8317ae795c503634c174a6fa288375efc372dc46a1",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "cd104e5cbf6dcfbedf7085b6d45ad9733301d29951177d239a8409130e1ef3c9",
    "source_lines": "L4205-L5554",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-010"
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
  "stable_id": "UXF-010",
  "title": "Every published storefront must pass business binding validation",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-011 — Runtime rendering must use published snapshots

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Preview may use draft state; public runtime remains on published Snapshot"
    ],
    "concrete_bindings": [
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "UXF-011.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                "source_type": "SOURCE_LITERAL",
                "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
              },
              "identifier": "UXF-011.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                "source_lines": "L663-L666",
                "source_section": "20. Architectural Principles > UXF-011"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.UXF-011.UXF-011.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
            "source_lines": "L663-L666",
            "source_section": "20. Architectural Principles > UXF-011"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "UXF-011.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                "source_type": "SOURCE_LITERAL",
                "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
              },
              "identifier": "UXF-011.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                "source_lines": "L663-L666",
                "source_section": "20. Architectural Principles > UXF-011"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.UXF-011.UXF-011.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
            "source_lines": "L663-L666",
            "source_section": "20. Architectural Principles > UXF-011"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
            "source_type": "SOURCE_LITERAL",
            "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
          },
          "identifier": "UXF-011.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
            "source_lines": "L663-L666",
            "source_section": "20. Architectural Principles > UXF-011"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.UXF-011.UXF-011.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
            "source_type": "SOURCE_LITERAL",
            "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
          },
          "identifier": "UXF-011.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
            "source_lines": "L663-L666",
            "source_section": "20. Architectural Principles > UXF-011"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.UXF-011.UXF-011.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
            "source_type": "SOURCE_LITERAL",
            "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
          },
          "identifier": "UXF-011.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
            "source_lines": "L663-L666",
            "source_section": "20. Architectural Principles > UXF-011"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.UXF-011.UXF-011.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
            "source_type": "SOURCE_LITERAL",
            "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
          },
          "identifier": "UXF-011.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
            "source_lines": "L663-L666",
            "source_section": "20. Architectural Principles > UXF-011"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.UXF-011.UXF-011.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
            "source_type": "SOURCE_LITERAL",
            "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
          },
          "identifier": "UXF-011.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
            "source_lines": "L663-L666",
            "source_section": "20. Architectural Principles > UXF-011"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.UXF-011.UXF-011.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.UXF-011",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Runtime renders mutable draft or authoring state"
    ],
    "operator_composition": [
      "REFERENCE_TARGET_VALID"
    ],
    "positive_oracle": [
      "Runtime rendering uses the published Snapshot"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
      "source_lines": "L663-L666",
      "source_section": "20. Architectural Principles > UXF-011"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
          "source_type": "SOURCE_LITERAL",
          "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
        },
        "identifier": "UXF-011.UXF-011.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "UXF-011.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/UXF/UXF-00.md",
          "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
          "source_lines": "L663-L666",
          "source_section": "20. Architectural Principles > UXF-011"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.UXF-011.UXF-011.UXF-011.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "UXF-011.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.STOREFRONT_ID",
        "FIELD.PUBLISHED_SNAPSHOT_ID",
        "FIELD.RUNTIME_SOURCE_ID",
        "FIELD.RENDER_RESULT"
      ],
      "producer": "UXF-011.EVIDENCE.PRODUCER",
      "required_collection_origin": "UXF-011.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.STOREFRONT_ID",
        "FIELD.PUBLISHED_SNAPSHOT_ID",
        "FIELD.RUNTIME_SOURCE_ID",
        "FIELD.RENDER_RESULT"
      ],
      "required_values_or_hashes": [
        "UXF-011.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "UXF-011.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "UXF-011.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "UXF-011-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID",
          "evaluator_consumed_bindings": [
            "allowed_lifecycle_states",
            "allowed_states",
            "reference",
            "registry",
            "registry_source",
            "target_id",
            "target_type"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
              "source_type": "SOURCE_LITERAL",
              "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
            },
            "identifier": "UXF-011.UXF-011.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/UXF/UXF-00.md",
              "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
              "source_lines": "L663-L666",
              "source_section": "20. Architectural Principles > UXF-011"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.UXF-011.UXF-011.UXF-011.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
              "source_type": "SOURCE_LITERAL",
              "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
            },
            "identifier": "UXF-011.UXF-011.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/UXF/UXF-00.md",
              "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
              "source_lines": "L663-L666",
              "source_section": "20. Architectural Principles > UXF-011"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.UXF-011.UXF-011.UXF-011.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "REFERENCE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "allowed_lifecycle_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "UXF-011.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                      "source_type": "SOURCE_LITERAL",
                      "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
                    },
                    "identifier": "UXF-011.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/UXF/UXF-00.md",
                      "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                      "source_lines": "L663-L666",
                      "source_section": "20. Architectural Principles > UXF-011"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.UXF-011.UXF-011.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                  "source_lines": "L663-L666",
                  "source_section": "20. Architectural Principles > UXF-011"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "UXF-011.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                      "source_type": "SOURCE_LITERAL",
                      "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
                    },
                    "identifier": "UXF-011.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/UXF/UXF-00.md",
                      "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                      "source_lines": "L663-L666",
                      "source_section": "20. Architectural Principles > UXF-011"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.UXF-011.UXF-011.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                  "source_lines": "L663-L666",
                  "source_section": "20. Architectural Principles > UXF-011"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                  "source_type": "SOURCE_LITERAL",
                  "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
                },
                "identifier": "UXF-011.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                  "source_lines": "L663-L666",
                  "source_section": "20. Architectural Principles > UXF-011"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.UXF-011.UXF-011.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                  "source_type": "SOURCE_LITERAL",
                  "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
                },
                "identifier": "UXF-011.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                  "source_lines": "L663-L666",
                  "source_section": "20. Architectural Principles > UXF-011"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.UXF-011.UXF-011.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                  "source_type": "SOURCE_LITERAL",
                  "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
                },
                "identifier": "UXF-011.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                  "source_lines": "L663-L666",
                  "source_section": "20. Architectural Principles > UXF-011"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.UXF-011.UXF-011.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                  "source_type": "SOURCE_LITERAL",
                  "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
                },
                "identifier": "UXF-011.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                  "source_lines": "L663-L666",
                  "source_section": "20. Architectural Principles > UXF-011"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.UXF-011.UXF-011.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                  "source_type": "SOURCE_LITERAL",
                  "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
                },
                "identifier": "UXF-011.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                  "source_lines": "L663-L666",
                  "source_section": "20. Architectural Principles > UXF-011"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.UXF-011.UXF-011.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                  "source_type": "SOURCE_LITERAL",
                  "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
                },
                "identifier": "UXF-011.UXF-011.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                  "source_lines": "L663-L666",
                  "source_section": "20. Architectural Principles > UXF-011"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.UXF-011.UXF-011.UXF-011.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                  "source_type": "SOURCE_LITERAL",
                  "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
                },
                "identifier": "UXF-011.UXF-011.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-00.md",
                  "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                  "source_lines": "L663-L666",
                  "source_section": "20. Architectural Principles > UXF-011"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.UXF-011.UXF-011.UXF-011.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                "source_type": "SOURCE_LITERAL",
                "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
              },
              "identifier": "UXF-011.UXF-011.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                "source_lines": "L663-L666",
                "source_section": "20. Architectural Principles > UXF-011"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.UXF-011.UXF-011.UXF-011.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "UXF-011-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
              "source_type": "SOURCE_LITERAL",
              "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
            },
            "identifier": "UXF-011.UXF-011.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/UXF/UXF-00.md",
              "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
              "source_lines": "L663-L666",
              "source_section": "20. Architectural Principles > UXF-011"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.UXF-011.UXF-011.UXF-011.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "REFERENCE_ID"
          },
          "operator_id": "REFERENCE_TARGET_VALID",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "allowed_lifecycle_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "UXF-011.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                    "source_type": "SOURCE_LITERAL",
                    "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
                  },
                  "identifier": "UXF-011.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/UXF/UXF-00.md",
                    "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                    "source_lines": "L663-L666",
                    "source_section": "20. Architectural Principles > UXF-011"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.UXF-011.UXF-011.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                "source_lines": "L663-L666",
                "source_section": "20. Architectural Principles > UXF-011"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "UXF-011.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                    "source_type": "SOURCE_LITERAL",
                    "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
                  },
                  "identifier": "UXF-011.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/UXF/UXF-00.md",
                    "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                    "source_lines": "L663-L666",
                    "source_section": "20. Architectural Principles > UXF-011"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.UXF-011.UXF-011.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                "source_lines": "L663-L666",
                "source_section": "20. Architectural Principles > UXF-011"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                "source_type": "SOURCE_LITERAL",
                "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
              },
              "identifier": "UXF-011.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                "source_lines": "L663-L666",
                "source_section": "20. Architectural Principles > UXF-011"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.UXF-011.UXF-011.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                "source_type": "SOURCE_LITERAL",
                "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
              },
              "identifier": "UXF-011.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                "source_lines": "L663-L666",
                "source_section": "20. Architectural Principles > UXF-011"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.UXF-011.UXF-011.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                "source_type": "SOURCE_LITERAL",
                "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
              },
              "identifier": "UXF-011.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                "source_lines": "L663-L666",
                "source_section": "20. Architectural Principles > UXF-011"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.UXF-011.UXF-011.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                "source_type": "SOURCE_LITERAL",
                "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
              },
              "identifier": "UXF-011.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                "source_lines": "L663-L666",
                "source_section": "20. Architectural Principles > UXF-011"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.UXF-011.UXF-011.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
                "source_type": "SOURCE_LITERAL",
                "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
              },
              "identifier": "UXF-011.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-011.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/UXF/UXF-00.md",
                "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
                "source_lines": "L663-L666",
                "source_section": "20. Architectural Principles > UXF-011"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.UXF-011.UXF-011.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        }
      ],
      "boundary_cases": [
        "Preview may use draft state; public runtime remains on published Snapshot"
      ],
      "contract_ast_sha256": "d78bd0809b5f003eb98ee6e9abaaabfbabc581ce078a54b42bae509aa42c57c4",
      "contract_id": "P2C.C4.CONTRACT.UXF-011",
      "criticality": "NORMAL",
      "disposition": "OPERATOR_REMAP_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-00.md#20. Architectural Principles > UXF-011",
            "source_type": "SOURCE_LITERAL",
            "version": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7"
          },
          "identifier": "UXF-011.UXF-011.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-011.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/UXF/UXF-00.md",
            "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
            "source_lines": "L663-L666",
            "source_section": "20. Architectural Principles > UXF-011"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.UXF-011.UXF-011.UXF-011.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "UXF-011.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.STOREFRONT_ID",
          "FIELD.PUBLISHED_SNAPSHOT_ID",
          "FIELD.RUNTIME_SOURCE_ID",
          "FIELD.RENDER_RESULT"
        ],
        "producer": "UXF-011.EVIDENCE.PRODUCER",
        "required_collection_origin": "UXF-011.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.STOREFRONT_ID",
          "FIELD.PUBLISHED_SNAPSHOT_ID",
          "FIELD.RUNTIME_SOURCE_ID",
          "FIELD.RENDER_RESULT"
        ],
        "required_values_or_hashes": [
          "UXF-011.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "UXF-011.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "UXF-011.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-2ADEBEC643D8FE33B499",
        "P2C-C4-FX-730915F92E43E570C395",
        "P2C-C4-FX-59B43E749E3F81E04429"
      ],
      "high_risk_audit_subset": false,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Runtime renders mutable draft or authoring state"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "UXF-011-O001",
          "obligation_text": "Runtime rendering must use published snapshots"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "UXF-011.O1.1.REFERENCE_TARGET_VALID"
          ],
          "coverage_count": 1,
          "obligation_id": "UXF-011-O001"
        }
      ],
      "operator_composition": [
        "REFERENCE_TARGET_VALID"
      ],
      "positive_oracles": [
        "Runtime rendering uses the published Snapshot"
      ],
      "preconditions": [
        "A published Storefront Snapshot is resolved"
      ],
      "prohibitions": [
        "Runtime renders mutable draft or authoring state"
      ],
      "requirement_id": "UXF-011",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/UXF/UXF-00.md",
        "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
        "source_lines": "L663-L666",
        "source_section": "20. Architectural Principles > UXF-011"
      },
      "source_statement": "Runtime rendering must use published snapshots.",
      "surrounding_source_context": "### UXF-011\n\nRuntime rendering must use published snapshots.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.UXF-011",
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
        "UXF-011-AC001",
        "UXF-011-AC002",
        "UXF-011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-011-O001",
      "obligation_text": "Runtime rendering must use published snapshots"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Runtime rendering must use published snapshots.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-011",
    "source_context_sha256": "7c0ef2c1dad3af2dc6b43cbf3ba331259204345c1cc0515a0920441f0dd53e35",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "9445290eaf31654edac7e2c758bf11ef5c938aa98eb54988843cf0718d17b0bd",
    "source_lines": "L5556-L6901",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-011"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-011",
  "title": "Runtime rendering must use published snapshots",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-012 — Design System components are shared across every portal

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
      "requirement_id": "UXF-012",
      "source_document": "docs/UXF/UXF-00.md",
      "source_fingerprint": "8c48c00ebf272ac978132828bfb82a8ae07ae488e23126c39f3373076d6e2353"
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
        "UXF-012-AC001",
        "UXF-012-AC002",
        "UXF-012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-012-O001",
      "obligation_text": "Design System components are shared across every portal"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Design System components are shared across every portal.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-012",
    "source_context_sha256": "ddf4b1f408cba50a83d3478401af65e794d89e0c346315c1ea30a8e124edad1e",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "8c48c00ebf272ac978132828bfb82a8ae07ae488e23126c39f3373076d6e2353",
    "source_lines": "L6903-L6978",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-012"
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
  "stable_id": "UXF-012",
  "title": "Design System components are shared across every portal",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
