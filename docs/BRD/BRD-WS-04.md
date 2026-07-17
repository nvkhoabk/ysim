---
document_code: "BRD-WS-04"
document_id: "BRD-WS-04"
title: "Product Catalog, Supplier & Product Intelligence"
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

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-04-001 — YSim sử dụng mô hình Four-Level Catalog: - Supplier Catalog - Master Catalog - Sales Catalog - S…

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
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-001",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-04-001",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "1ca51037474e1df7f7b741fdebc6e681b81ecb203ed3f3e8addd9b5e184cdbf4"
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
        "BD-04-001-AC001",
        "BD-04-001-AC005",
        "BD-04-001-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-001-O001",
      "obligation_text": "YSim sử dụng mô hình Four-Level Catalog: Supplier Catalog"
    },
    {
      "acceptance_criterion_references": [
        "BD-04-001-AC002",
        "BD-04-001-AC005",
        "BD-04-001-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-001-O002",
      "obligation_text": "YSim sử dụng mô hình Four-Level Catalog: Master Catalog"
    },
    {
      "acceptance_criterion_references": [
        "BD-04-001-AC003",
        "BD-04-001-AC005",
        "BD-04-001-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-001-O003",
      "obligation_text": "YSim sử dụng mô hình Four-Level Catalog: Sales Catalog"
    },
    {
      "acceptance_criterion_references": [
        "BD-04-001-AC004",
        "BD-04-001-AC005",
        "BD-04-001-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-001-O004",
      "obligation_text": "YSim sử dụng mô hình Four-Level Catalog: Storefront Catalog"
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
    "source_fingerprint": "1ca51037474e1df7f7b741fdebc6e681b81ecb203ed3f3e8addd9b5e184cdbf4",
    "source_lines": "L712-L825",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-04-001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-04-002",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "bbc834d4de1541279f743f7b843886f78ceeeabd28f46bc6c78123444db456cb"
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
        "BD-04-002-AC001",
        "BD-04-002-AC002",
        "BD-04-002-AC003"
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
    "source_fingerprint": "bbc834d4de1541279f743f7b843886f78ceeeabd28f46bc6c78123444db456cb",
    "source_lines": "L827-L902",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-04-002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-04-003",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "99922282fa8cc6f2c3e58e49b1727d2c54ed404f98b10fa4c607caec271123be"
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
        "BD-04-003-AC001",
        "BD-04-003-AC003",
        "BD-04-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-003-O001",
      "obligation_text": "Sales Catalog chỉ tham chiếu Master Product"
    },
    {
      "acceptance_criterion_references": [
        "BD-04-003-AC002",
        "BD-04-003-AC003",
        "BD-04-003-AC004"
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
    "source_fingerprint": "99922282fa8cc6f2c3e58e49b1727d2c54ed404f98b10fa4c607caec271123be",
    "source_lines": "L904-L989",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-04-003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-04-004",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "6503dc51d5a466cb212ae1ec8c096c6351a5a93713b4ee0fe9d0a2d80e746963"
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
        "BD-04-004-AC001",
        "BD-04-004-AC002",
        "BD-04-004-AC003"
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
    "source_fingerprint": "6503dc51d5a466cb212ae1ec8c096c6351a5a93713b4ee0fe9d0a2d80e746963",
    "source_lines": "L991-L1066",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-04-004"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "A named field may still be denied by a stricter applicable policy; unnamed fields remain immutable to Organization"
    ],
    "concrete_bindings": [
      {
        "actual_value": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BD-04-005.OBSERVED.ENUM.VALUE"
            ],
            "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
            "source_type": "SOURCE_LITERAL",
            "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
          },
          "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        },
        "allowed_values": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "SELLING.PRICE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "CURRENCY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "VISIBILITY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "MARKETING.CONTENT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            }
          ],
          "origin": {
            "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
        },
        "field": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
            "source_type": "SOURCE_LITERAL",
            "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
          },
          "identifier": "BD-04-005.FIELD",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "FIELD_ID",
            "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
            "version": "1.0.0"
          },
          "semantic_type": "FIELD_ID"
        }
      },
      {
        "actual_value": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BD-04-005.OBSERVED.ENUM.VALUE"
            ],
            "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
            "source_type": "SOURCE_LITERAL",
            "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
          },
          "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        },
        "allowed_values": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "SELLING.PRICE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "CURRENCY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "VISIBILITY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "MARKETING.CONTENT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            }
          ],
          "origin": {
            "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
        },
        "field": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
            "source_type": "SOURCE_LITERAL",
            "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
          },
          "identifier": "BD-04-005.FIELD",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "FIELD_ID",
            "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
            "version": "1.0.0"
          },
          "semantic_type": "FIELD_ID"
        }
      },
      {
        "actual_value": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BD-04-005.OBSERVED.ENUM.VALUE"
            ],
            "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
            "source_type": "SOURCE_LITERAL",
            "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
          },
          "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        },
        "allowed_values": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "SELLING.PRICE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "CURRENCY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "VISIBILITY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "MARKETING.CONTENT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            }
          ],
          "origin": {
            "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
        },
        "field": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
            "source_type": "SOURCE_LITERAL",
            "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
          },
          "identifier": "BD-04-005.FIELD",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "FIELD_ID",
            "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
            "version": "1.0.0"
          },
          "semantic_type": "FIELD_ID"
        }
      },
      {
        "actual_value": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BD-04-005.OBSERVED.ENUM.VALUE"
            ],
            "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
            "source_type": "SOURCE_LITERAL",
            "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
          },
          "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        },
        "allowed_values": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "SELLING.PRICE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "CURRENCY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "VISIBILITY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "MARKETING.CONTENT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            }
          ],
          "origin": {
            "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
        },
        "field": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
            "source_type": "SOURCE_LITERAL",
            "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
          },
          "identifier": "BD-04-005.FIELD",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "FIELD_ID",
            "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
            "version": "1.0.0"
          },
          "semantic_type": "FIELD_ID"
        }
      },
      {
        "actual_value": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BD-04-005.OBSERVED.ENUM.VALUE"
            ],
            "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
            "source_type": "SOURCE_LITERAL",
            "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
          },
          "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        },
        "allowed_values": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "SELLING.PRICE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "CURRENCY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "VISIBILITY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "MARKETING.CONTENT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            }
          ],
          "origin": {
            "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
        },
        "field": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
            "source_type": "SOURCE_LITERAL",
            "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
          },
          "identifier": "BD-04-005.FIELD",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "FIELD_ID",
            "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
            "version": "1.0.0"
          },
          "semantic_type": "FIELD_ID"
        }
      },
      {
        "actual_value": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BD-04-005.OBSERVED.ENUM.VALUE"
            ],
            "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
            "source_type": "SOURCE_LITERAL",
            "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
          },
          "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        },
        "allowed_values": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "SELLING.PRICE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "CURRENCY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "VISIBILITY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "MARKETING.CONTENT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "SELLING.PRICE",
                  "CURRENCY",
                  "COLLECTION",
                  "VISIBILITY",
                  "MARKETING.CONTENT",
                  "PRODUCT.CODE.PREFIX.POSTFIX"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            }
          ],
          "origin": {
            "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
        },
        "field": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
            "source_type": "SOURCE_LITERAL",
            "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
          },
          "identifier": "BD-04-005.FIELD",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "FIELD_ID",
            "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
            "version": "1.0.0"
          },
          "semantic_type": "FIELD_ID"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BD-04-005",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Any field outside the named set is changed by the Organization"
    ],
    "operator_composition": [
      "ENUM_VALUE_ALLOWED",
      "ENUM_VALUE_ALLOWED",
      "ENUM_VALUE_ALLOWED",
      "ENUM_VALUE_ALLOWED",
      "ENUM_VALUE_ALLOWED",
      "ENUM_VALUE_ALLOWED"
    ],
    "positive_oracle": [
      "Only Selling Price, Currency, Collection, Visibility, Marketing Content and Product Code Prefix or Postfix can be changed"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
      "source_lines": "L552-L562",
      "source_section": "24. Business Decisions (Locked) > BD-04-005"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
          "source_type": "SOURCE_LITERAL",
          "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
        },
        "identifier": "BD-04-005.BD-04-005.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BD-04-005.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-04.md",
          "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
          "source_lines": "L552-L562",
          "source_section": "24. Business Decisions (Locked) > BD-04-005"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BD-04-005.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.ORGANIZATION_ID",
        "FIELD.ACTOR_ID",
        "FIELD.CHANGED_FIELDS",
        "FIELD.ALLOWED_FIELDS",
        "FIELD.PERMISSION_RESULT",
        "FIELD.AUDIT_RECORD"
      ],
      "producer": "BD-04-005.EVIDENCE.PRODUCER",
      "required_collection_origin": "BD-04-005.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.ORGANIZATION_ID",
        "FIELD.ACTOR_ID",
        "FIELD.CHANGED_FIELDS",
        "FIELD.ALLOWED_FIELDS",
        "FIELD.PERMISSION_RESULT",
        "FIELD.AUDIT_RECORD"
      ],
      "required_values_or_hashes": [
        "BD-04-005.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BD-04-005.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BD-04-005.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BD-04-005-O001",
      "BD-04-005-O002",
      "BD-04-005-O003",
      "BD-04-005-O004",
      "BD-04-005-O005",
      "BD-04-005-O006"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED",
          "evaluator_consumed_bindings": [
            "actual_value",
            "allowed_values",
            "field"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "RESOLVE.BD-04-005.BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_value": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.OBSERVED.ENUM.VALUE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "allowed_values": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "SELLING.PRICE",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "CURRENCY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "COLLECTION",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "VISIBILITY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "MARKETING.CONTENT",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "field": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.FIELD",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "FIELD_ID",
                  "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
                  "version": "1.0.0"
                },
                "semantic_type": "FIELD_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BD-04-005.BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "ENUM_VALUE_ALLOWED"
          },
          "obligation_id": "BD-04-005-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O1.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "operator_id": "ENUM_VALUE_ALLOWED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_value": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-04-005.OBSERVED.ENUM.VALUE"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            "allowed_values": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "SELLING.PRICE",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "CURRENCY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "COLLECTION",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "VISIBILITY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "MARKETING.CONTENT",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                }
              ],
              "origin": {
                "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
            },
            "field": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.FIELD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O1.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            }
          }
        },
        {
          "assertion_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED",
          "evaluator_consumed_bindings": [
            "actual_value",
            "allowed_values",
            "field"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "RESOLVE.BD-04-005.BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_value": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.OBSERVED.ENUM.VALUE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "allowed_values": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "SELLING.PRICE",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "CURRENCY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "COLLECTION",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "VISIBILITY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "MARKETING.CONTENT",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "field": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.FIELD",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "FIELD_ID",
                  "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
                  "version": "1.0.0"
                },
                "semantic_type": "FIELD_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BD-04-005.BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "ENUM_VALUE_ALLOWED"
          },
          "obligation_id": "BD-04-005-O002",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O2.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "operator_id": "ENUM_VALUE_ALLOWED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_value": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-04-005.OBSERVED.ENUM.VALUE"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            "allowed_values": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "SELLING.PRICE",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "CURRENCY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "COLLECTION",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "VISIBILITY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "MARKETING.CONTENT",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                }
              ],
              "origin": {
                "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
            },
            "field": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.FIELD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O2.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            }
          }
        },
        {
          "assertion_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED",
          "evaluator_consumed_bindings": [
            "actual_value",
            "allowed_values",
            "field"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "RESOLVE.BD-04-005.BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_value": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.OBSERVED.ENUM.VALUE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "allowed_values": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "SELLING.PRICE",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "CURRENCY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "COLLECTION",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "VISIBILITY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "MARKETING.CONTENT",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "field": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.FIELD",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "FIELD_ID",
                  "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
                  "version": "1.0.0"
                },
                "semantic_type": "FIELD_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BD-04-005.BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "ENUM_VALUE_ALLOWED"
          },
          "obligation_id": "BD-04-005-O003",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O3.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "operator_id": "ENUM_VALUE_ALLOWED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_value": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-04-005.OBSERVED.ENUM.VALUE"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            "allowed_values": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "SELLING.PRICE",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "CURRENCY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "COLLECTION",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "VISIBILITY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "MARKETING.CONTENT",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                }
              ],
              "origin": {
                "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
            },
            "field": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.FIELD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O3.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            }
          }
        },
        {
          "assertion_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED",
          "evaluator_consumed_bindings": [
            "actual_value",
            "allowed_values",
            "field"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "RESOLVE.BD-04-005.BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_value": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.OBSERVED.ENUM.VALUE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "allowed_values": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "SELLING.PRICE",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "CURRENCY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "COLLECTION",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "VISIBILITY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "MARKETING.CONTENT",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "field": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.FIELD",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "FIELD_ID",
                  "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
                  "version": "1.0.0"
                },
                "semantic_type": "FIELD_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BD-04-005.BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "ENUM_VALUE_ALLOWED"
          },
          "obligation_id": "BD-04-005-O004",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O4.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "operator_id": "ENUM_VALUE_ALLOWED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_value": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-04-005.OBSERVED.ENUM.VALUE"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            "allowed_values": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "SELLING.PRICE",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "CURRENCY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "COLLECTION",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "VISIBILITY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "MARKETING.CONTENT",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                }
              ],
              "origin": {
                "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
            },
            "field": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.FIELD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O4.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            }
          }
        },
        {
          "assertion_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED",
          "evaluator_consumed_bindings": [
            "actual_value",
            "allowed_values",
            "field"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "RESOLVE.BD-04-005.BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_value": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.OBSERVED.ENUM.VALUE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "allowed_values": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "SELLING.PRICE",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "CURRENCY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "COLLECTION",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "VISIBILITY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "MARKETING.CONTENT",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "field": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.FIELD",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "FIELD_ID",
                  "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
                  "version": "1.0.0"
                },
                "semantic_type": "FIELD_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BD-04-005.BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "ENUM_VALUE_ALLOWED"
          },
          "obligation_id": "BD-04-005-O005",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O5.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "operator_id": "ENUM_VALUE_ALLOWED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_value": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-04-005.OBSERVED.ENUM.VALUE"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            "allowed_values": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "SELLING.PRICE",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "CURRENCY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "COLLECTION",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "VISIBILITY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "MARKETING.CONTENT",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                }
              ],
              "origin": {
                "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
            },
            "field": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.FIELD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O5.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            }
          }
        },
        {
          "assertion_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED",
          "evaluator_consumed_bindings": [
            "actual_value",
            "allowed_values",
            "field"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "RESOLVE.BD-04-005.BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_value": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.OBSERVED.ENUM.VALUE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "allowed_values": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "SELLING.PRICE",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "CURRENCY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "COLLECTION",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "VISIBILITY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "MARKETING.CONTENT",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  },
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SELLING.PRICE",
                        "CURRENCY",
                        "COLLECTION",
                        "VISIBILITY",
                        "MARKETING.CONTENT",
                        "PRODUCT.CODE.PREFIX.POSTFIX"
                      ],
                      "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                    },
                    "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-04.md",
                      "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                      "source_lines": "L552-L562",
                      "source_section": "24. Business Decisions (Locked) > BD-04-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "field": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.FIELD",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "FIELD_ID",
                  "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
                  "version": "1.0.0"
                },
                "semantic_type": "FIELD_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BD-04-005.BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                },
                "identifier": "BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-04.md",
                  "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                  "source_lines": "L552-L562",
                  "source_section": "24. Business Decisions (Locked) > BD-04-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "ENUM_VALUE_ALLOWED"
          },
          "obligation_id": "BD-04-005-O006",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
              "source_type": "SOURCE_LITERAL",
              "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
            },
            "identifier": "BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-04.md",
              "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
              "source_lines": "L552-L562",
              "source_section": "24. Business Decisions (Locked) > BD-04-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.O6.1.ENUM_VALUE_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "operator_id": "ENUM_VALUE_ALLOWED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_value": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-04-005.OBSERVED.ENUM.VALUE"
                ],
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.OBSERVED.ENUM.VALUE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ACTUAL_VALUE.ORIGIN",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "OBSERVE.BD-04-005.BD-04-005.OBSERVED.ENUM.VALUE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            "allowed_values": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "SELLING.PRICE",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.SELLING.PRICE",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "CURRENCY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.2",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.CURRENCY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "COLLECTION",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.3",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.COLLECTION",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "VISIBILITY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.4",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.VISIBILITY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "MARKETING.CONTENT",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.5",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.MARKETING.CONTENT",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                },
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "SELLING.PRICE",
                      "CURRENCY",
                      "COLLECTION",
                      "VISIBILITY",
                      "MARKETING.CONTENT",
                      "PRODUCT.CODE.PREFIX.POSTFIX"
                    ],
                    "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
                  },
                  "identifier": "PRODUCT.CODE.PREFIX.POSTFIX",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN.MEMBER.6",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-04.md",
                    "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                    "source_lines": "L552-L562",
                    "source_section": "24. Business Decisions (Locked) > BD-04-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_ENUM_VALUE",
                    "resolver_id": "RESOLVE.BD-04-005.PRODUCT.CODE.PREFIX.POSTFIX",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_ENUM_VALUE"
                }
              ],
              "origin": {
                "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.ALLOWED_VALUES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
            },
            "field": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
                "source_type": "SOURCE_LITERAL",
                "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
              },
              "identifier": "BD-04-005.FIELD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-04-005.O6.1.ENUM_VALUE_ALLOWED.FIELD.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-04.md",
                "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
                "source_lines": "L552-L562",
                "source_section": "24. Business Decisions (Locked) > BD-04-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BD-04-005.BD-04-005.FIELD",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            }
          }
        }
      ],
      "boundary_cases": [
        "A named field may still be denied by a stricter applicable policy; unnamed fields remain immutable to Organization"
      ],
      "contract_ast_sha256": "b2b8ad35759a993fe86441d207d9eb353d27e9f5906f0efac35f1f4ffc94af37",
      "contract_id": "P2C.C4.CONTRACT.BD-04-005",
      "criticality": "CRITICAL",
      "disposition": "COMPOUND_AST_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-04.md#24. Business Decisions (Locked) > BD-04-005",
            "source_type": "SOURCE_LITERAL",
            "version": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b"
          },
          "identifier": "BD-04-005.BD-04-005.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-04-005.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-04.md",
            "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
            "source_lines": "L552-L562",
            "source_section": "24. Business Decisions (Locked) > BD-04-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BD-04-005.BD-04-005.BD-04-005.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BD-04-005.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.ORGANIZATION_ID",
          "FIELD.ACTOR_ID",
          "FIELD.CHANGED_FIELDS",
          "FIELD.ALLOWED_FIELDS",
          "FIELD.PERMISSION_RESULT",
          "FIELD.AUDIT_RECORD"
        ],
        "producer": "BD-04-005.EVIDENCE.PRODUCER",
        "required_collection_origin": "BD-04-005.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.ORGANIZATION_ID",
          "FIELD.ACTOR_ID",
          "FIELD.CHANGED_FIELDS",
          "FIELD.ALLOWED_FIELDS",
          "FIELD.PERMISSION_RESULT",
          "FIELD.AUDIT_RECORD"
        ],
        "required_values_or_hashes": [
          "BD-04-005.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BD-04-005.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BD-04-005.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-3AADE6B801CA4FD16989",
        "P2C-C4-FX-1BFF9053A1F02BA897A0",
        "P2C-C4-FX-2DFD204C33D31A4863EE"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Any field outside the named set is changed by the Organization"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-04-005-O001",
          "obligation_text": "Organization chỉ được thay đổi: Selling Price"
        },
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-04-005-O002",
          "obligation_text": "Organization chỉ được thay đổi: Currency"
        },
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-04-005-O003",
          "obligation_text": "Organization chỉ được thay đổi: Collection"
        },
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-04-005-O004",
          "obligation_text": "Organization chỉ được thay đổi: Visibility"
        },
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-04-005-O005",
          "obligation_text": "Organization chỉ được thay đổi: Marketing Content"
        },
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-04-005-O006",
          "obligation_text": "Organization chỉ được thay đổi: Product Code Prefix/Postfix"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BD-04-005.O1.1.ENUM_VALUE_ALLOWED"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-04-005-O001"
        },
        {
          "assertion_ids": [
            "BD-04-005.O2.1.ENUM_VALUE_ALLOWED"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-04-005-O002"
        },
        {
          "assertion_ids": [
            "BD-04-005.O3.1.ENUM_VALUE_ALLOWED"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-04-005-O003"
        },
        {
          "assertion_ids": [
            "BD-04-005.O4.1.ENUM_VALUE_ALLOWED"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-04-005-O004"
        },
        {
          "assertion_ids": [
            "BD-04-005.O5.1.ENUM_VALUE_ALLOWED"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-04-005-O005"
        },
        {
          "assertion_ids": [
            "BD-04-005.O6.1.ENUM_VALUE_ALLOWED"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-04-005-O006"
        }
      ],
      "operator_composition": [
        "ENUM_VALUE_ALLOWED",
        "ENUM_VALUE_ALLOWED",
        "ENUM_VALUE_ALLOWED",
        "ENUM_VALUE_ALLOWED",
        "ENUM_VALUE_ALLOWED",
        "ENUM_VALUE_ALLOWED"
      ],
      "positive_oracles": [
        "Only Selling Price, Currency, Collection, Visibility, Marketing Content and Product Code Prefix or Postfix can be changed"
      ],
      "preconditions": [
        "The actor has catalog-edit permission for the Organization"
      ],
      "prohibitions": [
        "Any field outside the named set is changed by the Organization"
      ],
      "requirement_id": "BD-04-005",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-04.md",
        "source_fingerprint": "eb9138d5d95efdc68909c5ff912c28121c1caaf1cc8b51e5f482d87df77c2f0b",
        "source_lines": "L552-L562",
        "source_section": "24. Business Decisions (Locked) > BD-04-005"
      },
      "source_statement": "Organization chỉ được thay đổi: - Selling Price - Currency - Collection - Visibility - Marketing Content - Product Code Prefix/Postfix",
      "surrounding_source_context": "## BD-04-005\n\nOrganization chỉ được thay đổi:\n\n- Selling Price\n- Currency\n- Collection\n- Visibility\n- Marketing Content\n- Product Code Prefix/Postfix\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BD-04-005",
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
        "BD-04-005-AC001",
        "BD-04-005-AC007",
        "BD-04-005-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-005-O001",
      "obligation_text": "Organization chỉ được thay đổi: Selling Price"
    },
    {
      "acceptance_criterion_references": [
        "BD-04-005-AC002",
        "BD-04-005-AC007",
        "BD-04-005-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-005-O002",
      "obligation_text": "Organization chỉ được thay đổi: Currency"
    },
    {
      "acceptance_criterion_references": [
        "BD-04-005-AC003",
        "BD-04-005-AC007",
        "BD-04-005-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-005-O003",
      "obligation_text": "Organization chỉ được thay đổi: Collection"
    },
    {
      "acceptance_criterion_references": [
        "BD-04-005-AC004",
        "BD-04-005-AC007",
        "BD-04-005-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-005-O004",
      "obligation_text": "Organization chỉ được thay đổi: Visibility"
    },
    {
      "acceptance_criterion_references": [
        "BD-04-005-AC005",
        "BD-04-005-AC007",
        "BD-04-005-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-005-O005",
      "obligation_text": "Organization chỉ được thay đổi: Marketing Content"
    },
    {
      "acceptance_criterion_references": [
        "BD-04-005-AC006",
        "BD-04-005-AC007",
        "BD-04-005-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-005-O006",
      "obligation_text": "Organization chỉ được thay đổi: Product Code Prefix/Postfix"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-04-005 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-04-005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-04-005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-04-005-AC007"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-04-005-AC001",
        "BD-04-005-AC002",
        "BD-04-005-AC003",
        "BD-04-005-AC004",
        "BD-04-005-AC005",
        "BD-04-005-AC006"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-04-005 does not define a recovery obligation."
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
    "source_fingerprint": "2b68384eb42e1a9bb3a44fca9c535553df584ad6c7e506a3f5f7af48a14ff80b",
    "source_lines": "L1068-L9073",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-04-005"
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
      "requirement_id": "BD-04-006",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "99559f70e1d702ef413f4e6a2782ed164d02719c89fff82790e344547a3a4069"
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
        "BD-04-006-AC001",
        "BD-04-006-AC002",
        "BD-04-006-AC003"
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
    "source_fingerprint": "99559f70e1d702ef413f4e6a2782ed164d02719c89fff82790e344547a3a4069",
    "source_lines": "L9075-L9154",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-04-006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BD-04-007",
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
    "source_fingerprint": "4a7346604746c095e46c20a14a3f2039921cff8c1a5634f45b100773ac54d63f",
    "source_lines": "L9156-L9228",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-04-007"
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
      "requirement_id": "BD-04-008",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "e96c1df7c35275f311725bf4f0b245d3613267a07578fb004488ac927db99cb9"
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
        "BD-04-008-AC001",
        "BD-04-008-AC003",
        "BD-04-008-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-008-O001",
      "obligation_text": "Supplier Attribute Mapping phải hỗ trợ cấu hình"
    },
    {
      "acceptance_criterion_references": [
        "BD-04-008-AC002",
        "BD-04-008-AC003",
        "BD-04-008-AC004"
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
    "source_fingerprint": "e96c1df7c35275f311725bf4f0b245d3613267a07578fb004488ac927db99cb9",
    "source_lines": "L9230-L9319",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-04-008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-04-009",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "1be06bde4b159681baddcc0eb62fa995713146ea5449296b517c22a7952996ae"
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
        "BD-04-009-AC001",
        "BD-04-009-AC003",
        "BD-04-009-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-009-O001",
      "obligation_text": "Catalog Publish sử dụng Workflow"
    },
    {
      "acceptance_criterion_references": [
        "BD-04-009-AC002",
        "BD-04-009-AC003",
        "BD-04-009-AC004"
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
    "source_fingerprint": "1be06bde4b159681baddcc0eb62fa995713146ea5449296b517c22a7952996ae",
    "source_lines": "L9321-L9406",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-04-009"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-04-010",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "1c1a00e484fccf9e2a4c195708bb45d4a80f22898347353137e502d5ff1b29d4"
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
        "BD-04-010-AC001",
        "BD-04-010-AC002",
        "BD-04-010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-04-010-O001",
      "obligation_text": "Currency là một phần của Commercial Agreement giữa Organization và Parent"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-04-010 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-04-010 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-04-010 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-04-010-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-04-010-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-04-010 does not define a recovery obligation."
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
    "source_fingerprint": "1c1a00e484fccf9e2a4c195708bb45d4a80f22898347353137e502d5ff1b29d4",
    "source_lines": "L9408-L9516",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-04-010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-04-011",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "27fb26bfa0c40126ef4188a8469f334425c70ba71fcad2cb5931e83ff944953f"
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
        "BD-04-011-AC001",
        "BD-04-011-AC002",
        "BD-04-011-AC003"
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
    "source_fingerprint": "27fb26bfa0c40126ef4188a8469f334425c70ba71fcad2cb5931e83ff944953f",
    "source_lines": "L9518-L9593",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-04-011"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-04-R001",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "d8d7e85239280a630ed727ecb05c7fef2b537a7773e0327806cf9488759289cd"
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
        "BRD-WS-04-R001-AC001",
        "BRD-WS-04-R001-AC002",
        "BRD-WS-04-R001-AC003"
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
    "source_lines": "L9595-L9670",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-04-R002",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "39190b821e393a5c136483d87a4b55b15c2ccaaa5f78cf51672e54a0936f58ab"
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
        "BRD-WS-04-R002-AC001",
        "BRD-WS-04-R002-AC002",
        "BRD-WS-04-R002-AC003"
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
    "source_lines": "L9672-L9747",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-04-R003",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "f12d928fe850ddc8154049f0ae64db29c15b01f768f866cd9696a02e92dbf735"
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
        "BRD-WS-04-R003-AC001",
        "BRD-WS-04-R003-AC002",
        "BRD-WS-04-R003-AC003"
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
    "source_fingerprint": "f12d928fe850ddc8154049f0ae64db29c15b01f768f866cd9696a02e92dbf735",
    "source_lines": "L9749-L9824",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-04-R004",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "df3a83bb89510ac8fee953f1d7546d11d86c756713d7a9235fdf6a49bb817fe8"
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
        "BRD-WS-04-R004-AC001",
        "BRD-WS-04-R004-AC002",
        "BRD-WS-04-R004-AC003"
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
    "source_fingerprint": "df3a83bb89510ac8fee953f1d7546d11d86c756713d7a9235fdf6a49bb817fe8",
    "source_lines": "L9826-L9901",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-04-R005",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "373af057b744c73463148c052842b6c5a7214295ab6195235537c28402845fe3"
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
        "BRD-WS-04-R005-AC001",
        "BRD-WS-04-R005-AC002",
        "BRD-WS-04-R005-AC003"
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
    "source_fingerprint": "373af057b744c73463148c052842b6c5a7214295ab6195235537c28402845fe3",
    "source_lines": "L9903-L9978",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-04-R006",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "9f460dc0bcbc013734dd3d001ba368912f80394f670043840f360b19dc3e66bb"
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
        "BRD-WS-04-R006-AC001",
        "BRD-WS-04-R006-AC002",
        "BRD-WS-04-R006-AC003"
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
    "source_fingerprint": "9f460dc0bcbc013734dd3d001ba368912f80394f670043840f360b19dc3e66bb",
    "source_lines": "L9980-L10055",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-04-R007",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "0385ac4ab0a3867becfbe53e227a7e8994dbd7ed6c297d4601072f22fc2b1336"
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
        "BRD-WS-04-R007-AC001",
        "BRD-WS-04-R007-AC002",
        "BRD-WS-04-R007-AC003"
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
    "source_fingerprint": "0385ac4ab0a3867becfbe53e227a7e8994dbd7ed6c297d4601072f22fc2b1336",
    "source_lines": "L10057-L10132",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-04-R008",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "a26c7b68c66e64f89284f7630375e55f34079dbbf964986d2de2edd67d39cccc"
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
        "BRD-WS-04-R008-AC001",
        "BRD-WS-04-R008-AC002",
        "BRD-WS-04-R008-AC003"
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
    "source_fingerprint": "a26c7b68c66e64f89284f7630375e55f34079dbbf964986d2de2edd67d39cccc",
    "source_lines": "L10134-L10209",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-04-R009",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "2a047573a2af85d14843a52261cba5f8a18984208b73bb0d9b977431d4523f9e"
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
        "BRD-WS-04-R009-AC001",
        "BRD-WS-04-R009-AC002",
        "BRD-WS-04-R009-AC003"
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
    "source_lines": "L10211-L10286",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R009"
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
      "requirement_id": "BRD-WS-04-R010",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "e2c8b4e01d1c787f40cadd569f0ade53823324592972668b8a93050c2037af8c"
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
        "BRD-WS-04-R010-AC001",
        "BRD-WS-04-R010-AC002",
        "BRD-WS-04-R010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R010-O001",
      "obligation_text": "UUID mới là Identity duy nhất"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-04-R010-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-04-R010 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-04-R010 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-04-R010-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-04-R010-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-04-R010 does not define a recovery obligation."
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
    "source_lines": "L10288-L10402",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-008",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-04-R011",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "6bb54d0a12e1641c981d8a0c8e6b57e2d2ce0b1d0557481228ef9aaa7b3b9fb6"
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
        "BRD-WS-04-R011-AC001",
        "BRD-WS-04-R011-AC002",
        "BRD-WS-04-R011-AC003"
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
    "source_lines": "L10404-L10483",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R011"
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
### BRD-WS-04-R012 — Reason Required chỉ là bước ví dụ trong Catalog Governance và không phải yêu cầu atomic độc lập

```json
{
  "acceptance_contract": null,
  "acceptance_mechanism": null,
  "acceptance_rationale": "The extracted text is an example or explanatory statement, not a standalone requirement.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "STRUCTURAL_RECORD",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reason Required chỉ là bước ví dụ trong Catalog Governance và không phải yêu cầu atomic độc lập.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-04.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "17. Catalog Governance"
    },
    "deterministic_transformation": "EXPAND_RANGE_AND_RETIRE_EXAMPLE_EXTRACTION",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-04-012",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-04-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Catalog Governance",
    "source_context_sha256": "5287113b99d41e48aba0d41c3f941a52825e698b73d52e3968e7fe81040b40fe",
    "source_document": "docs/BRD/BRD-WS-04.md",
    "source_fingerprint": "a080f3cd971ac15a06c1b347e4e9ff18e489123ca0b0c74857c3e989d352f961",
    "source_fingerprint_before_c3": "1ad7dbe6622c151dd37051417ce4fbe800e64b01e46060c31fc80a64dbf6d7ac",
    "source_lines": "L10485-L10553",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-04.md",
      "lines": "L370",
      "section": "17. Catalog Governance"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R012"
  },
  "record_kind": "RETIRED_RECORD",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "retirement_reason": "EXPAND_RANGE_AND_RETIRE_EXAMPLE_EXTRACTION",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-04-R012",
  "title": "Reason Required chỉ là bước ví dụ trong Catalog Governance và không phải yêu cầu atomic độc lập",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-04-R013 — Các chức năng AI sẽ triển khai ở phiên bản sau

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-04-R013",
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
    "source_lines": "L10555-L10613",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R013"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-04-R014",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "a86254033bd80e5cec398da0e538b646685b87d1ed5808fec023dbd31f9ba989"
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
        "BRD-WS-04-R014-AC001",
        "BRD-WS-04-R014-AC002",
        "BRD-WS-04-R014-AC003"
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
    "source_lines": "L10615-L10690",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R014"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "SD-03"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-04-R015",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "8283a6799953a079b2cc0e454b9e40ad6c009841073997a546314d14ee10da5f"
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
        "BRD-WS-04-R015-AC001",
        "BRD-WS-04-R015-AC002",
        "BRD-WS-04-R015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R015-O001",
      "obligation_text": "Organization chỉ được sử dụng Currency đã được Parent Organization phê duyệt"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-04-R015 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-04-R015 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-04-R015 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-04-R015-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-04-R015-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-04-R015 does not define a recovery obligation."
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
    "source_lines": "L10692-L10806",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R015"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-04-R016",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "source_fingerprint": "b33d57c92832b977cdc06843a214f77bf6391496a2abcfca3140fad225d7ae6d"
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
        "BRD-WS-04-R016-AC001",
        "BRD-WS-04-R016-AC002",
        "BRD-WS-04-R016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-04-R016-O001",
      "obligation_text": "Việc thay đổi Exchange Rate phải được thống nhất giữa Organization và Parent"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-04-R016 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-04-R016 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-04-R016 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-04-R016-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-04-R016-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-04-R016 does not define a recovery obligation."
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
    "source_lines": "L10808-L10916",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-04-R016"
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
