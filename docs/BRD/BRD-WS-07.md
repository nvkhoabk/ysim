---
document_code: "BRD-WS-07"
title: "Sales Order, Purchase Order, Cart & Checkout Model"
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

# BRD Workshop 07

# Sales Order, Purchase Order, Cart & Checkout Model

---

# 1. Workshop Objective

Workshop này xác định toàn bộ Transaction Entry của nền tảng YSim.

Workshop bao gồm:

- Cart
- Checkout
- Checkout Session
- Sales Order
- Purchase Order
- Procurement Validation
- Procurement Capacity
- Inventory Reservation
- Allocation Preparation
- Customer Checkout Decision

Workshop này chỉ mô tả quá trình từ Customer lựa chọn sản phẩm đến khi Payment hoàn tất.

Payment Gateway, Fulfillment và Settlement sẽ được mô tả ở các Workshop tiếp theo.

---

# 2. Business Objects Introduced

| Business Object | Type |
|-----------------|------|
| Cart | Transaction |
| Cart Item | Transaction |
| Checkout Session | Transaction |
| Checkout Snapshot | Transaction |
| Sales Order | Transaction |
| Sales Order Item | Transaction |
| Purchase Order | Transaction |
| Purchase Order Item | Transaction |
| Procurement Validation | Transaction |
| Procurement Capacity | Transaction |
| Inventory Reservation | Transaction |
| Customer Checkout Decision | Transaction |
| Fulfillment Assignment | Transaction |

---

# 3. Transaction Domain Principle

Transaction Domain của YSim được chia thành các giai đoạn độc lập.

```text
Cart
    │
    ▼
Checkout
    │
    ▼
Payment
    │
    ▼
Fulfillment
    │
    ▼
Settlement
    │
    ▼
After Sales
```

Mỗi Workshop chỉ chịu trách nhiệm một giai đoạn.

---

# 4. Order Taxonomy

YSim định nghĩa hai loại Order độc lập.

## Sales Order (SO)

Sales Order phát sinh từ các kênh bán hàng.

SO là giao dịch giữa:

Organization

↓

Customer

Sales Order quản lý:

- Product
- Quantity
- Customer
- Commercial Snapshot
- Promotion Snapshot
- Payment
- Fulfillment

---

## Purchase Order (PO)

Purchase Order phát sinh khi YSim cần nhập Product Item từ Supplier.

PO là giao dịch giữa:

YSim

↓

Supplier

Purchase Order quản lý:

- Supplier Product
- Quantity
- Cost
- Supplier Agreement
- Supplier Wallet
- Credit
- Procurement

PO không sử dụng Payment Gateway bán lẻ.

Việc thanh toán tuân theo Supplier Agreement.

---

# 5. Procurement Validation

Checkout bắt buộc thực hiện Procurement Validation.

Quy trình:

```text
Inventory Available?

├── YES
│      │
│      ▼
│ Reserve Inventory
│
└── NO
       │
       ▼
Supplier Product Available?
       │
Supplier API Available?
       │
Supplier Payment Capacity?
       │
Purchase Order Feasible?
       │
       ▼
Checkout Allowed
```

Nếu Procurement Validation thất bại:

Checkout không được phép tạo Sales Order.

---

# 6. Procurement Capacity

Procurement Capacity xác định khả năng tạo Purchase Order.

Bao gồm:

- Supplier Availability
- Supplier Product Mapping
- Supplier API Availability
- Supplier Wallet Balance
- Supplier Credit Limit
- Supplier Agreement

Nếu Supplier yêu cầu thanh toán đặt cọc nhưng Wallet không đủ:

Purchase Order mặc định thất bại.

Checkout phải dừng trước Payment.

---

# 7. Cart

Cart thuộc Storefront.

Một Storefront chỉ có một Cart.

Một Cart không chứa:

- nhiều Storefront
- nhiều Organization

Cart có thời hạn mặc định:

24 giờ.

Guest Checkout được hỗ trợ.

Identity sẽ Merge sau nếu cần.

---

# 8. Checkout Session

Checkout Session là Transaction Object độc lập.

Checkout Session lưu:

- Cart
- Customer
- Currency
- Promotion
- Commercial Snapshot
- Price Reservation
- Inventory Reservation
- Procurement Validation

Checkout Snapshot được tạo khi Customer bắt đầu Checkout.

---

# 9. Sales Order Creation

Sales Order được tạo theo Model C.

```text
Cart

↓

Checkout

↓

Validation

↓

Sales Order

↓

Payment
```

Validation bao gồm:

- Product
- Catalog
- Price
- Promotion
- Inventory
- Procurement Capacity

---

# 10. Customer Information

Version 2.0 chỉ bắt buộc:

Primary Email.

Các thông tin khác đều Optional:

- Customer Name
- Phone Number
- Passport
- Billing Address
- Shipping Address

Primary Email luôn nhận:

- Payment Confirmation
- Invoice

Nếu không khai báo Recipient khác thì Primary Email cũng nhận toàn bộ QR Code.

---

# 11. Multi-Customer Order

Một Sales Order có thể phục vụ nhiều Customer.

Customer có thể khai báo:

- Recipient Email
- Recipient Phone
- Recipient Name

cho từng nhóm Item.

Ví dụ:

```text
Thailand 5GB/day ×2

↓

Recipient A
Recipient B
```

Nếu số Recipient ít hơn số lượng Item:

các Item còn lại gửi về Primary Email.

---

# 12. Fulfillment Assignment

Fulfillment Assignment thuộc Fulfillment Domain.

Customer có thể:

- khai báo Recipient ngay khi Checkout
- hoặc bổ sung sau Payment Success

Fulfillment Assignment quản lý:

- Recipient
- Product Item
- QR Recipient

---

# 13. Inventory Reservation

Nếu Inventory có đủ Item.

Khi Customer bắt đầu Payment:

Item phải được Reserve.

Reservation Time:

10 phút.

```text
Available

↓

Reserved

↓

Payment Success

↓

Allocated
```

Nếu Payment thất bại:

```text
Reserved

↓

Released

↓

Available
```

---

# 14. Purchase Order Trigger

Checkout không tạo Purchase Order.

Checkout chỉ xác nhận:

Purchase Order Feasible.

Sau Payment Success:

```text
Payment Success

↓

Revalidate Supplier

↓

Create Purchase Order

↓

Receive Product Item

↓

Inventory

↓

Allocation

↓

Fulfillment
```

Email Payment Success chỉ bao gồm:

- Payment Confirmation
- Invoice

Email Fulfillment được gửi riêng sau khi hoàn tất Allocation và Fulfillment.

---

# 15. Purchase Order Policy

Purchase Order tự động:

- chỉ mua đúng số lượng còn thiếu
- chỉ mua đúng Product cần thiết

Nếu Inventory đã có Item phù hợp:

Inventory sẽ được Reserve trước.

Supplier Policy có thể cấu hình:

- Minimum Purchase Quantity

Mặc định:

Không áp dụng.

Bulk Procurement được xử lý ngoài luồng Sales Order.

---

# 16. Purchase Order Relationship

Một Sales Order có thể phát sinh nhiều Purchase Order.

Purchase Order tự động luôn tham chiếu Sales Order.

Purchase Order nhập kho chủ động không tham chiếu Sales Order.

Một Product Item chỉ Allocation cho một Sales Order Item.

Nếu:

- Fulfillment thất bại
- Customer Return
- Activation thất bại

Item sẽ chuyển sang:

Revoked Inventory.

---

# 17. Purchase Order Failure

Sau Payment Success nếu Purchase Order thất bại:

Allocation Engine:

- thử Supplier khác
- Retry Procurement

Nếu vẫn thất bại:

- Pause Fulfillment
- Notify Customer
- Retry theo chính sách
- Full Refund nếu cần

Version 2.0 không hỗ trợ Customer tự chọn Product thay thế.

---

# 18. Order Status

Order Status chỉ quản lý Transaction thương mại.

```text
Draft

↓

Checkout

↓

Pending Payment

↓

Payment Success

↓

Payment Failed

↓

Cancelled
```

Các trạng thái:

- Fulfillment
- Assignment
- Delivery

được quản lý riêng trong Fulfillment Domain.

---

# 19. Customer Checkout Decision

Customer Checkout Decision là Business Object.

Bao gồm:

- Accept New Price
- Continue Checkout
- Cancel Checkout

Customer Decision được Snapshot cùng Checkout.

---

# 20. Order Ownership

Order luôn thuộc:

Payment Owner.

Order vẫn lưu Attribution:

- Organization
- Storefront
- Tracking
- Campaign
- Sales User
- Distribution Path

---

# 21. Order Number

Order Number được sinh theo Payment Owner.

Ví dụ:

```text
ABC-20260710-000123
```

Ngoài ra hệ thống sinh:

Global Order ID

để phục vụ:

- Traceability
- Parent Support
- Customer Support
- Correlation giữa SO, PO, Payment và Fulfillment

---

# 22. Order Modification

Sau Payment Success.

Không cho phép sửa:

- Product
- Quantity
- Currency
- Promotion
- Price

Chỉ cho phép thay đổi:

- Recipient
- Recipient Email
- Phone
- IM
- Fulfillment Assignment

Mọi thay đổi đều phải Audit.

---

# 23. Deferred Scope

Version sau sẽ bổ sung:

- Cart Recovery
- Product Replacement Suggestion
- Split Payment
- Multiple Payment
- Smart Procurement
- AI Procurement
- Bulk Procurement Recommendation

---

# 24. Business Decisions (Locked)

## BD-07-001

Transaction Domain được chia thành:

Cart → Checkout → Payment → Fulfillment → Settlement → After Sales.

---

## BD-07-002

YSim hỗ trợ hai loại Order:

Sales Order và Purchase Order.

---

## BD-07-003

Checkout bắt buộc thực hiện Procurement Validation.

---

## BD-07-004

Procurement Capacity là điều kiện bắt buộc trước Payment.

---

## BD-07-005

Sales Order được tạo theo Model C.

---

## BD-07-006

Cart thuộc Storefront.

---

## BD-07-007

Một Cart không chứa nhiều Storefront hoặc nhiều Organization.

---

## BD-07-008

Checkout Session là Transaction Object.

---

## BD-07-009

Primary Email là thông tin bắt buộc duy nhất.

---

## BD-07-010

Fulfillment Assignment thuộc Fulfillment Domain.

---

## BD-07-011

Inventory phải Reserve trong thời gian Price Reservation.

---

## BD-07-012

Purchase Order tự động chỉ được tạo sau Payment Success.

---

## BD-07-013

Purchase Order chỉ mua đúng số lượng và chủng loại còn thiếu.

---

## BD-07-014

Một Sales Order có thể phát sinh nhiều Purchase Order.

---

## BD-07-015

Một Product Item chỉ Allocation cho một Sales Order Item.

---

## BD-07-016

Purchase Order thất bại phải Retry hoặc Refund.

---

## BD-07-017

Order thuộc Payment Owner.

---

## BD-07-018

Order Number theo Payment Owner và có Global Order ID.

---

## BD-07-019

Sau Payment Success không được sửa Product, Quantity, Price hoặc Promotion.

---

# 25. Enterprise Design Principles

## EP-07-001

Sales Order và Purchase Order là hai Business Object độc lập.

---

## EP-07-002

Checkout chỉ xác nhận khả năng Procurement, không thực hiện Procurement.

---

## EP-07-003

Inventory Reservation phải đồng bộ với Price Reservation.

---

## EP-07-004

Fulfillment Assignment là Capability của Fulfillment Domain.

---

## EP-07-005

Mọi Product Item phải truy vết được:

Purchase Order

↓

Inventory

↓

Allocation

↓

Sales Order

↓

Customer

---

## EP-07-006

Transaction Domain chỉ tham chiếu Master Object và Commercial Object thông qua Snapshot.

---

# 26. Traceability

Workshop này kế thừa:

- BRD-WS-01
- BRD-WS-02
- BRD-WS-03
- BRD-WS-04
- BRD-WS-05
- BRD-WS-06

---

# 27. Impacts to Other Domains

Workshop này ảnh hưởng tới:

- Payment Engine
- Procurement Engine
- Inventory Domain
- Allocation Engine
- Fulfillment Engine
- Settlement Engine
- Customer Portal
- Customer Support
- Reporting
- API
- DMS
- DBD

---

# 28. Workshop Status

**Status:** FROZEN

Workshop này là Foundation cho:

- Payment Engine
- Procurement Engine
- Allocation Engine
- Fulfillment Engine
- Settlement Engine

---

# 29. Next Workshop

**BRD-WS-08 – Payment, Payment Gateway & Payment Lifecycle**

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-001 — Transaction Domain được chia thành: Cart → Checkout → Payment → Fulfillment → Settlement → After…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-001-AC001",
      "given": "the applicable business context, actor, and input for Transaction Domain được chia thành: Cart → Checkout → Payment → Fulfillment → Settlement → After…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Transaction Domain được chia thành: Cart → Checkout → Payment → Fulfillment → Settlement → After…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-001-O001"
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
        "BD-07-001-AC001",
        "BD-07-001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-001-O001",
      "obligation_text": "Transaction Domain được chia thành: Cart → Checkout → Payment → Fulfillment → Settlement → After Sales"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-07-001 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-07-001 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-07-001 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-07-001 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-07-001-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-07-001 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Transaction Domain được chia thành: Cart → Checkout → Payment → Fulfillment → Settlement → After Sales.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-001",
    "source_context_sha256": "f55c126003d54a46c1908072a1ebd8456945bcea7a3397190657e3625817e435",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "bad29219c6024dd00704eab59635d06e14d59c04295a70a92b3a1a676fbf1833",
    "source_lines": "L634-L639",
    "source_section": "24. Business Decisions (Locked) > BD-07-001"
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
  "stable_id": "BD-07-001",
  "title": "Transaction Domain được chia thành: Cart → Checkout → Payment → Fulfillment → Settlement → After…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-002 — YSim hỗ trợ hai loại Order: Sales Order và Purchase Order

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-002-AC001",
      "given": "the applicable business context, actor, and input for YSim hỗ trợ hai loại Order: Sales Order và Purchase Order",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-002-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by YSim hỗ trợ hai loại Order: Sales Order và Purchase Order",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-002-O001"
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
        "BD-07-002-AC001",
        "BD-07-002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-002-O001",
      "obligation_text": "YSim hỗ trợ hai loại Order: Sales Order và Purchase Order"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "YSim hỗ trợ hai loại Order: Sales Order và Purchase Order.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-002",
    "source_context_sha256": "f57aa293dc490be17c8e6d709ee8978e1dcbe167d3c8a88587268ae5c8fd9e73",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "ea3ae7f2aff7d53de77d6b01387fed0697e233cb94a55e20a7022645768ce46f",
    "source_lines": "L642-L647",
    "source_section": "24. Business Decisions (Locked) > BD-07-002"
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
  "stable_id": "BD-07-002",
  "title": "YSim hỗ trợ hai loại Order: Sales Order và Purchase Order",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-003 — Checkout bắt buộc thực hiện Procurement Validation

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-003-AC001",
      "given": "the applicable business context, actor, and input for Checkout bắt buộc thực hiện Procurement Validation",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Checkout bắt buộc thực hiện Procurement Validation",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-003-O001"
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
        "BD-07-003-AC001",
        "BD-07-003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-003-O001",
      "obligation_text": "Checkout bắt buộc thực hiện Procurement Validation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-07-003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-07-003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-07-003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-07-003 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-07-003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-07-003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Checkout bắt buộc thực hiện Procurement Validation.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Procurement Validation",
    "source_context_sha256": "09c4c12b18c53c171fc8599edfe49f3d037b8d9d3d2ed38dd6fa1aea530c77d4",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "893ef81b01d63886d3cc318c84f5749c23ae018fafdec22eebb7ec97d817a5ba",
    "source_lines": "L650-L653",
    "source_section": "24. Business Decisions (Locked) > BD-07-003"
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
  "stable_id": "BD-07-003",
  "title": "Checkout bắt buộc thực hiện Procurement Validation",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-004 — Procurement Capacity là điều kiện bắt buộc trước Payment

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-004-AC001",
      "given": "the applicable business context, actor, and input for Procurement Capacity là điều kiện bắt buộc trước Payment",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Procurement Capacity là điều kiện bắt buộc trước Payment",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-004-O001"
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
        "BD-07-004-AC001",
        "BD-07-004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-004-O001",
      "obligation_text": "Procurement Capacity là điều kiện bắt buộc trước Payment"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-07-004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-07-004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-07-004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-07-004 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-07-004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-07-004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Procurement Capacity là điều kiện bắt buộc trước Payment.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-004",
    "source_context_sha256": "42031d70708f17ac2f3044a3956da0f5cb43373d4d08a5806411eb6ca1d8f32c",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "fe9a8a17433e5aac1092bf240b4eb143d842829f4df3caed433455ccda8431fb",
    "source_lines": "L656-L659",
    "source_section": "24. Business Decisions (Locked) > BD-07-004"
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
  "stable_id": "BD-07-004",
  "title": "Procurement Capacity là điều kiện bắt buộc trước Payment",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-005 — Sales Order được tạo theo Model C

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-005-AC001",
      "given": "the applicable business context, actor, and input for Sales Order được tạo theo Model C",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-005-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Sales Order được tạo theo Model C",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-005-O001"
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
        "BD-07-005-AC001",
        "BD-07-005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-005-O001",
      "obligation_text": "Sales Order được tạo theo Model C"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sales Order được tạo theo Model C.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Sales Order Creation",
    "source_context_sha256": "624524de6957658198a8cceb53f2481b15e4ecf33adebe8bd487aa6a8fef894a",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "030bc7dc6ba90362ed1b042fdfbcd2140fb00153663a48b3bcc1cc101d3a0558",
    "source_lines": "L662-L665",
    "source_section": "24. Business Decisions (Locked) > BD-07-005"
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
  "stable_id": "BD-07-005",
  "title": "Sales Order được tạo theo Model C",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-006 — Cart thuộc Storefront

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-006-AC001",
      "given": "the applicable business context, actor, and input for Cart thuộc Storefront",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Cart thuộc Storefront",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-006-O001"
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
        "BD-07-006-AC001",
        "BD-07-006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-006-O001",
      "obligation_text": "Cart thuộc Storefront"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Cart thuộc Storefront.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Cart",
    "source_context_sha256": "2a151fb191691fafb4e40db77d2d6f250971c287d9e8919cf434118d7c4a60f4",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "76ae1072f806d5789d4f1a71fee7fa495c9b0e7582431066a47e7199732d56d0",
    "source_lines": "L668-L671",
    "source_section": "24. Business Decisions (Locked) > BD-07-006"
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
  "stable_id": "BD-07-006",
  "title": "Cart thuộc Storefront",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-007 — Một Cart không chứa nhiều Storefront hoặc nhiều Organization

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-007-AC001",
      "given": "the applicable business context, actor, and input for Một Cart không chứa nhiều Storefront hoặc nhiều Organization",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-007-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Một Cart không chứa nhiều Storefront hoặc nhiều Organization",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-007-O001"
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
        "BD-07-007-AC001",
        "BD-07-007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-007-O001",
      "obligation_text": "Một Cart không chứa nhiều Storefront hoặc nhiều Organization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một Cart không chứa nhiều Storefront hoặc nhiều Organization.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-007",
    "source_context_sha256": "641b50baca17f20a8ba90584976733d544da7163dd06423ead58544fbbd55886",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
    "source_lines": "L674-L677",
    "source_section": "24. Business Decisions (Locked) > BD-07-007"
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
  "stable_id": "BD-07-007",
  "title": "Một Cart không chứa nhiều Storefront hoặc nhiều Organization",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-008 — Checkout Session là Transaction Object

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-008-AC001",
      "given": "the applicable business context, actor, and input for Checkout Session là Transaction Object",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-008-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-008-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Checkout Session là Transaction Object",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-008-O001"
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
        "BD-07-008-AC001",
        "BD-07-008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-008-O001",
      "obligation_text": "Checkout Session là Transaction Object"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-07-008 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-07-008 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-07-008 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-07-008 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-07-008-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-07-008 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Checkout Session là Transaction Object.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-008",
    "source_context_sha256": "9073362e8b562486591e323893b814c9ba69f0f5a9d9bf3cd6b7cf6175daab40",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "93df9b4d971b8fbfe36429506cb67e8044fe274e07b9a457b7f470a396417481",
    "source_lines": "L680-L683",
    "source_section": "24. Business Decisions (Locked) > BD-07-008"
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
  "stable_id": "BD-07-008",
  "title": "Checkout Session là Transaction Object",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-009 — Primary Email là thông tin bắt buộc duy nhất

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-009-AC001",
      "given": "the applicable business context, actor, and input for Primary Email là thông tin bắt buộc duy nhất",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-009-O001"
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
        "BD-07-009-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-009-O001",
      "obligation_text": "Primary Email là thông tin bắt buộc duy nhất"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Primary Email là thông tin bắt buộc duy nhất.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-009",
    "source_context_sha256": "6a3390d9c17001b62049679973aaa8dc641d3eb93cf24771854c34a18fa9c760",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "40967dcf52a3b45cf40e51e0b9e4d72d41d1954ece5d0ad5b04e0ff214c79701",
    "source_lines": "L686-L689",
    "source_section": "24. Business Decisions (Locked) > BD-07-009"
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
  "stable_id": "BD-07-009",
  "title": "Primary Email là thông tin bắt buộc duy nhất",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-010 — Fulfillment Assignment thuộc Fulfillment Domain

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-010-AC001",
      "given": "the applicable business context, actor, and input for Fulfillment Assignment thuộc Fulfillment Domain",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-010-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-010-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Fulfillment Assignment thuộc Fulfillment Domain",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-010-O001"
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
        "BD-07-010-AC001",
        "BD-07-010-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-010-O001",
      "obligation_text": "Fulfillment Assignment thuộc Fulfillment Domain"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-07-010 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-07-010 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-07-010 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-07-010 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-07-010-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-07-010 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Fulfillment Assignment thuộc Fulfillment Domain.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Fulfillment Assignment",
    "source_context_sha256": "b6744f15982bd28e9762c6bf762966254e5010984bb08088f1173cbe88b80053",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "5b1ce55f2d3d2204667eb1dc259e582fdbfe2582dcefd3508cebbbfdb5545c7b",
    "source_lines": "L692-L695",
    "source_section": "24. Business Decisions (Locked) > BD-07-010"
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
  "stable_id": "BD-07-010",
  "title": "Fulfillment Assignment thuộc Fulfillment Domain",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-011 — Inventory phải Reserve trong thời gian Price Reservation

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-011-AC001",
      "given": "the applicable business context, actor, and input for Inventory phải Reserve trong thời gian Price Reservation",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-011-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Inventory phải Reserve trong thời gian Price Reservation",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-011-O001"
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
        "BD-07-011-AC001",
        "BD-07-011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-011-O001",
      "obligation_text": "Inventory phải Reserve trong thời gian Price Reservation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-07-011 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-07-011 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-07-011 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-07-011 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-07-011-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-07-011 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Inventory phải Reserve trong thời gian Price Reservation.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-011",
    "source_context_sha256": "e8b3dfc40f5b4f3c5c08ff1287f36d0a5fa531bc48f29478c4e000b68c69b524",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "6a333cc0e4ef8f0fdaec0711cdec99c57e872d6e8eb30876c35bdecb9a8b3ff5",
    "source_lines": "L698-L701",
    "source_section": "24. Business Decisions (Locked) > BD-07-011"
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
  "stable_id": "BD-07-011",
  "title": "Inventory phải Reserve trong thời gian Price Reservation",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-012 — Purchase Order tự động chỉ được tạo sau Payment Success

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-012-AC001",
      "given": "the applicable business context, actor, and input for Purchase Order tự động chỉ được tạo sau Payment Success",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-012-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-012-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Purchase Order tự động chỉ được tạo sau Payment Success",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-012-O001"
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
        "BD-07-012-AC001",
        "BD-07-012-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-012-O001",
      "obligation_text": "Purchase Order tự động chỉ được tạo sau Payment Success"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-07-012 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-07-012 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-07-012 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-07-012 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-07-012-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-07-012 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Purchase Order tự động chỉ được tạo sau Payment Success.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-012",
    "source_context_sha256": "186d8cfc286f0ca9174a147e67f07e845c03df1cc4a910a0974f71fb622075e5",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "deadb67b2a0e6e0ca75cfa40f2fe02df7006e9d26aa168e1fb0a619b4124cbd1",
    "source_lines": "L704-L707",
    "source_section": "24. Business Decisions (Locked) > BD-07-012"
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
  "stable_id": "BD-07-012",
  "title": "Purchase Order tự động chỉ được tạo sau Payment Success",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-013 — Purchase Order chỉ mua đúng số lượng và chủng loại còn thiếu

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-013-AC001",
      "given": "the applicable business context, actor, and input for Purchase Order chỉ mua đúng số lượng và chủng loại còn thiếu",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-013-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-013-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Purchase Order chỉ mua đúng số lượng và chủng loại còn thiếu",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-013-O001"
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
        "BD-07-013-AC001",
        "BD-07-013-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-013-O001",
      "obligation_text": "Purchase Order chỉ mua đúng số lượng và chủng loại còn thiếu"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Purchase Order chỉ mua đúng số lượng và chủng loại còn thiếu.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-013",
    "source_context_sha256": "6f2e785196aa5d64ddc0de5a684d47ca3b1515cee843311238a53c8ff8c7adcc",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "afc7a38ca5bf3827f76f10d87c4934404b98a9e73fbeaa664b05c8316d4dc423",
    "source_lines": "L710-L713",
    "source_section": "24. Business Decisions (Locked) > BD-07-013"
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
  "stable_id": "BD-07-013",
  "title": "Purchase Order chỉ mua đúng số lượng và chủng loại còn thiếu",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-014 — Một Sales Order có thể phát sinh nhiều Purchase Order

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-014-AC001",
      "given": "the applicable business context, actor, and input for Một Sales Order có thể phát sinh nhiều Purchase Order",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-014-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-014-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Một Sales Order có thể phát sinh nhiều Purchase Order",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-014-O001"
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
        "BD-07-014-AC001",
        "BD-07-014-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-014-O001",
      "obligation_text": "Một Sales Order có thể phát sinh nhiều Purchase Order"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một Sales Order có thể phát sinh nhiều Purchase Order.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-014",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Purchase Order Relationship",
    "source_context_sha256": "377ba4c9e2d7228a57bd381962536a997d53127ff0180913ea416eff141893e5",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "aea9df2dade06f29ff5b944ceb1de81ea0aba23b799624f884f51d436986df5a",
    "source_lines": "L716-L719",
    "source_section": "24. Business Decisions (Locked) > BD-07-014"
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
  "stable_id": "BD-07-014",
  "title": "Một Sales Order có thể phát sinh nhiều Purchase Order",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-015 — Một Product Item chỉ Allocation cho một Sales Order Item

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-015-AC001",
      "given": "the applicable business context, actor, and input for Một Product Item chỉ Allocation cho một Sales Order Item",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-015-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-015-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Một Product Item chỉ Allocation cho một Sales Order Item",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-015-O001"
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
        "BD-07-015-AC001",
        "BD-07-015-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-015-O001",
      "obligation_text": "Một Product Item chỉ Allocation cho một Sales Order Item"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-07-015 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-07-015 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-07-015 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-07-015 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-07-015-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-07-015 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một Product Item chỉ Allocation cho một Sales Order Item.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-015",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Purchase Order Relationship",
    "source_context_sha256": "377ba4c9e2d7228a57bd381962536a997d53127ff0180913ea416eff141893e5",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "ccdb341e2a7a60f9ca828ffc873a12943174d82a4a45f4f970d0a60b97992fd6",
    "source_lines": "L722-L725",
    "source_section": "24. Business Decisions (Locked) > BD-07-015"
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
  "stable_id": "BD-07-015",
  "title": "Một Product Item chỉ Allocation cho một Sales Order Item",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-016 — Purchase Order thất bại phải Retry hoặc Refund

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-016-AC001",
      "given": "the applicable business context, actor, and input for Purchase Order thất bại phải Retry hoặc Refund",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-016-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-016-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Purchase Order thất bại phải Retry hoặc Refund",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-016-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "IDEMPOTENCY",
      "controlled_contract": "EXPLICIT_IDEMPOTENCY_CONTRACT_V1",
      "criterion_id": "BD-07-016-AC003",
      "given": "a repeated request, retry, replay, or duplicate explicitly governed by Purchase Order thất bại phải Retry hoặc Refund",
      "observable_evidence": "original and repeated action identities, both outcomes, side-effect count, and resulting business state",
      "then": "the repeated action produces the requirement-specific stable result without an additional prohibited side effect",
      "verifies": [
        "BD-07-016-O001"
      ],
      "when": "the same governed action is presented again under the declared identity or deduplication boundary"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-07-016-AC001",
        "BD-07-016-AC002",
        "BD-07-016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-016-O001",
      "obligation_text": "Purchase Order thất bại phải Retry hoặc Refund"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-07-016 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-07-016 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [
        "BD-07-016-AC003"
      ],
      "status": "APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-07-016 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-07-016-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-07-016 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Purchase Order thất bại phải Retry hoặc Refund.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-016",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-016",
    "source_context_sha256": "9b6445cc64f07e51e624c5ae68dd08a37cf04bc15311452afbebe06d369de504",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "0eda26423f061eb661f76f4a4d9bd30cfa9f442065c15b1855bc91d126aa43ee",
    "source_lines": "L728-L731",
    "source_section": "24. Business Decisions (Locked) > BD-07-016"
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
  "stable_id": "BD-07-016",
  "title": "Purchase Order thất bại phải Retry hoặc Refund",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-017 — Order thuộc Payment Owner

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-017-AC001",
      "given": "the applicable business context, actor, and input for Order thuộc Payment Owner",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-017-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-017-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Order thuộc Payment Owner",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-017-O001"
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
        "BD-07-017-AC001",
        "BD-07-017-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-017-O001",
      "obligation_text": "Order thuộc Payment Owner"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-07-017 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-07-017 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-07-017 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-07-017 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-07-017-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-07-017 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Order thuộc Payment Owner.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-017",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-017",
    "source_context_sha256": "2963e59c01909323da4f306a54f027b70c0f8a7d949a0ef91af6697375134422",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "f3d64cee0bef7607fb1292ff4f2a239106018bb53198bff1e4977a03b35388d7",
    "source_lines": "L734-L737",
    "source_section": "24. Business Decisions (Locked) > BD-07-017"
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
  "stable_id": "BD-07-017",
  "title": "Order thuộc Payment Owner",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-018 — Order Number theo Payment Owner và có Global Order ID

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-018-AC001",
      "given": "the applicable business context, actor, and input for Order Number theo Payment Owner và có Global Order ID",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-07-018-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-018-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Order Number theo Payment Owner và có Global Order ID",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-018-O001"
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
        "BD-07-018-AC001",
        "BD-07-018-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-018-O001",
      "obligation_text": "Order Number theo Payment Owner và có Global Order ID"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-07-018 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-07-018 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-07-018 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-07-018 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-07-018-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-07-018 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Order Number theo Payment Owner và có Global Order ID.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-018",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-018",
    "source_context_sha256": "f7a1d74628316c68b965e40e20ab56945b52d32b76608251bb5348c282ed47d2",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "1b3809c9f634286223157540c96dec66991cb65882686d79d154a40a370959dc",
    "source_lines": "L740-L743",
    "source_section": "24. Business Decisions (Locked) > BD-07-018"
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
  "stable_id": "BD-07-018",
  "title": "Order Number theo Payment Owner và có Global Order ID",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-019 — Sau Payment Success không được sửa Product, Quantity, Price hoặc Promotion

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-07-019-AC001",
      "given": "the applicable business context, actor, and input for Sau Payment Success không được sửa Product, Quantity, Price hoặc Promotion",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BD-07-019-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-07-019-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Sau Payment Success không được sửa Product, Quantity, Price hoặc Promotion",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-07-019-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-07-019-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Sau Payment Success không được sửa Product, Quantity, Price hoặc Promotion",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-07-019-O001"
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
        "BD-07-019-AC001",
        "BD-07-019-AC002",
        "BD-07-019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-019-O001",
      "obligation_text": "Sau Payment Success không được sửa Product, Quantity, Price hoặc Promotion"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-07-019 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-07-019 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-07-019 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-07-019-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-07-019-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-07-019 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sau Payment Success không được sửa Product, Quantity, Price hoặc Promotion.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-019",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-019",
    "source_context_sha256": "79fc47e444f6e6689180d34eb1db9c51a3cb3fccf574d75dbc8284bd86c806c5",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "eed5724a1368231b18290ed8bca02d543a5ccc3f4ffd2639fee34edd1ed9fcf3",
    "source_lines": "L746-L749",
    "source_section": "24. Business Decisions (Locked) > BD-07-019"
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
  "stable_id": "BD-07-019",
  "title": "Sau Payment Success không được sửa Product, Quantity, Price hoặc Promotion",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R001 — Purchase Order phát sinh khi YSim cần nhập Product Item từ Supplier

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R001-AC001",
      "given": "the applicable business context, actor, and input for Purchase Order phát sinh khi YSim cần nhập Product Item từ Supplier",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Purchase Order phát sinh khi YSim cần nhập Product Item từ Supplier",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R001-O001"
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
        "BRD-WS-07-R001-AC001",
        "BRD-WS-07-R001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R001-O001",
      "obligation_text": "Purchase Order phát sinh khi YSim cần nhập Product Item từ Supplier"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R001 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R001 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R001 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R001 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-07-R001-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R001 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Purchase Order phát sinh khi YSim cần nhập Product Item từ Supplier.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-001",
    "previous_temporary_key": "TMP-BRD-WS-07-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "Purchase Order (PO)",
    "source_context_sha256": "8ba73bf3d27037bd42689497e98ff67a2b9470c09a4a610cb51ef2aeeaefe7fc",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "4ae91cbfa4c2c8ebb02387696a7ef83a2cd450667aa188ce91acb9a8d04465bd",
    "source_lines": "L120",
    "source_section": "4. Order Taxonomy > Purchase Order (PO)"
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
  "stable_id": "BRD-WS-07-R001",
  "title": "Purchase Order phát sinh khi YSim cần nhập Product Item từ Supplier",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R003 — Nếu Procurement Validation thất bại: Checkout không được phép tạo Sales Order

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R003-AC001",
      "given": "the applicable business context, actor, and input for Nếu Procurement Validation thất bại: Checkout không được phép tạo Sales Order",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-07-R003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Nếu Procurement Validation thất bại: Checkout không được phép tạo Sales Order",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R003-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-07-R003-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Nếu Procurement Validation thất bại: Checkout không được phép tạo Sales Order",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-07-R003-O001"
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
        "BRD-WS-07-R003-AC001",
        "BRD-WS-07-R003-AC002",
        "BRD-WS-07-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R003-O001",
      "obligation_text": "Nếu Procurement Validation thất bại: Checkout không được phép tạo Sales Order"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-07-R003-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-07-R003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu Procurement Validation thất bại: Checkout không được phép tạo Sales Order.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-003",
    "previous_temporary_key": "TMP-BRD-WS-07-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Procurement Validation",
    "source_context_sha256": "09c4c12b18c53c171fc8599edfe49f3d037b8d9d3d2ed38dd6fa1aea530c77d4",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "ebe4171ef9805a1be78ae846d995d6fd9973155be793be9b8ece74183a8490a6",
    "source_lines": "L175-L177",
    "source_section": "5. Procurement Validation"
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
  "stable_id": "BRD-WS-07-R003",
  "title": "Nếu Procurement Validation thất bại: Checkout không được phép tạo Sales Order",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R004 — Checkout phải dừng trước Payment

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R004-AC001",
      "given": "the applicable business context, actor, and input for Checkout phải dừng trước Payment",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Checkout phải dừng trước Payment",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R004-O001"
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
        "BRD-WS-07-R004-AC001",
        "BRD-WS-07-R004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R004-O001",
      "obligation_text": "Checkout phải dừng trước Payment"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R004 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-07-R004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Checkout phải dừng trước Payment.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-004",
    "previous_temporary_key": "TMP-BRD-WS-07-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Procurement Capacity",
    "source_context_sha256": "3d367e8860d74f1845736db291a02eb92c963f21a84005208567253d9048adca",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "815f09d2cfcb8171193d305d65651ad4ac51cf1d9f1f06b6babc7d2063146195",
    "source_lines": "L198",
    "source_section": "6. Procurement Capacity"
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
  "stable_id": "BRD-WS-07-R004",
  "title": "Checkout phải dừng trước Payment",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R005 — Identity sẽ Merge sau nếu cần

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R005-AC001",
      "given": "the applicable business context, actor, and input for Identity sẽ Merge sau nếu cần",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R005-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Identity sẽ Merge sau nếu cần",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R005-O001"
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
        "BRD-WS-07-R005-AC001",
        "BRD-WS-07-R005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R005-O001",
      "obligation_text": "Identity sẽ Merge sau nếu cần"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R005 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-07-R005-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Identity sẽ Merge sau nếu cần.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-005",
    "previous_temporary_key": "TMP-BRD-WS-07-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Cart",
    "source_context_sha256": "2a151fb191691fafb4e40db77d2d6f250971c287d9e8919cf434118d7c4a60f4",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
    "source_lines": "L219",
    "source_section": "7. Cart"
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
  "stable_id": "BRD-WS-07-R005",
  "title": "Identity sẽ Merge sau nếu cần",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R006 — Version 2.0 chỉ bắt buộc: Primary Email

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R006-AC001",
      "given": "the applicable business context, actor, and input for Version 2.0 chỉ bắt buộc: Primary Email",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Version 2.0 chỉ bắt buộc: Primary Email",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R006-O001"
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
        "BRD-WS-07-R006-AC001",
        "BRD-WS-07-R006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R006-O001",
      "obligation_text": "Version 2.0 chỉ bắt buộc: Primary Email"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Version 2.0 chỉ bắt buộc: Primary Email.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-006",
    "previous_temporary_key": "TMP-BRD-WS-07-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Customer Information",
    "source_context_sha256": "4e9815b138059f521584e985c83bbb92efb08decc438b45224a4ce2d37d75d23",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
    "source_lines": "L279-L281",
    "source_section": "10. Customer Information"
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
  "stable_id": "BRD-WS-07-R006",
  "title": "Version 2.0 chỉ bắt buộc: Primary Email",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R007 — Primary Email luôn nhận: - Payment Confirmation

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R007-AC001",
      "given": "the applicable business context, actor, and input for Primary Email luôn nhận: - Payment Confirmation",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R007-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Primary Email luôn nhận: - Payment Confirmation",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R007-O001"
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
        "BRD-WS-07-R007-AC001",
        "BRD-WS-07-R007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R007-O001",
      "obligation_text": "Primary Email luôn nhận: - Payment Confirmation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R007 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R007 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R007 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R007 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-07-R007-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R007 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Primary Email luôn nhận: - Payment Confirmation",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-007",
    "previous_temporary_key": "TMP-BRD-WS-07-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Customer Information",
    "source_context_sha256": "4e9815b138059f521584e985c83bbb92efb08decc438b45224a4ce2d37d75d23",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
    "source_lines": "L291-L293",
    "source_section": "10. Customer Information"
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
  "stable_id": "BRD-WS-07-R007",
  "title": "Primary Email luôn nhận: - Payment Confirmation",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R008 — Primary Email luôn nhận: - Invoice

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R008-AC001",
      "given": "the applicable business context, actor, and input for Primary Email luôn nhận: - Invoice",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R008-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R008-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Primary Email luôn nhận: - Invoice",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R008-O001"
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
        "BRD-WS-07-R008-AC001",
        "BRD-WS-07-R008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R008-O001",
      "obligation_text": "Primary Email luôn nhận: - Invoice"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Primary Email luôn nhận: - Invoice",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-008",
    "previous_temporary_key": "TMP-BRD-WS-07-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Customer Information",
    "source_context_sha256": "4e9815b138059f521584e985c83bbb92efb08decc438b45224a4ce2d37d75d23",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "a33e4af3eb3ae9cf508bc2c494867fbce0a55d454b44f3f236fd84cc66b46ea3",
    "source_lines": "L291-L294",
    "source_section": "10. Customer Information"
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
  "stable_id": "BRD-WS-07-R008",
  "title": "Primary Email luôn nhận: - Invoice",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R009 — Khi Customer bắt đầu Payment: Item phải được Reserve

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R009-AC001",
      "given": "the applicable business context, actor, and input for Khi Customer bắt đầu Payment: Item phải được Reserve",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R009-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R009-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Khi Customer bắt đầu Payment: Item phải được Reserve",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R009-O001"
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
        "BRD-WS-07-R009-AC001",
        "BRD-WS-07-R009-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R009-O001",
      "obligation_text": "Khi Customer bắt đầu Payment: Item phải được Reserve"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R009 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R009 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R009 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R009 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-07-R009-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R009 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Khi Customer bắt đầu Payment: Item phải được Reserve.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-009",
    "previous_temporary_key": "TMP-BRD-WS-07-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Inventory Reservation",
    "source_context_sha256": "bbb1bb9024c71508d6f6ac64841cde2691f20ddb7eac32d7202f0f280def7483",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
    "source_lines": "L350-L352",
    "source_section": "13. Inventory Reservation"
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
  "stable_id": "BRD-WS-07-R009",
  "title": "Khi Customer bắt đầu Payment: Item phải được Reserve",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R010 — Purchase Order tự động: - chỉ mua đúng số lượng còn thiếu - chỉ mua đúng Product cần thiết

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R010-AC001",
      "given": "the applicable business context, actor, and input for Purchase Order tự động: - chỉ mua đúng số lượng còn thiếu - chỉ mua đúng Product cần thiết",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R010-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R010-AC002",
      "given": "the applicable business context, actor, and input for Purchase Order tự động: - chỉ mua đúng số lượng còn thiếu - chỉ mua đúng Product cần thiết",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R010-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R010-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Purchase Order tự động: - chỉ mua đúng số lượng còn thiếu - chỉ mua đúng Product cần thiết",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R010-O001",
        "BRD-WS-07-R010-O002"
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
        "BRD-WS-07-R010-AC001",
        "BRD-WS-07-R010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R010-O001",
      "obligation_text": "Purchase Order tự động: chỉ mua đúng số lượng còn thiếu."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-07-R010-AC002",
        "BRD-WS-07-R010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R010-O002",
      "obligation_text": "Purchase Order tự động: chỉ mua đúng Product cần thiết."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Purchase Order tự động: - chỉ mua đúng số lượng còn thiếu - chỉ mua đúng Product cần thiết",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-010",
    "previous_temporary_key": "TMP-BRD-WS-07-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Purchase Order Policy",
    "source_context_sha256": "673e9ed2ed14ab642327d405c52df29ffef681ab912c9264a65ff4e2ac90d7dc",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
    "source_lines": "L439-L442",
    "source_section": "15. Purchase Order Policy"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_RULE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-07-R010",
  "title": "Purchase Order tự động: - chỉ mua đúng số lượng còn thiếu - chỉ mua đúng Product cần thiết",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R011 — Purchase Order tự động luôn tham chiếu Sales Order

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R011-AC001",
      "given": "the applicable business context, actor, and input for Purchase Order tự động luôn tham chiếu Sales Order",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R011-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Purchase Order tự động luôn tham chiếu Sales Order",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R011-O001"
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
        "BRD-WS-07-R011-AC001",
        "BRD-WS-07-R011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R011-O001",
      "obligation_text": "Purchase Order tự động luôn tham chiếu Sales Order"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Purchase Order tự động luôn tham chiếu Sales Order.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-011",
    "previous_temporary_key": "TMP-BRD-WS-07-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Purchase Order Relationship",
    "source_context_sha256": "377ba4c9e2d7228a57bd381962536a997d53127ff0180913ea416eff141893e5",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "3d7ba11d8feee75d0a0c0c15aaaf636e619717c2ca75c1cf8644c9edbc15dbbb",
    "source_lines": "L464",
    "source_section": "16. Purchase Order Relationship"
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
  "stable_id": "BRD-WS-07-R011",
  "title": "Purchase Order tự động luôn tham chiếu Sales Order",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R012 — Nếu vẫn thất bại: - Pause Fulfillment - Notify Customer - Retry theo chính sách - Full Refund nế…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R012-AC001",
      "given": "the applicable business context, actor, and input for Nếu vẫn thất bại: - Pause Fulfillment - Notify Customer - Retry theo chính sách - Full Refund nế…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R012-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R012-AC002",
      "given": "the applicable business context, actor, and input for Nếu vẫn thất bại: - Pause Fulfillment - Notify Customer - Retry theo chính sách - Full Refund nế…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R012-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R012-AC003",
      "given": "the applicable business context, actor, and input for Nếu vẫn thất bại: - Pause Fulfillment - Notify Customer - Retry theo chính sách - Full Refund nế…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R012-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R012-AC004",
      "given": "the applicable business context, actor, and input for Nếu vẫn thất bại: - Pause Fulfillment - Notify Customer - Retry theo chính sách - Full Refund nế…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R012-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R012-AC005",
      "given": "an unsupported or invalid business input at the boundary governed by Nếu vẫn thất bại: - Pause Fulfillment - Notify Customer - Retry theo chính sách - Full Refund nế…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R012-O001",
        "BRD-WS-07-R012-O002",
        "BRD-WS-07-R012-O003",
        "BRD-WS-07-R012-O004"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "IDEMPOTENCY",
      "controlled_contract": "EXPLICIT_IDEMPOTENCY_CONTRACT_V1",
      "criterion_id": "BRD-WS-07-R012-AC006",
      "given": "a repeated request, retry, replay, or duplicate explicitly governed by Nếu vẫn thất bại: - Pause Fulfillment - Notify Customer - Retry theo chính sách - Full Refund nế…",
      "observable_evidence": "original and repeated action identities, both outcomes, side-effect count, and resulting business state",
      "then": "the repeated action produces the requirement-specific stable result without an additional prohibited side effect",
      "verifies": [
        "BRD-WS-07-R012-O001",
        "BRD-WS-07-R012-O002",
        "BRD-WS-07-R012-O003",
        "BRD-WS-07-R012-O004"
      ],
      "when": "the same governed action is presented again under the declared identity or deduplication boundary"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-07-R012-AC001",
        "BRD-WS-07-R012-AC005",
        "BRD-WS-07-R012-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R012-O001",
      "obligation_text": "Nếu vẫn thất bại: Pause Fulfillment."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-07-R012-AC002",
        "BRD-WS-07-R012-AC005",
        "BRD-WS-07-R012-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R012-O002",
      "obligation_text": "Nếu vẫn thất bại: Notify Customer."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-07-R012-AC003",
        "BRD-WS-07-R012-AC005",
        "BRD-WS-07-R012-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R012-O003",
      "obligation_text": "Nếu vẫn thất bại: Retry theo chính sách."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-07-R012-AC004",
        "BRD-WS-07-R012-AC005",
        "BRD-WS-07-R012-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R012-O004",
      "obligation_text": "Nếu vẫn thất bại: Full Refund nếu cần."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R012 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R012 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [
        "BRD-WS-07-R012-AC006"
      ],
      "status": "APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R012 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-07-R012-AC001",
        "BRD-WS-07-R012-AC002",
        "BRD-WS-07-R012-AC003",
        "BRD-WS-07-R012-AC004"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R012 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu vẫn thất bại: - Pause Fulfillment - Notify Customer - Retry theo chính sách - Full Refund nếu cần",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-012",
    "previous_temporary_key": "TMP-BRD-WS-07-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Purchase Order Failure",
    "source_context_sha256": "722aeb6ff740623273c009b5eae31efeb0c9ca82e39bab1a0cb8cbec80ed1554",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "ef3281d3aaae09e4ee5fcdfdd8de1633076e64e4a5c0e308159b542884c07e50",
    "source_lines": "L491-L496",
    "source_section": "17. Purchase Order Failure"
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
  "stable_id": "BRD-WS-07-R012",
  "title": "Nếu vẫn thất bại: - Pause Fulfillment - Notify Customer - Retry theo chính sách - Full Refund nế…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R013 — Version 2.0 không hỗ trợ Customer tự chọn Product thay thế

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "EXCLUDED_FROM_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version 2.0 không hỗ trợ Customer tự chọn Product thay thế.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-013",
    "previous_temporary_key": "TMP-BRD-WS-07-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Purchase Order Failure",
    "source_context_sha256": "722aeb6ff740623273c009b5eae31efeb0c9ca82e39bab1a0cb8cbec80ed1554",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "6e5dc4e1d71f94740f0368cb0c96eeff53a3729e966ed220d5fc043134cafa41",
    "source_lines": "L498",
    "source_section": "17. Purchase Order Failure"
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
  "stable_id": "BRD-WS-07-R013",
  "title": "Version 2.0 không hỗ trợ Customer tự chọn Product thay thế",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R014 — Order luôn thuộc: Payment Owner

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R014-AC001",
      "given": "the applicable business context, actor, and input for Order luôn thuộc: Payment Owner",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R014-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R014-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Order luôn thuộc: Payment Owner",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R014-O001"
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
        "BRD-WS-07-R014-AC001",
        "BRD-WS-07-R014-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R014-O001",
      "obligation_text": "Order luôn thuộc: Payment Owner"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R014 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R014 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R014 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R014 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-07-R014-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R014 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Order luôn thuộc: Payment Owner.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-014",
    "previous_temporary_key": "TMP-BRD-WS-07-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Order Ownership",
    "source_context_sha256": "939e7e3f383f58df388dcd34c57f3cf691c5f84fd26da559d9ff391106fee0f1",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
    "source_lines": "L556-L558",
    "source_section": "20. Order Ownership"
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
  "stable_id": "BRD-WS-07-R014",
  "title": "Order luôn thuộc: Payment Owner",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R015 — Không cho phép sửa: - Product

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R015-AC001",
      "given": "the applicable business context, actor, and input for Không cho phép sửa: - Product",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R015-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R015-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Không cho phép sửa: - Product",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R015-O001"
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
        "BRD-WS-07-R015-AC001",
        "BRD-WS-07-R015-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R015-O001",
      "obligation_text": "Không cho phép sửa: - Product"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không cho phép sửa: - Product",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-015",
    "previous_temporary_key": "TMP-BRD-WS-07-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Order Modification",
    "source_context_sha256": "49b3e8f656c364bf08dada0a7ea8b50193274b34c461fcbd60a522cd7aca444b",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
    "source_lines": "L598-L600",
    "source_section": "22. Order Modification"
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
  "stable_id": "BRD-WS-07-R015",
  "title": "Không cho phép sửa: - Product",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R016 — Không cho phép sửa: - Quantity

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R016-AC001",
      "given": "the applicable business context, actor, and input for Không cho phép sửa: - Quantity",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R016-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R016-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Không cho phép sửa: - Quantity",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R016-O001"
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
        "BRD-WS-07-R016-AC001",
        "BRD-WS-07-R016-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R016-O001",
      "obligation_text": "Không cho phép sửa: - Quantity"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không cho phép sửa: - Quantity",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-016",
    "previous_temporary_key": "TMP-BRD-WS-07-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Order Modification",
    "source_context_sha256": "49b3e8f656c364bf08dada0a7ea8b50193274b34c461fcbd60a522cd7aca444b",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "df774e383daeaca33ecd53d4f1af89fdf10b7706c8a7c6be30031544c3051ce0",
    "source_lines": "L598-L601",
    "source_section": "22. Order Modification"
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
  "stable_id": "BRD-WS-07-R016",
  "title": "Không cho phép sửa: - Quantity",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R017 — Không cho phép sửa: - Currency

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R017-AC001",
      "given": "the applicable business context, actor, and input for Không cho phép sửa: - Currency",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R017-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R017-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Không cho phép sửa: - Currency",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R017-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-07-R017-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Không cho phép sửa: - Currency",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-07-R017-O001"
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
        "BRD-WS-07-R017-AC001",
        "BRD-WS-07-R017-AC002",
        "BRD-WS-07-R017-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R017-O001",
      "obligation_text": "Không cho phép sửa: - Currency"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R017 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R017 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R017 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-07-R017-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-07-R017-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R017 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không cho phép sửa: - Currency",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-017",
    "previous_temporary_key": "TMP-BRD-WS-07-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Order Modification",
    "source_context_sha256": "49b3e8f656c364bf08dada0a7ea8b50193274b34c461fcbd60a522cd7aca444b",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "0914350f8bcb00aec386fff5a9fad16fd2fa3efe6ca8c0f026fbe370804e7712",
    "source_lines": "L598-L602",
    "source_section": "22. Order Modification"
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
  "stable_id": "BRD-WS-07-R017",
  "title": "Không cho phép sửa: - Currency",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R018 — Không cho phép sửa: - Promotion

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R018-AC001",
      "given": "the applicable business context, actor, and input for Không cho phép sửa: - Promotion",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R018-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R018-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Không cho phép sửa: - Promotion",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R018-O001"
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
        "BRD-WS-07-R018-AC001",
        "BRD-WS-07-R018-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R018-O001",
      "obligation_text": "Không cho phép sửa: - Promotion"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không cho phép sửa: - Promotion",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-018",
    "previous_temporary_key": "TMP-BRD-WS-07-018",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Order Modification",
    "source_context_sha256": "49b3e8f656c364bf08dada0a7ea8b50193274b34c461fcbd60a522cd7aca444b",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "31b810dd7cd3fdbbc1fa03eed7e7eeeea0efbaaa4abfc0a14f90834e555da06b",
    "source_lines": "L598-L603",
    "source_section": "22. Order Modification"
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
  "stable_id": "BRD-WS-07-R018",
  "title": "Không cho phép sửa: - Promotion",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R019 — Không cho phép sửa: - Price

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R019-AC001",
      "given": "the applicable business context, actor, and input for Không cho phép sửa: - Price",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-07-R019-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R019-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Không cho phép sửa: - Price",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-07-R019-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-07-R019-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Không cho phép sửa: - Price",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-07-R019-O001"
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
        "BRD-WS-07-R019-AC001",
        "BRD-WS-07-R019-AC002",
        "BRD-WS-07-R019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R019-O001",
      "obligation_text": "Không cho phép sửa: - Price"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R019 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R019 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R019 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-07-R019-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-07-R019-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R019 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không cho phép sửa: - Price",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-019",
    "previous_temporary_key": "TMP-BRD-WS-07-019",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Order Modification",
    "source_context_sha256": "49b3e8f656c364bf08dada0a7ea8b50193274b34c461fcbd60a522cd7aca444b",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "1de0c76df7b88cabb7f8992d04d5ff9d40d966c181dc9c057033a4696e831cc9",
    "source_lines": "L598-L604",
    "source_section": "22. Order Modification"
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
  "stable_id": "BRD-WS-07-R019",
  "title": "Không cho phép sửa: - Price",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R020 — Mọi thay đổi đều phải Audit

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-07-R020-AC001",
      "given": "an operational task within the scope of Mọi thay đổi đều phải Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-07-R020-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-07-R020-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Mọi thay đổi đều phải Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-07-R020-O001"
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
        "BRD-WS-07-R020-AC001",
        "BRD-WS-07-R020-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R020-O001",
      "obligation_text": "Mọi thay đổi đều phải Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R020 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R020 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R020 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R020 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-07-R020-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-07-R020 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi thay đổi đều phải Audit.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-020",
    "previous_temporary_key": "TMP-BRD-WS-07-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Order Modification",
    "source_context_sha256": "49b3e8f656c364bf08dada0a7ea8b50193274b34c461fcbd60a522cd7aca444b",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "cd9db4c12934e25d077f0a1b9f1a7fcb3f5f3273ae2e35dd86549a876ba70fb1",
    "source_lines": "L614",
    "source_section": "22. Order Modification"
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
  "stable_id": "BRD-WS-07-R020",
  "title": "Mọi thay đổi đều phải Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R021 — Version sau sẽ bổ sung: - Cart Recovery

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version sau sẽ bổ sung: - Cart Recovery",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-021",
    "previous_temporary_key": "TMP-BRD-WS-07-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Deferred Scope",
    "source_context_sha256": "aa9fcaee6ff8a1abbb7bd53f9886bce79efae987261ac2ed3415c1e995d79cee",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "eb33243acc6025873e06f817782746ba0f0c757e0210acedca0492057d5fe63e",
    "source_lines": "L620-L622",
    "source_section": "23. Deferred Scope"
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
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-07-R021",
  "title": "Version sau sẽ bổ sung: - Cart Recovery",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R022 — Version sau sẽ bổ sung: - Product Replacement Suggestion

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version sau sẽ bổ sung: - Product Replacement Suggestion",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-022",
    "previous_temporary_key": "TMP-BRD-WS-07-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Deferred Scope",
    "source_context_sha256": "aa9fcaee6ff8a1abbb7bd53f9886bce79efae987261ac2ed3415c1e995d79cee",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "c6faa6f693559653007516d00d2896948a77d31d03959b5b931eee54227466e3",
    "source_lines": "L620-L623",
    "source_section": "23. Deferred Scope"
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
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-07-R022",
  "title": "Version sau sẽ bổ sung: - Product Replacement Suggestion",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R023 — Version sau sẽ bổ sung: - Split Payment

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version sau sẽ bổ sung: - Split Payment",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-023",
    "previous_temporary_key": "TMP-BRD-WS-07-023",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Deferred Scope",
    "source_context_sha256": "aa9fcaee6ff8a1abbb7bd53f9886bce79efae987261ac2ed3415c1e995d79cee",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "d33f7ad38be28c8813c3229d34e88aeacc6326dfbc40c9b22121067b277e40ae",
    "source_lines": "L620-L624",
    "source_section": "23. Deferred Scope"
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
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-07-R023",
  "title": "Version sau sẽ bổ sung: - Split Payment",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R024 — Version sau sẽ bổ sung: - Multiple Payment

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version sau sẽ bổ sung: - Multiple Payment",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-024",
    "previous_temporary_key": "TMP-BRD-WS-07-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Deferred Scope",
    "source_context_sha256": "aa9fcaee6ff8a1abbb7bd53f9886bce79efae987261ac2ed3415c1e995d79cee",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "95d9e6cf059a9e7d028753a7a9af9ed1b16a9769a29cc394be1d33f3fcd6639d",
    "source_lines": "L620-L625",
    "source_section": "23. Deferred Scope"
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
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-07-R024",
  "title": "Version sau sẽ bổ sung: - Multiple Payment",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R025 — Version sau sẽ bổ sung: - Smart Procurement

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version sau sẽ bổ sung: - Smart Procurement",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-025",
    "previous_temporary_key": "TMP-BRD-WS-07-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Deferred Scope",
    "source_context_sha256": "aa9fcaee6ff8a1abbb7bd53f9886bce79efae987261ac2ed3415c1e995d79cee",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "4720a167bdf842fb30af0155942cdd8ccc9dd0c82c9f67842385c007463f4c97",
    "source_lines": "L620-L626",
    "source_section": "23. Deferred Scope"
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
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-07-R025",
  "title": "Version sau sẽ bổ sung: - Smart Procurement",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R026 — Version sau sẽ bổ sung: - AI Procurement

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version sau sẽ bổ sung: - AI Procurement",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-026",
    "previous_temporary_key": "TMP-BRD-WS-07-026",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Deferred Scope",
    "source_context_sha256": "aa9fcaee6ff8a1abbb7bd53f9886bce79efae987261ac2ed3415c1e995d79cee",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "6e9a0c889c3660541a8760faaf94705a77f2252e5985479cacd04e56300a8ab6",
    "source_lines": "L620-L627",
    "source_section": "23. Deferred Scope"
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
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-07-R026",
  "title": "Version sau sẽ bổ sung: - AI Procurement",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R027 — Version sau sẽ bổ sung: - Bulk Procurement Recommendation

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version sau sẽ bổ sung: - Bulk Procurement Recommendation",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-027",
    "previous_temporary_key": "TMP-BRD-WS-07-027",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Deferred Scope",
    "source_context_sha256": "aa9fcaee6ff8a1abbb7bd53f9886bce79efae987261ac2ed3415c1e995d79cee",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "287bd84cad9b6d305892d7af910a9ca181b28747dca6a494ca50bd822cf2e9ee",
    "source_lines": "L620-L628",
    "source_section": "23. Deferred Scope"
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
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-07-R027",
  "title": "Version sau sẽ bổ sung: - Bulk Procurement Recommendation",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-07-001 — Sales Order và Purchase Order là hai Business Object độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "EP-07-001-AC001",
      "given": "a candidate Sales Order và Purchase Order là hai Business Object độc lập record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "EP-07-001-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "EP-07-001-AC002",
      "given": "a Sales Order và Purchase Order là hai Business Object độc lập candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "EP-07-001-O001"
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
        "EP-07-001-AC001",
        "EP-07-001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-07-001-O001",
      "obligation_text": "Sales Order và Purchase Order là hai Business Object độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sales Order và Purchase Order là hai Business Object độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-07-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-07-001",
    "source_context_sha256": "7a16be798c8f208cd58624aa19131a2c51820c4594aaf9a4cbd3b90281928592",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "d43565398823494aa8e8533eca97c9fab4707b8a9bbbe66c84951743f3f4d9a6",
    "source_lines": "L754-L757",
    "source_section": "25. Enterprise Design Principles > EP-07-001"
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
  "stable_id": "EP-07-001",
  "title": "Sales Order và Purchase Order là hai Business Object độc lập",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-07-002 — Checkout chỉ xác nhận khả năng Procurement, không thực hiện Procurement

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-07-002-AC001",
      "given": "the applicable business context, actor, and input for Checkout chỉ xác nhận khả năng Procurement, không thực hiện Procurement",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-07-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-07-002-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Checkout chỉ xác nhận khả năng Procurement, không thực hiện Procurement",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-07-002-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-07-002-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Checkout chỉ xác nhận khả năng Procurement, không thực hiện Procurement",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-07-002-O001"
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
        "EP-07-002-AC001",
        "EP-07-002-AC002",
        "EP-07-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-07-002-O001",
      "obligation_text": "Checkout chỉ xác nhận khả năng Procurement, không thực hiện Procurement"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-07-002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-07-002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-07-002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-07-002-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-07-002-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-07-002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Checkout chỉ xác nhận khả năng Procurement, không thực hiện Procurement.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-07-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-07-002",
    "source_context_sha256": "1569316653d8164e447873ad46bedd4b537e902397ef338cdc4165785959f9ac",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "20dedf0395bf0c1cea1a3b759cc764d320ed6f929d96ad4d27e2998c2960079c",
    "source_lines": "L760-L763",
    "source_section": "25. Enterprise Design Principles > EP-07-002"
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
  "stable_id": "EP-07-002",
  "title": "Checkout chỉ xác nhận khả năng Procurement, không thực hiện Procurement",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-07-003 — Inventory Reservation phải đồng bộ với Price Reservation

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-07-003-AC001",
      "given": "the applicable business context, actor, and input for Inventory Reservation phải đồng bộ với Price Reservation",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-07-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-07-003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Inventory Reservation phải đồng bộ với Price Reservation",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-07-003-O001"
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
        "EP-07-003-AC001",
        "EP-07-003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-07-003-O001",
      "obligation_text": "Inventory Reservation phải đồng bộ với Price Reservation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-07-003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-07-003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-07-003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EP-07-003 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-07-003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-07-003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Inventory Reservation phải đồng bộ với Price Reservation.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-07-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-07-003",
    "source_context_sha256": "a35edd96208b2e158a41db196e6abef502ea3f6344cc4e34daf7979aa26bc0ad",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "f7f12348ace9c8f232e5ea8171fbea18482a064caa4a5e8461ac3a5420bc9cc5",
    "source_lines": "L766-L769",
    "source_section": "25. Enterprise Design Principles > EP-07-003"
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
  "stable_id": "EP-07-003",
  "title": "Inventory Reservation phải đồng bộ với Price Reservation",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-07-004 — Fulfillment Assignment là Capability của Fulfillment Domain

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-07-004-AC001",
      "given": "the applicable business context, actor, and input for Fulfillment Assignment là Capability của Fulfillment Domain",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-07-004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-07-004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Fulfillment Assignment là Capability của Fulfillment Domain",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-07-004-O001"
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
        "EP-07-004-AC001",
        "EP-07-004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-07-004-O001",
      "obligation_text": "Fulfillment Assignment là Capability của Fulfillment Domain"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-07-004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-07-004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-07-004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EP-07-004 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-07-004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-07-004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Fulfillment Assignment là Capability của Fulfillment Domain.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-07-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-07-004",
    "source_context_sha256": "76956279943f9abd9e06fc1248ff1613371340d76ab58e023e1861d9520f1995",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "f590ae58c97a2111de1c5bd62c7174f5e2fa70c06185078be326b8770737ccaf",
    "source_lines": "L772-L775",
    "source_section": "25. Enterprise Design Principles > EP-07-004"
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
  "stable_id": "EP-07-004",
  "title": "Fulfillment Assignment là Capability của Fulfillment Domain",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-07-005 — Mọi Product Item phải truy vết được: Purchase Order ↓ Inventory ↓ Allocation ↓ Sales Order ↓ Cus…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-07-005-AC001",
      "given": "the applicable business context, actor, and input for Mọi Product Item phải truy vết được: Purchase Order ↓ Inventory ↓ Allocation ↓ Sales Order ↓ Cus…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-07-005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-07-005-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Mọi Product Item phải truy vết được: Purchase Order ↓ Inventory ↓ Allocation ↓ Sales Order ↓ Cus…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-07-005-O001"
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
        "EP-07-005-AC001",
        "EP-07-005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-07-005-O001",
      "obligation_text": "Mọi Product Item phải truy vết được: Purchase Order ↓ Inventory ↓ Allocation ↓ Sales Order ↓ Customer"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-07-005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-07-005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-07-005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EP-07-005 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-07-005-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-07-005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Product Item phải truy vết được: Purchase Order ↓ Inventory ↓ Allocation ↓ Sales Order ↓ Customer",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007",
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-07-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-07-005",
    "source_context_sha256": "dd0222a62fc1d8a4c95c720cc15fb7ccccc4a657bef21b7171e0018d65bffc55",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "cff31f585b3cf83d82690022c24aa6fd7c2fb754a834fe2fdc0cb2322aaf32de",
    "source_lines": "L778-L799",
    "source_section": "25. Enterprise Design Principles > EP-07-005"
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
  "stable_id": "EP-07-005",
  "title": "Mọi Product Item phải truy vết được: Purchase Order ↓ Inventory ↓ Allocation ↓ Sales Order ↓ Cus…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-07-006 — Transaction Domain chỉ tham chiếu Master Object và Commercial Object thông qua Snapshot

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "EP-07-006-AC001",
      "given": "a candidate Transaction Domain chỉ tham chiếu Master Object và Commercial Object thông qua Snapshot record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "EP-07-006-O001"
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
        "EP-07-006-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-07-006-O001",
      "obligation_text": "Transaction Domain chỉ tham chiếu Master Object và Commercial Object thông qua Snapshot"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Transaction Domain chỉ tham chiếu Master Object và Commercial Object thông qua Snapshot.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-07-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-07-006",
    "source_context_sha256": "6544ba81f342311f094fa231c838c86d40cc4782c405ad435ad9189adcce58c3",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "848bb9332d2999c816b0b945843891fa5a4e6f4ce63a2f10e30a7e24884f5f0c",
    "source_lines": "L802-L805",
    "source_section": "25. Enterprise Design Principles > EP-07-006"
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
  "stable_id": "EP-07-006",
  "title": "Transaction Domain chỉ tham chiếu Master Object và Commercial Object thông qua Snapshot",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
