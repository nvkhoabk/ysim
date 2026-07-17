---
document_code: "BRD-WS-01"
document_id: "BRD-WS-01"
title: "Product Vision & Strategy"
version: "2.3.0-draft.3"
document_revision: "2.3.0-draft.3"
status: "V2.3_DRAFT"
lifecycle_status: "V2.3_DRAFT"
language: "vi-VN"
baseline: "2.3"
product_baseline: "2.3"
source_lineage: "v2.2 + approved Phase 1/2A/2B + accepted Acceptance Model C1 + accepted Mapping C3"
source_baseline: "v2.2"
last_reviewed_date: "2026-07-15"
last_remediated_on: "2026-07-17"
applicable_scope: "V2.3_ACTIVE_AND_RETAINED_SCOPE_RECORDS"
generated_registry_role: "BRD_CANONICAL_SOURCE"
---
## Thẩm quyền nguồn yêu cầu v2.3

Các khối `YSIM:REQUIREMENT` trong phụ lục chuẩn tắc là nguồn yêu cầu có thẩm quyền cho baseline 2.3. Nội dung legacy bên dưới được giữ làm ngữ cảnh; nếu có khác biệt, khối chuẩn tắc và các quyết định v2.3 đã phê duyệt được ưu tiên.

# BRD Workshop 01
# Product Vision & Strategy

---

# 1. Workshop Objective

Xác định tầm nhìn, định vị sản phẩm, phạm vi nghiệp vụ và các nguyên tắc nền tảng của YSim v2.0 trước khi xây dựng các yêu cầu chi tiết.

Workshop này là nền tảng cho toàn bộ BRD v2.0.

---

# 2. Product Vision

YSim là nền tảng thương mại và phân phối eSIM toàn cầu (Global eSIM Commerce & Distribution Platform), kết nối các nhà cung cấp eSIM với nhiều kênh bán hàng và đối tác phân phối nhằm mang đến trải nghiệm mua, cấp phát, kích hoạt và quản lý eSIM thuận tiện cho khách du lịch quốc tế.

YSim không được định vị là một website bán eSIM đơn lẻ mà là một White-label Commerce Platform dành riêng cho ngành eSIM.

---

# 3. Product Positioning

YSim là một Product Line thuộc hệ sinh thái Digital Connectivity Platform (DCP).

```text
Digital Connectivity Platform (DCP)

├── YSim
│      eSIM Commerce Platform
│
├── YData
├── YTV
├── YTravel
├── YService
└── Future Products
```

Trong phiên bản 2.0 chỉ triển khai nghiệp vụ eSIM.

Các dịch vụ khác được xem là Out of Scope.

---

# 4. Product Scope

## In Scope

- eSIM Commerce
- White-label Commerce
- Multi-level Distribution
- Multi-supplier Integration
- Intelligent Allocation Engine
- Pricing
- Promotion
- Coupon
- Campaign
- Checkout
- Payment
- Fulfillment
- Activation
- Settlement
- CRM
- Customer Support
- Analytics

## Out of Scope

- Physical SIM
- Mobile Data Platform
- IPTV
- Flight
- Hotel
- Tour
- Digital Services

---

# 5. Product Philosophy

YSim không phải Marketplace.

YSim là White-label Commerce Platform.

Partner sử dụng nền tảng YSim để xây dựng thương hiệu, cửa hàng và hệ thống phân phối của riêng mình.

---

# 6. Core Business Capability

- White-label Commerce
- Multi-level Distribution
- Multi-supplier Integration
- Intelligent Allocation Engine
- Pricing & Promotion Engine
- Checkout & Payment
- Digital eSIM Fulfillment
- Settlement Engine
- CRM
- Analytics

---

# 7. Storefront Concept

Mỗi Partner có thể sở hữu nhiều Storefront.

Một Storefront bao gồm:

- Domain/Subdomain
- Landing Page
- Theme
- Logo
- Banner
- Payment Configuration
- Catalog
- Pricing
- Campaign
- QR Campaign
- Tracking

---

# 8. Commerce Lifecycle

```text
Discover
    ↓
Select
    ↓
Order
    ↓
Payment
    ↓
Fulfillment
    ↓
Activation
    ↓
Support
    ↓
Renewal
```

Khái niệm này được gọi là:

**Digital eSIM Fulfillment**

---

# 9. Sales Channels

Hệ thống phải hỗ trợ:

- Direct Website
- White-label Website
- Agency
- Multi-level Distribution
- Online Seller
- Social Commerce
- Marketplace
- API Partner
- Enterprise Customer

---

# 10. Pricing Strategy

YSim quản lý:

- Product
- Suggested Retail Price
- Discount Policy

Partner được quyền:

- Định giá bán
- Quản lý đại lý
- Thiết lập Commission
- Thiết lập Campaign

Hệ thống hỗ trợ:

- Promotion
- Coupon
- Loyalty

---

# 11. Settlement Strategy

Các hình thức thanh toán:

- Wallet / Deposit
- Pay-per-order
- Payment Gateway
- Postpaid Settlement

Toàn bộ đối soát sử dụng:

**Snapshot Pricing**

---

# 12. Intelligent Allocation Engine

Allocation Engine quyết định Supplier tối ưu dựa trên:

- Cost
- Margin
- SLA
- Availability
- API Health
- Credit Limit
- Priority
- Contract Policy

Mục tiêu:

- Giá cạnh tranh
- API ổn định
- Fulfillment thời gian thực

---

# 13. Customer Strategy

End Customer là trung tâm của toàn bộ hệ thống.

Partner là kênh phân phối.

---

# 14. Customer Ownership Model

Được thống nhất sử dụng:

**Hybrid Model**

- Partner sở hữu quan hệ thương mại.
- YSim quản lý hồ sơ kỹ thuật phục vụ Fulfillment, Activation, Support và Compliance.
- CRM có thể chia sẻ theo chính sách.

---

# 15. Competitive Advantages

- White-label Commerce
- Multi-level Distribution
- Multi-supplier Integration
- Intelligent Allocation Engine
- Snapshot Pricing
- Flexible Settlement
- Real-time Fulfillment
- Strong Customer Support

---

# 16. Business Principles

1. Business First
2. Platform before Store
3. Partner Empowerment
4. Customer-centric Lifecycle
5. Real-time Fulfillment
6. Snapshot Integrity
7. Open Integration
8. Enterprise Scalability

---

# 17. Open Items

Không.

Workshop đã được thống nhất.

---

# 18. Workshop Status

**FROZEN**

Workshop này được sử dụng làm nền tảng cho tất cả các Workshop tiếp theo.

---

# 19. Traceability

Nguồn:

- Thảo luận Workshop 01 giữa Product Owner và Solution Architect.
- Bài học rút ra từ YSim v1.0.

---

# 20. Next Workshop

**Workshop 02 – Business Model & Revenue Architecture**

---

# Architecture Decisions Applied

This Business Requirement Set is governed by the following architecture decisions:

- AFD-002 — Commerce Experience Platform
- AFD-003 — Business Factory
- AFD-005 — Unified Inheritance Framework
- AFD-006 — Payment Offering

---

# Impact to Future DIP

- Store Management Sprint
- Store Runtime Sprint
- Checkout Sprint
- Payment Sprint
- Theme Sprint

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R001 — YSim product positioning

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
      "requirement_id": "BRD-WS-01-R001",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "198983665fcb17bcd3ed74ae0869026b2655147e6ddfd3c5a5397270bea9f33e"
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
        "BRD-WS-01-R001-AC001",
        "BRD-WS-01-R001-AC002",
        "BRD-WS-01-R001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R001-O001",
      "obligation_text": "YSim không được định vị là một website bán eSIM đơn lẻ mà là một White-label Commerce Platform dành riêng cho ngành eSIM"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-016",
      "selected_disposition": "ROUTE_TO_REMEDIATION"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "YSim không được định vị là một website bán eSIM đơn lẻ mà là một White-label Commerce Platform dành riêng cho ngành eSIM.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-001",
    "previous_temporary_key": "TMP-BRD-WS-01-001",
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "2. Product Vision",
    "source_context_sha256": "e948a1e9ea01f121efdf989ead8e06f362626160cac248e570df371bd6972b0e",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "198983665fcb17bcd3ed74ae0869026b2655147e6ddfd3c5a5397270bea9f33e",
    "source_lines": "L349-L436",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R001"
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
  "stable_id": "BRD-WS-01-R001",
  "title": "YSim product positioning",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R002 — Các dịch vụ khác được xem là Out of Scope

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-01-R002",
    "scope_status": "OUT_OF_SCOPE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "EXCLUDED_FROM_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Các dịch vụ khác được xem là Out of Scope.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-002",
    "previous_temporary_key": "TMP-BRD-WS-01-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Product Positioning",
    "source_context_sha256": "5c2d9e49c39650ed65f1885415511ca1436774fafe2ddff640531733950d6a87",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "5825c88bd217ca00eb00a587e79affc88a967fe1095bce60a1b2fad59a3c2143",
    "source_lines": "L438-L496",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R002"
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
  "scope_status": "OUT_OF_SCOPE",
  "stable_id": "BRD-WS-01-R002",
  "title": "Các dịch vụ khác được xem là Out of Scope",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R003 — eSIM Commerce is included in the active YSim v2.3 product scope

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
      "requirement_id": "BRD-WS-01-R003",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "4c037cb3b0f7e499a2b9d502a03051e505b847cbfe46a823d3fd1710d4acf525"
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
        "BRD-WS-01-R003-AC001",
        "BRD-WS-01-R003-AC002",
        "BRD-WS-01-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R003-O001",
      "obligation_text": "eSIM Commerce is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "eSIM Commerce is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-003",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "4c037cb3b0f7e499a2b9d502a03051e505b847cbfe46a823d3fd1710d4acf525",
    "source_fingerprint_before_c3": "3d7e8b249215b7080b48bc4226ef6bb96e1e56b11b3c3b95e651a40dc0690a22",
    "source_lines": "L498-L594",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L61",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R003"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R003",
  "title": "eSIM Commerce is included in the active YSim v2.3 product scope",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R004 — White-label commerce principle

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
      "requirement_id": "BRD-WS-01-R004",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "0dd3753938d475e72b75400a04f95f043a96f593d109e19f6b9eb1243ce8b78a"
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
        "BRD-WS-01-R004-AC001",
        "BRD-WS-01-R004-AC002",
        "BRD-WS-01-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R004-O001",
      "obligation_text": "YSim phải cung cấp năng lực thương mại white-label như một nguyên tắc sản phẩm, với hành vi cụ thể được quy định bởi các yêu cầu kênh và cấu hình liên quan"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-017",
      "selected_disposition": "ROUTE_TO_REMEDIATION"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "YSim phải cung cấp năng lực thương mại white-label như một nguyên tắc sản phẩm, với hành vi cụ thể được quy định bởi các yêu cầu kênh và cấu hình liên quan.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-004",
    "previous_temporary_key": "TMP-BRD-WS-01-004",
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "0dd3753938d475e72b75400a04f95f043a96f593d109e19f6b9eb1243ce8b78a",
    "source_lines": "L596-L683",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R004"
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
  "stable_id": "BRD-WS-01-R004",
  "title": "White-label commerce principle",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R005 — Multi-level Distribution is included in the active YSim v2.3 product scope

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
      "requirement_id": "BRD-WS-01-R005",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "463aa14bc497af5d99c148eac852cec1bea7896dd9f32ed14679659975c87bad"
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
        "BRD-WS-01-R005-AC001",
        "BRD-WS-01-R005-AC002",
        "BRD-WS-01-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R005-O001",
      "obligation_text": "Multi-level Distribution is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Multi-level Distribution is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-005",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "463aa14bc497af5d99c148eac852cec1bea7896dd9f32ed14679659975c87bad",
    "source_fingerprint_before_c3": "244fb0a041b03025a3809f69ed1b23d2799e4bc31143915e40949103bac92c63",
    "source_lines": "L685-L781",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L63",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R005"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R005",
  "title": "Multi-level Distribution is included in the active YSim v2.3 product scope",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R006 — Multi-supplier Integration is included in the active YSim v2.3 product scope

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-01-R006",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "5b379035746f987761c4fb8b44ba3eaf3853c08a4fa914c80457d04c7c1c82c3"
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
        "BRD-WS-01-R006-AC001",
        "BRD-WS-01-R006-AC002",
        "BRD-WS-01-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R006-O001",
      "obligation_text": "Multi-supplier Integration is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Multi-supplier Integration is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-006",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "5b379035746f987761c4fb8b44ba3eaf3853c08a4fa914c80457d04c7c1c82c3",
    "source_fingerprint_before_c3": "a21a5a4a56ffcaa98d233ed64e857907e3eeb43ae6a6b36a00370a5bc2fefca1",
    "source_lines": "L783-L881",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L64",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R006"
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
  "stable_id": "BRD-WS-01-R006",
  "title": "Multi-supplier Integration is included in the active YSim v2.3 product scope",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R007 — Intelligent Allocation Engine is included in the active YSim v2.3 product scope

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-01-R007",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "7b572e235ae6e33ae35ed22b52d951d35ed35531211738b374be4b13a3bd82e9"
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
        "BRD-WS-01-R007-AC001",
        "BRD-WS-01-R007-AC002",
        "BRD-WS-01-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R007-O001",
      "obligation_text": "Intelligent Allocation Engine is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R007 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-01-R007-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-01-R007-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R007 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Intelligent Allocation Engine is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-007",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "7b572e235ae6e33ae35ed22b52d951d35ed35531211738b374be4b13a3bd82e9",
    "source_fingerprint_before_c3": "d3bc50416e160d27b85486f1bad960b8b118962c7e533a0c3aaad1eb4365d6ea",
    "source_lines": "L883-L1014",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L65",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R007"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R007",
  "title": "Intelligent Allocation Engine is included in the active YSim v2.3 product scope",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R008 — Pricing is included in the active YSim v2.3 product scope

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
      "requirement_id": "BRD-WS-01-R008",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "8a6b36f001c8a05a7fbe68ad273ad0a4072b68ace7c45010aa4718ddceae40e2"
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
        "BRD-WS-01-R008-AC001",
        "BRD-WS-01-R008-AC002",
        "BRD-WS-01-R008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R008-O001",
      "obligation_text": "Pricing is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R008 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R008 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R008 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-01-R008-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-01-R008-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R008 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Pricing is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-008",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "8a6b36f001c8a05a7fbe68ad273ad0a4072b68ace7c45010aa4718ddceae40e2",
    "source_fingerprint_before_c3": "d35805ed6b5b489709e3f3878bff9868d09b4c1db01021abf65a1a24a20a9ec2",
    "source_lines": "L1016-L1145",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L66",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R008"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R008",
  "title": "Pricing is included in the active YSim v2.3 product scope",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R009 — Promotion is included in the active YSim v2.3 product scope

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
      "requirement_id": "BRD-WS-01-R009",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "c6cc2ae801c58abcb03352e4191f351cd0cda7114c6f8732a4af1ec0ba346ea3"
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
        "BRD-WS-01-R009-AC001",
        "BRD-WS-01-R009-AC002",
        "BRD-WS-01-R009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R009-O001",
      "obligation_text": "Promotion is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Promotion is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-009",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "c6cc2ae801c58abcb03352e4191f351cd0cda7114c6f8732a4af1ec0ba346ea3",
    "source_fingerprint_before_c3": "978a2387cf21835ffc4d311dd0cc4cd86c412594dac0dffb9faa38d426ab1bc2",
    "source_lines": "L1147-L1243",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L67",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R009"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R009",
  "title": "Promotion is included in the active YSim v2.3 product scope",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R010 — Coupon is included in the active YSim v2.3 product scope

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
      "requirement_id": "BRD-WS-01-R010",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "816cfcba6eff8ea960f126b598e9f785b33acdf3f0f0f51b10c93c05698d7f1e"
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
        "BRD-WS-01-R010-AC001",
        "BRD-WS-01-R010-AC002",
        "BRD-WS-01-R010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R010-O001",
      "obligation_text": "Coupon is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Coupon is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-010",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "816cfcba6eff8ea960f126b598e9f785b33acdf3f0f0f51b10c93c05698d7f1e",
    "source_fingerprint_before_c3": "1230c15c28cd776f08c04ce3c94a342bc7782e9de5d78e1c6f9f34606ef61d4b",
    "source_lines": "L1245-L1341",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L68",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R010"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R010",
  "title": "Coupon is included in the active YSim v2.3 product scope",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R011 — Campaign is included in the active YSim v2.3 product scope

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
      "requirement_id": "BRD-WS-01-R011",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "75a1bc45e27b59e95472acd55031e30239f8761fc50de7f83598d5b03e0a305f"
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
        "BRD-WS-01-R011-AC001",
        "BRD-WS-01-R011-AC002",
        "BRD-WS-01-R011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R011-O001",
      "obligation_text": "Campaign is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Campaign is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-011",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "75a1bc45e27b59e95472acd55031e30239f8761fc50de7f83598d5b03e0a305f",
    "source_fingerprint_before_c3": "2523c93260968bd8f104d3045991c752e0611c91b341e5c3d00811feac9bd7b7",
    "source_lines": "L1343-L1439",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L69",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R011"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R011",
  "title": "Campaign is included in the active YSim v2.3 product scope",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R012 — Checkout is included in the active YSim v2.3 product scope

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
      "requirement_id": "BRD-WS-01-R012",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "f7223826576d084a141eef8db8d7665a963e446709121eecfee9affbe5adc878"
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
        "BRD-WS-01-R012-AC001",
        "BRD-WS-01-R012-AC002",
        "BRD-WS-01-R012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R012-O001",
      "obligation_text": "Checkout is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Checkout is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-012",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "f7223826576d084a141eef8db8d7665a963e446709121eecfee9affbe5adc878",
    "source_fingerprint_before_c3": "d5b73cedb7b7a4366f3a8a2c380d341052fba12df99ee6d54c856e940a4a7aa2",
    "source_lines": "L1441-L1537",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L70",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R012"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R012",
  "title": "Checkout is included in the active YSim v2.3 product scope",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R013 — Payment is included in the active YSim v2.3 product scope

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
      "requirement_id": "BRD-WS-01-R013",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "5f77af0318f13b4de907b582e1119a5ccf86720504c14eb3192028d557128ea6"
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
        "BRD-WS-01-R013-AC001",
        "BRD-WS-01-R013-AC002",
        "BRD-WS-01-R013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R013-O001",
      "obligation_text": "Payment is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R013 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R013 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R013 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-01-R013-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-01-R013-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R013 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Payment is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-013",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "5f77af0318f13b4de907b582e1119a5ccf86720504c14eb3192028d557128ea6",
    "source_fingerprint_before_c3": "f26784e7c96bfd795296d37f67ced0f5ded699f21a6ed197b402e88135f7fd5d",
    "source_lines": "L1539-L1668",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L71",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R013"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R013",
  "title": "Payment is included in the active YSim v2.3 product scope",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R014 — Fulfillment is included in the active YSim v2.3 product scope

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
      "requirement_id": "BRD-WS-01-R014",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "819e739e46d5301de44a002a9c45fa1a2706bbd877e7106bb13a055ec8c997c8"
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
        "BRD-WS-01-R014-AC001",
        "BRD-WS-01-R014-AC002",
        "BRD-WS-01-R014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R014-O001",
      "obligation_text": "Fulfillment is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R014 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-01-R014-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-01-R014-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-01-R014 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Fulfillment is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-014",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "819e739e46d5301de44a002a9c45fa1a2706bbd877e7106bb13a055ec8c997c8",
    "source_fingerprint_before_c3": "597260520ac2da3d42f4c11569f7a7731c2b315f9becd59fb56b7b56e7cdc29b",
    "source_lines": "L1670-L1799",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L72",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R014"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R014",
  "title": "Fulfillment is included in the active YSim v2.3 product scope",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R015 — Activation is included in the active YSim v2.3 product scope

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
      "requirement_id": "BRD-WS-01-R015",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "b0b6e49e1e702b4f8ec567de559b57bf46916b5f0a718ad5658adf9917263fb6"
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
        "BRD-WS-01-R015-AC001",
        "BRD-WS-01-R015-AC002",
        "BRD-WS-01-R015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R015-O001",
      "obligation_text": "Activation is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Activation is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-015",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "b0b6e49e1e702b4f8ec567de559b57bf46916b5f0a718ad5658adf9917263fb6",
    "source_fingerprint_before_c3": "800708fd26837300f9306c09194486bdeebdbbf1e3e3076dbea7c0bbdc6c1915",
    "source_lines": "L1801-L1897",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L73",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R015"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R015",
  "title": "Activation is included in the active YSim v2.3 product scope",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R016 — Settlement is included in the active YSim v2.3 product scope

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
      "requirement_id": "BRD-WS-01-R016",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "ec47f44126c40dc34b7a0f011af8f94732f14544964f7e838891421aabae828b"
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
        "BRD-WS-01-R016-AC001",
        "BRD-WS-01-R016-AC002",
        "BRD-WS-01-R016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R016-O001",
      "obligation_text": "Settlement is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Settlement is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-016",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "ec47f44126c40dc34b7a0f011af8f94732f14544964f7e838891421aabae828b",
    "source_fingerprint_before_c3": "0cf6da12565e4ffca3f15ea894c72fe257b2de49e0a9c83d10bac993711b26bc",
    "source_lines": "L1899-L1995",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L74",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R016"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R016",
  "title": "Settlement is included in the active YSim v2.3 product scope",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R017 — CRM is included in the active YSim v2.3 product scope

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
      "requirement_id": "BRD-WS-01-R017",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "5db7aba649823e8890ac24ce07db3e560936828710ccf33ddf528eafd9f2dbd4"
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
        "BRD-WS-01-R017-AC001",
        "BRD-WS-01-R017-AC002",
        "BRD-WS-01-R017-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R017-O001",
      "obligation_text": "CRM is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "CRM is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-017",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "15bc5e7009aa63fad237aaca371d34536c478266c20e39d3ecf7f06c9bb54727",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "5db7aba649823e8890ac24ce07db3e560936828710ccf33ddf528eafd9f2dbd4",
    "source_fingerprint_before_c3": "15bc5e7009aa63fad237aaca371d34536c478266c20e39d3ecf7f06c9bb54727",
    "source_lines": "L1997-L2093",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L75",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R017"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R017",
  "title": "CRM is included in the active YSim v2.3 product scope",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R018 — Customer Support is included in the active YSim v2.3 product scope

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-01-R018",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "254ee32b511d3541fe1609ed58408b92aaa90bdfa9072b5614b18223903f5664"
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
        "BRD-WS-01-R018-AC001",
        "BRD-WS-01-R018-AC002",
        "BRD-WS-01-R018-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R018-O001",
      "obligation_text": "Customer Support is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Support is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-018",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-018",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "254ee32b511d3541fe1609ed58408b92aaa90bdfa9072b5614b18223903f5664",
    "source_fingerprint_before_c3": "d0a10547452260b3866b7c0f0f80c62bee644450ee258e16bb40a3191650b41c",
    "source_lines": "L2095-L2193",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L76",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R018"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R018",
  "title": "Customer Support is included in the active YSim v2.3 product scope",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R019 — Analytics is included in the active YSim v2.3 product scope

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
      "requirement_id": "BRD-WS-01-R019",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "0da2bfbea60512cf3962fc4fd7eead1a809a65817f6fd6ae71e0d8c0be1e9f0e"
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
        "BRD-WS-01-R019-AC001",
        "BRD-WS-01-R019-AC002",
        "BRD-WS-01-R019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R019-O001",
      "obligation_text": "Analytics is included in the active YSim v2.3 product scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Analytics is included in the active YSim v2.3 product scope.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-01.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "4. Product Scope > In Scope"
    },
    "deterministic_transformation": "RESTORE_IN_SCOPE_PREDICATE",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-019",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-01-019",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "In Scope",
    "source_context_sha256": "38d43d01b0fdf81b82681b2fd34a75ff50c90b7ff040edfdda6f619baa2f2e50",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "0da2bfbea60512cf3962fc4fd7eead1a809a65817f6fd6ae71e0d8c0be1e9f0e",
    "source_fingerprint_before_c3": "843312debf82000c0390f3721a9d9a0acc29836cbc1e852f7e0cde3c4139ce93",
    "source_lines": "L2195-L2291",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-01.md",
      "lines": "L77",
      "section": "4. Product Scope > In Scope"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R019"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R019",
  "title": "Analytics is included in the active YSim v2.3 product scope",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R020 —  Physical SIM

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-01-R020",
    "scope_status": "OUT_OF_SCOPE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "EXCLUDED_FROM_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "- Physical SIM",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-020",
    "previous_temporary_key": "TMP-BRD-WS-01-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "Out of Scope",
    "source_context_sha256": "83a46d86fc2d2cf60871ce65bb47ab0d6bdb020c0116ab9507dee444c25302f8",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "d1e171be41a3ced2881aff7b70134d82f27ba34bcf4dbfe813cd0d19fb1b862b",
    "source_lines": "L2293-L2351",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R020"
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
  "scope_status": "OUT_OF_SCOPE",
  "stable_id": "BRD-WS-01-R020",
  "title": " Physical SIM",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R021 —  Mobile Data Platform

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-01-R021",
    "scope_status": "OUT_OF_SCOPE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "EXCLUDED_FROM_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "- Mobile Data Platform",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-021",
    "previous_temporary_key": "TMP-BRD-WS-01-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "Out of Scope",
    "source_context_sha256": "83a46d86fc2d2cf60871ce65bb47ab0d6bdb020c0116ab9507dee444c25302f8",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "b84d7f16056e0828d20010e769a111ff916145ae8cbb825161aeb6b8047c00e7",
    "source_lines": "L2353-L2411",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R021"
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
  "scope_status": "OUT_OF_SCOPE",
  "stable_id": "BRD-WS-01-R021",
  "title": " Mobile Data Platform",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R022 —  IPTV

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-01-R022",
    "scope_status": "OUT_OF_SCOPE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "EXCLUDED_FROM_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "- IPTV",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-022",
    "previous_temporary_key": "TMP-BRD-WS-01-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "662c2009a1daeb9b72ce3ac28273daf914cd4757337a36f30e0bda214850fba2",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "662c2009a1daeb9b72ce3ac28273daf914cd4757337a36f30e0bda214850fba2",
    "source_lines": "L2413-L2471",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R022"
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
  "scope_status": "OUT_OF_SCOPE",
  "stable_id": "BRD-WS-01-R022",
  "title": " IPTV",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R023 —  Flight

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-01-R023",
    "scope_status": "OUT_OF_SCOPE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "EXCLUDED_FROM_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "- Flight",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-023",
    "previous_temporary_key": "TMP-BRD-WS-01-023",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "Out of Scope",
    "source_context_sha256": "83a46d86fc2d2cf60871ce65bb47ab0d6bdb020c0116ab9507dee444c25302f8",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "618420e7c9ae5fa8f4e09c6320cdf0170e731643b987ff3d54782a9bc1eb01e3",
    "source_lines": "L2473-L2531",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R023"
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
  "scope_status": "OUT_OF_SCOPE",
  "stable_id": "BRD-WS-01-R023",
  "title": " Flight",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R024 —  Hotel

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-01-R024",
    "scope_status": "OUT_OF_SCOPE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "EXCLUDED_FROM_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "- Hotel",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-024",
    "previous_temporary_key": "TMP-BRD-WS-01-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "29eb1ca180d3ff6df7908cb84cad0ff57372a3ac44d5c11df470995e053207c0",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "29eb1ca180d3ff6df7908cb84cad0ff57372a3ac44d5c11df470995e053207c0",
    "source_lines": "L2533-L2591",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R024"
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
  "scope_status": "OUT_OF_SCOPE",
  "stable_id": "BRD-WS-01-R024",
  "title": " Hotel",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R025 —  Tour

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-01-R025",
    "scope_status": "OUT_OF_SCOPE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "EXCLUDED_FROM_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "- Tour",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-025",
    "previous_temporary_key": "TMP-BRD-WS-01-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "946a29b1356bcf52ed358c0e6f4fc06f8ff5bae87b44e26b98b5939d997fc248",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "946a29b1356bcf52ed358c0e6f4fc06f8ff5bae87b44e26b98b5939d997fc248",
    "source_lines": "L2593-L2651",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R025"
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
  "scope_status": "OUT_OF_SCOPE",
  "stable_id": "BRD-WS-01-R025",
  "title": " Tour",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R026 —  Digital Services

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-01-R026",
    "scope_status": "OUT_OF_SCOPE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "EXCLUDED_FROM_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "- Digital Services",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-026",
    "previous_temporary_key": "TMP-BRD-WS-01-026",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "Out of Scope",
    "source_context_sha256": "83a46d86fc2d2cf60871ce65bb47ab0d6bdb020c0116ab9507dee444c25302f8",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "4f4b0cbf054638ad840af81de53ce8fbb88bcd85c4b72f1861f850e9bbb56eed",
    "source_lines": "L2653-L2711",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R026"
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
  "scope_status": "OUT_OF_SCOPE",
  "stable_id": "BRD-WS-01-R026",
  "title": " Digital Services",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R027 — YSim không phải Marketplace

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
      "requirement_id": "BRD-WS-01-R027",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "58a27ae2d6596b8a8e713124ea6b9f1b16d75c5a4e2fa65bb3641622d25846a9"
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
        "BRD-WS-01-R027-AC001",
        "BRD-WS-01-R027-AC002",
        "BRD-WS-01-R027-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R027-O001",
      "obligation_text": "YSim không phải Marketplace"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "YSim không phải Marketplace.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-027",
    "previous_temporary_key": "TMP-BRD-WS-01-027",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Product Philosophy",
    "source_context_sha256": "048db5e25271fed906827e45b9ec41f103bb48262eb28fbe05a0930c2247008b",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "58a27ae2d6596b8a8e713124ea6b9f1b16d75c5a4e2fa65bb3641622d25846a9",
    "source_lines": "L2713-L2788",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R027"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R027",
  "title": "YSim không phải Marketplace",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R028 — Hệ thống phải hỗ trợ: - Direct Website

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
      "requirement_id": "BRD-WS-01-R028",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "5ee52367d15968631a62c8cb20f0d92a4b5fc3a90cb683f93546644c595f83af"
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
        "BRD-WS-01-R028-AC001",
        "BRD-WS-01-R028-AC002",
        "BRD-WS-01-R028-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R028-O001",
      "obligation_text": "Hệ thống phải hỗ trợ: - Direct Website"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Hệ thống phải hỗ trợ: - Direct Website",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-028",
    "previous_temporary_key": "TMP-BRD-WS-01-028",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Sales Channels",
    "source_context_sha256": "c51203f69e40724208e93909b1dff7733e62620546cbf8a408680d28ec69886e",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "5ee52367d15968631a62c8cb20f0d92a4b5fc3a90cb683f93546644c595f83af",
    "source_lines": "L2790-L2865",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R028"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R028",
  "title": "Hệ thống phải hỗ trợ: - Direct Website",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R029 — Hệ thống phải hỗ trợ: - White-label Website

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
      "requirement_id": "BRD-WS-01-R029",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "39e109aa723f11c8585e2f57e9bfba6f24de4aa8773caa0bd339f579aebdde73"
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
        "BRD-WS-01-R029-AC001",
        "BRD-WS-01-R029-AC002",
        "BRD-WS-01-R029-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R029-O001",
      "obligation_text": "Hệ thống phải hỗ trợ: - White-label Website"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-018",
      "selected_disposition": "CONFIRM_HIGH"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Hệ thống phải hỗ trợ: - White-label Website",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-029",
    "previous_temporary_key": "TMP-BRD-WS-01-029",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Sales Channels",
    "source_context_sha256": "c51203f69e40724208e93909b1dff7733e62620546cbf8a408680d28ec69886e",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "39e109aa723f11c8585e2f57e9bfba6f24de4aa8773caa0bd339f579aebdde73",
    "source_lines": "L2867-L2951",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R029"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R029",
  "title": "Hệ thống phải hỗ trợ: - White-label Website",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R030 — Hệ thống phải hỗ trợ: - Agency

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
      "requirement_id": "BRD-WS-01-R030",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "478e83e18c26398341e116b506638f6659f8e3fa177c8ff581eea60ce2490cdd"
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
        "BRD-WS-01-R030-AC001",
        "BRD-WS-01-R030-AC002",
        "BRD-WS-01-R030-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R030-O001",
      "obligation_text": "Hệ thống phải hỗ trợ: - Agency"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Hệ thống phải hỗ trợ: - Agency",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-030",
    "previous_temporary_key": "TMP-BRD-WS-01-030",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Sales Channels",
    "source_context_sha256": "c51203f69e40724208e93909b1dff7733e62620546cbf8a408680d28ec69886e",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "478e83e18c26398341e116b506638f6659f8e3fa177c8ff581eea60ce2490cdd",
    "source_lines": "L2953-L3028",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R030"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R030",
  "title": "Hệ thống phải hỗ trợ: - Agency",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R031 — Hệ thống phải hỗ trợ: - Multi-level Distribution

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
      "requirement_id": "BRD-WS-01-R031",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "7d978ce0adc64693dff0994784ab663692af1fc626adbf6cbb2c06df4895ce09"
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
        "BRD-WS-01-R031-AC001",
        "BRD-WS-01-R031-AC002",
        "BRD-WS-01-R031-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R031-O001",
      "obligation_text": "Hệ thống phải hỗ trợ: - Multi-level Distribution"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Hệ thống phải hỗ trợ: - Multi-level Distribution",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-031",
    "previous_temporary_key": "TMP-BRD-WS-01-031",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Sales Channels",
    "source_context_sha256": "c51203f69e40724208e93909b1dff7733e62620546cbf8a408680d28ec69886e",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "7d978ce0adc64693dff0994784ab663692af1fc626adbf6cbb2c06df4895ce09",
    "source_lines": "L3030-L3105",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R031"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R031",
  "title": "Hệ thống phải hỗ trợ: - Multi-level Distribution",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R032 — Hệ thống phải hỗ trợ: - Online Seller

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
      "requirement_id": "BRD-WS-01-R032",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "642a0a7d76a4dd2f29730e27f7d3366c63a42b472fd43958147bb69fdea57948"
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
        "BRD-WS-01-R032-AC001",
        "BRD-WS-01-R032-AC002",
        "BRD-WS-01-R032-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R032-O001",
      "obligation_text": "Hệ thống phải hỗ trợ: - Online Seller"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Hệ thống phải hỗ trợ: - Online Seller",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-032",
    "previous_temporary_key": "TMP-BRD-WS-01-032",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Sales Channels",
    "source_context_sha256": "c51203f69e40724208e93909b1dff7733e62620546cbf8a408680d28ec69886e",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "642a0a7d76a4dd2f29730e27f7d3366c63a42b472fd43958147bb69fdea57948",
    "source_lines": "L3107-L3182",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R032"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R032",
  "title": "Hệ thống phải hỗ trợ: - Online Seller",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R033 — Hệ thống phải hỗ trợ: - Social Commerce

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
      "requirement_id": "BRD-WS-01-R033",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "bb0af505b8fc3234f3a21f874a03482d81488f40523c24acd6e9ee13113637cb"
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
        "BRD-WS-01-R033-AC001",
        "BRD-WS-01-R033-AC002",
        "BRD-WS-01-R033-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R033-O001",
      "obligation_text": "Hệ thống phải hỗ trợ: - Social Commerce"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Hệ thống phải hỗ trợ: - Social Commerce",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-033",
    "previous_temporary_key": "TMP-BRD-WS-01-033",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Sales Channels",
    "source_context_sha256": "c51203f69e40724208e93909b1dff7733e62620546cbf8a408680d28ec69886e",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "bb0af505b8fc3234f3a21f874a03482d81488f40523c24acd6e9ee13113637cb",
    "source_lines": "L3184-L3259",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R033"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R033",
  "title": "Hệ thống phải hỗ trợ: - Social Commerce",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R034 — Hệ thống phải hỗ trợ: - Marketplace

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
      "requirement_id": "BRD-WS-01-R034",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "2af140284c1c5f335f24db4cdeb26ecf2fa0b15814e00beeab35ab9a16ae882e"
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
        "BRD-WS-01-R034-AC001",
        "BRD-WS-01-R034-AC002",
        "BRD-WS-01-R034-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R034-O001",
      "obligation_text": "Hệ thống phải hỗ trợ: - Marketplace"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Hệ thống phải hỗ trợ: - Marketplace",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-034",
    "previous_temporary_key": "TMP-BRD-WS-01-034",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Sales Channels",
    "source_context_sha256": "c51203f69e40724208e93909b1dff7733e62620546cbf8a408680d28ec69886e",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "2af140284c1c5f335f24db4cdeb26ecf2fa0b15814e00beeab35ab9a16ae882e",
    "source_lines": "L3261-L3336",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R034"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R034",
  "title": "Hệ thống phải hỗ trợ: - Marketplace",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R035 — Hệ thống phải hỗ trợ: - API Partner

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
      "requirement_id": "BRD-WS-01-R035",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "ca6381aff7515897f641af7aa57bd052258825d1d05ddbc8650b35c409bdd65b"
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
        "BRD-WS-01-R035-AC001",
        "BRD-WS-01-R035-AC002",
        "BRD-WS-01-R035-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R035-O001",
      "obligation_text": "Hệ thống phải hỗ trợ: - API Partner"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Hệ thống phải hỗ trợ: - API Partner",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-035",
    "previous_temporary_key": "TMP-BRD-WS-01-035",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Sales Channels",
    "source_context_sha256": "c51203f69e40724208e93909b1dff7733e62620546cbf8a408680d28ec69886e",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "ca6381aff7515897f641af7aa57bd052258825d1d05ddbc8650b35c409bdd65b",
    "source_lines": "L3338-L3413",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R035"
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
  "stable_id": "BRD-WS-01-R035",
  "title": "Hệ thống phải hỗ trợ: - API Partner",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-01-R036 — Hệ thống phải hỗ trợ: - Enterprise Customer

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
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-01-R036",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "source_fingerprint": "1e948d6e6aecffa3abe6396ba9e4c79316c30bf2ca4b98d5969f55ab5d21b6a0"
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
        "BRD-WS-01-R036-AC001",
        "BRD-WS-01-R036-AC002",
        "BRD-WS-01-R036-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-01-R036-O001",
      "obligation_text": "Hệ thống phải hỗ trợ: - Enterprise Customer"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Hệ thống phải hỗ trợ: - Enterprise Customer",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-01-036",
    "previous_temporary_key": "TMP-BRD-WS-01-036",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Sales Channels",
    "source_context_sha256": "c51203f69e40724208e93909b1dff7733e62620546cbf8a408680d28ec69886e",
    "source_document": "docs/BRD/BRD-WS-01.md",
    "source_fingerprint": "1e948d6e6aecffa3abe6396ba9e4c79316c30bf2ca4b98d5969f55ab5d21b6a0",
    "source_lines": "L3415-L3494",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-01-R036"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-01-R036",
  "title": "Hệ thống phải hỗ trợ: - Enterprise Customer",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
