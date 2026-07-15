---
document_code: "UXF-00"
title: "User Experience Foundation Overview"
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

## v2.3 normative requirement appendix



<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R001 — Every Storefront must be connected to business capabilities

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R001-AC001",
      "given": "a user in the applicable channel and context for Every Storefront must be connected to business capabilities",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-00-R001-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R001-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every Storefront must be connected to business capabilities",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R001-O001"
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
        "UXF-00-R001-AC001",
        "UXF-00-R001-AC002"
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
    "source_lines": "L248",
    "source_section": "7. Business Binding Principle"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R002-AC001",
      "given": "a user in the applicable channel and context for Without valid business bindings a Storefront **cannot be published**",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-00-R002-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R002-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Without valid business bindings a Storefront **cannot be published**",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R002-O001"
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
        "UXF-00-R002-AC001",
        "UXF-00-R002-AC002"
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
    "source_lines": "L262",
    "source_section": "7. Business Binding Principle"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R003-AC001",
      "given": "a user in the applicable channel and context for Storefronts never communicate with suppliers directly",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-00-R003-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R003-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Storefronts never communicate with suppliers directly",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R003-O001"
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
        "UXF-00-R003-AC001",
        "UXF-00-R003-AC002"
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
    "source_lines": "L270",
    "source_section": "8. Supplier Isolation Principle"
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
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is retained for a future baseline and is excluded from v2.3 delivery.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
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
    "source_lines": "L304",
    "source_section": "8. Supplier Isolation Principle"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R005-AC001",
      "given": "a user in the applicable channel and context for Supplier products are never exposed to: - Storefront",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-00-R005-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R005-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Supplier products are never exposed to: - Storefront",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R005-O001"
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
        "UXF-00-R005-AC001",
        "UXF-00-R005-AC002"
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
    "source_lines": "L345-L347",
    "source_section": "10. Product Principle"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R006-AC001",
      "given": "a user in the applicable channel and context for Supplier products are never exposed to: - Portal",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-00-R006-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R006-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Supplier products are never exposed to: - Portal",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R006-O001"
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
        "UXF-00-R006-AC001",
        "UXF-00-R006-AC002"
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
    "source_fingerprint": "7027a695ddd5d9408202fd923bf8ee487659aa7dd35054f6014276be6c8200d1",
    "source_lines": "L345-L348",
    "source_section": "10. Product Principle"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R007-AC001",
      "given": "a user in the applicable channel and context for Supplier products are never exposed to: - Customer",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-00-R007-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R007-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Supplier products are never exposed to: - Customer",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R007-O001"
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
        "UXF-00-R007-AC001",
        "UXF-00-R007-AC002"
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
    "source_fingerprint": "4760a88ae1d756ffb3a60c64b1c9c055e5ce81b95b6bebc6564099991f465a16",
    "source_lines": "L345-L349",
    "source_section": "10. Product Principle"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R008-AC001",
      "given": "a user in the applicable channel and context for Supplier products are never exposed to: - Agency",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-00-R008-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R008-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Supplier products are never exposed to: - Agency",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R008-O001"
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
        "UXF-00-R008-AC001",
        "UXF-00-R008-AC002"
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
    "source_fingerprint": "1d63b397beb70b24bbb22f2d6f7a00274431aca0fc1b79258a45612eef4636b5",
    "source_lines": "L345-L350",
    "source_section": "10. Product Principle"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R009-AC001",
      "given": "a user in the applicable channel and context for Supplier products are never exposed to: - Reseller",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-00-R009-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R009-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Supplier products are never exposed to: - Reseller",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R009-O001"
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
        "UXF-00-R009-AC001",
        "UXF-00-R009-AC002"
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
    "source_fingerprint": "3473749dff7b3ebeb4ae0019d80f6fc51ac2cae3b90a2067bd3b5d293115ada5",
    "source_lines": "L345-L351",
    "source_section": "10. Product Principle"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R010-AC001",
      "given": "a user in the applicable channel and context for Each level only overrides the required configuration",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-00-R010-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R010-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Each level only overrides the required configuration",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R010-O001"
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
        "UXF-00-R010-AC001",
        "UXF-00-R010-AC002"
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
    "source_lines": "L385",
    "source_section": "11. Experience Inheritance"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R011-AC001",
      "given": "a user in the applicable channel and context for Every runtime configuration must support fallback",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R011-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R011-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every runtime configuration must support fallback",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R011-O001"
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
        "UXF-00-R011-AC001",
        "UXF-00-R011-AC002"
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
    "source_lines": "L393",
    "source_section": "12. Fallback Experience"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R012-AC001",
      "given": "a user in the applicable channel and context for If a configuration cannot be resolved, the runtime automatically falls back to the nearest valid…",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R012-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_INHERITANCE_FAILURE_V1",
      "criterion_id": "UXF-00-R012-AC002",
      "given": "a child experience with no local value and an invalid or unavailable parent configuration for If a configuration cannot be resolved, the runtime automatically falls back to the nearest valid…",
      "observable_evidence": "child and parent configuration identities, resolution trace, fallback or failure result, and rendered value",
      "then": "resolution produces the declared deterministic fallback or a visible configuration failure and never renders an unexplained value",
      "verifies": [
        "UXF-00-R012-O001"
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
        "UXF-00-R012-AC001",
        "UXF-00-R012-AC002"
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
    "source_lines": "L409",
    "source_section": "12. Fallback Experience"
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
  "stable_id": "UXF-00-R012",
  "title": "If a configuration cannot be resolved, the runtime automatically falls back to the nearest valid…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R013 — No runtime request should fail solely because a child configuration is incomplete

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R013-AC001",
      "given": "a user in the applicable channel and context for No runtime request should fail solely because a child configuration is incomplete",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R013-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R013-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for No runtime request should fail solely because a child configuration is incomplete",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R013-O001"
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
        "UXF-00-R013-AC001",
        "UXF-00-R013-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R013-O001",
      "obligation_text": "No runtime request should fail solely because a child configuration is incomplete"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "No runtime request should fail solely because a child configuration is incomplete.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-013",
    "previous_temporary_key": "TMP-UXF-00-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Fallback Experience",
    "source_context_sha256": "60b4a5e34a152d8e66574e8461c34a0296b318eea1631ec5ff334805aa9c22c3",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "1796ccb7f406176950afb115a8cf25040721fd9b6a72488039a96d92c5eadadc",
    "source_lines": "L411",
    "source_section": "12. Fallback Experience"
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
  "stable_id": "UXF-00-R013",
  "title": "No runtime request should fail solely because a child configuration is incomplete",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-00-R014 — All applications must reuse the same component library

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R014-AC001",
      "given": "a user in the applicable channel and context for All applications must reuse the same component library",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-00-R014-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R014-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for All applications must reuse the same component library",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R014-O001"
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
        "UXF-00-R014-AC001",
        "UXF-00-R014-AC002"
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
    "source_lines": "L520",
    "source_section": "16. Design System Principle"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R015-AC001",
      "given": "a user in the applicable channel and context for UI duplication is prohibited",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-00-R015-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R015-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for UI duplication is prohibited",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R015-O001"
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
        "UXF-00-R015-AC001",
        "UXF-00-R015-AC002"
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
    "source_lines": "L522",
    "source_section": "16. Design System Principle"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "UXF-00-R016-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by White-label configuration must not require source-code modification",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance evidence identifies the governing configuration and shows that an approved configuration change alters the governed result without a source-code variant",
      "verifies": [
        "UXF-00-R016-O001"
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
        "UXF-00-R016-AC001"
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
    "source_fingerprint": "1dc2c699486bee6347757e644f608b7f9a467ee7e815d2d25b43ccae84f4e046",
    "source_lines": "L542",
    "source_section": "17. White-label Principle"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R017-AC001",
      "given": "a user in the applicable channel and context for Runtime rendering must use immutable published configurations",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R017-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R017-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Runtime rendering must use immutable published configurations",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R017-O001"
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
        "UXF-00-R017-AC001",
        "UXF-00-R017-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R017-O001",
      "obligation_text": "Runtime rendering must use immutable published configurations"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-00-R017 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-00-R017 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-00-R017 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "UXF-00-R017 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-00-R017-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-00-R017 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L548",
    "source_section": "18. Published Experience Snapshot"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R018-AC001",
      "given": "a user in the applicable channel and context for The runtime never renders directly from editable configurations",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R018-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R018-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The runtime never renders directly from editable configurations",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R018-O001"
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
        "UXF-00-R018-AC001",
        "UXF-00-R018-AC002"
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
    "source_lines": "L576",
    "source_section": "18. Published Experience Snapshot"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R019-AC001",
      "given": "a user in the applicable channel and context for The Experience Runtime must provide: - Dynamic Rendering",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R019-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R019-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Experience Runtime must provide: - Dynamic Rendering",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R019-O001"
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
        "UXF-00-R019-AC001",
        "UXF-00-R019-AC002"
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
    "source_lines": "L582-L584",
    "source_section": "19. Experience Runtime Goals"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R020-AC001",
      "given": "a user in the applicable channel and context for The Experience Runtime must provide: - White-label Support",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R020-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R020-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Experience Runtime must provide: - White-label Support",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R020-O001"
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
        "UXF-00-R020-AC001",
        "UXF-00-R020-AC002"
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
    "source_fingerprint": "2767e9f62ee522d1790d7f0211cdc5043584b8e2f04f3ccdbc6825d9b9162210",
    "source_lines": "L582-L585",
    "source_section": "19. Experience Runtime Goals"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R021-AC001",
      "given": "a user in the applicable channel and context for The Experience Runtime must provide: - Multi-tenant Isolation",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R021-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R021-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Experience Runtime must provide: - Multi-tenant Isolation",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R021-O001"
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
        "UXF-00-R021-AC001",
        "UXF-00-R021-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R021-O001",
      "obligation_text": "The Experience Runtime must provide: - Multi-tenant Isolation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-00-R021 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-00-R021 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-00-R021 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "UXF-00-R021 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-00-R021-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-00-R021 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "230ccfef4b981f4ff5a6445fd9d1c7c531e21876b10cd5fbd3da561c36349f47",
    "source_lines": "L582-L586",
    "source_section": "19. Experience Runtime Goals"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R022-AC001",
      "given": "a user in the applicable channel and context for The Experience Runtime must provide: - Localization",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R022-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R022-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Experience Runtime must provide: - Localization",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R022-O001"
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
        "UXF-00-R022-AC001",
        "UXF-00-R022-AC002"
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
    "source_fingerprint": "465cd69038d304d0bf9e3ac91752eeb9cd61da2ec5f24121e875b998a73f5d19",
    "source_lines": "L582-L587",
    "source_section": "19. Experience Runtime Goals"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R023-AC001",
      "given": "a user in the applicable channel and context for The Experience Runtime must provide: - Runtime Resolution",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R023-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R023-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Experience Runtime must provide: - Runtime Resolution",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R023-O001"
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
        "UXF-00-R023-AC001",
        "UXF-00-R023-AC002"
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
    "source_fingerprint": "53f6bc53a974857a1069ca868f01fe7a3bde356e74eb44b4c3af8abf07613167",
    "source_lines": "L582-L588",
    "source_section": "19. Experience Runtime Goals"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R024-AC001",
      "given": "a user in the applicable channel and context for The Experience Runtime must provide: - Experience Inheritance",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R024-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_INHERITANCE_FAILURE_V1",
      "criterion_id": "UXF-00-R024-AC002",
      "given": "a child experience with no local value and an invalid or unavailable parent configuration for The Experience Runtime must provide: - Experience Inheritance",
      "observable_evidence": "child and parent configuration identities, resolution trace, fallback or failure result, and rendered value",
      "then": "resolution produces the declared deterministic fallback or a visible configuration failure and never renders an unexplained value",
      "verifies": [
        "UXF-00-R024-O001"
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
        "UXF-00-R024-AC001",
        "UXF-00-R024-AC002"
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
    "source_fingerprint": "495c00dde3635dc6b12b6752474a3ba65bf780d994ea2b644d8290bc114f5ca7",
    "source_lines": "L582-L589",
    "source_section": "19. Experience Runtime Goals"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R025-AC001",
      "given": "a user in the applicable channel and context for The Experience Runtime must provide: - Safe Fallback",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R025-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R025-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Experience Runtime must provide: - Safe Fallback",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R025-O001"
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
        "UXF-00-R025-AC001",
        "UXF-00-R025-AC002"
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
    "source_fingerprint": "a42aee046efc41909cbf43c710b2caf5d408ece5e6d1ef5feb62877b446a1915",
    "source_lines": "L582-L590",
    "source_section": "19. Experience Runtime Goals"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R026-AC001",
      "given": "a user in the applicable channel and context for The Experience Runtime must provide: - Versioning",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R026-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R026-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Experience Runtime must provide: - Versioning",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R026-O001"
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
        "UXF-00-R026-AC001",
        "UXF-00-R026-AC002"
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
    "source_fingerprint": "243a80a03f52da544798efa8139dfbb09dec404ea59d30bdd9a4459c759efeee",
    "source_lines": "L582-L591",
    "source_section": "19. Experience Runtime Goals"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R027-AC001",
      "given": "a user in the applicable channel and context for The Experience Runtime must provide: - Preview",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R027-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R027-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Experience Runtime must provide: - Preview",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R027-O001"
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
        "UXF-00-R027-AC001",
        "UXF-00-R027-AC002"
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
    "source_fingerprint": "76d77fe2e27fcaeabbd658d752b4133d859cad9513d9f426886233613e0c3e83",
    "source_lines": "L582-L592",
    "source_section": "19. Experience Runtime Goals"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R028-AC001",
      "given": "a user in the applicable channel and context for The Experience Runtime must provide: - Publish",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R028-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R028-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Experience Runtime must provide: - Publish",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R028-O001"
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
        "UXF-00-R028-AC001",
        "UXF-00-R028-AC002"
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
    "source_fingerprint": "15aac68432d6c676a917abf95e543037ab44dc78e264dd4cab31e8ebe24514a3",
    "source_lines": "L582-L593",
    "source_section": "19. Experience Runtime Goals"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R029-AC001",
      "given": "a user in the applicable channel and context for The Experience Runtime must provide: - Rollback",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-00-R029-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R029-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Experience Runtime must provide: - Rollback",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R029-O001"
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
        "UXF-00-R029-AC001",
        "UXF-00-R029-AC002"
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
    "source_fingerprint": "4d787db16d34b2a2c52364bb708dd859e801b23f6998dd91c8588e3020d129b6",
    "source_lines": "L582-L594",
    "source_section": "19. Experience Runtime Goals"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-00-R030-AC001",
      "given": "an operational task within the scope of The Experience Runtime must provide: - Auditability",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "UXF-00-R030-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "UXF-00-R030-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for The Experience Runtime must provide: - Auditability",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "UXF-00-R030-O001"
      ],
      "when": "operational verification is performed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-00-R030-AC001",
        "UXF-00-R030-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R030-O001",
      "obligation_text": "The Experience Runtime must provide: - Auditability"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-00-R030 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-00-R030 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-00-R030 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "UXF-00-R030 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-00-R030-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-00-R030 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "d71d51f2507e6f20ca54aa1676fd3ea02ca80b9c3aa290f2d2c06e9b1eadf671",
    "source_lines": "L582-L595",
    "source_section": "19. Experience Runtime Goals"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
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
### UXF-00-R031 — The following principles are mandatory

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-00-R031-AC001",
      "given": "a user in the applicable channel and context for The following principles are mandatory",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-00-R031-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-00-R031-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The following principles are mandatory",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-00-R031-O001"
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
        "UXF-00-R031-AC001",
        "UXF-00-R031-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-00-R031-O001",
      "obligation_text": "The following principles are mandatory"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The following principles are mandatory.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-00-031",
    "previous_temporary_key": "TMP-UXF-00-031",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Architectural Principles",
    "source_context_sha256": "71d192fa479ef3e344cf99e4aefe5b668c34e24ae250df91f95329e121c994a7",
    "source_document": "docs/UXF/UXF-00.md",
    "source_fingerprint": "0182d8f960d53e8fca772781b8717e634251c8e80d1e866ea5070d2da1a5a3e4",
    "source_lines": "L601",
    "source_section": "20. Architectural Principles"
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
  "stable_id": "UXF-00-R031",
  "title": "The following principles are mandatory",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-001 — Experience is resolved at runtime

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-001-AC001",
      "given": "a user in the applicable channel and context for Experience is resolved at runtime",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-001-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-001-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Experience is resolved at runtime",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-001-O001"
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
        "UXF-001-AC001",
        "UXF-001-AC002"
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
    "source_fingerprint": "8d32021ae2b08d5a1d4e299d6f470517c3a27252e20d87b72a167b8d85aa2835",
    "source_lines": "L603-L606",
    "source_section": "20. Architectural Principles > UXF-001"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-002-AC001",
      "given": "a user in the applicable channel and context for Storefronts represent commercial experiences rather than websites",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-002-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-002-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Storefronts represent commercial experiences rather than websites",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-002-O001"
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
        "UXF-002-AC001",
        "UXF-002-AC002"
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
    "source_fingerprint": "610e4f9d816853535bcc5c6689c8cd189643194b7e83a1ddddde7dc7bd228710",
    "source_lines": "L609-L612",
    "source_section": "20. Architectural Principles > UXF-002"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-003-AC001",
      "given": "a user in the applicable channel and context for Storefronts consume YSim Products only",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-003-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-003-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Storefronts consume YSim Products only",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-003-O001"
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
        "UXF-003-AC001",
        "UXF-003-AC002"
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
    "source_fingerprint": "11303a5a1dd0542d5bd3b70cb99d2448e0384fdf880a4376fb21c09caa57f2e3",
    "source_lines": "L615-L618",
    "source_section": "20. Architectural Principles > UXF-003"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-004-AC001",
      "given": "a user in the applicable channel and context for Supplier systems are internal infrastructure",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-004-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-004-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Supplier systems are internal infrastructure",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-004-O001"
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
        "UXF-004-AC001",
        "UXF-004-AC002"
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
    "source_fingerprint": "6e3423c7a536edf235fb43108173193ba26440a7282658db9d941d16cffe08f8",
    "source_lines": "L621-L624",
    "source_section": "20. Architectural Principles > UXF-004"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-005-AC001",
      "given": "a user in the applicable channel and context for Allocation is the only capability allowed to select suppliers",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-005-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-005-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Allocation is the only capability allowed to select suppliers",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-005-O001"
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
        "UXF-005-AC001",
        "UXF-005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-005-O001",
      "obligation_text": "Allocation is the only capability allowed to select suppliers"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "UXF-005 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-005-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "30012f0050e7a8e0d6f0526bd429f1451090046ce7e7c4c9099075c826642a09",
    "source_lines": "L627-L630",
    "source_section": "20. Architectural Principles > UXF-005"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-006-AC001",
      "given": "a user in the applicable channel and context for Every runtime configuration supports inheritance",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-006-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_INHERITANCE_FAILURE_V1",
      "criterion_id": "UXF-006-AC002",
      "given": "a child experience with no local value and an invalid or unavailable parent configuration for Every runtime configuration supports inheritance",
      "observable_evidence": "child and parent configuration identities, resolution trace, fallback or failure result, and rendered value",
      "then": "resolution produces the declared deterministic fallback or a visible configuration failure and never renders an unexplained value",
      "verifies": [
        "UXF-006-O001"
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
        "UXF-006-AC001",
        "UXF-006-AC002"
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
    "source_fingerprint": "52b7f40d85ecf7daad1628356d97bc4abfcf9bc8e398552363b73786076f5a72",
    "source_lines": "L633-L636",
    "source_section": "20. Architectural Principles > UXF-006"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-007-AC001",
      "given": "a user in the applicable channel and context for Every runtime configuration supports fallback",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-007-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-007-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every runtime configuration supports fallback",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-007-O001"
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
        "UXF-007-AC001",
        "UXF-007-AC002"
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
    "source_fingerprint": "545204b63308d86e7b400cd37f7f8011b20ad02b68152fc405ba5b91f11461c5",
    "source_lines": "L639-L642",
    "source_section": "20. Architectural Principles > UXF-007"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-008-AC001",
      "given": "a user in the applicable channel and context for Localization defines customer experience, not only language",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-008-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-008-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Localization defines customer experience, not only language",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-008-O001"
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
        "UXF-008-AC001",
        "UXF-008-AC002"
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
    "source_fingerprint": "20303fc4b812bc36885cb2776af43159c7f4e037effd8d05e7b7405d6f321490",
    "source_lines": "L645-L648",
    "source_section": "20. Architectural Principles > UXF-008"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-009-AC001",
      "given": "a user in the applicable channel and context for Tracking participates in experience generation",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-009-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-009-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Tracking participates in experience generation",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-009-O001"
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
        "UXF-009-AC001",
        "UXF-009-AC002"
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
    "source_fingerprint": "83d11e8292821143b357b909b1baf9b72cd1bf67f9efd35130dcdd2864f68ec3",
    "source_lines": "L651-L654",
    "source_section": "20. Architectural Principles > UXF-009"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-010-AC001",
      "given": "a user in the applicable channel and context for Every published storefront must pass business binding validation",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-010-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-010-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every published storefront must pass business binding validation",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-010-O001"
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
        "UXF-010-AC001",
        "UXF-010-AC002"
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
    "source_fingerprint": "0ae77a6f7e289ee8f57703d05ba1cef4359dd41d441e5a3220c59766d31c7dbc",
    "source_lines": "L657-L660",
    "source_section": "20. Architectural Principles > UXF-010"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "UXF-011-AC001",
      "given": "a candidate Runtime rendering must use published snapshots record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "UXF-011-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-011-AC001"
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
    "source_fingerprint": "06fee0249e722baca5f14cbfea2d508a2315fddc88b7d8ce3fd9fe56616372c7",
    "source_lines": "L663-L666",
    "source_section": "20. Architectural Principles > UXF-011"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-012-AC001",
      "given": "a user in the applicable channel and context for Design System components are shared across every portal",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-012-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-012-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Design System components are shared across every portal",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-012-O001"
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
        "UXF-012-AC001",
        "UXF-012-AC002"
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
    "source_fingerprint": "d0c1beeda198069e186cc9d1f49e4f5f942b676b58ea3f742e67a51a7898cee1",
    "source_lines": "L669-L672",
    "source_section": "20. Architectural Principles > UXF-012"
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
