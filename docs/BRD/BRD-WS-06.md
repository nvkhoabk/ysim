---
document_code: BRD-WS-06
document_name: Promotion, Coupon, Campaign & Sales Enablement
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
workshop: WS-06
---

# BRD Workshop 06

# Promotion, Coupon, Campaign & Sales Enablement

---

# 1. Workshop Objective

Workshop này xác định toàn bộ mô hình Promotion, Coupon, Campaign và Sales Enablement của nền tảng YSim.

Workshop này xây dựng các công cụ hỗ trợ bán hàng dành cho Organization, Sales, Agency và Collaborator.

Workshop bao gồm:

- Promotion
- Coupon
- Campaign
- Landing Page
- Sales Enablement
- Reference QR
- Promotion QR
- Tracking
- Marketing Attribution
- Promotion Funding
- Promotion Snapshot

Workshop này là Foundation cho:

- Storefront
- Customer Portal
- Checkout
- Payment
- CRM
- Analytics

---

# 2. Business Objects Introduced

| Business Object | Status |
|-----------------|--------|
| Promotion | NEW |
| Coupon | NEW |
| Campaign | NEW |
| Promotion Rule | NEW |
| Promotion Audience | NEW |
| Promotion Funding | NEW |
| Promotion Snapshot | NEW |
| Landing Page | NEW |
| Reference QR | NEW |
| Promotion QR | NEW |
| Marketing Attribution | NEW |
| Tracking Link | NEW |
| Sales Tool | NEW |

---

# 3. Sales Enablement Domain

YSim xây dựng một Business Domain độc lập:

## Sales Enablement

Bao gồm:

- Landing Page
- Reference QR
- Tracking Link
- Marketing Attribution
- Campaign
- Sales Tool

Sales Enablement không phải Marketing.

Sales Enablement là tập hợp các công cụ giúp Distribution Network bán hàng hiệu quả hơn.

---

# 4. Promotion Ownership

Promotion thuộc Organization.

Promotion không thuộc:

- Product
- Storefront
- Landing Page
- Campaign

Campaign chỉ sử dụng Promotion.

Storefront chỉ Publish Promotion.

---

# 5. Coupon

Coupon là một loại Promotion.

Version 2.0 hỗ trợ:

- Fixed Amount
- Percentage
- Free Gift
- Bundle Promotion

Bundle nhiều dịch vụ được giữ lại cho các phiên bản sau.

---

# 6. Coupon Inheritance

Coupon kế thừa theo Distribution Network.

Ví dụ:

```text
YSim
    │
    ▼
ABC Travel
    │
    ▼
Agency
    │
    ▼
Collaborator
```

Child Organization có thể:

- Enable
- Disable
- Publish

Coupon kế thừa từ Parent.

Không cần tạo lại Coupon.

Coupon thuộc Price Book Owner nhưng có thể được kế thừa từ Parent giống như Price Book.

---

# 7. Campaign

Campaign là chiến lược bán hàng.

Campaign có thể bao gồm:

- Promotion
- Coupon
- Landing Page
- Reference QR
- Tracking
- Product Collection
- Analytics

Campaign không phải Landing Page.

Landing Page là Business Asset có thể tái sử dụng.

---

# 8. Landing Page

Landing Page thuộc Storefront.

Một Landing Page có thể được nhiều Campaign sử dụng.

Landing Page là công cụ kỹ thuật phục vụ bán hàng.

Campaign là chiến lược kinh doanh.

Hai khái niệm độc lập.

---

# 9. Reference QR

Reference QR là Business Object độc lập.

Reference QR không phải:

- Payment QR
- eSIM QR

Reference QR là điểm vào của Sales Funnel.

Reference QR có thể trỏ tới:

- Storefront
- Landing Page
- Product
- Product Collection

Reference QR luôn gắn Tracking ID.

Người dùng có quyền bán hàng có thể tạo:

- QR cho toàn Storefront
- QR cho Landing Page
- QR cho một Product
- QR cho một Collection

Reference QR có thể lọc sẵn Product để Customer chỉ cần thanh toán.

---

# 10. Promotion QR

Promotion QR là một loại QR riêng.

Customer trong quá trình Checkout có thể:

- Scan Promotion QR
- Upload Promotion QR

để áp dụng:

- Coupon
- Promotion
- Campaign

Promotion QR hoàn toàn khác:

- Payment QR
- eSIM QR
- Reference QR

---

# 11. Tracking

Tracking luôn gắn với User.

Tracking thuộc:

User

↓

Organization

↓

Distribution Network

Tracking dùng để:

- ghi nhận doanh số
- tính Commission
- Marketing Attribution

Tracking không phụ thuộc Campaign.

---

# 12. Marketing Attribution

Marketing Attribution là Business Object độc lập.

Một giao dịch cần Snapshot:

- Storefront
- Landing Page
- Campaign
- Reference QR
- Tracking ID
- Sales User
- Organization
- Distribution Path

Marketing Attribution phục vụ:

- Analytics
- Commission
- Reporting
- Settlement

---

# 13. Promotion Rule

Promotion Rule hỗ trợ:

- Country
- Product
- Category
- Collection
- Customer Group
- Organization
- Campaign
- Payment Method
- Date Range
- Order Value
- Quantity

Các Rule nâng cao sẽ triển khai ở phiên bản sau.

---

# 14. Promotion Audience

Promotion có Audience riêng.

Version 2.0 hỗ trợ:

- Public
- Customer Group
- Imported Customer List
- Invitation Only

Promotion có thể yêu cầu Customer xác thực thông tin trước khi áp dụng.

---

# 15. Coupon Eligibility

Coupon có thể yêu cầu Customer nhập hoặc xác thực thông tin.

Ví dụ:

- Email
- Phone Number
- Referral Phone
- Company Name
- Invitation Code
- Access Code

Có thể cấu hình:

- Exact Match
- Ignore Case
- Case Sensitive
- Regex
- Whitelist

Đây là tính năng Optional.

---

# 16. Promotion Funding

Mỗi Promotion phải có Funding Owner.

Funding Owner mặc định là Organization tạo Promotion.

Promotion Funding quản lý:

- Funding Owner
- Budget
- Used Budget
- Remaining Budget

Chi phí Promotion luôn được tính vào chi phí Marketing của Funding Owner.

Ví dụ:

Coupon do YSim tạo.

↓

ABC Travel kế thừa.

↓

YSim chịu chi phí Promotion.

ABC Travel vẫn hưởng doanh thu.

Ngược lại:

Coupon do ABC Travel tạo.

↓

ABC Travel tự chịu chi phí Promotion.

↓

Khoản thanh toán cho YSim không thay đổi.

---

# 17. Promotion Stack Policy

Promotion Engine hỗ trợ:

- Stackable
- Exclusive
- Highest Benefit

Version 2.0 mặc định:

Stackable.

Promotion hoặc Coupon có thể Override Stack Policy.

---

# 18. Promotion Snapshot

Promotion Snapshot được tạo sau Payment Success.

Snapshot bao gồm:

- Promotion
- Coupon
- Funding
- Audience
- Campaign
- Tracking
- Promotion Rule
- Stack Policy

Promotion Snapshot phục vụ:

- Settlement
- Audit
- Analytics

---

# 19. Sales Tool

Sales Tool bao gồm:

- Landing Page
- Reference QR
- Tracking Link
- Short URL

Các công cụ khác sẽ mở rộng trong các phiên bản sau.

---

# 20. Deferred Scope

Chưa triển khai trong Version 2.0:

- Loyalty
- Membership
- Referral Program
- Bundle nhiều dịch vụ
- AI Promotion
- AI Recommendation
- Social Campaign

Kiến trúc được giữ chỗ để mở rộng.

---

# 21. Business Decisions (Locked)

## BD-06-001

Promotion thuộc Organization.

---

## BD-06-002

Coupon thuộc Price Book Owner và hỗ trợ kế thừa theo Distribution Network.

---

## BD-06-003

Campaign là chiến lược bán hàng.

Landing Page là Business Asset.

---

## BD-06-004

Landing Page thuộc Storefront.

Một Landing Page có thể phục vụ nhiều Campaign.

---

## BD-06-005

Reference QR là Business Object độc lập.

---

## BD-06-006

Promotion QR là Business Object độc lập.

---

## BD-06-007

Tracking luôn gắn với User và Organization.

---

## BD-06-008

Marketing Attribution là Business Object độc lập.

---

## BD-06-009

Promotion Rule chỉ hỗ trợ các điều kiện đã thống nhất trong Version 2.0.

---

## BD-06-010

Coupon Eligibility là tính năng Optional.

---

## BD-06-011

Promotion Funding thuộc Organization tạo Promotion.

---

## BD-06-012

Chi phí Promotion luôn được ghi nhận vào chi phí Marketing của Funding Owner.

---

## BD-06-013

Promotion Engine hỗ trợ Stack Policy.

Version 2.0 mặc định là Stackable.

---

## BD-06-014

Promotion Snapshot được tạo sau Payment Success.

---

## BD-06-015

Sales Enablement là Domain độc lập.

---

## BD-06-016

Referral, Loyalty, Bundle nhiều dịch vụ và AI Promotion được đưa vào Deferred Scope.

---

# 22. Sales Enablement Architecture

```text
                         Organization
                               │
                               ▼
                     Sales Enablement Domain
                               │
      ┌──────────────┬──────────────┬──────────────┐
      │              │              │
 Landing Page   Reference QR   Tracking Link
      │              │              │
      └──────────────┼──────────────┘
                     ▼
           Marketing Attribution
                     │
                     ▼
                 Campaign
                     │
          ┌──────────┼──────────┐
          │          │          │
     Promotion    Coupon   Promotion Rule
          │          │          │
          └──────────┼──────────┘
                     ▼
             Promotion Engine
                     │
      ┌──────────────┼──────────────┐
      │              │              │
 Eligibility     Funding      Stack Policy
      │              │              │
      └──────────────┴──────────────┘
                     │
                     ▼
              Payment Success
                     │
                     ▼
           Promotion Snapshot
                     │
                     ▼
         Settlement / Analytics
```

---

# 23. Enterprise Design Principles

## EP-06-001

Sales Enablement là Domain độc lập với Product Domain và Commercial Domain.

---

## EP-06-002

Landing Page là Business Asset.

Không thuộc Campaign.

---

## EP-06-003

Reference QR, Promotion QR, Payment QR và eSIM QR là bốn Business Object độc lập.

---

## EP-06-004

Tracking luôn gắn với User và Organization.

---

## EP-06-005

Promotion Funding luôn thuộc Organization tạo Promotion.

---

## EP-06-006

Promotion Snapshot chỉ được tạo sau Payment Success.

---

# 24. Traceability

Workshop này kế thừa:

- BRD-WS-01
- BRD-WS-02
- BRD-WS-03
- BRD-WS-04
- BRD-WS-05

---

# 25. Impacts to Other Domains

Workshop này ảnh hưởng tới:

- Sales Enablement Domain
- Promotion Engine
- Campaign Management
- Checkout
- Payment
- Commission Engine
- Settlement
- CRM
- Analytics
- Reporting
- API
- DMS
- DBD

---

# 26. Workshop Status

**Status:** FROZEN

Workshop này là Foundation cho:

- Promotion Engine
- Campaign Management
- Sales Enablement
- Marketing Attribution
- Checkout
- CRM
- Analytics

---

# 27. Next Workshop

**BRD-WS-07 – Order Lifecycle, Cart & Checkout Flow**