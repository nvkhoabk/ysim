---
document_code: ESP-01
document_name: Repository Architecture Standards
project: YSim v2.0
document_set: Engineering Standards Pack
version: 1.0
status: FROZEN
language: en-US
---

# Repository Architecture Standards

## ESP-01

---

# 1. Purpose

Repository Architecture Standards định nghĩa kiến trúc chuẩn của Source Repository trong nền tảng YSim.

Repository không chỉ lưu trữ Source Code.

Repository là nơi quản lý toàn bộ:

- Source Code
- Documentation
- AI Artifacts
- Sprint Assets
- Infrastructure
- Deployment Assets
- Testing Assets

Repository phải được tổ chức nhất quán để AI và con người có thể hiểu, mở rộng và bảo trì lâu dài.

---

# 2. Principles

Repository tuân thủ các nguyên tắc:

- Single Source of Truth
- Modular
- Domain Oriented
- AI Friendly
- Human Readable
- Predictable
- Version Controlled
- Scalable

---

# 3. Repository Objectives

Repository phải:

- dễ khám phá (Discoverable);
- dễ mở rộng;
- hỗ trợ Monorepo;
- hỗ trợ Multi-Agent AI;
- hỗ trợ CI/CD;
- hỗ trợ Traceability;
- hỗ trợ Sprint-Driven Development.

---

# 4. Repository Architecture

Repository được chia thành các tầng:

```text
Repository

├── Applications
├── Shared Packages
├── Infrastructure
├── Integrations
├── Database
├── AI Workspace
├── Documentation
├── Scripts
├── DevOps
└── Tools
```

Không được đặt Source Code ngoài các tầng chuẩn.

---

# 5. Standard Repository Layout

```text
/
├── apps/
├── packages/
├── database/
├── infrastructure/
├── integrations/
├── ai/
├── docs/
├── scripts/
├── tools/
├── .github/
├── docker/
├── configs/
├── tests/
├── package.json
├── pnpm-workspace.yaml
└── README.md
```

Các thư mục gốc phải được giữ ổn định trong suốt vòng đời dự án.

---

# 6. Applications Layer

`apps/`

Chứa các ứng dụng độc lập.

Ví dụ:

```text
apps/

api/
portal/
admin/
agency/
mobile-api/
worker/
scheduler/
```

Mỗi Application có vòng đời triển khai riêng.

---

# 7. Shared Packages Layer

`packages/`

Chứa các thư viện dùng chung.

Ví dụ:

```text
packages/

core/
shared/
contracts/
events/
utils/
sdk/
```

Packages không phụ thuộc ngược vào Applications.

---

# 8. Database Layer

`database/`

Bao gồm:

```text
database/

schema/
migrations/
seed/
fixtures/
views/
functions/
```

Migration là bất biến sau khi phát hành.

---

# 9. Integration Layer

`integrations/`

Bao gồm:

```text
gigago/
onepay/
gpay/
sms/
email/
storage/
notification/
```

Mỗi Integration phải độc lập.

Không được gọi API của nhà cung cấp trực tiếp từ Domain.

---

# 10. Infrastructure Layer

`infrastructure/`

Bao gồm:

```text
docker/
k8s/
terraform/
nginx/
monitoring/
```

Infrastructure phải được quản lý dưới dạng Infrastructure as Code khi phù hợp.

---

# 11. AI Workspace

`ai/`

Bao gồm:

```text
contracts/
planning/
discovery/
evidence/
verification/
sprints/
manifests/
templates/
```

AI Workspace là vùng làm việc chuẩn của AI Agent.

AI không được tạo Artifact ngoài Workspace nếu không có quy định khác.

---

# 12. Documentation Layer

`docs/`

Bao gồm:

```text
BRD/
ABP/
AAP/
SGP/
ESP/
DIP/
VAP/
ROP/
ADR/
CHANGELOG/
```

Documentation là một phần của Repository.

Không quản lý tài liệu kiến trúc bên ngoài Repository nếu không có yêu cầu đặc biệt.

---

# 13. Scripts Layer

`scripts/`

Bao gồm:

```text
build/
migration/
release/
validation/
seed/
automation/
```

Scripts phải:

- có khả năng chạy lặp lại;
- không phụ thuộc môi trường cục bộ;
- có tài liệu hướng dẫn.

---

# 14. Tests Layer

`tests/`

Bao gồm:

```text
unit/
integration/
contract/
performance/
fixtures/
```

Không đặt Test xen kẽ với tài liệu hoặc Infrastructure.

(Có thể cho phép co-located tests trong module nếu được ESP-07 quy định.)

---

# 15. Repository Boundaries

Repository phải phân tách rõ:

- Business
- Application
- Infrastructure
- Integration
- AI
- Documentation

Không được trộn lẫn Responsibility.

---

# 16. Repository Naming

Thư mục:

- lowercase
- kebab-case khi gồm nhiều từ

Ví dụ:

```text
customer-care/

payment-gateway/

release-tools/
```

Không sử dụng:

```text
CustomerCare/

Customer_Care/

Customercare/
```

---

# 17. Repository Rules

RS-001 — Repository sử dụng Monorepo.

RS-002 — Mọi Source Code phải thuộc đúng Layer.

RS-003 — Không đặt Business Logic trong Integration Layer.

RS-004 — Không đặt Infrastructure trong Domain Layer.

RS-005 — AI Artifact chỉ nằm trong AI Workspace.

RS-006 — Documentation được quản lý cùng Repository.

RS-007 — Repository phải hỗ trợ Traceability.

RS-008 — Repository phải hỗ trợ CI/CD.

RS-009 — Repository phải hỗ trợ Multi-Agent AI.

RS-010 — Repository Structure chỉ thay đổi thông qua Architecture Review.

---

# 18. Repository Compliance Checklist

| Rule | Validation |
|------|------------|
| RC-0101 | Repository theo Monorepo |
| RC-0102 | Layer đúng chuẩn |
| RC-0103 | AI Workspace tồn tại |
| RC-0104 | Documentation đầy đủ |
| RC-0105 | Database Layer chuẩn |
| RC-0106 | Integration tách biệt |
| RC-0107 | Infrastructure tách biệt |
| RC-0108 | Shared Packages chuẩn |
| RC-0109 | Repository hỗ trợ CI/CD |
| RC-0110 | Repository hỗ trợ Sprint-Driven Development |

---

# 19. Relationship to Other Documents

ESP-01 liên kết với:

- ABP-01 Architecture Principles
- ABP-02 Layered Architecture
- AAP-01 Repository Discovery Model
- SGP-04 Sprint Execution Governance
- ESP-02 Source Code Standards
- ESP-03 Naming Standards

Repository Architecture là nền tảng vật lý để hiện thực toàn bộ kiến trúc của YSim.

---

# 20. Document Status

**Status: FROZEN**

ESP-01 là tài liệu chuẩn hóa kiến trúc Repository của nền tảng YSim.

Mọi Repository mới và mọi Sprint triển khai phải tuân thủ Repository Architecture Standards.

---