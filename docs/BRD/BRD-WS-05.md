---
document_code: BRD-WS-05
document_name: Pricing, Commercial Policy & Revenue Model
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
workshop: WS-05
---

# BRD Workshop 05

# Pricing, Commercial Policy & Revenue Model

---

# 1. Workshop Objective

Workshop này xác định mô hình Pricing, Commercial Policy và Revenue Model của YSim.

Workshop bao gồm:

- Price Book
- Commercial Agreement
- Cost Model
- Multi-Currency
- Exchange Rate
- Commission
- Revenue Sharing
- Snapshot Pricing
- Price Reservation
- Commercial Consistency
- Price Change Set

Workshop này là Foundation cho:

- Promotion
- Coupon
- Checkout
- Payment
- Settlement
- Financial Event
- Reporting

---

# 2. Business Objects Introduced

| Business Object | Status |
|-----------------|--------|
| Price Book | NEW |
| Price Change Set | NEW |
| Commercial Agreement | NEW |
| Commercial Snapshot | NEW |
| Payment Session | NEW |
| Price Reservation | NEW |
| Revenue Sharing | NEW |
| Commission Snapshot | NEW |
| Exchange Rate Policy | NEW |
| Currency Policy | NEW |

---

# 3. Commercial Domain

YSim tách riêng Product Domain và Commercial Domain.

## Product Domain

- Product
- Catalog
- Supplier
- Inventory
- Fulfillment

## Commercial Domain

- Pricing
- Price Book
- Commercial Agreement
- Promotion
- Commission
- Revenue Sharing
- Settlement
- Credit
- Wallet

Product trả lời:

> Bán cái gì.

Commercial trả lời:

> Bán với điều kiện thương mại nào.

---

# 4. Pricing Ownership

Price không thuộc Product.

Price thuộc Catalog.

Product chỉ lưu các thông tin tham khảo:

- Supplier MSRP
- Supplier Unit Price
- Suggested Retail Price
- Reference Price

Giá bán thực tế được quản lý thông qua Price Book.

---

# 5. Reference Price

Khi tạo Master Product từ Supplier Product, hệ thống cần lưu:

- Supplier Unit Price
- Supplier MSRP
- Supplier Discount Price
- Supplier Discount Rate
- Supplier Tax
- Supplier Fee
- Suggested Retail Price

Reference Price chỉ phục vụ tham khảo.

Không phải Selling Price.

---

# 6. Cost Model

Cost được xác định theo Distribution Network.

Ví dụ:

```text
Supplier

↓

YSim

↓

ABC Travel

↓

Agency

↓

Customer
```

Master Cost của YSim là giá mua từ Supplier.

Cost của ABC Travel là giá YSim bán cho ABC Travel.

Cost của Agency là giá ABC Travel bán cho Agency.

Cost có thể bao gồm:

- Product Cost
- Tax
- Fee
- Procurement Cost

Cost phải hỗ trợ bóc tách phục vụ Settlement.

---

# 7. Price Book

YSim sử dụng Price Book.

Price Book xác định:

- Selling Price
- Currency
- Formula
- Effective Date
- Expiry Date

Một Organization có thể có nhiều Price Book.

Ví dụ:

- Retail
- Corporate
- VIP
- Promotion

---

# 8. Payment Owner

Chỉ Payment Owner mới được phép tạo hoặc chỉnh sửa Price Book.

Payment Owner là Organization nhận tiền từ Customer.

Trong phiên bản 2.0:

- Payment Owner được cố định theo Commercial Agreement.
- Không hỗ trợ thay đổi theo Campaign.
- Nếu thanh toán tiền mặt thì Payment Owner là Organization sở hữu Storefront.

---

# 9. Multi-Currency Price Book

Price Book hỗ trợ nhiều Currency.

Mỗi Price Book phải có:

- Base Currency

Ngoài Base Currency có thể khai báo:

- USD
- EUR
- VND
- JPY
- ...

Các Currency phụ có thể:

- nhập thủ công
- kế thừa Parent
- tính theo Exchange Rate
- Override

---

# 10. Currency Governance

Currency là một phần của Commercial Agreement.

Parent và Child phải thống nhất:

- Settlement Currency
- Exchange Rate Source
- Effective Date
- Exchange Policy

Exchange Rate có thể tham khảo từ:

- ECB
- Vietcombank
- Manual
- Internal Source

---

# 11. Margin Policy

Partner được phép thiết lập giá bán.

Nếu:

Selling Price < Cost

hoặc

Selling Price thấp hơn Parent Recommendation

thì hệ thống phải:

- Warning
- Reason Required
- Parent Notification
- Audit

Nếu giá giảm do:

- Coupon
- Promotion
- Campaign

thì không xem là vi phạm.

---

# 12. Price Change Set

Mọi thay đổi Price Book phải được thực hiện thông qua Price Change Set.

Price Change Set hỗ trợ:

- Bulk Edit
- Bulk Review
- Bulk Approve
- Bulk Publish
- Bulk Archive
- Rollback

UI ưu tiên dạng Table View.

Cho phép:

- Filter
- Multi Select
- Select by Region
- Select by Category
- Create From Parent Catalog

---

# 13. Commission

Commission tách khỏi Pricing.

Commission chỉ áp dụng cho các thực thể trực tiếp tham gia bán hàng.

Ví dụ:

- Sales Department
- Sales User
- Collaborator
- Agency

Commission được Snapshot ngay khi Item được bán.

Portal chỉ hiển thị:

Estimated Commission.

Settlement mới tạo:

Confirmed Commission.

Commission được tính sau khi trừ:

- Tax
- Fee

---

# 14. Revenue Sharing

Revenue Sharing độc lập với Commission.

Revenue Sharing mô tả việc phân chia doanh thu giữa các Organization.

Ví dụ:

Customer

↓

Payment Gateway Fee

↓

Tax

↓

Net Revenue

↓

Payment Owner

↓

Parent

↓

YSim

↓

Supplier

Commission không thuộc Revenue Sharing.

---

# 15. Commercial Agreement

Commercial Agreement là Business Object trung tâm của Commercial Domain.

Commercial Agreement quản lý:

- Payment Owner
- Currency
- Exchange Policy
- Price Policy
- Cost Policy
- Margin Policy
- Commission Policy
- Revenue Sharing Policy
- Settlement Cycle
- Credit Policy
- Payment Policy
- Support Policy

Commercial Agreement là Business Configuration.

---

# 16. Dynamic Pricing

Version 2.0 hỗ trợ Pricing Formula.

Ví dụ:

- Cost + 20%
- Parent Price + 5%
- Reference Price - 10%
- Fixed Price

Không triển khai AI Pricing.

---

# 17. Snapshot Pricing

Snapshot Pricing lưu toàn bộ Commercial Context.

Bao gồm:

- Product Version
- Product Item
- Price Book Version
- Commercial Agreement Version
- Selling Price
- Distribution Cost
- Currency
- Exchange Rate
- Tax
- Fee
- Promotion
- Coupon
- Commission Policy
- Revenue Sharing Policy
- Settlement Policy

Mỗi tầng Distribution chỉ xem được Cost của mình.

---

# 18. Price Reservation

Khi Customer bắt đầu thanh toán, hệ thống tạo Price Reservation.

Bao gồm:

- Product
- Price
- Currency
- Price Book Version
- Commercial Agreement Version
- Exchange Rate Version
- Reservation Time
- Expiry Time

Reservation mặc định:

10 phút.

---

# 19. Payment Session

Payment Session là Business Object độc lập.

Payment Session quản lý:

- Checkout
- Reservation
- Payment
- Retry
- Cancel
- Expiry
- Validation

Payment Session không đồng nhất với Order.

---

# 20. Commercial Consistency Principle

Trước khi Fulfillment, hệ thống bắt buộc thực hiện:

Pre-Fulfillment Commercial Validation.

Kiểm tra:

- Product Version
- Price Book Version
- Commercial Agreement
- Exchange Rate
- Supplier Cost
- Supplier Availability
- Reservation
- Payment

Nếu hợp lệ:

```text
Payment Success

↓

Commercial Validation

↓

Commercial Snapshot Lock

↓

Fulfillment

↓

Deliver QR
```

Nếu không hợp lệ:

```text
Commercial Change

↓

Pause Fulfillment

↓

Customer Decision
```

Customer có thể:

- Pay Difference
- Refund Difference
- Full Refund

---

# 21. Publish Guard

Trước khi Publish Price Change Set, hệ thống phải:

- kiểm tra Payment Session đang mở
- cảnh báo số lượng Payment Session bị ảnh hưởng
- cho phép Review
- cho phép Delay Publish
- cho phép Continue Publish

Ví dụ:

"12 Payment Sessions đang sử dụng Price Book này."

---

# 22. Business Decisions (Locked)

## BD-05-001

Price thuộc Catalog.

---

## BD-05-002

Product chỉ lưu Reference Price.

---

## BD-05-003

Cost được tính theo Distribution Network.

---

## BD-05-004

Chỉ Payment Owner được tạo Price Book.

---

## BD-05-005

Payment Owner cố định theo Commercial Agreement trong phiên bản 2.0.

---

## BD-05-006

Price Book hỗ trợ Multi Currency.

---

## BD-05-007

Currency thuộc Commercial Agreement.

---

## BD-05-008

Partner được phép bán dưới Cost nhưng phải có Warning và Audit.

---

## BD-05-009

Price Book thay đổi thông qua Price Change Set.

---

## BD-05-010

Commission độc lập với Pricing.

---

## BD-05-011

Revenue Sharing độc lập với Commission.

---

## BD-05-012

Dynamic Pricing chỉ hỗ trợ Pricing Formula.

---

## BD-05-013

Commercial Agreement là Business Object trung tâm.

---

## BD-05-014

Snapshot Pricing lưu toàn bộ Commercial Context.

---

## BD-05-015

Payment Session là Business Object độc lập.

---

## BD-05-016

Bắt buộc Pre-Fulfillment Commercial Validation.

---

## BD-05-017

Publish Price Change Set phải kiểm tra Payment Session đang mở.

---

# 23. Commercial Pricing Flow

```text
Supplier Cost
      │
      ▼
Master Catalog
      │
      ▼
Commercial Agreement
      │
      ▼
Price Book
      │
      ▼
Price Reservation
      │
      ▼
Payment Session
      │
      ▼
Commercial Validation
      │
      ▼
Commercial Snapshot
      │
      ▼
Fulfillment
      │
      ▼
Settlement
```

---

# 24. Traceability

Workshop này kế thừa:

- BRD-WS-01
- BRD-WS-02
- BRD-WS-03
- BRD-WS-04

---

# 25. Impacts to Other Domains

Workshop này ảnh hưởng tới:

- Pricing Engine
- Promotion Engine
- Payment Engine
- Checkout
- Settlement
- Financial Event
- Reporting
- BI
- Commission Engine
- Revenue Sharing
- API
- DMS
- DBD

---

# 26. Workshop Status

**Status:** FROZEN

Workshop này là Foundation cho:

- Pricing
- Promotion
- Payment
- Checkout
- Settlement
- Revenue Sharing
- Financial Event

---

# 27. Next Workshop

**BRD-WS-06 – Promotion, Coupon & Campaign Model**