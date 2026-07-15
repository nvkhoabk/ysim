---
document_code: "BRD-UPDATE-01"
title: "Commerce Experience Platform (CXP)"
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

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R001 — Đối tác không cần sử dụng nền tảng Website hoặc E-Commerce của bên thứ ba để bán eSIM và các Dig…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R001-AC001",
      "given": "the applicable business context, actor, and input for Đối tác không cần sử dụng nền tảng Website hoặc E-Commerce của bên thứ ba để bán eSIM và các Dig…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-UPDATE-01-R001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-UPDATE-01-R001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Đối tác không cần sử dụng nền tảng Website hoặc E-Commerce của bên thứ ba để bán eSIM và các Dig…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-UPDATE-01-R001-O001"
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
        "BRD-UPDATE-01-R001-AC001",
        "BRD-UPDATE-01-R001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R001-O001",
      "obligation_text": "Đối tác không cần sử dụng nền tảng Website hoặc E-Commerce của bên thứ ba để bán eSIM và các Digital Connectivity Products"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Đối tác không cần sử dụng nền tảng Website hoặc E-Commerce của bên thứ ba để bán eSIM và các Digital Connectivity Products.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-001",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "1. Purpose",
    "source_context_sha256": "672b3ffe5ddee5a82b4237a876cf426c17b4be6a1dfeb541322282233dafe79c",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "8bff1baf03cc3b708e482ff550689d1fdbddabf509eacf81dd0c24b4c03212af",
    "source_lines": "L25",
    "source_section": "1. Purpose"
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
  "stable_id": "BRD-UPDATE-01-R001",
  "title": "Đối tác không cần sử dụng nền tảng Website hoặc E-Commerce của bên thứ ba để bán eSIM và các Dig…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R002 — CXP phải cho phép: ✓ tạo Store mới

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R002-AC001",
      "given": "the applicable business context, actor, and input for CXP phải cho phép: ✓ tạo Store mới",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-UPDATE-01-R002-O001"
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
        "BRD-UPDATE-01-R002-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R002-O001",
      "obligation_text": "CXP phải cho phép: ✓ tạo Store mới"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "CXP phải cho phép: ✓ tạo Store mới.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-002",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Business Objectives",
    "source_context_sha256": "23c080c46e93d52926c86714e2acd9b869876f0b9f57db1e9f1dc04522efefc1",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "6a7b5110e8b85b10d6e50e80b1e726ea6e0bc2af364795d416bf527018755660",
    "source_lines": "L62-L64",
    "source_section": "4. Business Objectives"
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
  "stable_id": "BRD-UPDATE-01-R002",
  "title": "CXP phải cho phép: ✓ tạo Store mới",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R003 — Store không được tạo từ đầu một cách thủ công

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R003-AC001",
      "given": "the applicable business context, actor, and input for Store không được tạo từ đầu một cách thủ công",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-UPDATE-01-R003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-UPDATE-01-R003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Store không được tạo từ đầu một cách thủ công",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-UPDATE-01-R003-O001"
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
        "BRD-UPDATE-01-R003-AC001",
        "BRD-UPDATE-01-R003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R003-O001",
      "obligation_text": "Store không được tạo từ đầu một cách thủ công"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Store không được tạo từ đầu một cách thủ công.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-003",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6A. Commerce Business Model",
    "source_context_sha256": "c4d37906a8b566d5287f6032754ed8beacda9395e42de6a99bf8110ce06f18d2",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "62429418fb4553779880bb4e7566cbc4bf3be6e7ec7bfb84f92139e67df2244f",
    "source_lines": "L200",
    "source_section": "6A. Commerce Business Model"
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
  "stable_id": "BRD-UPDATE-01-R003",
  "title": "Store không được tạo từ đầu một cách thủ công",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R004 — Business Blueprint không phải Source Code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R004-AC001",
      "given": "the applicable business context, actor, and input for Business Blueprint không phải Source Code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-UPDATE-01-R004-O001"
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
        "BRD-UPDATE-01-R004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R004-O001",
      "obligation_text": "Business Blueprint không phải Source Code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Blueprint không phải Source Code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-004",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6AA. Business Blueprint",
    "source_context_sha256": "4373732deda5bd23db6ac2cc78ab192103ef5f913f4cbb5b7996a09a99574361",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "8f9dd722cf79f0d82c1869853d5077332acc0d00245109776f7fba8ce47b445a",
    "source_lines": "L236",
    "source_section": "6AA. Business Blueprint"
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
  "stable_id": "BRD-UPDATE-01-R004",
  "title": "Business Blueprint không phải Source Code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R005 — Business Blueprint cũng không phải giao diện

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R005-AC001",
      "given": "the applicable business context, actor, and input for Business Blueprint cũng không phải giao diện",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-UPDATE-01-R005-O001"
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
        "BRD-UPDATE-01-R005-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R005-O001",
      "obligation_text": "Business Blueprint cũng không phải giao diện"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Blueprint cũng không phải giao diện.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-005",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6AA. Business Blueprint",
    "source_context_sha256": "4373732deda5bd23db6ac2cc78ab192103ef5f913f4cbb5b7996a09a99574361",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "57a336aa8e05c29854d222288b6a2d206c83edd49cb585ed96744650d2bb36e7",
    "source_lines": "L238",
    "source_section": "6AA. Business Blueprint"
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
  "stable_id": "BRD-UPDATE-01-R005",
  "title": "Business Blueprint cũng không phải giao diện",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R006 — Business Blueprint là tập hợp các Capability, Business Rules và Experience Flow cần có để triển …

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R006-AC001",
      "given": "the applicable business context, actor, and input for Business Blueprint là tập hợp các Capability, Business Rules và Experience Flow cần có để triển …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-UPDATE-01-R006-O001"
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
        "BRD-UPDATE-01-R006-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R006-O001",
      "obligation_text": "Business Blueprint là tập hợp các Capability, Business Rules và Experience Flow cần có để triển khai một Business Model"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Blueprint là tập hợp các Capability, Business Rules và Experience Flow cần có để triển khai một Business Model.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-006",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6AA. Business Blueprint",
    "source_context_sha256": "4373732deda5bd23db6ac2cc78ab192103ef5f913f4cbb5b7996a09a99574361",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "8fd273252c6c476a9e65598de44fb1305165c8396a0b28f60cd2c7e8e9b1849d",
    "source_lines": "L240",
    "source_section": "6AA. Business Blueprint"
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
  "stable_id": "BRD-UPDATE-01-R006",
  "title": "Business Blueprint là tập hợp các Capability, Business Rules và Experience Flow cần có để triển …",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R007 — AI không được phép Publish Blueprint khi chưa được phê duyệt

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R007-AC001",
      "given": "the applicable business context, actor, and input for AI không được phép Publish Blueprint khi chưa được phê duyệt",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-UPDATE-01-R007-O001"
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
        "BRD-UPDATE-01-R007-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R007-O001",
      "obligation_text": "AI không được phép Publish Blueprint khi chưa được phê duyệt"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "AI không được phép Publish Blueprint khi chưa được phê duyệt.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-007",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6AG. AI-assisted Blueprint Generation",
    "source_context_sha256": "e1f74008bb83e7880bca9d30ddb9997075b97de4972665a33872dc64b6b597bc",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "70b6f080ba2d6bebb24ffa45552237158d82cae2d1efe7f27772c4d9b9382b60",
    "source_lines": "L417",
    "source_section": "6AG. AI-assisted Blueprint Generation"
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
  "stable_id": "BRD-UPDATE-01-R007",
  "title": "AI không được phép Publish Blueprint khi chưa được phê duyệt",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R008 — Business Blueprint tuân thủ các nguyên tắc sau

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R008-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Business Blueprint tuân thủ các nguyên tắc sau",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-UPDATE-01-R008-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R008-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R008-O001",
      "obligation_text": "Business Blueprint tuân thủ các nguyên tắc sau"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Blueprint tuân thủ các nguyên tắc sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-008",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6AH. Business Principles",
    "source_context_sha256": "0d32406878b8d667cfff2752f3188e699323175901751e2151878ed5cc3a2132",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "ede48109dc3361ce5f84123f39a817c6fff446610d46bb79088bb55846c46863",
    "source_lines": "L423",
    "source_section": "6AH. Business Principles"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R008",
  "title": "Business Blueprint tuân thủ các nguyên tắc sau",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R009 — Store chỉ được phép nhận giao dịch khi ở trạng thái **Active**

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R009-AC001",
      "given": "the applicable business context, actor, and input for Store chỉ được phép nhận giao dịch khi ở trạng thái **Active**",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the resulting business state equals the declared destination for a valid transition and records the prior state, triggering input, and transition reason",
      "verifies": [
        "BRD-UPDATE-01-R009-O001"
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
        "BRD-UPDATE-01-R009-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R009-O001",
      "obligation_text": "Store chỉ được phép nhận giao dịch khi ở trạng thái **Active**"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Store chỉ được phép nhận giao dịch khi ở trạng thái **Active**.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-009",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6G. Store Lifecycle",
    "source_context_sha256": "35a3df74baf12464d09c9ade44259b3c77cef010e7ff83c8b8cb4493d97cf421",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "6fbadca9061d307322011cf8829e577dea15309bb27e1d78267ff4d5fb03f195",
    "source_lines": "L599",
    "source_section": "6G. Store Lifecycle"
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
  "stable_id": "BRD-UPDATE-01-R009",
  "title": "Store chỉ được phép nhận giao dịch khi ở trạng thái **Active**",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R010 — Business Principles composite parent

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Composite parent coverage is satisfied only through ALL_CHILDREN; the parent is not an acceptance unit.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "EARLIER_EXPLICIT_HUMAN_DECISION",
      "exception_id": "P2-CRIT-EXC-005",
      "selected_disposition": "COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION"
    }
  ],
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commerce Experience Platform tuân thủ toàn bộ các Business Principles được liên kết bên dưới.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-010",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-010",
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6I. Business Principles",
    "source_context_sha256": "570dd63c76e846645aa4563a910b0ba891da8c6cb160944ab082cf4f58b5f5ff",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "bb3af87cb0dedf57d250da1b457790ab1c45c177ccd3f2d55bf6d25c53e64bd8",
    "source_lines": "L629",
    "source_section": "6I. Business Principles"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-UPDATE-01-R021",
      "BRD-UPDATE-01-R022",
      "BRD-UPDATE-01-R023",
      "BRD-UPDATE-01-R029",
      "BRD-UPDATE-01-R025",
      "BRD-UPDATE-01-R026",
      "BRD-UPDATE-01-R027",
      "BRD-UPDATE-01-R028",
      "BRD-UPDATE-01-R030",
      "BRD-UPDATE-01-R031",
      "BRD-UPDATE-01-R032",
      "BRD-UPDATE-01-R033"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R010",
  "title": "Business Principles composite parent",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R011 — Commerce Experience không được xây dựng bằng cách kết nối trực tiếp từng Business Domain vào gia…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R011-AC001",
      "given": "the applicable business context, actor, and input for Commerce Experience không được xây dựng bằng cách kết nối trực tiếp từng Business Domain vào gia…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-UPDATE-01-R011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-UPDATE-01-R011-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Commerce Experience không được xây dựng bằng cách kết nối trực tiếp từng Business Domain vào gia…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-UPDATE-01-R011-O001"
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
        "BRD-UPDATE-01-R011-AC001",
        "BRD-UPDATE-01-R011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R011-O001",
      "obligation_text": "Commerce Experience không được xây dựng bằng cách kết nối trực tiếp từng Business Domain vào giao diện"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commerce Experience không được xây dựng bằng cách kết nối trực tiếp từng Business Domain vào giao diện.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-011",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6K. Experience Composition",
    "source_context_sha256": "0cbbf56355882d8c3553b9ded795417b2bbf3a117f20c6eb5fae22f2063d9fb8",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "004dbb0bde6181104507c4e8559af6e54e3182527ae70854f50bd691b998cefa",
    "source_lines": "L678",
    "source_section": "6K. Experience Composition"
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
  "stable_id": "BRD-UPDATE-01-R011",
  "title": "Commerce Experience không được xây dựng bằng cách kết nối trực tiếp từng Business Domain vào gia…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R012 — Mỗi Store phải hỗ trợ Tracking xuyên suốt hành trình khách hàng: Visitor

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R012-AC001",
      "given": "the applicable business context, actor, and input for Mỗi Store phải hỗ trợ Tracking xuyên suốt hành trình khách hàng: Visitor",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-UPDATE-01-R012-O001"
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
        "BRD-UPDATE-01-R012-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R012-O001",
      "obligation_text": "Mỗi Store phải hỗ trợ Tracking xuyên suốt hành trình khách hàng: Visitor"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Store phải hỗ trợ Tracking xuyên suốt hành trình khách hàng: Visitor",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-012",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Tracking & Analytics",
    "source_context_sha256": "798e76f3f42307928252ad9cd500a7dd577b9790af63b30e816fd1c139ccea58",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "19eaf9fd454c3382693fc86c0f55f59c4617d35ca94e387a0db4afd2ae5340e0",
    "source_lines": "L776-L778",
    "source_section": "11. Tracking & Analytics"
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
  "stable_id": "BRD-UPDATE-01-R012",
  "title": "Mỗi Store phải hỗ trợ Tracking xuyên suốt hành trình khách hàng: Visitor",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R013 — Store phải hỗ trợ: - Brand Name

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R013-AC001",
      "given": "the applicable business context, actor, and input for Store phải hỗ trợ: - Brand Name",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-UPDATE-01-R013-O001"
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
        "BRD-UPDATE-01-R013-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R013-O001",
      "obligation_text": "Store phải hỗ trợ: - Brand Name"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Store phải hỗ trợ: - Brand Name",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-013",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. White-label Capability",
    "source_context_sha256": "1d1b19353b25c41ed37be8332501222ca97205d6cb69e00674bfba8042debe4c",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "b3dd6e9b72d292fbcbe935b5a87091c877bb35dc7ef51cf3df0c8efe76061d0c",
    "source_lines": "L824-L826",
    "source_section": "12. White-label Capability"
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
  "stable_id": "BRD-UPDATE-01-R013",
  "title": "Store phải hỗ trợ: - Brand Name",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R014 — Store phải hỗ trợ: - Logo

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R014-AC001",
      "given": "the applicable business context, actor, and input for Store phải hỗ trợ: - Logo",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-UPDATE-01-R014-O001"
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
        "BRD-UPDATE-01-R014-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R014-O001",
      "obligation_text": "Store phải hỗ trợ: - Logo"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Store phải hỗ trợ: - Logo",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-014",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. White-label Capability",
    "source_context_sha256": "1d1b19353b25c41ed37be8332501222ca97205d6cb69e00674bfba8042debe4c",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "d155223601312c79769d4e6d1f582f02ee849d63c16de47b6fa589b41f74b775",
    "source_lines": "L824-L827",
    "source_section": "12. White-label Capability"
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
  "stable_id": "BRD-UPDATE-01-R014",
  "title": "Store phải hỗ trợ: - Logo",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R015 — Store phải hỗ trợ: - Domain

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R015-AC001",
      "given": "the applicable business context, actor, and input for Store phải hỗ trợ: - Domain",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-UPDATE-01-R015-O001"
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
        "BRD-UPDATE-01-R015-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R015-O001",
      "obligation_text": "Store phải hỗ trợ: - Domain"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Store phải hỗ trợ: - Domain",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-015",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. White-label Capability",
    "source_context_sha256": "1d1b19353b25c41ed37be8332501222ca97205d6cb69e00674bfba8042debe4c",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "359dc505d5f5df77831058b3fb286df5a00a959afaef320d78a739b5901e8b9c",
    "source_lines": "L824-L828",
    "source_section": "12. White-label Capability"
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
  "stable_id": "BRD-UPDATE-01-R015",
  "title": "Store phải hỗ trợ: - Domain",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R016 — Store phải hỗ trợ: - Theme

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R016-AC001",
      "given": "the applicable business context, actor, and input for Store phải hỗ trợ: - Theme",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-UPDATE-01-R016-O001"
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
        "BRD-UPDATE-01-R016-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R016-O001",
      "obligation_text": "Store phải hỗ trợ: - Theme"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Store phải hỗ trợ: - Theme",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-016",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. White-label Capability",
    "source_context_sha256": "1d1b19353b25c41ed37be8332501222ca97205d6cb69e00674bfba8042debe4c",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "3f9e724b1e332ec47853aa24618ebadfeb882885cdd2a8df45e67f81b540cf07",
    "source_lines": "L824-L829",
    "source_section": "12. White-label Capability"
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
  "stable_id": "BRD-UPDATE-01-R016",
  "title": "Store phải hỗ trợ: - Theme",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R017 — Store phải hỗ trợ: - Language

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R017-AC001",
      "given": "the applicable business context, actor, and input for Store phải hỗ trợ: - Language",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-UPDATE-01-R017-O001"
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
        "BRD-UPDATE-01-R017-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R017-O001",
      "obligation_text": "Store phải hỗ trợ: - Language"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Store phải hỗ trợ: - Language",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-017",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. White-label Capability",
    "source_context_sha256": "1d1b19353b25c41ed37be8332501222ca97205d6cb69e00674bfba8042debe4c",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "1b2800a60ae02a0f3ddcdddc80714a0b2e68d92886d20a02bfc3c8563295a55f",
    "source_lines": "L824-L830",
    "source_section": "12. White-label Capability"
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
  "stable_id": "BRD-UPDATE-01-R017",
  "title": "Store phải hỗ trợ: - Language",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R018 — Store phải hỗ trợ: - Currency

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R018-AC001",
      "given": "the applicable business context, actor, and input for Store phải hỗ trợ: - Currency",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-UPDATE-01-R018-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-UPDATE-01-R018-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Store phải hỗ trợ: - Currency",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-UPDATE-01-R018-O001"
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
        "BRD-UPDATE-01-R018-AC001",
        "BRD-UPDATE-01-R018-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R018-O001",
      "obligation_text": "Store phải hỗ trợ: - Currency"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION",
      "exception_id": "P2-CRIT-EXC-006",
      "selected_disposition": "CONFIRM_HIGH"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Store phải hỗ trợ: - Currency",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-018",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-018",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. White-label Capability",
    "source_context_sha256": "1d1b19353b25c41ed37be8332501222ca97205d6cb69e00674bfba8042debe4c",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "f56dcc4142718d10f4fc085dd1845ec9461176292b9adf3027c7fd0437158469",
    "source_lines": "L824-L831",
    "source_section": "12. White-label Capability"
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
  "stable_id": "BRD-UPDATE-01-R018",
  "title": "Store phải hỗ trợ: - Currency",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R019 — Store phải hỗ trợ: - Contact Information

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R019-AC001",
      "given": "the applicable business context, actor, and input for Store phải hỗ trợ: - Contact Information",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-UPDATE-01-R019-O001"
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
        "BRD-UPDATE-01-R019-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R019-O001",
      "obligation_text": "Store phải hỗ trợ: - Contact Information"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Store phải hỗ trợ: - Contact Information",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-019",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-019",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. White-label Capability",
    "source_context_sha256": "1d1b19353b25c41ed37be8332501222ca97205d6cb69e00674bfba8042debe4c",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "d7974287a07814f8a5b6c951667231927be81d22e2cb88d830f3d2fec531f3d2",
    "source_lines": "L824-L832",
    "source_section": "12. White-label Capability"
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
  "stable_id": "BRD-UPDATE-01-R019",
  "title": "Store phải hỗ trợ: - Contact Information",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R020 — Commerce Experience Platform tuân thủ: - Commerce First

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R020-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Commerce Experience Platform tuân thủ: - Commerce First",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-UPDATE-01-R020-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "BRD-UPDATE-01-R020-AC002",
      "given": "a proposed change with missing traceability or a boundary violation under Commerce Experience Platform tuân thủ: - Commerce First",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "BRD-UPDATE-01-R020-O001"
      ],
      "when": "design conformance is reviewed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R020-AC001",
        "BRD-UPDATE-01-R020-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R020-O001",
      "obligation_text": "Commerce Experience Platform tuân thủ: - Commerce First"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-007",
      "selected_disposition": "CONFIRM_HIGH"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commerce Experience Platform tuân thủ: - Commerce First",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-020",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Business Principles",
    "source_context_sha256": "63dc655309f8a4806db68f44a8ff990ca5872e6b558f1e8852306197a866f64a",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "1ca769cad82f645025d0be504a2004856406d0bcaa1a282c443b690ce6779b84",
    "source_lines": "L904-L906",
    "source_section": "17. Business Principles"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R020",
  "title": "Commerce Experience Platform tuân thủ: - Commerce First",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R021 — Configuration over Customization

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R021-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Configuration over Customization",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance evidence identifies the governing configuration and shows that an approved configuration change alters the governed result without a source-code variant",
      "verifies": [
        "BRD-UPDATE-01-R021-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R021-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R021-O001",
      "obligation_text": "Commerce Experience Platform tuân thủ: - Configuration over Customization"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION",
      "exception_id": "P2-CRIT-EXC-008",
      "selected_disposition": "CONFIRM_NORMAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commerce Experience Platform tuân thủ: - Configuration over Customization",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-021",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Business Principles",
    "source_context_sha256": "63dc655309f8a4806db68f44a8ff990ca5872e6b558f1e8852306197a866f64a",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "2df6adaae39f88c051ef9be44e137eaa6eb557665aa557f96a1ad2eb5ada2a5f",
    "source_lines": "L904-L907",
    "source_section": "17. Business Principles"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R010"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R021",
  "title": "Configuration over Customization",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R022 — White-label by Default

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R022-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by White-label by Default",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-UPDATE-01-R022-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "BRD-UPDATE-01-R022-AC002",
      "given": "a proposed change with missing traceability or a boundary violation under White-label by Default",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "BRD-UPDATE-01-R022-O001"
      ],
      "when": "design conformance is reviewed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R022-AC001",
        "BRD-UPDATE-01-R022-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R022-O001",
      "obligation_text": "Commerce Experience Platform tuân thủ: - White-label by Default"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION",
      "exception_id": "P2-CRIT-EXC-009",
      "selected_disposition": "CONFIRM_HIGH"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commerce Experience Platform tuân thủ: - White-label by Default",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-022",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Business Principles",
    "source_context_sha256": "63dc655309f8a4806db68f44a8ff990ca5872e6b558f1e8852306197a866f64a",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "212c6c8a693b315be9b87a48fc2c643a475d6c40cafc702919dd6a8309f95f2b",
    "source_lines": "L904-L908",
    "source_section": "17. Business Principles"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R010"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R022",
  "title": "White-label by Default",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R023 — Publish in Minutes

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R023-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Publish in Minutes",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-UPDATE-01-R023-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "BRD-UPDATE-01-R023-AC002",
      "given": "a proposed change with missing traceability or a boundary violation under Publish in Minutes",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "BRD-UPDATE-01-R023-O001"
      ],
      "when": "design conformance is reviewed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R023-AC001",
        "BRD-UPDATE-01-R023-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R023-O001",
      "obligation_text": "Commerce Experience Platform tuân thủ: - Publish in Minutes"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION",
      "exception_id": "P2-CRIT-EXC-010",
      "selected_disposition": "CONFIRM_HIGH"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commerce Experience Platform tuân thủ: - Publish in Minutes",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-023",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-023",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Business Principles",
    "source_context_sha256": "63dc655309f8a4806db68f44a8ff990ca5872e6b558f1e8852306197a866f64a",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "3e4ba4ecc4a01b561a5ef32e2307ee781c3e11ca5ee6d479321a261a5f6ecd01",
    "source_lines": "L904-L909",
    "source_section": "17. Business Principles"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R010"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R023",
  "title": "Publish in Minutes",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R024 — Commerce Experience Platform tuân thủ: - Multi-tenant

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R024-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Commerce Experience Platform tuân thủ: - Multi-tenant",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-UPDATE-01-R024-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "BRD-UPDATE-01-R024-AC002",
      "given": "a proposed change with missing traceability or a boundary violation under Commerce Experience Platform tuân thủ: - Multi-tenant",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "BRD-UPDATE-01-R024-O001"
      ],
      "when": "design conformance is reviewed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R024-AC001",
        "BRD-UPDATE-01-R024-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R024-O001",
      "obligation_text": "Commerce Experience Platform tuân thủ: - Multi-tenant"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-UPDATE-01-R024 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-UPDATE-01-R024 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-UPDATE-01-R024 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-UPDATE-01-R024 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-UPDATE-01-R024-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-UPDATE-01-R024 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION",
      "exception_id": "P2-CRIT-EXC-011",
      "selected_disposition": "CONFIRM_CRITICAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commerce Experience Platform tuân thủ: - Multi-tenant",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-024",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Business Principles",
    "source_context_sha256": "63dc655309f8a4806db68f44a8ff990ca5872e6b558f1e8852306197a866f64a",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "100fee1489823de31067dcee0948c1fbc7022a4d73ab9741dca386277ee16140",
    "source_lines": "L904-L910",
    "source_section": "17. Business Principles"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R024",
  "title": "Commerce Experience Platform tuân thủ: - Multi-tenant",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R025 — Multi-brand

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R025-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Multi-brand",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-UPDATE-01-R025-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "BRD-UPDATE-01-R025-AC002",
      "given": "a proposed change with missing traceability or a boundary violation under Multi-brand",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "BRD-UPDATE-01-R025-O001"
      ],
      "when": "design conformance is reviewed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R025-AC001",
        "BRD-UPDATE-01-R025-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R025-O001",
      "obligation_text": "Commerce Experience Platform tuân thủ: - Multi-brand"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION",
      "exception_id": "P2-CRIT-EXC-012",
      "selected_disposition": "CONFIRM_HIGH"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commerce Experience Platform tuân thủ: - Multi-brand",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-025",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Business Principles",
    "source_context_sha256": "63dc655309f8a4806db68f44a8ff990ca5872e6b558f1e8852306197a866f64a",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "a342159d57c5c458443f9e04609918d9367341d99569f1d1399827fd5a1921a7",
    "source_lines": "L904-L911",
    "source_section": "17. Business Principles"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R010"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R025",
  "title": "Multi-brand",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R026 — Multi-language

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R026-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Multi-language",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-UPDATE-01-R026-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "BRD-UPDATE-01-R026-AC002",
      "given": "a proposed change with missing traceability or a boundary violation under Multi-language",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "BRD-UPDATE-01-R026-O001"
      ],
      "when": "design conformance is reviewed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R026-AC001",
        "BRD-UPDATE-01-R026-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R026-O001",
      "obligation_text": "Commerce Experience Platform tuân thủ: - Multi-language"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION",
      "exception_id": "P2-CRIT-EXC-013",
      "selected_disposition": "CONFIRM_HIGH"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commerce Experience Platform tuân thủ: - Multi-language",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-026",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-026",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Business Principles",
    "source_context_sha256": "63dc655309f8a4806db68f44a8ff990ca5872e6b558f1e8852306197a866f64a",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "3906de07b7270ebc89cca94ad60f720bda554cb36c6629064603eb6a601517c2",
    "source_lines": "L904-L912",
    "source_section": "17. Business Principles"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R010"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R026",
  "title": "Multi-language",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R027 — Multi-country

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R027-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Multi-country",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-UPDATE-01-R027-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "BRD-UPDATE-01-R027-AC002",
      "given": "a proposed change with missing traceability or a boundary violation under Multi-country",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "BRD-UPDATE-01-R027-O001"
      ],
      "when": "design conformance is reviewed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R027-AC001",
        "BRD-UPDATE-01-R027-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R027-O001",
      "obligation_text": "Commerce Experience Platform tuân thủ: - Multi-country"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION",
      "exception_id": "P2-CRIT-EXC-014",
      "selected_disposition": "CONFIRM_HIGH"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commerce Experience Platform tuân thủ: - Multi-country",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-027",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-027",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Business Principles",
    "source_context_sha256": "63dc655309f8a4806db68f44a8ff990ca5872e6b558f1e8852306197a866f64a",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "98e103833da1ecacd7fb9cd5e799e9de74bd5adc2e0163bec5c1c6e2178f1ae6",
    "source_lines": "L904-L913",
    "source_section": "17. Business Principles"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R010"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R027",
  "title": "Multi-country",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R028 — API First

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R028-AC001",
      "given": "a contract interaction at the integration boundary defined by API First",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BRD-UPDATE-01-R028-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-UPDATE-01-R028-AC002",
      "given": "an interaction that violates the contract or ownership boundary for API First",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BRD-UPDATE-01-R028-O001"
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
        "BRD-UPDATE-01-R028-AC001",
        "BRD-UPDATE-01-R028-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R028-O001",
      "obligation_text": "Commerce Experience Platform tuân thủ: - API First"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commerce Experience Platform tuân thủ: - API First",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-028",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-028",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Business Principles",
    "source_context_sha256": "63dc655309f8a4806db68f44a8ff990ca5872e6b558f1e8852306197a866f64a",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "35687b54a029a38cbd3f9c7481d908f806e40d5a4816f59162df5fa2bbb7c25a",
    "source_lines": "L904-L914",
    "source_section": "17. Business Principles"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R010"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R028",
  "title": "API First",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R029 — Experience First

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R029-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Experience First",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-UPDATE-01-R029-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R029-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R029-O001",
      "obligation_text": "Commerce Experience phải ưu tiên trải nghiệm người dùng trong các quyết định trình bày mà không thay đổi hành vi nghiệp vụ chuẩn"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION",
      "exception_id": "P2-CRIT-EXC-015",
      "selected_disposition": "CONFIRM_NORMAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commerce Experience phải ưu tiên trải nghiệm người dùng trong các quyết định trình bày mà không thay đổi hành vi nghiệp vụ chuẩn.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-UPDATE-01-029",
    "previous_temporary_key": "TMP-BRD-UPDATE-01-029",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Business Principles",
    "source_context_sha256": "63dc655309f8a4806db68f44a8ff990ca5872e6b558f1e8852306197a866f64a",
    "source_document": "docs/BRD/BRD-UPDATE-01.md",
    "source_fingerprint": "8eeaf45d08df3e40528f9792d5fc12fbe58bf6086222b3bd047c3b0bc9e95bad",
    "source_lines": "L904-L915",
    "source_section": "17. Business Principles"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R010"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R029",
  "title": "Experience First",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R030 — Business Model First

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_MODEL_ROOT_TRACE_V1",
      "criterion_id": "BRD-UPDATE-01-R030-AC001",
      "given": "a Commerce Experience candidate with an identified Business Model",
      "observable_evidence": "Business Model identifier, experience identifier, creation trace, and publication trace",
      "then": "the accepted experience and publication evidence reference that Business Model as their origin",
      "verifies": [
        "BRD-UPDATE-01-R030-O001"
      ],
      "when": "creation or publication is requested"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_MODEL_ROOT_TRACE_V1",
      "criterion_id": "BRD-UPDATE-01-R030-AC002",
      "given": "a Commerce Experience candidate with no resolvable Business Model origin",
      "observable_evidence": "unresolved origin, conformance result, rejection reason, and publication state",
      "then": "the request is rejected as non-conforming and no unrooted publication is accepted",
      "verifies": [
        "BRD-UPDATE-01-R030-O001"
      ],
      "when": "creation or publication is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R030-AC001",
        "BRD-UPDATE-01-R030-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R030-O001",
      "obligation_text": "Creation and publication of every Commerce Experience is traceably rooted in an identified Business Model."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Model là điểm khởi đầu của mọi Commerce Experience trên nền tảng YSim.",
  "provenance": {
    "allocation_contract": "BUSINESS_PRINCIPLES_CHILD_RECONCILIATION",
    "approved_decisions": [
      "HUMAN_DECISION_2026-07-14"
    ],
    "identity_origin": "PHASE_2C_NEW_ALLOCATION",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6I. Business Principles",
    "source_context_sha256": "570dd63c76e846645aa4563a910b0ba891da8c6cb160944ab082cf4f58b5f5ff",
    "source_document": "docs/BRD/BRD-UPDATE-01.md"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-UPDATE-01-R010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R010"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R030",
  "title": "Business Model First",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R031 — Template Driven

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R031-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Template Driven",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-UPDATE-01-R031-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R031-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R031-O001",
      "obligation_text": "Mỗi Commerce Experience phải được khởi tạo từ Store Template được phê duyệt thay vì xây dựng thủ công từ đầu"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Commerce Experience phải được khởi tạo từ Store Template được phê duyệt thay vì xây dựng thủ công từ đầu.",
  "provenance": {
    "allocation_contract": "BUSINESS_PRINCIPLES_CHILD_RECONCILIATION",
    "approved_decisions": [
      "HUMAN_DECISION_2026-07-14"
    ],
    "identity_origin": "PHASE_2C_NEW_ALLOCATION",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "029798f84bc8ea391103f762eea87f18127350d5a00d8294bcc7c01a30ab3b22",
    "source_document": "docs/BRD/BRD-UPDATE-01.md"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-UPDATE-01-R010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R010"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R031",
  "title": "Template Driven",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R032 — Headless Ready

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R032-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Headless Ready",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-UPDATE-01-R032-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R032-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R032-O001",
      "obligation_text": "Commerce Experience phải có khả năng sử dụng các contract API chuẩn mà không phụ thuộc vào một lớp trình bày cụ thể"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commerce Experience phải có khả năng sử dụng các contract API chuẩn mà không phụ thuộc vào một lớp trình bày cụ thể.",
  "provenance": {
    "allocation_contract": "BUSINESS_PRINCIPLES_CHILD_RECONCILIATION",
    "approved_decisions": [
      "HUMAN_DECISION_2026-07-14"
    ],
    "identity_origin": "PHASE_2C_NEW_ALLOCATION",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "fef28a7d46165c900ba41a8336ee0a8fb884718d2de7fcbe39556fb2e2ad828e",
    "source_document": "docs/BRD/BRD-UPDATE-01.md"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-UPDATE-01-R010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R010"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R032",
  "title": "Headless Ready",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-UPDATE-01-R033 — AI Ready

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R033-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by AI Ready",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-UPDATE-01-R033-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-UPDATE-01-R033-AC002",
      "given": "a v2.3 capability, configuration, or design change governed by AI Ready",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-UPDATE-01-R033-O002"
      ],
      "when": "conformance is reviewed before the change is accepted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R033-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R033-O001",
      "obligation_text": "Nền tảng phải chuẩn bị contract và metadata có quản trị để hỗ trợ khả năng AI trong tương lai"
    },
    {
      "acceptance_criterion_references": [
        "BRD-UPDATE-01-R033-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-UPDATE-01-R033-O002",
      "obligation_text": "nguyên tắc này không được diễn giải thành một tính năng sản phẩm AI active nếu chưa có yêu cầu được phê duyệt"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "non_inference_guard": "MUST_NOT_BE_INTERPRETED_AS_AN_ACTIVE_AI_PRODUCT_FEATURE_WITHOUT_AN_APPROVED_REQUIREMENT",
  "normative_statement": "Nền tảng phải chuẩn bị contract và metadata có quản trị để hỗ trợ khả năng AI trong tương lai; nguyên tắc này không được diễn giải thành một tính năng sản phẩm AI active nếu chưa có yêu cầu được phê duyệt.",
  "provenance": {
    "allocation_contract": "BUSINESS_PRINCIPLES_CHILD_RECONCILIATION",
    "approved_decisions": [
      "HUMAN_DECISION_2026-07-14"
    ],
    "identity_origin": "PHASE_2C_NEW_ALLOCATION",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "55b257eacf89e41506941ecf65514c622530798ceecffdda75b0e2831e25f741",
    "source_document": "docs/BRD/BRD-UPDATE-01.md"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-UPDATE-01-R010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R010"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-UPDATE-01-R033",
  "title": "AI Ready",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
