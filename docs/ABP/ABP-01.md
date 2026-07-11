---
document_code: ABP-01
document_name: Repository Architecture
project: YSim v2.0
document_set: Architecture Baseline Pack
version: 1.0
status: FROZEN
language: en-US
---

# Repository Architecture

## ABP-01

---

# 1. Purpose

Repository Architecture định nghĩa cấu trúc Repository chuẩn của nền tảng YSim.

Mục tiêu là:

- chuẩn hóa Repository Structure;
- chuẩn hóa Module Organization;
- chuẩn hóa Ownership;
- chuẩn hóa Dependency;
- hỗ trợ AI Implementation;
- hỗ trợ Repository Discovery.

Repository Structure là bất biến trong suốt vòng đời dự án.

---

# 2. Repository Principles

Repository được tổ chức theo các nguyên tắc:

- Domain First
- Module First
- Contract First
- Monorepo
- Shared Kernel
- Clear Ownership
- AI Friendly
- Testable
- Maintainable

---

# 3. Repository Layout

```text
/
├── apps/
├── packages/
├── database/
├── integrations/
├── infrastructure/
├── ai/
├── docs/
├── scripts/
├── tools/
├── tests/
└── .github/
```

---

# 4. Repository Responsibilities

| Folder | Responsibility |
|----------|---------------|
| apps | Deployable applications |
| packages | Business modules & shared libraries |
| database | Schema, migration, seed |
| integrations | External integrations |
| infrastructure | Docker, Kubernetes, IaC |
| ai | AI assets, Sprint Packs, CIP |
| docs | Project documentation |
| scripts | Build & automation scripts |
| tools | Internal developer tools |
| tests | Shared testing assets |

---

# 5. Apps Layer

`apps/` chỉ chứa các ứng dụng có thể triển khai.

Ví dụ:

```text
apps/

api/

portal/

customer-portal/

worker/

scheduler/

admin/

mobile-api/
```

Apps không chứa Business Logic.

Business Logic luôn nằm trong packages.

---

# 6. Packages Layer

`packages/` là trung tâm của Repository.

Mỗi Package đại diện cho một Module hoặc Shared Component.

Ví dụ:

```text
packages/

commercial/

order/

payment/

inventory/

fulfillment/

customer/

notification/

configuration/

security/

shared/
```

---

# 7. Shared Kernel

Shared Kernel chỉ chứa các thành phần dùng chung.

Ví dụ:

- Common Types
- Base Classes
- Shared Utilities
- Error Definitions
- Result Objects
- Framework Adapters

Không chứa Business Logic của Domain.

---

# 8. Database Layer

Database được quản lý tập trung.

```text
database/

schema/

migration/

seed/

fixtures/

reference-data/
```

Migration chỉ được thêm mới.

Không sửa Migration đã phát hành.

---

# 9. Integration Layer

Integration được tách riêng khỏi Business Domain.

Ví dụ:

```text
integrations/

gigago/

onepay/

gpay/

email/

sms/

webhook/

partner/
```

Business Domain không giao tiếp trực tiếp với hệ thống ngoài.

Mọi giao tiếp phải thông qua Integration Layer.

---

# 10. AI Layer

Toàn bộ tài liệu phục vụ AI được đặt trong `ai/`.

Ví dụ:

```text
ai/

roadmap/

contracts/

sprints/

cip/

prompts/

manifests/

reports/

templates/
```

AI không đọc toàn bộ Repository.

AI đọc đúng Artifact được chỉ định trong Sprint Contract.

---

# 11. Documentation Layer

Tài liệu được quản lý tập trung.

```text
docs/

BRD/

DMS/

DBD/

API/

ABP/

DIP/

ESP/

SGP/

VAP/

ORP/
```

Documentation là Source of Truth.

---

# 12. Ownership Rules

Mỗi thư mục đều có Ownership rõ ràng.

| Area | Owner |
|------|-------|
| apps | Application Team |
| packages | Domain Team |
| database | Database Team |
| integrations | Integration Team |
| ai | AI Engineering |
| docs | Architecture Team |

AI chỉ được thay đổi các thành phần thuộc Sprint Ownership.

---

# 13. Repository Discovery

Repository Discovery phải thu thập tối thiểu:

- Existing Apps
- Existing Packages
- Existing Database
- Existing APIs
- Existing Integration
- Existing Tests
- Existing Documents
- Existing Technical Debt

Đây là bước bắt buộc trước mỗi Sprint.

---

# 14. Repository Principles

RP-001 — Monorepo.

RP-002 — Domain First.

RP-003 — Package Ownership.

RP-004 — Shared Kernel.

RP-005 — No Business Logic in Apps.

RP-006 — Integration Isolation.

RP-007 — Documentation First.

RP-008 — AI Friendly Repository.

RP-009 — One Module, One Responsibility.

RP-010 — Repository must remain discoverable.

---

# 15. Repository Constitution

Repository Architecture là chuẩn bắt buộc cho toàn bộ mã nguồn của nền tảng YSim.

Mọi Sprint, Module hoặc Repository mới phải tuân thủ cấu trúc và nguyên tắc được định nghĩa trong tài liệu này.

---

# Document Status

**Status: FROZEN**

ABP-01 là tài liệu nền tảng quy định cấu trúc Repository chuẩn của nền tảng YSim.

Mọi thay đổi đối với Repository Structure phải được Architecture Review và Approval trước khi áp dụng.

---