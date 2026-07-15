---
document_code: "UXF-05"
title: "Experience Runtime & Commerce Runtime Integration"
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

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## v2.3 normative requirement appendix



<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R001 — The Experience Runtime never performs business decisions

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R001-AC001",
      "given": "a user in the applicable channel and context for The Experience Runtime never performs business decisions",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-05-R001-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R001-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Experience Runtime never performs business decisions",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R001-O001"
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
        "UXF-05-R001-AC001",
        "UXF-05-R001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R001-O001",
      "obligation_text": "The Experience Runtime never performs business decisions"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Experience Runtime never performs business decisions.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-001",
    "previous_temporary_key": "TMP-UXF-05-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Experience Runtime",
    "source_context_sha256": "c28fef10654829397d0317078f87d1c3b1ac30f2cc5d836c6517b5d4ac15726c",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "733718b882f2515355e9f2299431158e6c2295871e3f768dbc5e8140e8ae945c",
    "source_lines": "L66",
    "source_section": "3. Experience Runtime"
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
  "stable_id": "UXF-05-R001",
  "title": "The Experience Runtime never performs business decisions",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R002 — The Commerce Runtime never renders UI

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R002-AC001",
      "given": "a user in the applicable channel and context for The Commerce Runtime never renders UI",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-05-R002-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R002-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Commerce Runtime never renders UI",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R002-O001"
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
        "UXF-05-R002-AC001",
        "UXF-05-R002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R002-O001",
      "obligation_text": "The Commerce Runtime never renders UI"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Commerce Runtime never renders UI.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-002",
    "previous_temporary_key": "TMP-UXF-05-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Commerce Runtime",
    "source_context_sha256": "6f65baebd41ed9e60048e1aefe564f6201c714ec05c0b1afb5a09ad5220f0b5a",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "04147975e0d09a8fa24202c9a551cd2149ca9f44b3925ec915b1342209c17770",
    "source_lines": "L87",
    "source_section": "4. Commerce Runtime"
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
  "stable_id": "UXF-05-R002",
  "title": "The Commerce Runtime never renders UI",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R003 — Infrastructure never communicates directly with Storefront UI

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R003-AC001",
      "given": "a user in the applicable channel and context for Infrastructure never communicates directly with Storefront UI",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R003-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R003-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Infrastructure never communicates directly with Storefront UI",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R003-O001"
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
        "UXF-05-R003-AC001",
        "UXF-05-R003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R003-O001",
      "obligation_text": "Infrastructure never communicates directly with Storefront UI"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Infrastructure never communicates directly with Storefront UI.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-003",
    "previous_temporary_key": "TMP-UXF-05-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Infrastructure Runtime",
    "source_context_sha256": "e24a99e29fb30454c345f49421befbb01f0c38bfbe98fd229e12b0326513ea0d",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "9dfcf56ab93283cd5f49e4b1e64c814e1d6578767224a612c5bed10037f3b2af",
    "source_lines": "L104",
    "source_section": "5. Infrastructure Runtime"
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
  "stable_id": "UXF-05-R003",
  "title": "Infrastructure never communicates directly with Storefront UI",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R004 — Storefronts never own: - Products

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R004-AC001",
      "given": "a user in the applicable channel and context for Storefronts never own: - Products",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R004-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R004-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Storefronts never own: - Products",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R004-O001"
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
        "UXF-05-R004-AC001",
        "UXF-05-R004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R004-O001",
      "obligation_text": "Storefronts never own: - Products"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Storefronts never own: - Products",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-004",
    "previous_temporary_key": "TMP-UXF-05-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Storefront Responsibilities",
    "source_context_sha256": "14bd2412e8fb184033e702f38ec039b832d191a9a3cd0383a46bb7efa680146f",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "0964cb7a12e1fd74b2df7f54b52d039dd176367bcce9546fa80e626b866e7da7",
    "source_lines": "L158-L160",
    "source_section": "7. Storefront Responsibilities"
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
  "stable_id": "UXF-05-R004",
  "title": "Storefronts never own: - Products",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R005 — Storefronts never own: - Pricing

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R005-AC001",
      "given": "a user in the applicable channel and context for Storefronts never own: - Pricing",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R005-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R005-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Storefronts never own: - Pricing",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R005-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "UXF-05-R005-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Storefronts never own: - Pricing",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "UXF-05-R005-O001"
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
        "UXF-05-R005-AC001",
        "UXF-05-R005-AC002",
        "UXF-05-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R005-O001",
      "obligation_text": "Storefronts never own: - Pricing"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-05-R005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-05-R005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-05-R005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "UXF-05-R005-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-05-R005-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-05-R005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-034",
      "selected_disposition": "CONFIRM_CRITICAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Storefronts never own: - Pricing",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-005",
    "previous_temporary_key": "TMP-UXF-05-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Storefront Responsibilities",
    "source_context_sha256": "14bd2412e8fb184033e702f38ec039b832d191a9a3cd0383a46bb7efa680146f",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "f3480c9a5dc4c1a6c0ead27b5e3297d384540be5ea098e14e0536516c22fc86a",
    "source_lines": "L158-L161",
    "source_section": "7. Storefront Responsibilities"
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
  "stable_id": "UXF-05-R005",
  "title": "Storefronts never own: - Pricing",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R006 — Storefronts never own: - Supplier

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R006-AC001",
      "given": "a user in the applicable channel and context for Storefronts never own: - Supplier",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R006-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R006-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Storefronts never own: - Supplier",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R006-O001"
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
        "UXF-05-R006-AC001",
        "UXF-05-R006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R006-O001",
      "obligation_text": "Storefronts never own: - Supplier"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Storefronts never own: - Supplier",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-006",
    "previous_temporary_key": "TMP-UXF-05-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Storefront Responsibilities",
    "source_context_sha256": "14bd2412e8fb184033e702f38ec039b832d191a9a3cd0383a46bb7efa680146f",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "b71c207d10278d32b34aa6d0e4318e1e722050fa6b3b374732e9b2af50fd265a",
    "source_lines": "L158-L162",
    "source_section": "7. Storefront Responsibilities"
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
  "stable_id": "UXF-05-R006",
  "title": "Storefronts never own: - Supplier",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R007 — Storefronts never own: - Inventory

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R007-AC001",
      "given": "a user in the applicable channel and context for Storefronts never own: - Inventory",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R007-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R007-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Storefronts never own: - Inventory",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R007-O001"
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
        "UXF-05-R007-AC001",
        "UXF-05-R007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R007-O001",
      "obligation_text": "Storefronts never own: - Inventory"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Storefronts never own: - Inventory",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-007",
    "previous_temporary_key": "TMP-UXF-05-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Storefront Responsibilities",
    "source_context_sha256": "14bd2412e8fb184033e702f38ec039b832d191a9a3cd0383a46bb7efa680146f",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "c080025514c2e154f5cca29ae61d32f7c43a42e59327389f8e1b33d1f7381b5f",
    "source_lines": "L158-L163",
    "source_section": "7. Storefront Responsibilities"
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
  "stable_id": "UXF-05-R007",
  "title": "Storefronts never own: - Inventory",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R008 — Storefronts never own: - Allocation

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R008-AC001",
      "given": "a user in the applicable channel and context for Storefronts never own: - Allocation",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R008-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R008-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Storefronts never own: - Allocation",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R008-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "UXF-05-R008-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Storefronts never own: - Allocation",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "UXF-05-R008-O001"
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
        "UXF-05-R008-AC001",
        "UXF-05-R008-AC002",
        "UXF-05-R008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R008-O001",
      "obligation_text": "Storefronts never own: - Allocation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-05-R008 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-05-R008 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-05-R008 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "UXF-05-R008-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-05-R008-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-05-R008 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-035",
      "selected_disposition": "CONFIRM_CRITICAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Storefronts never own: - Allocation",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-008",
    "previous_temporary_key": "TMP-UXF-05-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Storefront Responsibilities",
    "source_context_sha256": "14bd2412e8fb184033e702f38ec039b832d191a9a3cd0383a46bb7efa680146f",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "6e33714aeda92b927f91b980160fa97c0aa5ca0c08a3f651da97a2a2c0b0e5ce",
    "source_lines": "L158-L164",
    "source_section": "7. Storefront Responsibilities"
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
  "stable_id": "UXF-05-R008",
  "title": "Storefronts never own: - Allocation",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R009 — Storefronts never own: - Fulfillment

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R009-AC001",
      "given": "a user in the applicable channel and context for Storefronts never own: - Fulfillment",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R009-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R009-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Storefronts never own: - Fulfillment",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R009-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "UXF-05-R009-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Storefronts never own: - Fulfillment",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "UXF-05-R009-O001"
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
        "UXF-05-R009-AC001",
        "UXF-05-R009-AC002",
        "UXF-05-R009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R009-O001",
      "obligation_text": "Storefronts never own: - Fulfillment"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-05-R009 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-05-R009 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-05-R009 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "UXF-05-R009-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-05-R009-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-05-R009 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-036",
      "selected_disposition": "CONFIRM_CRITICAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Storefronts never own: - Fulfillment",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-009",
    "previous_temporary_key": "TMP-UXF-05-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Storefront Responsibilities",
    "source_context_sha256": "14bd2412e8fb184033e702f38ec039b832d191a9a3cd0383a46bb7efa680146f",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "c45131205d4682ddaedcf1fbe0d65a1a8fdd6de87b19c73e57250cb459333aac",
    "source_lines": "L158-L165",
    "source_section": "7. Storefront Responsibilities"
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
  "stable_id": "UXF-05-R009",
  "title": "Storefronts never own: - Fulfillment",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R010 — The UI never queries business objects directly

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "UXF-05-R010-AC001",
      "given": "a candidate The UI never queries business objects directly record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns REJECTED when the prohibited value or relationship is present, and no rejected state is persisted",
      "verifies": [
        "UXF-05-R010-O001"
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
        "UXF-05-R010-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R010-O001",
      "obligation_text": "The UI never queries business objects directly"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The UI never queries business objects directly.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-010",
    "previous_temporary_key": "TMP-UXF-05-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Business Binding",
    "source_context_sha256": "ceb98b80bb55ca158ab4b4b934cd4c0fff93245fe366140ee6299555bb0988be",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "2b1a281b2f3efb0f4c365f346a57759559660d94095bb9a98549a079be327957",
    "source_lines": "L199",
    "source_section": "8. Business Binding"
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
  "stable_id": "UXF-05-R010",
  "title": "The UI never queries business objects directly",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R011 — Widgets never access databases

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R011-AC001",
      "given": "a user in the applicable channel and context for Widgets never access databases",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R011-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R011-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Widgets never access databases",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R011-O001"
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
        "UXF-05-R011-AC001",
        "UXF-05-R011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R011-O001",
      "obligation_text": "Widgets never access databases"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Widgets never access databases.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-011",
    "previous_temporary_key": "TMP-UXF-05-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Widget Binding",
    "source_context_sha256": "b90ab1a2f9e0ad09501d869c940e07caa14836f3ad08f9199424f95dca751398",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "82c1565e143a48cbd263114541e24d0207e57fc9b466a3c1859c8ce3dd33e88b",
    "source_lines": "L272",
    "source_section": "11. Widget Binding"
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
  "stable_id": "UXF-05-R011",
  "title": "Widgets never access databases",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R012 — Widgets never call suppliers

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R012-AC001",
      "given": "a user in the applicable channel and context for Widgets never call suppliers",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R012-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R012-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Widgets never call suppliers",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R012-O001"
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
        "UXF-05-R012-AC001",
        "UXF-05-R012-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R012-O001",
      "obligation_text": "Widgets never call suppliers"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Widgets never call suppliers.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-012",
    "previous_temporary_key": "TMP-UXF-05-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Widget Binding",
    "source_context_sha256": "b90ab1a2f9e0ad09501d869c940e07caa14836f3ad08f9199424f95dca751398",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "1fe89d430fb567338625d55c4d88261db8ce3d899cf0471a6f464af1b26fef3e",
    "source_lines": "L274",
    "source_section": "11. Widget Binding"
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
  "stable_id": "UXF-05-R012",
  "title": "Widgets never call suppliers",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R014 — Supplier objects are prohibited from appearing inside: - Storefront

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R014-AC001",
      "given": "a user in the applicable channel and context for Supplier objects are prohibited from appearing inside: - Storefront",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R014-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R014-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Supplier objects are prohibited from appearing inside: - Storefront",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R014-O001"
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
        "UXF-05-R014-AC001",
        "UXF-05-R014-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R014-O001",
      "obligation_text": "Supplier objects are prohibited from appearing inside: - Storefront"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier objects are prohibited from appearing inside: - Storefront",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-014",
    "previous_temporary_key": "TMP-UXF-05-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Supplier Isolation",
    "source_context_sha256": "dc108312936f693a85890834bd6c47790a4d45113d282193ba44fa4c9e46e84d",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "4f8ec824d3f67b9aa353ab6964b480d80d0e0881b8539e52d6771b7a436cf960",
    "source_lines": "L380-L382",
    "source_section": "15. Supplier Isolation"
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
  "stable_id": "UXF-05-R014",
  "title": "Supplier objects are prohibited from appearing inside: - Storefront",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R015 — Supplier objects are prohibited from appearing inside: - Components

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R015-AC001",
      "given": "a user in the applicable channel and context for Supplier objects are prohibited from appearing inside: - Components",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R015-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R015-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Supplier objects are prohibited from appearing inside: - Components",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R015-O001"
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
        "UXF-05-R015-AC001",
        "UXF-05-R015-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R015-O001",
      "obligation_text": "Supplier objects are prohibited from appearing inside: - Components"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier objects are prohibited from appearing inside: - Components",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-015",
    "previous_temporary_key": "TMP-UXF-05-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Supplier Isolation",
    "source_context_sha256": "dc108312936f693a85890834bd6c47790a4d45113d282193ba44fa4c9e46e84d",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "31390ad49520c609e8065f839751e26c00f41bd4bc3f894b7e85fd4600b3fc3b",
    "source_lines": "L380-L383",
    "source_section": "15. Supplier Isolation"
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
  "stable_id": "UXF-05-R015",
  "title": "Supplier objects are prohibited from appearing inside: - Components",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R016 — Supplier objects are prohibited from appearing inside: - Widgets

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R016-AC001",
      "given": "a user in the applicable channel and context for Supplier objects are prohibited from appearing inside: - Widgets",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R016-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R016-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Supplier objects are prohibited from appearing inside: - Widgets",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R016-O001"
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
        "UXF-05-R016-AC001",
        "UXF-05-R016-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R016-O001",
      "obligation_text": "Supplier objects are prohibited from appearing inside: - Widgets"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier objects are prohibited from appearing inside: - Widgets",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-016",
    "previous_temporary_key": "TMP-UXF-05-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Supplier Isolation",
    "source_context_sha256": "dc108312936f693a85890834bd6c47790a4d45113d282193ba44fa4c9e46e84d",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "16595eaf36ec62e3029f988441fe6d54e824ed83cee7dc30dae459c85c1c97bd",
    "source_lines": "L380-L384",
    "source_section": "15. Supplier Isolation"
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
  "stable_id": "UXF-05-R016",
  "title": "Supplier objects are prohibited from appearing inside: - Widgets",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R017 — Supplier objects are prohibited from appearing inside: - Pages

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R017-AC001",
      "given": "a user in the applicable channel and context for Supplier objects are prohibited from appearing inside: - Pages",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R017-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R017-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Supplier objects are prohibited from appearing inside: - Pages",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R017-O001"
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
        "UXF-05-R017-AC001",
        "UXF-05-R017-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R017-O001",
      "obligation_text": "Supplier objects are prohibited from appearing inside: - Pages"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier objects are prohibited from appearing inside: - Pages",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-017",
    "previous_temporary_key": "TMP-UXF-05-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Supplier Isolation",
    "source_context_sha256": "dc108312936f693a85890834bd6c47790a4d45113d282193ba44fa4c9e46e84d",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "780c3c984e1ad7c3de5f0358c1e79a3532aaec29cae466ee7716fe6f2dfec793",
    "source_lines": "L380-L385",
    "source_section": "15. Supplier Isolation"
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
  "stable_id": "UXF-05-R017",
  "title": "Supplier objects are prohibited from appearing inside: - Pages",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R018 — Supplier objects are prohibited from appearing inside: - Catalog

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R018-AC001",
      "given": "a user in the applicable channel and context for Supplier objects are prohibited from appearing inside: - Catalog",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R018-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R018-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Supplier objects are prohibited from appearing inside: - Catalog",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R018-O001"
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
        "UXF-05-R018-AC001",
        "UXF-05-R018-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R018-O001",
      "obligation_text": "Supplier objects are prohibited from appearing inside: - Catalog"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier objects are prohibited from appearing inside: - Catalog",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-018",
    "previous_temporary_key": "TMP-UXF-05-018",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Supplier Isolation",
    "source_context_sha256": "dc108312936f693a85890834bd6c47790a4d45113d282193ba44fa4c9e46e84d",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "d3115edecdbeb62bdde2fe7f06966406d0b9d950c0e0cdb6eb03ce2b15734f2f",
    "source_lines": "L380-L386",
    "source_section": "15. Supplier Isolation"
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
  "stable_id": "UXF-05-R018",
  "title": "Supplier objects are prohibited from appearing inside: - Catalog",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R019 — Supplier objects are prohibited from appearing inside: - Checkout

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R019-AC001",
      "given": "a user in the applicable channel and context for Supplier objects are prohibited from appearing inside: - Checkout",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R019-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R019-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Supplier objects are prohibited from appearing inside: - Checkout",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R019-O001"
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
        "UXF-05-R019-AC001",
        "UXF-05-R019-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R019-O001",
      "obligation_text": "Supplier objects are prohibited from appearing inside: - Checkout"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier objects are prohibited from appearing inside: - Checkout",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-019",
    "previous_temporary_key": "TMP-UXF-05-019",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Supplier Isolation",
    "source_context_sha256": "dc108312936f693a85890834bd6c47790a4d45113d282193ba44fa4c9e46e84d",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "20f66fa18bc637e9b852c744f2209f4a7f208cd4986d5b3ff85563463f87bb4c",
    "source_lines": "L380-L387",
    "source_section": "15. Supplier Isolation"
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
  "stable_id": "UXF-05-R019",
  "title": "Supplier objects are prohibited from appearing inside: - Checkout",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R020 — Editable configuration never participates directly

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R020-AC001",
      "given": "a user in the applicable channel and context for Editable configuration never participates directly",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-05-R020-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R020-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Editable configuration never participates directly",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R020-O001"
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
        "UXF-05-R020-AC001",
        "UXF-05-R020-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R020-O001",
      "obligation_text": "Editable configuration never participates directly"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Editable configuration never participates directly.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-020",
    "previous_temporary_key": "TMP-UXF-05-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Runtime Snapshot",
    "source_context_sha256": "82b69606bdd6b28bb2f93cd6d75ce9c1f7bfe1f1712eb0ca10bb51922e4b69a7",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "f961fd3a750d99f34881793b5b04d2227147392371e7e797be5c243eb623690b",
    "source_lines": "L482",
    "source_section": "17. Runtime Snapshot"
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
  "stable_id": "UXF-05-R020",
  "title": "Editable configuration never participates directly",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R021 — If runtime cannot resolve a binding: ``` Runtime

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R021-AC001",
      "given": "a user in the applicable channel and context for If runtime cannot resolve a binding: ``` Runtime",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-05-R021-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R021-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for If runtime cannot resolve a binding: ``` Runtime",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R021-O001"
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
        "UXF-05-R021-AC001",
        "UXF-05-R021-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R021-O001",
      "obligation_text": "If runtime cannot resolve a binding: ``` Runtime"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "If runtime cannot resolve a binding: ``` Runtime",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-021",
    "previous_temporary_key": "TMP-UXF-05-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Runtime Failure Fallback",
    "source_context_sha256": "1f402571e08efbad34e108b23aa39a1cea04849e8524589bd8cba8f2010ecfce",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "47a3a698c676bc62852961cae11cb55b5e77cb57f149704e438dd7f8f055acb1",
    "source_lines": "L514-L517",
    "source_section": "19. Runtime Failure Fallback"
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
  "stable_id": "UXF-05-R021",
  "title": "If runtime cannot resolve a binding: ``` Runtime",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R022 — Rendering should continue whenever possible

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R022-AC001",
      "given": "a user in the applicable channel and context for Rendering should continue whenever possible",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-05-R022-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R022-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Rendering should continue whenever possible",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R022-O001"
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
        "UXF-05-R022-AC001",
        "UXF-05-R022-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R022-O001",
      "obligation_text": "Rendering should continue whenever possible"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Rendering should continue whenever possible.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-022",
    "previous_temporary_key": "TMP-UXF-05-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Runtime Failure Fallback",
    "source_context_sha256": "1f402571e08efbad34e108b23aa39a1cea04849e8524589bd8cba8f2010ecfce",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "794eb82eb9e78d338ffc9d42fcc7366db07e16e6a99fbeab2e5e80665b38dba2",
    "source_lines": "L534",
    "source_section": "19. Runtime Failure Fallback"
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
  "stable_id": "UXF-05-R022",
  "title": "Rendering should continue whenever possible",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R033 — The architecture supports future extensions without changing storefront implementations

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
  "normative_statement": "The architecture supports future extensions without changing storefront implementations.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-033",
    "previous_temporary_key": "TMP-UXF-05-033",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Future Extensions",
    "source_context_sha256": "86b27df40f2e57aaa3358cd71cba0d227f148ce3a7e6c2cb236dd84b42c98303",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "021cda8048c7f55c84bc4766d8a020788feaf05e7f868a0005d88ae502d4761a",
    "source_lines": "L705",
    "source_section": "25. Future Extensions"
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
  "stable_id": "UXF-05-R033",
  "title": "The architecture supports future extensions without changing storefront implementations",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R034 — Examples include: - Additional suppliers

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
  "normative_statement": "Examples include: - Additional suppliers",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-034",
    "previous_temporary_key": "TMP-UXF-05-034",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Future Extensions",
    "source_context_sha256": "86b27df40f2e57aaa3358cd71cba0d227f148ce3a7e6c2cb236dd84b42c98303",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "4eb7a26d7eb55615edac3f66a9796f623879cc45010d14b88b0beeb44b0cb862",
    "source_lines": "L707-L709",
    "source_section": "25. Future Extensions"
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
  "stable_id": "UXF-05-R034",
  "title": "Examples include: - Additional suppliers",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R035 — Examples include: - New payment gateways

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
  "normative_statement": "Examples include: - New payment gateways",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-035",
    "previous_temporary_key": "TMP-UXF-05-035",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Future Extensions",
    "source_context_sha256": "86b27df40f2e57aaa3358cd71cba0d227f148ce3a7e6c2cb236dd84b42c98303",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "9c4579daf5a6a6f3f32764e1718d11c5e7235ca8d66c0565a6b8c12e548e9795",
    "source_lines": "L707-L710",
    "source_section": "25. Future Extensions"
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
  "stable_id": "UXF-05-R035",
  "title": "Examples include: - New payment gateways",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R036 — Examples include: - Dynamic pricing engines

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
  "normative_statement": "Examples include: - Dynamic pricing engines",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-036",
    "previous_temporary_key": "TMP-UXF-05-036",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Future Extensions",
    "source_context_sha256": "86b27df40f2e57aaa3358cd71cba0d227f148ce3a7e6c2cb236dd84b42c98303",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "95f5ae2dd5224cfc540af3ea593510f7f3e3d95bb778867031ff369dd1e1af9e",
    "source_lines": "L707-L711",
    "source_section": "25. Future Extensions"
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
  "stable_id": "UXF-05-R036",
  "title": "Examples include: - Dynamic pricing engines",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R037 — Examples include: - Recommendation engines

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-05-R037-AC001",
      "given": "a user in the applicable channel and context for Examples include: - Recommendation engines",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-05-R037-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-05-R037-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Examples include: - Recommendation engines",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-05-R037-O001"
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
        "UXF-05-R037-AC001",
        "UXF-05-R037-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R037-O001",
      "obligation_text": "Examples include: - Recommendation engines"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Examples include: - Recommendation engines",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-037",
    "previous_temporary_key": "TMP-UXF-05-037",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Future Extensions",
    "source_context_sha256": "86b27df40f2e57aaa3358cd71cba0d227f148ce3a7e6c2cb236dd84b42c98303",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "4a227e5baef5a2e8a20c14b42df32a9ade4c1e0b3d90a139d728596c3c4509f4",
    "source_lines": "L707-L712",
    "source_section": "25. Future Extensions"
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
  "stable_id": "UXF-05-R037",
  "title": "Examples include: - Recommendation engines",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R038 — Examples include: - AI-assisted personalization

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
  "normative_statement": "Examples include: - AI-assisted personalization",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-038",
    "previous_temporary_key": "TMP-UXF-05-038",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Future Extensions",
    "source_context_sha256": "86b27df40f2e57aaa3358cd71cba0d227f148ce3a7e6c2cb236dd84b42c98303",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "57822e0f8b7b68d226a981be0c6236ab902be78acbc52dd5b6d92cf3a14096cd",
    "source_lines": "L707-L713",
    "source_section": "25. Future Extensions"
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
  "stable_id": "UXF-05-R038",
  "title": "Examples include: - AI-assisted personalization",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R039 — Examples include: - Headless commerce APIs

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
  "normative_statement": "Examples include: - Headless commerce APIs",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-039",
    "previous_temporary_key": "TMP-UXF-05-039",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Future Extensions",
    "source_context_sha256": "86b27df40f2e57aaa3358cd71cba0d227f148ce3a7e6c2cb236dd84b42c98303",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "97ac3dd03c11b98317025085dfb52e67c277c927091ac5e3e9e557357465e316",
    "source_lines": "L707-L714",
    "source_section": "25. Future Extensions"
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
  "stable_id": "UXF-05-R039",
  "title": "Examples include: - Headless commerce APIs",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R040 — Examples include: - Native mobile storefronts

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
  "normative_statement": "Examples include: - Native mobile storefronts",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-040",
    "previous_temporary_key": "TMP-UXF-05-040",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Future Extensions",
    "source_context_sha256": "86b27df40f2e57aaa3358cd71cba0d227f148ce3a7e6c2cb236dd84b42c98303",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "44749d3c283991009f7e6695afcc8bd6558aadd86cd8c49b0e12d2d34d205cbf",
    "source_lines": "L707-L715",
    "source_section": "25. Future Extensions"
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
  "stable_id": "UXF-05-R040",
  "title": "Examples include: - Native mobile storefronts",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R041 — Examples include: - Partner embedded commerce

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
  "normative_statement": "Examples include: - Partner embedded commerce",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-041",
    "previous_temporary_key": "TMP-UXF-05-041",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Future Extensions",
    "source_context_sha256": "86b27df40f2e57aaa3358cd71cba0d227f148ce3a7e6c2cb236dd84b42c98303",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "2b506ceb5df44456541044d2b7cd390a338601c02d5c8442131936945cb84034",
    "source_lines": "L707-L716",
    "source_section": "25. Future Extensions"
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
  "stable_id": "UXF-05-R041",
  "title": "Examples include: - Partner embedded commerce",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R042 — Examples include: - Marketplace channels

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
  "normative_statement": "Examples include: - Marketplace channels",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-05-042",
    "previous_temporary_key": "TMP-UXF-05-042",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Future Extensions",
    "source_context_sha256": "86b27df40f2e57aaa3358cd71cba0d227f148ce3a7e6c2cb236dd84b42c98303",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "341edf6a6ef0367988ff2c0c528c373a4f3950b7e0cab9461b836690549fe998",
    "source_lines": "L707-L717",
    "source_section": "25. Future Extensions"
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
  "stable_id": "UXF-05-R042",
  "title": "Examples include: - Marketplace channels",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-05-R054 — Customer-facing provider disclosure boundary

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "CUSTOMER_DISCLOSURE_RENDERING_V1",
      "criterion_id": "UXF-05-R054-AC001",
      "given": "a journey whose Catalog, legal, or product definition requires provider, network, or brand disclosure",
      "observable_evidence": "rendered disclosure, read-only state, governing disclosure requirement, and visible values",
      "then": "the required disclosure is visible, read-only, and contains only the allowed customer-facing information",
      "verifies": [
        "UXF-05-R054-O001"
      ],
      "when": "the customer-facing state is rendered"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "CUSTOMER_DISCLOSURE_PROHIBITION_V1",
      "criterion_id": "UXF-05-R054-AC002",
      "given": "a customer-facing UI state and its Storefront API response",
      "observable_evidence": "rendered fields and complete response-field inventory showing prohibited fields absent",
      "then": "no prohibited internal supplier, procurement, cost, margin, routing, health, connector, or allocation field is present",
      "verifies": [
        "UXF-05-R054-O002"
      ],
      "when": "the disclosure surface and payload are inspected"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DISCLOSURE_ALLOCATION_INDEPENDENCE_V1",
      "criterion_id": "UXF-05-R054-AC003",
      "given": "two otherwise identical allocation requests differing only in customer-facing disclosure",
      "observable_evidence": "both allocation inputs, disclosure difference, and identical allocation decision evidence",
      "then": "the allocation decision is unchanged by disclosure data",
      "verifies": [
        "UXF-05-R054-O003"
      ],
      "when": "Allocation evaluates both requests"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "MANDATORY_DISCLOSURE_FAIL_CLOSED_V1",
      "criterion_id": "UXF-05-R054-AC004",
      "given": "a journey where disclosure is mandatory but required disclosure data is missing",
      "observable_evidence": "missing-data condition, unavailable or blocked action, and rendered customer outcome",
      "then": "the affected action is unavailable or blocked with a customer-visible deterministic outcome",
      "verifies": [
        "UXF-05-R054-O004"
      ],
      "when": "the journey attempts to proceed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-05-R054-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R054-O001",
      "obligation_text": "Customer-facing provider, network, or brand disclosure is rendered read-only only when Catalog, legal, or product definition requires it."
    },
    {
      "acceptance_criterion_references": [
        "UXF-05-R054-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R054-O002",
      "obligation_text": "UI state and Storefront API payloads exclude internal Supplier ID, procurement source, cost, margin, routing priority, supplier health, connector identity, and allocation details."
    },
    {
      "acceptance_criterion_references": [
        "UXF-05-R054-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R054-O003",
      "obligation_text": "Customer-facing disclosure does not affect the Allocation decision."
    },
    {
      "acceptance_criterion_references": [
        "UXF-05-R054-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-05-R054-O004",
      "obligation_text": "A journey requiring mandatory disclosure does not proceed when that disclosure data is missing."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer-facing provider, network, or brand information may be shown as read-only disclosure when required by Catalog, legal, or product definition; internal supplier ID, procurement source, cost or margin, routing priority, supplier health, connector identity, and allocation details must never be exposed or influence allocation, and missing mandatory disclosure data must fail closed.",
  "provenance": {
    "allocation_contract": "P2-ALLOC-002",
    "approved_decision_contracts": {
      "P2-DEC-007": {
        "decision_id": "P2-DEC-007",
        "sections": [
          {
            "heading": "Existing principle",
            "items": [
              "Reclassify UXF-505 as DESIGN_PRINCIPLE and preserve its stable ID.",
              "Storefront does not select, route, or directly integrate Supplier; Allocation alone owns supplier selection."
            ]
          },
          {
            "heading": "New disclosure requirement",
            "items": [
              "Add one V2.3_ACTIVE UX_REQUIREMENT with reserved stable ID UXF-05-R054.",
              "Customer-facing provider/network/brand may be shown when required by Catalog, legal, or product definition, as read-only disclosure.",
              "Internal Supplier ID, procurement source, cost/margin, routing priority, supplier health, connector identity, and allocation details must never be exposed.",
              "Storefront API payloads must not contain those internal fields.",
              "Disclosure must not influence allocation.",
              "Missing mandatory disclosure data uses fail-closed business behavior.",
              "The new requirement has HIGH verification criticality."
            ]
          }
        ],
        "selected_option": 1,
        "status": "DECIDED_PENDING_PACK_APPROVAL",
        "title": "Storefront supplier decoupling and disclosure split"
      }
    },
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PHASE_2C_NEW_ALLOCATION",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "APPROVED_DECISION_CONTRACT",
    "source_context_sha256": "a898e18b3bfbc60236e50e99e2111615fd4e1cc8634528655c3f3fa711015e9c",
    "source_document": "docs/UXF/UXF-05.md"
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
  "stable_id": "UXF-05-R054",
  "title": "Customer-facing provider disclosure boundary",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-501 — Experience Runtime owns presentation while business domains retain ownership of business behavio…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "UXF-501-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Experience Runtime owns presentation while business domains retain ownership of business behavio…",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "UXF-501-O001"
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
        "UXF-501-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-501-O001",
      "obligation_text": "Experience Runtime owns presentation while business domains retain ownership of business behavior"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-045",
      "selected_disposition": "ROUTE_TO_REMEDIATION"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Experience Runtime owns presentation while business domains retain ownership of business behavior.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-501",
    "previous_temporary_key": null,
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-501",
    "source_context_sha256": "6050de1b43b14e637557ac6b36116885c3d0104e726e8cd811b2e41803173e46",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "a21471df220f3611acd3205a131597e7fe2a3659425ab51f7ea09b80e7877eb5",
    "source_lines": "L643-L646",
    "source_section": "24. Architectural Principles > UXF-501"
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
  "stable_id": "UXF-501",
  "title": "Experience Runtime owns presentation while business domains retain ownership of business behavio…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-502 — Commerce Runtime owns business capabilities

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-502-AC001",
      "given": "a user in the applicable channel and context for Commerce Runtime owns business capabilities",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-502-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-502-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Commerce Runtime owns business capabilities",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-502-O001"
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
        "UXF-502-AC001",
        "UXF-502-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-502-O001",
      "obligation_text": "Commerce Runtime owns business capabilities"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commerce Runtime owns business capabilities.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-502",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-502",
    "source_context_sha256": "5ad44adf4658657ffc6a1d9664e840ca1493526ed5b58afaee9b072137143aed",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "1e1e887202fbebba1edbeb2becd42fa48af062d74d2d5ec58e73bb7c10526288",
    "source_lines": "L649-L652",
    "source_section": "24. Architectural Principles > UXF-502"
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
  "stable_id": "UXF-502",
  "title": "Commerce Runtime owns business capabilities",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-503 — Infrastructure Runtime owns integrations

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "UXF-503-AC001",
      "given": "a contract interaction at the integration boundary defined by Infrastructure Runtime owns integrations",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "UXF-503-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "UXF-503-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Infrastructure Runtime owns integrations",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "UXF-503-O001"
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
        "UXF-503-AC001",
        "UXF-503-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-503-O001",
      "obligation_text": "Infrastructure Runtime owns integrations"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Infrastructure Runtime owns integrations.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-503",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-503",
    "source_context_sha256": "9ec3a3d38d02df00631996d092439914580fe4a4ce35f68b2f216a7dc82f28ae",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "9f50f54681b21fe46b60594b12ddb79665361e8935d7ab94a0806d833f0b9358",
    "source_lines": "L655-L658",
    "source_section": "24. Architectural Principles > UXF-503"
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
  "stable_id": "UXF-503",
  "title": "Infrastructure Runtime owns integrations",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-504 — Business Binding connects Experience with Commerce

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-504-AC001",
      "given": "a user in the applicable channel and context for Business Binding connects Experience with Commerce",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-504-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-504-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Business Binding connects Experience with Commerce",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-504-O001"
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
        "UXF-504-AC001",
        "UXF-504-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-504-O001",
      "obligation_text": "Business Binding connects Experience with Commerce"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Binding connects Experience with Commerce.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-504",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-504",
    "source_context_sha256": "d18eef72520ed20598554f51eeb63cee8f724228fcba7ac22a65a0dc86376e4e",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "4ffd4b1832800447d60f3972ff225dda25e5fbb6304fbc03e6853bff901d97da",
    "source_lines": "L661-L664",
    "source_section": "24. Architectural Principles > UXF-504"
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
  "stable_id": "UXF-504",
  "title": "Business Binding connects Experience with Commerce",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-505 — Storefronts never know suppliers

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-505-AC001",
      "given": "a user in the applicable channel and context for Storefronts never know suppliers",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-505-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-505-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Storefronts never know suppliers",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-505-O001"
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
        "UXF-505-AC001",
        "UXF-505-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-505-O001",
      "obligation_text": "Storefronts never know suppliers"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Storefronts never know suppliers.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-505",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Allocation Principle",
    "source_context_sha256": "c6611e3c03ef3c82584e8c88d9b24f953779d35fe950ec34b801dad64fd818a2",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "115368e9a04c30e94e8c61b510badc59b95e56531e7469c5853c4cf2a10b9a99",
    "source_lines": "L667-L670",
    "source_section": "24. Architectural Principles > UXF-505"
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
  "stable_id": "UXF-505",
  "title": "Storefronts never know suppliers",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-506 — Allocation is the only capability allowed to select suppliers

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-506-AC001",
      "given": "a user in the applicable channel and context for Allocation is the only capability allowed to select suppliers",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-506-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-506-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Allocation is the only capability allowed to select suppliers",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-506-O001"
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
        "UXF-506-AC001",
        "UXF-506-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-506-O001",
      "obligation_text": "Allocation is the only capability allowed to select suppliers"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-506 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-506 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-506 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "UXF-506 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-506-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-506 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-046",
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
    "original_identity": "UXF-506",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-506",
    "source_context_sha256": "91c223af9261dad7624e7efedb194c38d9f0cc7cda9529cf0e2d053c4783bd78",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "8a4fc68772b435c911f76901b82fa61625dcb2917323306c1d7b2940c4d9175a",
    "source_lines": "L673-L676",
    "source_section": "24. Architectural Principles > UXF-506"
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
  "stable_id": "UXF-506",
  "title": "Allocation is the only capability allowed to select suppliers",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-507 — Business Configuration supports inheritance

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-507-AC001",
      "given": "a user in the applicable channel and context for Business Configuration supports inheritance",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "a missing child value resolves to the parent configuration, an explicit child override wins only at its declared scope, and the rendered result identifies the effective source",
      "verifies": [
        "UXF-507-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_INHERITANCE_FAILURE_V1",
      "criterion_id": "UXF-507-AC002",
      "given": "a child experience with no local value and an invalid or unavailable parent configuration for Business Configuration supports inheritance",
      "observable_evidence": "child and parent configuration identities, resolution trace, fallback or failure result, and rendered value",
      "then": "resolution produces the declared deterministic fallback or a visible configuration failure and never renders an unexplained value",
      "verifies": [
        "UXF-507-O001"
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
        "UXF-507-AC001",
        "UXF-507-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-507-O001",
      "obligation_text": "Business Configuration supports inheritance"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Configuration supports inheritance.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-507",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Business Configuration Inheritance",
    "source_context_sha256": "596d18cc1c8f71ce23606c1b487613133846c4bfd6da3e2901965e065c5c8525",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "27f76e5ed0f6eff27d1153e587800862a4a7c9de8f1a6e992db8f3da39338c95",
    "source_lines": "L679-L682",
    "source_section": "24. Architectural Principles > UXF-507"
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
  "stable_id": "UXF-507",
  "title": "Business Configuration supports inheritance",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-508 — Business Configuration supports fallback

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-508-AC001",
      "given": "a user in the applicable channel and context for Business Configuration supports fallback",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-508-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-508-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Business Configuration supports fallback",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-508-O001"
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
        "UXF-508-AC001",
        "UXF-508-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-508-O001",
      "obligation_text": "Business Configuration supports fallback"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Configuration supports fallback.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-508",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-508",
    "source_context_sha256": "0c337f28a8b8407fa7c8a032cc5d055383ec827d9668a7751346ca92dc9732db",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "299bce8d120f2d5eb9279d329fb2c32cdd4c751c0bf29268800fa100caf74a54",
    "source_lines": "L685-L688",
    "source_section": "24. Architectural Principles > UXF-508"
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
  "stable_id": "UXF-508",
  "title": "Business Configuration supports fallback",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-509 — Published snapshots are immutable

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "UXF-509-AC001",
      "given": "a candidate Published snapshots are immutable record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "UXF-509-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "UXF-509-AC002",
      "given": "a Published snapshots are immutable candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "UXF-509-O001"
      ],
      "when": "the candidate is validated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-509-AC001",
        "UXF-509-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-509-O001",
      "obligation_text": "Published snapshots are immutable"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-509 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-509 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-509 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "UXF-509 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-509-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-509 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Published snapshots are immutable.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-509",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-509",
    "source_context_sha256": "f6c1778626981bf6fbfac96c6573b6f0f4ba9837308f3d6d7ad26daf5155aa07",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "ebc8280019b41948a0bbdd9b5bf05937841de07a79a2c4e7042db56ee668a6a9",
    "source_lines": "L691-L694",
    "source_section": "24. Architectural Principles > UXF-509"
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
  "stable_id": "UXF-509",
  "title": "Published snapshots are immutable",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-510 — Experience Runtime and Commerce Runtime remain independent

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-510-AC001",
      "given": "a user in the applicable channel and context for Experience Runtime and Commerce Runtime remain independent",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-510-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-510-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Experience Runtime and Commerce Runtime remain independent",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-510-O001"
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
        "UXF-510-AC001",
        "UXF-510-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-510-O001",
      "obligation_text": "Experience Runtime and Commerce Runtime remain independent"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Experience Runtime and Commerce Runtime remain independent.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-510",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-510",
    "source_context_sha256": "66db7c83ca099860cd9ae996e16a25227a0c88d9166ca079a9d3a8b66a3144ba",
    "source_document": "docs/UXF/UXF-05.md",
    "source_fingerprint": "75bc154d1a1bd90d4def4beb155374006051f3de4c32aa189fc93c52e10da126",
    "source_lines": "L697-L700",
    "source_section": "24. Architectural Principles > UXF-510"
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
  "stable_id": "UXF-510",
  "title": "Experience Runtime and Commerce Runtime remain independent",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
