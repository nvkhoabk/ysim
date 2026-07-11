---
document_code: BRD-WS-04
document_name: Product Catalog, Supplier & Product Intelligence
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
workshop: WS-04
---

# BRD Workshop 04

# Product Catalog, Supplier & Product Intelligence

---

# 1. Workshop Objective

Workshop này xác định mô hình Product Catalog của YSim, phương pháp chuẩn hóa sản phẩm từ Supplier, cơ chế xây dựng Sales Catalog cho từng Organization và nền tảng Product Intelligence.

Workshop này là Foundation cho:

- Product Domain
- Catalog Domain
- Pricing
- Promotion
- Search
- Recommendation
- Allocation
- Storefront
- Analytics

---

# 2. Business Objects Introduced

| Business Object | Status |
|-----------------|--------|
| Product | Existing (WS-02) |
| Supplier Product | Existing (WS-02) |
| Product Mapping | Existing (WS-02) |
| Product Intelligence | Existing (WS-02) |
| Product Catalog | NEW |
| Master Catalog | NEW |
| Sales Catalog | NEW |
| Storefront Catalog | NEW |
| Product Category | NEW |
| Product Collection | NEW |
| Product Attribute | NEW |
| Product Tag | NEW |
| Product Version | NEW |
| Catalog Governance | NEW |

---

# 3. Four-Level Catalog Architecture

YSim sử dụng mô hình **Four-Level Catalog**.

```text
Supplier Catalog
        │
        ▼
Master Catalog (YSim)
        │
        ▼
Sales Catalog (Organization)
        │
        ▼
Storefront Catalog
```

---

# 4. Supplier Catalog

Supplier Catalog được đồng bộ từ API của Supplier.

Bao gồm:

- Supplier Product
- Product Code
- Product Attributes
- Product Policy
- Availability
- Purchase Price
- Metadata

Supplier Catalog chỉ phục vụ mục đích đồng bộ dữ liệu.

Không hiển thị trực tiếp tới khách hàng.

---

# 5. Master Catalog

Master Catalog do YSim quản lý.

Đây là Product Catalog chuẩn của toàn bộ hệ thống.

Master Catalog chịu trách nhiệm:

- Chuẩn hóa Product
- Product Mapping
- Product Specification
- Product Attribute
- Product Category
- Product Collection
- Product Version
- Product Intelligence
- Catalog Governance

Master Catalog là nguồn dữ liệu chuẩn duy nhất (Single Source of Truth).

---

# 6. Sales Catalog

Sales Catalog thuộc Organization.

Sales Catalog không tạo Product mới.

Sales Catalog chỉ tham chiếu Product trong Master Catalog.

Organization có thể:

- lựa chọn Product muốn bán
- thiết lập giá bán
- lựa chọn Currency
- thiết lập Collection
- thiết lập Tag
- thiết lập Visibility
- bổ sung nội dung Marketing
- thay đổi Product Code bằng Prefix hoặc Postfix theo quy tắc của Organization

Organization không được phép thay đổi:

- Product Specification
- Coverage
- Data Package
- Duration
- Activation Policy
- Product Attribute chuẩn
- Product Version

---

# 7. Storefront Catalog

Storefront Catalog là phần Product được Publish ra Storefront.

Storefront Catalog phục vụ:

- Website
- Landing Page
- Campaign
- Customer Portal
- QR Landing

Storefront Catalog chỉ chứa những Product được Publish.

---

# 8. Product Strategy

Product của YSim là Commercial Product.

Supplier Product là Raw Product.

Một Product của YSim có thể được tạo từ:

- một Supplier Product
- nhiều Supplier Product

Người dùng cuối chỉ nhìn thấy Product của YSim.

Không nhìn thấy Supplier Product.

---

# 9. Product Category

Product hỗ trợ nhiều Taxonomy.

Ví dụ:

Theo Country

- Thailand
- Japan
- Vietnam

Theo Region

- Asia
- Europe
- America

Theo Business Category

- Local
- Regional
- Global

Category Tree không bị giới hạn.

---

# 10. Product Collection

Collection độc lập với Category.

Ví dụ:

- Best Seller
- Featured
- Recommended
- New Arrival
- Summer Promotion
- Staff Pick

Một Product có thể thuộc nhiều Collection.

---

# 11. Product Specification

Product Specification là dữ liệu chuẩn.

Bao gồm:

- Coverage
- Country
- Region
- Total Data
- Daily Data
- Duration
- Network
- Speed
- Hotspot
- Recharge
- Top-up Extension
- Activation Policy
- Auto Renewal

Specification chỉ được quản lý tại Master Catalog.

---

# 12. Product Attribute

Product Attribute độc lập với Specification.

Ví dụ:

- Featured
- Hidden
- Recommendation
- Internal Tag
- Marketing Flag

Attribute phục vụ vận hành và marketing.

---

# 13. Product Variant

Product Variant chưa được triển khai trong phiên bản 2.0.

Nếu khác:

- Coverage
- Data
- Duration
- Activation Policy

thì được xem là Product mới.

---

# 14. Product Code

Product Code của YSim độc lập với Product Code của Supplier.

Product Code là Business Code.

UUID mới là Identity duy nhất.

Product Code có thể được sinh:

- theo quy tắc của YSim
- tham khảo Supplier Product Code
- thông qua Regex Mapping

Product Code có thể tái sử dụng nếu Product cũ đã Archive hoàn toàn.

UUID không bao giờ thay đổi.

---

# 15. Supplier Product

Supplier Product được đồng bộ từ API.

Một Supplier Product có thể bao gồm:

- plan_id
- supplier_product_code
- product_name
- package_description
- hotspot
- apn
- network_type
- countries
- operator
- parent_group_id
- parent_group_name
- total_data
- daily_data
- validity
- topup_extension
- activation_policy

YSim hỗ trợ Attribute Mapping.

Không hardcode theo từng Supplier.

---

# 16. Product Version

Nếu Supplier thay đổi:

- Product Policy
- Product Specification
- Activation Rule
- Product Behavior

YSim tạo Product Version mới.

Version luôn đi kèm Publish Workflow.

Không Publish tự động.

---

# 17. Catalog Governance

Catalog Governance chịu trách nhiệm:

- Validation
- Publish Workflow
- Warning
- Approval
- Audit

Ví dụ:

Partner thiết lập giá bán thấp hơn giá vốn.

↓

Warning

↓

Reason Required

↓

Audit

↓

Parent Notification

---

# 18. Catalog Synchronization

Supplier Catalog được đồng bộ định kỳ.

Quy trình bao gồm:

- Pull Product
- Compare
- Detect New Product
- Detect Removed Product
- Detect Price Change
- Detect Policy Change
- Detect Availability Change
- Detect Attribute Change

Nếu có thay đổi:

↓

Warning

↓

Operator Review

↓

Publish

---

# 19. Product Intelligence

Phiên bản 2.0 chỉ triển khai:

- Product Synchronization
- Difference Detection
- Price Change Detection
- Policy Change Detection
- Availability Detection
- Missing Mapping Detection

Các chức năng AI sẽ triển khai ở phiên bản sau.

---

# 20. Sales Catalog Governance

Sales Catalog thuộc Organization.

Sales Catalog có thể:

- thêm Product từ Master Catalog
- ẩn Product
- thiết lập giá bán
- thiết lập Currency
- thiết lập Collection
- thiết lập Marketing Content

Sales Catalog không được sửa Product Specification.

---

# 21. Currency Governance

Currency là một phần của Commercial Agreement.

Organization chỉ được sử dụng Currency đã được Parent Organization phê duyệt.

Muốn bổ sung Currency mới:

Request

↓

Parent Approval

↓

Exchange Rate Agreement

↓

Effective Date

↓

Activate Currency

Việc thay đổi Exchange Rate phải được thống nhất giữa Organization và Parent.

---

# 22. Search & Recommendation

Search hỗ trợ:

- Country
- Region
- Total Data
- Daily Data
- Duration
- Keyword
- Tag
- AI Search

Recommendation hỗ trợ:

- Similar Product
- Best Seller
- Recommended
- Higher Package
- Lower Price

---

# 23. Catalog Lifecycle

Sales Catalog có vòng đời:

```text
Draft
    │
    ▼
Active
    │
    ▼
Hidden
    │
    ▼
Archived
```

Master Catalog sử dụng Publish Workflow độc lập.

---

# 24. Business Decisions (Locked)

## BD-04-001

YSim sử dụng mô hình Four-Level Catalog:

- Supplier Catalog
- Master Catalog
- Sales Catalog
- Storefront Catalog

---

## BD-04-002

Sales Catalog thuộc Organization.

---

## BD-04-003

Sales Catalog chỉ tham chiếu Master Product.

Không sao chép Product.

---

## BD-04-004

Product Specification chỉ được quản lý tại Master Catalog.

---

## BD-04-005

Organization chỉ được thay đổi:

- Selling Price
- Currency
- Collection
- Visibility
- Marketing Content
- Product Code Prefix/Postfix

---

## BD-04-006

Product Version được tạo khi Supplier thay đổi Policy hoặc Specification.

---

## BD-04-007

Product Variant chưa triển khai trong phiên bản 2.0.

---

## BD-04-008

Supplier Attribute Mapping phải hỗ trợ cấu hình.

Không hardcode.

---

## BD-04-009

Catalog Publish sử dụng Workflow.

Không Publish trực tiếp.

---

## BD-04-010

Currency là một phần của Commercial Agreement giữa Organization và Parent.

---

## BD-04-011

Product Intelligence phiên bản 2.0 chỉ tập trung vào Synchronization và Difference Detection.

---

# 25. Four-Level Catalog Model

```text
                        Supplier Catalog
                               │
                      Supplier Product
                               │
                    Catalog Synchronization
                               │
                               ▼
                    Master Catalog (YSim)
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
 Product Specification   Product Intelligence   Product Version
          │                    │                    │
          └────────────────────┼────────────────────┘
                               │
                               ▼
                 Sales Catalog (Organization)
                               │
        ┌─────────────┬─────────────┬──────────────┬──────────────┐
        │             │             │              │
     Price        Currency     Collection    Marketing Content
        │             │             │              │
        └─────────────┴─────────────┴──────────────┘
                               │
                               ▼
                     Storefront Catalog
                               │
                               ▼
                         End Customer
```

---

# 26. Traceability

Workshop được xây dựng dựa trên:

- BRD Workshop 01
- BRD Workshop 02
- BRD Workshop 03
- Kinh nghiệm triển khai YSim v1.0
- Mô hình White-label Commerce Platform
- Mô hình Multi-level Distribution

---

# 27. Impacts to Other Domains

Workshop này ảnh hưởng trực tiếp tới:

- DMS – Product Domain
- DMS – Catalog Domain
- DMS – Supplier Domain
- DBD – Product, Product Catalog, Sales Catalog
- Pricing Engine
- Promotion Engine
- Search Engine
- Recommendation Engine
- Allocation Engine
- Storefront
- Admin Portal
- Partner Portal
- Customer Portal
- API Specification
- SATP

---

# 28. Workshop Status

**Status:** FROZEN

Workshop này là Foundation cho:

- Product Catalog
- Pricing
- Promotion
- Search
- Recommendation
- Allocation
- Product Intelligence
- Storefront

---

# 29. Next Workshop

**BRD-WS-05 – Pricing, Commercial Policy & Revenue Model**