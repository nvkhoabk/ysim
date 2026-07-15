---
document_code: "BRD-WS-04"
title: "Product Catalog, Supplier & Product Intelligence"
product_baseline: "2.3"
document_revision: "2.3.0-draft.1"
lifecycle_status: "V2.3_DRAFT"
language: "vi-VN"
source_baseline: "v2.2"
generated_registry_role: "BRD_CANONICAL_SOURCE"
last_remediated_on: "2026-07-15"
---
## Thẩm quyền nguồn yêu cầu v2.3

Các khối `YSIM:REQUIREMENT` trong phụ lục chuẩn tắc là nguồn yêu cầu có thẩm quyền cho baseline 2.3. Nội dung legacy bên dưới được giữ làm ngữ cảnh; nếu có khác biệt, khối chuẩn tắc và các quyết định v2.3 đã phê duyệt được ưu tiên.

# BRD Workshop 04

# Product Catalog, Supplier & Product Intelligence

---

# 1. Workshop Objective

Workshop này xác định mô hình Product Catalog của YSim, phương pháp chuẩn hóa sản phẩm từ Supplier, cơ chế xây dựng Sales Catalog cho từng Organization và nền tảng Product Intelligence.

Workshop này là Foundation cho:

- Product Domain
- Catalog Domain
- Pricing
- Promotion
- Search
- Recommendation
- Allocation
- Storefront
- Analytics

---

# 2. Business Objects Introduced

| Business Object | Status |
|-----------------|--------|
| Product | Existing (WS-02) |
| Supplier Product | Existing (WS-02) |
| Product Mapping | Existing (WS-02) |
| Product Intelligence | Existing (WS-02) |
| Product Catalog | NEW |
| Master Catalog | NEW |
| Sales Catalog | NEW |
| Storefront Catalog | NEW |
| Product Category | NEW |
| Product Collection | NEW |
| Product Attribute | NEW |
| Product Tag | NEW |
| Product Version | NEW |
| Catalog Governance | NEW |

---

# 3. Four-Level Catalog Architecture

YSim sử dụng mô hình **Four-Level Catalog**.

```text
Supplier Catalog
        │
        ▼
Master Catalog (YSim)
        │
        ▼
Sales Catalog (Organization)
        │
        ▼
Storefront Catalog
```

---

# 4. Supplier Catalog

Supplier Catalog được đồng bộ từ API của Supplier.

Bao gồm:

- Supplier Product
- Product Code
- Product Attributes
- Product Policy
- Availability
- Purchase Price
- Metadata

Supplier Catalog chỉ phục vụ mục đích đồng bộ dữ liệu.

Không hiển thị trực tiếp tới khách hàng.

---

# 5. Master Catalog

Master Catalog do YSim quản lý.

Đây là Product Catalog chuẩn của toàn bộ hệ thống.

Master Catalog chịu trách nhiệm:

- Chuẩn hóa Product
- Product Mapping
- Product Specification
- Product Attribute
- Product Category
- Product Collection
- Product Version
- Product Intelligence
- Catalog Governance

Master Catalog là nguồn dữ liệu chuẩn duy nhất (Single Source of Truth).

---

# 6. Sales Catalog

Sales Catalog thuộc Organization.

Sales Catalog không tạo Product mới.

Sales Catalog chỉ tham chiếu Product trong Master Catalog.

Organization có thể:

- lựa chọn Product muốn bán
- thiết lập giá bán
- lựa chọn Currency
- thiết lập Collection
- thiết lập Tag
- thiết lập Visibility
- bổ sung nội dung Marketing
- thay đổi Product Code bằng Prefix hoặc Postfix theo quy tắc của Organization

Organization không được phép thay đổi:

- Product Specification
- Coverage
- Data Package
- Duration
- Activation Policy
- Product Attribute chuẩn
- Product Version

---

# 7. Storefront Catalog

Storefront Catalog là phần Product được Publish ra Storefront.

Storefront Catalog phục vụ:

- Website
- Landing Page
- Campaign
- Customer Portal
- QR Landing

Storefront Catalog chỉ chứa những Product được Publish.

---

# 8. Product Strategy

Product của YSim là Commercial Product.

Supplier Product là Raw Product.

Một Product của YSim có thể được tạo từ:

- một Supplier Product
- nhiều Supplier Product

Người dùng cuối chỉ nhìn thấy Product của YSim.

Không nhìn thấy Supplier Product.

---

# 9. Product Category

Product hỗ trợ nhiều Taxonomy.

Ví dụ:

Theo Country

- Thailand
- Japan
- Vietnam

Theo Region

- Asia
- Europe
- America

Theo Business Category

- Local
- Regional
- Global

Category Tree không bị giới hạn.

---

# 10. Product Collection

Collection độc lập với Category.

Ví dụ:

- Best Seller
- Featured
- Recommended
- New Arrival
- Summer Promotion
- Staff Pick

Một Product có thể thuộc nhiều Collection.

---

# 11. Product Specification

Product Specification là dữ liệu chuẩn.

Bao gồm:

- Coverage
- Country
- Region
- Total Data
- Daily Data
- Duration
- Network
- Speed
- Hotspot
- Recharge
- Top-up Extension
- Activation Policy
- Auto Renewal

Specification chỉ được quản lý tại Master Catalog.

---

# 12. Product Attribute

Product Attribute độc lập với Specification.

Ví dụ:

- Featured
- Hidden
- Recommendation
- Internal Tag
- Marketing Flag

Attribute phục vụ vận hành và marketing.

---

# 13. Product Variant

Product Variant chưa được triển khai trong phiên bản 2.0.

Nếu khác:

- Coverage
- Data
- Duration
- Activation Policy

thì được xem là Product mới.

---

# 14. Product Code

Product Code của YSim độc lập với Product Code của Supplier.

Product Code là Business Code.

UUID mới là Identity duy nhất.

Product Code có thể được sinh:

- theo quy tắc của YSim
- tham khảo Supplier Product Code
- thông qua Regex Mapping

Product Code có thể tái sử dụng nếu Product cũ đã Archive hoàn toàn.

UUID không bao giờ thay đổi.

---

# 15. Supplier Product

Supplier Product được đồng bộ từ API.

Một Supplier Product có thể bao gồm:

- plan_id
- supplier_product_code
- product_name
- package_description
- hotspot
- apn
- network_type
- countries
- operator
- parent_group_id
- parent_group_name
- total_data
- daily_data
- validity
- topup_extension
- activation_policy

YSim hỗ trợ Attribute Mapping.

Không hardcode theo từng Supplier.

---

# 16. Product Version

Nếu Supplier thay đổi:

- Product Policy
- Product Specification
- Activation Rule
- Product Behavior

YSim tạo Product Version mới.

Version luôn đi kèm Publish Workflow.

Không Publish tự động.

---

# 17. Catalog Governance

Catalog Governance chịu trách nhiệm:

- Validation
- Publish Workflow
- Warning
- Approval
- Audit

Ví dụ:

Partner thiết lập giá bán thấp hơn giá vốn.

↓

Warning

↓

Reason Required

↓

Audit

↓

Parent Notification

---

# 18. Catalog Synchronization

Supplier Catalog được đồng bộ định kỳ.

Quy trình bao gồm:

- Pull Product
- Compare
- Detect New Product
- Detect Removed Product
- Detect Price Change
- Detect Policy Change
- Detect Availability Change
- Detect Attribute Change

Nếu có thay đổi:

↓

Warning

↓

Operator Review

↓

Publish

---

# 19. Product Intelligence

Phiên bản 2.0 chỉ triển khai:

- Product Synchronization
- Difference Detection
- Price Change Detection
- Policy Change Detection
- Availability Detection
- Missing Mapping Detection

Các chức năng AI sẽ triển khai ở phiên bản sau.

---

# 20. Sales Catalog Governance

Sales Catalog thuộc Organization.

Sales Catalog có thể:

- thêm Product từ Master Catalog
- ẩn Product
- thiết lập giá bán
- thiết lập Currency
- thiết lập Collection
- thiết lập Marketing Content

Sales Catalog không được sửa Product Specification.

---

# 21. Currency Governance

Currency là một phần của Commercial Agreement.

Organization chỉ được sử dụng Currency đã được Parent Organization phê duyệt.

Muốn bổ sung Currency mới:

Request

↓

Parent Approval

↓

Exchange Rate Agreement

↓

Effective Date

↓

Activate Currency

Việc thay đổi Exchange Rate phải được thống nhất giữa Organization và Parent.

---

# 22. Search & Recommendation

Search hỗ trợ:

- Country
- Region
- Total Data
- Daily Data
- Duration
- Keyword
- Tag
- AI Search

Recommendation hỗ trợ:

- Similar Product
- Best Seller
- Recommended
- Higher Package
- Lower Price

---

# 23. Catalog Lifecycle

Sales Catalog có vòng đời:

```text
Draft
    │
    ▼
Active
    │
    ▼
Hidden
    │
    ▼
Archived
```

Master Catalog sử dụng Publish Workflow độc lập.

---

# 24. Business Decisions (Locked)

## BD-04-001

YSim sử dụng mô hình Four-Level Catalog:

- Supplier Catalog
- Master Catalog
- Sales Catalog
- Storefront Catalog

---

## BD-04-002

Sales Catalog thuộc Organization.

---

## BD-04-003

Sales Catalog chỉ tham chiếu Master Product.

Không sao chép Product.

---

## BD-04-004

Product Specification chỉ được quản lý tại Master Catalog.

---

## BD-04-005

Organization chỉ được thay đổi:

- Selling Price
- Currency
- Collection
- Visibility
- Marketing Content
- Product Code Prefix/Postfix

---

## BD-04-006

Product Version được tạo khi Supplier thay đổi Policy hoặc Specification.

---

## BD-04-007

Product Variant chưa triển khai trong phiên bản 2.0.

---

## BD-04-008

Supplier Attribute Mapping phải hỗ trợ cấu hình.

Không hardcode.

---

## BD-04-009

Catalog Publish sử dụng Workflow.

Không Publish trực tiếp.

---

## BD-04-010

Currency là một phần của Commercial Agreement giữa Organization và Parent.

---

## BD-04-011

Product Intelligence phiên bản 2.0 chỉ tập trung vào Synchronization và Difference Detection.

---

# 25. Four-Level Catalog Model

```text
                        Supplier Catalog
                               │
                      Supplier Product
                               │
                    Catalog Synchronization
                               │
                               ▼
                    Master Catalog (YSim)
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
 Product Specification   Product Intelligence   Product Version
          │                    │                    │
          └────────────────────┼────────────────────┘
                               │
                               ▼
                 Sales Catalog (Organization)
                               │
        ┌─────────────┬─────────────┬──────────────┬──────────────┐
        │             │             │              │
     Price        Currency     Collection    Marketing Content
        │             │             │              │
        └─────────────┴─────────────┴──────────────┘
                               │
                               ▼
                     Storefront Catalog
                               │
                               ▼
                         End Customer
```

---

# 26. Traceability

Workshop được xây dựng dựa trên:

- BRD Workshop 01
- BRD Workshop 02
- BRD Workshop 03
- Kinh nghiệm triển khai YSim v1.0
- Mô hình White-label Commerce Platform
- Mô hình Multi-level Distribution

---

# 27. Impacts to Other Domains

Workshop này ảnh hưởng trực tiếp tới:

- DMS – Product Domain
- DMS – Catalog Domain
- DMS – Supplier Domain
- DBD – Product, Product Catalog, Sales Catalog
- Pricing Engine
- Promotion Engine
- Search Engine
- Recommendation Engine
- Allocation Engine
- Storefront
- Admin Portal
- Partner Portal
- Customer Portal
- API Specification
- SATP

---

# 28. Workshop Status

**Status:** FROZEN

Workshop này là Foundation cho:

- Product Catalog
- Pricing
- Promotion
- Search
- Recommendation
- Allocation
- Product Intelligence
- Storefront

---

# 29. Next Workshop

**BRD-WS-05 – Pricing, Commercial Policy & Revenue Model**

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-04-001 — YSim sử dụng mô hình Four-Level Catalog: - Supplier Catalog - Master Catalog - Sales Catalog - S…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-001-AC001",
      "given": "the applicable business context, actor, and input for YSim sử dụng mô hình Four-Level Catalog: - Supplier Catalog - Master Catalog - Sales Catalog - S…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-001-AC002",
      "given": "the applicable business context, actor, and input for YSim sử dụng mô hình Four-Level Catalog: - Supplier Catalog - Master Catalog - Sales Catalog - S…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-001-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-001-AC003",
      "given": "the applicable business context, actor, and input for YSim sử dụng mô hình Four-Level Catalog: - Supplier Catalog - Master Catalog - Sales Catalog - S…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-001-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-001-AC004",
      "given": "the applicable business context, actor, and input for YSim sử dụng mô hình Four-Level Catalog: - Supplier Catalog - Master Catalog - Sales Catalog - S…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-001-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-04-001-AC005",
      "given": "an unsupported or invalid business input at the boundary governed by YSim sử dụng mô hình Four-Level Catalog: - Supplier Catalog - Master Catalog - Sales Catalog - S…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-04-001-O001",
        "BD-04-001-O002",
        "BD-04-001-O003",
        "BD-04-001-O004"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-04-001-AC001",
        "BD-04-001-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-001-O001",
      "obligation_text": "YSim sử dụng mô hình Four-Level Catalog: Supplier Catalog."
    },
    {
      "acceptance_criterion_references": [
        "BD-04-001-AC002",
        "BD-04-001-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-001-O002",
      "obligation_text": "YSim sử dụng mô hình Four-Level Catalog: Master Catalog."
    },
    {
      "acceptance_criterion_references": [
        "BD-04-001-AC003",
        "BD-04-001-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-001-O003",
      "obligation_text": "YSim sử dụng mô hình Four-Level Catalog: Sales Catalog."
    },
    {
      "acceptance_criterion_references": [
        "BD-04-001-AC004",
        "BD-04-001-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-001-O004",
      "obligation_text": "YSim sử dụng mô hình Four-Level Catalog: Storefront Catalog."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "YSim sử dụng mô hình Four-Level Catalog: - Supplier Catalog - Master Catalog - Sales Catalog - Storefront Catalog",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-04-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-04-001",
    "source_context_sha256": "678620f32e0db94988f43ea4b56d23e284fd5b41953e9520fb328b5bc66e233d",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "63df232f43395e2a0fe801be558496ee7e5c652dc21b08b269c0b52ca6e99acf",
    "source_lines": "L521-L529",
    "source_section": "24. Business Decisions (Locked) > BD-04-001"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-04-001",
  "title": "YSim sử dụng mô hình Four-Level Catalog: - Supplier Catalog - Master Catalog - Sales Catalog - S…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-04-002 — Sales Catalog thuộc Organization

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-002-AC001",
      "given": "the applicable business context, actor, and input for Sales Catalog thuộc Organization",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-04-002-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Sales Catalog thuộc Organization",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-04-002-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-04-002-AC001",
        "BD-04-002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-002-O001",
      "obligation_text": "Sales Catalog thuộc Organization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sales Catalog thuộc Organization.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-04-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Sales Catalog",
    "source_context_sha256": "93060d1ad79d5976f5cfade005f283427b423ec1bc4931f5881ea8338ceb30c8",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "be311ffaaf3ac0a04057cf20a10930b5a3e9d29994a7e7ca6d4f22bdbecddc73",
    "source_lines": "L532-L535",
    "source_section": "24. Business Decisions (Locked) > BD-04-002"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-04-002",
  "title": "Sales Catalog thuộc Organization",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-04-003 — Sales Catalog chỉ tham chiếu Master Product. Không sao chép Product

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-003-AC001",
      "given": "the applicable business context, actor, and input for Sales Catalog chỉ tham chiếu Master Product. Không sao chép Product",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-003-AC002",
      "given": "the applicable business context, actor, and input for Sales Catalog chỉ tham chiếu Master Product. Không sao chép Product",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-003-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-04-003-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Sales Catalog chỉ tham chiếu Master Product. Không sao chép Product",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-04-003-O001",
        "BD-04-003-O002"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-04-003-AC001",
        "BD-04-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-003-O001",
      "obligation_text": "Sales Catalog chỉ tham chiếu Master Product"
    },
    {
      "acceptance_criterion_references": [
        "BD-04-003-AC002",
        "BD-04-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-003-O002",
      "obligation_text": "Không sao chép Product"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sales Catalog chỉ tham chiếu Master Product. Không sao chép Product.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-04-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-04-003",
    "source_context_sha256": "314375f19ac326307972255814629ada8cedcc65af444144b2a6e663b7690f36",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "b4c933ec320c50ad16d7be6facda33019bb8c6857fcbcb69f81d04fe8d00ea5a",
    "source_lines": "L538-L543",
    "source_section": "24. Business Decisions (Locked) > BD-04-003"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-04-003",
  "title": "Sales Catalog chỉ tham chiếu Master Product. Không sao chép Product",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-04-004 — Product Specification chỉ được quản lý tại Master Catalog

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-004-AC001",
      "given": "the applicable business context, actor, and input for Product Specification chỉ được quản lý tại Master Catalog",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-04-004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Product Specification chỉ được quản lý tại Master Catalog",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-04-004-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-04-004-AC001",
        "BD-04-004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-004-O001",
      "obligation_text": "Product Specification chỉ được quản lý tại Master Catalog"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Product Specification chỉ được quản lý tại Master Catalog.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-04-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-04-004",
    "source_context_sha256": "f6db0eee9a0222fac12d792701d207d12e9c92509adc93ba801016d995a878f0",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "1d9260d8f6a1b3b47f387db94ad87ef606f4f62efab1ef68da4759cfe6eb9623",
    "source_lines": "L546-L549",
    "source_section": "24. Business Decisions (Locked) > BD-04-004"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-04-004",
  "title": "Product Specification chỉ được quản lý tại Master Catalog",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-04-005 — Organization chỉ được thay đổi: - Selling Price - Currency - Collection - Visibility - Marketing…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-005-AC001",
      "given": "the applicable business context, actor, and input for Organization chỉ được thay đổi: - Selling Price - Currency - Collection - Visibility - Marketing…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-005-AC002",
      "given": "the applicable business context, actor, and input for Organization chỉ được thay đổi: - Selling Price - Currency - Collection - Visibility - Marketing…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-005-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-005-AC003",
      "given": "the applicable business context, actor, and input for Organization chỉ được thay đổi: - Selling Price - Currency - Collection - Visibility - Marketing…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-005-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-005-AC004",
      "given": "the applicable business context, actor, and input for Organization chỉ được thay đổi: - Selling Price - Currency - Collection - Visibility - Marketing…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-005-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-005-AC005",
      "given": "the applicable business context, actor, and input for Organization chỉ được thay đổi: - Selling Price - Currency - Collection - Visibility - Marketing…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-005-O005"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-005-AC006",
      "given": "the applicable business context, actor, and input for Organization chỉ được thay đổi: - Selling Price - Currency - Collection - Visibility - Marketing…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-005-O006"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-04-005-AC007",
      "given": "an unsupported or invalid business input at the boundary governed by Organization chỉ được thay đổi: - Selling Price - Currency - Collection - Visibility - Marketing…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-04-005-O001",
        "BD-04-005-O002",
        "BD-04-005-O003",
        "BD-04-005-O004",
        "BD-04-005-O005",
        "BD-04-005-O006"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-04-005-AC001",
        "BD-04-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-005-O001",
      "obligation_text": "Organization chỉ được thay đổi: Selling Price."
    },
    {
      "acceptance_criterion_references": [
        "BD-04-005-AC002",
        "BD-04-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-005-O002",
      "obligation_text": "Organization chỉ được thay đổi: Currency."
    },
    {
      "acceptance_criterion_references": [
        "BD-04-005-AC003",
        "BD-04-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-005-O003",
      "obligation_text": "Organization chỉ được thay đổi: Collection."
    },
    {
      "acceptance_criterion_references": [
        "BD-04-005-AC004",
        "BD-04-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-005-O004",
      "obligation_text": "Organization chỉ được thay đổi: Visibility."
    },
    {
      "acceptance_criterion_references": [
        "BD-04-005-AC005",
        "BD-04-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-005-O005",
      "obligation_text": "Organization chỉ được thay đổi: Marketing Content."
    },
    {
      "acceptance_criterion_references": [
        "BD-04-005-AC006",
        "BD-04-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-005-O006",
      "obligation_text": "Organization chỉ được thay đổi: Product Code Prefix/Postfix."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-04-005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-04-005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-04-005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-04-005 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-04-005-AC001",
        "BD-04-005-AC002",
        "BD-04-005-AC003",
        "BD-04-005-AC004",
        "BD-04-005-AC005",
        "BD-04-005-AC006"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-04-005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization chỉ được thay đổi: - Selling Price - Currency - Collection - Visibility - Marketing Content - Product Code Prefix/Postfix",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-04-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-04-005",
    "source_context_sha256": "24d95e4f0271bbc330b7b12041ecafe1e701df2926c8634bd172b8be41e2e529",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
    "source_lines": "L552-L562",
    "source_section": "24. Business Decisions (Locked) > BD-04-005"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-04-005",
  "title": "Organization chỉ được thay đổi: - Selling Price - Currency - Collection - Visibility - Marketing…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-04-006 — Product Version được tạo khi Supplier thay đổi Policy hoặc Specification

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-006-AC001",
      "given": "the applicable business context, actor, and input for Product Version được tạo khi Supplier thay đổi Policy hoặc Specification",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-04-006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Product Version được tạo khi Supplier thay đổi Policy hoặc Specification",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-04-006-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-04-006-AC001",
        "BD-04-006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-006-O001",
      "obligation_text": "Product Version được tạo khi Supplier thay đổi Policy hoặc Specification"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Product Version được tạo khi Supplier thay đổi Policy hoặc Specification.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-04-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-04-006",
    "source_context_sha256": "95a288a64ee23b3b36c6ac9374fb2c7145018b67c6b69b7c58e5bddb165eb31f",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "2390b42c438c0c93477060d2ddf7da07772be536b6ad6d8d64771fd67cd9fd5e",
    "source_lines": "L565-L568",
    "source_section": "24. Business Decisions (Locked) > BD-04-006"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-04-006",
  "title": "Product Version được tạo khi Supplier thay đổi Policy hoặc Specification",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-04-007 — Product Variant outside v2.3

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "EARLIER_EXPLICIT_HUMAN_DECISION",
      "exception_id": "P2-CRIT-EXC-001",
      "selected_disposition": "ROUTE_TO_SCOPE_REMEDIATION"
    }
  ],
  "criticality_unit": false,
  "delivery_commitment": "EXCLUDED_FROM_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Product Variant nằm ngoài phạm vi sản phẩm v2.3.",
  "provenance": {
    "approved_decisions": [
      "SD-02"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-04-007",
    "previous_temporary_key": null,
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-04-007",
    "source_context_sha256": "ad74cdbab86309f762bd8522f6c7e8d3301e0381903feb80431b4d4ed80689c0",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "d8c31f2ec78bac7b115dd5523d9144523d425ef4fe50d7b49da301e631d6f283",
    "source_lines": "L571-L574",
    "source_section": "24. Business Decisions (Locked) > BD-04-007"
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
  "stable_id": "BD-04-007",
  "title": "Product Variant outside v2.3",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-04-008 — Supplier Attribute Mapping phải hỗ trợ cấu hình. Không hardcode

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-008-AC001",
      "given": "the applicable business context, actor, and input for Supplier Attribute Mapping phải hỗ trợ cấu hình. Không hardcode",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-04-008-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-008-AC002",
      "given": "the applicable business context, actor, and input for Supplier Attribute Mapping phải hỗ trợ cấu hình. Không hardcode",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-04-008-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-04-008-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-008-O001",
      "obligation_text": "Supplier Attribute Mapping phải hỗ trợ cấu hình"
    },
    {
      "acceptance_criterion_references": [
        "BD-04-008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-008-O002",
      "obligation_text": "Không hardcode"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier Attribute Mapping phải hỗ trợ cấu hình. Không hardcode.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-04-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-04-008",
    "source_context_sha256": "6a801dc222070147cc09b1a572a98c06c34b0921c5d60988dd3ddb6af15f2b9a",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "678aab58550234a0b592f8ccf90524534852790f3abdb11593a95357e6676338",
    "source_lines": "L577-L582",
    "source_section": "24. Business Decisions (Locked) > BD-04-008"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-04-008",
  "title": "Supplier Attribute Mapping phải hỗ trợ cấu hình. Không hardcode",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-04-009 — Catalog Publish sử dụng Workflow. Không Publish trực tiếp

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-009-AC001",
      "given": "the applicable business context, actor, and input for Catalog Publish sử dụng Workflow. Không Publish trực tiếp",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-009-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-009-AC002",
      "given": "the applicable business context, actor, and input for Catalog Publish sử dụng Workflow. Không Publish trực tiếp",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-009-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-04-009-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Catalog Publish sử dụng Workflow. Không Publish trực tiếp",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-04-009-O001",
        "BD-04-009-O002"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-04-009-AC001",
        "BD-04-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-009-O001",
      "obligation_text": "Catalog Publish sử dụng Workflow"
    },
    {
      "acceptance_criterion_references": [
        "BD-04-009-AC002",
        "BD-04-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-009-O002",
      "obligation_text": "Không Publish trực tiếp"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Catalog Publish sử dụng Workflow. Không Publish trực tiếp.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-04-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-04-009",
    "source_context_sha256": "e12eb544e70d04f47791f8efba55cd05590b1adfe8285af1759df39ebc478a96",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "01d70a8a53d1d1530d17335c147365f3037e568d3cafbbc4c3f9763874111389",
    "source_lines": "L585-L590",
    "source_section": "24. Business Decisions (Locked) > BD-04-009"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-04-009",
  "title": "Catalog Publish sử dụng Workflow. Không Publish trực tiếp",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-04-010 — Currency là một phần của Commercial Agreement giữa Organization và Parent

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-010-AC001",
      "given": "the applicable business context, actor, and input for Currency là một phần của Commercial Agreement giữa Organization và Parent",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-010-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-04-010-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Currency là một phần của Commercial Agreement giữa Organization và Parent",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-04-010-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-04-010-AC001",
        "BD-04-010-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-010-O001",
      "obligation_text": "Currency là một phần của Commercial Agreement giữa Organization và Parent"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-04-010 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-04-010 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-04-010 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-04-010 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-04-010-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-04-010 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Currency là một phần của Commercial Agreement giữa Organization và Parent.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-04-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-04-010",
    "source_context_sha256": "89425b281051fe06bc32986c908b27503edefdd463b15a4b0c7adf948b6d7095",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "3607bf1995c38394243af4e86dfcc3e68d5e7edf655cd53b7062e1d9d9853b36",
    "source_lines": "L593-L596",
    "source_section": "24. Business Decisions (Locked) > BD-04-010"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-04-010",
  "title": "Currency là một phần của Commercial Agreement giữa Organization và Parent",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-04-011 — Product Intelligence phiên bản 2.0 chỉ tập trung vào Synchronization và Difference Detection

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-04-011-AC001",
      "given": "the applicable business context, actor, and input for Product Intelligence phiên bản 2.0 chỉ tập trung vào Synchronization và Difference Detection",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-04-011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-04-011-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Product Intelligence phiên bản 2.0 chỉ tập trung vào Synchronization và Difference Detection",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-04-011-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-04-011-AC001",
        "BD-04-011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-011-O001",
      "obligation_text": "Product Intelligence phiên bản 2.0 chỉ tập trung vào Synchronization và Difference Detection"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Product Intelligence phiên bản 2.0 chỉ tập trung vào Synchronization và Difference Detection.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-04-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-04-011",
    "source_context_sha256": "18d0be241f786934d094515ebce0c57dda34004475f0a083a219f90eb2d280cd",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "5e81b5b9e39434126d9da1f4945d05c055fb655c942d404d2e2f24eee4bb575a",
    "source_lines": "L599-L602",
    "source_section": "24. Business Decisions (Locked) > BD-04-011"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-04-011",
  "title": "Product Intelligence phiên bản 2.0 chỉ tập trung vào Synchronization và Difference Detection",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R001 — Master Catalog là nguồn dữ liệu chuẩn duy nhất (Single Source of Truth)

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R001-AC001",
      "given": "the applicable business context, actor, and input for Master Catalog là nguồn dữ liệu chuẩn duy nhất (Single Source of Truth)",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-04-R001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-04-R001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Master Catalog là nguồn dữ liệu chuẩn duy nhất (Single Source of Truth)",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-04-R001-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R001-AC001",
        "BRD-WS-04-R001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R001-O001",
      "obligation_text": "Master Catalog là nguồn dữ liệu chuẩn duy nhất (Single Source of Truth)"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Master Catalog là nguồn dữ liệu chuẩn duy nhất (Single Source of Truth).",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-001",
    "previous_temporary_key": "TMP-BRD-WS-04-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Master Catalog",
    "source_context_sha256": "6904959a694aac59e1f248d5fb51198fd6de46b6467223970721c14e264e13c4",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "d8d7e85239280a630ed727ecb05c7fef2b537a7773e0327806cf9488759289cd",
    "source_lines": "L116",
    "source_section": "5. Master Catalog"
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
  "stable_id": "BRD-WS-04-R001",
  "title": "Master Catalog là nguồn dữ liệu chuẩn duy nhất (Single Source of Truth)",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R002 — Organization không được phép thay đổi: - Product Specification

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R002-AC001",
      "given": "the applicable business context, actor, and input for Organization không được phép thay đổi: - Product Specification",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-04-R002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-04-R002-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Organization không được phép thay đổi: - Product Specification",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-04-R002-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R002-AC001",
        "BRD-WS-04-R002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R002-O001",
      "obligation_text": "Organization không được phép thay đổi: - Product Specification"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization không được phép thay đổi: - Product Specification",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-002",
    "previous_temporary_key": "TMP-BRD-WS-04-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Sales Catalog",
    "source_context_sha256": "93060d1ad79d5976f5cfade005f283427b423ec1bc4931f5881ea8338ceb30c8",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "39190b821e393a5c136483d87a4b55b15c2ccaaa5f78cf51672e54a0936f58ab",
    "source_lines": "L139-L141",
    "source_section": "6. Sales Catalog"
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
  "stable_id": "BRD-WS-04-R002",
  "title": "Organization không được phép thay đổi: - Product Specification",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R003 — Organization không được phép thay đổi: - Coverage

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R003-AC001",
      "given": "the applicable business context, actor, and input for Organization không được phép thay đổi: - Coverage",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-04-R003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-04-R003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Organization không được phép thay đổi: - Coverage",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-04-R003-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R003-AC001",
        "BRD-WS-04-R003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R003-O001",
      "obligation_text": "Organization không được phép thay đổi: - Coverage"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization không được phép thay đổi: - Coverage",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-003",
    "previous_temporary_key": "TMP-BRD-WS-04-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Sales Catalog",
    "source_context_sha256": "93060d1ad79d5976f5cfade005f283427b423ec1bc4931f5881ea8338ceb30c8",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "dfe994376efbc43bcfb2f08bb71f2eace62f49c696c43bb7f99a1110bd48892c",
    "source_lines": "L139-L142",
    "source_section": "6. Sales Catalog"
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
  "stable_id": "BRD-WS-04-R003",
  "title": "Organization không được phép thay đổi: - Coverage",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R004 — Organization không được phép thay đổi: - Data Package

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R004-AC001",
      "given": "the applicable business context, actor, and input for Organization không được phép thay đổi: - Data Package",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-04-R004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-04-R004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Organization không được phép thay đổi: - Data Package",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-04-R004-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R004-AC001",
        "BRD-WS-04-R004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R004-O001",
      "obligation_text": "Organization không được phép thay đổi: - Data Package"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization không được phép thay đổi: - Data Package",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-004",
    "previous_temporary_key": "TMP-BRD-WS-04-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Sales Catalog",
    "source_context_sha256": "93060d1ad79d5976f5cfade005f283427b423ec1bc4931f5881ea8338ceb30c8",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "75bf2951534fa9aabeacfe37214f47e2d5e3e8ad9d09e3eca45dd5ec99a1e008",
    "source_lines": "L139-L143",
    "source_section": "6. Sales Catalog"
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
  "stable_id": "BRD-WS-04-R004",
  "title": "Organization không được phép thay đổi: - Data Package",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R005 — Organization không được phép thay đổi: - Duration

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R005-AC001",
      "given": "the applicable business context, actor, and input for Organization không được phép thay đổi: - Duration",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-04-R005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-04-R005-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Organization không được phép thay đổi: - Duration",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-04-R005-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R005-AC001",
        "BRD-WS-04-R005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R005-O001",
      "obligation_text": "Organization không được phép thay đổi: - Duration"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization không được phép thay đổi: - Duration",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-005",
    "previous_temporary_key": "TMP-BRD-WS-04-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Sales Catalog",
    "source_context_sha256": "93060d1ad79d5976f5cfade005f283427b423ec1bc4931f5881ea8338ceb30c8",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "4bfcc3c67f19c7c550458b9ef7bd55dcb9b7c1f2f8d2a6232707894b24e6565e",
    "source_lines": "L139-L144",
    "source_section": "6. Sales Catalog"
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
  "stable_id": "BRD-WS-04-R005",
  "title": "Organization không được phép thay đổi: - Duration",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R006 — Organization không được phép thay đổi: - Activation Policy

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R006-AC001",
      "given": "the applicable business context, actor, and input for Organization không được phép thay đổi: - Activation Policy",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-04-R006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-04-R006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Organization không được phép thay đổi: - Activation Policy",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-04-R006-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R006-AC001",
        "BRD-WS-04-R006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R006-O001",
      "obligation_text": "Organization không được phép thay đổi: - Activation Policy"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization không được phép thay đổi: - Activation Policy",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-006",
    "previous_temporary_key": "TMP-BRD-WS-04-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Sales Catalog",
    "source_context_sha256": "93060d1ad79d5976f5cfade005f283427b423ec1bc4931f5881ea8338ceb30c8",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "91575869ae2b92cc948eabb2c5234c060deb84fd0ee514ac838b01dc3278eb65",
    "source_lines": "L139-L145",
    "source_section": "6. Sales Catalog"
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
  "stable_id": "BRD-WS-04-R006",
  "title": "Organization không được phép thay đổi: - Activation Policy",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R007 — Organization không được phép thay đổi: - Product Attribute chuẩn

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R007-AC001",
      "given": "the applicable business context, actor, and input for Organization không được phép thay đổi: - Product Attribute chuẩn",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-04-R007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-04-R007-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Organization không được phép thay đổi: - Product Attribute chuẩn",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-04-R007-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R007-AC001",
        "BRD-WS-04-R007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R007-O001",
      "obligation_text": "Organization không được phép thay đổi: - Product Attribute chuẩn"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization không được phép thay đổi: - Product Attribute chuẩn",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-007",
    "previous_temporary_key": "TMP-BRD-WS-04-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Sales Catalog",
    "source_context_sha256": "93060d1ad79d5976f5cfade005f283427b423ec1bc4931f5881ea8338ceb30c8",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "4a1c7adcb2fc7ef67ce1a5462fb8b3c196718cc6469212a64716df250f630d82",
    "source_lines": "L139-L146",
    "source_section": "6. Sales Catalog"
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
  "stable_id": "BRD-WS-04-R007",
  "title": "Organization không được phép thay đổi: - Product Attribute chuẩn",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R008 — Organization không được phép thay đổi: - Product Version

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R008-AC001",
      "given": "the applicable business context, actor, and input for Organization không được phép thay đổi: - Product Version",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-04-R008-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-04-R008-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Organization không được phép thay đổi: - Product Version",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-04-R008-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R008-AC001",
        "BRD-WS-04-R008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R008-O001",
      "obligation_text": "Organization không được phép thay đổi: - Product Version"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization không được phép thay đổi: - Product Version",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-008",
    "previous_temporary_key": "TMP-BRD-WS-04-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Sales Catalog",
    "source_context_sha256": "93060d1ad79d5976f5cfade005f283427b423ec1bc4931f5881ea8338ceb30c8",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "3d64b5b95b6fc76c88b1e747429c226654abe2519288e54d612870138015808d",
    "source_lines": "L139-L147",
    "source_section": "6. Sales Catalog"
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
  "stable_id": "BRD-WS-04-R008",
  "title": "Organization không được phép thay đổi: - Product Version",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R009 — Specification chỉ được quản lý tại Master Catalog

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R009-AC001",
      "given": "the applicable business context, actor, and input for Specification chỉ được quản lý tại Master Catalog",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-04-R009-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-04-R009-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Specification chỉ được quản lý tại Master Catalog",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-04-R009-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R009-AC001",
        "BRD-WS-04-R009-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R009-O001",
      "obligation_text": "Specification chỉ được quản lý tại Master Catalog"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Specification chỉ được quản lý tại Master Catalog.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-009",
    "previous_temporary_key": "TMP-BRD-WS-04-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Product Specification",
    "source_context_sha256": "0e3f3cfb1e6a1e2f5b27c6c3c92f09b2e5cf1510bdbcad1335ed395ea153a5da",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "2a047573a2af85d14843a52261cba5f8a18984208b73bb0d9b977431d4523f9e",
    "source_lines": "L249",
    "source_section": "11. Product Specification"
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
  "stable_id": "BRD-WS-04-R009",
  "title": "Specification chỉ được quản lý tại Master Catalog",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R010 — UUID mới là Identity duy nhất

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R010-AC001",
      "given": "the applicable business context, actor, and input for UUID mới là Identity duy nhất",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-04-R010-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-04-R010-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by UUID mới là Identity duy nhất",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-04-R010-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R010-AC001",
        "BRD-WS-04-R010-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R010-O001",
      "obligation_text": "UUID mới là Identity duy nhất"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R010 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R010 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R010 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R010 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-04-R010-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R010 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "UUID mới là Identity duy nhất.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-010",
    "previous_temporary_key": "TMP-BRD-WS-04-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "14. Product Code",
    "source_context_sha256": "02b5adf9cb4416c7384d4b32e9be846442912f957aca391d9778d49b6c40337e",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "e2c8b4e01d1c787f40cadd569f0ade53823324592972668b8a93050c2037af8c",
    "source_lines": "L290",
    "source_section": "14. Product Code"
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
  "stable_id": "BRD-WS-04-R010",
  "title": "UUID mới là Identity duy nhất",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R011 — Version luôn đi kèm Publish Workflow

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R011-AC001",
      "given": "the applicable business context, actor, and input for Version luôn đi kèm Publish Workflow",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-04-R011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-04-R011-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Version luôn đi kèm Publish Workflow",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-04-R011-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R011-AC001",
        "BRD-WS-04-R011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R011-O001",
      "obligation_text": "Version luôn đi kèm Publish Workflow"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Version luôn đi kèm Publish Workflow.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-011",
    "previous_temporary_key": "TMP-BRD-WS-04-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Product Version",
    "source_context_sha256": "e9410d76d17f90c82beb3d0eaf9adb331f726c739666d65d585cd1d4e4ef325b",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "6bb54d0a12e1641c981d8a0c8e6b57e2d2ce0b1d0557481228ef9aaa7b3b9fb6",
    "source_lines": "L344",
    "source_section": "16. Product Version"
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
  "stable_id": "BRD-WS-04-R011",
  "title": "Version luôn đi kèm Publish Workflow",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R012 — Reason Required

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R012-AC001",
      "given": "the applicable business context, actor, and input for Reason Required",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-04-R012-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-04-R012-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Reason Required",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-04-R012-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R012-AC001",
        "BRD-WS-04-R012-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R012-O001",
      "obligation_text": "Reason Required"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reason Required",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-012",
    "previous_temporary_key": "TMP-BRD-WS-04-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Catalog Governance",
    "source_context_sha256": "5287113b99d41e48aba0d41c3f941a52825e698b73d52e3968e7fe81040b40fe",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "1ad7dbe6622c151dd37051417ce4fbe800e64b01e46060c31fc80a64dbf6d7ac",
    "source_lines": "L370",
    "source_section": "17. Catalog Governance"
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
  "stable_id": "BRD-WS-04-R012",
  "title": "Reason Required",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R013 — Các chức năng AI sẽ triển khai ở phiên bản sau

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
  "normative_statement": "Các chức năng AI sẽ triển khai ở phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-013",
    "previous_temporary_key": "TMP-BRD-WS-04-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Product Intelligence",
    "source_context_sha256": "b7f02eb97c2804f5ee01f93e64746281f9d2ba0a695050c0921f015020b51bf9",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "d02b5899938011561e7bb251bde6c97b0f38c6386627dee0b20a20720da5f7be",
    "source_lines": "L424",
    "source_section": "19. Product Intelligence"
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
  "stable_id": "BRD-WS-04-R013",
  "title": "Các chức năng AI sẽ triển khai ở phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R014 — Sales Catalog không được sửa Product Specification

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R014-AC001",
      "given": "the applicable business context, actor, and input for Sales Catalog không được sửa Product Specification",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-04-R014-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-04-R014-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Sales Catalog không được sửa Product Specification",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-04-R014-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R014-AC001",
        "BRD-WS-04-R014-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R014-O001",
      "obligation_text": "Sales Catalog không được sửa Product Specification"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sales Catalog không được sửa Product Specification.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-014",
    "previous_temporary_key": "TMP-BRD-WS-04-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Sales Catalog Governance",
    "source_context_sha256": "01c984c64cc19a7215e2a0b2b3e54bf3e21fd4331260ffbcf5cde9b9e2b753c6",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "a86254033bd80e5cec398da0e538b646685b87d1ed5808fec023dbd31f9ba989",
    "source_lines": "L441",
    "source_section": "20. Sales Catalog Governance"
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
  "stable_id": "BRD-WS-04-R014",
  "title": "Sales Catalog không được sửa Product Specification",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R015 — Organization chỉ được sử dụng Currency đã được Parent Organization phê duyệt

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R015-AC001",
      "given": "the applicable business context, actor, and input for Organization chỉ được sử dụng Currency đã được Parent Organization phê duyệt",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "BRD-WS-04-R015-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_APPROVAL_BOUNDARY_V1",
      "criterion_id": "BRD-WS-04-R015-AC002",
      "given": "a governed change with missing, expired, rejected, or unauthorized approval under Organization chỉ được sử dụng Currency đã được Parent Organization phê duyệt",
      "observable_evidence": "change identity, approval policy and status, approver authorization, rejection or pending reason, and unchanged accepted state",
      "then": "the change does not enter the accepted state and the approval reason and status remain observable",
      "verifies": [
        "BRD-WS-04-R015-O001"
      ],
      "when": "the change is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R015-AC001",
        "BRD-WS-04-R015-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R015-O001",
      "obligation_text": "Organization chỉ được sử dụng Currency đã được Parent Organization phê duyệt"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R015 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R015 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R015 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R015 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-04-R015-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R015 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization chỉ được sử dụng Currency đã được Parent Organization phê duyệt.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-015",
    "previous_temporary_key": "TMP-BRD-WS-04-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Currency Governance",
    "source_context_sha256": "813b59bdc4285ee8bd17cc6d2b347e2cc3c353ffdf6fdfbc8ffcb1e432ab5404",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "8283a6799953a079b2cc0e454b9e40ad6c009841073997a546314d14ee10da5f",
    "source_lines": "L449",
    "source_section": "21. Currency Governance"
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
  "stable_id": "BRD-WS-04-R015",
  "title": "Organization chỉ được sử dụng Currency đã được Parent Organization phê duyệt",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R016 — Việc thay đổi Exchange Rate phải được thống nhất giữa Organization và Parent

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-04-R016-AC001",
      "given": "the applicable business context, actor, and input for Việc thay đổi Exchange Rate phải được thống nhất giữa Organization và Parent",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-04-R016-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-04-R016-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Việc thay đổi Exchange Rate phải được thống nhất giữa Organization và Parent",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-04-R016-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-04-R016-AC001",
        "BRD-WS-04-R016-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R016-O001",
      "obligation_text": "Việc thay đổi Exchange Rate phải được thống nhất giữa Organization và Parent"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R016 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R016 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R016 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R016 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-04-R016-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-04-R016 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Việc thay đổi Exchange Rate phải được thống nhất giữa Organization và Parent.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-016",
    "previous_temporary_key": "TMP-BRD-WS-04-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Currency Governance",
    "source_context_sha256": "813b59bdc4285ee8bd17cc6d2b347e2cc3c353ffdf6fdfbc8ffcb1e432ab5404",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "b33d57c92832b977cdc06843a214f77bf6391496a2abcfca3140fad225d7ae6d",
    "source_lines": "L471",
    "source_section": "21. Currency Governance"
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
  "stable_id": "BRD-WS-04-R016",
  "title": "Việc thay đổi Exchange Rate phải được thống nhất giữa Organization và Parent",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
