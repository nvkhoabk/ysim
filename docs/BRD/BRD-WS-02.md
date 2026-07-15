---
document_code: "BRD-WS-02"
title: "Business Model & Revenue Architecture"
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

# BRD Workshop 02

# Business Model & Revenue Architecture

---

# 1. Workshop Objective

Workshop này xác định mô hình kinh doanh của YSim, cách hình thành sản phẩm, chuỗi cung ứng eSIM, mô hình doanh thu và các Business Entity cốt lõi của hệ thống.

Workshop này là nền tảng cho:

- Product Domain
- Supplier Domain
- Procurement Domain
- Inventory Domain
- Allocation Engine
- Fulfillment Engine
- Pricing Engine
- Settlement Engine

---

# 2. Business Vision

YSim không bán dịch vụ viễn thông.

YSim là nền tảng thương mại chuyên phân phối eSIM.

Giá trị mà khách hàng cuối nhận được là:

- QR Code
- Activation Code
- eSIM Profile

Sau khi eSIM được kích hoạt, toàn bộ quá trình quản lý thuê bao và gói cước sẽ do hệ thống của Mobile Network Operator (MNO) hoặc Mobile Virtual Network Operator (MVNO) thực hiện.

Trong phạm vi phiên bản 2.0, YSim không quản lý:

- Charging
- Data Usage
- OCS
- PCRF
- HSS
- Chính sách sử dụng dữ liệu

Các chức năng như:

- Top-up
- Data Add-on
- Emergency Suspension
- Renewal

được xem là ngoài phạm vi của phiên bản 2.0.

---

# 3. Business Entity Hierarchy

Business Entity trung tâm của toàn bộ hệ thống là **Product**.

Mọi Business Domain đều xoay quanh Product.

```text
Supplier
    │
    ▼
Supplier Product
    │
    ▼
Product Mapping
    │
    ▼
YSim Product
    │
    ▼
Product Item
    │
    ▼
Inventory
    │
    ▼
Allocation
    │
    ▼
Order
    │
    ▼
Fulfillment
```

---

# 4. Product Strategy

YSim Product là **Commercial Product** do YSim định nghĩa và quản lý.

Supplier Product là **Raw Product** do Supplier cung cấp.

Một YSim Product có thể được xây dựng từ một hoặc nhiều Supplier Product.

Người dùng cuối chỉ nhìn thấy YSim Product.

Supplier Product không hiển thị trực tiếp trên các kênh bán hàng.

---

# 5. Supplier Product

Supplier Product phản ánh đúng sản phẩm mà Supplier đang cung cấp.

Ví dụ:

- Supplier A: ASEAN-5GB
- Supplier B: Thailand-5GB

Các Supplier có thể sử dụng các quy tắc đặt tên, thông số kỹ thuật và chính sách giá khác nhau.

YSim chịu trách nhiệm chuẩn hóa các sản phẩm này thành Product Catalog thống nhất.

---

# 6. Product Mapping

Product Mapping là một Business Capability độc lập.

## Một Supplier Product tạo thành nhiều YSim Product

Ví dụ:

```text
Supplier Product

ASEAN-5GB

        │
        ├────────► Thailand 5GB
        │
        ├────────► Malaysia 5GB
        │
        └────────► ASEAN 5GB
```

## Nhiều Supplier Product cùng phục vụ một YSim Product

```text
Supplier A Thailand 5GB
                │
                ├────────► Thailand 5GB
                │
Supplier B Thailand 5GB
```

Allocation Engine sẽ lựa chọn Supplier phù hợp tại thời điểm Fulfillment.

---

# 7. Product Specification

Mỗi YSim Product phải có Product Specification chuẩn.

Ví dụ:

- Coverage
- Country
- Region
- Data Type
- Total Data
- Daily Data
- Validity
- Network
- Speed
- Hotspot
- Recharge
- Auto Renewal
- Activation Policy

YSim Product không nhất thiết phản ánh nguyên văn tên sản phẩm của Supplier.

Tuy nhiên Product Specification phải phản ánh đúng khả năng sử dụng thực tế của eSIM.

Ví dụ:

- Thailand 5GB
- Thailand 5GB/day

là hai sản phẩm hoàn toàn khác nhau.

---

# 8. Product Lifecycle

```text
Draft
    │
    ▼
Review
    │
    ▼
Active
    │
    ▼
Warning
    │
    ▼
Out of Stock
    │
    ▼
Archived
```

Trạng thái Warning được sinh khi:

- Supplier thay đổi giá
- Supplier thay đổi package
- Supplier thay đổi chính sách
- Supplier ngừng cung cấp

Operator sẽ đánh giá và quyết định việc Publish Product.

---

# 9. Product Intelligence

Product Intelligence là Business Capability mới của YSim v2.0.

Bao gồm:

- Supplier Catalog Synchronization
- Product Comparison
- Price Change Detection
- Availability Detection
- Package Change Detection
- Product Mapping Suggestion
- Missing Mapping Detection
- Operator Review
- Publish

Trong các phiên bản tiếp theo, hệ thống có thể sử dụng AI để gợi ý Product Mapping.

---

# 10. Allocation Engine

Allocation Engine chỉ chịu trách nhiệm lựa chọn nguồn cung phù hợp.

Allocation Engine không quản lý Product.

Allocation Engine không quản lý Catalog.

Các tiêu chí lựa chọn bao gồm:

- Giá đầu vào
- Availability
- SLA
- API Health
- Contract Policy
- Credit Limit
- Priority

---

# 11. Inventory Strategy

Inventory được định nghĩa là **Digital Asset Inventory**.

Inventory không chỉ là kho vật lý.

Inventory quản lý:

- Product Item
- QR Code
- ICCID
- Activation Code
- Supplier Reference
- Purchase Cost
- Current Owner
- Inventory Status
- Lifecycle

Inventory luôn tồn tại.

Ngay cả khi Product Item được mua tức thời từ Supplier để phục vụ một đơn hàng cụ thể.

Inventory là cơ sở cho:

- Accounting
- Audit
- Traceability
- Customer Support
- Refund
- Return
- Revoke

---

# 12. Product Item

Product Item là một **Digital Asset**.

Một Product bao gồm nhiều Product Item.

Mỗi Product Item bao gồm:

- QR Code
- ICCID
- Activation Code
- Supplier
- Purchase Order
- Inventory Record
- Current Owner
- Purchase Cost
- Lifecycle

Product Item là đơn vị nhỏ nhất được cấp phát cho khách hàng.

---

# 13. Procurement

Procurement là Business Domain độc lập.

Procurement chịu trách nhiệm:

- Purchase Order
- Supplier Purchase
- Goods Receiving
- Inventory Receiving
- Cost Recording
- Supplier Settlement

Procurement hỗ trợ:

- Nhập kho trước
- Mua tức thời theo Order

Dù theo hình thức nào, mọi Product Item đều phải được ghi nhận vào Inventory.

---

# 14. Inventory Lifecycle

```text
Created
    │
    ▼
Purchased
    │
    ▼
Received
    │
    ▼
Available
    │
    ▼
Reserved
    │
    ▼
Allocated
    │
    ▼
Delivered
    │
    ▼
Activated
    │
    ▼
Consumed
    │
    ▼
Expired
    │
    ▼
Revoked
    │
    ▼
Refunded
```

Lifecycle này phục vụ:

- Accounting
- Audit
- Customer Support
- Refund
- Return
- Revoke

---

# 15. Revenue Model

Nguồn doanh thu chính của YSim:

- Wholesale Margin
- Markup
- Commission
- Promotion Funding

YSim quản lý:

- Product
- Suggested Retail Price
- Discount Policy

Partner được quyền:

- Tự định giá bán
- Xây dựng bảng giá riêng
- Quản lý đại lý
- Thiết lập Commission
- Thiết lập Campaign

---

# 16. Settlement Model

Hệ thống hỗ trợ:

- Wallet / Deposit
- Payment Gateway
- Pay-per-order
- Postpaid Settlement

Toàn bộ Settlement phải sử dụng **Snapshot Pricing**.

Mọi nghiệp vụ tài chính đều được tính theo giá và chính sách tại thời điểm giao dịch.

Không sử dụng Current Price.

---

# 17. Business Decisions (Locked)

## BD-02-001

**Decision**

Business Entity trung tâm của YSim là Product.

**Rationale**

Product là đối tượng được khách hàng lựa chọn, là nền tảng của Catalog, Pricing, Allocation, Inventory, Fulfillment và Reporting.

---

## BD-02-002

**Decision**

Supplier Product và YSim Product là hai Business Object khác nhau.

**Rationale**

Supplier Product phản ánh sản phẩm gốc của nhà cung cấp.

YSim Product là sản phẩm thương mại hóa do YSim xây dựng.

---

## BD-02-003

**Decision**

Allocation Engine chỉ lựa chọn Fulfillment Source.

Không quản lý Product Catalog.

**Rationale**

Tách biệt trách nhiệm giữa Catalog Management và Fulfillment giúp hệ thống mở rộng dễ dàng.

---

## BD-02-004

**Decision**

Inventory được định nghĩa là Digital Asset Inventory.

Không chỉ là Warehouse.

**Rationale**

Mọi Product Item đều là tài sản số có giá trị kinh tế và cần được quản lý trong suốt vòng đời.

---

## BD-02-005

**Decision**

Mọi Product Item đều phải có Inventory Record.

Kể cả mua tức thời.

**Rationale**

Đảm bảo Accounting, Audit, Traceability, Refund và Customer Support.

---

## BD-02-006

**Decision**

Product Intelligence là Business Capability bắt buộc.

**Rationale**

Giúp đồng bộ Catalog, phát hiện thay đổi từ Supplier và hỗ trợ vận hành Product hiệu quả.

---

## BD-02-007

**Decision**

Snapshot Pricing là nguyên tắc bắt buộc.

**Rationale**

Mọi Settlement và nghiệp vụ tài chính phải sử dụng giá tại thời điểm phát sinh giao dịch.

---

# 18. Business Object Model

```text
                        Supplier
                            │
                            ▼
                    Supplier Product
                            │
                    Catalog Synchronization
                            │
                            ▼
                  Product Intelligence
                            │
                    Product Mapping Engine
                            │
                            ▼
                       YSim Product
                            │
                  Product Specification
                            │
                            ▼
                       Product Item
                            │
                            ▼
                        Procurement
                            │
                    Purchase / Receive
                            │
                            ▼
                 Digital Asset Inventory
                            │
                            ▼
                    Allocation Engine
                            │
                            ▼
                           Order
                            │
                            ▼
                       Fulfillment
                            │
                            ▼
                         Customer
```

---

# 19. Traceability

Workshop 02 được xây dựng dựa trên:

- BRD Workshop 01 – Product Vision & Strategy
- Các bài học triển khai từ YSim v1.0
- Mô hình White-label Commerce Platform
- Mô hình Multi-supplier Fulfillment
- Thực tiễn triển khai MVP

---

# 20. Workshop Status

**Status:** FROZEN

Workshop này là nền tảng cho:

- Product Domain
- Supplier Domain
- Procurement Domain
- Inventory Domain
- Allocation Engine
- Fulfillment Engine
- Pricing Engine
- Settlement Engine

---

# 21. Next Workshop

**BRD-WS-03 – Customer, Partner & Organization Model**

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-02-001 — **Decision** Business Entity trung tâm của YSim là Product. **Rationale** Product là đối tượng đ…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-02-001-AC001",
      "given": "the applicable business context, actor, and input for **Decision** Business Entity trung tâm của YSim là Product. **Rationale** Product là đối tượng đ…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-02-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-02-001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by **Decision** Business Entity trung tâm của YSim là Product. **Rationale** Product là đối tượng đ…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-02-001-O001"
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
        "BD-02-001-AC001",
        "BD-02-001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-001-O001",
      "obligation_text": "**Decision** Business Entity trung tâm của YSim là Product. **Rationale** Product là đối tượng được khách hàng lựa chọn, là nền tảng của Catalog, Pricing, Allocation, Inventory, Fulfillment và Reporting"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-02-001 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-02-001 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-02-001 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-02-001 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-02-001-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-02-001 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "**Decision** Business Entity trung tâm của YSim là Product. **Rationale** Product là đối tượng được khách hàng lựa chọn, là nền tảng của Catalog, Pricing, Allocation, Inventory, Fulfillment và Reporting.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007",
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-02-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-02-001",
    "source_context_sha256": "d306690cb04d415d1e2342b0f9d1a8204753ce8a48dd776d59a17534c95fe200",
    "source_document": "docs/BRD/BRD-WS-02.md",
    "source_fingerprint": "8a6d427075df0239b590948b82eecad9f7139d08efce5aeb4996fb4ee5787141",
    "source_lines": "L448-L457",
    "source_section": "17. Business Decisions (Locked) > BD-02-001"
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
  "stable_id": "BD-02-001",
  "title": "**Decision** Business Entity trung tâm của YSim là Product. **Rationale** Product là đối tượng đ…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-02-002 — **Decision** Supplier Product và YSim Product là hai Business Object khác nhau. **Rationale** Su…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-02-002-AC001",
      "given": "a candidate **Decision** Supplier Product và YSim Product là hai Business Object khác nhau. **Rationale** Su… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-02-002-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-02-002-AC002",
      "given": "a candidate **Decision** Supplier Product và YSim Product là hai Business Object khác nhau. **Rationale** Su… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-02-002-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-02-002-AC003",
      "given": "a **Decision** Supplier Product và YSim Product là hai Business Object khác nhau. **Rationale** Su… candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-02-002-O001",
        "BD-02-002-O002"
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
        "BD-02-002-AC001",
        "BD-02-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-002-O001",
      "obligation_text": "**Decision** Supplier Product và YSim Product là hai Business Object khác nhau. **Rationale** Supplier Product phản ánh sản phẩm gốc của nhà cung cấp"
    },
    {
      "acceptance_criterion_references": [
        "BD-02-002-AC002",
        "BD-02-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-002-O002",
      "obligation_text": "YSim Product là sản phẩm thương mại hóa do YSim xây dựng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "**Decision** Supplier Product và YSim Product là hai Business Object khác nhau. **Rationale** Supplier Product phản ánh sản phẩm gốc của nhà cung cấp. YSim Product là sản phẩm thương mại hóa do YSim xây dựng.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-02-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-02-001",
    "source_context_sha256": "d306690cb04d415d1e2342b0f9d1a8204753ce8a48dd776d59a17534c95fe200",
    "source_document": "docs/BRD/BRD-WS-02.md",
    "source_fingerprint": "a6fd6ad5d5f53ab525063619b287517866584c44c8deb76c7a821c70fbe1c0f3",
    "source_lines": "L460-L471",
    "source_section": "17. Business Decisions (Locked) > BD-02-002"
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
  "stable_id": "BD-02-002",
  "title": "**Decision** Supplier Product và YSim Product là hai Business Object khác nhau. **Rationale** Su…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-02-003 — **Decision** Allocation Engine chỉ lựa chọn Fulfillment Source. Không quản lý Product Catalog. *…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-02-003-AC001",
      "given": "the applicable business context, actor, and input for **Decision** Allocation Engine chỉ lựa chọn Fulfillment Source. Không quản lý Product Catalog. *…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-02-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-02-003-AC002",
      "given": "the applicable business context, actor, and input for **Decision** Allocation Engine chỉ lựa chọn Fulfillment Source. Không quản lý Product Catalog. *…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "BD-02-003-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-02-003-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by **Decision** Allocation Engine chỉ lựa chọn Fulfillment Source. Không quản lý Product Catalog. *…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-02-003-O001",
        "BD-02-003-O002"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-02-003-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by **Decision** Allocation Engine chỉ lựa chọn Fulfillment Source. Không quản lý Product Catalog. *…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-02-003-O001",
        "BD-02-003-O002"
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
        "BD-02-003-AC001",
        "BD-02-003-AC003",
        "BD-02-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-003-O001",
      "obligation_text": "**Decision** Allocation Engine chỉ lựa chọn Fulfillment Source"
    },
    {
      "acceptance_criterion_references": [
        "BD-02-003-AC002",
        "BD-02-003-AC003",
        "BD-02-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-003-O002",
      "obligation_text": "Không quản lý Product Catalog. **Rationale** Tách biệt trách nhiệm giữa Catalog Management và Fulfillment giúp hệ thống mở rộng dễ dàng"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-02-003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-02-003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-02-003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-02-003-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-02-003-AC001",
        "BD-02-003-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-02-003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "**Decision** Allocation Engine chỉ lựa chọn Fulfillment Source. Không quản lý Product Catalog. **Rationale** Tách biệt trách nhiệm giữa Catalog Management và Fulfillment giúp hệ thống mở rộng dễ dàng.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-02-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-02-001",
    "source_context_sha256": "d306690cb04d415d1e2342b0f9d1a8204753ce8a48dd776d59a17534c95fe200",
    "source_document": "docs/BRD/BRD-WS-02.md",
    "source_fingerprint": "e62f2d47d04787914c58164c93654e3087e18053f12f5e1c4c8a103987947037",
    "source_lines": "L474-L485",
    "source_section": "17. Business Decisions (Locked) > BD-02-003"
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
  "stable_id": "BD-02-003",
  "title": "**Decision** Allocation Engine chỉ lựa chọn Fulfillment Source. Không quản lý Product Catalog. *…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-02-004 — **Decision** Inventory được định nghĩa là Digital Asset Inventory. Không chỉ là Warehouse. **Rat…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-02-004-AC001",
      "given": "the applicable business context, actor, and input for **Decision** Inventory được định nghĩa là Digital Asset Inventory. Không chỉ là Warehouse. **Rat…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-02-004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-02-004-AC002",
      "given": "the applicable business context, actor, and input for **Decision** Inventory được định nghĩa là Digital Asset Inventory. Không chỉ là Warehouse. **Rat…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-02-004-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-02-004-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by **Decision** Inventory được định nghĩa là Digital Asset Inventory. Không chỉ là Warehouse. **Rat…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-02-004-O001",
        "BD-02-004-O002"
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
        "BD-02-004-AC001",
        "BD-02-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-004-O001",
      "obligation_text": "**Decision** Inventory được định nghĩa là Digital Asset Inventory"
    },
    {
      "acceptance_criterion_references": [
        "BD-02-004-AC002",
        "BD-02-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-004-O002",
      "obligation_text": "Không chỉ là Warehouse. **Rationale** Mọi Product Item đều là tài sản số có giá trị kinh tế và cần được quản lý trong suốt vòng đời"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "**Decision** Inventory được định nghĩa là Digital Asset Inventory. Không chỉ là Warehouse. **Rationale** Mọi Product Item đều là tài sản số có giá trị kinh tế và cần được quản lý trong suốt vòng đời.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-02-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-02-001",
    "source_context_sha256": "d306690cb04d415d1e2342b0f9d1a8204753ce8a48dd776d59a17534c95fe200",
    "source_document": "docs/BRD/BRD-WS-02.md",
    "source_fingerprint": "8288e8bc0e8fccb7afcd3e76f9e48282b000d72057179f725b7e7a2390a6d0c6",
    "source_lines": "L488-L499",
    "source_section": "17. Business Decisions (Locked) > BD-02-004"
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
  "stable_id": "BD-02-004",
  "title": "**Decision** Inventory được định nghĩa là Digital Asset Inventory. Không chỉ là Warehouse. **Rat…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-02-005 — **Decision** Mọi Product Item đều phải có Inventory Record. Kể cả mua tức thời. **Rationale** Đả…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-02-005-AC001",
      "given": "an operational task within the scope of **Decision** Mọi Product Item đều phải có Inventory Record. Kể cả mua tức thời. **Rationale** Đả…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-02-005-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-02-005-AC002",
      "given": "an operational task within the scope of **Decision** Mọi Product Item đều phải có Inventory Record. Kể cả mua tức thời. **Rationale** Đả…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-02-005-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-02-005-AC003",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for **Decision** Mọi Product Item đều phải có Inventory Record. Kể cả mua tức thời. **Rationale** Đả…",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-02-005-O001",
        "BD-02-005-O002"
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
        "BD-02-005-AC001",
        "BD-02-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-005-O001",
      "obligation_text": "**Decision** Mọi Product Item đều phải có Inventory Record"
    },
    {
      "acceptance_criterion_references": [
        "BD-02-005-AC002",
        "BD-02-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-005-O002",
      "obligation_text": "Kể cả mua tức thời. **Rationale** Đảm bảo Accounting, Audit, Traceability, Refund và Customer Support"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-02-005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-02-005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-02-005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-02-005 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-02-005-AC001",
        "BD-02-005-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-02-005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "**Decision** Mọi Product Item đều phải có Inventory Record. Kể cả mua tức thời. **Rationale** Đảm bảo Accounting, Audit, Traceability, Refund và Customer Support.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-02-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-02-001",
    "source_context_sha256": "d306690cb04d415d1e2342b0f9d1a8204753ce8a48dd776d59a17534c95fe200",
    "source_document": "docs/BRD/BRD-WS-02.md",
    "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
    "source_lines": "L502-L513",
    "source_section": "17. Business Decisions (Locked) > BD-02-005"
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
  "stable_id": "BD-02-005",
  "title": "**Decision** Mọi Product Item đều phải có Inventory Record. Kể cả mua tức thời. **Rationale** Đả…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-02-006 — **Decision** Product Intelligence là Business Capability bắt buộc. **Rationale** Giúp đồng bộ Ca…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-02-006-AC001",
      "given": "the applicable business context, actor, and input for **Decision** Product Intelligence là Business Capability bắt buộc. **Rationale** Giúp đồng bộ Ca…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-02-006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-02-006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by **Decision** Product Intelligence là Business Capability bắt buộc. **Rationale** Giúp đồng bộ Ca…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-02-006-O001"
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
        "BD-02-006-AC001",
        "BD-02-006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-006-O001",
      "obligation_text": "**Decision** Product Intelligence là Business Capability bắt buộc. **Rationale** Giúp đồng bộ Catalog, phát hiện thay đổi từ Supplier và hỗ trợ vận hành Product hiệu quả"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "**Decision** Product Intelligence là Business Capability bắt buộc. **Rationale** Giúp đồng bộ Catalog, phát hiện thay đổi từ Supplier và hỗ trợ vận hành Product hiệu quả.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-02-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-02-001",
    "source_context_sha256": "d306690cb04d415d1e2342b0f9d1a8204753ce8a48dd776d59a17534c95fe200",
    "source_document": "docs/BRD/BRD-WS-02.md",
    "source_fingerprint": "62671d6e8bf656c834e5ec8ae9a167d32afe56062d3cd5a5039d6d1b54674afe",
    "source_lines": "L516-L525",
    "source_section": "17. Business Decisions (Locked) > BD-02-006"
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
  "stable_id": "BD-02-006",
  "title": "**Decision** Product Intelligence là Business Capability bắt buộc. **Rationale** Giúp đồng bộ Ca…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-02-007 — **Decision** Snapshot Pricing là nguyên tắc bắt buộc. **Rationale** Mọi Settlement và nghiệp vụ …

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-02-007-AC001",
      "given": "a candidate **Decision** Snapshot Pricing là nguyên tắc bắt buộc. **Rationale** Mọi Settlement và nghiệp vụ … record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-02-007-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-02-007-AC002",
      "given": "a **Decision** Snapshot Pricing là nguyên tắc bắt buộc. **Rationale** Mọi Settlement và nghiệp vụ … candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-02-007-O001"
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
        "BD-02-007-AC001",
        "BD-02-007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-007-O001",
      "obligation_text": "**Decision** Snapshot Pricing là nguyên tắc bắt buộc. **Rationale** Mọi Settlement và nghiệp vụ tài chính phải sử dụng giá tại thời điểm phát sinh giao dịch"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-02-007 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-02-007 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-02-007 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-02-007 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-02-007-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-02-007 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "**Decision** Snapshot Pricing là nguyên tắc bắt buộc. **Rationale** Mọi Settlement và nghiệp vụ tài chính phải sử dụng giá tại thời điểm phát sinh giao dịch.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-02-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-02-001",
    "source_context_sha256": "d306690cb04d415d1e2342b0f9d1a8204753ce8a48dd776d59a17534c95fe200",
    "source_document": "docs/BRD/BRD-WS-02.md",
    "source_fingerprint": "7af8eb671480487ce7ad8a69570cd059eeaf894f8c9bfa0f618bd52314efdfc0",
    "source_lines": "L528-L537",
    "source_section": "17. Business Decisions (Locked) > BD-02-007"
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
  "stable_id": "BD-02-007",
  "title": "**Decision** Snapshot Pricing là nguyên tắc bắt buộc. **Rationale** Mọi Settlement và nghiệp vụ …",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-02-R002 — Mỗi YSim Product phải có Product Specification chuẩn

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-02-R002-AC001",
      "given": "the applicable business context, actor, and input for Mỗi YSim Product phải có Product Specification chuẩn",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-02-R002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-02-R002-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Mỗi YSim Product phải có Product Specification chuẩn",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-02-R002-O001"
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
        "BRD-WS-02-R002-AC001",
        "BRD-WS-02-R002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-02-R002-O001",
      "obligation_text": "Mỗi YSim Product phải có Product Specification chuẩn"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi YSim Product phải có Product Specification chuẩn.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-02-002",
    "previous_temporary_key": "TMP-BRD-WS-02-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Product Specification",
    "source_context_sha256": "d7612da5223a59b34cf5f31ed5d0f6b24a088ad9cad981382b42647856dc2e29",
    "source_document": "docs/BRD/BRD-WS-02.md",
    "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
    "source_lines": "L173",
    "source_section": "7. Product Specification"
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
  "stable_id": "BRD-WS-02-R002",
  "title": "Mỗi YSim Product phải có Product Specification chuẩn",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-02-R003 — Tuy nhiên Product Specification phải phản ánh đúng khả năng sử dụng thực tế của eSIM

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-02-R003-AC001",
      "given": "the applicable business context, actor, and input for Tuy nhiên Product Specification phải phản ánh đúng khả năng sử dụng thực tế của eSIM",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-02-R003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-02-R003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Tuy nhiên Product Specification phải phản ánh đúng khả năng sử dụng thực tế của eSIM",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-02-R003-O001"
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
        "BRD-WS-02-R003-AC001",
        "BRD-WS-02-R003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-02-R003-O001",
      "obligation_text": "Tuy nhiên Product Specification phải phản ánh đúng khả năng sử dụng thực tế của eSIM"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Tuy nhiên Product Specification phải phản ánh đúng khả năng sử dụng thực tế của eSIM.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-02-003",
    "previous_temporary_key": "TMP-BRD-WS-02-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Product Specification",
    "source_context_sha256": "d7612da5223a59b34cf5f31ed5d0f6b24a088ad9cad981382b42647856dc2e29",
    "source_document": "docs/BRD/BRD-WS-02.md",
    "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
    "source_lines": "L193",
    "source_section": "7. Product Specification"
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
  "stable_id": "BRD-WS-02-R003",
  "title": "Tuy nhiên Product Specification phải phản ánh đúng khả năng sử dụng thực tế của eSIM",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-02-R004 — Inventory luôn tồn tại

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-02-R004-AC001",
      "given": "the applicable business context, actor, and input for Inventory luôn tồn tại",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-02-R004-O001"
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
        "BRD-WS-02-R004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-02-R004-O001",
      "obligation_text": "Inventory luôn tồn tại"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Inventory luôn tồn tại.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-02-004",
    "previous_temporary_key": "TMP-BRD-WS-02-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Inventory Strategy",
    "source_context_sha256": "76bbf48c25b2025bff4104c11af6bb8c6c5bb117a75fd18750975701f7918cdc",
    "source_document": "docs/BRD/BRD-WS-02.md",
    "source_fingerprint": "42cf4a9d51db01c52c656589d8253e7da10ce639572bfabf27c7a36f69937102",
    "source_lines": "L294",
    "source_section": "11. Inventory Strategy"
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
  "stable_id": "BRD-WS-02-R004",
  "title": "Inventory luôn tồn tại",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-02-R005 — Dù theo hình thức nào, mọi Product Item đều phải được ghi nhận vào Inventory

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-02-R005-AC001",
      "given": "the applicable business context, actor, and input for Dù theo hình thức nào, mọi Product Item đều phải được ghi nhận vào Inventory",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-02-R005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-02-R005-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Dù theo hình thức nào, mọi Product Item đều phải được ghi nhận vào Inventory",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-02-R005-O001"
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
        "BRD-WS-02-R005-AC001",
        "BRD-WS-02-R005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-02-R005-O001",
      "obligation_text": "Dù theo hình thức nào, mọi Product Item đều phải được ghi nhận vào Inventory"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-02-R005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-02-R005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-02-R005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-02-R005 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-02-R005-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-02-R005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Dù theo hình thức nào, mọi Product Item đều phải được ghi nhận vào Inventory.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-02-005",
    "previous_temporary_key": "TMP-BRD-WS-02-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Procurement",
    "source_context_sha256": "377e072cfa8bcc23b6d97045bcb6edf274f97036bdf44a1016faada16fb6d1d6",
    "source_document": "docs/BRD/BRD-WS-02.md",
    "source_fingerprint": "efe2b9be4bf4ab6bacce8451064efe73631b539bb8a58a6f8c19d56bb8bada9b",
    "source_lines": "L350",
    "source_section": "13. Procurement"
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
  "stable_id": "BRD-WS-02-R005",
  "title": "Dù theo hình thức nào, mọi Product Item đều phải được ghi nhận vào Inventory",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-02-R006 — Toàn bộ Settlement phải sử dụng **Snapshot Pricing**

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-02-R006-AC001",
      "given": "a candidate Toàn bộ Settlement phải sử dụng **Snapshot Pricing** record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-WS-02-R006-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-02-R006-AC002",
      "given": "a Toàn bộ Settlement phải sử dụng **Snapshot Pricing** candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BRD-WS-02-R006-O001"
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
        "BRD-WS-02-R006-AC001",
        "BRD-WS-02-R006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-02-R006-O001",
      "obligation_text": "Toàn bộ Settlement phải sử dụng **Snapshot Pricing**"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-02-R006 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-02-R006 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-02-R006 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-02-R006 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-02-R006-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-02-R006 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ Settlement phải sử dụng **Snapshot Pricing**.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-02-006",
    "previous_temporary_key": "TMP-BRD-WS-02-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Settlement Model",
    "source_context_sha256": "ec06c47a8c4e338f3c476d4ef4899a8d3ae56d8ac9bb9800d8be2675fde0bff1",
    "source_document": "docs/BRD/BRD-WS-02.md",
    "source_fingerprint": "e45959b3c665bf3a011395e1fdeb3e5e4e5dc62721e3867696b09ecca8634bf4",
    "source_lines": "L438",
    "source_section": "16. Settlement Model"
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
  "stable_id": "BRD-WS-02-R006",
  "title": "Toàn bộ Settlement phải sử dụng **Snapshot Pricing**",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
