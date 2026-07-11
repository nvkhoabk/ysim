---
document_code: BRD-WS-07
document_name: Sales Order, Purchase Order, Cart & Checkout Model
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
workshop: WS-07
---

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