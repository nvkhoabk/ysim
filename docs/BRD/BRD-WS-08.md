---
document_code: "BRD-WS-08"
document_id: "BRD-WS-08"
title: "Payment, Payment Gateway & Payment Lifecycle"
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

# BRD Workshop 08

# Payment, Payment Gateway & Payment Lifecycle

---

# 1. Workshop Objective

Workshop này xác định toàn bộ Payment Domain của YSim.

Workshop bao gồm:

- Payment Session
- Payment Method
- Payment Gateway
- Merchant Account
- Payment Attempt
- Payment Callback
- Payment Snapshot
- Refund
- Offline Payment
- Payment Notification

Workshop mô tả toàn bộ vòng đời thanh toán từ thời điểm SalesOrder chuyển sang Pending Payment đến khi Payment được xác nhận thành công hoặc thất bại.

Settlement, Financial Event và Accounting được mô tả ở các Workshop tiếp theo.

---

# 2. Business Objects Introduced

| Business Object | Type |
|-----------------|------|
| PaymentSession | Transaction |
| PaymentTransaction | Transaction |
| PaymentAttempt | Transaction |
| PaymentGateway | Master |
| MerchantAccount | Commercial |
| PaymentMethod | Master |
| PaymentInstruction | Transaction |
| PaymentCallback | Transaction |
| PaymentSnapshot | Transaction |
| RefundRequest | Transaction |
| RefundTransaction | Transaction |
| OfflinePaymentConfirmation | Transaction |

---

# 3. Payment Domain Architecture

Payment Domain được chia thành các Business Object độc lập.

```text
Payment Method
        │
        ▼
Merchant Account
        │
        ▼
Payment Gateway
        │
        ▼
Payment Session
        │
        ▼
Payment Attempt
        │
        ▼
Payment Callback
        │
        ▼
Payment Snapshot
        │
        ▼
Refund
```

Mỗi Business Object có trách nhiệm riêng.

---

# 4. Payment Owner

PaymentSession luôn thuộc PaymentOwner.

PaymentOwner chịu trách nhiệm:

- Nhận tiền
- Quản lý Merchant Account
- Quản lý Payment Configuration
- Quản lý Refund

Trong Version 2.0:

PaymentOwner không được thay đổi sau khi PaymentSession được tạo.

Đối với Offline Payment:

- PaymentOwner vẫn là Organization nhận tiền.
- Sales chỉ được phép xác nhận thanh toán nếu có Offline Payment Capability.

---

# 5. Payment Gateway

PaymentGateway Definition thuộc YSim.

YSim chịu trách nhiệm:

- Phát triển Gateway Adapter
- Kiểm thử tích hợp
- Quản lý phiên bản API
- Quản lý cấu hình kỹ thuật
- Chứng nhận Gateway

Chỉ các PaymentGateway đã được YSim chứng nhận mới được Organization sử dụng.

---

# 6. Merchant Account

MerchantAccount thuộc Organization.

PaymentOwner có thể:

- Khai báo Merchant Account
- Merchant ID
- API Key
- Secret Key
- Webhook URL
- Callback URL
- Settlement Account
- Test Connection
- Test Payment

YSim cũng có Merchant Account nội bộ để kiểm thử PaymentGateway.

Trong Payment Lifecycle, Gateway luôn sử dụng MerchantAccount tương ứng của PaymentOwner.

---

# 7. Payment Method

PaymentMethod độc lập với PaymentGateway.

Ví dụ:

PaymentMethod:

- Credit Card
- QR Payment
- Apple Pay
- Google Pay
- Bank Transfer
- Cash

PaymentGateway:

- Stripe
- OnePay
- PayPal
- Airwallex

Một PaymentMethod có thể được hỗ trợ bởi nhiều Gateway.

---

# 8. Payment Session

PaymentSession là Transaction Object.

PaymentSession quản lý:

- SalesOrder
- PaymentOwner
- MerchantAccount
- PaymentMethod
- Currency
- Amount
- Reservation
- Status

PaymentSession không thay đổi trong suốt quá trình Retry.

---

# 9. Payment Attempt

PaymentAttempt là Business Object độc lập.

Một PaymentSession có thể có nhiều PaymentAttempt.

Ví dụ:

```text
Payment Session
        │
        ▼
Attempt #1
        │
     Failed
        │
        ▼
Attempt #2
        │
    Success
```

Toàn bộ lịch sử PaymentAttempt phải được lưu.

---

# 10. Reservation Timeout

Sau khi Customer chọn PaymentMethod và bấm:

**Thanh toán**

Hệ thống cập nhật:

- Payment Reservation Timeout
- Price Reservation Timeout
- Inventory Reservation Timeout

theo cấu hình của PaymentGateway.

Gateway Timeout là giá trị ưu tiên.

---

# 11. Payment Callback

PaymentCallback là Business Object.

Lưu:

- Gateway
- Payload
- Signature
- Verify Result
- Callback Time
- Processing Result
- Retry Count

Mọi Callback phải được Audit.

---

# 12. Payment Snapshot

PaymentSnapshot được tạo sau Payment Success.

Snapshot bao gồm:

- SalesOrder
- PaymentSession
- MerchantAccount
- PaymentGateway
- PaymentMethod
- Currency
- ExchangeRate
- Amount
- GatewayFee
- CommercialSnapshot Reference
- Payment Time
- Callback Reference

PaymentSnapshot phục vụ:

- Settlement
- Reporting
- Audit
- Reconciliation

---

# 13. Payment Fee

Gateway Fee được cấu hình linh hoạt.

Fee có thể:

- Customer chịu
- PaymentOwner chịu
- Chia sẻ

Việc tính Fee dựa trên:

CommercialAgreement.

---

# 14. Multi-Currency Payment

Version 2.0 yêu cầu:

Payment Currency phải thuộc Currency đã được khai báo trong PriceBook.

PriceBook có thể hỗ trợ nhiều Currency.

Customer lựa chọn Currency trước Checkout.

Không hỗ trợ đổi Currency trong PaymentSession.

---

# 15. Payment Retry

Retry giữ nguyên:

PaymentSession.

Retry tạo:

PaymentAttempt mới.

Không tạo PaymentSession mới.

---

# 16. Partial Payment

Version 2.0:

Không hỗ trợ Partial Payment.

Một SalesOrder chỉ có một PaymentSession.

---

# 17. Offline Payment

Version 2.0 hỗ trợ:

- Cash
- Manual Bank Transfer

Để Payment thành công:

Sales phải có:

Offline Payment Capability.

Sales phải xác nhận:

Đã nhận thanh toán.

Sau khi xác nhận:

PaymentSession chuyển sang:

Payment Success.

---

# 18. Payment Success

Payment Success chỉ phản ánh:

Customer đã thanh toán thành công.

Payment Success không phản ánh:

- Inventory
- Procurement
- Allocation
- Fulfillment

Sau Payment Success hệ thống thực hiện:

- PaymentSnapshot
- CommercialSnapshot
- Payment Notification

Sau đó kích hoạt Workflow:

```text
Inventory

↓

Auto Procurement

↓

Allocation

↓

Fulfillment
```

Email Payment Success chỉ bao gồm:

- Payment Confirmation
- Invoice

Fulfillment Notification được gửi sau khi Fulfillment hoàn tất.

---

# 19. Refund

Refund là Business Object độc lập.

Refund có thể phát sinh khi:

- Customer Cancel
- PurchaseOrder Failure
- Commercial Change
- Payment Error

Refund quản lý:

- Refund Amount
- Refund Reason
- Refund Status
- Refund Reference

Refund không thuộc PaymentSession.

---

# 20. Payment Notification

Payment Notification gửi tới các bên liên quan.

Customer:

- Payment Success
- Invoice

Organization:

- Payment Success
- SalesOrder Paid

Sales:

- Payment Success
- SalesOrder Paid
- Commission Pending (nếu có)

Payment Notification không bao gồm Fulfillment.

---

# 21. Payment Security

PaymentSession lưu:

- IP Address
- Device
- Browser
- Country
- Fraud Score
- Risk Metadata

Version 2.0 chỉ lưu dữ liệu.

Anti Fraud Engine sẽ triển khai ở phiên bản sau.

---

# 22. Payment Session Status

PaymentSession hỗ trợ các trạng thái:

```text
Created

↓

Pending

↓

Redirected

↓

Waiting Callback

↓

Success

↓

Failed

↓

Cancelled

↓

Expired

↓

Unknown

↓

Reconciliation
```

Unknown:

Gateway chưa xác nhận trạng thái cuối.

Reconciliation:

Đồng bộ lại trạng thái với Gateway.

---

# 23. Business Decisions (Locked)

## BD-08-001

PaymentSession luôn thuộc PaymentOwner.

---

## BD-08-002

PaymentGateway Definition thuộc YSim.

---

## BD-08-003

MerchantAccount thuộc Organization.

---

## BD-08-004

PaymentMethod độc lập với PaymentGateway.

---

## BD-08-005

PaymentAttempt là Business Object.

---

## BD-08-006

Reservation Timeout ưu tiên theo PaymentGateway.

---

## BD-08-007

PaymentCallback là Business Object.

---

## BD-08-008

PaymentSnapshot được tạo sau Payment Success.

---

## BD-08-009

GatewayFee được cấu hình theo CommercialAgreement.

---

## BD-08-010

Payment Currency phải thuộc PriceBook.

---

## BD-08-011

Retry giữ nguyên PaymentSession.

---

## BD-08-012

Version 2.0 không hỗ trợ Partial Payment.

---

## BD-08-013

Offline Payment yêu cầu Offline Payment Capability.

---

## BD-08-014

Payment Success không bao gồm Procurement hoặc Fulfillment.

---

## BD-08-015

Refund là Business Object độc lập.

---

## BD-08-016

Payment Notification tách biệt Fulfillment Notification.

---

## BD-08-017

PaymentSession lưu Risk Metadata.

---

# 24. Enterprise Design Principles

## EP-08-001

Payment Domain độc lập với Commercial Domain và Fulfillment Domain.

---

## EP-08-002

PaymentGateway và MerchantAccount là hai Business Object độc lập.

---

## EP-08-003

PaymentMethod không phụ thuộc PaymentGateway.

---

## EP-08-004

Payment Success chỉ xác nhận việc nhận tiền thành công.

---

## EP-08-005

PaymentSession là Business Object trung tâm của Payment Lifecycle.

---

## EP-08-006

Retry chỉ tạo PaymentAttempt mới.

---

## EP-08-007

Payment Notification và Fulfillment Notification là hai Workflow độc lập.

---

# 25. Payment Lifecycle

```text
Checkout Session
        │
        ▼
Payment Session
        │
        ▼
Payment Attempt
        │
        ▼
Payment Gateway
        │
        ▼
Payment Callback
        │
        ▼
Payment Success
        │
        ├── Payment Snapshot
        ├── Commercial Snapshot
        ├── Payment Notification
        └── Trigger Transaction Workflow
                │
                ▼
Inventory

↓

Auto Procurement

↓

Allocation

↓

Fulfillment
```

---

# 26. Traceability

Workshop này kế thừa:

- BRD-WS-01
- BRD-WS-02
- BRD-WS-03
- BRD-WS-04
- BRD-WS-05
- BRD-WS-06
- BRD-WS-07

---

# 27. Impacts to Other Domains

Workshop này ảnh hưởng tới:

- Procurement Engine
- Inventory Domain
- Fulfillment Engine
- Settlement Engine
- Financial Event Engine
- Reconciliation Engine
- Anti Fraud Engine
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
- Fulfillment Engine
- Settlement Engine
- Financial Event Engine

---

# 29. Next Workshop

**BRD-WS-09 – Inventory, Allocation & Fulfillment Lifecycle**

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-001 — PaymentSession luôn thuộc PaymentOwner

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
      "requirement_id": "BD-08-001",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "5f251a7da80b9c664dd58dc760e75cf2ad4bc433785a4d7c79cab0149ca2666b"
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
        "BD-08-001-AC001",
        "BD-08-001-AC002",
        "BD-08-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-001-O001",
      "obligation_text": "PaymentSession luôn thuộc PaymentOwner"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-001 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-001 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-001 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-001-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-001-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-001 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "PaymentSession luôn thuộc PaymentOwner.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Payment Owner",
    "source_context_sha256": "d66fa58ef3786b25e98e8867a9f8aa4b327df523f28370ac1eaa41dddd5cf2c5",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "5f251a7da80b9c664dd58dc760e75cf2ad4bc433785a4d7c79cab0149ca2666b",
    "source_lines": "L788-L896",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-001"
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
  "stable_id": "BD-08-001",
  "title": "PaymentSession luôn thuộc PaymentOwner",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-002 — PaymentGateway Definition thuộc YSim

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-08-002",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "7887546466016d375651b0cdfb8306a85f1954486795495171b5aded931fbaa9"
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
        "BD-08-002-AC001",
        "BD-08-002-AC002",
        "BD-08-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-002-O001",
      "obligation_text": "PaymentGateway Definition thuộc YSim"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-002 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-002-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-002-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-002 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "PaymentGateway Definition thuộc YSim.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Payment Gateway",
    "source_context_sha256": "ec7f9600cdedec66bf0905fb5f489da2ff259f56a166fd36a47d2a50ebea89a1",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "7887546466016d375651b0cdfb8306a85f1954486795495171b5aded931fbaa9",
    "source_lines": "L898-L1010",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-002"
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
  "stable_id": "BD-08-002",
  "title": "PaymentGateway Definition thuộc YSim",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-003 — MerchantAccount thuộc Organization

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
      "requirement_id": "BD-08-003",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "9b16fab95e280669c4ed72c3cadf2fa8c71438c7d83081f488042308bda83ed0"
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
        "BD-08-003-AC001",
        "BD-08-003-AC002",
        "BD-08-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-003-O001",
      "obligation_text": "MerchantAccount thuộc Organization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "MerchantAccount thuộc Organization.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Merchant Account",
    "source_context_sha256": "aa494a2dff62a50d9623529c4e07a13f63064d5bd7030267a5ddfb4baf1aeb35",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "9b16fab95e280669c4ed72c3cadf2fa8c71438c7d83081f488042308bda83ed0",
    "source_lines": "L1012-L1087",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-003"
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
  "stable_id": "BD-08-003",
  "title": "MerchantAccount thuộc Organization",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-004 — PaymentMethod độc lập với PaymentGateway

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-08-004",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "e036cf79cad2c98eae8a16f735d76b356322344f81ebf617f23b768925cf379b"
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
        "BD-08-004-AC001",
        "BD-08-004-AC002",
        "BD-08-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-004-O001",
      "obligation_text": "PaymentMethod độc lập với PaymentGateway"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-004-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-004 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "PaymentMethod độc lập với PaymentGateway.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Payment Method",
    "source_context_sha256": "a6fc840350ecdd5ffc30aff91741cae504eff8273bb15874385893f7fabf37bc",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "e036cf79cad2c98eae8a16f735d76b356322344f81ebf617f23b768925cf379b",
    "source_lines": "L1089-L1203",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-004"
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
  "stable_id": "BD-08-004",
  "title": "PaymentMethod độc lập với PaymentGateway",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-005 — PaymentAttempt là Business Object

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
      "requirement_id": "BD-08-005",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "4d8aa12e6735ca766f5791c602e38e2a2de50f14b177b7c91e584f7d14f7e2cc"
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
        "BD-08-005-AC001",
        "BD-08-005-AC002",
        "BD-08-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-005-O001",
      "obligation_text": "PaymentAttempt là Business Object"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-005 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-005 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "PaymentAttempt là Business Object.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-08-005",
    "source_context_sha256": "185759f9ffcd05be7692ff598c547fb5cf3ec95fdb3dabb98a2cff5a7087ecf2",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "4d8aa12e6735ca766f5791c602e38e2a2de50f14b177b7c91e584f7d14f7e2cc",
    "source_lines": "L1205-L1313",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-005"
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
  "stable_id": "BD-08-005",
  "title": "PaymentAttempt là Business Object",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-006 — Reservation Timeout ưu tiên theo PaymentGateway

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-08-006",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "8af54e3c1a951e216980270d65eefd35ef0f02f136bed95f1c4e218e52f76cb4"
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
        "BD-08-006-AC001",
        "BD-08-006-AC002",
        "BD-08-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-006-O001",
      "obligation_text": "Reservation Timeout ưu tiên theo PaymentGateway"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-006 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-006-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-006-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-006 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reservation Timeout ưu tiên theo PaymentGateway.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-08-006",
    "source_context_sha256": "668e3b3657053002212fffd5cc37a068167bf4086e3a7044a77a5332fb8edf1d",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "8af54e3c1a951e216980270d65eefd35ef0f02f136bed95f1c4e218e52f76cb4",
    "source_lines": "L1315-L1427",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-006"
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
  "stable_id": "BD-08-006",
  "title": "Reservation Timeout ưu tiên theo PaymentGateway",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-007 — PaymentCallback là Business Object

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
      "requirement_id": "BD-08-007",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "bd99f83d34577d6b5c51d2c4f388cc8eb4a3397fc6b675981461d454e44e5f48"
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
        "BD-08-007-AC001",
        "BD-08-007-AC002",
        "BD-08-007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-007-O001",
      "obligation_text": "PaymentCallback là Business Object"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-007 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-007-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-007-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-007 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "PaymentCallback là Business Object.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Payment Callback",
    "source_context_sha256": "772b50470e988ce974487239f2ab6a668575877d6f1e7331d12cda9bc0984013",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "bd99f83d34577d6b5c51d2c4f388cc8eb4a3397fc6b675981461d454e44e5f48",
    "source_lines": "L1429-L1537",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-007"
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
  "stable_id": "BD-08-007",
  "title": "PaymentCallback là Business Object",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-008 — PaymentSnapshot được tạo sau Payment Success

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Failed or pending Payment does not create a success snapshot"
    ],
    "concrete_bindings": [
      {
        "from_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BD-08-008.FROM_STATE"
            ],
            "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
            "source_type": "SOURCE_LITERAL",
            "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
          },
          "identifier": "BD-08-008.FROM_STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
            "source_lines": "L576-L579",
            "source_section": "23. Business Decisions (Locked) > BD-08-008"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "RESOLVE.BD-08-008.BD-08-008.FROM_STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        },
        "state_machine": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
            "source_type": "SOURCE_LITERAL",
            "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
          },
          "identifier": "BD-08-008.STATE_MACHINE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
            "source_lines": "L576-L579",
            "source_section": "23. Business Decisions (Locked) > BD-08-008"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_MACHINE_ID",
            "resolver_id": "RESOLVE.BD-08-008.BD-08-008.STATE_MACHINE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_MACHINE_ID"
        },
        "to_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BD-08-008.TO_STATE"
            ],
            "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
            "source_type": "SOURCE_LITERAL",
            "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
          },
          "identifier": "BD-08-008.TO_STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
            "source_lines": "L576-L579",
            "source_section": "23. Business Decisions (Locked) > BD-08-008"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "RESOLVE.BD-08-008.BD-08-008.TO_STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        },
        "trigger": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
            "source_type": "SOURCE_LITERAL",
            "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
          },
          "identifier": "BD-08-008.TRIGGER",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
            "source_lines": "L576-L579",
            "source_section": "23. Business Decisions (Locked) > BD-08-008"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ACTION_ID",
            "resolver_id": "RESOLVE.BD-08-008.BD-08-008.TRIGGER",
            "version": "1.0.0"
          },
          "semantic_type": "ACTION_ID"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BD-08-008",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "A PaymentSnapshot is created before success or absent after success"
    ],
    "operator_composition": [
      "STATE_TRANSITION_ALLOWED"
    ],
    "positive_oracle": [
      "A PaymentSnapshot is created after Payment Success"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
      "source_lines": "L576-L579",
      "source_section": "23. Business Decisions (Locked) > BD-08-008"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
          "source_type": "SOURCE_LITERAL",
          "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
        },
        "identifier": "BD-08-008.BD-08-008.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BD-08-008.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-08.md",
          "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
          "source_lines": "L576-L579",
          "source_section": "23. Business Decisions (Locked) > BD-08-008"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BD-08-008.BD-08-008.BD-08-008.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BD-08-008.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.PAYMENT_ID",
        "FIELD.PAYMENT_STATE",
        "FIELD.PAYMENT_SUCCESS_TIME",
        "FIELD.SNAPSHOT_ID",
        "FIELD.SNAPSHOT_TIME"
      ],
      "producer": "BD-08-008.EVIDENCE.PRODUCER",
      "required_collection_origin": "BD-08-008.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.PAYMENT_ID",
        "FIELD.PAYMENT_STATE",
        "FIELD.PAYMENT_SUCCESS_TIME",
        "FIELD.SNAPSHOT_ID",
        "FIELD.SNAPSHOT_TIME"
      ],
      "required_values_or_hashes": [
        "BD-08-008.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BD-08-008.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BD-08-008.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BD-08-008-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED",
          "evaluator_consumed_bindings": [
            "from_state",
            "state_machine",
            "to_state",
            "trigger"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
              "source_type": "SOURCE_LITERAL",
              "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
            },
            "identifier": "BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
              "source_lines": "L576-L579",
              "source_section": "23. Business Decisions (Locked) > BD-08-008"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-08-008.BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
              "source_type": "SOURCE_LITERAL",
              "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
            },
            "identifier": "BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
              "source_lines": "L576-L579",
              "source_section": "23. Business Decisions (Locked) > BD-08-008"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "RESOLVE.BD-08-008.BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "STATE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "from_state": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-08-008.FROM_STATE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
                },
                "identifier": "BD-08-008.FROM_STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
                  "source_lines": "L576-L579",
                  "source_section": "23. Business Decisions (Locked) > BD-08-008"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BD-08-008.BD-08-008.FROM_STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "state_machine": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
                },
                "identifier": "BD-08-008.STATE_MACHINE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
                  "source_lines": "L576-L579",
                  "source_section": "23. Business Decisions (Locked) > BD-08-008"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_MACHINE_ID",
                  "resolver_id": "RESOLVE.BD-08-008.BD-08-008.STATE_MACHINE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_MACHINE_ID"
              },
              "to_state": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-08-008.TO_STATE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
                },
                "identifier": "BD-08-008.TO_STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
                  "source_lines": "L576-L579",
                  "source_section": "23. Business Decisions (Locked) > BD-08-008"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BD-08-008.BD-08-008.TO_STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "trigger": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
                },
                "identifier": "BD-08-008.TRIGGER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
                  "source_lines": "L576-L579",
                  "source_section": "23. Business Decisions (Locked) > BD-08-008"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.BD-08-008.BD-08-008.TRIGGER",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
                },
                "identifier": "BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
                  "source_lines": "L576-L579",
                  "source_section": "23. Business Decisions (Locked) > BD-08-008"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BD-08-008.BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
                },
                "identifier": "BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
                  "source_lines": "L576-L579",
                  "source_section": "23. Business Decisions (Locked) > BD-08-008"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "OBSERVE.BD-08-008.BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
                "source_type": "SOURCE_LITERAL",
                "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
              },
              "identifier": "BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
                "source_lines": "L576-L579",
                "source_section": "23. Business Decisions (Locked) > BD-08-008"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-08-008.BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "STATE_TRANSITION_ALLOWED"
          },
          "obligation_id": "BD-08-008-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
              "source_type": "SOURCE_LITERAL",
              "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
            },
            "identifier": "BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
              "source_lines": "L576-L579",
              "source_section": "23. Business Decisions (Locked) > BD-08-008"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "OBSERVE.BD-08-008.BD-08-008.BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "STATE_ID"
          },
          "operator_id": "STATE_TRANSITION_ALLOWED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "from_state": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-08-008.FROM_STATE"
                ],
                "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
                "source_type": "SOURCE_LITERAL",
                "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
              },
              "identifier": "BD-08-008.FROM_STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
                "source_lines": "L576-L579",
                "source_section": "23. Business Decisions (Locked) > BD-08-008"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BD-08-008.BD-08-008.FROM_STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            },
            "state_machine": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
                "source_type": "SOURCE_LITERAL",
                "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
              },
              "identifier": "BD-08-008.STATE_MACHINE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
                "source_lines": "L576-L579",
                "source_section": "23. Business Decisions (Locked) > BD-08-008"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_MACHINE_ID",
                "resolver_id": "RESOLVE.BD-08-008.BD-08-008.STATE_MACHINE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_MACHINE_ID"
            },
            "to_state": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-08-008.TO_STATE"
                ],
                "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
                "source_type": "SOURCE_LITERAL",
                "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
              },
              "identifier": "BD-08-008.TO_STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
                "source_lines": "L576-L579",
                "source_section": "23. Business Decisions (Locked) > BD-08-008"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BD-08-008.BD-08-008.TO_STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            },
            "trigger": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
                "source_type": "SOURCE_LITERAL",
                "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
              },
              "identifier": "BD-08-008.TRIGGER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
                "source_lines": "L576-L579",
                "source_section": "23. Business Decisions (Locked) > BD-08-008"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ACTION_ID",
                "resolver_id": "RESOLVE.BD-08-008.BD-08-008.TRIGGER",
                "version": "1.0.0"
              },
              "semantic_type": "ACTION_ID"
            }
          }
        }
      ],
      "boundary_cases": [
        "Failed or pending Payment does not create a success snapshot"
      ],
      "contract_ast_sha256": "efa68e86ce4c124236847fb99354b0c13d52f6dd3e754c5d40cc7d604e41cdaf",
      "contract_id": "P2C.C4.CONTRACT.BD-08-008",
      "criticality": "CRITICAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-008",
            "source_type": "SOURCE_LITERAL",
            "version": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14"
          },
          "identifier": "BD-08-008.BD-08-008.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-08-008.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
            "source_lines": "L576-L579",
            "source_section": "23. Business Decisions (Locked) > BD-08-008"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BD-08-008.BD-08-008.BD-08-008.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BD-08-008.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.PAYMENT_ID",
          "FIELD.PAYMENT_STATE",
          "FIELD.PAYMENT_SUCCESS_TIME",
          "FIELD.SNAPSHOT_ID",
          "FIELD.SNAPSHOT_TIME"
        ],
        "producer": "BD-08-008.EVIDENCE.PRODUCER",
        "required_collection_origin": "BD-08-008.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.PAYMENT_ID",
          "FIELD.PAYMENT_STATE",
          "FIELD.PAYMENT_SUCCESS_TIME",
          "FIELD.SNAPSHOT_ID",
          "FIELD.SNAPSHOT_TIME"
        ],
        "required_values_or_hashes": [
          "BD-08-008.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BD-08-008.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BD-08-008.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-A70054B1EF95861BF110",
        "P2C-C4-FX-98D14953F65F36B24DC5",
        "P2C-C4-FX-94F0F1738C2D595CC469"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "A PaymentSnapshot is created before success or absent after success"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-08-008-O001",
          "obligation_text": "PaymentSnapshot được tạo sau Payment Success"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BD-08-008.O1.1.STATE_TRANSITION_ALLOWED"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-08-008-O001"
        }
      ],
      "operator_composition": [
        "STATE_TRANSITION_ALLOWED"
      ],
      "positive_oracles": [
        "A PaymentSnapshot is created after Payment Success"
      ],
      "preconditions": [
        "The successful Payment and its final payment context are committed"
      ],
      "prohibitions": [
        "A PaymentSnapshot is created before success or absent after success"
      ],
      "requirement_id": "BD-08-008",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-08.md",
        "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
        "source_lines": "L576-L579",
        "source_section": "23. Business Decisions (Locked) > BD-08-008"
      },
      "source_statement": "PaymentSnapshot được tạo sau Payment Success.",
      "surrounding_source_context": "## BD-08-008\n\nPaymentSnapshot được tạo sau Payment Success.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BD-08-008",
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
        "BD-08-008-AC001",
        "BD-08-008-AC002",
        "BD-08-008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-008-O001",
      "obligation_text": "PaymentSnapshot được tạo sau Payment Success"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-008 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-008 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-008 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-008-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-008-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-008 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "PaymentSnapshot được tạo sau Payment Success.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Payment Snapshot",
    "source_context_sha256": "98ecf427d6353da6c05776af0c88cf43dcc65652ca90a0e07bdbe0a91032e6af",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "04e82d84cd262d494aa962a5f1948f41a0d61bafc19cc23794eda1d766eb9246",
    "source_lines": "L1539-L2522",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-008"
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
  "stable_id": "BD-08-008",
  "title": "PaymentSnapshot được tạo sau Payment Success",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-009 — GatewayFee được cấu hình theo CommercialAgreement

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-08-009",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "314950c9d1084bd28000aeafb062db05e315d68ecfb367cb96f65fbfa7cd04fb"
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
        "BD-08-009-AC001",
        "BD-08-009-AC002",
        "BD-08-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-009-O001",
      "obligation_text": "GatewayFee được cấu hình theo CommercialAgreement"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "GatewayFee được cấu hình theo CommercialAgreement.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-08-009",
    "source_context_sha256": "8661e2448ae8a083de39d3fb475d0e0a443c442aad9004afeff05af9fbe12655",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "314950c9d1084bd28000aeafb062db05e315d68ecfb367cb96f65fbfa7cd04fb",
    "source_lines": "L2524-L2603",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-009"
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
  "stable_id": "BD-08-009",
  "title": "GatewayFee được cấu hình theo CommercialAgreement",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-010 — Payment Currency phải thuộc PriceBook

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
      "requirement_id": "BD-08-010",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "df1da2b382518e5d111b177395ad16da518dd8b0f115ec131c960a3f6460d76c"
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
        "BD-08-010-AC001",
        "BD-08-010-AC002",
        "BD-08-010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-010-O001",
      "obligation_text": "Payment Currency phải thuộc PriceBook"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-010 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-010 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-010 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-010-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-010-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-010 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Payment Currency phải thuộc PriceBook.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-08-010",
    "source_context_sha256": "199c2a1c4fe8c34bb2109711c09c3ebf4e6b6e2af90c2f25fe09ae1619972086",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "df1da2b382518e5d111b177395ad16da518dd8b0f115ec131c960a3f6460d76c",
    "source_lines": "L2605-L2713",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-010"
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
  "stable_id": "BD-08-010",
  "title": "Payment Currency phải thuộc PriceBook",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-011 — Retry giữ nguyên PaymentSession

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-08-011",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "edfeb53861ec476050b5c87abdcd95b4a3f45fb3bb6a2017bbef86471e0d9af2"
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
        "BD-08-011-AC001",
        "BD-08-011-AC002",
        "BD-08-011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-011-O001",
      "obligation_text": "Retry giữ nguyên PaymentSession"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-011 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-011 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-011 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-011-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-011-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-011 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Retry giữ nguyên PaymentSession.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-08-011",
    "source_context_sha256": "a17a7840355c183b3190cc1296850e1f2e737013050286f02a3e99f9f7c5f2d2",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "edfeb53861ec476050b5c87abdcd95b4a3f45fb3bb6a2017bbef86471e0d9af2",
    "source_lines": "L2715-L2827",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-011"
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
  "stable_id": "BD-08-011",
  "title": "Retry giữ nguyên PaymentSession",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-012 — Version 2.0 không hỗ trợ Partial Payment

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BD-08-012",
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
  "normative_statement": "Version 2.0 không hỗ trợ Partial Payment.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-08-012",
    "source_context_sha256": "c272252be54dc5555ad1c1b150296fdf45023f09dd5d84c2bbeeefbd7d09355b",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "30fb85485bb2c1b130b7fa3e0ed82b494b046ff8ab9f7f8911e8743f21477812",
    "source_lines": "L2829-L2887",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-012"
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
  "stable_id": "BD-08-012",
  "title": "Version 2.0 không hỗ trợ Partial Payment",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-013 — Offline Payment yêu cầu Offline Payment Capability

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
      "requirement_id": "BD-08-013",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "d08a1757a0a45bcd99fa044ff43fe3bb6f226195b42231b95d97d0060ab50409"
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
        "BD-08-013-AC001",
        "BD-08-013-AC002",
        "BD-08-013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-013-O001",
      "obligation_text": "Offline Payment yêu cầu Offline Payment Capability"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-013 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-013 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-013 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-013-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-013-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-013 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Offline Payment yêu cầu Offline Payment Capability.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-08-013",
    "source_context_sha256": "390bc97a5dc5aef02224c4396066bd778a8b69ce04c1d4b3adcb26704b8907e9",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "d08a1757a0a45bcd99fa044ff43fe3bb6f226195b42231b95d97d0060ab50409",
    "source_lines": "L2889-L3001",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-013"
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
  "stable_id": "BD-08-013",
  "title": "Offline Payment yêu cầu Offline Payment Capability",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-014 — Payment Success không bao gồm Procurement hoặc Fulfillment

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
      "requirement_id": "BD-08-014",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "0aefdd92f5dc76b7cd99153538a386ecb5490dea3f7aefe1910ce8004fd9acb8"
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
        "BD-08-014-AC001",
        "BD-08-014-AC002",
        "BD-08-014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-014-O001",
      "obligation_text": "Payment Success không bao gồm Procurement hoặc Fulfillment"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-014 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-014-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-014-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-014 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Payment Success không bao gồm Procurement hoặc Fulfillment.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-014",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-08-014",
    "source_context_sha256": "8bb7c58b41ec190146a9868b0f0bedc9a16cae5bc5cd2f99e65fdc786ecc15eb",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "0aefdd92f5dc76b7cd99153538a386ecb5490dea3f7aefe1910ce8004fd9acb8",
    "source_lines": "L3003-L3111",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-014"
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
  "stable_id": "BD-08-014",
  "title": "Payment Success không bao gồm Procurement hoặc Fulfillment",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-015 — Refund là Business Object độc lập

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
      "requirement_id": "BD-08-015",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "f93ce798e98485d5b5806a6d4513ce8ffe0ea41ad39f30226b0f006198ad9b7a"
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
        "BD-08-015-AC001",
        "BD-08-015-AC002",
        "BD-08-015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-015-O001",
      "obligation_text": "Refund là Business Object độc lập"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-015-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-015 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-015 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-015-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-015-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-015 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Refund là Business Object độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-015",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Refund",
    "source_context_sha256": "25d0833c3baff25db0c2b3f2babcf535a41968c879657577fe597908e458b2ca",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "f93ce798e98485d5b5806a6d4513ce8ffe0ea41ad39f30226b0f006198ad9b7a",
    "source_lines": "L3113-L3223",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-015"
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
  "stable_id": "BD-08-015",
  "title": "Refund là Business Object độc lập",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-016 — Payment Notification tách biệt Fulfillment Notification

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
      "requirement_id": "BD-08-016",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "04a802bc153f1244bf0f5830ab9716f44ec6c25f0eb9f2a0ce71c3b2453a44c7"
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
        "BD-08-016-AC001",
        "BD-08-016-AC002",
        "BD-08-016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-016-O001",
      "obligation_text": "Payment Notification tách biệt Fulfillment Notification"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-016 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-016 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-016 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-016-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-016-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-016 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Payment Notification tách biệt Fulfillment Notification.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-016",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-08-016",
    "source_context_sha256": "8157fe4e1b665bc07bad1df2990b01fcee096303b416f5ba0d0fcc1e53ec61b2",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "04a802bc153f1244bf0f5830ab9716f44ec6c25f0eb9f2a0ce71c3b2453a44c7",
    "source_lines": "L3225-L3333",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-016"
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
  "stable_id": "BD-08-016",
  "title": "Payment Notification tách biệt Fulfillment Notification",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-017 — PaymentSession lưu Risk Metadata

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "A PaymentSession with no applicable risk signal records the governed no-signal result rather than invented metadata"
    ],
    "concrete_bindings": [
      {
        "actual_set": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-017",
            "source_type": "SOURCE_LITERAL",
            "version": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41"
          },
          "identifier": "RESOLVED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BD-08-017.RESOLVED.COLLECTION",
          "origin": {
            "origin_id": "YSIM.BD-08-017.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [
              "BDD-26",
              "SD-03"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
            "source_lines": "L630-L633",
            "source_section": "23. Business Decisions (Locked) > BD-08-017"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "OBSERVE.BD-08-017.RESOLVED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
        },
        "required_members": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-017",
            "source_type": "SOURCE_LITERAL",
            "version": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41"
          },
          "identifier": "GOVERNED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BD-08-017.GOVERNED.COLLECTION",
          "origin": {
            "origin_id": "BD-08-017.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "BDD-26",
              "SD-03"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
            "source_lines": "L630-L633",
            "source_section": "23. Business Decisions (Locked) > BD-08-017"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "RESOLVE.BD-08-017.GOVERNED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BD-08-017",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Applicable Risk Metadata is missing or detached from the PaymentSession"
    ],
    "operator_composition": [
      "SET_CONTAINS"
    ],
    "positive_oracle": [
      "The PaymentSession retains the applicable Risk Metadata"
    ],
    "provenance": {
      "approved_decision_references": [
        "BDD-26",
        "SD-03"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
      "source_lines": "L630-L633",
      "source_section": "23. Business Decisions (Locked) > BD-08-017"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-017",
          "source_type": "SOURCE_LITERAL",
          "version": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41"
        },
        "identifier": "BD-08-017.BD-08-017.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BD-08-017.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "BDD-26",
            "SD-03"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-08.md",
          "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
          "source_lines": "L630-L633",
          "source_section": "23. Business Decisions (Locked) > BD-08-017"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BD-08-017.BD-08-017.BD-08-017.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BD-08-017.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.PAYMENT_SESSION_ID",
        "FIELD.RISK_RULE_ID",
        "FIELD.RISK_SIGNAL_REFS",
        "FIELD.RISK_RESULT",
        "FIELD.RISK_METADATA_VERSION",
        "FIELD.AUDIT_RECORD"
      ],
      "producer": "BD-08-017.EVIDENCE.PRODUCER",
      "required_collection_origin": "BD-08-017.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.PAYMENT_SESSION_ID",
        "FIELD.RISK_RULE_ID",
        "FIELD.RISK_SIGNAL_REFS",
        "FIELD.RISK_RESULT",
        "FIELD.RISK_METADATA_VERSION",
        "FIELD.AUDIT_RECORD"
      ],
      "required_values_or_hashes": [
        "BD-08-017.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BD-08-017.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BD-08-017.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BD-08-017-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BD-08-017.O1.1.SET_CONTAINS",
          "evaluator_consumed_bindings": [
            "actual_set",
            "required_members"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-017",
              "source_type": "SOURCE_LITERAL",
              "version": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41"
            },
            "identifier": "BD-08-017.BD-08-017.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-08-017.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "BDD-26",
                "SD-03"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
              "source_lines": "L630-L633",
              "source_section": "23. Business Decisions (Locked) > BD-08-017"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-08-017.BD-08-017.BD-08-017.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-08-017.BD-08-017.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-017",
                  "source_type": "SOURCE_LITERAL",
                  "version": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41"
                },
                "identifier": "BD-08-017.BD-08-017.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-08-017.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "BDD-26",
                    "SD-03"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
                  "source_lines": "L630-L633",
                  "source_section": "23. Business Decisions (Locked) > BD-08-017"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BD-08-017.BD-08-017.BD-08-017.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BD-08-017.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "BDD-26",
                "SD-03"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
              "source_lines": "L630-L633",
              "source_section": "23. Business Decisions (Locked) > BD-08-017"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_set": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-017",
                  "source_type": "SOURCE_LITERAL",
                  "version": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41"
                },
                "identifier": "RESOLVED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BD-08-017.RESOLVED.COLLECTION",
                "origin": {
                  "origin_id": "YSIM.BD-08-017.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "BDD-26",
                    "SD-03"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
                  "source_lines": "L630-L633",
                  "source_section": "23. Business Decisions (Locked) > BD-08-017"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "OBSERVE.BD-08-017.RESOLVED_MEMBER_COLLECTION",
                  "version": "1.0.0"
                },
                "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
              },
              "required_members": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-017",
                  "source_type": "SOURCE_LITERAL",
                  "version": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41"
                },
                "identifier": "GOVERNED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BD-08-017.GOVERNED.COLLECTION",
                "origin": {
                  "origin_id": "BD-08-017.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "BDD-26",
                    "SD-03"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
                  "source_lines": "L630-L633",
                  "source_section": "23. Business Decisions (Locked) > BD-08-017"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "RESOLVE.BD-08-017.GOVERNED_MEMBER_COLLECTION",
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
                        "BD-08-017.BD-08-017.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-017",
                      "source_type": "SOURCE_LITERAL",
                      "version": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41"
                    },
                    "identifier": "BD-08-017.BD-08-017.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-08-017.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "BDD-26",
                        "SD-03"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-08.md",
                      "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
                      "source_lines": "L630-L633",
                      "source_section": "23. Business Decisions (Locked) > BD-08-017"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-08-017.BD-08-017.BD-08-017.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BD-08-017.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "BDD-26",
                    "SD-03"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
                  "source_lines": "L630-L633",
                  "source_section": "23. Business Decisions (Locked) > BD-08-017"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "observed": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BD-08-017.BD-08-017.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-017",
                      "source_type": "SOURCE_LITERAL",
                      "version": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41"
                    },
                    "identifier": "BD-08-017.BD-08-017.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-08-017.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "BDD-26",
                        "SD-03"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-08.md",
                      "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
                      "source_lines": "L630-L633",
                      "source_section": "23. Business Decisions (Locked) > BD-08-017"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "OBSERVE.BD-08-017.BD-08-017.BD-08-017.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BD-08-017.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "BDD-26",
                    "SD-03"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
                  "source_lines": "L630-L633",
                  "source_section": "23. Business Decisions (Locked) > BD-08-017"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-017",
                "source_type": "SOURCE_LITERAL",
                "version": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41"
              },
              "identifier": "BD-08-017.BD-08-017.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-08-017.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "BDD-26",
                  "SD-03"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
                "source_lines": "L630-L633",
                "source_section": "23. Business Decisions (Locked) > BD-08-017"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-08-017.BD-08-017.BD-08-017.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "SET_CONTAINS"
          },
          "obligation_id": "BD-08-017-O001",
          "observed_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-08-017.BD-08-017.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-017",
                  "source_type": "SOURCE_LITERAL",
                  "version": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41"
                },
                "identifier": "BD-08-017.BD-08-017.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-08-017.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "BDD-26",
                    "SD-03"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
                  "source_lines": "L630-L633",
                  "source_section": "23. Business Decisions (Locked) > BD-08-017"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BD-08-017.BD-08-017.BD-08-017.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BD-08-017.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "BDD-26",
                "SD-03"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
              "source_lines": "L630-L633",
              "source_section": "23. Business Decisions (Locked) > BD-08-017"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "operator_id": "SET_CONTAINS",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_set": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-017",
                "source_type": "SOURCE_LITERAL",
                "version": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41"
              },
              "identifier": "RESOLVED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BD-08-017.RESOLVED.COLLECTION",
              "origin": {
                "origin_id": "YSIM.BD-08-017.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [
                  "BDD-26",
                  "SD-03"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
                "source_lines": "L630-L633",
                "source_section": "23. Business Decisions (Locked) > BD-08-017"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "OBSERVE.BD-08-017.RESOLVED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
            },
            "required_members": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-017",
                "source_type": "SOURCE_LITERAL",
                "version": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41"
              },
              "identifier": "GOVERNED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BD-08-017.GOVERNED.COLLECTION",
              "origin": {
                "origin_id": "BD-08-017.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "BDD-26",
                  "SD-03"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
                "source_lines": "L630-L633",
                "source_section": "23. Business Decisions (Locked) > BD-08-017"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "RESOLVE.BD-08-017.GOVERNED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
            }
          }
        }
      ],
      "boundary_cases": [
        "A PaymentSession with no applicable risk signal records the governed no-signal result rather than invented metadata"
      ],
      "contract_ast_sha256": "46cc962b3309c9a96bf7bda660261e1ac7c9af0fa7ff9653a8a4d9e305c66c89",
      "contract_id": "P2C.C4.CONTRACT.BD-08-017",
      "criticality": "CRITICAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#23. Business Decisions (Locked) > BD-08-017",
            "source_type": "SOURCE_LITERAL",
            "version": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41"
          },
          "identifier": "BD-08-017.BD-08-017.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-08-017.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "BDD-26",
              "SD-03"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
            "source_lines": "L630-L633",
            "source_section": "23. Business Decisions (Locked) > BD-08-017"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BD-08-017.BD-08-017.BD-08-017.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BD-08-017.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.PAYMENT_SESSION_ID",
          "FIELD.RISK_RULE_ID",
          "FIELD.RISK_SIGNAL_REFS",
          "FIELD.RISK_RESULT",
          "FIELD.RISK_METADATA_VERSION",
          "FIELD.AUDIT_RECORD"
        ],
        "producer": "BD-08-017.EVIDENCE.PRODUCER",
        "required_collection_origin": "BD-08-017.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.PAYMENT_SESSION_ID",
          "FIELD.RISK_RULE_ID",
          "FIELD.RISK_SIGNAL_REFS",
          "FIELD.RISK_RESULT",
          "FIELD.RISK_METADATA_VERSION",
          "FIELD.AUDIT_RECORD"
        ],
        "required_values_or_hashes": [
          "BD-08-017.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BD-08-017.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BD-08-017.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-R2-FX-5BB956611A8310831791",
        "P2C-C4-R2-FX-C541D7BC20677210AAFF",
        "P2C-C4-R2-FX-029AED71F3DBCF8C184D"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Applicable Risk Metadata is missing or detached from the PaymentSession"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-08-017-O001",
          "obligation_text": "PaymentSession lưu Risk Metadata"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BD-08-017.O1.1.SET_CONTAINS"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-08-017-O001"
        }
      ],
      "operator_composition": [
        "SET_CONTAINS"
      ],
      "positive_oracles": [
        "The PaymentSession retains the applicable Risk Metadata"
      ],
      "preconditions": [
        "The PaymentSession and evaluated risk evidence are identified"
      ],
      "prohibitions": [
        "Applicable Risk Metadata is missing or detached from the PaymentSession"
      ],
      "requirement_id": "BD-08-017",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "BDD-26",
          "SD-03"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-08.md",
        "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
        "source_lines": "L630-L633",
        "source_section": "23. Business Decisions (Locked) > BD-08-017"
      },
      "source_statement": "PaymentSession lưu Risk Metadata.",
      "surrounding_source_context": "## BD-08-017\n\nPaymentSession lưu Risk Metadata.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BD-08-017",
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
        "BD-08-017-AC001",
        "BD-08-017-AC002",
        "BD-08-017-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-017-O001",
      "obligation_text": "PaymentSession lưu Risk Metadata"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-017 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-017 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-017 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-017-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-08-017-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-08-017 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "PaymentSession lưu Risk Metadata.",
  "provenance": {
    "approved_decisions": [
      "BDD-26",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-08-017",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-08-017",
    "source_context_sha256": "186b3eebbbcd342cfa4c4abd26a0b05d5eb26bab1d101b1e45e50bc88433313f",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "8e58333317287748470cf586b093fd4aca4d6c9f5a55d197a2c7bd324a2d33b9",
    "source_lines": "L3335-L4229",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-08-017"
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
  "stable_id": "BD-08-017",
  "title": "PaymentSession lưu Risk Metadata",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-08-R002 — Trong Version 2.0: PaymentOwner không được thay đổi sau khi PaymentSession được tạo

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
      "requirement_id": "BRD-WS-08-R002",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "2e0d46ad718e1519ac608453910bea4dca0ff7434aafc063964f1011ee18fbf6"
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
        "BRD-WS-08-R002-AC001",
        "BRD-WS-08-R002-AC002",
        "BRD-WS-08-R002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R002-O001",
      "obligation_text": "Trong Version 2.0: PaymentOwner không được thay đổi sau khi PaymentSession được tạo"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R002 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R002-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R002-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R002 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Trong Version 2.0: PaymentOwner không được thay đổi sau khi PaymentSession được tạo.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-08-002",
    "previous_temporary_key": "TMP-BRD-WS-08-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Payment Owner",
    "source_context_sha256": "d66fa58ef3786b25e98e8867a9f8aa4b327df523f28370ac1eaa41dddd5cf2c5",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "2e0d46ad718e1519ac608453910bea4dca0ff7434aafc063964f1011ee18fbf6",
    "source_lines": "L4231-L4339",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-08-R002"
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
  "stable_id": "BRD-WS-08-R002",
  "title": "Trong Version 2.0: PaymentOwner không được thay đổi sau khi PaymentSession được tạo",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-08-R003 — Đối với Offline Payment: - PaymentOwner vẫn là Organization nhận tiền. - Sales chỉ được phép xác…

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
      "requirement_id": "BRD-WS-08-R003",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "f23c02995911fdefe35ffe00b7bcf12788b1c202365ccfbd0d69349ada423ed9"
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
        "BRD-WS-08-R003-AC001",
        "BRD-WS-08-R003-AC003",
        "BRD-WS-08-R003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R003-O001",
      "obligation_text": "Đối với Offline Payment: PaymentOwner vẫn là Organization nhận tiền"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-08-R003-AC002",
        "BRD-WS-08-R003-AC003",
        "BRD-WS-08-R003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R003-O002",
      "obligation_text": "Đối với Offline Payment: Sales chỉ được phép xác nhận thanh toán nếu có Offline Payment Capability"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R003 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R003-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R003-AC001",
        "BRD-WS-08-R003-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R003 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Đối với Offline Payment: - PaymentOwner vẫn là Organization nhận tiền. - Sales chỉ được phép xác nhận thanh toán nếu có Offline Payment Capability.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-08-003",
    "previous_temporary_key": "TMP-BRD-WS-08-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Payment Owner",
    "source_context_sha256": "d66fa58ef3786b25e98e8867a9f8aa4b327df523f28370ac1eaa41dddd5cf2c5",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "f23c02995911fdefe35ffe00b7bcf12788b1c202365ccfbd0d69349ada423ed9",
    "source_lines": "L4341-L4464",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-08-R003"
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
  "stable_id": "BRD-WS-08-R003",
  "title": "Đối với Offline Payment: - PaymentOwner vẫn là Organization nhận tiền. - Sales chỉ được phép xác…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-08-R004 — Trong Payment Lifecycle, Gateway luôn sử dụng MerchantAccount tương ứng của PaymentOwner

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "A PaymentOwner with no valid MerchantAccount fails before gateway processing"
    ],
    "concrete_bindings": [
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-08-R004.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                "source_type": "SOURCE_LITERAL",
                "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
              },
              "identifier": "BRD-WS-08-R004.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
            "source_lines": "L151",
            "source_section": "6. Merchant Account"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-08-R004.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                "source_type": "SOURCE_LITERAL",
                "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
              },
              "identifier": "BRD-WS-08-R004.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
            "source_lines": "L151",
            "source_section": "6. Merchant Account"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
            "source_type": "SOURCE_LITERAL",
            "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
          },
          "identifier": "BRD-WS-08-R004.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
            "source_lines": "L151",
            "source_section": "6. Merchant Account"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
            "source_type": "SOURCE_LITERAL",
            "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
          },
          "identifier": "BRD-WS-08-R004.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
            "source_lines": "L151",
            "source_section": "6. Merchant Account"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
            "source_type": "SOURCE_LITERAL",
            "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
          },
          "identifier": "BRD-WS-08-R004.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
            "source_lines": "L151",
            "source_section": "6. Merchant Account"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
            "source_type": "SOURCE_LITERAL",
            "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
          },
          "identifier": "BRD-WS-08-R004.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
            "source_lines": "L151",
            "source_section": "6. Merchant Account"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
            "source_type": "SOURCE_LITERAL",
            "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
          },
          "identifier": "BRD-WS-08-R004.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
            "source_lines": "L151",
            "source_section": "6. Merchant Account"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      },
      {
        "expected_outcome": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-WS-08-R004.POLICY.OUTCOME.CONFORMING"
            ],
            "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
            "source_type": "SOURCE_LITERAL",
            "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
          },
          "identifier": "BRD-WS-08-R004.POLICY.OUTCOME.CONFORMING",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
            "source_lines": "L151",
            "source_section": "6. Merchant Account"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_OUTCOME",
            "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.POLICY.OUTCOME.CONFORMING",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_OUTCOME"
        },
        "policy": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
            "source_type": "SOURCE_LITERAL",
            "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
          },
          "identifier": "BRD-WS-08-R004.POLICY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
            "source_lines": "L151",
            "source_section": "6. Merchant Account"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.POLICY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "policy_inputs": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
            "source_type": "SOURCE_LITERAL",
            "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
          },
          "identifier": "BRD-WS-08-R004.POLICY_INPUTS",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
            "source_lines": "L151",
            "source_section": "6. Merchant Account"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.POLICY_INPUTS",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "policy_version": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
            "source_type": "SOURCE_LITERAL",
            "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
          },
          "identifier": "BRD-WS-08-R004.POLICY_VERSION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
            "source_lines": "L151",
            "source_section": "6. Merchant Account"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_VERSION",
            "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.POLICY_VERSION",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_VERSION"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-08-R004",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Gateway uses another owner's MerchantAccount"
    ],
    "operator_composition": [
      "REFERENCE_TARGET_VALID",
      "POLICY_OUTCOME_EQUALS"
    ],
    "positive_oracle": [
      "Gateway uses the MerchantAccount corresponding to PaymentOwner"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2-DEC-006"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
      "source_lines": "L151",
      "source_section": "6. Merchant Account"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
          "source_type": "SOURCE_LITERAL",
          "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
        },
        "identifier": "BRD-WS-08-R004.BRD-WS-08-R004.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-08-R004.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2-DEC-006"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-08.md",
          "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
          "source_lines": "L151",
          "source_section": "6. Merchant Account"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-08-R004.BRD-WS-08-R004.BRD-WS-08-R004.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-08-R004.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.PAYMENT_ID",
        "FIELD.PAYMENT_OWNER_ID",
        "FIELD.MERCHANT_ACCOUNT_ID",
        "FIELD.GATEWAY_REQUEST",
        "FIELD.SELECTION_RESULT"
      ],
      "producer": "BRD-WS-08-R004.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-08-R004.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.PAYMENT_ID",
        "FIELD.PAYMENT_OWNER_ID",
        "FIELD.MERCHANT_ACCOUNT_ID",
        "FIELD.GATEWAY_REQUEST",
        "FIELD.SELECTION_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-WS-08-R004.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-08-R004.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-08-R004.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-08-R004-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID",
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
              "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
              "source_type": "SOURCE_LITERAL",
              "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
            },
            "identifier": "BRD-WS-08-R004.BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-006"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
              "source_lines": "L151",
              "source_section": "6. Merchant Account"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-08-R004.BRD-WS-08-R004.BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
              "source_type": "SOURCE_LITERAL",
              "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
            },
            "identifier": "BRD-WS-08-R004.BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-006"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
              "source_lines": "L151",
              "source_section": "6. Merchant Account"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                        "BRD-WS-08-R004.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                      "source_type": "SOURCE_LITERAL",
                      "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                    },
                    "identifier": "BRD-WS-08-R004.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-006"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-08.md",
                      "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                      "source_lines": "L151",
                      "source_section": "6. Merchant Account"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-08-R004.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                      "source_type": "SOURCE_LITERAL",
                      "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                    },
                    "identifier": "BRD-WS-08-R004.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-006"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-08.md",
                      "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                      "source_lines": "L151",
                      "source_section": "6. Merchant Account"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                  "source_type": "SOURCE_LITERAL",
                  "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                },
                "identifier": "BRD-WS-08-R004.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                  "source_type": "SOURCE_LITERAL",
                  "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                },
                "identifier": "BRD-WS-08-R004.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                  "source_type": "SOURCE_LITERAL",
                  "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                },
                "identifier": "BRD-WS-08-R004.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                  "source_type": "SOURCE_LITERAL",
                  "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                },
                "identifier": "BRD-WS-08-R004.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                  "source_type": "SOURCE_LITERAL",
                  "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                },
                "identifier": "BRD-WS-08-R004.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                  "source_type": "SOURCE_LITERAL",
                  "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                },
                "identifier": "BRD-WS-08-R004.BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                  "source_type": "SOURCE_LITERAL",
                  "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                },
                "identifier": "BRD-WS-08-R004.BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-08-R004.BRD-WS-08-R004.BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                "source_type": "SOURCE_LITERAL",
                "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
              },
              "identifier": "BRD-WS-08-R004.BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-08-R004.BRD-WS-08-R004.BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "BRD-WS-08-R004-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
              "source_type": "SOURCE_LITERAL",
              "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
            },
            "identifier": "BRD-WS-08-R004.BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-006"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
              "source_lines": "L151",
              "source_section": "6. Merchant Account"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.BRD-WS-08-R004.BRD-WS-08-R004.BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                      "BRD-WS-08-R004.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                    "source_type": "SOURCE_LITERAL",
                    "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                  },
                  "identifier": "BRD-WS-08-R004.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-006"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-08.md",
                    "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                    "source_lines": "L151",
                    "source_section": "6. Merchant Account"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BRD-WS-08-R004.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                    "source_type": "SOURCE_LITERAL",
                    "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                  },
                  "identifier": "BRD-WS-08-R004.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-006"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-08.md",
                    "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                    "source_lines": "L151",
                    "source_section": "6. Merchant Account"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                "source_type": "SOURCE_LITERAL",
                "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
              },
              "identifier": "BRD-WS-08-R004.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                "source_type": "SOURCE_LITERAL",
                "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
              },
              "identifier": "BRD-WS-08-R004.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                "source_type": "SOURCE_LITERAL",
                "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
              },
              "identifier": "BRD-WS-08-R004.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                "source_type": "SOURCE_LITERAL",
                "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
              },
              "identifier": "BRD-WS-08-R004.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                "source_type": "SOURCE_LITERAL",
                "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
              },
              "identifier": "BRD-WS-08-R004.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        },
        {
          "assertion_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS",
          "evaluator_consumed_bindings": [
            "expected_outcome",
            "policy",
            "policy_inputs",
            "policy_version"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
              "source_type": "SOURCE_LITERAL",
              "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
            },
            "identifier": "BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-006"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
              "source_lines": "L151",
              "source_section": "6. Merchant Account"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-08-R004.BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
              "source_type": "SOURCE_LITERAL",
              "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
            },
            "identifier": "BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-006"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
              "source_lines": "L151",
              "source_section": "6. Merchant Account"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
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
                    "BRD-WS-08-R004.POLICY.OUTCOME.CONFORMING"
                  ],
                  "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                  "source_type": "SOURCE_LITERAL",
                  "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                },
                "identifier": "BRD-WS-08-R004.POLICY.OUTCOME.CONFORMING",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.POLICY.OUTCOME.CONFORMING",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "policy": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                  "source_type": "SOURCE_LITERAL",
                  "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                },
                "identifier": "BRD-WS-08-R004.POLICY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.POLICY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "policy_inputs": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                  "source_type": "SOURCE_LITERAL",
                  "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                },
                "identifier": "BRD-WS-08-R004.POLICY_INPUTS",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.POLICY_INPUTS",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "policy_version": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                  "source_type": "SOURCE_LITERAL",
                  "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                },
                "identifier": "BRD-WS-08-R004.POLICY_VERSION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_VERSION",
                  "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.POLICY_VERSION",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_VERSION"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                  "source_type": "SOURCE_LITERAL",
                  "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                },
                "identifier": "BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                  "source_type": "SOURCE_LITERAL",
                  "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
                },
                "identifier": "BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                  "source_lines": "L151",
                  "source_section": "6. Merchant Account"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "OBSERVE.BRD-WS-08-R004.BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                "source_type": "SOURCE_LITERAL",
                "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
              },
              "identifier": "BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-08-R004.BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "POLICY_OUTCOME_EQUALS"
          },
          "obligation_id": "BRD-WS-08-R004-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
              "source_type": "SOURCE_LITERAL",
              "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
            },
            "identifier": "BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-006"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
              "source_lines": "L151",
              "source_section": "6. Merchant Account"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "OBSERVE.BRD-WS-08-R004.BRD-WS-08-R004.BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
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
                  "BRD-WS-08-R004.POLICY.OUTCOME.CONFORMING"
                ],
                "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                "source_type": "SOURCE_LITERAL",
                "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
              },
              "identifier": "BRD-WS-08-R004.POLICY.OUTCOME.CONFORMING",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_OUTCOME",
                "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.POLICY.OUTCOME.CONFORMING",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_OUTCOME"
            },
            "policy": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                "source_type": "SOURCE_LITERAL",
                "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
              },
              "identifier": "BRD-WS-08-R004.POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "policy_inputs": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                "source_type": "SOURCE_LITERAL",
                "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
              },
              "identifier": "BRD-WS-08-R004.POLICY_INPUTS",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.POLICY_INPUTS",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "policy_version": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
                "source_type": "SOURCE_LITERAL",
                "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
              },
              "identifier": "BRD-WS-08-R004.POLICY_VERSION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
                "source_lines": "L151",
                "source_section": "6. Merchant Account"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_VERSION",
                "resolver_id": "RESOLVE.BRD-WS-08-R004.BRD-WS-08-R004.POLICY_VERSION",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_VERSION"
            }
          }
        }
      ],
      "boundary_cases": [
        "A PaymentOwner with no valid MerchantAccount fails before gateway processing"
      ],
      "contract_ast_sha256": "43027ad219b4bbc9cf1e4e6c4459b0d66c376b2cd9e330dbeb8d87003702e90a",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-08-R004",
      "criticality": "CRITICAL",
      "disposition": "OPERATOR_REMAP_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#6. Merchant Account",
            "source_type": "SOURCE_LITERAL",
            "version": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b"
          },
          "identifier": "BRD-WS-08-R004.BRD-WS-08-R004.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-08-R004.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
            "source_lines": "L151",
            "source_section": "6. Merchant Account"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-08-R004.BRD-WS-08-R004.BRD-WS-08-R004.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-08-R004.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.PAYMENT_ID",
          "FIELD.PAYMENT_OWNER_ID",
          "FIELD.MERCHANT_ACCOUNT_ID",
          "FIELD.GATEWAY_REQUEST",
          "FIELD.SELECTION_RESULT"
        ],
        "producer": "BRD-WS-08-R004.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-08-R004.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.PAYMENT_ID",
          "FIELD.PAYMENT_OWNER_ID",
          "FIELD.MERCHANT_ACCOUNT_ID",
          "FIELD.GATEWAY_REQUEST",
          "FIELD.SELECTION_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-WS-08-R004.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-08-R004.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-08-R004.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-52016F0C896B948134DC",
        "P2C-C4-FX-ADC8DC4BECED03CEBE4E",
        "P2C-C4-FX-C10BCA3DB4322D86DF32"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Gateway uses another owner's MerchantAccount"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-08-R004-O001",
          "obligation_text": "Trong Payment Lifecycle, Gateway luôn sử dụng MerchantAccount tương ứng của PaymentOwner"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-08-R004.O1.1.REFERENCE_TARGET_VALID",
            "BRD-WS-08-R004.O1.2.POLICY_OUTCOME_EQUALS"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-08-R004-O001"
        }
      ],
      "operator_composition": [
        "REFERENCE_TARGET_VALID",
        "POLICY_OUTCOME_EQUALS"
      ],
      "positive_oracles": [
        "Gateway uses the MerchantAccount corresponding to PaymentOwner"
      ],
      "preconditions": [
        "PaymentOwner and corresponding MerchantAccount are resolved"
      ],
      "prohibitions": [
        "Gateway uses another owner's MerchantAccount"
      ],
      "requirement_id": "BRD-WS-08-R004",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2-DEC-006"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-08.md",
        "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
        "source_lines": "L151",
        "source_section": "6. Merchant Account"
      },
      "source_statement": "Trong Payment Lifecycle, Gateway luôn sử dụng MerchantAccount tương ứng của PaymentOwner.",
      "surrounding_source_context": "### BRD-WS-08-R004 — Trong Payment Lifecycle, Gateway luôn sử dụng MerchantAccount tương ứng của PaymentOwner"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-08-R004",
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
        "BRD-WS-08-R004-AC001",
        "BRD-WS-08-R004-AC002",
        "BRD-WS-08-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R004-O001",
      "obligation_text": "Trong Payment Lifecycle, Gateway luôn sử dụng MerchantAccount tương ứng của PaymentOwner"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R004 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R004 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Trong Payment Lifecycle, Gateway luôn sử dụng MerchantAccount tương ứng của PaymentOwner.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-08-004",
    "previous_temporary_key": "TMP-BRD-WS-08-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Merchant Account",
    "source_context_sha256": "aa494a2dff62a50d9623529c4e07a13f63064d5bd7030267a5ddfb4baf1aeb35",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "e01668368c4ba04424cb664603e685811326780e58b96803741bc1d90dd3524b",
    "source_lines": "L4466-L6620",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-08-R004"
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
  "stable_id": "BRD-WS-08-R004",
  "title": "Trong Payment Lifecycle, Gateway luôn sử dụng MerchantAccount tương ứng của PaymentOwner",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-08-R005 — Toàn bộ lịch sử PaymentAttempt phải được lưu

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
      "requirement_id": "BRD-WS-08-R005",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "e065597e42dbce97bb5f0f9bdbafd39afca45c366a0c838da99d68aa9a6506a4"
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
        "BRD-WS-08-R005-AC001",
        "BRD-WS-08-R005-AC002",
        "BRD-WS-08-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R005-O001",
      "obligation_text": "Toàn bộ lịch sử PaymentAttempt phải được lưu"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R005 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R005 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ lịch sử PaymentAttempt phải được lưu.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-08-005",
    "previous_temporary_key": "TMP-BRD-WS-08-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Payment Attempt",
    "source_context_sha256": "81a3bab7521a7cc1e31d673c7d0e3076858d205db08720833cd565cc5f794f81",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "e065597e42dbce97bb5f0f9bdbafd39afca45c366a0c838da99d68aa9a6506a4",
    "source_lines": "L6622-L6730",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-08-R005"
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
  "stable_id": "BRD-WS-08-R005",
  "title": "Toàn bộ lịch sử PaymentAttempt phải được lưu",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-08-R006 — Mọi Callback phải được Audit

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
      "requirement_id": "BRD-WS-08-R006",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "e080c2fa4429847bcb9fd0be7cb69de53a6bf5a731fa51d64bfabf02364c7680"
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
        "BRD-WS-08-R006-AC001",
        "BRD-WS-08-R006-AC002",
        "BRD-WS-08-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R006-O001",
      "obligation_text": "Mọi Callback phải được Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R006 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R006-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R006-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R006 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Callback phải được Audit.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-08-006",
    "previous_temporary_key": "TMP-BRD-WS-08-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Payment Callback",
    "source_context_sha256": "772b50470e988ce974487239f2ab6a668575877d6f1e7331d12cda9bc0984013",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "e080c2fa4429847bcb9fd0be7cb69de53a6bf5a731fa51d64bfabf02364c7680",
    "source_lines": "L6732-L6840",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-08-R006"
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
  "stable_id": "BRD-WS-08-R006",
  "title": "Mọi Callback phải được Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-08-R007 — Version 2.0 yêu cầu: Payment Currency phải thuộc Currency đã được khai báo trong PriceBook

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
      "requirement_id": "BRD-WS-08-R007",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "af150e14d999ab514f93415a7cebf8facc5bfc439c4e91bcc1bf9d98a2362578"
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
        "BRD-WS-08-R007-AC001",
        "BRD-WS-08-R007-AC002",
        "BRD-WS-08-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R007-O001",
      "obligation_text": "Version 2.0 yêu cầu: Payment Currency phải thuộc Currency đã được khai báo trong PriceBook"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R007 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R007-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R007-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R007 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Version 2.0 yêu cầu: Payment Currency phải thuộc Currency đã được khai báo trong PriceBook.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-08-007",
    "previous_temporary_key": "TMP-BRD-WS-08-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "14. Multi-Currency Payment",
    "source_context_sha256": "ee1abfc0bf12aca98c026b85eb6afb6311fecc853f3da4f196d04bef63b4af52",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "af150e14d999ab514f93415a7cebf8facc5bfc439c4e91bcc1bf9d98a2362578",
    "source_lines": "L6842-L6950",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-08-R007"
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
  "stable_id": "BRD-WS-08-R007",
  "title": "Version 2.0 yêu cầu: Payment Currency phải thuộc Currency đã được khai báo trong PriceBook",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-08-R008 — Không hỗ trợ đổi Currency trong PaymentSession

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-08-R008",
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
  "normative_statement": "Không hỗ trợ đổi Currency trong PaymentSession.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-08-008",
    "previous_temporary_key": "TMP-BRD-WS-08-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "14. Multi-Currency Payment",
    "source_context_sha256": "ee1abfc0bf12aca98c026b85eb6afb6311fecc853f3da4f196d04bef63b4af52",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "50f33d938e69fd48869650acc7403be7b96b71586df400c1640b26af251919c2",
    "source_lines": "L6952-L7010",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-08-R008"
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
  "stable_id": "BRD-WS-08-R008",
  "title": "Không hỗ trợ đổi Currency trong PaymentSession",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-08-R010 — Để Payment thành công: Sales phải có

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
      "requirement_id": "BRD-WS-08-R010",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "d7fc3820ed6cd4d0c47feccf0137df852ba231716a4ceac0271cd22a7942eb72"
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
        "BRD-WS-08-R010-AC001",
        "BRD-WS-08-R010-AC002",
        "BRD-WS-08-R010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R010-O001",
      "obligation_text": "Để Payment thành công: Sales phải có"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R010 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R010 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R010 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R010-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R010-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R010 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Để Payment thành công: Sales phải có:",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-08-010",
    "previous_temporary_key": "TMP-BRD-WS-08-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Offline Payment",
    "source_context_sha256": "669ce2aeaf92671d7f7a06e2b69f6a4e81b90a0e9c71ae2178ef2ddd497c1736",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "d7fc3820ed6cd4d0c47feccf0137df852ba231716a4ceac0271cd22a7942eb72",
    "source_lines": "L7012-L7120",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-08-R010"
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
  "stable_id": "BRD-WS-08-R010",
  "title": "Để Payment thành công: Sales phải có",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-08-R011 — Sales phải xác nhận: Đã nhận thanh toán

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
      "requirement_id": "BRD-WS-08-R011",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "3d863b8520be3ce77d5e86ea7f89b6fbe8752e11e8a2f74d4533d5b7c4f5471e"
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
        "BRD-WS-08-R011-AC001",
        "BRD-WS-08-R011-AC002",
        "BRD-WS-08-R011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R011-O001",
      "obligation_text": "Sales phải xác nhận: Đã nhận thanh toán"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R011 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R011 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R011 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R011-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R011-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R011 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sales phải xác nhận: Đã nhận thanh toán.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-08-011",
    "previous_temporary_key": "TMP-BRD-WS-08-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Offline Payment",
    "source_context_sha256": "669ce2aeaf92671d7f7a06e2b69f6a4e81b90a0e9c71ae2178ef2ddd497c1736",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "3d863b8520be3ce77d5e86ea7f89b6fbe8752e11e8a2f74d4533d5b7c4f5471e",
    "source_lines": "L7122-L7230",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-08-R011"
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
  "stable_id": "BRD-WS-08-R011",
  "title": "Sales phải xác nhận: Đã nhận thanh toán",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-08-R012 — Deferred ML fraud scoring

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-08-R012",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-020",
      "selected_disposition": "APPROVED_SCOPE_PROMOTION_REMEDIATION"
    }
  ],
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "ML scoring cho Fraud/Risk Engine được hoãn sang sau v2.3.",
  "provenance": {
    "approved_decisions": [
      "BDD-26",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-08-012",
    "previous_temporary_key": "TMP-BRD-WS-08-012",
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Payment Security",
    "source_context_sha256": "30a7109a401c637339457ea6dd0b6a1d386a48422f78b16d0e4e5fd841abb3d0",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "faffd0dea0a019685990eac28cf703b1a8886f04facada463ec6a264058e069c",
    "source_lines": "L7232-L7305",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-08-R012"
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
  "stable_id": "BRD-WS-08-R012",
  "title": "Deferred ML fraud scoring",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-08-R013 — Active rule-based Fraud/Risk Engine

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-26",
        "SD-03"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-08-R013",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "534fa8b9244f0354810be24c6528d558a2350061ba0ddb09125160ec06d38416"
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
        "BRD-WS-08-R013-AC001",
        "BRD-WS-08-R013-AC003",
        "BRD-WS-08-R013-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R013-O001",
      "obligation_text": "Trong v2.3, Fraud/Risk Engine phải áp dụng rule-based risk cho authentication/account, checkout và payment"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-08-R013-AC002",
        "BRD-WS-08-R013-AC003",
        "BRD-WS-08-R013-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R013-O002",
      "obligation_text": "quyết định tối thiểu gồm ALLOW, CHALLENGE, BLOCK và REVIEW, đồng thời rule, signal, reason, override và audit phải được versioning"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R013-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R013 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R013 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R013-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-08-R013-AC001",
        "BRD-WS-08-R013-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-08-R013 does not define a recovery obligation."
    }
  },
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-020",
      "selected_disposition": "APPROVED_SCOPE_PROMOTION_REMEDIATION"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Trong v2.3, Fraud/Risk Engine phải áp dụng rule-based risk cho authentication/account, checkout và payment; quyết định tối thiểu gồm ALLOW, CHALLENGE, BLOCK và REVIEW, đồng thời rule, signal, reason, override và audit phải được versioning.",
  "provenance": {
    "allocation_contract": "FRAUD_RISK_ACTIVE_DEFERRED_SPLIT",
    "approved_decisions": [
      "BDD-26",
      "SD-03"
    ],
    "identity_origin": "PHASE_2C_NEW_ALLOCATION",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Payment Security",
    "source_context_sha256": "30a7109a401c637339457ea6dd0b6a1d386a48422f78b16d0e4e5fd841abb3d0",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "534fa8b9244f0354810be24c6528d558a2350061ba0ddb09125160ec06d38416",
    "source_lines": "L7307-L7444",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-08-R013"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-WS-08-R012"
    ],
    "derived_requirements": []
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-08-R013",
  "title": "Active rule-based Fraud/Risk Engine",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-08-001 — Payment Domain độc lập với Commercial Domain và Fulfillment Domain

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
      "requirement_id": "EP-08-001",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "49ae5df31bbcd884d5d46fbd5304a0e8d9d5372d3adbbf5d49beb67b802da0fa"
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
        "EP-08-001-AC001",
        "EP-08-001-AC002",
        "EP-08-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-08-001-O001",
      "obligation_text": "Payment Domain độc lập với Commercial Domain và Fulfillment Domain"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-001-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-001 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-001 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-001-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-001-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-001 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Payment Domain độc lập với Commercial Domain và Fulfillment Domain.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-08-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-08-001",
    "source_context_sha256": "42104cacd5e4789df9db049a2938e833232847bce876218c39137566166645ba",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "49ae5df31bbcd884d5d46fbd5304a0e8d9d5372d3adbbf5d49beb67b802da0fa",
    "source_lines": "L7446-L7556",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-08-001"
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
  "stable_id": "EP-08-001",
  "title": "Payment Domain độc lập với Commercial Domain và Fulfillment Domain",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-08-002 — PaymentGateway và MerchantAccount là hai Business Object độc lập

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-08-002",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "cc0e6be38dd34f08c1c6051526a06771d6f0f68153bb435a37d29ba11b1dba1f"
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
        "EP-08-002-AC001",
        "EP-08-002-AC002",
        "EP-08-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-08-002-O001",
      "obligation_text": "PaymentGateway và MerchantAccount là hai Business Object độc lập"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-002-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-002-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-002-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-002 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "PaymentGateway và MerchantAccount là hai Business Object độc lập.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-08-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-08-002",
    "source_context_sha256": "cb8a763ff4d65e4fa8e084301b66a41d616e3b2f5e65f305cd5fb0663bd55551",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "cc0e6be38dd34f08c1c6051526a06771d6f0f68153bb435a37d29ba11b1dba1f",
    "source_lines": "L7558-L7672",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-08-002"
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
  "stable_id": "EP-08-002",
  "title": "PaymentGateway và MerchantAccount là hai Business Object độc lập",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-08-003 — PaymentMethod không phụ thuộc PaymentGateway

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-08-003",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "aaa8aea0650cb8d623e92b35f00cd31c0be28bae7a47a4d1fd9dc4523ba0bb9d"
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
        "EP-08-003-AC001",
        "EP-08-003-AC002",
        "EP-08-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-08-003-O001",
      "obligation_text": "PaymentMethod không phụ thuộc PaymentGateway"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-003 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-003 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "PaymentMethod không phụ thuộc PaymentGateway.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-08-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-08-003",
    "source_context_sha256": "c907c757e79bd3840f6be23171a660998cecdf6f5c96c1157bd8eafb40566f1f",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "aaa8aea0650cb8d623e92b35f00cd31c0be28bae7a47a4d1fd9dc4523ba0bb9d",
    "source_lines": "L7674-L7786",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-08-003"
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
  "stable_id": "EP-08-003",
  "title": "PaymentMethod không phụ thuộc PaymentGateway",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-08-004 — Payment Success chỉ xác nhận việc nhận tiền thành công

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Separate downstream states may follow success without changing its payment meaning"
    ],
    "concrete_bindings": [
      {
        "expected_outcome": {
          "authoritative_source": {
            "allowed_identifiers": [
              "EP-08-004.POLICY.OUTCOME.CONFORMING"
            ],
            "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
            "source_type": "SOURCE_LITERAL",
            "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
          },
          "identifier": "EP-08-004.POLICY.OUTCOME.CONFORMING",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
            "source_lines": "L656-L659",
            "source_section": "24. Enterprise Design Principles > EP-08-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_OUTCOME",
            "resolver_id": "RESOLVE.EP-08-004.EP-08-004.POLICY.OUTCOME.CONFORMING",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_OUTCOME"
        },
        "policy": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
            "source_type": "SOURCE_LITERAL",
            "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
          },
          "identifier": "EP-08-004.POLICY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
            "source_lines": "L656-L659",
            "source_section": "24. Enterprise Design Principles > EP-08-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.EP-08-004.EP-08-004.POLICY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "policy_inputs": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
            "source_type": "SOURCE_LITERAL",
            "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
          },
          "identifier": "EP-08-004.POLICY_INPUTS",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
            "source_lines": "L656-L659",
            "source_section": "24. Enterprise Design Principles > EP-08-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "RESOLVE.EP-08-004.EP-08-004.POLICY_INPUTS",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "policy_version": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
            "source_type": "SOURCE_LITERAL",
            "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
          },
          "identifier": "EP-08-004.POLICY_VERSION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
            "source_lines": "L656-L659",
            "source_section": "24. Enterprise Design Principles > EP-08-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_VERSION",
            "resolver_id": "RESOLVE.EP-08-004.EP-08-004.POLICY_VERSION",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_VERSION"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.EP-08-004",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Payment Success is used as proof of fulfillment, delivery or another later obligation"
    ],
    "operator_composition": [
      "POLICY_OUTCOME_EQUALS"
    ],
    "positive_oracle": [
      "Payment Success asserts only successful receipt of money"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
      "source_lines": "L656-L659",
      "source_section": "24. Enterprise Design Principles > EP-08-004"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
          "source_type": "SOURCE_LITERAL",
          "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
        },
        "identifier": "EP-08-004.EP-08-004.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "EP-08-004.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-08.md",
          "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
          "source_lines": "L656-L659",
          "source_section": "24. Enterprise Design Principles > EP-08-004"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.EP-08-004.EP-08-004.EP-08-004.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "EP-08-004.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.PAYMENT_ID",
        "FIELD.RECEIPT_CONFIRMATION",
        "FIELD.PAYMENT_STATE",
        "FIELD.DOWNSTREAM_STATES",
        "FIELD.TRANSITION_TIME"
      ],
      "producer": "EP-08-004.EVIDENCE.PRODUCER",
      "required_collection_origin": "EP-08-004.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.PAYMENT_ID",
        "FIELD.RECEIPT_CONFIRMATION",
        "FIELD.PAYMENT_STATE",
        "FIELD.DOWNSTREAM_STATES",
        "FIELD.TRANSITION_TIME"
      ],
      "required_values_or_hashes": [
        "EP-08-004.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "EP-08-004.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "EP-08-004.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "EP-08-004-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS",
          "evaluator_consumed_bindings": [
            "expected_outcome",
            "policy",
            "policy_inputs",
            "policy_version"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
              "source_type": "SOURCE_LITERAL",
              "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
            },
            "identifier": "EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
              "source_lines": "L656-L659",
              "source_section": "24. Enterprise Design Principles > EP-08-004"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.EP-08-004.EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
              "source_type": "SOURCE_LITERAL",
              "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
            },
            "identifier": "EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
              "source_lines": "L656-L659",
              "source_section": "24. Enterprise Design Principles > EP-08-004"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "RESOLVE.EP-08-004.EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
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
                    "EP-08-004.POLICY.OUTCOME.CONFORMING"
                  ],
                  "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
                },
                "identifier": "EP-08-004.POLICY.OUTCOME.CONFORMING",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
                  "source_lines": "L656-L659",
                  "source_section": "24. Enterprise Design Principles > EP-08-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.EP-08-004.EP-08-004.POLICY.OUTCOME.CONFORMING",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "policy": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
                },
                "identifier": "EP-08-004.POLICY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
                  "source_lines": "L656-L659",
                  "source_section": "24. Enterprise Design Principles > EP-08-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.EP-08-004.EP-08-004.POLICY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "policy_inputs": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
                },
                "identifier": "EP-08-004.POLICY_INPUTS",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
                  "source_lines": "L656-L659",
                  "source_section": "24. Enterprise Design Principles > EP-08-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.EP-08-004.EP-08-004.POLICY_INPUTS",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "policy_version": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
                },
                "identifier": "EP-08-004.POLICY_VERSION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
                  "source_lines": "L656-L659",
                  "source_section": "24. Enterprise Design Principles > EP-08-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_VERSION",
                  "resolver_id": "RESOLVE.EP-08-004.EP-08-004.POLICY_VERSION",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_VERSION"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
                },
                "identifier": "EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
                  "source_lines": "L656-L659",
                  "source_section": "24. Enterprise Design Principles > EP-08-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.EP-08-004.EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
                },
                "identifier": "EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
                  "source_lines": "L656-L659",
                  "source_section": "24. Enterprise Design Principles > EP-08-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "OBSERVE.EP-08-004.EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
                "source_type": "SOURCE_LITERAL",
                "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
              },
              "identifier": "EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
                "source_lines": "L656-L659",
                "source_section": "24. Enterprise Design Principles > EP-08-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.EP-08-004.EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "POLICY_OUTCOME_EQUALS"
          },
          "obligation_id": "EP-08-004-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
              "source_type": "SOURCE_LITERAL",
              "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
            },
            "identifier": "EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
              "source_lines": "L656-L659",
              "source_section": "24. Enterprise Design Principles > EP-08-004"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "OBSERVE.EP-08-004.EP-08-004.EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
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
                  "EP-08-004.POLICY.OUTCOME.CONFORMING"
                ],
                "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
                "source_type": "SOURCE_LITERAL",
                "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
              },
              "identifier": "EP-08-004.POLICY.OUTCOME.CONFORMING",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
                "source_lines": "L656-L659",
                "source_section": "24. Enterprise Design Principles > EP-08-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_OUTCOME",
                "resolver_id": "RESOLVE.EP-08-004.EP-08-004.POLICY.OUTCOME.CONFORMING",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_OUTCOME"
            },
            "policy": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
                "source_type": "SOURCE_LITERAL",
                "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
              },
              "identifier": "EP-08-004.POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
                "source_lines": "L656-L659",
                "source_section": "24. Enterprise Design Principles > EP-08-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.EP-08-004.EP-08-004.POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "policy_inputs": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
                "source_type": "SOURCE_LITERAL",
                "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
              },
              "identifier": "EP-08-004.POLICY_INPUTS",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
                "source_lines": "L656-L659",
                "source_section": "24. Enterprise Design Principles > EP-08-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "RESOLVE.EP-08-004.EP-08-004.POLICY_INPUTS",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "policy_version": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
                "source_type": "SOURCE_LITERAL",
                "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
              },
              "identifier": "EP-08-004.POLICY_VERSION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
                "source_lines": "L656-L659",
                "source_section": "24. Enterprise Design Principles > EP-08-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_VERSION",
                "resolver_id": "RESOLVE.EP-08-004.EP-08-004.POLICY_VERSION",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_VERSION"
            }
          }
        }
      ],
      "boundary_cases": [
        "Separate downstream states may follow success without changing its payment meaning"
      ],
      "contract_ast_sha256": "8000966a2340fade8e7938ad2f11093e0c9e4407075a7e4c51f87e08272d9a41",
      "contract_id": "P2C.C4.CONTRACT.EP-08-004",
      "criticality": "CRITICAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-08.md#24. Enterprise Design Principles > EP-08-004",
            "source_type": "SOURCE_LITERAL",
            "version": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d"
          },
          "identifier": "EP-08-004.EP-08-004.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-004.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
            "source_lines": "L656-L659",
            "source_section": "24. Enterprise Design Principles > EP-08-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.EP-08-004.EP-08-004.EP-08-004.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "EP-08-004.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.PAYMENT_ID",
          "FIELD.RECEIPT_CONFIRMATION",
          "FIELD.PAYMENT_STATE",
          "FIELD.DOWNSTREAM_STATES",
          "FIELD.TRANSITION_TIME"
        ],
        "producer": "EP-08-004.EVIDENCE.PRODUCER",
        "required_collection_origin": "EP-08-004.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.PAYMENT_ID",
          "FIELD.RECEIPT_CONFIRMATION",
          "FIELD.PAYMENT_STATE",
          "FIELD.DOWNSTREAM_STATES",
          "FIELD.TRANSITION_TIME"
        ],
        "required_values_or_hashes": [
          "EP-08-004.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "EP-08-004.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "EP-08-004.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-4046FA5C5CDCA4CF2B25",
        "P2C-C4-FX-3015DCD1311D50F62C9C",
        "P2C-C4-FX-001F10639B991EFDE567"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Payment Success is used as proof of fulfillment, delivery or another later obligation"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "EP-08-004-O001",
          "obligation_text": "Payment Success chỉ xác nhận việc nhận tiền thành công"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "EP-08-004.O1.1.POLICY_OUTCOME_EQUALS"
          ],
          "coverage_count": 1,
          "obligation_id": "EP-08-004-O001"
        }
      ],
      "operator_composition": [
        "POLICY_OUTCOME_EQUALS"
      ],
      "positive_oracles": [
        "Payment Success asserts only successful receipt of money"
      ],
      "preconditions": [
        "Receipt of funds is confirmed"
      ],
      "prohibitions": [
        "Payment Success is used as proof of fulfillment, delivery or another later obligation"
      ],
      "requirement_id": "EP-08-004",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-08.md",
        "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
        "source_lines": "L656-L659",
        "source_section": "24. Enterprise Design Principles > EP-08-004"
      },
      "source_statement": "Payment Success chỉ xác nhận việc nhận tiền thành công.",
      "surrounding_source_context": "## EP-08-004\n\nPayment Success chỉ xác nhận việc nhận tiền thành công.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.EP-08-004",
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
        "EP-08-004-AC001",
        "EP-08-004-AC002",
        "EP-08-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-08-004-O001",
      "obligation_text": "Payment Success chỉ xác nhận việc nhận tiền thành công"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-004 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-004 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Payment Success chỉ xác nhận việc nhận tiền thành công.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-08-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-08-004",
    "source_context_sha256": "308645c3e6033ffe46dbc377ea9ab0b06d39293abc6c589f17ab4ce01aab1423",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "aa893562f2117df2f0a2a41b2d7b7b9cdc2bae5c2e12693fa5d644f2f395bed6",
    "source_lines": "L7788-L8762",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-08-004"
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
  "stable_id": "EP-08-004",
  "title": "Payment Success chỉ xác nhận việc nhận tiền thành công",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-08-005 — PaymentSession là Business Object trung tâm của Payment Lifecycle

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
      "requirement_id": "EP-08-005",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "ea31e7df011340278e7e9deb24e4a5ebe4d83f09ce3ec36d685f5c9470be06c3"
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
        "EP-08-005-AC001",
        "EP-08-005-AC002",
        "EP-08-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-08-005-O001",
      "obligation_text": "PaymentSession là Business Object trung tâm của Payment Lifecycle"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-005 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-005 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "PaymentSession là Business Object trung tâm của Payment Lifecycle.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-08-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-08-005",
    "source_context_sha256": "49b43494ae058151349b1e7701743c10f44644e9af7c54e5a46cbc85d1230014",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "ea31e7df011340278e7e9deb24e4a5ebe4d83f09ce3ec36d685f5c9470be06c3",
    "source_lines": "L8764-L8872",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-08-005"
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
  "stable_id": "EP-08-005",
  "title": "PaymentSession là Business Object trung tâm của Payment Lifecycle",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-08-006 — Retry chỉ tạo PaymentAttempt mới

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "No retry creates no new attempt; an eligible retry creates exactly one new attempt"
    ],
    "concrete_bindings": [
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "EP-08-006.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-08-006.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.EP-08-006.EP-08-006.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-08-006-OPT-1",
              "P2-DEC-003"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
            "source_lines": "L668-L671",
            "source_section": "24. Enterprise Design Principles > EP-08-006"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "EP-08-006.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-08-006.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.EP-08-006.EP-08-006.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-08-006-OPT-1",
              "P2-DEC-003"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
            "source_lines": "L668-L671",
            "source_section": "24. Enterprise Design Principles > EP-08-006"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "EP-08-006.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-08-006-OPT-1",
              "P2-DEC-003"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
            "source_lines": "L668-L671",
            "source_section": "24. Enterprise Design Principles > EP-08-006"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.EP-08-006.EP-08-006.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "EP-08-006.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-08-006-OPT-1",
              "P2-DEC-003"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
            "source_lines": "L668-L671",
            "source_section": "24. Enterprise Design Principles > EP-08-006"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.EP-08-006.EP-08-006.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "EP-08-006.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-08-006-OPT-1",
              "P2-DEC-003"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
            "source_lines": "L668-L671",
            "source_section": "24. Enterprise Design Principles > EP-08-006"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.EP-08-006.EP-08-006.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "EP-08-006.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-08-006-OPT-1",
              "P2-DEC-003"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
            "source_lines": "L668-L671",
            "source_section": "24. Enterprise Design Principles > EP-08-006"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.EP-08-006.EP-08-006.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "EP-08-006.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-08-006-OPT-1",
              "P2-DEC-003"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
            "source_lines": "L668-L671",
            "source_section": "24. Enterprise Design Principles > EP-08-006"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.EP-08-006.EP-08-006.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      },
      {
        "from_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "EP-08-006.FROM_STATE"
            ],
            "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "EP-08-006.FROM_STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-08-006-OPT-1",
              "P2-DEC-003"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
            "source_lines": "L668-L671",
            "source_section": "24. Enterprise Design Principles > EP-08-006"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "RESOLVE.EP-08-006.EP-08-006.FROM_STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        },
        "state_machine": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "EP-08-006.STATE_MACHINE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-08-006-OPT-1",
              "P2-DEC-003"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
            "source_lines": "L668-L671",
            "source_section": "24. Enterprise Design Principles > EP-08-006"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_MACHINE_ID",
            "resolver_id": "RESOLVE.EP-08-006.EP-08-006.STATE_MACHINE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_MACHINE_ID"
        },
        "to_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "EP-08-006.TO_STATE"
            ],
            "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "EP-08-006.TO_STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-08-006-OPT-1",
              "P2-DEC-003"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
            "source_lines": "L668-L671",
            "source_section": "24. Enterprise Design Principles > EP-08-006"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "RESOLVE.EP-08-006.EP-08-006.TO_STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        },
        "trigger": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "EP-08-006.TRIGGER",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-08-006-OPT-1",
              "P2-DEC-003"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
            "source_lines": "L668-L671",
            "source_section": "24. Enterprise Design Principles > EP-08-006"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ACTION_ID",
            "resolver_id": "RESOLVE.EP-08-006.EP-08-006.TRIGGER",
            "version": "1.0.0"
          },
          "semantic_type": "ACTION_ID"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.EP-08-006",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Retry mutates or reuses the prior PaymentAttempt identity"
    ],
    "operator_composition": [
      "REFERENCE_TARGET_VALID",
      "STATE_TRANSITION_ALLOWED"
    ],
    "positive_oracle": [
      "Retry creates a new PaymentAttempt"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2C-OBT-C1-EP-08-006-OPT-1",
        "P2-DEC-003"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
      "source_lines": "L668-L671",
      "source_section": "24. Enterprise Design Principles > EP-08-006"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
          "source_type": "APPROVED_DECISION",
          "version": "2026-07-16"
        },
        "identifier": "EP-08-006.EP-08-006.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "EP-08-006.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2C-OBT-C1-EP-08-006-OPT-1",
            "P2-DEC-003"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-08.md",
          "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
          "source_lines": "L668-L671",
          "source_section": "24. Enterprise Design Principles > EP-08-006"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.EP-08-006.EP-08-006.EP-08-006.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "EP-08-006.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.PAYMENT_ID",
        "FIELD.PRIOR_ATTEMPT_ID",
        "FIELD.NEW_ATTEMPT_ID",
        "FIELD.RETRY_NUMBER",
        "FIELD.RETRY_POLICY",
        "FIELD.AUDIT_RECORD"
      ],
      "producer": "EP-08-006.EVIDENCE.PRODUCER",
      "required_collection_origin": "EP-08-006.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.PAYMENT_ID",
        "FIELD.PRIOR_ATTEMPT_ID",
        "FIELD.NEW_ATTEMPT_ID",
        "FIELD.RETRY_NUMBER",
        "FIELD.RETRY_POLICY",
        "FIELD.AUDIT_RECORD"
      ],
      "required_values_or_hashes": [
        "EP-08-006.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "EP-08-006.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "EP-08-006.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "EP-08-006-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": {
        "meaning": "Every retry creates a new PaymentAttempt; retry limits come from applicable versioned policy and no universal value three is asserted.",
        "non_inferences": [
          "Unlimited retries are not permitted by omission.",
          "No gateway retry topology is inferred."
        ],
        "option_id": "P2C-OBT-C1-EP-08-006-OPT-1"
      },
      "assertions": [
        {
          "assertion_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID",
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
              "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "EP-08-006.EP-08-006.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-EP-08-006-OPT-1",
                "P2-DEC-003"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
              "source_lines": "L668-L671",
              "source_section": "24. Enterprise Design Principles > EP-08-006"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.EP-08-006.EP-08-006.EP-08-006.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "EP-08-006.EP-08-006.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "APPROVED_DECISION"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-EP-08-006-OPT-1",
                "P2-DEC-003"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
              "source_lines": "L668-L671",
              "source_section": "24. Enterprise Design Principles > EP-08-006"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.EP-08-006.EP-08-006.EP-08-006.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                        "EP-08-006.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "EP-08-006.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-EP-08-006-OPT-1",
                        "P2-DEC-003"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-08.md",
                      "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                      "source_lines": "L668-L671",
                      "source_section": "24. Enterprise Design Principles > EP-08-006"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.EP-08-006.EP-08-006.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "EP-08-006.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "EP-08-006.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-EP-08-006-OPT-1",
                        "P2-DEC-003"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-08.md",
                      "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                      "source_lines": "L668-L671",
                      "source_section": "24. Enterprise Design Principles > EP-08-006"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.EP-08-006.EP-08-006.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-08-006.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.EP-08-006.EP-08-006.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-08-006.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.EP-08-006.EP-08-006.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-08-006.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.EP-08-006.EP-08-006.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-08-006.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.EP-08-006.EP-08-006.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-08-006.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.EP-08-006.EP-08-006.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-08-006.EP-08-006.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.EP-08-006.EP-08-006.EP-08-006.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-08-006.EP-08-006.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.EP-08-006.EP-08-006.EP-08-006.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-08-006.EP-08-006.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.EP-08-006.EP-08-006.EP-08-006.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "EP-08-006-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "EP-08-006.EP-08-006.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-EP-08-006-OPT-1",
                "P2-DEC-003"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
              "source_lines": "L668-L671",
              "source_section": "24. Enterprise Design Principles > EP-08-006"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.EP-08-006.EP-08-006.EP-08-006.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                      "EP-08-006.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "EP-08-006.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-EP-08-006-OPT-1",
                      "P2-DEC-003"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-08.md",
                    "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                    "source_lines": "L668-L671",
                    "source_section": "24. Enterprise Design Principles > EP-08-006"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.EP-08-006.EP-08-006.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "EP-08-006.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "EP-08-006.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-EP-08-006-OPT-1",
                      "P2-DEC-003"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-08.md",
                    "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                    "source_lines": "L668-L671",
                    "source_section": "24. Enterprise Design Principles > EP-08-006"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.EP-08-006.EP-08-006.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-08-006.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.EP-08-006.EP-08-006.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-08-006.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.EP-08-006.EP-08-006.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-08-006.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.EP-08-006.EP-08-006.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-08-006.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.EP-08-006.EP-08-006.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-08-006.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-006.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.EP-08-006.EP-08-006.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        },
        {
          "assertion_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED",
          "evaluator_consumed_bindings": [
            "from_state",
            "state_machine",
            "to_state",
            "trigger"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-EP-08-006-OPT-1",
                "P2-DEC-003"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
              "source_lines": "L668-L671",
              "source_section": "24. Enterprise Design Principles > EP-08-006"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.EP-08-006.EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.AUTHORITY.ORIGIN",
              "origin_type": "APPROVED_DECISION"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-EP-08-006-OPT-1",
                "P2-DEC-003"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
              "source_lines": "L668-L671",
              "source_section": "24. Enterprise Design Principles > EP-08-006"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "RESOLVE.EP-08-006.EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "STATE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "from_state": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-08-006.FROM_STATE"
                  ],
                  "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-08-006.FROM_STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.EP-08-006.EP-08-006.FROM_STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "state_machine": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-08-006.STATE_MACHINE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_MACHINE_ID",
                  "resolver_id": "RESOLVE.EP-08-006.EP-08-006.STATE_MACHINE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_MACHINE_ID"
              },
              "to_state": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-08-006.TO_STATE"
                  ],
                  "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-08-006.TO_STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.EP-08-006.EP-08-006.TO_STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "trigger": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-08-006.TRIGGER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.EP-08-006.EP-08-006.TRIGGER",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.AUTHORITY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.EP-08-006.EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-08-006-OPT-1",
                    "P2-DEC-003"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-08.md",
                  "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                  "source_lines": "L668-L671",
                  "source_section": "24. Enterprise Design Principles > EP-08-006"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "OBSERVE.EP-08-006.EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.EP-08-006.EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "STATE_TRANSITION_ALLOWED"
          },
          "obligation_id": "EP-08-006-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-EP-08-006-OPT-1",
                "P2-DEC-003"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-08.md",
              "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
              "source_lines": "L668-L671",
              "source_section": "24. Enterprise Design Principles > EP-08-006"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "OBSERVE.EP-08-006.EP-08-006.EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "STATE_ID"
          },
          "operator_id": "STATE_TRANSITION_ALLOWED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "from_state": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "EP-08-006.FROM_STATE"
                ],
                "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-08-006.FROM_STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.EP-08-006.EP-08-006.FROM_STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            },
            "state_machine": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-08-006.STATE_MACHINE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_MACHINE_ID",
                "resolver_id": "RESOLVE.EP-08-006.EP-08-006.STATE_MACHINE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_MACHINE_ID"
            },
            "to_state": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "EP-08-006.TO_STATE"
                ],
                "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-08-006.TO_STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.EP-08-006.EP-08-006.TO_STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            },
            "trigger": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-08-006.TRIGGER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-08-006-OPT-1",
                  "P2-DEC-003"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-08.md",
                "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
                "source_lines": "L668-L671",
                "source_section": "24. Enterprise Design Principles > EP-08-006"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ACTION_ID",
                "resolver_id": "RESOLVE.EP-08-006.EP-08-006.TRIGGER",
                "version": "1.0.0"
              },
              "semantic_type": "ACTION_ID"
            }
          }
        }
      ],
      "boundary_cases": [
        "No retry creates no new attempt; an eligible retry creates exactly one new attempt"
      ],
      "contract_ast_sha256": "947e3392214f471125bc5f22497b851db6a1413c726e82f9a6b32ff154a3f953",
      "contract_id": "P2C.C4.CONTRACT.EP-08-006",
      "criticality": "CRITICAL",
      "disposition": "SOURCE_CLARIFICATION_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-EP-08-006-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "EP-08-006.EP-08-006.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-08-006.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-08-006-OPT-1",
              "P2-DEC-003"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-08.md",
            "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
            "source_lines": "L668-L671",
            "source_section": "24. Enterprise Design Principles > EP-08-006"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.EP-08-006.EP-08-006.EP-08-006.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "EP-08-006.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.PAYMENT_ID",
          "FIELD.PRIOR_ATTEMPT_ID",
          "FIELD.NEW_ATTEMPT_ID",
          "FIELD.RETRY_NUMBER",
          "FIELD.RETRY_POLICY",
          "FIELD.AUDIT_RECORD"
        ],
        "producer": "EP-08-006.EVIDENCE.PRODUCER",
        "required_collection_origin": "EP-08-006.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.PAYMENT_ID",
          "FIELD.PRIOR_ATTEMPT_ID",
          "FIELD.NEW_ATTEMPT_ID",
          "FIELD.RETRY_NUMBER",
          "FIELD.RETRY_POLICY",
          "FIELD.AUDIT_RECORD"
        ],
        "required_values_or_hashes": [
          "EP-08-006.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "EP-08-006.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "EP-08-006.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-C598A024187A7CBE17E3",
        "P2C-C4-FX-80F4B581651AF233CC86",
        "P2C-C4-FX-6FEC7A945160BC3A0587"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Retry mutates or reuses the prior PaymentAttempt identity"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "EP-08-006-O001",
          "obligation_text": "Retry chỉ tạo PaymentAttempt mới"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "EP-08-006.O1.1.REFERENCE_TARGET_VALID",
            "EP-08-006.O1.2.STATE_TRANSITION_ALLOWED"
          ],
          "coverage_count": 1,
          "obligation_id": "EP-08-006-O001"
        }
      ],
      "operator_composition": [
        "REFERENCE_TARGET_VALID",
        "STATE_TRANSITION_ALLOWED"
      ],
      "positive_oracles": [
        "Retry creates a new PaymentAttempt"
      ],
      "preconditions": [
        "The prior attempt and retry policy are known"
      ],
      "prohibitions": [
        "Retry mutates or reuses the prior PaymentAttempt identity"
      ],
      "requirement_id": "EP-08-006",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2C-OBT-C1-EP-08-006-OPT-1",
          "P2-DEC-003"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-08.md",
        "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
        "source_lines": "L668-L671",
        "source_section": "24. Enterprise Design Principles > EP-08-006"
      },
      "source_statement": "Retry chỉ tạo PaymentAttempt mới.",
      "surrounding_source_context": "## EP-08-006\n\nRetry chỉ tạo PaymentAttempt mới.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.EP-08-006",
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
        "EP-08-006-AC001",
        "EP-08-006-AC002",
        "EP-08-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-08-006-O001",
      "obligation_text": "Retry chỉ tạo PaymentAttempt mới"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-006 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-006-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-006-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-006 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Retry chỉ tạo PaymentAttempt mới.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-08-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-08-006",
    "source_context_sha256": "d6a16bec8c6087aac9fbe13c02f789b1d4d5c78db9ae83edda8a33fa694c49a5",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "3e7bef82bf61b7f561564ea3e402dd008c2a5ab518a4347ac05bfd2156c052f9",
    "source_lines": "L8874-L11103",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-08-006"
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
  "stable_id": "EP-08-006",
  "title": "Retry chỉ tạo PaymentAttempt mới",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-08-007 — Payment Notification và Fulfillment Notification là hai Workflow độc lập

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
      "requirement_id": "EP-08-007",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "source_fingerprint": "bf353dccaff5f80ac6e078dd5c479a74ed45b091554c676c2259bd6d434680dc"
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
        "EP-08-007-AC001",
        "EP-08-007-AC002",
        "EP-08-007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-08-007-O001",
      "obligation_text": "Payment Notification và Fulfillment Notification là hai Workflow độc lập"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-007-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-007-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-08-007-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-08-007 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Payment Notification và Fulfillment Notification là hai Workflow độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-08-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-08-007",
    "source_context_sha256": "5ccf9efb44eb902b3bdbd3fcdab65885648c776f8555ba40f1baa4e7771c312d",
    "source_document": "docs/BRD/BRD-WS-08.md",
    "source_fingerprint": "bf353dccaff5f80ac6e078dd5c479a74ed45b091554c676c2259bd6d434680dc",
    "source_lines": "L11105-L11215",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-08-007"
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
  "stable_id": "EP-08-007",
  "title": "Payment Notification và Fulfillment Notification là hai Workflow độc lập",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
