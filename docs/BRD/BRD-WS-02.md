---
document_code: "BRD-WS-02"
document_id: "BRD-WS-02"
title: "Business Model & Revenue Architecture"
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

Trong phạm vi Inventory Strategy v2.3, mỗi Product Item được quản lý trong Inventory phải có đúng một Inventory Record. Inventory Record lưu các dữ liệu áp dụng gồm QR Code, ICCID, Activation Code, Supplier Reference, Purchase Cost, Current Owner, Inventory Status và Lifecycle; quy tắc này vẫn áp dụng khi item được mua tức thời từ Supplier cho một đơn hàng cụ thể.

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

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-02-001 — **Decision** Business Entity trung tâm của YSim là Product. **Rationale** Product là đối tượng đ…

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
      "requirement_id": "BD-02-001",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "source_fingerprint": "1f12873fd757d0631fb4e720417af4f653d2afce7011b8635c15af6d9619127a"
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
        "BD-02-001-AC001",
        "BD-02-001-AC002",
        "BD-02-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-001-O001",
      "obligation_text": "**Decision** Business Entity trung tâm của YSim là Product. **Rationale** Product là đối tượng được khách hàng lựa chọn, là nền tảng của Catalog, Pricing, Allocation, Inventory, Fulfillment và Reporting"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-001 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-001 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-001 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-02-001-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-02-001-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-001 does not define a recovery obligation."
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
    "source_fingerprint": "1f12873fd757d0631fb4e720417af4f653d2afce7011b8635c15af6d9619127a",
    "source_lines": "L632-L746",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-02-001"
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
      "requirement_id": "BD-02-002",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "source_fingerprint": "77f301e076ffed907b53e276c51af44cdd789642d1d99337fabd4bfc4eed953a"
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
        "BD-02-002-AC001",
        "BD-02-002-AC003",
        "BD-02-002-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-002-O001",
      "obligation_text": "**Decision** Supplier Product và YSim Product là hai Business Object khác nhau. **Rationale** Supplier Product phản ánh sản phẩm gốc của nhà cung cấp"
    },
    {
      "acceptance_criterion_references": [
        "BD-02-002-AC002",
        "BD-02-002-AC003",
        "BD-02-002-AC004"
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
    "source_fingerprint": "77f301e076ffed907b53e276c51af44cdd789642d1d99337fabd4bfc4eed953a",
    "source_lines": "L748-L837",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-02-002"
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
      "requirement_id": "BD-02-003",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "source_fingerprint": "9cc41f072b0d72211bba3cf7c5183877c272f12144b3c0a2f5221e5a7fb49e61"
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-003 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-02-003-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-02-003-AC001",
        "BD-02-003-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-003 does not define a recovery obligation."
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
    "source_fingerprint": "9cc41f072b0d72211bba3cf7c5183877c272f12144b3c0a2f5221e5a7fb49e61",
    "source_lines": "L839-L962",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-02-003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-02-004",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "source_fingerprint": "f17e338d58414bd804c08bcab882b53038db88284a3eb9058337443188d9bbd3"
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
        "BD-02-004-AC001",
        "BD-02-004-AC003",
        "BD-02-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-004-O001",
      "obligation_text": "**Decision** Inventory được định nghĩa là Digital Asset Inventory"
    },
    {
      "acceptance_criterion_references": [
        "BD-02-004-AC002",
        "BD-02-004-AC003",
        "BD-02-004-AC004"
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
    "source_fingerprint": "f17e338d58414bd804c08bcab882b53038db88284a3eb9058337443188d9bbd3",
    "source_lines": "L964-L1049",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-02-004"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "Immediate purchase and normal procurement have different acquisition paths but the same record obligation"
    ],
    "concrete_bindings": [
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-02-005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                "source_type": "SOURCE_LITERAL",
                "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
              },
              "identifier": "BD-02-005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                "source_lines": "L502-L513",
                "source_section": "17. Business Decisions (Locked) > BD-02-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BD-02-005.BD-02-005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
            "source_lines": "L502-L513",
            "source_section": "17. Business Decisions (Locked) > BD-02-005"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-02-005.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                "source_type": "SOURCE_LITERAL",
                "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
              },
              "identifier": "BD-02-005.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                "source_lines": "L502-L513",
                "source_section": "17. Business Decisions (Locked) > BD-02-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BD-02-005.BD-02-005.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
            "source_lines": "L502-L513",
            "source_section": "17. Business Decisions (Locked) > BD-02-005"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
            "source_type": "SOURCE_LITERAL",
            "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
          },
          "identifier": "BD-02-005.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
            "source_lines": "L502-L513",
            "source_section": "17. Business Decisions (Locked) > BD-02-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BD-02-005.BD-02-005.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
            "source_type": "SOURCE_LITERAL",
            "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
          },
          "identifier": "BD-02-005.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
            "source_lines": "L502-L513",
            "source_section": "17. Business Decisions (Locked) > BD-02-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BD-02-005.BD-02-005.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
            "source_type": "SOURCE_LITERAL",
            "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
          },
          "identifier": "BD-02-005.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
            "source_lines": "L502-L513",
            "source_section": "17. Business Decisions (Locked) > BD-02-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BD-02-005.BD-02-005.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
            "source_type": "SOURCE_LITERAL",
            "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
          },
          "identifier": "BD-02-005.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
            "source_lines": "L502-L513",
            "source_section": "17. Business Decisions (Locked) > BD-02-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BD-02-005.BD-02-005.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
            "source_type": "SOURCE_LITERAL",
            "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
          },
          "identifier": "BD-02-005.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
            "source_lines": "L502-L513",
            "source_section": "17. Business Decisions (Locked) > BD-02-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.BD-02-005.BD-02-005.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      },
      {
        "baseline": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BD-02-005.BASELINE"
            ],
            "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
            "source_type": "SOURCE_LITERAL",
            "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
          },
          "identifier": "BD-02-005.BASELINE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.BASELINE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
            "source_lines": "L502-L513",
            "source_section": "17. Business Decisions (Locked) > BD-02-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "RESOLVE.BD-02-005.BD-02-005.BASELINE",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        },
        "scope": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BD-02-005.SCOPE"
            ],
            "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
            "source_type": "SOURCE_LITERAL",
            "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
          },
          "identifier": "BD-02-005.SCOPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.SCOPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
            "source_lines": "L502-L513",
            "source_section": "17. Business Decisions (Locked) > BD-02-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "RESOLVE.BD-02-005.BD-02-005.SCOPE",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        },
        "subject": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
            "source_type": "SOURCE_LITERAL",
            "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
          },
          "identifier": "BD-02-005.SUBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.SUBJECT.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
            "source_lines": "L502-L513",
            "source_section": "17. Business Decisions (Locked) > BD-02-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BD-02-005.BD-02-005.SUBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BD-02-005",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "A Product Item exists without an Inventory Record"
    ],
    "operator_composition": [
      "REFERENCE_TARGET_VALID",
      "SCOPE_ACTIVE"
    ],
    "positive_oracle": [
      "An Inventory Record is created for every Product Item, including immediate purchase, supporting accounting, audit, traceability, refund and support"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2-DEC-008"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-02.md",
      "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
      "source_lines": "L502-L513",
      "source_section": "17. Business Decisions (Locked) > BD-02-005"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
          "source_type": "SOURCE_LITERAL",
          "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
        },
        "identifier": "BD-02-005.BD-02-005.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BD-02-005.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2-DEC-008"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-02.md",
          "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
          "source_lines": "L502-L513",
          "source_section": "17. Business Decisions (Locked) > BD-02-005"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BD-02-005.BD-02-005.BD-02-005.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BD-02-005.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.PRODUCT_ITEM_ID",
        "FIELD.ACQUISITION_PATH",
        "FIELD.INVENTORY_RECORD_ID",
        "FIELD.ACCOUNTING_REF",
        "FIELD.AUDIT_REF",
        "FIELD.TRACEABILITY_REF"
      ],
      "producer": "BD-02-005.EVIDENCE.PRODUCER",
      "required_collection_origin": "BD-02-005.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.PRODUCT_ITEM_ID",
        "FIELD.ACQUISITION_PATH",
        "FIELD.INVENTORY_RECORD_ID",
        "FIELD.ACCOUNTING_REF",
        "FIELD.AUDIT_REF",
        "FIELD.TRACEABILITY_REF"
      ],
      "required_values_or_hashes": [
        "BD-02-005.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BD-02-005.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BD-02-005.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BD-02-005-O001",
      "BD-02-005-O002"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID",
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
              "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
              "source_type": "SOURCE_LITERAL",
              "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
            },
            "identifier": "BD-02-005.BD-02-005.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
              "source_lines": "L502-L513",
              "source_section": "17. Business Decisions (Locked) > BD-02-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-02-005.BD-02-005.BD-02-005.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
              "source_type": "SOURCE_LITERAL",
              "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
            },
            "identifier": "BD-02-005.BD-02-005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
              "source_lines": "L502-L513",
              "source_section": "17. Business Decisions (Locked) > BD-02-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.BD-02-005.BD-02-005.BD-02-005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                        "BD-02-005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                    },
                    "identifier": "BD-02-005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-02.md",
                      "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                      "source_lines": "L502-L513",
                      "source_section": "17. Business Decisions (Locked) > BD-02-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BD-02-005.BD-02-005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                  "source_lines": "L502-L513",
                  "source_section": "17. Business Decisions (Locked) > BD-02-005"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BD-02-005.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                      "source_type": "SOURCE_LITERAL",
                      "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                    },
                    "identifier": "BD-02-005.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-02.md",
                      "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                      "source_lines": "L502-L513",
                      "source_section": "17. Business Decisions (Locked) > BD-02-005"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BD-02-005.BD-02-005.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                  "source_lines": "L502-L513",
                  "source_section": "17. Business Decisions (Locked) > BD-02-005"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                },
                "identifier": "BD-02-005.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                  "source_lines": "L502-L513",
                  "source_section": "17. Business Decisions (Locked) > BD-02-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BD-02-005.BD-02-005.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                },
                "identifier": "BD-02-005.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                  "source_lines": "L502-L513",
                  "source_section": "17. Business Decisions (Locked) > BD-02-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BD-02-005.BD-02-005.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                },
                "identifier": "BD-02-005.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                  "source_lines": "L502-L513",
                  "source_section": "17. Business Decisions (Locked) > BD-02-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BD-02-005.BD-02-005.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                },
                "identifier": "BD-02-005.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                  "source_lines": "L502-L513",
                  "source_section": "17. Business Decisions (Locked) > BD-02-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BD-02-005.BD-02-005.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                },
                "identifier": "BD-02-005.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                  "source_lines": "L502-L513",
                  "source_section": "17. Business Decisions (Locked) > BD-02-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.BD-02-005.BD-02-005.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                },
                "identifier": "BD-02-005.BD-02-005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                  "source_lines": "L502-L513",
                  "source_section": "17. Business Decisions (Locked) > BD-02-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BD-02-005.BD-02-005.BD-02-005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                },
                "identifier": "BD-02-005.BD-02-005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                  "source_lines": "L502-L513",
                  "source_section": "17. Business Decisions (Locked) > BD-02-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.BD-02-005.BD-02-005.BD-02-005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                "source_type": "SOURCE_LITERAL",
                "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
              },
              "identifier": "BD-02-005.BD-02-005.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                "source_lines": "L502-L513",
                "source_section": "17. Business Decisions (Locked) > BD-02-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-02-005.BD-02-005.BD-02-005.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "BD-02-005-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
              "source_type": "SOURCE_LITERAL",
              "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
            },
            "identifier": "BD-02-005.BD-02-005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
              "source_lines": "L502-L513",
              "source_section": "17. Business Decisions (Locked) > BD-02-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.BD-02-005.BD-02-005.BD-02-005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                      "BD-02-005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                  },
                  "identifier": "BD-02-005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-02.md",
                    "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                    "source_lines": "L502-L513",
                    "source_section": "17. Business Decisions (Locked) > BD-02-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BD-02-005.BD-02-005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                "source_lines": "L502-L513",
                "source_section": "17. Business Decisions (Locked) > BD-02-005"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BD-02-005.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                    "source_type": "SOURCE_LITERAL",
                    "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                  },
                  "identifier": "BD-02-005.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-02.md",
                    "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                    "source_lines": "L502-L513",
                    "source_section": "17. Business Decisions (Locked) > BD-02-005"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BD-02-005.BD-02-005.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                "source_lines": "L502-L513",
                "source_section": "17. Business Decisions (Locked) > BD-02-005"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                "source_type": "SOURCE_LITERAL",
                "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
              },
              "identifier": "BD-02-005.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                "source_lines": "L502-L513",
                "source_section": "17. Business Decisions (Locked) > BD-02-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BD-02-005.BD-02-005.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                "source_type": "SOURCE_LITERAL",
                "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
              },
              "identifier": "BD-02-005.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                "source_lines": "L502-L513",
                "source_section": "17. Business Decisions (Locked) > BD-02-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BD-02-005.BD-02-005.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                "source_type": "SOURCE_LITERAL",
                "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
              },
              "identifier": "BD-02-005.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                "source_lines": "L502-L513",
                "source_section": "17. Business Decisions (Locked) > BD-02-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BD-02-005.BD-02-005.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                "source_type": "SOURCE_LITERAL",
                "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
              },
              "identifier": "BD-02-005.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                "source_lines": "L502-L513",
                "source_section": "17. Business Decisions (Locked) > BD-02-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BD-02-005.BD-02-005.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                "source_type": "SOURCE_LITERAL",
                "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
              },
              "identifier": "BD-02-005.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-02-005.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                "source_lines": "L502-L513",
                "source_section": "17. Business Decisions (Locked) > BD-02-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.BD-02-005.BD-02-005.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        },
        {
          "assertion_id": "BD-02-005.O2.1.SCOPE_ACTIVE",
          "evaluator_consumed_bindings": [
            "baseline",
            "scope",
            "subject"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
              "source_type": "SOURCE_LITERAL",
              "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
            },
            "identifier": "BD-02-005.BD-02-005.O2.1.SCOPE_ACTIVE.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
              "source_lines": "L502-L513",
              "source_section": "17. Business Decisions (Locked) > BD-02-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-02-005.BD-02-005.BD-02-005.O2.1.SCOPE_ACTIVE.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
              "source_type": "SOURCE_LITERAL",
              "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
            },
            "identifier": "BD-02-005.BD-02-005.O2.1.SCOPE_ACTIVE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
              "source_lines": "L502-L513",
              "source_section": "17. Business Decisions (Locked) > BD-02-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "ENTITY_ID",
              "resolver_id": "RESOLVE.BD-02-005.BD-02-005.BD-02-005.O2.1.SCOPE_ACTIVE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "ENTITY_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "baseline": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-02-005.BASELINE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                },
                "identifier": "BD-02-005.BASELINE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.BASELINE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                  "source_lines": "L502-L513",
                  "source_section": "17. Business Decisions (Locked) > BD-02-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BD-02-005.BD-02-005.BASELINE",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "scope": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-02-005.SCOPE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                },
                "identifier": "BD-02-005.SCOPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.SCOPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                  "source_lines": "L502-L513",
                  "source_section": "17. Business Decisions (Locked) > BD-02-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BD-02-005.BD-02-005.SCOPE",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "subject": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                },
                "identifier": "BD-02-005.SUBJECT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.SUBJECT.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                  "source_lines": "L502-L513",
                  "source_section": "17. Business Decisions (Locked) > BD-02-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BD-02-005.BD-02-005.SUBJECT",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                },
                "identifier": "BD-02-005.BD-02-005.O2.1.SCOPE_ACTIVE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                  "source_lines": "L502-L513",
                  "source_section": "17. Business Decisions (Locked) > BD-02-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BD-02-005.BD-02-005.BD-02-005.O2.1.SCOPE_ACTIVE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
                },
                "identifier": "BD-02-005.BD-02-005.O2.1.SCOPE_ACTIVE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                  "source_lines": "L502-L513",
                  "source_section": "17. Business Decisions (Locked) > BD-02-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "OBSERVE.BD-02-005.BD-02-005.BD-02-005.O2.1.SCOPE_ACTIVE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                "source_type": "SOURCE_LITERAL",
                "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
              },
              "identifier": "BD-02-005.BD-02-005.O2.1.SCOPE_ACTIVE.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                "source_lines": "L502-L513",
                "source_section": "17. Business Decisions (Locked) > BD-02-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-02-005.BD-02-005.BD-02-005.O2.1.SCOPE_ACTIVE.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "SCOPE_ACTIVE"
          },
          "obligation_id": "BD-02-005-O002",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
              "source_type": "SOURCE_LITERAL",
              "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
            },
            "identifier": "BD-02-005.BD-02-005.O2.1.SCOPE_ACTIVE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
              "source_lines": "L502-L513",
              "source_section": "17. Business Decisions (Locked) > BD-02-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "ENTITY_ID",
              "resolver_id": "OBSERVE.BD-02-005.BD-02-005.BD-02-005.O2.1.SCOPE_ACTIVE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "ENTITY_ID"
          },
          "operator_id": "SCOPE_ACTIVE",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "baseline": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-02-005.BASELINE"
                ],
                "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                "source_type": "SOURCE_LITERAL",
                "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
              },
              "identifier": "BD-02-005.BASELINE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.BASELINE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                "source_lines": "L502-L513",
                "source_section": "17. Business Decisions (Locked) > BD-02-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-02-005.BD-02-005.BASELINE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            "scope": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-02-005.SCOPE"
                ],
                "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                "source_type": "SOURCE_LITERAL",
                "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
              },
              "identifier": "BD-02-005.SCOPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.SCOPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                "source_lines": "L502-L513",
                "source_section": "17. Business Decisions (Locked) > BD-02-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BD-02-005.BD-02-005.SCOPE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            "subject": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
                "source_type": "SOURCE_LITERAL",
                "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
              },
              "identifier": "BD-02-005.SUBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-02-005.O2.1.SCOPE_ACTIVE.SUBJECT.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
                "source_lines": "L502-L513",
                "source_section": "17. Business Decisions (Locked) > BD-02-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BD-02-005.BD-02-005.SUBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            }
          }
        }
      ],
      "boundary_cases": [
        "Immediate purchase and normal procurement have different acquisition paths but the same record obligation"
      ],
      "contract_ast_sha256": "8b90c65da30ced98d2e91a477b4d7b7d878140229dc53694bb4718733ec18464",
      "contract_id": "P2C.C4.CONTRACT.BD-02-005",
      "criticality": "CRITICAL",
      "disposition": "COMPOUND_AST_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-02.md#17. Business Decisions (Locked) > BD-02-005",
            "source_type": "SOURCE_LITERAL",
            "version": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe"
          },
          "identifier": "BD-02-005.BD-02-005.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-02-005.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
            "source_lines": "L502-L513",
            "source_section": "17. Business Decisions (Locked) > BD-02-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BD-02-005.BD-02-005.BD-02-005.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BD-02-005.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.PRODUCT_ITEM_ID",
          "FIELD.ACQUISITION_PATH",
          "FIELD.INVENTORY_RECORD_ID",
          "FIELD.ACCOUNTING_REF",
          "FIELD.AUDIT_REF",
          "FIELD.TRACEABILITY_REF"
        ],
        "producer": "BD-02-005.EVIDENCE.PRODUCER",
        "required_collection_origin": "BD-02-005.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.PRODUCT_ITEM_ID",
          "FIELD.ACQUISITION_PATH",
          "FIELD.INVENTORY_RECORD_ID",
          "FIELD.ACCOUNTING_REF",
          "FIELD.AUDIT_REF",
          "FIELD.TRACEABILITY_REF"
        ],
        "required_values_or_hashes": [
          "BD-02-005.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BD-02-005.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BD-02-005.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-61047493F1B6BF01933A",
        "P2C-C4-FX-D5A93015A256313F589F",
        "P2C-C4-FX-FC8EFBE5136DEF9D85D1"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "A Product Item exists without an Inventory Record"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-02-005-O001",
          "obligation_text": "**Decision** Mọi Product Item đều phải có Inventory Record"
        },
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-02-005-O002",
          "obligation_text": "Kể cả mua tức thời. **Rationale** Đảm bảo Accounting, Audit, Traceability, Refund và Customer Support"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BD-02-005.O1.1.REFERENCE_TARGET_VALID"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-02-005-O001"
        },
        {
          "assertion_ids": [
            "BD-02-005.O2.1.SCOPE_ACTIVE"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-02-005-O002"
        }
      ],
      "operator_composition": [
        "REFERENCE_TARGET_VALID",
        "SCOPE_ACTIVE"
      ],
      "positive_oracles": [
        "An Inventory Record is created for every Product Item, including immediate purchase, supporting accounting, audit, traceability, refund and support"
      ],
      "preconditions": [
        "A canonical Product Item identity exists"
      ],
      "prohibitions": [
        "A Product Item exists without an Inventory Record"
      ],
      "requirement_id": "BD-02-005",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2-DEC-008"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-02.md",
        "source_fingerprint": "2e2e73a64b6338360b13b6999f74bca61893416d8fe14a6382fd93aff2ef8efe",
        "source_lines": "L502-L513",
        "source_section": "17. Business Decisions (Locked) > BD-02-005"
      },
      "source_statement": "**Decision** Mọi Product Item đều phải có Inventory Record. Kể cả mua tức thời. **Rationale** Đảm bảo Accounting, Audit, Traceability, Refund và Customer Support.",
      "surrounding_source_context": "## BD-02-005\n\n**Decision**\n\nMọi Product Item đều phải có Inventory Record.\n\nKể cả mua tức thời.\n\n**Rationale**\n\nĐảm bảo Accounting, Audit, Traceability, Refund và Customer Support.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BD-02-005",
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
        "BD-02-005-AC001",
        "BD-02-005-AC003",
        "BD-02-005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-005-O001",
      "obligation_text": "**Decision** Mọi Product Item đều phải có Inventory Record"
    },
    {
      "acceptance_criterion_references": [
        "BD-02-005-AC002",
        "BD-02-005-AC003",
        "BD-02-005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-005-O002",
      "obligation_text": "Kể cả mua tức thời. **Rationale** Đảm bảo Accounting, Audit, Traceability, Refund và Customer Support"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-005 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-02-005-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-02-005-AC001",
        "BD-02-005-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-005 does not define a recovery obligation."
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
    "source_fingerprint": "19d6c18ce3fa6fb4292491d05eeb73441d3c5a18c5ea63df6aff24f38c62cf38",
    "source_lines": "L1051-L3120",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-02-005"
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
      "requirement_id": "BD-02-006",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "source_fingerprint": "f0f66f4297f48d70e46fc74b5b466a6eec6dab90f3663e402a98d3611df41681"
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
        "BD-02-006-AC001",
        "BD-02-006-AC002",
        "BD-02-006-AC003"
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
    "source_fingerprint": "f0f66f4297f48d70e46fc74b5b466a6eec6dab90f3663e402a98d3611df41681",
    "source_lines": "L3122-L3203",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-02-006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-02-007",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "source_fingerprint": "05576e69f9f3b02cba1a23afd61887a75929bf860a4e95e3d1f3d45d2dd60884"
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
        "BD-02-007-AC001",
        "BD-02-007-AC002",
        "BD-02-007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-02-007-O001",
      "obligation_text": "**Decision** Snapshot Pricing là nguyên tắc bắt buộc. **Rationale** Mọi Settlement và nghiệp vụ tài chính phải sử dụng giá tại thời điểm phát sinh giao dịch"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-007 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-02-007-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-02-007-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-02-007 does not define a recovery obligation."
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
    "source_fingerprint": "05576e69f9f3b02cba1a23afd61887a75929bf860a4e95e3d1f3d45d2dd60884",
    "source_lines": "L3205-L3313",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-02-007"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "Draft may remain incomplete; publication requires the specification"
    ],
    "concrete_bindings": [
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-02-R002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                "source_type": "SOURCE_LITERAL",
                "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
              },
              "identifier": "BRD-WS-02-R002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                "source_lines": "L173",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
            "source_lines": "L173",
            "source_section": "7. Product Specification"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-02-R002.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                "source_type": "SOURCE_LITERAL",
                "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
              },
              "identifier": "BRD-WS-02-R002.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                "source_lines": "L173",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
            "source_lines": "L173",
            "source_section": "7. Product Specification"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
            "source_type": "SOURCE_LITERAL",
            "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
          },
          "identifier": "BRD-WS-02-R002.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
            "source_lines": "L173",
            "source_section": "7. Product Specification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
            "source_type": "SOURCE_LITERAL",
            "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
          },
          "identifier": "BRD-WS-02-R002.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
            "source_lines": "L173",
            "source_section": "7. Product Specification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
            "source_type": "SOURCE_LITERAL",
            "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
          },
          "identifier": "BRD-WS-02-R002.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
            "source_lines": "L173",
            "source_section": "7. Product Specification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
            "source_type": "SOURCE_LITERAL",
            "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
          },
          "identifier": "BRD-WS-02-R002.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
            "source_lines": "L173",
            "source_section": "7. Product Specification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
            "source_type": "SOURCE_LITERAL",
            "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
          },
          "identifier": "BRD-WS-02-R002.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
            "source_lines": "L173",
            "source_section": "7. Product Specification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-02-R002",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "The Product is published without a Product Specification"
    ],
    "operator_composition": [
      "REFERENCE_TARGET_VALID"
    ],
    "positive_oracle": [
      "The Product has a standard Product Specification"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-02.md",
      "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
      "source_lines": "L173",
      "source_section": "7. Product Specification"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
          "source_type": "SOURCE_LITERAL",
          "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
        },
        "identifier": "BRD-WS-02-R002.BRD-WS-02-R002.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-02-R002.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-02.md",
          "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
          "source_lines": "L173",
          "source_section": "7. Product Specification"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-02-R002.BRD-WS-02-R002.BRD-WS-02-R002.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-02-R002.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.PRODUCT_ID",
        "FIELD.SPECIFICATION_ID",
        "FIELD.SPECIFICATION_VERSION",
        "FIELD.PUBLISH_STATE",
        "FIELD.VALIDATION_RESULT"
      ],
      "producer": "BRD-WS-02-R002.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-02-R002.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.PRODUCT_ID",
        "FIELD.SPECIFICATION_ID",
        "FIELD.SPECIFICATION_VERSION",
        "FIELD.PUBLISH_STATE",
        "FIELD.VALIDATION_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-WS-02-R002.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-02-R002.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-02-R002.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-02-R002-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID",
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
              "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
              "source_type": "SOURCE_LITERAL",
              "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
            },
            "identifier": "BRD-WS-02-R002.BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
              "source_lines": "L173",
              "source_section": "7. Product Specification"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-02-R002.BRD-WS-02-R002.BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
              "source_type": "SOURCE_LITERAL",
              "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
            },
            "identifier": "BRD-WS-02-R002.BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
              "source_lines": "L173",
              "source_section": "7. Product Specification"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                        "BRD-WS-02-R002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                      "source_type": "SOURCE_LITERAL",
                      "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
                    },
                    "identifier": "BRD-WS-02-R002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-02.md",
                      "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                      "source_lines": "L173",
                      "source_section": "7. Product Specification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                  "source_lines": "L173",
                  "source_section": "7. Product Specification"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-02-R002.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                      "source_type": "SOURCE_LITERAL",
                      "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
                    },
                    "identifier": "BRD-WS-02-R002.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-02.md",
                      "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                      "source_lines": "L173",
                      "source_section": "7. Product Specification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                  "source_lines": "L173",
                  "source_section": "7. Product Specification"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
                },
                "identifier": "BRD-WS-02-R002.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                  "source_lines": "L173",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
                },
                "identifier": "BRD-WS-02-R002.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                  "source_lines": "L173",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
                },
                "identifier": "BRD-WS-02-R002.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                  "source_lines": "L173",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
                },
                "identifier": "BRD-WS-02-R002.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                  "source_lines": "L173",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
                },
                "identifier": "BRD-WS-02-R002.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                  "source_lines": "L173",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
                },
                "identifier": "BRD-WS-02-R002.BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                  "source_lines": "L173",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
                },
                "identifier": "BRD-WS-02-R002.BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                  "source_lines": "L173",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-02-R002.BRD-WS-02-R002.BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                "source_type": "SOURCE_LITERAL",
                "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
              },
              "identifier": "BRD-WS-02-R002.BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                "source_lines": "L173",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-02-R002.BRD-WS-02-R002.BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "BRD-WS-02-R002-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
              "source_type": "SOURCE_LITERAL",
              "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
            },
            "identifier": "BRD-WS-02-R002.BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
              "source_lines": "L173",
              "source_section": "7. Product Specification"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.BRD-WS-02-R002.BRD-WS-02-R002.BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                      "BRD-WS-02-R002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                    "source_type": "SOURCE_LITERAL",
                    "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
                  },
                  "identifier": "BRD-WS-02-R002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-02.md",
                    "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                    "source_lines": "L173",
                    "source_section": "7. Product Specification"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                "source_lines": "L173",
                "source_section": "7. Product Specification"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BRD-WS-02-R002.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                    "source_type": "SOURCE_LITERAL",
                    "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
                  },
                  "identifier": "BRD-WS-02-R002.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-02.md",
                    "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                    "source_lines": "L173",
                    "source_section": "7. Product Specification"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                "source_lines": "L173",
                "source_section": "7. Product Specification"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                "source_type": "SOURCE_LITERAL",
                "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
              },
              "identifier": "BRD-WS-02-R002.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                "source_lines": "L173",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                "source_type": "SOURCE_LITERAL",
                "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
              },
              "identifier": "BRD-WS-02-R002.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                "source_lines": "L173",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                "source_type": "SOURCE_LITERAL",
                "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
              },
              "identifier": "BRD-WS-02-R002.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                "source_lines": "L173",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                "source_type": "SOURCE_LITERAL",
                "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
              },
              "identifier": "BRD-WS-02-R002.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                "source_lines": "L173",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
                "source_type": "SOURCE_LITERAL",
                "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
              },
              "identifier": "BRD-WS-02-R002.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
                "source_lines": "L173",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.BRD-WS-02-R002.BRD-WS-02-R002.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        }
      ],
      "boundary_cases": [
        "Draft may remain incomplete; publication requires the specification"
      ],
      "contract_ast_sha256": "83d0a25dc36b1a38b2094d4efebdd62d564c9b012d19a5d4cbc349ed65d0541b",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-02-R002",
      "criticality": "HIGH",
      "disposition": "OPERATOR_REMAP_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-02.md#7. Product Specification",
            "source_type": "SOURCE_LITERAL",
            "version": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073"
          },
          "identifier": "BRD-WS-02-R002.BRD-WS-02-R002.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-02-R002.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
            "source_lines": "L173",
            "source_section": "7. Product Specification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-02-R002.BRD-WS-02-R002.BRD-WS-02-R002.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-02-R002.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.PRODUCT_ID",
          "FIELD.SPECIFICATION_ID",
          "FIELD.SPECIFICATION_VERSION",
          "FIELD.PUBLISH_STATE",
          "FIELD.VALIDATION_RESULT"
        ],
        "producer": "BRD-WS-02-R002.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-02-R002.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.PRODUCT_ID",
          "FIELD.SPECIFICATION_ID",
          "FIELD.SPECIFICATION_VERSION",
          "FIELD.PUBLISH_STATE",
          "FIELD.VALIDATION_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-WS-02-R002.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-02-R002.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-02-R002.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-6F6504F3F1E3292DA5C4",
        "P2C-C4-FX-65F1B0C88FA0CCD0B2A8",
        "P2C-C4-FX-FD7418A36FE83B1265FB"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "The Product is published without a Product Specification"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-02-R002-O001",
          "obligation_text": "Mỗi YSim Product phải có Product Specification chuẩn"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-02-R002.O1.1.REFERENCE_TARGET_VALID"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-02-R002-O001"
        }
      ],
      "operator_composition": [
        "REFERENCE_TARGET_VALID"
      ],
      "positive_oracles": [
        "The Product has a standard Product Specification"
      ],
      "preconditions": [
        "A canonical Product identity exists"
      ],
      "prohibitions": [
        "The Product is published without a Product Specification"
      ],
      "requirement_id": "BRD-WS-02-R002",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-02.md",
        "source_fingerprint": "b84948fb45528791425f4593e62c8fd44b8e15ea95340601b141f32469fa6073",
        "source_lines": "L173",
        "source_section": "7. Product Specification"
      },
      "source_statement": "Mỗi YSim Product phải có Product Specification chuẩn.",
      "surrounding_source_context": "### BRD-WS-02-R002 — Mỗi YSim Product phải có Product Specification chuẩn"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-02-R002",
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
        "BRD-WS-02-R002-AC001",
        "BRD-WS-02-R002-AC002",
        "BRD-WS-02-R002-AC003"
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
    "source_lines": "L3315-L4664",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-02-R002"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "Marketing wording may vary but cannot change actual usage semantics"
    ],
    "concrete_bindings": [
      {
        "actual_set": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "ESIM.OPERATIONAL.CAPABILITY.RESOLVER.SET",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "YSIM.ESIM_OPERATIONAL_CAPABILITY.RESOLVED_CAPABILITY_SET.RUNTIME_OBSERVED",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
            "source_lines": "L193",
            "source_section": "7. Product Specification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "OBSERVE.BRD-WS-02-R003.ESIM.OPERATIONAL.CAPABILITY.RESOLVER.SET",
            "version": "1.0.0"
          },
          "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
        },
        "expected_set": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "ESIM.CAPABILITY.REGISTRY.ACTIVE.SET",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "YSIM.ESIM_CAPABILITY_REGISTRY.ACTIVE_CAPABILITY_SET.CANONICAL_REGISTRY",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
            "source_lines": "L193",
            "source_section": "7. Product Specification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "RESOLVE.BRD-WS-02-R003.ESIM.CAPABILITY.REGISTRY.ACTIVE.SET",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
        }
      },
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-02-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-02-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                "source_lines": "L193",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
            "source_lines": "L193",
            "source_section": "7. Product Specification"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-02-R003.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-02-R003.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                "source_lines": "L193",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
            "source_lines": "L193",
            "source_section": "7. Product Specification"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-02-R003.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
            "source_lines": "L193",
            "source_section": "7. Product Specification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-02-R003.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
            "source_lines": "L193",
            "source_section": "7. Product Specification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-02-R003.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
            "source_lines": "L193",
            "source_section": "7. Product Specification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-02-R003.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
            "source_lines": "L193",
            "source_section": "7. Product Specification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-02-R003.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
            "source_lines": "L193",
            "source_section": "7. Product Specification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-02-R003",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Specification claims an unsupported capability or omits a required usage constraint"
    ],
    "operator_composition": [
      "SET_EQUALS",
      "REFERENCE_TARGET_VALID"
    ],
    "positive_oracle": [
      "The Product Specification matches actual eSIM usage capability"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-02.md",
      "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
      "source_lines": "L193",
      "source_section": "7. Product Specification"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
          "source_type": "APPROVED_DECISION",
          "version": "2026-07-16"
        },
        "identifier": "BRD-WS-02-R003.BRD-WS-02-R003.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-02-R003.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-02.md",
          "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
          "source_lines": "L193",
          "source_section": "7. Product Specification"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-02-R003.BRD-WS-02-R003.BRD-WS-02-R003.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-02-R003.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.PRODUCT_ID",
        "FIELD.SPECIFICATION_CAPABILITIES",
        "FIELD.ACTUAL_CAPABILITIES",
        "FIELD.VALIDATION_RESULT",
        "FIELD.SOURCE_VERSION"
      ],
      "producer": "BRD-WS-02-R003.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-02-R003.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.PRODUCT_ID",
        "FIELD.SPECIFICATION_CAPABILITIES",
        "FIELD.ACTUAL_CAPABILITIES",
        "FIELD.VALIDATION_RESULT",
        "FIELD.SOURCE_VERSION"
      ],
      "required_values_or_hashes": [
        "BRD-WS-02-R003.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-02-R003.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-02-R003.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-02-R003-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": {
        "meaning": "A versioned canonical eSIM Capability Registry is compared with an independently resolved operational capability set.",
        "non_inferences": [
          "No capability member is invented.",
          "Provider-native schemas need not be identical."
        ],
        "option_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
      },
      "assertions": [
        {
          "assertion_id": "BRD-WS-02-R003.O1.1.SET_EQUALS",
          "evaluator_consumed_bindings": [
            "actual_set",
            "expected_set"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-02-R003.O1.1.SET_EQUALS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
              "source_lines": "L193",
              "source_section": "7. Product Specification"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-02-R003.BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R003.O1.1.SET_EQUALS.AUTHORITY.ORIGIN.MEMBER.1",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BRD-WS-02-R003.O1.1.SET_EQUALS.AUTHORITY.ORIGIN",
              "origin_type": "APPROVED_DECISION"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
              "source_lines": "L193",
              "source_section": "7. Product Specification"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_set": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "ESIM.OPERATIONAL.CAPABILITY.RESOLVER.SET",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "YSIM.ESIM_OPERATIONAL_CAPABILITY.RESOLVED_CAPABILITY_SET.RUNTIME_OBSERVED",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "OBSERVE.BRD-WS-02-R003.ESIM.OPERATIONAL.CAPABILITY.RESOLVER.SET",
                  "version": "1.0.0"
                },
                "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
              },
              "expected_set": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "ESIM.CAPABILITY.REGISTRY.ACTIVE.SET",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "YSIM.ESIM_CAPABILITY_REGISTRY.ACTIVE_CAPABILITY_SET.CANONICAL_REGISTRY",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "RESOLVE.BRD-WS-02-R003.ESIM.CAPABILITY.REGISTRY.ACTIVE.SET",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
              }
            },
            "comparison": {
              "expected": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-02-R003.O1.1.SET_EQUALS.AUTHORITY.ORIGIN.MEMBER.1",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-02.md",
                      "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                      "source_lines": "L193",
                      "source_section": "7. Product Specification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-02-R003.O1.1.SET_EQUALS.AUTHORITY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "observed": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-02-R003.O1.1.SET_EQUALS.OBSERVED.ORIGIN.MEMBER.1",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-02.md",
                      "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                      "source_lines": "L193",
                      "source_section": "7. Product Specification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "OBSERVE.BRD-WS-02-R003.BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-02-R003.O1.1.SET_EQUALS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R003.O1.1.SET_EQUALS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                "source_lines": "L193",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-02-R003.BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "SET_EQUALS"
          },
          "obligation_id": "BRD-WS-02-R003-O001",
          "observed_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R003.O1.1.SET_EQUALS.OBSERVED.ORIGIN.MEMBER.1",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BRD-WS-02-R003.BRD-WS-02-R003.BRD-WS-02-R003.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BRD-WS-02-R003.O1.1.SET_EQUALS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
              "source_lines": "L193",
              "source_section": "7. Product Specification"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "operator_id": "SET_EQUALS",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_set": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "ESIM.OPERATIONAL.CAPABILITY.RESOLVER.SET",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "YSIM.ESIM_OPERATIONAL_CAPABILITY.RESOLVED_CAPABILITY_SET.RUNTIME_OBSERVED",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                "source_lines": "L193",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "OBSERVE.BRD-WS-02-R003.ESIM.OPERATIONAL.CAPABILITY.RESOLVER.SET",
                "version": "1.0.0"
              },
              "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
            },
            "expected_set": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "ESIM.CAPABILITY.REGISTRY.ACTIVE.SET",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "YSIM.ESIM_CAPABILITY_REGISTRY.ACTIVE_CAPABILITY_SET.CANONICAL_REGISTRY",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                "source_lines": "L193",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "RESOLVE.BRD-WS-02-R003.ESIM.CAPABILITY.REGISTRY.ACTIVE.SET",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
            }
          }
        },
        {
          "assertion_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID",
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
              "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BRD-WS-02-R003.BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
              "source_lines": "L193",
              "source_section": "7. Product Specification"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-02-R003.BRD-WS-02-R003.BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BRD-WS-02-R003.BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "APPROVED_DECISION"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
              "source_lines": "L193",
              "source_section": "7. Product Specification"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                        "BRD-WS-02-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "BRD-WS-02-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-02.md",
                      "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                      "source_lines": "L193",
                      "source_section": "7. Product Specification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-02-R003.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "BRD-WS-02-R003.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-02.md",
                      "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                      "source_lines": "L193",
                      "source_section": "7. Product Specification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-02-R003.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-02-R003.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-02-R003.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-02-R003.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-02-R003.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-02-R003.BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-02-R003.BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-02.md",
                  "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                  "source_lines": "L193",
                  "source_section": "7. Product Specification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-02-R003.BRD-WS-02-R003.BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-02-R003.BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                "source_lines": "L193",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-02-R003.BRD-WS-02-R003.BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "BRD-WS-02-R003-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BRD-WS-02-R003.BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-02.md",
              "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
              "source_lines": "L193",
              "source_section": "7. Product Specification"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.BRD-WS-02-R003.BRD-WS-02-R003.BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                      "BRD-WS-02-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "BRD-WS-02-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-02.md",
                    "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                    "source_lines": "L193",
                    "source_section": "7. Product Specification"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                "source_lines": "L193",
                "source_section": "7. Product Specification"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BRD-WS-02-R003.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "BRD-WS-02-R003.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-02.md",
                    "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                    "source_lines": "L193",
                    "source_section": "7. Product Specification"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                "source_lines": "L193",
                "source_section": "7. Product Specification"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-02-R003.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                "source_lines": "L193",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-02-R003.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                "source_lines": "L193",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-02-R003.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                "source_lines": "L193",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-02-R003.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                "source_lines": "L193",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-02-R003.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-02.md",
                "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
                "source_lines": "L193",
                "source_section": "7. Product Specification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.BRD-WS-02-R003.BRD-WS-02-R003.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        }
      ],
      "boundary_cases": [
        "Marketing wording may vary but cannot change actual usage semantics"
      ],
      "contract_ast_sha256": "d8b4b0fc43f80e504489bab23390a56953ccda6d707f292fc4586f23a94d5df8",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-02-R003",
      "criticality": "HIGH",
      "disposition": "SOURCE_CLARIFICATION_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-02-R003.BRD-WS-02-R003.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-02-R003.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-02.md",
            "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
            "source_lines": "L193",
            "source_section": "7. Product Specification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-02-R003.BRD-WS-02-R003.BRD-WS-02-R003.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-02-R003.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.PRODUCT_ID",
          "FIELD.SPECIFICATION_CAPABILITIES",
          "FIELD.ACTUAL_CAPABILITIES",
          "FIELD.VALIDATION_RESULT",
          "FIELD.SOURCE_VERSION"
        ],
        "producer": "BRD-WS-02-R003.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-02-R003.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.PRODUCT_ID",
          "FIELD.SPECIFICATION_CAPABILITIES",
          "FIELD.ACTUAL_CAPABILITIES",
          "FIELD.VALIDATION_RESULT",
          "FIELD.SOURCE_VERSION"
        ],
        "required_values_or_hashes": [
          "BRD-WS-02-R003.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-02-R003.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-02-R003.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-EC0DA27511453DBC914E",
        "P2C-C4-FX-D7AD453C6E35892FDF53",
        "P2C-C4-FX-B387E9104C27FBB1CB95"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Specification claims an unsupported capability or omits a required usage constraint"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-02-R003-O001",
          "obligation_text": "Tuy nhiên Product Specification phải phản ánh đúng khả năng sử dụng thực tế của eSIM"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-02-R003.O1.1.SET_EQUALS",
            "BRD-WS-02-R003.O1.2.REFERENCE_TARGET_VALID"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-02-R003-O001"
        }
      ],
      "operator_composition": [
        "SET_EQUALS",
        "REFERENCE_TARGET_VALID"
      ],
      "positive_oracles": [
        "The Product Specification matches actual eSIM usage capability"
      ],
      "preconditions": [
        "Actual eSIM usage capabilities are known"
      ],
      "prohibitions": [
        "Specification claims an unsupported capability or omits a required usage constraint"
      ],
      "requirement_id": "BRD-WS-02-R003",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2C-OBT-C1-BRD-WS-02-R003-OPT-1"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-02.md",
        "source_fingerprint": "ae96c39e161b05df291f5553a75b7216774b12490e8c08564db14ea303640386",
        "source_lines": "L193",
        "source_section": "7. Product Specification"
      },
      "source_statement": "Tuy nhiên Product Specification phải phản ánh đúng khả năng sử dụng thực tế của eSIM.",
      "surrounding_source_context": "### BRD-WS-02-R003 — Tuy nhiên Product Specification phải phản ánh đúng khả năng sử dụng thực tế của eSIM"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-02-R003",
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
        "BRD-WS-02-R003-AC001",
        "BRD-WS-02-R003-AC002",
        "BRD-WS-02-R003-AC003"
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
    "source_lines": "L4666-L6641",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-02-R003"
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
### BRD-WS-02-R004 — Trong phạm vi Inventory Strategy v2.3, mỗi Product Item được quản lý trong Inventory phải có đúng một Inventory Recor…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2C-SC-C1-DEC-007/OPT-CLARIFY"
      ],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-007",
        "option_id": "OPT-CLARIFY"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-02-R004",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "source_fingerprint": "164d1757848b2601ecac33ae8269e9c8eb05186ee7a2fa879076ec0832843c97"
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
        "BRD-WS-02-R004-AC001",
        "BRD-WS-02-R004-AC002",
        "BRD-WS-02-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-02-R004-O001",
      "obligation_text": "Trong phạm vi Inventory Strategy v2.3, mỗi Product Item được quản lý trong Inventory phải có đúng một Inventory Record. Inventory Record lưu các dữ liệu áp dụng gồm QR Code, ICCID, Activation Code, Supplier Reference, Purchase Cost, Current Owner, Inventory Status và Lifecycle; quy tắc này vẫn áp dụng khi item được mua tức thời từ Supplier cho một đơn hàng cụ thể"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Trong phạm vi Inventory Strategy v2.3, mỗi Product Item được quản lý trong Inventory phải có đúng một Inventory Record. Inventory Record lưu các dữ liệu áp dụng gồm QR Code, ICCID, Activation Code, Supplier Reference, Purchase Cost, Current Owner, Inventory Status và Lifecycle; quy tắc này vẫn áp dụng khi item được mua tức thời từ Supplier cho một đơn hàng cụ thể.",
  "provenance": {
    "approved_decisions": [
      "P2C-SC-C1-DEC-007/OPT-CLARIFY"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-02-004",
    "previous_temporary_key": "TMP-BRD-WS-02-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Inventory Strategy",
    "source_context_sha256": "76bbf48c25b2025bff4104c11af6bb8c6c5bb117a75fd18750975701f7918cdc",
    "source_document": "docs/BRD/BRD-WS-02.md",
    "source_fingerprint": "164d1757848b2601ecac33ae8269e9c8eb05186ee7a2fa879076ec0832843c97",
    "source_lines": "L6643-L6726",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-02-R004"
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
  "title": "Trong phạm vi Inventory Strategy v2.3, mỗi Product Item được quản lý trong Inventory phải có đúng một Inventory Recor…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-02-R005 — Dù theo hình thức nào, mọi Product Item đều phải được ghi nhận vào Inventory

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
      "requirement_id": "BRD-WS-02-R005",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "source_fingerprint": "efe2b9be4bf4ab6bacce8451064efe73631b539bb8a58a6f8c19d56bb8bada9b"
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
        "BRD-WS-02-R005-AC001",
        "BRD-WS-02-R005-AC002",
        "BRD-WS-02-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-02-R005-O001",
      "obligation_text": "Dù theo hình thức nào, mọi Product Item đều phải được ghi nhận vào Inventory"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-02-R005 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-02-R005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-02-R005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-02-R005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-02-R005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-02-R005 does not define a recovery obligation."
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
    "source_lines": "L6728-L6836",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-02-R005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-02-R006",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "source_fingerprint": "e45959b3c665bf3a011395e1fdeb3e5e4e5dc62721e3867696b09ecca8634bf4"
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
        "BRD-WS-02-R006-AC001",
        "BRD-WS-02-R006-AC002",
        "BRD-WS-02-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-02-R006-O001",
      "obligation_text": "Toàn bộ Settlement phải sử dụng **Snapshot Pricing**"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-02-R006 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-02-R006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-02-R006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-02-R006-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-02-R006-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-02-R006 does not define a recovery obligation."
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
    "source_lines": "L6838-L6946",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-02-R006"
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
