---
document_code: BRD-WS-02
document_name: Business Model & Revenue Architecture
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
workshop: WS-02
---

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