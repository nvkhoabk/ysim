---
document_code: BRD-WS-01
document_name: Product Vision & Strategy
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
---

# BRD Workshop 01
# Product Vision & Strategy

---

# 1. Workshop Objective

Xác định tầm nhìn, định vị sản phẩm, phạm vi nghiệp vụ và các nguyên tắc nền tảng của YSim v2.0 trước khi xây dựng các yêu cầu chi tiết.

Workshop này là nền tảng cho toàn bộ BRD v2.0.

---

# 2. Product Vision

YSim là nền tảng thương mại và phân phối eSIM toàn cầu (Global eSIM Commerce & Distribution Platform), kết nối các nhà cung cấp eSIM với nhiều kênh bán hàng và đối tác phân phối nhằm mang đến trải nghiệm mua, cấp phát, kích hoạt và quản lý eSIM thuận tiện cho khách du lịch quốc tế.

YSim không được định vị là một website bán eSIM đơn lẻ mà là một White-label Commerce Platform dành riêng cho ngành eSIM.

---

# 3. Product Positioning

YSim là một Product Line thuộc hệ sinh thái Digital Connectivity Platform (DCP).

```text
Digital Connectivity Platform (DCP)

├── YSim
│      eSIM Commerce Platform
│
├── YData
├── YTV
├── YTravel
├── YService
└── Future Products
```

Trong phiên bản 2.0 chỉ triển khai nghiệp vụ eSIM.

Các dịch vụ khác được xem là Out of Scope.

---

# 4. Product Scope

## In Scope

- eSIM Commerce
- White-label Commerce
- Multi-level Distribution
- Multi-supplier Integration
- Intelligent Allocation Engine
- Pricing
- Promotion
- Coupon
- Campaign
- Checkout
- Payment
- Fulfillment
- Activation
- Settlement
- CRM
- Customer Support
- Analytics

## Out of Scope

- Physical SIM
- Mobile Data Platform
- IPTV
- Flight
- Hotel
- Tour
- Digital Services

---

# 5. Product Philosophy

YSim không phải Marketplace.

YSim là White-label Commerce Platform.

Partner sử dụng nền tảng YSim để xây dựng thương hiệu, cửa hàng và hệ thống phân phối của riêng mình.

---

# 6. Core Business Capability

- White-label Commerce
- Multi-level Distribution
- Multi-supplier Integration
- Intelligent Allocation Engine
- Pricing & Promotion Engine
- Checkout & Payment
- Digital eSIM Fulfillment
- Settlement Engine
- CRM
- Analytics

---

# 7. Storefront Concept

Mỗi Partner có thể sở hữu nhiều Storefront.

Một Storefront bao gồm:

- Domain/Subdomain
- Landing Page
- Theme
- Logo
- Banner
- Payment Configuration
- Catalog
- Pricing
- Campaign
- QR Campaign
- Tracking

---

# 8. Commerce Lifecycle

```text
Discover
    ↓
Select
    ↓
Order
    ↓
Payment
    ↓
Fulfillment
    ↓
Activation
    ↓
Support
    ↓
Renewal
```

Khái niệm này được gọi là:

**Digital eSIM Fulfillment**

---

# 9. Sales Channels

Hệ thống phải hỗ trợ:

- Direct Website
- White-label Website
- Agency
- Multi-level Distribution
- Online Seller
- Social Commerce
- Marketplace
- API Partner
- Enterprise Customer

---

# 10. Pricing Strategy

YSim quản lý:

- Product
- Suggested Retail Price
- Discount Policy

Partner được quyền:

- Định giá bán
- Quản lý đại lý
- Thiết lập Commission
- Thiết lập Campaign

Hệ thống hỗ trợ:

- Promotion
- Coupon
- Loyalty

---

# 11. Settlement Strategy

Các hình thức thanh toán:

- Wallet / Deposit
- Pay-per-order
- Payment Gateway
- Postpaid Settlement

Toàn bộ đối soát sử dụng:

**Snapshot Pricing**

---

# 12. Intelligent Allocation Engine

Allocation Engine quyết định Supplier tối ưu dựa trên:

- Cost
- Margin
- SLA
- Availability
- API Health
- Credit Limit
- Priority
- Contract Policy

Mục tiêu:

- Giá cạnh tranh
- API ổn định
- Fulfillment thời gian thực

---

# 13. Customer Strategy

End Customer là trung tâm của toàn bộ hệ thống.

Partner là kênh phân phối.

---

# 14. Customer Ownership Model

Được thống nhất sử dụng:

**Hybrid Model**

- Partner sở hữu quan hệ thương mại.
- YSim quản lý hồ sơ kỹ thuật phục vụ Fulfillment, Activation, Support và Compliance.
- CRM có thể chia sẻ theo chính sách.

---

# 15. Competitive Advantages

- White-label Commerce
- Multi-level Distribution
- Multi-supplier Integration
- Intelligent Allocation Engine
- Snapshot Pricing
- Flexible Settlement
- Real-time Fulfillment
- Strong Customer Support

---

# 16. Business Principles

1. Business First
2. Platform before Store
3. Partner Empowerment
4. Customer-centric Lifecycle
5. Real-time Fulfillment
6. Snapshot Integrity
7. Open Integration
8. Enterprise Scalability

---

# 17. Open Items

Không.

Workshop đã được thống nhất.

---

# 18. Workshop Status

**FROZEN**

Workshop này được sử dụng làm nền tảng cho tất cả các Workshop tiếp theo.

---

# 19. Traceability

Nguồn:

- Thảo luận Workshop 01 giữa Product Owner và Solution Architect.
- Bài học rút ra từ YSim v1.0.

---

# 20. Next Workshop

**Workshop 02 – Business Model & Revenue Architecture**

---

# Architecture Decisions Applied

This Business Requirement Set is governed by the following architecture decisions:

- AFD-002 — Commerce Experience Platform
- AFD-003 — Business Factory
- AFD-005 — Unified Inheritance Framework
- AFD-006 — Payment Offering

---

# Impact to Future DIP

- Store Management Sprint
- Store Runtime Sprint
- Checkout Sprint
- Payment Sprint
- Theme Sprint