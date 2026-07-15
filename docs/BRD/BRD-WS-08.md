---
document_code: "BRD-WS-08"
title: "Payment, Payment Gateway & Payment Lifecycle"
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

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-08-001 — PaymentSession luôn thuộc PaymentOwner

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-08-001-AC001",
      "given": "the applicable business context, actor, and input for PaymentSession luôn thuộc PaymentOwner",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-08-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-08-001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by PaymentSession luôn thuộc PaymentOwner",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-08-001-O001"
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
        "BD-08-001-AC001",
        "BD-08-001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-001-O001",
      "obligation_text": "PaymentSession luôn thuộc PaymentOwner"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-08-001 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-08-001 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-08-001 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-08-001 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-08-001-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-08-001 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "17d1ef05f04fe0b9679dcb6a08e98b3792d84e23fa73fb774d5174ad545b4953",
    "source_lines": "L534-L537",
    "source_section": "23. Business Decisions (Locked) > BD-08-001"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-08-002-AC001",
      "given": "a contract interaction at the integration boundary defined by PaymentGateway Definition thuộc YSim",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-08-002-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-08-002-AC002",
      "given": "an interaction that violates the contract or ownership boundary for PaymentGateway Definition thuộc YSim",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-08-002-O001"
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
        "BD-08-002-AC001",
        "BD-08-002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-002-O001",
      "obligation_text": "PaymentGateway Definition thuộc YSim"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-08-002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-08-002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-08-002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-08-002 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-08-002-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-08-002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "69a2b64f55b808e69b3327082f06717fa95205dcce32dbb7913f70ea642ae004",
    "source_lines": "L540-L543",
    "source_section": "23. Business Decisions (Locked) > BD-08-002"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-08-003-AC001",
      "given": "the applicable business context, actor, and input for MerchantAccount thuộc Organization",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-08-003-O001"
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
        "BD-08-003-AC001"
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
    "source_fingerprint": "2f0ba8527ad497cb88a0112ee61cc783555f29c3a65336c689c2a75cde87971b",
    "source_lines": "L546-L549",
    "source_section": "23. Business Decisions (Locked) > BD-08-003"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-08-004-AC001",
      "given": "a contract interaction at the integration boundary defined by PaymentMethod độc lập với PaymentGateway",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "each boundary object keeps a distinct identity, owner, reference, and lifecycle; changing one does not implicitly mutate the other",
      "verifies": [
        "BD-08-004-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-08-004-AC002",
      "given": "an interaction that violates the contract or ownership boundary for PaymentMethod độc lập với PaymentGateway",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-08-004-O001"
      ],
      "when": "the interaction reaches the integration boundary"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-08-004-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by PaymentMethod độc lập với PaymentGateway",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-08-004-O001"
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
      "criterion_references": [],
      "rationale": "BD-08-004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-08-004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-08-004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-08-004-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-08-004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-08-004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "c36bd855978812aaf941bdf62c65403511f4dd04c998bb6dda8e3f38916af80c",
    "source_lines": "L552-L555",
    "source_section": "23. Business Decisions (Locked) > BD-08-004"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-08-005-AC001",
      "given": "a candidate PaymentAttempt là Business Object record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-08-005-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-08-005-AC002",
      "given": "a PaymentAttempt là Business Object candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-08-005-O001"
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
        "BD-08-005-AC001",
        "BD-08-005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-005-O001",
      "obligation_text": "PaymentAttempt là Business Object"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-08-005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-08-005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-08-005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-08-005 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-08-005-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-08-005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "3835b02c630cbd73904b2a7eabd1517229884c6568b28587d0d541296b73be08",
    "source_lines": "L558-L561",
    "source_section": "23. Business Decisions (Locked) > BD-08-005"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-08-006-AC001",
      "given": "a contract interaction at the integration boundary defined by Reservation Timeout ưu tiên theo PaymentGateway",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-08-006-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-08-006-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Reservation Timeout ưu tiên theo PaymentGateway",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-08-006-O001"
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
        "BD-08-006-AC001",
        "BD-08-006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-006-O001",
      "obligation_text": "Reservation Timeout ưu tiên theo PaymentGateway"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-08-006 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-08-006 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-08-006 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-08-006 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-08-006-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-08-006 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "b957302d39ec353324ae67302b8761893be1d7d6d511205ed82485f3057806be",
    "source_lines": "L564-L567",
    "source_section": "23. Business Decisions (Locked) > BD-08-006"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-08-007-AC001",
      "given": "a candidate PaymentCallback là Business Object record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-08-007-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-08-007-AC002",
      "given": "a PaymentCallback là Business Object candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-08-007-O001"
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
        "BD-08-007-AC001",
        "BD-08-007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-007-O001",
      "obligation_text": "PaymentCallback là Business Object"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-08-007 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-08-007 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-08-007 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-08-007 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-08-007-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-08-007 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "c94ec44d477feb72fa880bb0262ed54fc233839a78ece691816ff1ecc4d3a8cf",
    "source_lines": "L570-L573",
    "source_section": "23. Business Decisions (Locked) > BD-08-007"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-08-008-AC001",
      "given": "a candidate PaymentSnapshot được tạo sau Payment Success record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-08-008-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-08-008-AC002",
      "given": "a PaymentSnapshot được tạo sau Payment Success candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-08-008-O001"
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
        "BD-08-008-AC001",
        "BD-08-008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-008-O001",
      "obligation_text": "PaymentSnapshot được tạo sau Payment Success"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-08-008 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-08-008 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-08-008 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-08-008 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-08-008-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-08-008 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "b32ea2159be9224c0315c568b93a9e764b1f6cd0eacff69de9dd067ac057fc14",
    "source_lines": "L576-L579",
    "source_section": "23. Business Decisions (Locked) > BD-08-008"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-08-009-AC001",
      "given": "a contract interaction at the integration boundary defined by GatewayFee được cấu hình theo CommercialAgreement",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-08-009-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-08-009-AC002",
      "given": "an interaction that violates the contract or ownership boundary for GatewayFee được cấu hình theo CommercialAgreement",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-08-009-O001"
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
        "BD-08-009-AC001",
        "BD-08-009-AC002"
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
    "source_fingerprint": "f847f599e00d3033b8bb9a4464d427df4101352324e15a4288de5f9cdec34d96",
    "source_lines": "L582-L585",
    "source_section": "23. Business Decisions (Locked) > BD-08-009"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-08-010-AC001",
      "given": "the applicable business context, actor, and input for Payment Currency phải thuộc PriceBook",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-08-010-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-08-010-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Payment Currency phải thuộc PriceBook",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-08-010-O001"
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
        "BD-08-010-AC001",
        "BD-08-010-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-010-O001",
      "obligation_text": "Payment Currency phải thuộc PriceBook"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-08-010 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-08-010 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-08-010 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-08-010 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-08-010-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-08-010 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "2e92abbef60f1d40bae110ecc1a6fbe215ed03444e36fb97544060666c900cff",
    "source_lines": "L588-L591",
    "source_section": "23. Business Decisions (Locked) > BD-08-010"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-08-011-AC001",
      "given": "the applicable business context, actor, and input for Retry giữ nguyên PaymentSession",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-08-011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-08-011-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Retry giữ nguyên PaymentSession",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-08-011-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "IDEMPOTENCY",
      "controlled_contract": "EXPLICIT_IDEMPOTENCY_CONTRACT_V1",
      "criterion_id": "BD-08-011-AC003",
      "given": "a repeated request, retry, replay, or duplicate explicitly governed by Retry giữ nguyên PaymentSession",
      "observable_evidence": "original and repeated action identities, both outcomes, side-effect count, and resulting business state",
      "then": "the repeated action produces the requirement-specific stable result without an additional prohibited side effect",
      "verifies": [
        "BD-08-011-O001"
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
      "criterion_references": [],
      "rationale": "BD-08-011 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-08-011 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [
        "BD-08-011-AC003"
      ],
      "status": "APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-08-011 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-08-011-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-08-011 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "c7097c5a940c3076f487869e224a0ce5341dfd29a9ca69080631a94d813ebee0",
    "source_lines": "L594-L597",
    "source_section": "23. Business Decisions (Locked) > BD-08-011"
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
    "source_fingerprint": "85c290d576e6ef2887b527557bee9b0ce7f1e0acb6b334f5a907a67aac2797f8",
    "source_lines": "L600-L603",
    "source_section": "23. Business Decisions (Locked) > BD-08-012"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-08-013-AC001",
      "given": "the applicable business context, actor, and input for Offline Payment yêu cầu Offline Payment Capability",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the governed business action is available only when the required Capability is active in the same applicable scope, and the outcome records the Capability reference used",
      "verifies": [
        "BD-08-013-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_CAPABILITY_DEPENDENCY_FAILURE_V1",
      "criterion_id": "BD-08-013-AC002",
      "given": "the governed business action without the required active Capability for Offline Payment yêu cầu Offline Payment Capability",
      "observable_evidence": "Capability status and scope, rejected action, unchanged business state, and missing-capability reason",
      "then": "the action is unavailable or rejected, no success state is recorded, and the missing Capability is identified",
      "verifies": [
        "BD-08-013-O001"
      ],
      "when": "the action is requested"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-08-013-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Offline Payment yêu cầu Offline Payment Capability",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-08-013-O001"
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
      "criterion_references": [],
      "rationale": "BD-08-013 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-08-013 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-08-013 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-08-013-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-08-013-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-08-013 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "fa3377efbfab55e35c2706b0bc41542b5060d942cbf8bd11a5df0bfcd93debad",
    "source_lines": "L606-L609",
    "source_section": "23. Business Decisions (Locked) > BD-08-013"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-08-014-AC001",
      "given": "the applicable business context, actor, and input for Payment Success không bao gồm Procurement hoặc Fulfillment",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-08-014-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-08-014-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Payment Success không bao gồm Procurement hoặc Fulfillment",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-08-014-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-08-014-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Payment Success không bao gồm Procurement hoặc Fulfillment",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-08-014-O001"
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
      "criterion_references": [],
      "rationale": "BD-08-014 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-08-014 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-08-014 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-08-014-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-08-014-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-08-014 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "f8d5e865227f087a93b559414de64c4e289155e76d09c654089d82567c91ac59",
    "source_lines": "L612-L615",
    "source_section": "23. Business Decisions (Locked) > BD-08-014"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-08-015-AC001",
      "given": "a candidate Refund là Business Object độc lập record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-08-015-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-08-015-AC002",
      "given": "a Refund là Business Object độc lập candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-08-015-O001"
      ],
      "when": "the candidate is validated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-08-015-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Refund là Business Object độc lập",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-08-015-O001"
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
      "criterion_references": [],
      "rationale": "BD-08-015 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-08-015 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-08-015 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-08-015-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-08-015-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-08-015 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "9befafc78e0b3b574724d3a9ce650bd4cb174f1c8d3311a113129f04ffe48e13",
    "source_lines": "L618-L621",
    "source_section": "23. Business Decisions (Locked) > BD-08-015"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-08-016-AC001",
      "given": "the applicable business context, actor, and input for Payment Notification tách biệt Fulfillment Notification",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "BD-08-016-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-08-016-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Payment Notification tách biệt Fulfillment Notification",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-08-016-O001"
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
        "BD-08-016-AC001",
        "BD-08-016-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-016-O001",
      "obligation_text": "Payment Notification tách biệt Fulfillment Notification"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-08-016 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-08-016 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-08-016 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-08-016 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-08-016-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-08-016 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "ec1e03a3d3389bfa342c58b0bad3728a1c3ecd064f6b487110a48a15ac0f3dcb",
    "source_lines": "L624-L627",
    "source_section": "23. Business Decisions (Locked) > BD-08-016"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-08-017-AC001",
      "given": "the applicable business context, actor, and input for PaymentSession lưu Risk Metadata",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-08-017-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-08-017-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by PaymentSession lưu Risk Metadata",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-08-017-O001"
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
        "BD-08-017-AC001",
        "BD-08-017-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-08-017-O001",
      "obligation_text": "PaymentSession lưu Risk Metadata"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-08-017 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-08-017 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-08-017 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-08-017 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-08-017-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-08-017 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "148d41ea6961d6c78c50a1f2afd396f50d0859d71ff84090b0e14348e8a23d41",
    "source_lines": "L630-L633",
    "source_section": "23. Business Decisions (Locked) > BD-08-017"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-08-R002-AC001",
      "given": "the applicable business context, actor, and input for Trong Version 2.0: PaymentOwner không được thay đổi sau khi PaymentSession được tạo",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-08-R002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-08-R002-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Trong Version 2.0: PaymentOwner không được thay đổi sau khi PaymentSession được tạo",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-08-R002-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-08-R002-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Trong Version 2.0: PaymentOwner không được thay đổi sau khi PaymentSession được tạo",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-08-R002-O001"
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
      "criterion_references": [],
      "rationale": "BRD-WS-08-R002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-08-R002-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-08-R002-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L106-L108",
    "source_section": "4. Payment Owner"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-08-R003-AC001",
      "given": "the applicable business context, actor, and input for Đối với Offline Payment: - PaymentOwner vẫn là Organization nhận tiền. - Sales chỉ được phép xác…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-08-R003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-08-R003-AC002",
      "given": "the applicable business context, actor, and input for Đối với Offline Payment: - PaymentOwner vẫn là Organization nhận tiền. - Sales chỉ được phép xác…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-08-R003-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-08-R003-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Đối với Offline Payment: - PaymentOwner vẫn là Organization nhận tiền. - Sales chỉ được phép xác…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-08-R003-O001",
        "BRD-WS-08-R003-O002"
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
        "BRD-WS-08-R003-AC001",
        "BRD-WS-08-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R003-O001",
      "obligation_text": "Đối với Offline Payment: PaymentOwner vẫn là Organization nhận tiền."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-08-R003-AC002",
        "BRD-WS-08-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R003-O002",
      "obligation_text": "Đối với Offline Payment: Sales chỉ được phép xác nhận thanh toán nếu có Offline Payment Capability."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R003 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-08-R003-AC001",
        "BRD-WS-08-R003-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L110-L113",
    "source_section": "4. Payment Owner"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-WS-08-R004-AC001",
      "given": "a contract interaction at the integration boundary defined by Trong Payment Lifecycle, Gateway luôn sử dụng MerchantAccount tương ứng của PaymentOwner",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BRD-WS-08-R004-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-08-R004-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Trong Payment Lifecycle, Gateway luôn sử dụng MerchantAccount tương ứng của PaymentOwner",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BRD-WS-08-R004-O001"
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
        "BRD-WS-08-R004-AC001",
        "BRD-WS-08-R004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R004-O001",
      "obligation_text": "Trong Payment Lifecycle, Gateway luôn sử dụng MerchantAccount tương ứng của PaymentOwner"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R004 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-08-R004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L151",
    "source_section": "6. Merchant Account"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-08-R005-AC001",
      "given": "the applicable business context, actor, and input for Toàn bộ lịch sử PaymentAttempt phải được lưu",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-08-R005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-08-R005-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Toàn bộ lịch sử PaymentAttempt phải được lưu",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-08-R005-O001"
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
        "BRD-WS-08-R005-AC001",
        "BRD-WS-08-R005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R005-O001",
      "obligation_text": "Toàn bộ lịch sử PaymentAttempt phải được lưu"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R005 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-08-R005-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L222",
    "source_section": "9. Payment Attempt"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-08-R006-AC001",
      "given": "an operational task within the scope of Mọi Callback phải được Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-08-R006-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-08-R006-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Mọi Callback phải được Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-08-R006-O001"
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
        "BRD-WS-08-R006-AC001",
        "BRD-WS-08-R006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R006-O001",
      "obligation_text": "Mọi Callback phải được Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R006 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R006 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R006 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R006 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-08-R006-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R006 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L258",
    "source_section": "11. Payment Callback"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-08-R007-AC001",
      "given": "the applicable business context, actor, and input for Version 2.0 yêu cầu: Payment Currency phải thuộc Currency đã được khai báo trong PriceBook",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-08-R007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-08-R007-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Version 2.0 yêu cầu: Payment Currency phải thuộc Currency đã được khai báo trong PriceBook",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-08-R007-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-08-R007-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Version 2.0 yêu cầu: Payment Currency phải thuộc Currency đã được khai báo trong PriceBook",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-08-R007-O001"
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
      "criterion_references": [],
      "rationale": "BRD-WS-08-R007 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R007 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R007 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-08-R007-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-08-R007-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R007 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L308-L310",
    "source_section": "14. Multi-Currency Payment"
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
    "source_lines": "L316",
    "source_section": "14. Multi-Currency Payment"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-08-R010-AC001",
      "given": "the applicable business context, actor, and input for Để Payment thành công: Sales phải có",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-08-R010-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-08-R010-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Để Payment thành công: Sales phải có",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-08-R010-O001"
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
        "BRD-WS-08-R010-AC001",
        "BRD-WS-08-R010-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R010-O001",
      "obligation_text": "Để Payment thành công: Sales phải có"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R010 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R010 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R010 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R010 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-08-R010-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R010 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L351-L353",
    "source_section": "17. Offline Payment"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-08-R011-AC001",
      "given": "the applicable business context, actor, and input for Sales phải xác nhận: Đã nhận thanh toán",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-08-R011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-08-R011-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Sales phải xác nhận: Đã nhận thanh toán",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-08-R011-O001"
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
        "BRD-WS-08-R011-AC001",
        "BRD-WS-08-R011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R011-O001",
      "obligation_text": "Sales phải xác nhận: Đã nhận thanh toán"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R011 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R011 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R011 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R011 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-08-R011-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R011 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L357-L359",
    "source_section": "17. Offline Payment"
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
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
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
    "source_fingerprint": "499c23a50bc71664e46482edc08c0170e57f58e123c54af047511c4f40491542",
    "source_lines": "L474",
    "source_section": "21. Payment Security"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "RULE_BASED_RISK_DECISIONS_V1",
      "criterion_id": "BRD-WS-08-R013-AC001",
      "given": "risk evidence matching no challenge, block, or review rule",
      "observable_evidence": "input evidence references, ALLOW result, applied rule versions, and reason",
      "then": "the decision is ALLOW with the applied rule set and reason recorded",
      "verifies": [
        "BRD-WS-08-R013-O001"
      ],
      "when": "rule-based risk is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "RULE_BASED_RISK_DECISIONS_V1",
      "criterion_id": "BRD-WS-08-R013-AC002",
      "given": "risk evidence requiring additional assurance",
      "observable_evidence": "CHALLENGE result, triggering rule, required assurance, and reason",
      "then": "the decision is CHALLENGE and identifies the required assurance",
      "verifies": [
        "BRD-WS-08-R013-O002"
      ],
      "when": "rule-based risk is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "RULE_BASED_RISK_DECISIONS_V1",
      "criterion_id": "BRD-WS-08-R013-AC003",
      "given": "risk evidence matching a blocking rule",
      "observable_evidence": "BLOCK result, blocking rule and reason, and unchanged protected state",
      "then": "the decision is BLOCK and the protected action does not proceed",
      "verifies": [
        "BRD-WS-08-R013-O003"
      ],
      "when": "rule-based risk is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "RULE_BASED_RISK_DECISIONS_V1",
      "criterion_id": "BRD-WS-08-R013-AC004",
      "given": "risk evidence requiring human review",
      "observable_evidence": "REVIEW result, triggering rule and reason, and pending protected state",
      "then": "the decision is REVIEW and the protected action remains pending the review outcome",
      "verifies": [
        "BRD-WS-08-R013-O004"
      ],
      "when": "rule-based risk is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "VERSIONED_RISK_EVIDENCE_V1",
      "criterion_id": "BRD-WS-08-R013-AC005",
      "given": "a completed rule-based risk decision",
      "observable_evidence": "decision record with resolvable version identifiers for each applicable evidence component",
      "then": "rule, signal, reason, override if present, and audit versions are all recorded and resolvable",
      "verifies": [
        "BRD-WS-08-R013-O005"
      ],
      "when": "decision evidence is inspected"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "RISK_EVIDENCE_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-08-R013-AC006",
      "given": "a risk request missing mandatory evidence or containing invalid evidence",
      "observable_evidence": "non-ALLOW result, evidence-validation reason, and unchanged protected state",
      "then": "the protected action receives no ALLOW result and the missing or invalid evidence is identified",
      "verifies": [
        "BRD-WS-08-R013-O006"
      ],
      "when": "rule-based risk is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "AUTHORIZED_RISK_OVERRIDE_V1",
      "criterion_id": "BRD-WS-08-R013-AC007",
      "given": "an override request from an actor without override authorization",
      "observable_evidence": "actor and scope, authorization result, original and effective decision, denial reason, and audit record",
      "then": "the override is denied, the original risk decision remains effective, and the attempt is audited",
      "verifies": [
        "BRD-WS-08-R013-O007"
      ],
      "when": "the override is attempted"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "AUTHORIZED_RISK_OVERRIDE_V1",
      "criterion_id": "BRD-WS-08-R013-AC008",
      "given": "an authorized override request with a reason",
      "observable_evidence": "authorization evidence, before/after decision, reason, actor, and immutable audit record",
      "then": "the effective decision changes only as authorized and records actor, reason, original decision, override decision, and evidence versions",
      "verifies": [
        "BRD-WS-08-R013-O007"
      ],
      "when": "the override is applied"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-08-R013-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R013-O001",
      "obligation_text": "Applicable rule-based risk input produces an ALLOW decision when no challenge, block, or review rule matches."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-08-R013-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R013-O002",
      "obligation_text": "Applicable rule-based risk input produces a CHALLENGE decision when additional assurance is required."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-08-R013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R013-O003",
      "obligation_text": "Applicable rule-based risk input produces a BLOCK decision when a blocking rule matches."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-08-R013-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R013-O004",
      "obligation_text": "Applicable rule-based risk input produces a REVIEW decision when human review is required."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-08-R013-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R013-O005",
      "obligation_text": "Each risk decision records the versions of its rule, signal, reason, override, and audit evidence."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-08-R013-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R013-O006",
      "obligation_text": "Missing or invalid mandatory risk evidence fails closed."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-08-R013-AC007",
        "BRD-WS-08-R013-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-08-R013-O007",
      "obligation_text": "A risk override is accepted only from an authorized actor and is recorded in audit evidence."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BRD-WS-08-R013-AC007",
        "BRD-WS-08-R013-AC008"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R013 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R013 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-08-R013-AC003",
        "BRD-WS-08-R013-AC006"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-08-R013-AC001",
        "BRD-WS-08-R013-AC002",
        "BRD-WS-08-R013-AC004",
        "BRD-WS-08-R013-AC005"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-08-R013 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_document": "docs/BRD/BRD-WS-08.md"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-08-001-AC001",
      "given": "the applicable business context, actor, and input for Payment Domain độc lập với Commercial Domain và Fulfillment Domain",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "EP-08-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-08-001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Payment Domain độc lập với Commercial Domain và Fulfillment Domain",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-08-001-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-08-001-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Payment Domain độc lập với Commercial Domain và Fulfillment Domain",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-08-001-O001"
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
      "criterion_references": [],
      "rationale": "EP-08-001 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-08-001 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-08-001 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-08-001-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-08-001-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-08-001 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "4cf7d2623fcd095b19dd60b93773b1ee9ce98e33d90793ecee7713fc0364ec39",
    "source_lines": "L638-L641",
    "source_section": "24. Enterprise Design Principles > EP-08-001"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "PAYMENT_OBJECT_INDEPENDENCE_V1",
      "criterion_id": "EP-08-002-AC001",
      "given": "a PaymentGateway and a MerchantAccount",
      "observable_evidence": "both object identities and distinct-identity comparison",
      "then": "each object has a distinct stable identity and neither identity substitutes for the other",
      "verifies": [
        "EP-08-002-O001"
      ],
      "when": "their business identities are inspected"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PAYMENT_OBJECT_INDEPENDENCE_V1",
      "criterion_id": "EP-08-002-AC002",
      "given": "a PaymentGateway and a MerchantAccount used in the same payment configuration",
      "observable_evidence": "owner of each object and references resolving independently to each identity",
      "then": "each object retains its own owner and is referenced explicitly through its own identity",
      "verifies": [
        "EP-08-002-O002"
      ],
      "when": "ownership and references are inspected"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "PAYMENT_OBJECT_INDEPENDENCE_V1",
      "criterion_id": "EP-08-002-AC003",
      "given": "a candidate that conflates PaymentGateway and MerchantAccount into one identity or implicit reference",
      "observable_evidence": "validation rejection, conflated identity or reference, and unchanged accepted object records",
      "then": "the candidate is rejected with the identity or ownership violation identified",
      "verifies": [
        "EP-08-002-O001",
        "EP-08-002-O002"
      ],
      "when": "the business-object relationship is validated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PAYMENT_OBJECT_LIFECYCLE_INDEPENDENCE_V1",
      "criterion_id": "EP-08-002-AC004",
      "given": "independent PaymentGateway and MerchantAccount objects",
      "observable_evidence": "before/after lifecycle states for both object identities and explicit transition evidence",
      "then": "the other object does not automatically inherit that lifecycle transition",
      "verifies": [
        "EP-08-002-O003"
      ],
      "when": "one object changes lifecycle state"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-08-002-AC001",
        "EP-08-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-08-002-O001",
      "obligation_text": "PaymentGateway and MerchantAccount have independent business identities."
    },
    {
      "acceptance_criterion_references": [
        "EP-08-002-AC002",
        "EP-08-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-08-002-O002",
      "obligation_text": "PaymentGateway and MerchantAccount retain independent ownership and references."
    },
    {
      "acceptance_criterion_references": [
        "EP-08-002-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-08-002-O003",
      "obligation_text": "PaymentGateway and MerchantAccount retain independent lifecycles."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-08-002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-08-002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-08-002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-08-002-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-08-002-AC001",
        "EP-08-002-AC002",
        "EP-08-002-AC004"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-08-002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "32c8987b389ec5b4d87f9d00bf8f7dd0e6ee9ccfd6a4bd5cd36effed8da76944",
    "source_lines": "L644-L647",
    "source_section": "24. Enterprise Design Principles > EP-08-002"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EP-08-003-AC001",
      "given": "a contract interaction at the integration boundary defined by PaymentMethod không phụ thuộc PaymentGateway",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EP-08-003-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "EP-08-003-AC002",
      "given": "an interaction that violates the contract or ownership boundary for PaymentMethod không phụ thuộc PaymentGateway",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "EP-08-003-O001"
      ],
      "when": "the interaction reaches the integration boundary"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-08-003-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by PaymentMethod không phụ thuộc PaymentGateway",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-08-003-O001"
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
      "criterion_references": [],
      "rationale": "EP-08-003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-08-003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-08-003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-08-003-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-08-003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-08-003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "cbd366d866946c8cc1291326dc766b8d2d105f00d843f60c9c554840c34aad29",
    "source_lines": "L650-L653",
    "source_section": "24. Enterprise Design Principles > EP-08-003"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-08-004-AC001",
      "given": "the applicable business context, actor, and input for Payment Success chỉ xác nhận việc nhận tiền thành công",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-08-004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-08-004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Payment Success chỉ xác nhận việc nhận tiền thành công",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-08-004-O001"
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
        "EP-08-004-AC001",
        "EP-08-004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-08-004-O001",
      "obligation_text": "Payment Success chỉ xác nhận việc nhận tiền thành công"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-08-004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-08-004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-08-004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EP-08-004 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-08-004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-08-004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "dc5b7b6c06fa9463615e0bfa5855fb7566b27a4fe9a65a17f82ca29281311b9d",
    "source_lines": "L656-L659",
    "source_section": "24. Enterprise Design Principles > EP-08-004"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "EP-08-005-AC001",
      "given": "a candidate PaymentSession là Business Object trung tâm của Payment Lifecycle record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "EP-08-005-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "EP-08-005-AC002",
      "given": "a PaymentSession là Business Object trung tâm của Payment Lifecycle candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "EP-08-005-O001"
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
        "EP-08-005-AC001",
        "EP-08-005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-08-005-O001",
      "obligation_text": "PaymentSession là Business Object trung tâm của Payment Lifecycle"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-08-005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-08-005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-08-005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EP-08-005 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-08-005-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-08-005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "20574ff4401d6a740d5f5f34d49939e37fad3832b66f0eaa289140246da5eaa9",
    "source_lines": "L662-L665",
    "source_section": "24. Enterprise Design Principles > EP-08-005"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-08-006-AC001",
      "given": "the applicable business context, actor, and input for Retry chỉ tạo PaymentAttempt mới",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-08-006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-08-006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Retry chỉ tạo PaymentAttempt mới",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-08-006-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "IDEMPOTENCY",
      "controlled_contract": "EXPLICIT_IDEMPOTENCY_CONTRACT_V1",
      "criterion_id": "EP-08-006-AC003",
      "given": "a repeated request, retry, replay, or duplicate explicitly governed by Retry chỉ tạo PaymentAttempt mới",
      "observable_evidence": "original and repeated action identities, both outcomes, side-effect count, and resulting business state",
      "then": "the repeated action produces the requirement-specific stable result without an additional prohibited side effect",
      "verifies": [
        "EP-08-006-O001"
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
      "criterion_references": [],
      "rationale": "EP-08-006 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-08-006 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [
        "EP-08-006-AC003"
      ],
      "status": "APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EP-08-006 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-08-006-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-08-006 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "31badfa5acbdf88ded5c232a84cadf2e62ae3a1d24f2ad9c3ed82a59969c3c42",
    "source_lines": "L668-L671",
    "source_section": "24. Enterprise Design Principles > EP-08-006"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-08-007-AC001",
      "given": "the applicable business context, actor, and input for Payment Notification và Fulfillment Notification là hai Workflow độc lập",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "EP-08-007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-08-007-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Payment Notification và Fulfillment Notification là hai Workflow độc lập",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-08-007-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-08-007-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Payment Notification và Fulfillment Notification là hai Workflow độc lập",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-08-007-O001"
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
      "criterion_references": [],
      "rationale": "EP-08-007 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-08-007 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-08-007 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-08-007-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-08-007-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-08-007 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "43c36eec79489433ffbe61bf2f0339c8f44488429057f015ce5be613d3138a25",
    "source_lines": "L674-L677",
    "source_section": "24. Enterprise Design Principles > EP-08-007"
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
