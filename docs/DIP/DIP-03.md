---
document_code: DIP-03
document_name: Seed & Reference Data Standard
project: YSim v2.1
document_set: Development & Implementation Pack
version: 2.1
status: FROZEN
language: en-US
---

# Seed & Reference Data Standard

## DIP-03

---

# 1. Purpose

Seed & Reference Data Standard định nghĩa tiêu chuẩn xây dựng, quản lý và sử dụng dữ liệu mẫu trong toàn bộ quá trình triển khai của YSim AI Software Factory.

Seed Information là nguồn dữ liệu mặc định để AI Coding Assistant tạo ra một Capability có thể Build, Test, Demonstrate và Verify ngay sau khi hoàn thành Sprint.

Seed không chỉ phục vụ Database.

Seed còn phục vụ Frontend, Integration, Demonstration, Dashboard và Validation.

---

# 2. Position in Software Factory

```text
Business Context

↓

Architecture Context

↓

Seed & Reference Data

↓

Prompt Assembly

↓

AI Coding

↓

Validation

↓

Capability Demonstration
```

Seed Information là đầu vào bắt buộc của mọi Executable Sprint Package (ESPK).

---

# 3. Objectives

Seed & Reference Data nhằm:

- cung cấp dữ liệu mặc định cho AI;
- tạo khả năng triển khai Full-stack;
- hỗ trợ Demonstration;
- hỗ trợ Testing;
- hỗ trợ Validation;
- chuẩn hóa Integration Reference;
- tạo Dashboard và KPI mẫu.

---

# 4. Principles

Seed Management tuân thủ:

- Seed-driven Development
- Source of Truth
- Business-oriented
- Full-stack Ready
- Environment-aware
- Repeatable
- Version Controlled
- AI Friendly
- Demonstration First

---

# 5. Seed Categories

Seed được chia thành các nhóm sau:

| Category | Purpose |
|-----------|----------|
| Business Seed | Business Objects |
| Configuration Seed | Platform Configuration |
| Integration Seed | External Systems |
| Frontend Seed | UI & Experience |
| Demonstration Seed | Demo Scenarios |
| Validation Seed | Test & Verification |
| Analytics Seed | KPI & Dashboard |
| Runtime Seed | Environment Defaults |

---

# 6. Business Seed

Business Seed bao gồm:

- Organizations
- Users
- Roles
- Permissions
- Products
- Packages
- Pricing
- Inventory
- Orders
- Customers

Ví dụ:

```yaml
product:
  code: VN-ESIM-5D-5GB
  name: Vietnam eSIM 5 Days 5GB
  supplier: GIGAGO
  validity_days: 5
  data_allowance_mb: 5120
  list_price: 150000
  currency: VND
```

Business Seed phải phản ánh nghiệp vụ thực tế.

---

# 7. Integration Seed

Integration Seed định nghĩa cấu hình tham chiếu cho các đối tác.

Ví dụ:

- Gigago
- OnePay
- GPay
- PayPal
- Airwallex
- SMTP
- SMS Gateway
- Google OAuth

Ví dụ:

```yaml
payment_provider:
  code: ONEPAY
  channel: CREDIT_CARD
  display_mode: GENERIC

supplier:
  code: GIGAGO
  environment: sandbox
  timeout_ms: 30000
```

Không lưu Secret hoặc Credential thật trong Seed.

---

# 8. Frontend Seed

Frontend Seed phục vụ:

- Portal
- Storefront
- Landing Page
- Checkout
- Dashboard

Bao gồm:

- Theme
- Navigation
- Banner
- Homepage Layout
- Menu
- Footer
- Sample Content

Frontend Seed giúp Capability có giao diện chạy được ngay sau Sprint.

---

# 9. Demonstration Seed

Demonstration Seed gồm:

- Demo Users
- Demo Organizations
- Demo Orders
- Demo Payments
- Demo Storefront
- Demo Products
- Demo Customer Journey

Ví dụ:

```yaml
demo_user:
  email: admin@ysim.local
  role: PLATFORM_ADMIN

demo_store:
  code: TRAVEL_ABC
  theme: BLUE
```

Demonstration Seed không được sử dụng cho Production.

---

# 10. Validation Seed

Validation Seed phục vụ:

- Unit Test
- Integration Test
- Contract Test
- Frontend Test
- End-to-End Test

Bao gồm:

- Expected Response
- Sample Payload
- Expected Events
- Expected Database State

Validation phải có thể chạy tự động.

---

# 11. Analytics Seed

Analytics Seed gồm:

- Dashboard KPI
- Revenue
- Orders
- Conversion Rate
- Payment Success Rate
- Activation Rate

Ví dụ:

```yaml
target_metrics:
  first_5_days_july:
    orders: 500
    revenue_vnd: 75000000
    conversion_rate: 4.5
```

Analytics Seed giúp Dashboard có dữ liệu ngay sau Sprint.

---

# 12. Runtime Seed

Runtime Seed định nghĩa:

- Feature Flags
- Default Configuration
- Initial Tenant
- Initial Storefront
- Initial Theme
- Default Payment Offering

Runtime Seed không chứa Secret.

---

# 13. Seed Versioning

Mỗi Seed phải có:

- Version
- Owner
- Source
- Applicable Environment
- Last Updated

Seed được quản lý cùng Source Code.

---

# 14. Seed Lifecycle

```text
Business Definition

↓

Reference Data

↓

Seed Package

↓

AI Coding

↓

Database

↓

Frontend

↓

Testing

↓

Demonstration
```

Seed được sinh một lần và tái sử dụng trong nhiều Sprint.

---

# 15. Environment Strategy

Seed được phân loại theo môi trường:

- local
- development
- integration
- uat
- demonstration
- production (reference only)

Production chỉ sử dụng Reference Configuration, không sử dụng Demo Seed.

---

# 16. Prohibited Practices

Không được:

- lưu Production Secret;
- hardcode API Key;
- sử dụng dữ liệu khách hàng thật;
- dùng Demonstration Seed cho Production;
- tạo Seed không có Version;
- thay đổi Seed mà không cập nhật Manifest.

---

# 17. Rules

SEED-001 — Mọi Sprint phải có Seed Package.

SEED-002 — Integration phải có Reference Configuration.

SEED-003 — Capability có UI phải có Frontend Seed.

SEED-004 — Capability Demonstration phải có Demonstration Seed.

SEED-005 — Validation phải có Validation Seed.

SEED-006 — Analytics phải có KPI Seed.

SEED-007 — Runtime chỉ dùng Reference Configuration.

SEED-008 — Seed được Version hóa.

SEED-009 — Seed là Source of Context cho AI.

SEED-010 — Không lưu Secret trong Seed.

---

# 18. Compliance Checklist

| Rule | Validation |
|------|------------|
| SDC-0301 | Business Seed đầy đủ |
| SDC-0302 | Integration Seed đầy đủ |
| SDC-0303 | Frontend Seed đầy đủ |
| SDC-0304 | Demonstration Seed đầy đủ |
| SDC-0305 | Validation Seed đầy đủ |
| SDC-0306 | Analytics Seed đầy đủ |
| SDC-0307 | Runtime Seed đúng chuẩn |
| SDC-0308 | Không chứa Secret |
| SDC-0309 | Seed có Version |
| SDC-0310 | Tuân thủ DIP |

---

# 19. Relationship to Other Documents

DIP-03 liên kết với:

- DIP-00 Implementation Constitution
- DIP-01 Executable Sprint Package Standard
- DIP-02 AI Context Resolution & Prompt Assembly Standard
- BRD
- ABP
- ESP
- SGP
- VAP

DIP-03 là tài liệu chuẩn hóa toàn bộ Seed & Reference Data của YSim AI Software Factory.

---

# 20. Document Status

**Status: FROZEN**

Từ phiên bản 2.1, mọi Capability của YSim phải được triển khai cùng một **Seed Package** đầy đủ.

Seed Package là nguồn dữ liệu chuẩn để AI Coding Assistant sinh Backend, Frontend, Demonstration, Validation và Dashboard theo mô hình **Full-stack Capability Delivery**, đồng thời là nguồn **Reference Data** thống nhất cho toàn bộ vòng đời phát triển và vận hành của nền tảng.