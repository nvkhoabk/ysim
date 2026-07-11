---
document_code: BRD-WS-08
document_name: Payment, Payment Gateway & Payment Lifecycle
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
workshop: WS-08
---

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