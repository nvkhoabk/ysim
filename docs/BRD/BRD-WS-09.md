---
document_code: BRD-WS-09
document_name: Inventory, Allocation & Fulfillment Lifecycle
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
workshop: WS-09
---

# BRD Workshop 09

# Inventory, Allocation & Fulfillment Lifecycle

---

# 1. Workshop Objective

Workshop này xác định toàn bộ Inventory Domain và Fulfillment Domain của YSim.

Bao gồm:

- Inventory
- Inventory Item
- Allocation
- Fulfillment
- Delivery
- Customer Assignment
- QR Security
- Customer Portal Access
- Fulfillment Notification

Workshop kết thúc khi Fulfillment hoàn thành.

Việc kích hoạt eSIM trên mạng di động (Activation) không thuộc phạm vi Workshop này.

---

# 2. Business Objects Introduced

| Business Object | Type |
|-----------------|------|
| Inventory | Master |
| InventoryType | Master |
| InventoryItem | Transaction |
| InventoryReservation | Transaction |
| AllocationRequest | Transaction |
| AllocationPolicy | Master |
| AllocationResult | Transaction |
| FulfillmentSession | Transaction |
| FulfillmentTask | Transaction |
| FulfillmentPackage | Transaction |
| DeliveryChannel | Master |
| DeliveryNotification | Transaction |
| FulfillmentSnapshot | Transaction |
| CustomerAssignment | Transaction |
| CustomerPortalAccess | Transaction |

---

# 3. Inventory Architecture

Inventory là Business Object quản lý kho.

Inventory **không phải** là trạng thái của Product Item.

Một Inventory có thể có nhiều loại.

Ví dụ:

- Ready Inventory
- Revoked Inventory
- Error Inventory
- Quarantine Inventory
- Imported Inventory

Kiến trúc Inventory được thiết kế mở để hỗ trợ nhiều mô hình nhập hàng trong các phiên bản tiếp theo.

---

# 4. Product Item Lifecycle

Inventory quản lý Product Item.

Product Item có vòng đời riêng.

```text
Ready

↓

Reserved

↓

Allocated

↓

Delivered

↓

Viewed

↓

Activated (Reference)

↓

Expired
```

Ngoài ra:

```text
Revoked
```

được sử dụng khi:

- Return
- Activation Failure
- Manual Recovery

Inventory và Product Item Lifecycle là hai khái niệm độc lập.

---

# 5. Inventory Ownership

Inventory luôn thuộc YSim.

Tuy nhiên Inventory View được phân quyền.

Organization chỉ nhìn thấy các Inventory Item mà Organization đang xử lý.

Ví dụ:

- Reserved
- Allocated
- Revoked
- Error

không hiển thị cho Organization khác.

---

# 6. Inventory Source

Inventory Item có thể phát sinh từ:

- Bulk Procurement
- Purchase Order
- Manual Import
- Auto Procurement

Ngay cả Auto Procurement trước Fulfillment cũng phải ghi nhận Product Item vào Inventory trước khi Allocation.

Điều này phục vụ:

- Audit
- Settlement
- Customer Support
- Traceability

---

# 7. Allocation Engine

Allocation được thực hiện theo từng Product.

Nếu SalesOrder có nhiều Product khác nhau:

Allocation được thực hiện độc lập cho từng Product.

Allocation Engine luôn ưu tiên:

1. Inventory có Cost thấp nhất.
2. Supplier Priority.
3. Supplier Cost.
4. Supplier Health.
5. Supplier Response Time.

Allocation chỉ áp dụng giữa các Supplier Mapping của cùng một Product.

---

# 8. Allocation Timing

Allocation được thực hiện Realtime.

Trigger:

```text
Payment Success

↓

Inventory Check

↓

Allocation
```

---

# 9. Fulfillment Session

FulfillmentSession là Transaction Object.

FulfillmentSession quản lý:

- SalesOrder
- Allocation
- Product Item
- Delivery
- Customer Assignment

---

# 10. Fulfillment Task

FulfillmentTask được tạo theo Delivery Channel.

Một FulfillmentTask tương ứng với:

- Một Email
- Một WhatsApp Message
- Một Telegram Message
- Một Zalo OA Message
- Một Portal Notification

Một Task có thể Delivery nhiều Product Item.

---

# 11. Fulfillment Package

FulfillmentPackage nhóm các Product Item theo Recipient.

Ví dụ:

```text
Customer A

↓

Thailand eSIM

Japan eSIM

↓

Email
Portal
WhatsApp
```

Một FulfillmentPackage có thể được gửi qua nhiều Delivery Channel.

Các Channel sử dụng Template riêng nhưng cùng một nội dung Fulfillment.

---

# 12. Delivery Channel

Version 2.0 hỗ trợ:

- Email
- Customer Portal
- Download QR
- WhatsApp
- Telegram
- Zalo OA

SMS chỉ sử dụng cho Notification Alert.

Không gửi QR Code qua SMS.

---

# 13. Customer Portal Access

Customer Portal là Capability độc lập.

Fulfillment chịu trách nhiệm:

- Tạo Customer Portal Access
- Tạo Access Account
- Gửi Access Information

Customer Portal hỗ trợ:

- View Order
- Download Purchased QR
- Customer Support
- Ticket
- Knowledge Base
- Product Catalog
- Reorder

---

# 14. Fulfillment Retry

Nếu Delivery thất bại:

Hệ thống Retry tối đa:

3 lần.

Nếu vẫn thất bại:

- Alternative Delivery Channel
- Customer cập nhật Delivery Channel
- Manual Support

Nếu Customer vẫn còn Payment Session hợp lệ trên Storefront:

cho phép nhập lại Delivery Information.

---

# 15. Delivery Status

Delivery Status:

```text
Pending

↓

Processing

↓

Delivered

↓

Viewed

↓

Downloaded
```

Activation không thuộc Delivery Domain.

Viewed phản ánh Customer đã mở nội dung Fulfillment.

---

# 16. Activation

Activation thuộc Mobile Network Domain.

Version 2.0 không Poll Supplier API.

Activation Monitoring sẽ được triển khai ở phiên bản sau.

---

# 17. Revoked Inventory

Product Item Return không quay về Ready Inventory ngay.

Item chuyển sang:

Revoked Inventory.

Quy trình phục hồi:

```text
Revoked

↓

Export Revoked List

↓

Supplier / MNO Verification

↓

Unused Confirmation

↓

Ready Inventory
```

---

# 18. Allocation Failure

Nếu Allocation thất bại:

- Retry Supplier
- Retry Procurement
- Manual Queue
- Refund

Kiến trúc mở để hỗ trợ thêm Failure Strategy trong các phiên bản sau.

---

# 19. Fulfillment Notification

Fulfillment Notification có thể bao gồm:

- QR Code
- Activation Guide
- APN
- Hotline
- Promotion
- Customer Portal URL
- Customer Portal Access
- Marketing Content

Nội dung được sinh từ Notification Template.

Payment Notification và Fulfillment Notification là hai Workflow độc lập.

---

# 20. Fulfillment Snapshot

FulfillmentSnapshot được tạo sau Delivery thành công.

Snapshot lưu:

- Inventory Item
- Recipient
- Delivery Channel
- Allocation Result
- Delivery Time

---

# 21. Customer Assignment

CustomerAssignment có thể chỉnh sửa.

Quy tắc:

Nếu Fulfillment Package chỉ chứa:

1 Product Item

↓

Không cho phép đổi Recipient.

Nếu Fulfillment Package chứa nhiều Product Item:

↓

Cho phép Assignment lại.

Recipient cũ sẽ nhận Notification:

QR Code trước đây đã được chuyển sang Recipient khác.

---

# 22. QR Security

QR gốc chỉ được Download một lần trong Distribution Network.

Sau lần đầu:

- Portal hiển thị Watermark.
- Portal hiển thị Blur.

QR gốc được Archive.

Chỉ YSim Staff có quyền truy cập.

Customer Portal muốn xem lại QR gốc:

Bắt buộc:

- Two-Factor Authentication (OTP).

---

# 23. Fulfillment Completion

Fulfillment được coi là hoàn thành khi:

Delivery thành công.

Không chờ:

- Activation
- Usage

---

# 24. Delivery ≠ Activation Principle

Delivery và Activation là hai Capability độc lập.

```text
Payment

↓

Inventory

↓

Allocation

↓

Fulfillment

↓

Delivery

======================
YSim Responsibility
======================

↓

Activation

↓

Usage

↓

Renewal

↓

Topup

======================
MNO / Future Version
======================
```

---

# 25. Business Decisions (Locked)

## BD-09-001

Inventory và Product Item Lifecycle là hai Business Concept độc lập.

---

## BD-09-002

Inventory luôn thuộc YSim.

---

## BD-09-003

Allocation ưu tiên:

Inventory Cost → Supplier Priority → Supplier Cost → Supplier Health → Supplier Response Time.

---

## BD-09-004

Allocation được Trigger sau Payment Success.

---

## BD-09-005

FulfillmentSession là Business Object.

---

## BD-09-006

FulfillmentTask được tạo theo Delivery Channel.

---

## BD-09-007

FulfillmentPackage nhóm các Product Item theo Recipient.

---

## BD-09-008

Customer Portal là Capability độc lập.

---

## BD-09-009

Fulfillment Retry tối đa 3 lần.

---

## BD-09-010

SMS không truyền QR Code.

---

## BD-09-011

Revoked Inventory yêu cầu Manual Verification.

---

## BD-09-012

QR gốc chỉ Download một lần trên Distribution Network.

---

## BD-09-013

Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc.

---

## BD-09-014

Fulfillment hoàn thành khi Delivery thành công.

---

## BD-09-015

Delivery và Activation là hai Business Capability độc lập.

---

# 26. Enterprise Design Principles

## EP-09-001

Inventory chỉ quản lý Product Item.

---

## EP-09-002

Mọi Product Item phải đi qua Inventory trước khi Allocation.

---

## EP-09-003

Allocation Engine độc lập với Fulfillment Engine.

---

## EP-09-004

Fulfillment chỉ chịu trách nhiệm Delivery.

---

## EP-09-005

Customer Portal là điểm truy cập thống nhất sau bán hàng.

---

## EP-09-006

QR Code là Digital Asset có yêu cầu bảo mật cao.

---

## EP-09-007

Product Item là Digital Asset có Lifecycle và Traceability xuyên suốt hệ thống.

---

# 27. Fulfillment Lifecycle

```text
Payment Success
        │
        ▼
Inventory Check
        │
        ▼
Auto Procurement (nếu cần)
        │
        ▼
Inventory
        │
        ▼
Allocation
        │
        ▼
Fulfillment Session
        │
        ▼
Fulfillment Package
        │
        ▼
Delivery
        ├── Email
        ├── Customer Portal
        ├── WhatsApp
        ├── Telegram
        └── Zalo OA
        │
        ▼
Delivered
```

---

# 28. Traceability

Workshop này kế thừa:

- BRD-WS-01
- BRD-WS-02
- BRD-WS-03
- BRD-WS-04
- BRD-WS-05
- BRD-WS-06
- BRD-WS-07
- BRD-WS-08

---

# 29. Impacts to Other Domains

Workshop này ảnh hưởng tới:

- Settlement Engine
- Customer Support
- Customer Portal
- Notification Center
- Inventory Management
- Supplier Integration
- Reporting
- API
- DMS
- DBD

---

# 30. Workshop Status

**Status:** FROZEN

Workshop này là Foundation cho:

- Inventory Engine
- Allocation Engine
- Fulfillment Engine
- Customer Portal
- Notification Center
- Settlement Engine

---

# 31. Next Workshop

**BRD-WS-10 – Settlement, Revenue Sharing & Financial Lifecycle**