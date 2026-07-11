---
document_code: BRD-UPDATE-01
document_name: Commerce Experience Platform (CXP)
project: YSim v2.1
document_set: Business Requirement Documents
version: 2.1
status: FROZEN
language: en-US
---

# Commerce Experience Platform (CXP)

## BRD-UPDATE-01

---

# 1. Purpose

Version 2.1 bổ sung Business Domain mới:

**Commerce Experience Platform (CXP)**

CXP là nền tảng giúp Organization có thể tự xây dựng, xuất bản và vận hành các kênh bán hàng số (Digital Commerce Experience) trực tiếp trên YSim.

Đối tác không cần sử dụng nền tảng Website hoặc E-Commerce của bên thứ ba để bán eSIM và các Digital Connectivity Products.

---

# 2. Business Vision

Commerce Experience Platform hướng tới mục tiêu:

- giúp Partner có thể bán hàng sau vài phút cấu hình;
- giảm phụ thuộc vào nền tảng bên ngoài;
- chuẩn hóa trải nghiệm mua hàng;
- hỗ trợ Multi-brand;
- hỗ trợ White-label;
- hỗ trợ Multi-language;
- hỗ trợ Multi-country.

---

# 3. Business Scope

CXP bao gồm:

- Store Management
- Theme Management
- Landing Builder
- Storefront Runtime
- Checkout Experience
- Payment Experience
- Publishing
- Campaign Management
- Tracking & Analytics
- SEO Management

---

# 4. Business Objectives

CXP phải cho phép:

✓ tạo Store mới.

✓ Publish Website.

✓ kết nối Domain.

✓ cấu hình Theme.

✓ bán eSIM.

✓ bán Data Package.

✓ chạy Campaign.

✓ Tracking Conversion.

✓ hỗ trợ Affiliate.

---

# 5. Business Actors

Các Actor chính:

| Actor | Description |
|---------|-------------|
| Platform Administrator | Quản trị toàn bộ nền tảng |
| Organization Administrator | Quản trị Store của Organization |
| Marketing Manager | Quản lý Landing Page và Campaign |
| Sales Partner | Chia sẻ Link bán hàng |
| Customer | Mua sản phẩm |

---

# 6. Business Capabilities

CXP bổ sung các Capability sau:

## Store Management

- Create Store
- Configure Store
- Activate Store
- Suspend Store

---

## Theme Management

- Theme Selection
- Logo
- Color Palette
- Typography
- Layout

---

## Landing Builder

- Hero Banner
- Promotion Banner
- Product Section
- Country Section
- FAQ
- Footer
- Marketing Blocks

---

## Publishing

- Publish
- Draft
- Preview
- Version
- Rollback

---

## Checkout Experience

- Cart
- Checkout
- Coupon
- Promotion
- Upsell
- Cross Sell

---

## Payment Experience

- Payment Offering
- Payment Selection
- Payment Session
- Payment Result

---

## Campaign Management

- Campaign
- Landing
- Promotion
- Referral
- Affiliate

---

## Tracking

- Visitor
- Click
- Checkout
- Payment
- Conversion
- Activation

---

## Analytics

- Orders
- Revenue
- Conversion Rate
- Traffic
- Campaign Performance

---

# 6A. Commerce Business Model

Commerce Experience Platform (CXP) chuẩn hóa việc xây dựng Store thông qua **Business Model**.

Business Model định nghĩa cách một Organization triển khai hoạt động kinh doanh trên nền tảng YSim.

Store không được tạo từ đầu một cách thủ công.

Mỗi Store được sinh từ một **Store Template**, và mỗi Store Template được xây dựng dựa trên một Business Model chuẩn hóa.

```text
Business Model

↓

Store Template

↓

Store Instance

↓

Publishing
```

Business Model giúp:

- chuẩn hóa quy trình triển khai;
- giảm thời gian cấu hình;
- tăng khả năng tái sử dụng;
- hỗ trợ AI tự động sinh Store;
- đảm bảo thống nhất giữa các Organization.

---

# 6AA. Business Blueprint

Business Blueprint là lớp chuẩn hóa nghiệp vụ nằm giữa **Business Model** và **Store Template**.

Business Blueprint mô tả cách một mô hình kinh doanh được hiện thực hóa trên nền tảng YSim.

Business Blueprint không phải Source Code.

Business Blueprint cũng không phải giao diện.

Business Blueprint là tập hợp các Capability, Business Rules và Experience Flow cần có để triển khai một Business Model.

```text
Business Model

↓

Business Blueprint

↓

Store Template

↓

Store Instance
```

Business Blueprint giúp:

- chuẩn hóa các mô hình kinh doanh;
- giảm thời gian triển khai Store;
- tái sử dụng Business Capability;
- giúp AI sinh Store theo đúng nghiệp vụ;
- đảm bảo các Store cùng Business Model có hành vi thống nhất.

---

# 6AB. Business Blueprint Components

Một Business Blueprint bao gồm tối thiểu các thành phần sau.

| Component | Description |
|-----------|-------------|
| Business Capability | Các Capability cần kích hoạt |
| Experience Flow | Luồng trải nghiệm khách hàng |
| Store Structure | Cấu trúc Website/Landing |
| Checkout Flow | Luồng Checkout |
| Payment Strategy | Chiến lược Payment Offering |
| Tracking Strategy | Tracking & Analytics |
| SEO Strategy | SEO mặc định |
| Branding Rules | Quy tắc White-label |
| Feature Flags | Các tính năng mặc định |
| Default Configuration | Các cấu hình mặc định |

Business Blueprint không chứa dữ liệu của Organization.

Business Blueprint chỉ mô tả mô hình chuẩn.

---

# 6AC. Relationship Model

Commerce Experience Platform chuẩn hóa mối quan hệ giữa các đối tượng như sau.

```text
Business Model

↓

Business Blueprint

↓

Store Template

↓

Store

↓

Publishing Target
```

Trong đó:

Business Model

- xác định mô hình kinh doanh.

Business Blueprint

- xác định cách mô hình đó hoạt động.

Store Template

- hiện thực Blueprint bằng cấu hình mặc định.

Store

- là Website hoặc Commerce Experience cụ thể của Organization.

Publishing Target

- xác định nơi Commerce Experience được xuất bản.

---

# 6AD. Blueprint Catalog

Version 2.1 chuẩn hóa các Business Blueprint mặc định.

| Blueprint | Description |
|------------|-------------|
| Direct Sales Blueprint | Website bán hàng trực tiếp |
| Travel Agency Blueprint | Website của công ty du lịch |
| Hotel Blueprint | Website dành cho khách sạn |
| OTA Blueprint | Website của OTA |
| Affiliate Blueprint | Landing dành cho Affiliate |
| Campaign Blueprint | Landing theo chiến dịch |
| Enterprise Blueprint | Portal dành cho doanh nghiệp |
| Embedded Commerce Blueprint | Commerce nhúng vào Website hoặc Mobile App |
| QR Commerce Blueprint | Landing mở từ QR Code |

Blueprint có thể được mở rộng theo nhu cầu của nền tảng.

---

# 6AE. Blueprint Lifecycle

Business Blueprint đi qua các trạng thái sau.

```text
Draft

↓

Design

↓

Approved

↓

Published

↓

Deprecated

↓

Archived
```

Chỉ Blueprint ở trạng thái **Published** mới được phép sử dụng để tạo Store mới.

---

# 6AF. Blueprint Versioning

Business Blueprint hỗ trợ Versioning.

Một Organization có thể:

- tiếp tục sử dụng Blueprint cũ;
- nâng cấp lên Blueprint mới;
- tạo Blueprint kế thừa từ Blueprint chuẩn.

Việc nâng cấp Blueprint không làm thay đổi Store hiện hữu nếu Organization chưa chấp thuận.

---

# 6AG. AI-assisted Blueprint Generation

Version 2.1 cho phép AI hỗ trợ sinh Business Blueprint.

AI có thể:

- đề xuất Blueprint phù hợp với Business Model;
- sinh Store Template từ Blueprint;
- sinh Landing Structure;
- sinh Navigation;
- sinh Default Configuration.

AI không được phép Publish Blueprint khi chưa được phê duyệt.

---

# 6AH. Business Principles

Business Blueprint tuân thủ các nguyên tắc sau.

- Blueprint First
- Reusable by Design
- Configuration over Customization
- Version Controlled
- Business Driven
- Experience Oriented
- AI Assisted
- Human Approved

Business Blueprint là nền tảng chuẩn hóa toàn bộ Commerce Experience của YSim.

---

# 6B. Business Model Catalog

Version 2.1 chuẩn hóa các Business Model mặc định.

| Business Model | Description |
|----------------|-------------|
| Direct Sales | Website bán hàng trực tiếp của YSim hoặc Organization |
| Travel Agency | Website bán hàng cho công ty du lịch |
| OTA Partner | Website hoặc Landing cho OTA |
| Hotel Partner | Store dành cho khách sạn hoặc Resort |
| Affiliate | Store dành cho Affiliate hoặc KOL |
| Campaign | Landing Page cho chiến dịch Marketing |
| Enterprise | Store dành cho khách hàng doanh nghiệp |
| Embedded Commerce | Commerce được nhúng vào Website hoặc Mobile App |
| QR Commerce | Landing Page mở từ QR Code |
| API Commerce | Store hoạt động thông qua API hoặc Headless Commerce |

Organization có thể sử dụng Business Model mặc định hoặc tạo Business Model mới nếu được cấp quyền.

---

# 6C. Store Template

Store Template là mẫu cấu hình chuẩn được sử dụng để tạo Store.

Store Template bao gồm:

- Theme mặc định
- Navigation
- Landing Structure
- Component Layout
- Checkout Flow
- Payment Offering
- Tracking Configuration
- SEO Configuration
- Default Pages
- Feature Configuration

Store Template giúp rút ngắn thời gian triển khai và đảm bảo tính nhất quán giữa các Store.

---

# 6D. Store Types

Mỗi Store được phân loại theo mục đích sử dụng.

| Store Type | Description |
|------------|-------------|
| Direct Store | Website bán hàng trực tiếp |
| Organization Store | Website của Organization |
| Campaign Store | Landing cho Campaign |
| Affiliate Store | Website của Affiliate hoặc KOL |
| Embedded Store | Commerce nhúng vào Website hoặc Mobile App |
| Partner Store | Website White-label cho đối tác |

Store Type không làm thay đổi Business Logic mà chỉ ảnh hưởng tới cách tổ chức trải nghiệm người dùng.

---

# 6E. Publishing Targets

Commerce Experience có thể được Publish tới nhiều đích khác nhau.

Version 2.1 chuẩn hóa các Publishing Target sau.

| Publishing Target | Description |
|-------------------|-------------|
| Website | Website hoàn chỉnh |
| Landing Page | Landing Page chuyên biệt |
| QR Landing | Landing mở từ QR Code |
| Custom Domain | Domain riêng |
| Subdomain | Subdomain của Organization |
| Embedded Widget | Widget nhúng |
| WebView | WebView trong Mobile App |
| Mini App | Mini Application |
| Headless API | Commerce thông qua API |

Publishing Target được lựa chọn trong quá trình Publish mà không làm thay đổi Business Model.

---

# 6F. Store Creation Workflow

Version 2.1 chuẩn hóa quy trình tạo Store.

```text
Organization

↓

Choose Business Model

↓

Choose Store Template

↓

Configure Branding

↓

Configure Domain

↓

Configure Payment Offering

↓

Configure Tracking

↓

Preview

↓

Publish

↓

Store Ready
```

Mục tiêu của nền tảng là giúp một Organization có thể tạo Store hoàn chỉnh chỉ trong vài phút.

---

# 6G. Store Lifecycle

Một Store đi qua các trạng thái sau.

```text
Draft

↓

Configured

↓

Preview

↓

Published

↓

Active

↓

Maintenance

↓

Archived
```

Store chỉ được phép nhận giao dịch khi ở trạng thái **Active**.

---

# 6H. Business Objects

Version 2.1 bổ sung các Business Objects sau.

| Business Object | Description |
|-----------------|-------------|
| Business Model | Định nghĩa mô hình kinh doanh |
| Store Template | Mẫu Store chuẩn |
| Store | Website hoặc Commerce Instance |
| Store Version | Phiên bản Store |
| Publishing Target | Đích Publish |
| Landing | Landing Page |
| Page | Trang nội dung |
| Page Component | Thành phần giao diện |
| Theme | Theme của Store |
| Checkout Session | Phiên Checkout |
| Payment Offering | Phương thức thanh toán hiển thị |
| Campaign | Chiến dịch Marketing |
| Tracking Link | Link theo dõi |
| Visitor Session | Phiên truy cập |
| Publish Job | Tác vụ Publish |

---

# 6I. Business Principles

Commerce Experience Platform tuân thủ các nguyên tắc sau.

- Business Model First
- Template Driven
- Configuration over Customization
- White-label by Default
- Publish in Minutes
- Experience First
- Multi-brand
- Multi-language
- Multi-country
- API First
- Headless Ready
- AI Ready

Business Model là điểm khởi đầu của mọi Commerce Experience trên nền tảng YSim.


---

# 6J. Commerce Runtime Overview

Sau khi Store được tạo và Publish, Commerce Experience được vận hành thông qua Runtime Architecture của CXP.

```text
Business Model
        │
        ▼
Business Blueprint
        │
        ▼
Store Template
        │
        ▼
Store Instance
        │
        ▼
Experience Composition
        │
        ▼
Publishing Target
```

Business Layer chỉ mô tả mô hình nghiệp vụ. Runtime chịu trách nhiệm tổng hợp dữ liệu và cung cấp trải nghiệm cho khách hàng.

---

# 6K. Experience Composition

Commerce Experience không được xây dựng bằng cách kết nối trực tiếp từng Business Domain vào giao diện.

Mọi dữ liệu được tổng hợp thành một Experience thống nhất trước khi hiển thị.

Experience có thể bao gồm:

- Product Information
- Pricing
- Promotion
- Payment Offering
- Theme
- Campaign Content
- SEO Metadata
- Tracking Metadata

Điều này giúp đảm bảo tính nhất quán, khả năng mở rộng và hỗ trợ AI sinh Experience trong tương lai.


---

# 7. Store Management

Một Organization có thể sở hữu:

- nhiều Store.

Mỗi Store có:

- Domain
- Theme
- Language
- Currency
- Payment Configuration
- SEO Configuration

Store hoạt động độc lập nhưng kế thừa cấu hình từ Organization theo chính sách kế thừa của nền tảng.

---

# 8. Payment Experience

CXP không quản lý trực tiếp Payment Gateway.

CXP quản lý **Payment Offering**.

Payment Offering là tập hợp các phương thức thanh toán được phép hiển thị cho khách hàng tại thời điểm Checkout.

Ví dụ:

- Credit Card
- PayPal
- Apple Pay
- Google Pay
- Alipay
- WeChat Pay
- Bank QR

Payment Offering được xác định theo cấu hình của Organization và có thể kế thừa từ Parent Organization.

---

# 9. Payment Inheritance

Organization có thể:

- sử dụng Merchant của chính mình;
- kế thừa Merchant từ Parent;
- kết hợp cả hai.

Ví dụ:

Travel ABC

- Bank QR → Merchant của Travel ABC.
- Credit Card → Merchant OnePay của Parent (YSim).
- PayPal → Merchant PayPal của Parent.

Việc Settlement và Commission được xử lý bởi Payment Platform theo chính sách cấu hình.

---

# 10. Store Publishing

Store có thể Publish thông qua:

- Default Domain
- Custom Domain
- Subdomain
- Vanity URL

Publish không yêu cầu can thiệp kỹ thuật sau khi cấu hình hoàn tất.

Một Store có thể được Publish đồng thời tới nhiều Publishing Target mà vẫn sử dụng cùng một Business Blueprint và Store Template.

---

# 11. Tracking & Analytics

Mỗi Store phải hỗ trợ Tracking xuyên suốt hành trình khách hàng:

Visitor

↓

Landing View

↓

Product View

↓

Cart

↓

Checkout

↓

Payment

↓

Order

↓

Activation

↓

Renewal

Tracking phục vụ:

- Analytics
- Conversion
- Campaign
- Affiliate
- Marketing

---

# 12. White-label Capability

Store phải hỗ trợ:

- Brand Name
- Logo
- Domain
- Theme
- Language
- Currency
- Contact Information

White-label không làm thay đổi Business Logic của nền tảng.

---

# 13. Organization Inheritance

Store kế thừa theo Organization:

- Theme
- Payment Profile
- Pricing
- Notification
- Feature Configuration

Organization có thể Override hoặc Inherit theo Unified Inheritance Framework.

---

# 14. Success Criteria

Một Store được coi là sẵn sàng kinh doanh khi:

- đã Publish;
- Domain hoạt động;
- Payment Offering khả dụng;
- Checkout thành công;
- Tracking hoạt động;
- Analytics thu thập dữ liệu.

---

# 15. Related Business Objects

Version 2.1 bổ sung các Business Objects:

- Store
- Theme
- Landing
- Page
- Page Component
- Store Version
- Publish Job
- Payment Offering
- Campaign
- Tracking Link
- Visitor Session
- Checkout Session

---

# 16. Related Business Domains

CXP liên kết với:

- Identity
- Organization
- Product
- Pricing
- Order
- Payment
- Fulfillment
- Notification
- Analytics

CXP không thay thế các Domain trên mà sử dụng các Capability đã được chuẩn hóa để xây dựng trải nghiệm thương mại số hoàn chỉnh.

---

# 17. Business Principles

Commerce Experience Platform tuân thủ:

- Commerce First
- Configuration over Customization
- White-label by Default
- Publish in Minutes
- Multi-tenant
- Multi-brand
- Multi-language
- Multi-country
- API First
- Experience Driven

---

# 18. Document Status

**Status: FROZEN**

BRD-UPDATE-01 bổ sung Business Domain **Commerce Experience Platform (CXP)** cho YSim AI Software Factory Version 2.1.

CXP trở thành Business Domain chính thức của nền tảng và là nền tảng cho toàn bộ khả năng xây dựng, xuất bản và vận hành các Storefront thương mại số trên YSim.

---