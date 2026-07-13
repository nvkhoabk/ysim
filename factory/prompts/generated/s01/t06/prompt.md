# ROLE

You are the primary AI coding agent operating the YSim Software Factory.

# EXECUTION ID

- Sprint: S01
- Task: T06
- Prompt ID: s01-t06
- Provider: codex

# OBJECTIVE

Establish the shared background execution foundation using BullMQ and a scheduler abstraction, including queue naming, worker lifecycle, retry/backoff defaults, failed-job handling, observability seams, and test coverage without implementing any production business job.

# REPOSITORY SNAPSHOT

## Branch

feat/s01-platform-foundation

## Working Tree

```text
M factory/contexts/generated/s00/context.json
 M factory/executions/s00/t00/plan.json
 M factory/executions/s00/t00/report.json
 M factory/executions/s00/t00/report.md
 M factory/index/catalog.json
 M factory/index/documents.json
 M factory/index/knowledge.json
 M factory/prompts/generated/s00/t00/manifest.json
 M factory/prompts/generated/s00/t00/prompt.json
 M factory/prompts/generated/s00/t00/prompt.md
 M knowledge/catalog/capabilities.json
 M knowledge/catalog/document-sets.json
 M knowledge/catalog/documents.json
 M knowledge/catalog/integrations.json
 M knowledge/catalog/knowledge-graph.json
 M knowledge/catalog/relationships.json
 M knowledge/catalog/summary.json
 M knowledge/normalized/documents.json
```

## Recent Commits

```text
c30889e (HEAD -> feat/s01-platform-foundation, origin/feat/s01-platform-foundation) chore(factory): refresh generated knowledge artifacts
ed2d2c1 chore(factory): refresh generated knowledge artifacts
6a980c8 docs(s01): expand tasks t06-t10 and add human acceptance
1da2ff0 (tag: s01-t05-complete) feat(s01-t05): establish local infrastructure baseline
72c3aca (tag: s01-t04-complete) feat(s01-t04): add structured logging and platform error handling
e5e1ac3 (tag: s01-t03-complete) feat(s01-t03): add typed configuration and environment validation
7548433 prepared
af7d70e (tag: s01-t02-complete) feat(s01-t02): bootstrap NestJS API application
bdcec14 (tag: s01-t01-complete) feat(s01-t01): establish monorepo workspace foundation
e3ed5dd prepared
```

## Repository Tree

```text
.
./.agents
./.mypy_cache
./.mypy_cache/.gitignore
./.mypy_cache/3.11
./.mypy_cache/CACHEDIR.TAG
./.ruff_cache
./.ruff_cache/.gitignore
./.ruff_cache/0.15.21
./.ruff_cache/CACHEDIR.TAG
./ACCEPTANCE.md
./DOCUMENT_BASELINE.md
./EXECUTION_ORDER.md
./GOVERNANCE.md
./HUMAN_ACCEPTANCE_FRAMEWORK.md
./README.md
./SCOPE.md
./SPRINT-01-INSTALL.md
./TARGET_STRUCTURE.md
./ai
./ai/manifests
./ai/sprints
./ai/templates
./docs
./docs/AAP
./docs/ABP
./docs/AFM
./docs/BRD
./docs/CAP
./docs/DIP
./docs/ECS
./docs/ESP
./docs/ESPK
./docs/INDEX.md
./docs/MASTER_INDEX.md
./docs/PCS
./docs/POL
./docs/ROP
./docs/SGP
./docs/UXF
./docs/YADF
./factory
./factory/README.md
./factory/config
./factory/context-manifests
./factory/contexts
./factory/evidence
./factory/executions
./factory/index
./factory/manifests
./factory/prompt-manifests
./factory/prompts
./factory/providers
./factory/releases
./factory/reports
./factory/runtime
./factory/schemas
./factory/seeds
./factory/templates
./factory/validation
./human-acceptance
./human-acceptance/s01-t06-human-acceptance.md
./human-acceptance/s01-t07-human-acceptance.md
./human-acceptance/s01-t08-human-acceptance.md
./human-acceptance/s01-t09-human-acceptance.md
./human-acceptance/s01-t10-human-acceptance.md
./knowledge
./knowledge/README.md
./knowledge/api
./knowledge/business-rules
./knowledge/cache
./knowledge/capabilities
./knowledge/catalog
./knowledge/domains
./knowledge/entities
./knowledge/glossary
./knowledge/integrations
./knowledge/knowledge.yaml
./knowledge/normalized
./knowledge/raw
./knowledge/seed
./knowledge/ui
./runtime
./runtime/auto-runner
./runtime/cache
./runtime/codex
./runtime/codex-readiness
./runtime/reports
./runtime/state
./runtime/tmp
./scripts
./scripts/bootstrap.sh
./scripts/build-context.legacy.sh
./scripts/build-context.sh
./scripts/build-factory-index.legacy.sh
./scripts/build-factory-index.sh
./scripts/build-knowledge.legacy.sh
./scripts/build-knowledge.sh
./scripts/build-prompt.legacy.sh
./scripts/build-prompt.sh
./scripts/build-sprint-01-context.sh
./scripts/build-sprint-01-prompt.sh
./scripts/commission.sh
./scripts/install-sprint-01.sh
./scripts/local-infra.sh
./scripts/regenerate-sprint-01-prompt-manifests.py
./scripts/resume.sh
./scripts/run-execution.sh
./scripts/run-sprint-01-auto.sh
./scripts/run-sprint-01-task.sh
./scripts/run-sprint-01.sh
./scripts/run-sprint.sh
./scripts/run-task.sh
./scripts/validate-sprint-01-pack.sh
./scripts/validate.sh
./scripts/verify-factory.sh
./scripts/verify-local-infra.sh
./scripts/ysf.sh
./sprint.json
./tools
./tools/context
./tools/indexing
./tools/knowledge
./tools/prompt
./tools/ysf
```

# SOURCE DOCUMENTS

- ABP-00 (docs/ABP/ABP-00.md)
- ABP-01 (docs/ABP/ABP-01.md)
- ABP-02 (docs/ABP/ABP-02.md)
- ABP-03 (docs/ABP/ABP-03.md)
- ABP-18 (docs/ABP/ABP-18.md)
- AFM-00 (docs/AFM/AFM-00.md)
- CAP-00 (docs/CAP/CAP-00.md)
- DIP-00 (docs/DIP/DIP-00.md)
- DIP-01 (docs/DIP/DIP-01.md)
- DIP-02 (docs/DIP/DIP-02.md)
- DIP-04 (docs/DIP/DIP-04.md)
- DIP-05 (docs/DIP/DIP-05.md)
- DIP-06 (docs/DIP/DIP-06.md)
- DIP-09 (docs/DIP/DIP-09.md)
- ECS-00 (docs/ECS/ECS-00.md)
- ESP-00 (docs/ESP/ESP-00.md)
- ESP-01 (docs/ESP/ESP-01.md)
- ESP-02 (docs/ESP/ESP-02.md)
- ESPK-S00 (docs/ESPK/ESPK-S00.md)
- PCS-00 (docs/PCS/PCS-00.md)
- POL-00 (docs/POL/POL-00.md)
- UXF-00 (docs/UXF/UXF-00.md)
- UXF-02 (docs/UXF/UXF-02.md)
- UXF-05 (docs/UXF/UXF-05.md)
- YADF-00 (docs/YADF/YADF-00.md)
- AAP-01 (docs/AAP/AAP-01.md)
- AAP-02 (docs/AAP/AAP-02.md)
- AAP-03 (docs/AAP/AAP-03.md)
- AAP-04 (docs/AAP/AAP-04.md)
- AAP-05 (docs/AAP/AAP-05.md)

# CONTEXT

# Source: ABP-00

- Path: `docs/ABP/ABP-00.md`
- Set: `ABP`
- Version: `1.0`
- Status: `FROZEN`

# Architecture Principles

## ABP-00

---

# 1. Purpose

Architecture Principles định nghĩa các nguyên tắc kiến trúc cốt lõi của nền tảng YSim.

Các nguyên tắc này là nền tảng để:

- thiết kế hệ thống;
- triển khai Sprint;
- review kiến trúc;
- review source code;
- đánh giá chất lượng;
- mở rộng hệ thống.

Architecture Principles là tài liệu bất biến (Architecture Constitution).

Mọi thiết kế và triển khai phải tuân thủ tài liệu này.

---

# 2. Objectives

Architecture Principles nhằm:

- Chuẩn hóa kiến trúc.
- Chuẩn hóa Domain Ownership.
- Chuẩn hóa Dependency.
- Chuẩn hóa Module Boundary.
- Chuẩn hóa Integration.
- Chuẩn hóa Event-Driven Architecture.
- Chuẩn hóa Configuration-Driven Platform.
- Chuẩn hóa Security.
- Chuẩn hóa Observability.
- Chuẩn hóa AI Development.
- Chuẩn hóa Full-stack Capability Delivery.
- Chuẩn hóa Experience-driven Architecture.

---

# 3. Architecture Layers

YSim sử dụng kiến trúc phân lớp.

```text
Experience

↓

Application

↓

Domain

↓

Infrastructure

↓

Platform
```

Nguyên tắc:

Layer chỉ được phụ thuộc xuống dưới.

Không phụ thuộc ngược.

---

# 4. Principle AP-001

## Business First

Business Requirement quyết định Architecture.

Architecture không quyết định Business.

---

# 5. Principle AP-002

## Business Registry is Source of Truth

Business Object

Capability

Policy

Event

Snapshot

được định nghĩa duy nhất trong Enterprise Registry.

Source Code không được định nghĩa lại.

---

# 6. Principle AP-003

## Domain Ownership

Mỗi Business Domain có Ownership riêng.

Một Domain:

- quản lý Business Object của mình;
- quản lý Event của mình;
- quản lý Policy của mình.

Không được sửa Domain khác nếu chưa được phê duyệt.

---

# 7. Principle AP-004

## Clear Module Boundary

Module phải có Boundary rõ ràng.

Module chỉ giao tiếp thông qua:

- API
- Event
- Shared Contract

Không truy cập trực tiếp Implementation của Module khác.

---

# 8. Principle AP-005

## Contract First

Business Contract được xác định trước.

Sau đó mới triển khai Source Code.

Contract bao gồm:

- API
- Event
- Policy
- Snapshot
- Configuration

---

# 9. Principle AP-006

## Configuration over Hard-code

Business Behavior ưu tiên điều khiển bằng Configuration.

Không Hard-code nếu có thể cấu hình.

---

# 10. Principle AP-007

## Event-Driven Architecture

Business Event là cơ chế giao tiếp chuẩn giữa các Domain.

Không gọi trực tiếp nếu Event phù hợp hơn.

Mọi Business Event phải được đăng ký trong Event Registry.

---

# 11. Principle AP-008

## Snapshot as Business Evidence

Snapshot là Business Evidence.

Snapshot:

- Immutable
- Versioned
- Traceable

Snapshot không phải History.

---

# 12. Principle AP-009

## Policy Driven Platform

Business Behavior được quyết định bởi Policy.

Business Rule chỉ mô tả Logic.

Policy quyết định Rule nào được sử dụng.

---

# 13. Principle AP-010

## Secure by Design

Security là yêu cầu mặc định.

Không phải tính năng bổ sung.

Mọi Module phải hỗ trợ:

- Authentication
- Authorization
- Audit
- Data Protection

---

# 14. Principle AP-011

## Observable by Default

Mọi Module phải hỗ trợ:

- Logging
- Metrics
- Monitoring
- Trace
- Health Check

Observability không được bổ sung sau.

---

# 15. Principle AP-012

## AI Implements, Never Defines Architecture

AI chỉ triển khai.

AI không được:

- tạo Business Object;
- tạo Capability;
- tạo Policy;
- tạo Event;
- tạo Snapshot;
- thay đổi Architecture.

AI chỉ được tạo Architecture Change Proposal.

---

# 16. Principle AP-013

## Repository Discovery First

Trước mọi Sprint:

AI phải thực hiện:

- Repository Discovery
- Dependency Analysis
- Gap Analysis

Sau đó mới triển khai.

---

# 17. Principle AP-014

## Small and Independent Sprint

Sprint triển khai theo Technical Capability.

Sprint phải:

- nhỏ;
- độc lập;
- test được;
- release được.

---

# 18. Principle AP-015

## Traceability

Mọi Artifact phải Trace được.

```text
Requirement

↓

Capability

↓

Business Object

↓

Policy

↓

Rule

↓

Event

↓

Snapshot

↓

API

↓

Source Code

↓

Test
```

---

# 19. Principle AP-016

## One Source of Truth

Mỗi khái niệm chỉ có một Source of Truth.

Ví dụ:

| Artifact | Source of Truth |
|----------|-----------------|
| Business Object | BO Registry |
| Capability | Capability Registry |
| Policy | Policy Registry |
| Event | Event Registry |
| Snapshot | Snapshot Registry |
| Sprint Scope | Sprint Contract |

Không được định nghĩa trùng lặp.

---

# 20. Principle AP-017

## Backward Compatibility

Public Contract phải ưu tiên tương thích ngược.

Nếu phá vỡ Compatibility:

- phải Version.
- phải Migration.
- phải Approval.

---

# 21. Principle AP-018

## Architecture Change Control

Mọi thay đổi kiến trúc phải:

- Architecture Review
- Impact Analysis
- Approval

Không thay đổi trực tiếp trong Sprint.

---

# 22. Principle AP-019

## Operational Readiness

Một Module chỉ được Release khi:

- Build PASS
- Test PASS
- Monitoring
- Logging
- Alert
- Runbook (nếu yêu cầu)

---

# 23. Principle AP-020

## Long-term Maintainability

Mọi quyết định kiến trúc phải ưu tiên:

- đơn giản;
- mở rộng;
- bảo trì;
- quan sát;
- kiểm thử;
- tự động hóa.

Không tối ưu cục bộ làm ảnh hưởng kiến trúc tổng thể.


---

# 23A. Principle AP-021

## Experience First

Đối với các Capability có giao diện người dùng, Experience là một phần của kiến trúc, không phải lớp trình bày độc lập.

Kiến trúc phải được thiết kế từ Customer Journey và Business Experience trước khi hiện thực hóa bằng API hoặc Source Code.

---

# 23B. Principle AP-022

## Full-stack Capability Delivery

Một Capability hoàn chỉnh bao gồm:

- Backend
- API
- Frontend
- Seed Data
- Capability Demonstration
- Verification

Không triển khai Backend độc lập đối với Capability có giao diện người dùng.

---

# 23C. Principle AP-023

## Engine-based Architecture

Các nền tảng lớn như Commerce Experience Platform phải được thiết kế theo các Engine độc lập (Theme Engine, Experience Composition Engine, Publishing Engine, Analytics Engine...) để giảm Coupling và tăng khả năng mở rộng.


---

# 24. Architecture Constitution

Architecture Principles là "Hiến pháp kiến trúc" của nền tảng YSim.

Mọi tài liệu thuộc:

- ABP
- DIP
- ESP
- SGP
- VAP
- ORP
- CIP

đều phải tuân thủ các nguyên tắc trong ABP-00.

---

# Document Status

**Status: FROZEN**

ABP-00 là tài liệu nền tảng của Architecture Baseline Pack và là chuẩn kiến trúc bất biến của nền tảng YSim.

Mọi thay đổi đối với các nguyên tắc trong tài liệu này phải được thực hiện thông qua Architecture Governance và phê duyệt chính thức trước khi áp dụng.

---


---

# Source: ABP-01

- Path: `docs/ABP/ABP-01.md`
- Set: `ABP`
- Version: `1.0`
- Status: `FROZEN`

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


---

# Source: ABP-02

- Path: `docs/ABP/ABP-02.md`
- Set: `ABP`
- Version: `1.0`
- Status: `FROZEN`

# Module Architecture

## ABP-02

---

# 1. Purpose

Module Architecture định nghĩa cấu trúc chuẩn của một Module trong nền tảng YSim.

Mục tiêu:

- Chuẩn hóa Module Structure.
- Chuẩn hóa Layering.
- Chuẩn hóa Dependency.
- Chuẩn hóa Ownership.
- Chuẩn hóa Runtime Boundary.
- Chuẩn hóa AI Implementation.

Module là đơn vị triển khai nhỏ nhất của Platform.

---

# 2. Module Principles

Mọi Module phải tuân thủ các nguyên tắc sau:

- Single Responsibility
- High Cohesion
- Low Coupling
- Contract First
- Domain Ownership
- Event Driven
- Testable
- Observable

---

# 3. Module Definition

Module là một đơn vị triển khai độc lập, chịu trách nhiệm hiện thực một hoặc nhiều **Business Capability** có liên quan trong cùng một **Business Domain**.

Một Module:

- Có Ownership riêng.
- Có API riêng (nếu cần).
- Có Event riêng.
- Có Test riêng.
- Có Documentation riêng.
- Có Lifecycle riêng.

---

# 4. Module Layering

Mỗi Module sử dụng cấu trúc phân lớp chuẩn.

```text
Module

├── Application
├── Domain
├── Infrastructure
└── Interface
```

Không được bổ sung Layer mới nếu chưa được Architecture Review.

---

# 5. Application Layer

Application Layer chịu trách nhiệm:

- Use Cases
- Command
- Query
- Orchestration
- Transaction Boundary
- Permission Check

Application Layer không chứa Business Persistence.

---

# 6. Domain Layer

Domain Layer là trung tâm của Module.

Bao gồm:

- Aggregate
- Entity
- Value Object
- Domain Service
- Domain Event
- Domain Policy
- Domain Validation

Domain Layer không phụ thuộc Infrastructure.

---

# 7. Infrastructure Layer

Infrastructure Layer hiện thực các thành phần kỹ thuật.

Ví dụ:

- Repository
- ORM
- External Connector
- Queue Adapter
- Cache
- Storage
- Mail
- Payment Gateway Adapter

Infrastructure không chứa Business Decision.

---

# 8. Interface Layer

Interface Layer cung cấp điểm truy cập vào Module.

Ví dụ:

- REST Controller
- GraphQL Resolver
- Message Consumer
- Scheduler Entry
- CLI
- Admin Endpoint

Interface chỉ chuyển tiếp yêu cầu vào Application Layer.

---

# 9. Module Folder Structure

Ví dụ:

```text
payment/

application/
domain/
infrastructure/
interface/
tests/
docs/
```

Không đặt Business Logic ngoài Module.

---

# 10. Module Ownership

Mỗi Module có Ownership rõ ràng.

Ownership bao gồm:

- Business Owner
- Architecture Owner
- Sprint Ownership
- Source Code Ownership

Không có Module "không chủ".

---

# 11. Module Contract

Mỗi Module công bố Contract.

Contract có thể gồm:

- Public API
- Published Events
- Consumed Events
- Configuration
- Permissions
- Error Codes

Module khác chỉ được sử dụng Contract công khai.

---

# 12. Module Communication

Các Module giao tiếp thông qua:

- API
- Event
- Shared Contract

Không truy cập trực tiếp Internal Implementation của Module khác.

---

# 13. Module Dependency Rules

Module chỉ được phụ thuộc:

- Shared Kernel
- Public Contract của Module khác
- Platform Services

Không phụ thuộc trực tiếp vào:

- Database của Module khác
- Internal Repository
- Internal Service
- Internal Entity

---

# 14. Module Lifecycle

Mỗi Module có Lifecycle.

```text
Design

↓

Implementation

↓

Testing

↓

Release

↓

Maintenance

↓

Deprecation

↓

Retirement
```

---

# 15. Module Observability

Mọi Module phải hỗ trợ:

- Logging
- Metrics
- Health Check
- Trace ID
- Audit (nếu áp dụng)

Observability là yêu cầu bắt buộc.

---

# 16. Module Testability

Mỗi Module phải có:

- Unit Test
- Contract Test
- Integration Test (nếu cần)

Business Scenario Test được thực hiện ở mức Sprint.

---

# 17. Module Versioning

Module hỗ trợ Version.

Breaking Change phải:

- Version.
- Migration.
- Approval.

Không thay đổi Public Contract trực tiếp.

---

# 18. AI Implementation Rules

AI chỉ được triển khai trong phạm vi Module.

AI không được:

- tạo Module mới;
- thay đổi Module Boundary;
- thay đổi Ownership.

Nếu cần thay đổi:

→ Architecture Change Proposal.

---

# 19. Module Principles

MA-001 — One Module, One Responsibility.

MA-002 — Business Logic belongs to Domain Layer.

MA-003 — Application orchestrates.

MA-004 — Infrastructure implements technology.

MA-005 — Interface exposes contracts.

MA-006 — Module owns its data.

MA-007 — Module communicates by contract.

MA-008 — Module publishes events.

MA-009 — Module is independently testable.

MA-010 — Module is independently deployable (when architecture allows).

---

# 20. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0201 | Module có Ownership rõ ràng |
| ACC-0202 | Business Logic chỉ nằm trong Domain Layer |
| ACC-0203 | Application Layer không truy cập trực tiếp Infrastructure của Module khác |
| ACC-0204 | Infrastructure không chứa Business Rule |
| ACC-0205 | Interface không chứa Business Logic |
| ACC-0206 | Module chỉ sử dụng Public Contract |
| ACC-0207 | Module có Logging, Metrics và Health Check |
| ACC-0208 | Module có Test tối thiểu theo chuẩn YADF |
| ACC-0209 | Module công bố đầy đủ API/Event Contract |
| ACC-0210 | Module tuân thủ Domain Ownership |

Checklist này được sử dụng trong:

- Architecture Review.
- Code Review.
- AI Review.
- CI/CD Validation.

---

# 21. Document Status

**Status: FROZEN**

ABP-02 là tài liệu nền tảng quy định kiến trúc chuẩn của mọi Module trong nền tảng YSim.

Mọi Module mới phải tuân thủ tài liệu này trước khi được đưa vào triển khai hoặc phát hành.

---


---

# Source: ABP-03

- Path: `docs/ABP/ABP-03.md`
- Set: `ABP`
- Version: `1.0`
- Status: `FROZEN`

# Dependency Rules

## ABP-03

---

# 1. Purpose

Dependency Rules định nghĩa các quy tắc phụ thuộc giữa các Module trong nền tảng YSim.

Mục tiêu:

- loại bỏ Circular Dependency;
- chuẩn hóa Module Communication;
- đảm bảo Domain Boundary;
- đảm bảo Repository Discoverability;
- đảm bảo AI Implementation nhất quán.

Dependency Rules là một phần của Architecture Constitution.

---

# 2. Principles

Dependency phải tuân thủ:

- One Direction
- Contract First
- Domain Ownership
- Explicit Dependency
- No Hidden Dependency

Không được phụ thuộc ngầm.

---

# 3. Dependency Types

Platform định nghĩa bốn loại Dependency.

| Type | Description |
|-------|-------------|
| Compile Dependency | Import Source Code |
| Runtime Dependency | Runtime Invocation |
| Event Dependency | Publish / Subscribe |
| Shared Contract Dependency | DTO / Interface / Contract |

Mỗi Dependency phải được xác định rõ loại.

---

# 4. Layer Dependency

Dependency giữa các Layer.

```text
Presentation
        │
        ▼
Application
        │
        ▼
Domain
        │
        ▼
Infrastructure
        │
        ▼
Platform
```

Không được phụ thuộc ngược.

---

# 5. Module Dependency

Module chỉ được phụ thuộc:

- Shared Kernel
- Public Contract
- Platform Service

Không được Import:

- Internal Entity
- Internal Repository
- Internal Service
- Internal Database

---

# 6. Domain Ownership

Domain sở hữu:

- Business Object
- Event
- Policy
- Snapshot
- API

Module khác không được sửa.

---

# 7. Communication Rules

Module chỉ giao tiếp qua:

- REST API
- Internal API
- Event
- Queue
- Shared Contract

Không được truy cập trực tiếp Database của Module khác.

---

# 8. Shared Kernel Rules

Shared Kernel chỉ chứa:

- Base Types
- Common Interface
- Common Exception
- Utility
- Result Object

Không chứa:

- Business Rule
- Business Service
- Domain Entity

---

# 9. Integration Rules

Integration luôn thông qua:

```text
Business Module

↓

Gateway

↓

Connector

↓

External System
```

Business Module không gọi Supplier trực tiếp.

---

# 10. Event Dependency

Business Event là Dependency yếu (Loose Coupling).

Publisher không biết Subscriber.

Subscriber đăng ký Event.

Không được gọi ngược Publisher.

---

# 11. API Dependency

API chỉ được gọi:

- Public API
- Versioned API

Không gọi Internal Endpoint.

---

# 12. Database Dependency

Database Ownership thuộc Module.

Module khác:

- không SELECT trực tiếp;
- không UPDATE trực tiếp;
- không JOIN trực tiếp.

Trao đổi dữ liệu thông qua Contract.

---

# 13. Configuration Dependency

Configuration được đọc qua Configuration Service.

Không đọc trực tiếp Database.

Không Hard-code.

---

# 14. Security Dependency

Security Module được phép được tất cả Module sử dụng.

Security không phụ thuộc Business Domain.

---

# 15. Logging Dependency

Logging thông qua Logging Framework.

Không gọi Logger của Module khác.

---

# 16. Notification Dependency

Business Module Publish Event.

Notification Subscribe Event.

Business Module không gửi Notification trực tiếp.

---

# 17. Analytics Dependency

Analytics đọc:

- Snapshot
- Event
- Reporting View

Không đọc Runtime Database để tạo báo cáo.

---

# 18. Dependency Matrix

| From | Allowed |
|------|---------|
| Commercial | Shared, Configuration, Security, Integration |
| Order | Commercial, Shared, Configuration |
| Payment | Order (Contract), Commercial (Contract), Shared |
| Inventory | Order (Contract), Shared |
| Fulfillment | Inventory, Payment (Contract), Shared |
| Notification | Event Bus, Shared |
| Analytics | Snapshot, Event, Reporting View |
| Configuration | Shared |
| Security | Shared |
| Operations | Shared |

Mọi Dependency khác phải được Architecture Review.

---

# 19. Forbidden Dependencies

Không được:

- Circular Dependency
- Cross Database Query
- Shared Entity
- Shared Repository
- Business Logic trong Shared
- Module gọi Internal Service của Module khác

---

# 20. AI Dependency Rules

AI không được:

- tạo Dependency mới;
- Import Internal Module;
- Bypass Contract;
- tạo Circular Dependency.

Nếu cần:

↓

Architecture Change Proposal.

---

# 21. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0301 | Không có Circular Dependency |
| ACC-0302 | Không Import Internal Module |
| ACC-0303 | Không Cross Database Query |
| ACC-0304 | Chỉ dùng Public Contract |
| ACC-0305 | Event tuân thủ Event Registry |
| ACC-0306 | Shared Kernel không chứa Business Logic |
| ACC-0307 | Module Ownership không bị vi phạm |
| ACC-0308 | Integration thông qua Gateway |
| ACC-0309 | Configuration không Hard-code |
| ACC-0310 | Dependency Matrix được tuân thủ |

Checklist này được sử dụng bởi:

- Architecture Review
- AI Review
- CI/CD Validation
- Code Review

---

# 22. Document Status

**Status: FROZEN**

ABP-03 quy định toàn bộ Dependency Rules của nền tảng YSim.

Mọi Module, Sprint và AI Implementation phải tuân thủ các quy tắc trong tài liệu này.

---


---

# Source: ABP-18

- Path: `docs/ABP/ABP-18.md`
- Set: `ABP`
- Version: `1.0`
- Status: `Draft`

# ABP-18 — Runtime Resolution Architecture

---

# 1. Purpose

This document defines the Runtime Resolution Architecture of the YSim Platform.

The Runtime Resolution Architecture is responsible for transforming an incoming request into a fully resolved commercial experience by combining Experience Runtime, Business Runtime, Policy Runtime and Published Snapshots.

This document establishes the canonical runtime behavior used by all applications within the platform.

---

# 2. Objectives

The Runtime Resolution Architecture shall provide:

- Deterministic request resolution
- Experience composition
- Business capability resolution
- Policy evaluation
- Configuration inheritance
- Published snapshot consumption
- Runtime fallback
- Immutable rendering
- Runtime scalability

---

# 3. Architectural Philosophy

The Runtime Resolution Engine is an orchestration layer.

It does **not** own business logic.

It does **not** own business data.

It resolves references, composes runtime context and delegates business execution to Platform Capabilities.

```
Request

↓

Runtime Resolution

↓

Platform Capabilities

↓

Resolved Experience

↓

Rendering
```

---

# 4. Runtime Architecture

```
HTTP Request

↓

Runtime Context Resolver

↓

Experience Resolver

↓

Business Resolver

↓

Policy Resolver

↓

Snapshot Resolver

↓

Component Resolver

↓

Rendering Engine

↓

Response
```

Each resolver performs a single responsibility.

---

# 5. Runtime Context

The Runtime Context represents the complete execution context for a request.

The context may contain:

- Platform
- Organization
- Storefront
- Campaign
- Tracking
- Localization
- Identity
- Customer Segment
- Device
- Feature Flags
- Runtime Overrides

Runtime Context remains immutable during request processing.

---

# 6. Runtime Resolution Order

Runtime Resolution follows a fixed hierarchy.

```
Platform

↓

Organization

↓

Storefront

↓

Campaign

↓

Tracking

↓

User Preference

↓

Runtime Override
```

Higher levels provide defaults.

Lower levels override only explicitly configured properties.

---

# 7. Experience Runtime

The Experience Runtime resolves presentation concerns.

Responsibilities include:

- Theme
- Design Tokens
- Layout
- Navigation
- Assets
- Sections
- Components
- Localization
- Experience Profile

The Experience Runtime never evaluates business rules.

---

# 8. Business Runtime

The Business Runtime resolves platform capabilities.

Responsibilities include:

- Catalog
- Product
- Pricing
- Promotion
- Checkout
- Payment
- Customer
- Support
- Fulfillment Policy

Business Runtime delegates execution to Platform Capabilities.

---

# 9. Policy Runtime

The Policy Runtime evaluates configurable business decisions.

Responsibilities include:

- Visibility
- Pricing Eligibility
- Checkout
- Promotion
- Fraud
- Allocation
- Inventory
- Access Control

Policy Runtime never renders UI.

---

# 10. Snapshot Runtime

Only Published Snapshots participate in Runtime Resolution.

```
Draft Configuration

↓

Publish

↓

Immutable Snapshot

↓

Runtime Resolution
```

Draft configurations are never consumed directly.

---

# 11. Resolver Pipeline

```
Request

↓

Context Resolver

↓

Experience Resolver

↓

Business Resolver

↓

Policy Resolver

↓

Snapshot Resolver

↓

Asset Resolver

↓

Component Resolver

↓

Rendering
```

Resolvers execute in deterministic order.

---

# 12. Reference Resolution Principle

The Runtime Resolution Engine resolves **references**, not business logic.

Example:

```
Storefront

↓

Catalog Reference

↓

Catalog Capability

↓

Products
```

The Runtime Resolution Engine never performs:

- Product Selection
- Pricing Calculation
- Supplier Routing
- Allocation
- Settlement

These responsibilities belong to Platform Capabilities.

---

# 13. Merge Strategy

Configuration merge follows deterministic rules.

| Configuration Type | Merge Strategy |
|--------------------|----------------|
| Scalar | Replace |
| Object | Merge |
| Map | Merge |
| List | Replace |
| Ordered Collection | Replace |

No resolver may introduce custom merge behavior.

---

# 14. Runtime Cache

Published snapshots may be cached.

Typical cache key:

```
Storefront

+

Locale

+

Theme

+

Snapshot Version

+

Device
```

Cache invalidation occurs only after successful publication.

---

# 15. Runtime Fallback

If a configuration cannot be resolved, fallback is applied.

```
Runtime Override

↓

Campaign

↓

Storefront

↓

Organization

↓

Platform
```

Fallback is evaluated independently for each configuration object.

---

# 16. Error Handling

Resolution failures should degrade gracefully whenever possible.

Examples:

Missing Campaign

↓

Fallback to Storefront

Missing Theme

↓

Fallback to Organization Theme

Missing Asset

↓

Fallback to Platform Asset

Fatal runtime errors should occur only when no valid fallback exists.

---

# 17. Runtime Sequence

```
Browser

↓

Gateway

↓

Runtime Context

↓

Experience Runtime

↓

Business Runtime

↓

Policy Runtime

↓

Snapshot Runtime

↓

Rendering

↓

HTML / JSON Response
```

---

# 18. Runtime Characteristics

The Runtime Resolution Architecture shall be:

- Stateless
- Deterministic
- Idempotent
- Cache Friendly
- Snapshot Driven
- Extensible
- Multi-tenant
- Localization Aware

---

# 19. AI Implementation Guidelines

AI agents shall:

- Never bypass Runtime Resolution.
- Never consume Draft configurations.
- Never hardcode themes.
- Never hardcode storefront configuration.
- Never implement business logic inside Runtime Resolution.
- Always resolve references through Platform Capabilities.
- Always support inheritance.
- Always support fallback.
- Always consume Published Snapshots.

---

# 20. Architectural Principles

### ABP-1801

Runtime Resolution is deterministic.

---

### ABP-1802

Runtime Resolution consumes Published Snapshots only.

---

### ABP-1803

Runtime Resolution resolves references, not business logic.

---

### ABP-1804

Business execution belongs to Platform Capabilities.

---

### ABP-1805

Experience Runtime is independent from Business Runtime.

---

### ABP-1806

Policy Runtime evaluates configurable business decisions.

---

### ABP-1807

Configuration inheritance follows a fixed hierarchy.

---

### ABP-1808

Fallback is mandatory for runtime resilience.

---

### ABP-1809

Supplier systems never participate in Runtime Resolution.

---

### ABP-1810

Runtime Resolution must remain stateless and cache-friendly.

---

# 21. References

This document should be read together with:

- BRD — Business Requirements
- YADF — YSim Architecture Definition Framework
- AFM — AI Factory Model
- UXF-00 — User Experience Foundation Overview
- UXF-05 — Experience Runtime & Commerce Runtime Integration
- CAP-00 — Platform Capability Registry
- ECS-00 — Experience Configuration Schema
- PCS-00 — Platform Configuration Schema
- POL-00 — Platform Policy Framework
- DIP — Development & Implementation Principles


---

# Source: AFM-00

- Path: `docs/AFM/AFM-00.md`
- Set: `AFM`
- Version: `2.1`
- Status: `FROZEN`

# AI Factory Manual

## AFM-00

---

# 1. Purpose

AI Factory Manual (AFM) là tài liệu giới thiệu tổng thể về YSim AI Software Factory.

AFM định nghĩa:

- Triết lý phát triển.
- Kiến trúc framework.
- Vòng đời phát triển.
- Mối quan hệ giữa các bộ tài liệu.
- Nguyên tắc phối hợp giữa AI và con người.

Đây là tài liệu đầu tiên cần đọc trước khi tham gia dự án.

---

# 2. Vision

YSim AI Software Factory hướng tới một quy trình phát triển phần mềm:

- AI-Driven
- Business-Driven
- Architecture-Driven
- Sprint-Driven
- Experience-Driven
- Quality-Driven
- Traceable
- Continuously Improving

Mọi thay đổi đều phải có nguồn gốc, bằng chứng và khả năng kiểm chứng.

---

# 3. Core Principles

Framework tuân thủ các nguyên tắc:

- Business First
- Architecture First
- Experience First
- Sprint Driven
- Full-stack Capability Delivery
- AI Assisted
- Engineering by Standards
- Configuration over Customization
- Governance by Evidence
- Continuous Improvement

---

# 4. Framework Architecture

```text
Business Layer
────────────────────────
BRD
YADF

↓

Architecture Layer
────────────────────────
ABP

↓

AI & Governance Layer
────────────────────────
AAP
SGP

↓

Engineering Layer
────────────────────────
ESP

↓

Implementation Layer
────────────────────────
DIP

↓

Verification Layer
────────────────────────
VAP

↓

Operations Layer
────────────────────────
ROP
```

Mỗi bộ tài liệu có trách nhiệm riêng và đóng vai trò là một phần của chuỗi phát triển thống nhất.

---

# 5. Sprint Lifecycle

```text
Business

↓

Architecture

↓

Sprint Planning

↓

Backend
   +
Frontend

↓

Integration

↓

Capability Demonstration

↓

Verification

↓

Release

↓

Operations

↓

Continuous Improvement
```

Một Sprint chỉ hoàn thành khi Capability đã được Demonstration và Verification thành công.

---

# 6. Roles

| Role | Responsibility |
|------|----------------|
| Business Owner | Định nghĩa Business |
| Architect | Thiết kế Architecture |
| AI Agent | Sinh Artifact theo Standards |
| Developer | Hiện thực và Review |
| QA | Verification |
| Operations | Production Operations |

---

# 7. AI Working Principles

AI phải:

- đọc đúng tài liệu;
- tuân thủ Standards;
- không tự thay đổi Architecture;
- không vượt Sprint Scope;
- luôn tạo Evidence;
- luôn đảm bảo Traceability;
- triển khai Backend và Frontend đồng thời;
- sinh Seed Data phục vụ kiểm thử;
- tạo Capability Demonstration Surface;
- không hoàn thành Capability khi chưa có Demonstration.

AI là thành viên của Factory, không phải người quyết định kiến trúc.

---

# 8. Engineering Philosophy

Framework coi mọi đầu ra đều là Engineering Asset.

Bao gồm:

- Source Code
- API
- Documentation
- Migration
- Test
- Configuration
- Release
- Runbook
- Storefront
- Portal
- Landing Page
- Component Library
- Design System
- Capability Demonstration Surface

Mọi Asset đều có vòng đời, version và khả năng truy vết.

---

# 9. Continuous Improvement

Sau mỗi Sprint và mỗi Release:

- Lessons Learned
- Operational Feedback
- Incident Review
- Architecture Review

được sử dụng để cải tiến Framework và hệ thống.

---

# 10. Success Criteria

Một Sprint được coi là thành công khi:

- Business Requirement được đáp ứng;
- Architecture được tuân thủ;
- Standards được tuân thủ;
- Capability Demonstration PASS;
- Verification PASS;
- Release thành công;
- Operations tiếp nhận;
- Lessons Learned được ghi nhận.

---

# 11. Relationship to Other Documents

Chuỗi tài liệu của AI Factory:

```text
BRD
    ↓
YADF
    ↓
ABP
    ↓
AAP
    ↓
SGP
    ↓
ESP
    ↓
DIP
    ↓
VAP
    ↓
ROP
```

Mỗi bộ tài liệu không chỉ định nghĩa yêu cầu kỹ thuật mà còn tạo thành chuỗi hướng dẫn để AI chuyển đổi từ Business Requirement sang Sprint Implementation một cách có khả năng truy vết.

---

# 12. Document Status

**Status: FROZEN**

AFM là tài liệu định hướng cao nhất của YSim AI Software Factory và phản ánh trạng thái kiến trúc hiện hành của phiên bản v2.1.


---

# Source: CAP-00

- Path: `docs/CAP/CAP-00.md`
- Set: `CAP`
- Version: `1.0`
- Status: `Draft`

# CAP-00 — Platform Capability Registry

---

# 1. Purpose

This document defines the canonical Business Capability Registry of the YSim Platform.

The registry establishes a single source of truth for all platform capabilities used throughout:

- Business Requirements
- Architecture
- Domain Models
- APIs
- AI Factory
- Runtime
- Documentation
- Sprint Planning

A Capability represents **what the platform is able to do**, independent of implementation technology.

Capabilities are stable architectural concepts and should evolve much slower than services or applications.

---

# 2. Capability Philosophy

The YSim Platform is capability-driven.

Applications do not own business logic.

Applications consume Platform Capabilities.

```
Portal

Storefront

Embedded Commerce

Public APIs

↓

Business Capability

↓

Application Services

↓

Infrastructure
```

Capabilities remain independent from presentation.

---

# 3. Capability Definition

A Capability describes:

- Business Responsibility
- Business Ownership
- Business Rules
- Domain Boundaries
- Events
- APIs
- Permissions

A Capability never describes:

- UI
- Database Tables
- Frameworks
- Programming Languages
- External Suppliers

---

# 4. Capability Hierarchy

The platform organizes capabilities hierarchically.

```
Platform

↓

Business Domain

↓

Capability

↓

Application Service

↓

Infrastructure
```

Capabilities are implementation-independent.

---

# 5. Capability Classification

Capabilities are grouped into five categories.

## Foundation

Core platform capabilities.

Examples:

- Identity
- Organization
- Configuration
- Localization
- Branding

---

## Commerce

Commercial capabilities.

Examples:

- Catalog
- Product
- Pricing
- Promotion
- Checkout
- Order

---

## Fulfillment

Delivery capabilities.

Examples:

- Allocation
- Fulfillment
- Inventory
- Delivery

---

## Operations

Operational capabilities.

Examples:

- Monitoring
- Reporting
- Notification
- Scheduler

---

## Integration

External connectivity.

Examples:

- Supplier Gateway
- Payment Gateway
- Notification Gateway
- Webhooks

---

# 6. Canonical Capability Registry

The following capabilities are defined for YSim v2.1.

---

## Foundation

- Identity
- Access Control
- Organization
- User Management
- Branding
- Theme
- Localization
- Configuration
- Storefront
- Asset Management
- Domain Management
- Feature Flags

---

## Commerce

- Catalog
- Product
- Pricing
- Promotion
- Shopping Cart
- Checkout
- Order
- Customer
- Payment
- Refund
- Voucher

---

## Fulfillment

- Allocation
- Inventory
- Fulfillment
- Delivery
- Activation
- Replacement

---

## Finance

- Settlement
- Ledger
- Commission
- Billing
- Invoice
- Revenue

---

## Support

- Customer Care
- Knowledge Base
- Ticketing
- Feedback

---

## Platform Operations

- Reporting
- Analytics
- Monitoring
- Scheduler
- Audit
- Logging

---

## Integration

- Supplier Gateway
- Payment Gateway
- Notification Gateway
- Authentication Gateway
- External APIs

---

# 7. Capability Dependency

Capabilities may depend on other capabilities.

Example:

```
Checkout

↓

Pricing

↓

Catalog

↓

Product
```

Another example:

```
Order

↓

Allocation

↓

Fulfillment

↓

Delivery
```

Dependencies always point downward.

Circular dependencies are prohibited.

---

# 8. Capability Exposure

Capabilities are exposed through different channels.

Examples:

```
Portal

↓

Capability
```

```
Storefront

↓

Capability
```

```
Public API

↓

Capability
```

```
Background Jobs

↓

Capability
```

Capabilities remain channel independent.

---

# 9. Capability Ownership

Each capability has one business owner.

Example:

| Capability | Owner |
|------------|-------|
| Catalog | Commerce Domain |
| Pricing | Commerce Domain |
| Allocation | Fulfillment Domain |
| Settlement | Finance Domain |
| Branding | Foundation Domain |

Ownership prevents duplicated business logic.

---

# 10. Capability Lifecycle

Capabilities evolve independently.

Lifecycle:

```
Planned

↓

Draft

↓

Active

↓

Deprecated

↓

Retired
```

Deprecated capabilities remain backward compatible until retired.

---

# 11. Capability Contracts

Capabilities expose contracts.

Contracts include:

- APIs
- Events
- Commands
- Queries
- Permissions

Consumers communicate only through contracts.

---

# 12. Capability Boundaries

Capabilities never access each other's internal models.

Interaction occurs through:

- Commands
- Queries
- Events

Direct database access across capabilities is prohibited.

---

# 13. Experience Integration

Experience Runtime consumes capabilities.

Example:

```
Featured Products Widget

↓

Catalog Capability

↓

Pricing Capability

↓

Promotion Capability
```

Widgets never access infrastructure directly.

---

# 14. Commerce Runtime

Commerce Runtime consists of:

- Catalog
- Product
- Pricing
- Promotion
- Checkout
- Payment
- Customer
- Order

These capabilities define commercial behavior.

---

# 15. Allocation Capability

Allocation is a first-class capability.

Responsibilities:

- Inventory Reservation
- Supplier Routing
- Cost Optimization
- Fulfillment Selection
- Retry
- Replacement

Allocation is the only capability allowed to determine which supplier provides an eSIM.

---

# 16. Supplier Isolation

Supplier systems are not capabilities.

Supplier systems are infrastructure resources.

Correct architecture:

```
Capability

↓

Supplier Gateway

↓

Supplier
```

Storefronts never consume suppliers.

Commerce Runtime never exposes supplier objects.

---

# 17. Capability Matrix

| Capability | Portal | Storefront | API | Background |
|------------|--------|------------|-----|------------|
| Catalog | ✓ | ✓ | ✓ | - |
| Pricing | ✓ | ✓ | ✓ | - |
| Checkout | - | ✓ | ✓ | - |
| Allocation | ✓ | - | Internal | ✓ |
| Fulfillment | ✓ | - | Internal | ✓ |
| Settlement | ✓ | - | Internal | ✓ |
| Monitoring | ✓ | - | Internal | ✓ |

---

# 18. AI Implementation Rules

AI agents shall:

- Treat Capabilities as architectural boundaries.
- Never merge unrelated capabilities.
- Never expose infrastructure through capabilities.
- Never expose suppliers to storefronts.
- Always communicate through capability contracts.
- Keep business rules inside capabilities.
- Keep UI independent from capability implementation.

---

# 19. Architectural Principles

### CAP-001

Capabilities define business responsibilities.

---

### CAP-002

Capabilities are independent from implementation.

---

### CAP-003

Capabilities expose contracts.

---

### CAP-004

Capabilities own business rules.

---

### CAP-005

Capabilities never expose infrastructure.

---

### CAP-006

Suppliers are infrastructure resources.

---

### CAP-007

Allocation owns supplier selection.

---

### CAP-008

Storefronts consume capabilities only.

---

### CAP-009

Capabilities communicate through contracts.

---

### CAP-010

Business ownership is unique.

---

# 20. References

This document should be read together with:

- BRD — Business Requirements
- ABP — Architecture Blueprint
- YADF — YSim Architecture Definition Framework
- AFM — AI Factory Model
- UXF-00 ~ UXF-05
- DIP — Development & Implementation Principles


---

# Source: DIP-00

- Path: `docs/DIP/DIP-00.md`
- Set: `DIP`
- Version: `2.1`
- Status: `FROZEN`

# Implementation Constitution & Executable Sprint Model

## DIP-00

---

# 1. Purpose

Development & Implementation Pack (DIP) là tầng tài liệu triển khai của YSim AI Software Factory.

DIP chuyển đổi toàn bộ Architecture, Business và Engineering Standards thành các Sprint có khả năng thực thi trực tiếp bởi AI Coding Assistant.

DIP không mô tả kiến trúc.

DIP mô tả cách kiến trúc được hiện thực hóa.

---

# 2. Position in Software Factory

```text
Business Architecture

↓

Engineering Architecture

↓

Governance

↓

Engineering Standards

↓

Implementation (DIP)

↓

Codex Execution

↓

Evidence

↓

Release
```

DIP là cầu nối giữa Architecture và Source Code.

---

# 3. Objectives

DIP nhằm:

- chuẩn hóa quá trình triển khai;
- cung cấp Context đầy đủ cho Codex;
- tạo Sprint có khả năng thực thi tự động;
- đảm bảo Backend và Frontend được triển khai đồng thời;
- tạo Capability Demonstration cho từng Sprint;
- sinh Evidence phục vụ Review và Release.

---

# 4. Principles

Implementation tuân thủ:

- Architecture First
- Capability Driven
- Full-stack Delivery
- Seed-driven Development
- Demonstration First
- Validation Before Completion
- Evidence by Design
- Automation by Default
- Repeatable Execution
- Explainable AI Delivery

---

# 5. Executable Sprint Model

Mỗi Sprint trong DIP phải là một Executable Sprint Package.

Package này có thể được Codex thực thi trực tiếp mà không cần bổ sung Prompt ngoài tài liệu.

```text
Sprint Package

↓

Repository Discovery

↓

Planning

↓

Backend

↓

API

↓

Frontend

↓

Seed Data

↓

Capability Demonstration

↓

Testing

↓

Validation

↓

Evidence

↓

Git Commit
```

---

# 6. Full-stack Capability Delivery

Mọi Capability có giao diện người dùng phải được triển khai đồng thời:

- Backend
- API
- Frontend
- Design System Integration
- Experience API
- Seed Data
- Demonstration
- Tests
- Evidence

Không được triển khai Backend độc lập đối với Capability có UI.

---

# 7. Seed-driven Development

Mỗi Sprint phải cung cấp Seed Information cho Codex.

Seed Information bao gồm tối thiểu:

- Business Context
- Architecture Context
- Engineering Constraints
- Reference Data
- Sample Data
- Integration Configuration
- Target Metrics
- Acceptance Scenario

Seed là nguồn dữ liệu mặc định để AI triển khai Capability.

---

# 8. Executable Sprint Package

Mỗi Sprint phát hành dưới dạng một Package chuẩn.

```text
README

↓

Sprint Manifest

↓

Task Manifest

↓

Prompt

↓

Context

↓

Reference Data

↓

Runner

↓

Validation

↓

Evidence
```

Mọi Sprint phải có cấu trúc thống nhất.

---

# 9. Task Model

Mọi Sprint sử dụng cùng cấu trúc Task.

| Task | Responsibility |
|--------|----------------|
| t00 | Repository Discovery |
| t01 | Domain Model |
| t02 | Database & Migration |
| t03 | Backend API |
| t04 | Business Services |
| t05 | Integration |
| t06 | Queue & Background |
| t07 | Frontend & Demonstration |
| t08 | Testing |
| t09 | Validation & Evidence |
| t10 | Final Review & Commit |

Task không được thay đổi thứ tự.

Task có thể được đánh dấu Not Applicable nhưng không được loại bỏ.

---

# 10. Context Resolution

Trước khi Coding, AI phải đọc đầy đủ:

- BRD
- ABP
- YADF
- AAP
- SGP
- ESP
- API
- DMS
- DBD
- Capability DIP

Không được Coding nếu Context chưa đầy đủ.

---

# 11. Prompt Contract

Mỗi Task phải có Prompt độc lập.

Prompt tối thiểu gồm:

- Role
- Objective
- Scope
- Input Documents
- Files Allowed To Change
- Files Prohibited To Change
- Business Rules
- Architecture Constraints
- Reference Data
- Validation Commands
- Expected Evidence
- Completion Criteria

Không sử dụng Prompt tổng hợp cho toàn Sprint.

---

# 12. Bash Runner

Mỗi Sprint phải cung cấp Bash Runner.

Runner phải hỗ trợ:

- run
- resume
- from-task
- single-task
- dry-run

Runner phải:

- ghi Log;
- lưu Exit Code;
- Validate sau mỗi Task;
- Commit khi PASS.

Không được tiếp tục nếu Validation FAIL.

---

# 13. Validation Model

Validation diễn ra sau từng Task.

Validation tối thiểu:

- Build
- Test
- Lint
- Architecture Compliance
- Engineering Compliance
- Demonstration
- Evidence

Task chỉ được PASS khi Validation PASS.

---

# 14. Evidence Model

Mỗi Task phải sinh:

- Execution Log
- Validation Result
- Git Diff
- Evidence Package

Mỗi Sprint phải sinh:

- Sprint Report
- Demonstration Report
- Evidence Manifest

Evidence là điều kiện bắt buộc để Review.

---

# 15. Git Strategy

Khuyến nghị Commit theo từng Task.

Ví dụ:

```text
feat(s14): implement product repository

feat(s14): implement product api

feat(s14): implement product frontend

test(s14): product capability verification
```

Commit chỉ được tạo khi Validation PASS.

---

# 16. ACP Integration

Nếu phát hiện:

- Architecture Conflict
- Business Conflict
- Frozen Document Violation

AI phải:

- dừng Sprint;
- sinh ACP;
- không tiếp tục Coding.

Không được tự ý thay đổi Architecture.

---

# 17. Deliverables

Một Sprint hoàn chỉnh phải sinh:

- Backend Source Code
- Frontend Source Code
- API
- Migration
- Seed Data
- Tests
- Demonstration
- Documentation
- Evidence
- Git Commit

Không chấp nhận Sprint chỉ sinh Source Code.

---

# 18. Rules

DIP-001 — Mọi Sprint phải là Executable Sprint.

DIP-002 — Mọi Sprint phải có Seed Information.

DIP-003 — Capability có UI phải Full-stack.

DIP-004 — Validation sau từng Task.

DIP-005 — Runner phải hỗ trợ Resume.

DIP-006 — Prompt phải độc lập theo Task.

DIP-007 — Evidence là bắt buộc.

DIP-008 — ACP được kích hoạt khi phát hiện xung đột.

DIP-009 — Commit chỉ khi Validation PASS.

DIP-010 — DIP là nguồn Seed chính thức cho Codex.

---

# 19. Compliance Checklist

| Rule | Validation |
|------|------------|
| DIC-0001 | Sprint Package đúng chuẩn |
| DIC-0002 | Seed đầy đủ |
| DIC-0003 | Context đầy đủ |
| DIC-0004 | Prompt đầy đủ |
| DIC-0005 | Runner hoạt động |
| DIC-0006 | Validation PASS |
| DIC-0007 | Demonstration hoàn chỉnh |
| DIC-0008 | Evidence đầy đủ |
| DIC-0009 | Commit thành công |
| DIC-0010 | Tuân thủ DIP |

---

# 20. Relationship to Other Documents

DIP-00 liên kết với:

- AFM-00 Architecture Freeze Manifest
- BRD Meta Model
- YADF-00 AI Development Framework
- AAP-00 AI Architecture Principles
- SGP-00 Sprint Governance Principles
- ESP-00 Engineering Standards
- ROP Release & Operations Pack
- VAP Verification & Acceptance Pack

DIP-00 là tài liệu gốc của toàn bộ Development & Implementation Pack.

---

# 21. Document Status

**Status: FROZEN**

DIP-00 là Implementation Constitution của YSim AI Software Factory.

Từ phiên bản 2.1, mọi Capability đều phải được triển khai thông qua Executable Sprint Package, sử dụng Seed Information làm nguồn Context chính thức cho Codex và được thực thi bằng Bash Runner theo mô hình Full-stack Capability Delivery.


---

# Source: DIP-01

- Path: `docs/DIP/DIP-01.md`
- Set: `DIP`
- Version: `2.1`
- Status: `FROZEN`

# Executable Sprint Package Standard (ESPK)

## DIP-01

---

# 1. Purpose

Executable Sprint Package (ESPK) là đơn vị triển khai chuẩn của YSim AI Software Factory.

Mỗi Sprint không còn được phát hành chỉ dưới dạng tài liệu.

Thay vào đó, Sprint được phát hành dưới dạng một Package hoàn chỉnh có thể được AI Coding Assistant thực thi trực tiếp.

ESPK là cầu nối giữa DIP và Source Code.

---

# 2. Position in Software Factory

```text
DIP

↓

Executable Sprint Package

↓

Bash Runner

↓

AI Coding Agent

↓

Validation

↓

Evidence

↓

Git Commit
```

---

# 3. Objectives

ESPK nhằm:

- chuẩn hóa mọi Sprint;
- tạo khả năng thực thi tự động;
- cung cấp đầy đủ Context;
- giảm Prompt Engineering thủ công;
- đảm bảo khả năng Resume;
- đảm bảo khả năng Audit.

---

# 4. Principles

ESPK tuân thủ:

- Executable by Design
- Context First
- Seed-driven Development
- Capability Driven
- Full-stack Delivery
- Validation First
- Evidence First
- Repeatable Execution
- AI Independent

---

# 5. Package Structure

```text
Sprint Package
│
├── README.md
├── sprint.json
│
├── ai/
│
├── scripts/
│
├── validation/
│
├── evidence/
│
└── logs/
```

Mọi Sprint phải tuân thủ đúng cấu trúc này.

---

# 6. AI Directory

```text
ai/

├── sprints/

├── manifests/

├── prompts/

├── context/

└── seeds/
```

Không được thay đổi cấu trúc thư mục.

---

# 7. Sprint Manifest

Sprint Manifest định nghĩa:

- Sprint ID
- Capability
- Scope
- Dependencies
- Deliverables
- Validation
- Completion Criteria

Manifest là Entry Point của Sprint.

---

# 8. Task Manifest

Mỗi Task có một Manifest riêng.

```text
t00

↓

t01

↓

...

↓

t10
```

Manifest mô tả:

- Objective
- Inputs
- Outputs
- Dependencies
- Validation
- Evidence

---

# 9. Prompt Package

Prompt được lưu riêng.

```text
prompts/

t00.md

...

t10.md
```

Prompt không được Hardcode trong Runner.

---

# 10. Context Package

Context bao gồm:

- Business Context
- Architecture Context
- Engineering Context
- Repository Context
- Frontend Context
- Acceptance Context

AI chỉ được Coding sau khi Context được nạp đầy đủ.

---

# 11. Seed Package

Seed bao gồm:

- Reference Data
- Demo Data
- Integration Configuration
- Sample Users
- Sample Products
- Target Metrics

Seed là nguồn dữ liệu mặc định của Sprint.

---

# 12. Validation Package

Validation bao gồm:

- Build Commands
- Test Commands
- Lint Commands
- Demo Scenarios
- Acceptance Checklist

Validation phải có khả năng chạy tự động.

---

# 13. Bash Runner

Runner tối thiểu hỗ trợ:

- run
- resume
- dry-run
- single-task
- from-task

Runner phải:

- ghi log;
- lưu Exit Code;
- dừng khi FAIL;
- Commit khi PASS.

---

# 14. Evidence Package

Evidence phải sinh:

- Execution Log
- Validation Report
- Build Report
- Test Report
- Demonstration Report
- Git Diff
- Sprint Report

Evidence là đầu ra bắt buộc.

---

# 15. Capability Demonstration

Mỗi Capability có UI phải cung cấp:

- Demonstration Guide
- Demo Users
- Demo Data
- Demo Scenarios
- Expected Results

Capability chỉ được Accepted khi Demonstration PASS.

---

# 16. AI Independence

ESPK không phụ thuộc AI cụ thể.

Có thể thực thi bởi:

- Codex
- Claude Code
- Gemini CLI
- OpenHands
- Cursor Agent
- AI Coding Assistant khác

Không được Hardcode Prompt theo Model.

---

# 17. Versioning

Package có Version độc lập.

Ví dụ:

```text
ESPK

v2.1.0
```

Version không phụ thuộc Repository Version.

---

# 18. Rules

ESPK-001 — Mọi Sprint phải phát hành dưới dạng ESPK.

ESPK-002 — Package phải đầy đủ Manifest.

ESPK-003 — Prompt phải độc lập.

ESPK-004 — Seed là bắt buộc.

ESPK-005 — Runner phải Resume được.

ESPK-006 — Validation phải tự động.

ESPK-007 — Evidence là bắt buộc.

ESPK-008 — Demonstration là bắt buộc đối với Capability có UI.

ESPK-009 — Không phụ thuộc AI Model.

ESPK-010 — Package phải Version hóa.

---

# 19. Compliance Checklist

| Rule | Validation |
|------|------------|
| EPC-0101 | Package đúng cấu trúc |
| EPC-0102 | Manifest đầy đủ |
| EPC-0103 | Prompt đầy đủ |
| EPC-0104 | Context đầy đủ |
| EPC-0105 | Seed đầy đủ |
| EPC-0106 | Runner hoạt động |
| EPC-0107 | Validation PASS |
| EPC-0108 | Evidence đầy đủ |
| EPC-0109 | Demonstration PASS |
| EPC-0110 | Tuân thủ DIP |

---

# 20. Relationship to Other Documents

ESPK liên kết với:

- DIP-00 Implementation Constitution
- AAP Sprint Planning
- SGP Sprint Governance
- ESP Engineering Standards
- VAP Verification & Acceptance Pack
- ROP Release & Operations Pack

ESPK là Implementation Artifact chuẩn của YSim AI Software Factory.

---

# 21. Document Status

**Status: FROZEN**

Từ phiên bản 2.1, mọi Sprint của YSim phải được phát hành dưới dạng **Executable Sprint Package (ESPK)**.

ESPK là định dạng triển khai chuẩn, độc lập với AI Coding Agent, cung cấp đầy đủ Context, Seed, Prompt, Validation và Evidence để AI có thể thực thi Sprint theo mô hình Full-stack Capability Delivery.


---

# Source: DIP-02

- Path: `docs/DIP/DIP-02.md`
- Set: `DIP`
- Version: `2.1`
- Status: `FROZEN`

# AI Context Resolution & Prompt Assembly Standard

## DIP-02

---

# 1. Purpose

AI Coding Assistant chỉ có thể tạo ra Source Code đúng khi được cung cấp đầy đủ Context.

DIP-02 định nghĩa cơ chế thu thập, hợp nhất và chuẩn hóa Context trước khi bắt đầu mỗi Sprint hoặc Task.

Mọi Prompt đều phải được sinh ra từ Context đã được chuẩn hóa.

Không cho phép AI Coding Assistant triển khai khi Context chưa đầy đủ.

---

# 2. Position in Software Factory

```text
Repository

↓

Discovery

↓

Context Resolution

↓

Prompt Assembly

↓

AI Coding

↓

Validation
```

Context Resolution là bước bắt buộc trước AI Coding.

---

# 3. Objectives

Context Resolution nhằm:

- xác định đúng phạm vi Sprint;
- giảm Hallucination;
- loại bỏ Prompt thủ công;
- tăng khả năng tái lập;
- bảo đảm tuân thủ Architecture;
- tối ưu Token sử dụng.

---

# 4. Principles

Context Resolution tuân thủ:

- Context First
- Source of Truth
- Minimal but Complete
- Architecture-aware
- Capability-aware
- Explainable
- Deterministic
- Repeatable

---

# 5. Context Layers

Context được chia thành nhiều lớp.

```text
Business

↓

Architecture

↓

Engineering

↓

Capability

↓

Repository

↓

Runtime

↓

Task
```

Không được bỏ qua bất kỳ lớp nào nếu có liên quan.

---

# 6. Context Sources

AI có thể sử dụng Context từ:

- BRD
- ABP
- DMS
- DBD
- API
- ESP
- SGP
- YADF
- DIP
- Repository
- Sprint Manifest
- Seed Package

Không sử dụng nguồn ngoài nếu chưa được phê duyệt.

---

# 7. Context Resolution Pipeline

```text
Discovery

↓

Repository Scan

↓

Sprint Manifest

↓

Capability Manifest

↓

Business Context

↓

Architecture Context

↓

Engineering Context

↓

Repository Context

↓

Task Context

↓

Prompt Assembly
```

Prompt chỉ được tạo sau khi Context Resolution hoàn thành.

---

# 8. Business Context

Business Context tối thiểu gồm:

- Capability
- Business Rules
- Actors
- Use Cases
- Constraints
- Acceptance Criteria

Business Context được lấy từ BRD.

---

# 9. Architecture Context

Architecture Context gồm:

- Business Domains
- Services
- Modules
- Events
- Ownership
- Integration
- Deployment Constraints

Nguồn chính:

- ABP
- AFM
- YADF

---

# 10. Engineering Context

Engineering Context gồm:

- Coding Standards
- Naming Standards
- API Standards
- Testing Standards
- Security Standards
- Performance Standards

Nguồn:

ESP.

---

# 11. Repository Context

Repository Context gồm:

- Folder Structure
- Existing Modules
- Package Dependencies
- Build System
- Existing Tests
- Existing APIs

Repository luôn là Source of Truth cho trạng thái hiện tại của Source Code.

---

# 12. Capability Context

Capability Context bao gồm:

- Domain Model
- API
- Database
- Frontend
- Experience API
- Seed Data
- Demonstration

Capability Context được lấy từ Sprint Package.

---

# 13. Runtime Context

Runtime Context bao gồm:

- Environment
- Feature Flags
- Configuration
- Secrets Reference
- Infrastructure

Không nhúng Secret trực tiếp vào Prompt.

---

# 14. Task Context

Task Context chỉ chứa:

- Objective
- Files Allowed
- Files Protected
- Dependencies
- Expected Outputs
- Validation Commands

Task Context phải nhỏ nhất có thể.

---

# 15. Prompt Assembly

Prompt được tạo theo thứ tự:

```text
Role

↓

Objective

↓

Scope

↓

Context

↓

Business Rules

↓

Architecture Constraints

↓

Engineering Constraints

↓

Repository Constraints

↓

Implementation Tasks

↓

Validation

↓

Completion Criteria
```

Prompt không được viết thủ công cho từng Sprint.

Prompt phải được sinh từ Context.

---

# 16. Context Size Control

AI không được nạp toàn bộ tài liệu.

Chỉ nạp:

- tài liệu liên quan;
- Capability hiện tại;
- Repository hiện tại.

Ưu tiên Context có mức ảnh hưởng cao.

---

# 17. Conflict Resolution

Nếu phát hiện:

- Architecture Conflict
- Business Conflict
- Repository Conflict

AI phải:

- dừng Prompt Assembly;
- sinh ACP;
- không Coding.

---

# 18. Rules

CTX-001 — Context Resolution bắt buộc trước Coding.

CTX-002 — Prompt sinh từ Context.

CTX-003 — Không Coding nếu thiếu Context.

CTX-004 — Repository là Source of Truth cho Source Code.

CTX-005 — Architecture Document là Source of Truth cho Design.

CTX-006 — Không nhúng Secret.

CTX-007 — Chỉ nạp Context liên quan.

CTX-008 — Capability Context luôn ưu tiên.

CTX-009 — Conflict kích hoạt ACP.

CTX-010 — Prompt phải tái lập được.

---

# 19. Compliance Checklist

| Rule | Validation |
|------|------------|
| CRC-0201 | Business Context đầy đủ |
| CRC-0202 | Architecture Context đầy đủ |
| CRC-0203 | Engineering Context đầy đủ |
| CRC-0204 | Repository Context đầy đủ |
| CRC-0205 | Capability Context đầy đủ |
| CRC-0206 | Prompt được sinh tự động |
| CRC-0207 | Không có Conflict |
| CRC-0208 | Validation Commands đầy đủ |
| CRC-0209 | Context tối ưu |
| CRC-0210 | Tuân thủ DIP |

---

# 20. Relationship to Other Documents

DIP-02 liên kết với:

- DIP-00 Implementation Constitution
- DIP-01 Executable Sprint Package Standard
- AFM-00
- BRD
- ABP
- YADF
- AAP
- SGP
- ESP

DIP-02 là tài liệu chuẩn hóa Context Resolution của YSim AI Software Factory.

---

# 21. Document Status

**Status: FROZEN**

Từ phiên bản 2.1, mọi Prompt của AI Coding Assistant phải được tạo thông qua Context Resolution theo tiêu chuẩn của DIP-02.

Không cho phép AI Coding trực tiếp từ Prompt thủ công hoặc Context không đầy đủ.


---

# Source: DIP-04

- Path: `docs/DIP/DIP-04.md`
- Set: `DIP`
- Version: `2.1`
- Status: `FROZEN`

# AI Execution Runtime & Bash Runner Standard

## DIP-04

---

# 1. Purpose

AI Execution Runtime định nghĩa môi trường thực thi chuẩn cho mọi Executable Sprint Package (ESPK).

Runtime chịu trách nhiệm điều phối toàn bộ vòng đời triển khai của một Sprint, từ Repository Discovery đến Validation, Evidence Generation và Git Commit.

Runtime không phụ thuộc vào AI Coding Agent cụ thể.

---

# 2. Position in Software Factory

```text
Executable Sprint Package

↓

AI Execution Runtime

↓

Bash Runner

↓

AI Coding Agent

↓

Validation

↓

Evidence

↓

Git Commit
```

Runtime là Execution Engine của Software Factory.

---

# 3. Objectives

AI Execution Runtime nhằm:

- chuẩn hóa quá trình triển khai;
- tự động hóa Sprint;
- hỗ trợ Resume;
- hỗ trợ Retry;
- hỗ trợ Parallel-safe Execution;
- tạo khả năng Audit;
- giảm thao tác thủ công.

---

# 4. Principles

Runtime tuân thủ:

- Automation by Default
- Non-interactive Execution
- Deterministic Execution
- Fail Fast
- Resume Safe
- Evidence First
- AI Independent
- Observable Runtime
- Reproducible

---

# 5. Runtime Components

```text
Execution Runtime

├── Runner

├── Task Scheduler

├── Prompt Loader

├── Context Loader

├── Seed Loader

├── Validation Engine

├── Evidence Collector

├── Git Manager

└── Reporting Engine
```

Mỗi thành phần có trách nhiệm độc lập.

---

# 6. Runner Responsibilities

Runner chịu trách nhiệm:

- đọc Sprint Manifest;
- đọc Task Manifest;
- khởi tạo Context;
- khởi tạo Seed;
- gọi AI Coding Agent;
- thực thi Validation;
- sinh Evidence;
- Commit.

Runner không chứa Business Logic.

---

# 7. Execution Lifecycle

```text
Environment Check

↓

Repository Discovery

↓

Load Manifest

↓

Load Context

↓

Load Seed

↓

Execute Task

↓

Validation

↓

Evidence

↓

Git Commit

↓

Next Task
```

---

# 8. Task Scheduler

Scheduler điều phối:

- t00 → t10

Không được bỏ qua Task.

Task có thể:

- PASS
- FAIL
- SKIPPED (Not Applicable)

Scheduler phải lưu trạng thái.

---

# 9. Execution Modes

Runtime hỗ trợ:

### Full Sprint

```bash
run-sprint.sh
```

---

### Resume

```bash
run-sprint.sh --resume
```

---

### From Task

```bash
run-sprint.sh --from-task t05
```

---

### Single Task

```bash
run-task.sh t03
```

---

### Dry Run

```bash
run-sprint.sh --dry-run
```

---

# 10. Environment Validation

Runtime phải kiểm tra:

- Git
- Node.js
- pnpm
- Docker (nếu yêu cầu)
- AI CLI
- Environment Variables
- Required Services

Nếu thiếu Dependency thì dừng Sprint.

---

# 11. AI Provider Abstraction

Runtime không phụ thuộc AI cụ thể.

Có thể cấu hình:

```yaml
provider:

codex

claude-code

gemini-cli

openhands

cursor-agent
```

Runner chỉ giao tiếp qua Provider Adapter.

---

# 12. Logging Standard

Runtime phải ghi:

```text
logs/

sprint.log

task-t00.log

task-t01.log

...

task-t10.log
```

Log tối thiểu gồm:

- Timestamp
- Task
- Command
- Exit Code
- Duration

---

# 13. Resume Strategy

Runner phải lưu:

```text
runtime/

state.json
```

Ví dụ:

```json
{
  "current_task":"t06",
  "status":"FAILED",
  "completed":[
    "t00",
    "t01",
    "t02",
    "t03",
    "t04",
    "t05"
  ]
}
```

Resume không được thực hiện lại Task đã PASS.

---

# 14. Retry Strategy

Runner chỉ Retry khi:

- AI Timeout
- Network Error
- Temporary Failure

Không Retry khi:

- Validation FAIL
- Architecture Conflict
- Business Conflict

---

# 15. Validation Integration

Sau mỗi Task:

```text
Build

↓

Lint

↓

Tests

↓

Compliance

↓

Capability Demonstration

↓

Evidence
```

Validation FAIL phải dừng Sprint.

---

# 16. Git Strategy

Runner phải:

- kiểm tra Working Tree;
- Commit theo Task;
- gắn Sprint ID;
- lưu Git Diff.

Không tự động Push trừ khi được cấu hình.

---

# 17. Exit Codes

| Code | Meaning |
|-------|---------|
| 0 | SUCCESS |
| 1 | Validation Failed |
| 2 | Build Failed |
| 3 | AI Execution Failed |
| 4 | Missing Dependency |
| 5 | Repository Conflict |
| 6 | Architecture Conflict |
| 7 | Business Conflict |
| 8 | User Interrupted |
| 9 | Unknown Error |

Exit Code phải được ghi vào Log.

---

# 18. Directory Layout

```text
runtime/

logs/

evidence/

reports/

state/

cache/

tmp/
```

Runtime không ghi dữ liệu ra ngoài Workspace.

---

# 19. Runtime Rules

RUNTIME-001 — Runner phải Non-interactive.

RUNTIME-002 — Resume là bắt buộc.

RUNTIME-003 — Validation sau từng Task.

RUNTIME-004 — Evidence sau từng Task.

RUNTIME-005 — Commit sau Validation PASS.

RUNTIME-006 — Không Retry Validation FAIL.

RUNTIME-007 — Runtime không phụ thuộc AI.

RUNTIME-008 — Runtime phải ghi Log.

RUNTIME-009 — Runtime phải lưu State.

RUNTIME-010 — Runtime phải có Exit Code chuẩn.

---

# 20. Compliance Checklist

| Rule | Validation |
|------|------------|
| RTC-0401 | Runtime khởi tạo đúng |
| RTC-0402 | Manifest được nạp |
| RTC-0403 | Context được nạp |
| RTC-0404 | Seed được nạp |
| RTC-0405 | Validation hoạt động |
| RTC-0406 | Resume hoạt động |
| RTC-0407 | Retry đúng quy tắc |
| RTC-0408 | Evidence đầy đủ |
| RTC-0409 | Git Commit thành công |
| RTC-0410 | Tuân thủ DIP |

---

# 21. Relationship to Other Documents

DIP-04 liên kết với:

- DIP-00 Implementation Constitution
- DIP-01 Executable Sprint Package Standard
- DIP-02 AI Context Resolution & Prompt Assembly Standard
- DIP-03 Seed & Reference Data Standard
- SGP Sprint Governance Pack
- ESP Engineering Standards Pack
- VAP Verification & Acceptance Pack
- ROP Release & Operations Pack

DIP-04 là tiêu chuẩn Runtime cho mọi Sprint của YSim AI Software Factory.

---

# 22. Document Status

**Status: FROZEN**

Từ phiên bản 2.1, mọi Sprint của YSim phải được thực thi thông qua **AI Execution Runtime** theo tiêu chuẩn của DIP-04.

Runtime là tầng điều phối thống nhất, độc lập với AI Coding Agent, bảo đảm mọi Sprint có thể được thực thi, tạm dừng, tiếp tục, kiểm thử, nghiệm thu và truy vết một cách nhất quán theo mô hình **Executable Sprint Package (ESPK)**.


---

# Source: DIP-05

- Path: `docs/DIP/DIP-05.md`
- Set: `DIP`
- Version: `2.1`
- Status: `FROZEN`

# AI Prompt Orchestration & Task Assembly Standard

## DIP-05

---

# 1. Purpose

AI Prompt Orchestration định nghĩa quy trình tạo Prompt cuối cùng được gửi tới AI Coding Agent.

Prompt không được viết thủ công.

Prompt phải được sinh tự động từ:

- Sprint Manifest
- Task Manifest
- Context
- Seed Package
- Repository State
- Engineering Standards

Prompt là kết quả của Prompt Assembly.

---

# 2. Position in Software Factory

```text
Sprint Package

↓

Context Resolution

↓

Seed Resolution

↓

Prompt Orchestration

↓

Prompt Assembly

↓

AI Coding Agent

↓

Validation
```

Prompt Orchestration là bước cuối cùng trước AI Coding.

---

# 3. Objectives

Prompt Assembly nhằm:

- chuẩn hóa Prompt;
- giảm Prompt thủ công;
- giảm Hallucination;
- tối ưu Token;
- tăng khả năng tái lập;
- tăng chất lượng Source Code;
- độc lập AI Provider.

---

# 4. Principles

Prompt Assembly tuân thủ:

- Context First
- Seed First
- Task Driven
- Minimal but Complete
- Deterministic
- Explainable
- Provider Independent
- Architecture Safe
- Repeatable

---

# 5. Prompt Pipeline

```text
Sprint Manifest

↓

Task Manifest

↓

Context

↓

Seed

↓

Repository Snapshot

↓

Prompt Template

↓

Prompt Assembly

↓

Prompt Validation

↓

Execution
```

Không được bỏ qua bất kỳ bước nào.

---

# 6. Prompt Components

Một Prompt hoàn chỉnh gồm:

1. Role

2. Objective

3. Sprint Context

4. Task Context

5. Business Context

6. Architecture Constraints

7. Engineering Constraints

8. Repository Constraints

9. Seed Information

10. Implementation Tasks

11. Validation Commands

12. Expected Deliverables

13. Evidence Requirements

14. Completion Criteria

15. Stop Conditions

---

# 7. Standard Prompt Template

```text
ROLE

OBJECTIVE

SPRINT

TASK

BUSINESS CONTEXT

ARCHITECTURE CONTEXT

ENGINEERING CONSTRAINTS

REPOSITORY CONTEXT

SEED INFORMATION

FILES ALLOWED

FILES PROTECTED

IMPLEMENTATION STEPS

VALIDATION COMMANDS

EXPECTED OUTPUT

EXPECTED EVIDENCE

COMPLETION CONDITIONS

STOP CONDITIONS
```

Không được thay đổi thứ tự.

---

# 8. Task-specific Prompt

Mỗi Task có Prompt riêng.

Ví dụ:

```text
t00

Repository Discovery
```

```text
t01

Domain Model
```

```text
t02

Database
```

...

```text
t10

Final Review
```

Không sử dụng Prompt chung cho toàn Sprint.

---

# 9. Prompt Sources

Prompt được sinh từ:

| Source | Purpose |
|----------|----------|
| Sprint Manifest | Scope |
| Task Manifest | Objective |
| BRD | Business |
| ABP | Architecture |
| ESP | Engineering |
| Repository | Existing Code |
| Seed | Demo Data |
| Validation | Commands |

Prompt không sử dụng dữ liệu ngoài Source of Truth.

---

# 10. Repository Awareness

Prompt phải mô tả:

- Module hiện có
- Folder Structure
- Existing APIs
- Existing Database
- Existing Frontend
- Existing Tests

AI không được giả định Repository.

---

# 11. Allowed Changes

Prompt phải khai báo:

```text
Allowed:

apps/api/modules/product

packages/common/product

apps/admin/product
```

Protected:

```text
docs/

architecture/

database/history/

legacy/
```

AI không được sửa ngoài phạm vi.

---

# 12. Token Budget

Prompt Assembly phải:

- ưu tiên Context gần nhất;
- loại bỏ dữ liệu dư thừa;
- không lặp lại Standards;
- chỉ nạp Capability liên quan.

Prompt phải tối ưu Token.

---

# 13. Prompt Compression

Có thể rút gọn:

- BRD
- ESP
- SGP

nhưng không được thay đổi ý nghĩa.

Prompt phải giữ nguyên Constraint.

---

# 14. Stop Conditions

AI phải dừng khi:

- Architecture Conflict
- Missing Context
- Missing Dependency
- Protected File Modification
- Validation Failure
- Repository Conflict

Không được tiếp tục Coding.

---

# 15. Prompt Validation

Trước khi gửi AI:

Kiểm tra:

- Context đủ
- Seed đủ
- Prompt đủ Section
- Files Allowed
- Validation Commands
- Completion Criteria

Prompt không đạt thì không thực thi.

---

# 16. AI Provider Compatibility

Prompt phải chạy được với:

- Codex
- Claude Code
- Gemini CLI
- Cursor Agent
- OpenHands

Không Hardcode Prompt theo AI.

---

# 17. Prompt Versioning

Prompt có:

- Version
- Sprint
- Task
- Capability
- Timestamp

Prompt được lưu cùng Evidence.

---

# 18. Prompt Logging

Runner phải lưu:

```text
prompts/

t00.prompt.md

t01.prompt.md

...

t10.prompt.md
```

Prompt đã sử dụng phải được lưu để Audit.

---

# 19. Rules

PROMPT-001 — Prompt được sinh tự động.

PROMPT-002 — Prompt phải dùng Context Resolution.

PROMPT-003 — Prompt phải dùng Seed Information.

PROMPT-004 — Prompt phải có Files Allowed.

PROMPT-005 — Prompt phải có Files Protected.

PROMPT-006 — Prompt phải có Validation Commands.

PROMPT-007 — Prompt phải có Completion Criteria.

PROMPT-008 — Prompt phải có Stop Conditions.

PROMPT-009 — Prompt phải được Version hóa.

PROMPT-010 — Prompt phải lưu vào Evidence.

---

# 20. Compliance Checklist

| Rule | Validation |
|------|------------|
| PAC-0501 | Prompt đúng Template |
| PAC-0502 | Context đầy đủ |
| PAC-0503 | Seed đầy đủ |
| PAC-0504 | Files Allowed đầy đủ |
| PAC-0505 | Files Protected đầy đủ |
| PAC-0506 | Validation Commands đầy đủ |
| PAC-0507 | Completion Criteria đầy đủ |
| PAC-0508 | Stop Conditions đầy đủ |
| PAC-0509 | Prompt được lưu |
| PAC-0510 | Tuân thủ DIP |

---

# 21. Relationship to Other Documents

DIP-05 liên kết với:

- DIP-00 Implementation Constitution
- DIP-01 Executable Sprint Package Standard
- DIP-02 AI Context Resolution & Prompt Assembly Standard
- DIP-03 Seed & Reference Data Standard
- DIP-04 AI Execution Runtime & Bash Runner Standard
- ESP Engineering Standards Pack
- SGP Sprint Governance Pack
- VAP Verification & Acceptance Pack

DIP-05 là tiêu chuẩn chính thức cho Prompt Orchestration của YSim AI Software Factory.

---

# 22. Document Status

**Status: FROZEN**

Từ phiên bản 2.1, mọi Prompt gửi tới AI Coding Agent phải được tạo thông qua Prompt Orchestration theo tiêu chuẩn của DIP-05.

Prompt không còn là nội dung được soạn thủ công mà là một Artifact được sinh tự động từ Sprint Package, Context, Seed Information và Repository State.

Prompt trở thành một thành phần của Evidence Package và phải được lưu trữ, version hóa và truy vết giống như Source Code.


---

# Source: DIP-06

- Path: `docs/DIP/DIP-06.md`
- Set: `DIP`
- Version: `2.1`
- Status: `FROZEN`

# Validation, Evidence & Acceptance Standard

## DIP-06

---

# 1. Purpose

Validation, Evidence & Acceptance Standard định nghĩa tiêu chuẩn xác minh, thu thập bằng chứng và nghiệm thu đối với mọi Executable Sprint Package (ESPK).

Một Sprint chỉ được xem là hoàn thành khi:

- Validation PASS;
- Evidence đầy đủ;
- Capability được Acceptance.

Build thành công không đồng nghĩa Sprint hoàn thành.

---

# 2. Position in Software Factory

```text
AI Coding

↓

Build

↓

Validation

↓

Evidence

↓

Capability Demonstration

↓

Acceptance

↓

Git Commit

↓

Release
```

Validation và Acceptance là điều kiện bắt buộc trước Release.

---

# 3. Objectives

Tiêu chuẩn này nhằm:

- xác minh chất lượng Source Code;
- chứng minh Capability hoạt động;
- tạo Evidence phục vụ Audit;
- chuẩn hóa Acceptance;
- hỗ trợ Release;
- hỗ trợ Rollback.

---

# 4. Principles

Validation & Acceptance tuân thủ:

- Validate Everything
- Evidence by Design
- Demonstration First
- Repeatable
- Explainable
- Traceable
- AI Independent
- Automation First
- Capability Oriented

---

# 5. Validation Model

Validation gồm nhiều tầng.

```text
Source

↓

Build

↓

Static Analysis

↓

Unit Test

↓

Integration Test

↓

Contract Test

↓

Frontend Test

↓

End-to-End Test

↓

Compliance

↓

Capability Demonstration
```

Không được bỏ qua tầng Validation bắt buộc.

---

# 6. Validation Categories

| Category | Purpose |
|----------|----------|
| Build Validation | Kiểm tra Build |
| Static Validation | Lint, Type Check |
| Unit Validation | Business Logic |
| Integration Validation | Service Interaction |
| Contract Validation | API Compatibility |
| Frontend Validation | UI & Components |
| E2E Validation | User Journey |
| Compliance Validation | ESP / SGP / DIP |
| Runtime Validation | Execution Runtime |
| Demonstration Validation | Demo Scenario |

---

# 7. Capability Demonstration

Capability có UI phải chứng minh được:

- Login
- CRUD
- Search
- Checkout
- Payment
- Dashboard
- Reporting

(tùy Capability)

Demonstration là một phần của Validation.

---

# 8. Evidence Model

Mỗi Task phải sinh:

- Execution Log
- Validation Result
- Build Output
- Test Output
- Git Diff

Mỗi Sprint phải sinh:

- Sprint Report
- Capability Report
- Demonstration Report
- Acceptance Report

---

# 9. Evidence Package

```text
evidence/

├── prompts/

├── logs/

├── validation/

├── screenshots/

├── videos/

├── reports/

├── git/

└── acceptance/
```

Evidence Package phải được lưu cùng Sprint.

---

# 10. Frontend Evidence

Capability có Frontend phải có:

- Screenshot
- Navigation Flow
- UI Components
- Theme Verification
- Responsive Verification

Nếu phù hợp, bổ sung Video Demonstration.

---

# 11. Acceptance Criteria

Capability được ACCEPT khi:

✓ Build PASS

✓ Validation PASS

✓ Tests PASS

✓ Demonstration PASS

✓ Evidence đầy đủ

✓ Documentation cập nhật

✓ Git Commit thành công

---

# 12. Acceptance Checklist

Acceptance tối thiểu gồm:

- Business Rules
- API
- Database
- Frontend
- Design System
- Experience API
- Security
- Performance
- Documentation

---

# 13. PASS / FAIL Rules

Capability:

PASS

khi:

- không có Validation Error;
- không có Critical Bug;
- Acceptance PASS.

FAIL

khi:

- Build FAIL;
- Test FAIL;
- Demonstration FAIL;
- Architecture Conflict;
- Business Conflict.

---

# 14. Validation Report

Runner phải sinh:

```text
validation/

summary.md

build.md

tests.md

compliance.md

acceptance.md
```

Validation Report là đầu ra bắt buộc.

---

# 15. Evidence Traceability

Mọi Evidence phải truy vết được:

```text
Sprint

↓

Task

↓

Prompt

↓

Commit

↓

Report

↓

Acceptance
```

Không được có Evidence mồ côi.

---

# 16. Acceptance Authority

Acceptance được thực hiện bởi:

- AI Runtime (tự động)
- Developer Review
- Technical Lead
- Product Owner (nếu cần)

AI chỉ được đánh dấu PASS khi đáp ứng đầy đủ Checklist.

---

# 17. Failure Handling

Nếu Validation FAIL:

Runner phải:

- dừng Sprint;
- lưu Log;
- lưu Prompt;
- lưu Exit Code;
- sinh Failure Report.

Không Commit.

---

# 18. Rules

VAL-001 — Validation sau từng Task.

VAL-002 — Evidence sau từng Task.

VAL-003 — Capability có UI phải Demonstration.

VAL-004 — Acceptance bắt buộc.

VAL-005 — Screenshot là bắt buộc với Frontend.

VAL-006 — Validation Report phải sinh tự động.

VAL-007 — Failure Report phải được lưu.

VAL-008 — Không Commit khi Acceptance FAIL.

VAL-009 — Evidence phải Version hóa.

VAL-010 — Sprint chỉ COMPLETE khi Acceptance PASS.

---

# 19. Compliance Checklist

| Rule | Validation |
|------|------------|
| VAC-0601 | Build PASS |
| VAC-0602 | Tests PASS |
| VAC-0603 | Compliance PASS |
| VAC-0604 | Demonstration PASS |
| VAC-0605 | Frontend Evidence đầy đủ |
| VAC-0606 | Acceptance PASS |
| VAC-0607 | Failure Handling đúng chuẩn |
| VAC-0608 | Evidence đầy đủ |
| VAC-0609 | Git Commit thành công |
| VAC-0610 | Tuân thủ DIP |

---

# 20. Relationship to Other Documents

DIP-06 liên kết với:

- DIP-00 Implementation Constitution
- DIP-01 Executable Sprint Package Standard
- DIP-02 AI Context Resolution & Prompt Assembly Standard
- DIP-03 Seed & Reference Data Standard
- DIP-04 AI Execution Runtime & Bash Runner Standard
- DIP-05 AI Prompt Orchestration & Task Assembly Standard
- ESP Engineering Standards Pack
- SGP Sprint Governance Pack
- VAP Verification & Acceptance Pack
- ROP Release & Operations Pack

DIP-06 là tiêu chuẩn chính thức cho Validation, Evidence và Acceptance của YSim AI Software Factory.

---

# 21. Acceptance Workflow

```text
Task Completed

↓

Build

↓

Validation

↓

Evidence Collection

↓

Capability Demonstration

↓

Acceptance Checklist

↓

PASS

↓

Git Commit

↓

Next Task
```

Nếu FAIL ở bất kỳ bước nào:

```text
Failure Report

↓

Stop Sprint

↓

ACP (nếu có Architecture Conflict)
```

---

# 22. Document Status

**Status: FROZEN**

Từ phiên bản 2.1, mọi Sprint của YSim phải hoàn thành đầy đủ ba giai đoạn:

- Validation
- Evidence
- Acceptance

Capability chỉ được coi là **Completed** khi vượt qua toàn bộ Validation Pipeline, tạo đủ Evidence Package và được Acceptance theo tiêu chuẩn của DIP-06.

Validation, Evidence và Acceptance là điều kiện bắt buộc trước Git Commit và Release.


---

# Source: DIP-09

- Path: `docs/DIP/DIP-09.md`
- Set: `DIP`
- Version: `2.1`
- Status: `FROZEN`

# AI Execution Governance & Exception Handling Standard

## DIP-09

---

# 1. Purpose

AI Execution Governance định nghĩa các quy tắc điều phối, giám sát và xử lý ngoại lệ trong quá trình AI Coding Assistant thực thi Executable Sprint Package (ESPK).

Tiêu chuẩn này bảo đảm AI luôn hoạt động trong phạm vi Architecture đã được phê duyệt và có cơ chế dừng, khôi phục hoặc chuyển giao khi gặp tình huống vượt ngoài thẩm quyền.

Governance là lớp bảo vệ cuối cùng của Software Factory.

---

# 2. Position in Software Factory

```text
Architecture

↓

Implementation

↓

AI Execution Governance

↓

AI Runtime

↓

Capability Delivery

↓

Validation

↓

Acceptance
```

Governance áp dụng xuyên suốt toàn bộ vòng đời Sprint.

---

# 3. Objectives

AI Execution Governance nhằm:

- bảo đảm AI tuân thủ Architecture;
- chuẩn hóa xử lý ngoại lệ;
- hỗ trợ Human-in-the-loop;
- bảo vệ Repository;
- giảm Hallucination;
- giảm Scope Drift;
- bảo đảm Auditability.

---

# 4. Principles

Governance tuân thủ:

- Architecture First
- Human Override
- Explainable AI
- Fail Fast
- Stop on Uncertainty
- Traceable
- Repeatable
- Least Privilege
- Controlled Automation

---

# 5. Governance Scope

Governance áp dụng cho:

- Sprint Planning
- Prompt Assembly
- AI Execution
- Validation
- Repository
- Git
- Demonstration
- Acceptance

Không giới hạn ở AI Coding.

---

# 6. AI Decision Authority

AI được phép:

- sinh Source Code;
- tạo Migration;
- sinh API;
- tạo Frontend;
- sinh Tests;
- sinh Documentation;
- tạo Seed Data;
- Commit theo quy tắc.

AI không được phép:

- thay đổi Architecture Frozen;
- thay đổi Meta Model;
- thay đổi Business Domain;
- sửa Protected Files;
- bỏ qua Validation;
- bỏ qua Acceptance.

---

# 7. Exception Classification

Ngoại lệ được phân loại:

| Level | Description |
|---------|-------------|
| E0 | Information |
| E1 | Warning |
| E2 | Validation Failure |
| E3 | Repository Conflict |
| E4 | Architecture Conflict |
| E5 | Security Violation |
| E6 | Human Approval Required |

---

# 8. Stop Conditions

AI phải dừng ngay khi:

- Architecture Conflict
- Missing Context
- Missing Dependency
- Protected File Modification
- Repository Corruption
- Security Policy Violation
- Validation Failure (Critical)

Không được tự tiếp tục.

---

# 9. Recovery Policy

Recovery chỉ được phép khi:

- Dependency được bổ sung;
- Validation PASS sau khi sửa;
- Repository sạch;
- Human chấp thuận (nếu cần).

Recovery phải tiếp tục từ Checkpoint gần nhất.

---

# 10. Retry Policy

Retry chỉ áp dụng cho:

- Timeout;
- Network Failure;
- AI Provider Unavailable;
- Temporary Infrastructure Error.

Không Retry khi:

- Business Rule Conflict;
- Architecture Conflict;
- Validation Logic Failure.

---

# 11. Human-in-the-loop

Con người có quyền:

- Approve;
- Reject;
- Retry;
- Resume;
- Skip (nếu chính sách cho phép);
- Stop Sprint.

Mọi quyết định đều phải được ghi vào Evidence.

---

# 12. ACP & ADR Trigger

Runner phải tạo ACP khi phát hiện:

- Architecture Conflict;
- Capability vượt Scope;
- Meta Model thay đổi;
- Business Domain mới.

Runner phải yêu cầu ADR khi:

- thay đổi Decision đã Frozen;
- thay đổi Design Pattern;
- thay đổi Platform Strategy.

AI không được tự quyết định.

---

# 13. Repository Protection

Protected Areas:

```text
docs/frozen/
architecture/
release/
database/history/
```

AI không được sửa nếu Sprint không cho phép.

---

# 14. Audit Trail

Mọi Sprint phải lưu:

- Prompt;
- Context;
- Seed;
- Commands;
- Logs;
- Validation;
- Evidence;
- Git Diff;
- Exception Report.

Audit Trail là bắt buộc.

---

# 15. Escalation Flow

```text
Warning

↓

Validation Failure

↓

Recovery

↓

Retry

↓

Human Review

↓

ACP / ADR

↓

Stop Sprint
```

Không được bỏ qua bước Escalation.

---

# 16. Governance States

Một Sprint chỉ có thể ở một trong các trạng thái:

- Planned
- Running
- Waiting
- Validation Failed
- Blocked
- Human Review
- Accepted
- Completed
- Cancelled

Runner phải lưu trạng thái hiện tại.

---

# 17. AI Provider Failure

Nếu AI Provider:

- Timeout;
- Rate Limited;
- Unavailable;

Runner phải:

- Retry theo Policy;
- lưu Error;
- không làm mất State.

Không được Restart Sprint từ đầu.

---

# 18. Exception Report

Nếu Sprint FAIL phải sinh:

```text
reports/

exception.md

failure.md

recovery.md
```

Exception Report là Deliverable bắt buộc.

---

# 19. Governance Rules

GOV-001 — AI phải tuân thủ Architecture.

GOV-002 — AI không được sửa Protected Files.

GOV-003 — Architecture Conflict phải tạo ACP.

GOV-004 — Design Decision thay đổi phải tạo ADR.

GOV-005 — Validation Critical Failure phải dừng Sprint.

GOV-006 — Human Override phải được ghi nhận.

GOV-007 — Retry theo Policy.

GOV-008 — Recovery theo Checkpoint.

GOV-009 — Audit Trail là bắt buộc.

GOV-010 — Không AI nào được vượt quá Governance Policy.

---

# 20. Compliance Checklist

| Rule | Validation |
|------|------------|
| GVC-0901 | Governance Policy được áp dụng |
| GVC-0902 | Protected Files không bị sửa |
| GVC-0903 | ACP được tạo khi cần |
| GVC-0904 | ADR được yêu cầu khi cần |
| GVC-0905 | Retry đúng Policy |
| GVC-0906 | Recovery đúng Checkpoint |
| GVC-0907 | Audit Trail đầy đủ |
| GVC-0908 | Human Review được ghi nhận |
| GVC-0909 | Exception Report đầy đủ |
| GVC-0910 | Tuân thủ DIP |

---

# 21. Relationship to Other Documents

DIP-09 liên kết với:

- DIP-00 Implementation Constitution
- DIP-01 Executable Sprint Package Standard
- DIP-02 AI Context Resolution & Prompt Assembly Standard
- DIP-03 Seed & Reference Data Standard
- DIP-04 AI Execution Runtime & Bash Runner Standard
- DIP-05 AI Prompt Orchestration & Task Assembly Standard
- DIP-06 Validation, Evidence & Acceptance Standard
- DIP-07 Repository Workflow & Git Strategy Standard
- DIP-08 Full-stack Capability Delivery Standard
- AFM-00 Architecture Freeze Manifest
- AAP AI Architecture Principles
- SGP Sprint Governance Principles
- ESP Engineering Standards
- ROP Release & Operations Pack

DIP-09 là lớp Governance cao nhất của Development & Implementation Pack.

---

# 22. AI Execution Governance Workflow

```text
Sprint Planned

↓

Context Loaded

↓

Prompt Generated

↓

AI Execution

↓

Validation

↓

Exception?

├── No
│
│   ↓
│
│ Acceptance
│
│   ↓
│
│ Complete
│
└── Yes
    ↓
Exception Classification
    ↓
Recovery / Retry
    ↓
Human Review (nếu cần)
    ↓
ACP / ADR (nếu cần)
    ↓
Resume hoặc Stop
```

---

# 23. Document Status

**Status: FROZEN**

DIP-09 là tài liệu cuối cùng của **Implementation Foundation**.

Từ phiên bản **YSim AI Software Factory v2.1**, mọi Sprint phải được thực thi dưới sự điều phối của **AI Execution Governance**.

Không AI Coding Agent nào được phép vượt qua các giới hạn về Architecture, Governance, Validation hoặc Security đã được định nghĩa trong Development & Implementation Pack.

Implementation Foundation (DIP-00 → DIP-09) được xem là **Architecture & Execution Baseline** cho toàn bộ quá trình phát triển YSim.


---

# Source: ECS-00

- Path: `docs/ECS/ECS-00.md`
- Set: `ECS`
- Version: `1.0`
- Status: `Draft`

# ECS-00 — Experience Configuration Schema

---

# 1. Purpose

This document defines the canonical configuration schema used by the YSim Experience Runtime.

The schema standardizes how runtime configurations are represented, validated, inherited, published and consumed across the platform.

All runtime configuration must conform to the ECS specification.

This document applies to:

- Experience Profiles
- Storefront Profiles
- Themes
- Templates
- Sections
- Widgets
- Business Bindings
- Runtime Policies
- Published Snapshots

---

# 2. Design Goals

The ECS model follows several principles.

- Human readable
- Machine readable
- Version controlled
- Inheritable
- Immutable after publishing
- AI friendly
- Schema validated
- Backward compatible

---

# 3. Configuration Hierarchy

Configuration follows a hierarchical model.

```
Platform

↓

Organization

↓

Storefront

↓

Campaign

↓

Tracking

↓

Runtime Override
```

Each layer overrides only necessary properties.

---

# 4. Configuration Object

Every ECS object shares the same metadata.

```yaml
id:
code:
name:
description:

schemaVersion:

status:

owner:

createdAt:

updatedAt:

inherits:

tags:

metadata:
```

---

# 5. Experience Profile

Experience Profile defines presentation behavior.

Example

```yaml
experienceProfile:

  id: EXP-DEFAULT

  theme: YSIM-GREEN

  navigation: NAV-DEFAULT

  layout: LAYOUT-TRAVEL

  assets: ASSET-DEFAULT

  localization: LOC-GLOBAL

  runtimePolicies:

    - POLICY-001

    - POLICY-002
```

---

# 6. Theme Configuration

```yaml
theme:

  preset: ysim-green

  colors:

    primary: "#2BA84A"

    secondary: "#6D6F72"

    success: "#00B050"

    warning: "#F5A623"

    danger: "#E53935"

  typography:

    heading: Inter

    body: Inter

  radius:

    default: 12

  spacing:

    scale: default

  icons:

    provider: heroicons
```

---

# 7. Storefront Profile

A Storefront Profile combines Experience and Commerce.

```yaml
storefront:

  storefrontId: STOREFRONT-JP

  experienceProfile: EXP-JAPAN

  businessProfile: BUS-JAPAN

  catalog: CAT-JAPAN

  pricingProfile: PRICE-JP

  paymentProfile: PAYMENT-JP

  checkoutFlow: CHECKOUT-DEFAULT

  supportProfile: SUPPORT-JP

  localization: JA-JP
```

---

# 8. Business Profile

Business Profile references platform capabilities.

```yaml
businessProfile:

  catalog:

    reference: CAT-JAPAN

  pricing:

    reference: PRICE-JAPAN

  promotion:

    reference: PROMO-SUMMER

  payment:

    reference: PAYMENT-JP

  checkout:

    reference: CHECKOUT-DEFAULT

  support:

    reference: SUPPORT-JP

  fulfillment:

    reference: FULFILLMENT-STANDARD
```

Business Profiles never reference suppliers.

---

# 9. Section Configuration

Each section is independently configurable.

```yaml
section:

  type: featured-products

  enabled: true

  order: 20

  layout:

    columns: 4

  businessBinding:

    catalog: CAT-JAPAN

    pricing: PRICE-JAPAN

    promotion: PROMO-JP

  rendering:

    card: PACKAGE-CARD

    style: default
```

---

# 10. Widget Configuration

Widgets are presentation components.

```yaml
widget:

  type: package-card

  component: PACKAGE_CARD

  datasource:

    capability: Catalog

  properties:

    showPrice: true

    showCoverage: true

    showPromotion: true
```

Widgets never access databases directly.

---

# 11. Business Binding

Business Binding connects UI with Platform Capabilities.

```yaml
businessBinding:

  capability: Catalog

  bindingType: reference

  referenceId: CAT-JAPAN

  fallback: inherit
```

Another example

```yaml
businessBinding:

  capability: Pricing

  referenceId: PRICE-JAPAN
```

---

# 12. Runtime Policy

Runtime Policies define dynamic behavior.

```yaml
runtimePolicy:

  guestCheckout: true

  requireOtp: false

  allowGuestPurchase: true

  enablePromotion: true

  enableRecommendations: false
```

---

# 13. Localization Profile

```yaml
localization:

  locale: ja-JP

  currency: JPY

  timezone: Asia/Tokyo

  paymentProfile: PAYMENT-JP

  supportProfile: SUPPORT-JP

  terms: TERMS-JP
```

---

# 14. Asset Profile

```yaml
assets:

  logo: LOGO-JAPAN

  favicon: ICON-JAPAN

  hero: HERO-JAPAN

  footer: FOOTER-JAPAN
```

---

# 15. Navigation Profile

```yaml
navigation:

  profile: NAV-DEFAULT

  items:

    - Home

    - Packages

    - Coverage

    - FAQ

    - Support
```

---

# 16. Inheritance

Objects inherit from parents.

```yaml
inherits:

  from: STORE-DEFAULT

  strategy: merge
```

Supported strategies:

- merge
- replace
- append
- remove

---

# 17. Merge Rules

Configuration merge follows deterministic rules.

| Type | Strategy |
|------|----------|
| Scalar | Replace |
| Object | Merge |
| List | Replace by default |
| Ordered List | Replace |
| Map | Merge |

Platform implementations must not invent merge rules.

---

# 18. Validation

Every configuration must pass validation.

Examples:

- Required fields
- Existing references
- Circular inheritance detection
- Invalid capability references
- Invalid localization
- Invalid payment profile

Invalid configurations cannot be published.

---

# 19. Published Snapshot

Published snapshots are immutable.

```yaml
snapshot:

  version: 5

  storefront: STOREFRONT-JP

  experienceProfile: EXP-JP

  businessProfile: BUS-JP

  checksum: SHA256

  publishedAt: 2026-07-12T08:00:00Z
```

Runtime always consumes snapshots.

---

# 20. Versioning

Every configuration is versioned.

```
Draft

↓

Revision

↓

Published

↓

Archived
```

Previous versions remain available for rollback.

---

# 21. AI Implementation Guidelines

AI agents shall:

- Never invent configuration fields.
- Always follow ECS schema.
- Keep Experience and Business configurations separate.
- Use references instead of embedding duplicated objects.
- Validate references before publishing.
- Support inheritance.
- Support fallback.
- Support immutable snapshots.

---

# 22. Architectural Principles

### ECS-001

Every runtime configuration follows ECS.

---

### ECS-002

Every object is versioned.

---

### ECS-003

Every object supports inheritance.

---

### ECS-004

Every object supports validation.

---

### ECS-005

Published configurations are immutable.

---

### ECS-006

Experience configuration is independent from business configuration.

---

### ECS-007

Business configuration references Capabilities.

---

### ECS-008

Business configuration never references Suppliers.

---

### ECS-009

Configuration merge is deterministic.

---

### ECS-010

Runtime consumes Published Snapshots only.

---

# 23. References

This document should be read together with:

- UXF-00 ~ UXF-05
- CAP-00
- BRD
- ABP
- AFM
- YADF
- DIP


---

# Source: ESP-00

- Path: `docs/ESP/ESP-00.md`
- Set: `ESP`
- Version: `2.1`
- Status: `FROZEN`

# Engineering Standards Overview

## ESP-00

---

# 1. Purpose

Engineering Standards Pack (ESP) định nghĩa toàn bộ tiêu chuẩn kỹ thuật của nền tảng YSim.

ESP là nền tảng để đảm bảo:

- Consistency
- Maintainability
- Scalability
- Security
- Quality
- AI Compatibility

ESP áp dụng cho:

- AI Coding Agent
- Developer
- Reviewer
- QA
- DevOps
- Release Team

---

# 2. Objectives

Engineering Standards nhằm:

- Chuẩn hóa toàn bộ hoạt động kỹ thuật.
- Đảm bảo mọi Sprint triển khai theo cùng một tiêu chuẩn.
- Hạn chế Technical Debt.
- Đảm bảo khả năng bảo trì dài hạn.
- Hỗ trợ AI sinh mã nguồn ổn định và nhất quán.

---

# 3. Engineering Principles

YSim Engineering tuân thủ các nguyên tắc:

- Architecture First
- Contract Driven
- Domain Driven
- Convention over Configuration
- Security by Default
- Testability
- Observability
- Automation First
- AI Friendly
- Backward Compatibility (khi áp dụng)
- Full-stack Engineering
- Experience-driven Engineering

---

# 4. Engineering Scope

ESP áp dụng cho toàn bộ:

- Repository
- Source Code
- Database
- API
- Event
- Snapshot
- Configuration
- Testing
- Documentation
- Deployment
- Operations
- Frontend
- Design System
- Storefront Experience

---

# 5. Engineering Hierarchy

Engineering Standards được áp dụng theo thứ tự ưu tiên sau:

```text
BRD
    │
Enterprise Registry
    │
YADF
    │
ABP
    │
AAP
    │
SGP
    │
ESP
    │
DIP
```

Nếu có xung đột:

Tài liệu ở tầng trên luôn có độ ưu tiên cao hơn.

---

# 6. Engineering Layers

ESP được chia thành các nhóm tiêu chuẩn.

| Layer | Description |
|---------|-------------|
| Repository | Repository & Folder Standards |
| Source Code | Coding Standards |
| Naming | Naming Convention |
| Database | Database Standards |
| API | API Standards |
| Migration | Migration Standards |
| Testing | Testing Standards |
| Logging | Logging Standards |
| Security | Security Standards |
| Configuration | Configuration Standards |
| Documentation | Documentation Standards |
| Git | Version Control Standards |
| Performance | Performance Standards |
| Release | Release Standards |
| Frontend | Frontend Engineering Standards |
| Design System | Design System Standards |
| Experience | Experience Delivery Standards |

---

# 6A. Full-stack Engineering Model

Đối với Capability có giao diện người dùng, Engineering Standards áp dụng đồng thời cho:

- Backend
- API
- Frontend
- Design System
- Seed Data
- Capability Demonstration

Không được coi Frontend là hạng mục triển khai độc lập ngoài Sprint.

---

# 7. Engineering Responsibilities

ESP quy định trách nhiệm cho:

| Role | Responsibility |
|------|----------------|
| AI Coding Agent | Tuân thủ toàn bộ Engineering Standards |
| Developer | Thực hiện theo Standards |
| Reviewer | Kiểm tra việc tuân thủ Standards |
| QA | Xác minh kết quả triển khai |
| Architecture Owner | Ban hành và cập nhật Standards |
| Release Manager | Kiểm tra Standards trước Release |

Không có ngoại lệ nếu chưa được Architecture Owner phê duyệt.

---

# 8. Standards Lifecycle

Một Engineering Standard có vòng đời:

```text
Draft
    │
    ▼
Review
    │
    ▼
Approved
    │
    ▼
Published
    │
    ▼
Adopted
    │
    ▼
Deprecated
    │
    ▼
Archived
```

Mọi thay đổi Standards phải được quản trị theo Governance.

---

# 9. Compliance Model

Mỗi Sprint phải chứng minh việc tuân thủ ESP.

Các mức đánh giá:

| Status | Description |
|---------|-------------|
| Compliant | Tuân thủ đầy đủ |
| Compliant with Exceptions | Có ngoại lệ đã được phê duyệt |
| Non-Compliant | Không tuân thủ |

Mọi Exception phải được ghi nhận và phê duyệt.

---

# 10. Standards Enforcement

Engineering Standards được kiểm soát thông qua:

- AI Verification
- Human Review
- Code Review
- Static Analysis
- Automated Validation
- CI/CD Pipeline

Không được kiểm tra Standards thủ công nếu có thể tự động hóa.

---

# 11. Engineering Artifacts

ESP áp dụng cho các Artifact:

- Source Code
- Configuration
- API Contract
- Database Schema
- Migration
- Test Suite
- Documentation
- Deployment Manifest
- Release Manifest
- Frontend Assets
- Design Tokens
- Demonstration Assets

Mỗi Artifact phải tuân thủ Standards tương ứng.

---

# 12. Engineering Metrics

Platform theo dõi:

- Standards Compliance Rate
- Code Review Findings
- Static Analysis Findings
- Technical Debt
- Security Violations
- Documentation Coverage
- Test Coverage
- AI Compliance Rate
- Frontend Standards Compliance
- Design System Compliance

Các Metrics phục vụ Continuous Improvement.

---

# 13. Standards Rules

ES-001 — Mọi Sprint phải tuân thủ ESP.

ES-002 — AI phải tuân thủ ESP.

ES-003 — Developer phải tuân thủ ESP.

ES-004 — Standards được kiểm tra tự động khi có thể.

ES-005 — Không được bỏ qua Standards nếu không có Exception được phê duyệt.

ES-006 — Standards phải có Version.

ES-007 — Standards phải có Traceability.

ES-008 — Standards phải hỗ trợ Audit.

ES-009 — Standards phải hỗ trợ AI Coding.

ES-010 — Standards là Technical Constitution của Platform.

ES-011 — Capability có UI phải tuân thủ Full-stack Engineering Standards.

ES-012 — Frontend và Design System phải được kiểm tra cùng Backend.

---

# 14. Engineering Resolution Pipeline (ERP)

```text
Architecture

↓

Engineering Standards

↓

Sprint Implementation

↓

Capability Demonstration

↓

Validation

↓

Verification

↓

Compliance

↓

Release
```

Engineering Resolution Pipeline là chuỗi thực thi chuẩn của mọi Sprint.

---

# 15. Engineering Standards Roadmap

Engineering Standards Pack bao gồm:

| Code | Document |
|------|----------|
| ESP-00 | Engineering Standards Overview |
| ESP-01 | Repository Standards |
| ESP-02 | Source Code Standards |
| ESP-03 | Naming Standards |
| ESP-04 | API Standards |
| ESP-05 | Database Standards |
| ESP-06 | Migration Standards |
| ESP-07 | Testing Standards |
| ESP-08 | Logging & Observability Standards |
| ESP-09 | Configuration Standards |
| ESP-10 | Security Standards |
| ESP-11 | Documentation Standards |
| ESP-12 | Version Control Standards |
| ESP-13 | Code Review Standards |
| ESP-14 | Performance Standards |
| ESP-15 | Release Standards |

---

# 16. Relationship to Other Documents

ESP liên kết với:

- BRD Workshop
- Enterprise Registry
- YADF
- ABP
- AAP
- SGP
- DIP
- VAP
- ROP

ESP là bộ tiêu chuẩn kỹ thuật áp dụng cho toàn bộ hoạt động Engineering của nền tảng YSim, bao gồm Backend, Frontend, Design System và Experience Delivery.

---

# 17. Document Status

**Status: FROZEN**

ESP-00 là tài liệu nền tảng quy định hệ thống Engineering Standards của YSim.

Mọi AI Agent, Developer và Engineering Team phải tuân thủ các tiêu chuẩn trong Engineering Standards Pack trước khi triển khai bất kỳ Sprint nào.

---


---

# Source: ESP-01

- Path: `docs/ESP/ESP-01.md`
- Set: `ESP`
- Version: `1.0`
- Status: `FROZEN`

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


---

# Source: ESP-02

- Path: `docs/ESP/ESP-02.md`
- Set: `ESP`
- Version: `1.0`
- Status: `FROZEN`

# Source Code Engineering Standards

## ESP-02

---

# 1. Purpose

Source Code Engineering Standards định nghĩa các tiêu chuẩn xây dựng, tổ chức và bảo trì Source Code trong nền tảng YSim.

Tài liệu này áp dụng cho:

- AI Coding Agent
- Developer
- Reviewer
- QA
- Architecture Owner

Source Code phải được viết để:

- dễ đọc;
- dễ kiểm thử;
- dễ mở rộng;
- dễ bảo trì;
- thân thiện với AI.

---

# 2. Principles

Source Code tuân thủ các nguyên tắc:

- Readability First
- Simplicity
- Maintainability
- Testability
- Deterministic
- Explicit
- Low Coupling
- High Cohesion

---

# 3. Source Code Objectives

Source Code phải:

- phản ánh Business Capability;
- phản ánh Domain Model;
- phản ánh Architecture;
- không chứa Business Logic sai Layer;
- dễ Review;
- dễ Refactor.

---

# 4. Engineering Rules

Source Code phải:

- nhỏ;
- rõ ràng;
- có trách nhiệm duy nhất;
- có khả năng kiểm thử độc lập;
- hạn chế Side Effects.

---

# 5. Module Organization

Một Module chuẩn bao gồm:

```text
module/

controller/

service/

application/

domain/

repository/

dto/

mapper/

events/

tests/
```

Không bắt buộc mọi module phải có đầy đủ các thư mục trên, nhưng phải tuân thủ kiến trúc đã được định nghĩa trong ABP. Không được đặt Business Logic trực tiếp trong `controller`.

---

# 6. Source Code Structure

Thứ tự ưu tiên:

```text
Module

↓

Application

↓

Domain

↓

Infrastructure

↓

Integration
```

Không gọi ngược Layer.

---

# 7. Business Logic

Business Logic chỉ được phép nằm trong:

- Domain
- Application

Không được đặt trong:

- Controller
- DTO
- Mapper
- Integration Adapter
- Configuration

---

# 8. Class Standards

Mỗi Class:

- có một trách nhiệm;
- có tên rõ nghĩa;
- không vượt quá phạm vi trách nhiệm đã thiết kế;
- không phụ thuộc trực tiếp vào Infrastructure nếu không cần thiết.

---

# 9. Method Standards

Method nên:

- ngắn;
- rõ ràng;
- một mục đích;
- hạn chế lồng điều kiện sâu.

Method không nên:

- xử lý nhiều Use Case;
- chứa nhiều nhánh điều kiện không liên quan.

---

# 10. Dependency Injection

Toàn bộ Dependency phải:

- Inject
- Không new trực tiếp Service nếu Framework đã hỗ trợ DI
- Không Singleton thủ công

Dependency Injection phải tuân thủ ABP.

---

# 11. Error Handling

Source Code:

- không swallow exception;
- không ignore error;
- phải trả về Error Model chuẩn;
- phải log đúng chuẩn.

Chi tiết được quy định tại:

ESP-08 Logging Standards

ESP-10 Security Standards

---

# 12. Async Programming

Async phải:

- sử dụng async/await thống nhất;
- không tạo Promise không được await (trừ khi có chủ đích rõ ràng);
- xử lý timeout và cancellation khi phù hợp.

Không được block Event Loop.

---

# 13. Code Reuse

Ưu tiên:

- Shared Package
- Common Library
- Utility
- Base Component

Không copy/paste Business Logic giữa các Module.

---

# 14. Refactoring

Refactoring:

- không thay đổi Business Behavior;
- không thay đổi Public Contract nếu chưa được phê duyệt;
- phải giữ nguyên Sprint Scope.

Refactoring lớn phải được xem xét trong Planning hoặc thông qua ACP nếu ảnh hưởng kiến trúc.

---

# 15. Code Generation

AI sinh mã phải:

- tuân thủ ESP;
- tuân thủ ABP;
- tuân thủ Sprint Contract;
- không sinh mã ngoài Scope;
- không tự tạo Pattern mới.

---

# 16. Code Review Readiness

Code được coi là sẵn sàng Review khi:

- Build PASS;
- Test PASS theo yêu cầu Sprint;
- Static Analysis PASS (nếu áp dụng);
- Documentation đã cập nhật;
- Evidence đã tạo.

---

# 17. Source Code Quality

Mỗi Sprint phải đạt:

- Build Success
- Zero Critical Error
- Zero Compiler Warning (đối với mã nguồn mới hoặc phần được chỉnh sửa, trừ khi có ngoại lệ được phê duyệt)
- Không có TODO/FIXME chưa được theo dõi bằng Work Item
- Không Hardcode Secret
- Không Dead Code mới

---

# 18. Prohibited Practices

Không được:

- Hardcode Credentials
- Hardcode Business Rules
- Circular Dependency
- Duplicate Business Logic
- Commented-out Code
- Unused Public API
- Bypass Architecture

---

# 19. Source Code Rules

SC-001 — Source Code phải phản ánh Architecture.

SC-002 — Business Logic chỉ nằm đúng Layer.

SC-003 — Controller không chứa Business Logic.

SC-004 — Không tạo Circular Dependency.

SC-005 — Mọi Dependency phải được quản lý theo chuẩn của Framework.

SC-006 — AI không được sinh Pattern mới ngoài Standards.

SC-007 — Refactoring không thay đổi Business Behavior.

SC-008 — Source Code phải Reviewable.

SC-009 — Source Code phải Testable.

SC-010 — Source Code phải Maintainable.

---

# 20. Source Code Compliance Checklist

| Rule | Validation |
|------|------------|
| SCC-0201 | Layer đúng chuẩn |
| SCC-0202 | Business Logic đúng vị trí |
| SCC-0203 | Dependency Injection đúng chuẩn |
| SCC-0204 | Không Circular Dependency |
| SCC-0205 | Build PASS |
| SCC-0206 | Test PASS |
| SCC-0207 | Không Hardcode Secret |
| SCC-0208 | Không Dead Code mới |
| SCC-0209 | Source Code Reviewable |
| SCC-0210 | Tuân thủ ESP |

---

# 21. Relationship to Other Documents

ESP-02 liên kết với:

- ESP-01 Repository Architecture Standards
- ESP-03 Naming Standards
- ESP-04 API Standards
- ESP-05 Database Standards
- ESP-07 Testing Standards
- ESP-08 Logging & Observability Standards
- ABP-02 Layered Architecture
- ABP-03 Dependency Architecture

Source Code Engineering Standards là nền tảng cho mọi hoạt động phát triển mã nguồn của YSim.

---

# 22. Document Status

**Status: FROZEN**

ESP-02 là tài liệu chuẩn hóa toàn bộ tiêu chuẩn xây dựng và bảo trì Source Code của YSim.

Mọi AI Agent và Developer phải tuân thủ tài liệu này khi tạo, sửa đổi hoặc tái cấu trúc mã nguồn.

---


---

# Source: ESPK-S00

- Path: `docs/ESPK/ESPK-S00.md`
- Set: `ESPK`
- Version: `2.1`
- Status: `FROZEN`

Sprint-00 — Factory Commissioning & Repository Bootstrap
Type	Foundation Sprint
Deliverable	AI Software Factory Ready
Objective

Sprint-00 có mục tiêu:

Bootstrap Repository
Bootstrap Workspace
Import Documentation
Bootstrap AI Runtime
Bootstrap Factory
Bootstrap Bash Runner
Validate toàn bộ Software Factory

Không phát triển bất kỳ Business Capability nào.

Business Value

Sau Sprint-00:

✅ Repository sẵn sàng

✅ Documentation sẵn sàng

✅ AI Runtime sẵn sàng

✅ Codex Runner sẵn sàng

✅ Prompt Engine sẵn sàng

✅ Seed Repository sẵn sàng

✅ Validation Pipeline sẵn sàng

Deliverables
1. Repository Bootstrap
apps/

packages/

database/

integrations/

infrastructure/

docs/

ai/

factory/

runtime/

scripts/

tools/

.github/
2. Documentation Repository
docs/

AFM/

BRD/

ABP/

YADF/

AAP/

SGP/

ESP/

DIP/

ROP/
3. Factory
factory/

providers/

runtime/

prompts/

contexts/

templates/

seeds/

validation/

evidence/

reports/
4. Runtime
runtime/

logs/

state/

cache/

reports/

evidence/
5. Scripts
scripts/

bootstrap.sh

commission.sh

run-sprint.sh

run-task.sh

resume.sh

validate.sh
6. Provider
factory/providers/

codex/

claude/

gemini/

openhands/

Sprint-00 chỉ implement:

codex/
7. Prompt Templates
factory/prompts/

task.md

review.md

migration.md

refactor.md

hotfix.md
8. Context Templates
factory/contexts/

business.md

architecture.md

engineering.md

repository.md

runtime.md

task.md
9. Seed Repository
factory/seeds/

products/

pricing/

users/

organizations/

themes/

payments/

gigago/

onepay/

gpay/

analytics/
Sprint Tasks

Sprint-00 vẫn sử dụng chuẩn t00 → t10 để đồng nhất với các Sprint sau.

t00 — Repository Discovery

Mục tiêu

Kiểm tra cấu trúc Repository.
Kiểm tra Git.
Kiểm tra Workspace.

Output

Repository Report.
Working Tree Report.
t01 — Workspace Bootstrap

Tạo các thư mục chuẩn:

factory/

runtime/

tools/

Không tạo Business Module.

t02 — Documentation Commissioning

Import Documentation theo Layer:

Layer 0

AFM
YADF
AAP

Layer 1

BRD

Layer 2

ABP

Layer 3

SGP
ESP

Layer 4

DIP

Layer 5

ROP

Sinh:

docs/INDEX.md

docs/MASTER_INDEX.md
t03 — Factory Bootstrap

Tạo:

factory/

providers/

runtime/

templates/

contexts/

prompts/

seeds/

validation/

reports/

evidence/
t04 — Runtime Bootstrap

Sinh:

runtime/

logs/

cache/

state/

reports/

evidence/
t05 — AI Provider Bootstrap

Implement:

factory/providers/codex/

Tạo interface cho:

claude/

gemini/

openhands/
t06 — Prompt & Context Bootstrap

Sinh:

prompt templates

context templates

manifest templates

seed templates
t07 — Validation Bootstrap

Sinh:

validate.sh

preflight.sh

healthcheck.sh

environment.sh

Validation:

Node
pnpm
Git
Docker
Codex CLI
t08 — Dry Run

Runner thực hiện:

Repository

↓

Manifest

↓

Context

↓

Seed

↓

Prompt

↓

Runtime

↓

Validation

Không Coding.

Không Commit Business.

t09 — Evidence Generation

Sinh:

Factory Report

Runtime Report

Environment Report

Repository Report

Validation Report
t10 — Commissioning Report

Sinh:

SPRING-00-REPORT.md

FACTORY_READY.md

COMMISSIONING_REPORT.md

Commit:

chore(s00): commission AI software factory
Acceptance Criteria

Sprint-00 PASS khi:

Repository
 Repository đúng cấu trúc.
Documentation
 Documentation import hoàn chỉnh.
 MASTER_INDEX tồn tại.
Factory
 Factory Bootstrap hoàn tất.
Runtime
 Runtime Bootstrap hoàn tất.
Provider
 Codex Provider hoạt động.
 Provider Interface chuẩn hóa.
Prompt
 Prompt Template đầy đủ.
Seed
 Seed Repository đầy đủ.
Validation
 Validation PASS.
Dry Run
 Dry Run PASS.
Evidence
 Evidence đầy đủ.
Sprint Outputs
Repository

Factory

Runtime

Provider

Prompt

Context

Seed

Validation

Evidence

Reports
Exit Criteria

Sau Sprint-00:

AI Software Factory

STATUS

READY

và mới được phép chuyển sang Sprint-01.


---

# Source: PCS-00

- Path: `docs/PCS/PCS-00.md`
- Set: `PCS`
- Version: `1.0`
- Status: `Draft`

# PCS-00 — Platform Configuration Schema

---

# 1. Purpose

This document defines the canonical configuration model used across the YSim Platform.

The Platform Configuration Schema (PCS) establishes a unified standard for defining, validating, versioning, publishing and consuming configuration objects.

Every configurable object within the platform shall conform to PCS.

PCS applies to:

- Experience Configuration
- Business Configuration
- Commerce Configuration
- Organization Configuration
- Platform Configuration
- Integration Configuration
- Operational Configuration

---

# 2. Objectives

PCS is designed to provide:

- One configuration standard
- Version-controlled configuration
- Immutable published snapshots
- Runtime-safe configuration
- AI-friendly structure
- Deterministic inheritance
- Deterministic merge
- Auditability
- Rollback capability

---

# 3. Configuration Philosophy

Configuration is considered business data.

Configuration is **NOT** application source code.

```
Configuration

↓

Validation

↓

Publish

↓

Snapshot

↓

Runtime
```

Applications consume configuration.

Applications do not own configuration.

---

# 4. Configuration Categories

The platform defines the following configuration groups.

## Foundation

- Organization
- Branding
- Theme
- Localization
- Domain
- Users
- Roles
- Permissions

---

## Experience

- Experience Profile
- Storefront
- Navigation
- Layout
- Components
- Assets

---

## Commerce

- Catalog
- Pricing
- Promotion
- Checkout
- Payment
- Customer
- Product Visibility

---

## Fulfillment

- Allocation Policy
- Fulfillment Policy
- Inventory Policy
- Retry Policy
- Replacement Policy

---

## Integration

- Supplier Gateway
- Payment Gateway
- Notification Gateway
- Webhook
- OAuth
- API Keys

---

## Operations

- Scheduler
- Queue
- Monitoring
- Alert
- Report
- Retention
- Logging

---

# 5. Configuration Metadata

Every configuration object shares common metadata.

```yaml
id:

code:

name:

description:

type:

category:

schemaVersion:

status:

owner:

createdAt:

updatedAt:

createdBy:

updatedBy:

tags:

labels:

metadata:
```

---

# 6. Configuration Identity

Every configuration object shall have:

- Global ID
- Business Code
- Display Name

Example

```yaml
id: CFG-000001

code: PRICE-JAPAN

name: Japan Pricing

type: PricingProfile
```

IDs never change.

Codes remain stable.

Names may change.

---

# 7. Configuration References

Configurations reference other configurations.

References shall use identifiers.

Example

```yaml
catalog:

  reference: CAT-JAPAN
```

Never embed duplicated configuration.

---

# 8. Configuration Composition

Configuration may consist of child configurations.

Example

```
Storefront

↓

Navigation

↓

Menu

↓

Menu Item
```

Child configurations remain independently versioned.

---

# 9. Configuration Inheritance

Inheritance hierarchy

```
Platform

↓

Organization

↓

Storefront

↓

Campaign

↓

Tracking

↓

Runtime Override
```

Children override parent properties.

---

# 10. Merge Strategy

Supported merge strategies

| Strategy | Description |
|----------|-------------|
| replace | Replace parent value |
| merge | Merge objects |
| append | Append list |
| prepend | Prepend list |
| remove | Remove inherited item |
| inherit | Keep parent |

Every configurable property shall specify its merge strategy.

---

# 11. Validation Rules

Configuration validation includes:

- Required fields
- Reference integrity
- Circular dependency detection
- Inheritance validation
- Capability validation
- Policy validation
- Business validation

Invalid configuration cannot be published.

---

# 12. Publish Lifecycle

Configuration lifecycle

```
Draft

↓

Validated

↓

Preview

↓

Published

↓

Archived
```

Only Published configurations are visible to Runtime.

---

# 13. Immutable Snapshots

Publishing generates immutable snapshots.

```
Configuration

↓

Publish

↓

Snapshot

↓

Runtime
```

Snapshots include:

- Version
- Timestamp
- Checksum
- Parent References
- Dependency References

Snapshots cannot be modified.

---

# 14. Runtime Consumption

Runtime never reads Draft configurations.

Runtime always reads Published Snapshots.

```
Snapshot

↓

Cache

↓

Runtime

↓

Rendering
```

---

# 15. Rollback

Rollback restores a previous published snapshot.

```
Snapshot V5

↓

Rollback

↓

Snapshot V4
```

Rollback never edits historical versions.

---

# 16. Configuration Cache

Cache keys may include

- Configuration Type
- Organization
- Storefront
- Locale
- Version
- Snapshot

Cache invalidation occurs only after successful publishing.

---

# 17. Configuration Security

Configuration access shall support:

- Read
- Write
- Publish
- Rollback
- Archive

Permissions are evaluated independently.

---

# 18. Configuration Audit

Every configuration change is audited.

Audit includes:

- Previous Value
- New Value
- User
- Timestamp
- Action
- Reason

Audit records are immutable.

---

# 19. Configuration Dependencies

Configurations may depend on others.

Example

```
Storefront

↓

Catalog

↓

Pricing

↓

Payment

↓

Checkout
```

Dependency graphs must remain acyclic.

---

# 20. Configuration Templates

Frequently used configurations may be published as reusable templates.

Examples

- Theme Template
- Storefront Template
- Pricing Template
- Promotion Template
- Allocation Template

Templates accelerate provisioning.

---

# 21. AI Implementation Guidelines

AI agents shall:

- Never invent configuration structures.
- Always follow PCS.
- Always use references.
- Never duplicate configuration.
- Support inheritance.
- Support deterministic merge.
- Validate before publish.
- Consume snapshots only.

---

# 22. Architectural Principles

### PCS-001

Configuration is business data.

---

### PCS-002

Every configuration has metadata.

---

### PCS-003

Every configuration is versioned.

---

### PCS-004

Every configuration supports validation.

---

### PCS-005

Published configurations are immutable.

---

### PCS-006

Runtime consumes snapshots only.

---

### PCS-007

Configuration supports inheritance.

---

### PCS-008

Configuration merge is deterministic.

---

### PCS-009

Configuration changes are auditable.

---

### PCS-010

Configuration shall be reusable through templates.

---

# 23. Relationship with Other Specifications

| Specification | Responsibility |
|---------------|----------------|
| CAP | Defines business capabilities |
| ECS | Defines Experience Runtime configuration |
| PCS | Defines common configuration model |
| UXF | Defines Experience Architecture |
| ABP | Defines Runtime implementation |
| DMS | Defines business data models |

PCS acts as the foundation for every configuration specification.

---

# 24. Future Extensions

The PCS model is designed to support future configuration domains without changing the core schema.

Potential future extensions include:

- Policy Configuration Schema
- Security Configuration Schema
- Integration Configuration Schema
- AI Configuration Schema
- Workflow Configuration Schema
- Workflow DSL
- Rules Engine Configuration
- Feature Management Configuration

All future schemas shall inherit the conventions defined by PCS.

---

# 25. References

This document should be read together with:

- CAP-00 — Platform Capability Registry
- ECS-00 — Experience Configuration Schema
- UXF-00 ~ UXF-05
- BRD
- ABP
- AFM
- YADF
- DIP


---

# Source: POL-00

- Path: `docs/POL/POL-00.md`
- Set: `POL`
- Version: `1.0`
- Status: `Draft`

# POL-00 — Platform Policy Framework

---

# 1. Purpose

This document defines the Policy Framework used throughout the YSim Platform.

Policies represent configurable business decisions evaluated at runtime.

Rather than embedding decision logic inside application code, YSim externalizes business decisions into reusable Policy objects.

The Policy Framework standardizes:

- Policy Definition
- Policy Evaluation
- Policy Composition
- Policy Inheritance
- Policy Versioning
- Policy Publication
- Policy Runtime

Every configurable business decision shall be represented by a Policy.

---

# 2. Policy Philosophy

Business capabilities describe **what the platform can do**.

Policies describe **when, how and under which conditions those capabilities are allowed to execute**.

```
Capability

↓

Policy

↓

Decision

↓

Execution
```

Capabilities remain stable.

Policies evolve frequently.

---

# 3. Policy Definition

A Policy is a declarative business decision object.

Policies are:

- Versioned
- Configurable
- Runtime Evaluated
- Auditable
- Inheritable
- Publishable

Policies are not source code.

---

# 4. Policy Lifecycle

```
Draft

↓

Review

↓

Validated

↓

Published

↓

Runtime

↓

Archived
```

Only Published policies participate in runtime evaluation.

---

# 5. Policy Categories

The platform defines the following policy groups.

## Experience Policies

- Theme Policy
- Navigation Policy
- Visibility Policy
- Localization Policy

---

## Commerce Policies

- Pricing Policy
- Promotion Policy
- Checkout Policy
- Cart Policy
- Product Visibility Policy

---

## Fulfillment Policies

- Allocation Policy
- Inventory Policy
- Fulfillment Policy
- Retry Policy
- Replacement Policy

---

## Finance Policies

- Settlement Policy
- Commission Policy
- Billing Policy
- Refund Policy

---

## Security Policies

- Authentication Policy
- Authorization Policy
- MFA Policy
- Fraud Policy

---

## Operational Policies

- Scheduler Policy
- Monitoring Policy
- Alert Policy
- Notification Policy

---

# 6. Policy Metadata

Every Policy shares common metadata.

```yaml
id:
code:
name:
category:

status:

version:

owner:

priority:

effectiveFrom:

effectiveTo:

description:
```

---

# 7. Policy Structure

Every Policy consists of:

```yaml
policy:

  conditions:

  actions:

  fallback:

  priority:

  metadata:
```

---

# 8. Policy Evaluation

Policies are evaluated by the Policy Engine.

```
Runtime Context

↓

Applicable Policies

↓

Priority Resolution

↓

Condition Evaluation

↓

Decision

↓

Capability Execution
```

Policies never execute business logic directly.

---

# 9. Policy Context

Policies may evaluate:

- Organization
- Storefront
- User
- Role
- Locale
- Device
- Product
- Country
- Campaign
- Tracking
- Time
- Customer Segment

The Policy Engine receives a normalized runtime context.

---

# 10. Policy Composition

Multiple policies may apply simultaneously.

Example:

```
Checkout Policy

+

Promotion Policy

+

Fraud Policy

+

Payment Policy

↓

Final Decision
```

---

# 11. Policy Priority

Policies are evaluated in priority order.

```
Highest Priority

↓

Specific Policy

↓

Inherited Policy

↓

Default Policy
```

Lower-priority policies never override higher-priority decisions.

---

# 12. Policy Inheritance

Policies support inheritance.

```
Platform

↓

Organization

↓

Storefront

↓

Campaign

↓

Runtime Override
```

Only overridden rules are replaced.

---

# 13. Policy Fallback

If no policy matches,

```
Runtime

↓

Campaign

↓

Storefront

↓

Organization

↓

Platform Default
```

A valid decision must always be produced.

---

# 14. Policy Resolution

Policy resolution is deterministic.

Inputs:

- Runtime Context
- Applicable Policies
- Effective Dates
- Priority
- Version

Outputs:

- Final Decision
- Evaluation Trace

---

# 15. Policy Engine

The Policy Engine is responsible for:

- Loading policies
- Resolving inheritance
- Selecting applicable policies
- Evaluating conditions
- Producing decisions
- Recording audit trails

The Policy Engine does not own business capabilities.

---

# 16. Policy Examples

## Allocation Policy

Determines:

- preferred supplier routing
- inventory preference
- retry behavior
- replacement strategy

---

## Pricing Policy

Determines:

- markup
- discount
- currency rounding
- customer segment pricing

---

## Checkout Policy

Determines:

- guest checkout
- OTP requirements
- payment sequence
- order validation

---

## Visibility Policy

Determines:

- product visibility
- catalog visibility
- destination availability

---

# 17. Policy Audit

Every policy evaluation may generate an audit trace.

Example:

```text
Runtime Context

↓

Matched Policy

↓

Conditions

↓

Decision

↓

Capability
```

Audit logs improve troubleshooting and compliance.

---

# 18. Policy Versioning

Policies are immutable after publication.

Changes create new versions.

Rollback restores previous published versions.

---

# 19. Policy Integration

Policies never communicate directly with infrastructure.

```
Policy Engine

↓

Capability

↓

Application Service

↓

Infrastructure
```

Policies remain implementation-independent.

---

# 20. AI Implementation Guidelines

AI agents shall:

- Never hardcode business decisions.
- Represent configurable decisions as Policies.
- Keep Policy evaluation separate from business execution.
- Support inheritance and fallback.
- Version every Policy.
- Produce deterministic evaluation.
- Never bypass the Policy Engine.

---

# 21. Architectural Principles

### POL-001

Policies define business decisions.

---

### POL-002

Capabilities define business responsibilities.

---

### POL-003

Policies are runtime evaluated.

---

### POL-004

Policies are declarative.

---

### POL-005

Policies support inheritance.

---

### POL-006

Policies support fallback.

---

### POL-007

Policies are immutable after publication.

---

### POL-008

Policy evaluation is deterministic.

---

### POL-009

Policy evaluation is auditable.

---

### POL-010

Infrastructure never evaluates business policies.

---

# 22. Relationship with Other Specifications

| Specification | Responsibility |
|---------------|----------------|
| CAP | Business Capabilities |
| UXF | Experience Runtime |
| ECS | Experience Configuration |
| PCS | Configuration Standard |
| POL | Business Decisions |
| ABP | Runtime Architecture |

The Policy Framework governs decision making across all platform capabilities.

---

# 23. Future Evolution

The Policy Framework is designed to evolve into a full Policy Decision Point (PDP) architecture.

Future extensions may include:

- Policy DSL
- Visual Policy Editor
- Rule Composer
- Decision Graph
- Simulation Mode
- Impact Analysis
- Explainable Decisions
- AI-assisted Policy Authoring
- External Policy APIs

These capabilities extend the framework without changing existing business capabilities.

---

# 24. References

This document should be read together with:

- CAP-00 — Platform Capability Registry
- UXF-00 ~ UXF-05
- ECS-00 — Experience Configuration Schema
- PCS-00 — Platform Configuration Schema
- BRD
- ABP
- AFM
- YADF
- DIP


---

# Source: UXF-00

- Path: `docs/UXF/UXF-00.md`
- Set: `UXF`
- Version: `1.0`
- Status: `Draft`

# UXF-00 — User Experience Foundation Overview

---

# 1. Purpose

This document defines the **User Experience Foundation (UXF)** for the YSim Platform.

Unlike traditional UI guideline documents, UXF defines the architectural principles that govern how every Portal, Storefront and Customer Experience is designed, rendered and operated.

UXF serves as the authoritative reference for:

- Business Architecture
- Frontend Architecture
- White-label Architecture
- Storefront Runtime
- Portal Design
- Theme Engine
- Localization Engine
- Experience Runtime
- AI (YSF / Codex) generated frontend implementations

UXF is considered the **Source of Truth** for every frontend application within the YSim Platform.

---

# 2. Vision

YSim is **NOT** a website.

YSim is **NOT** an online shop.

YSim is an **Experience Platform** capable of rendering different commercial experiences according to runtime business context.

The same URL may produce completely different user experiences depending on:

- Organization
- Storefront
- Domain
- Campaign
- Tracking ID
- Customer Segment
- Device
- Localization
- Currency
- Runtime Policies

Therefore,

> Every rendered page is the result of runtime context resolution rather than static page implementation.

---

# 3. Experience First Principle

Traditional commerce systems generally follow:

```
Website

↓

Page

↓

Product

↓

Checkout
```

YSim follows a different philosophy.

```
Request

↓

Runtime Context Resolution

↓

Experience Resolution

↓

Business Resolution

↓

Commercial Resolution

↓

Localization Resolution

↓

Storefront Runtime

↓

Rendered Experience
```

The UI is therefore an output of the platform, not a hardcoded implementation.

---

# 4. User Experience Architecture

Every customer interaction is rendered by resolving multiple independent contexts.

```
Incoming Request

        │

        ▼

Platform Context

        │

        ▼

Organization Context

        │

        ▼

Storefront Context

        │

        ▼

Campaign Context

        │

        ▼

Tracking Context

        │

        ▼

Localization Context

        │

        ▼

Business Context

        │

        ▼

Commerce Experience

        │

        ▼

Rendered UI
```

No individual module independently determines the final interface.

---

# 5. Runtime Experience Resolution

Experience Resolution consists of several independent engines.

```
Experience Runtime

├── Theme Resolver

├── Template Resolver

├── Asset Resolver

├── Navigation Resolver

├── Layout Resolver

├── Localization Resolver

├── Business Binding Resolver

├── Payment Resolver

├── Catalog Resolver

├── Promotion Resolver

├── Checkout Resolver

├── Support Resolver

└── Runtime Policy Resolver
```

Each resolver contributes part of the final rendered experience.

---

# 6. Storefront Definition

A Storefront is **NOT** a website template.

A Storefront is a complete commercial experience configuration.

A Storefront contains:

- Experience Configuration
- Business Configuration
- Commercial Configuration
- Operational Configuration
- Runtime Policies

A Storefront is therefore an independent business entity.

---

# 7. Business Binding Principle

Every Storefront must be connected to business capabilities.

Examples include:

- Product Catalog
- Pricing Policy
- Promotion Policy
- Payment Profile
- Checkout Flow
- Fulfillment Policy
- Customer Policy
- Support Profile
- Legal Profile

Without valid business bindings a Storefront **cannot be published**.

---

# 8. Supplier Isolation Principle

Supplier systems are internal infrastructure.

Storefronts never communicate with suppliers directly.

The correct architecture is:

```
Storefront

↓

Order

↓

Allocation Engine

↓

Supplier Gateway

↓

Supplier
```

Storefronts only understand YSim Products.

Supplier Products are hidden behind the Allocation Engine.

This architecture guarantees:

- supplier independence
- routing flexibility
- cost optimization
- failover capability
- future supplier replacement

without changing storefront implementations.

---

# 9. Allocation Principle

Allocation is a core business capability of YSim.

Allocation is responsible for:

- Supplier Routing
- Inventory Reservation
- Inventory Release
- Fulfillment
- Retry
- Replacement
- Cost Optimization
- Availability Decision

Allocation is the only business component allowed to determine which supplier provides an eSIM.

---

# 10. Product Principle

Storefronts expose only YSim Products.

```
YSim Product

↓

Allocation Rule

↓

Supplier Mapping
```

Supplier products are never exposed to:

- Storefront
- Portal
- Customer
- Agency
- Reseller

Supplier Mapping remains internal configuration.

---

# 11. Experience Inheritance

Every experience supports hierarchical inheritance.

```
Platform

↓

Organization

↓

Storefront

↓

Campaign

↓

Tracking

↓

Runtime Override
```

Each level only overrides the required configuration.

All unspecified properties inherit from their parent.

---

# 12. Fallback Experience

Every runtime configuration must support fallback.

Fallback applies to every configurable aspect.

Examples:

- Theme
- Catalog
- Payment
- Promotion
- Checkout
- Support
- Localization
- Assets
- Navigation

If a configuration cannot be resolved, the runtime automatically falls back to the nearest valid parent configuration.

No runtime request should fail solely because a child configuration is incomplete.

---

# 13. Localization Principle

Localization extends beyond language translation.

Localization defines the complete customer experience for a specific market.

Localization may affect:

- Language
- Currency
- Date Format
- Number Format
- Timezone
- Payment Methods
- Promotions
- Hero Banner
- Product Recommendations
- Support Information
- FAQ
- Legal Documents
- Checkout Flow
- Email Templates
- SMS Templates
- Notifications

Localization therefore represents a localized commercial experience.

---

# 14. Tracking Context

Tracking identifiers are part of runtime experience resolution.

Tracking may influence:

- Landing Page
- Campaign
- Promotion
- Banner
- CTA
- Product Visibility
- Pricing
- Commission
- Affiliate Attribution
- Support Channel
- Analytics

Tracking is not limited to reporting.

Tracking participates in experience generation.

---

# 15. Page Composition

Pages are dynamically composed.

A page consists of Sections.

Each Section consists of Components.

```
Page

↓

Sections

↓

Components

↓

Business Data

↓

Rendered Experience
```

Sections may be:

- enabled
- disabled
- reordered
- replaced

without modifying application code.

---

# 16. Design System Principle

All portals share a unified Design System.

Applications include:

- Platform Portal
- Administration Portal
- Agency Portal
- Partner Portal
- Customer Portal
- White-label Storefront

All applications must reuse the same component library.

UI duplication is prohibited.

---

# 17. White-label Principle

Every tenant may own multiple storefronts.

Each storefront may have:

- Domain
- Branding
- Theme
- Assets
- Localization
- Catalog
- Payment Profile
- Checkout Policy
- Support Profile

White-label customization must never require source code modification.

---

# 18. Published Experience Snapshot

Runtime rendering must use immutable published configurations.

Lifecycle:

```
Draft

↓

Preview

↓

Validation

↓

Publish

↓

Published Snapshot

↓

Runtime Rendering
```

The runtime never renders directly from editable configurations.

---

# 19. Experience Runtime Goals

The Experience Runtime must provide:

- Dynamic Rendering
- White-label Support
- Multi-tenant Isolation
- Localization
- Runtime Resolution
- Experience Inheritance
- Safe Fallback
- Versioning
- Preview
- Publish
- Rollback
- Auditability

---

# 20. Architectural Principles

The following principles are mandatory.

### UXF-001

Experience is resolved at runtime.

---

### UXF-002

Storefronts represent commercial experiences rather than websites.

---

### UXF-003

Storefronts consume YSim Products only.

---

### UXF-004

Supplier systems are internal infrastructure.

---

### UXF-005

Allocation is the only capability allowed to select suppliers.

---

### UXF-006

Every runtime configuration supports inheritance.

---

### UXF-007

Every runtime configuration supports fallback.

---

### UXF-008

Localization defines customer experience, not only language.

---

### UXF-009

Tracking participates in experience generation.

---

### UXF-010

Every published storefront must pass business binding validation.

---

### UXF-011

Runtime rendering must use published snapshots.

---

### UXF-012

Design System components are shared across every portal.

---

# 21. References

This document should be read together with:

- BRD — Business Requirements
- AFM — AI Factory Model
- YADF — YSim Architecture Definition Framework
- ABP — Architecture Blueprint
- DIP — Development & Implementation Principles
- UXF-01 — Channels, Personas & Navigation
- UXF-02 — Design System, Theme & Experience Inheritance
- UXF-03 — Storefront Template & Page Composition
- UXF-04 — White-label, Localization & Runtime Context Resolution
- UXF-05 — Storefront Runtime Architecture & Business Binding


---

# Source: UXF-02

- Path: `docs/UXF/UXF-02.md`
- Set: `UXF`
- Version: `1.0`
- Status: `Draft`

# UXF-02 — Design System, Theme & Experience Inheritance

---

# 1. Purpose

This document defines the Design Runtime Architecture used by the YSim Platform.

Unlike traditional frontend systems where themes only control visual appearance, YSim themes represent configurable experience layers that participate in runtime rendering.

This document specifies:

- Design System
- Design Tokens
- Theme Architecture
- Experience Profiles
- Theme Inheritance
- Fallback Strategy
- Asset Resolution
- Component Registry
- UI Composition Rules

---

# 2. Design Philosophy

The YSim Platform follows a **Single Design System** strategy.

All applications share the same visual language.

Applications include:

- Platform Portal
- Administration Portal
- Organization Portal
- Agency Portal
- Customer Portal
- White-label Storefront
- Embedded Commerce

No application may create an isolated component library.

---

# 3. Design Runtime

Rendering follows the Design Runtime pipeline.

```
Experience Context

↓

Theme Resolver

↓

Design Token Resolver

↓

Asset Resolver

↓

Component Registry

↓

Layout Resolver

↓

Rendered UI
```

Visual appearance is resolved dynamically.

---

# 4. Design System Layers

```
Design Tokens

↓

Theme

↓

Experience Profile

↓

Layout

↓

Components

↓

Pages

↓

Applications
```

Each layer depends only on its parent.

---

# 5. Design Tokens

The platform defines immutable Design Tokens.

Token categories include:

## Color

- Primary
- Secondary
- Accent
- Success
- Warning
- Error
- Background
- Surface
- Border
- Text
- Muted

---

## Typography

- Heading Font
- Body Font
- Code Font
- Font Scale
- Line Height
- Letter Spacing

---

## Layout

- Grid
- Container Width
- Radius
- Elevation
- Shadow
- Spacing
- Breakpoints

---

## Motion

- Transition
- Animation
- Hover
- Focus
- Loading
- Skeleton

---

## Icons

- Icon Set
- Size
- Weight
- Filled
- Outlined

---

# 6. Theme

A Theme is a configuration object.

A Theme is **NOT** a stylesheet.

Example:

```
Theme

├── Color Tokens

├── Typography

├── Icons

├── Illustration Style

├── Card Style

├── Navigation Style

├── Button Style

├── Input Style

├── Animation Profile

└── Assets
```

---

# 7. Theme Presets

The platform provides several built-in presets.

Recommended presets:

- YSim Green
- Ocean Blue
- Sunset Orange
- Ruby Red
- Violet
- Minimal White

Organizations may derive custom themes from these presets.

---

# 8. Experience Profile

A Theme only defines appearance.

An Experience Profile defines behavior.

Example:

```
Experience Profile

├── Theme

├── Navigation Profile

├── Hero Style

├── CTA Style

├── Content Density

├── Component Visibility

├── Interaction Style

├── Asset Profile

└── Motion Profile
```

Different Storefronts may share the same Theme while using different Experience Profiles.

---

# 9. Theme Inheritance

Themes support inheritance.

```
Platform Theme

↓

Organization Theme

↓

Storefront Theme

↓

Campaign Theme

↓

Runtime Override
```

Each level overrides only required properties.

---

# 10. Experience Inheritance

Experience inheritance extends beyond themes.

Inherited objects include:

- Theme
- Assets
- Navigation
- Typography
- Component Visibility
- Hero
- CTA
- Empty States
- Loading Style
- Icons
- Motion

Experience inheritance is resolved independently for every request.

---

# 11. Fallback Strategy

If a configuration cannot be resolved, runtime falls back to the nearest valid parent.

```
Runtime Override

↓

Campaign

↓

Storefront

↓

Organization

↓

Platform
```

Fallback applies to every configurable property.

No incomplete configuration may break rendering.

---

# 12. Asset Management

Assets are runtime resources.

Supported asset categories:

- Logo
- Favicon
- Hero Image
- Banner
- Background
- Illustration
- Icons
- Email Branding
- Social Preview
- Empty State Graphics

Assets are referenced by identifier rather than embedded.

---

# 13. Asset Resolution

Runtime asset resolution:

```
Platform Assets

↓

Organization Assets

↓

Storefront Assets

↓

Campaign Assets

↓

Runtime Assets
```

Asset resolution follows the same inheritance model as themes.

---

# 14. Component Registry

Every UI component belongs to a shared registry.

```
packages/ui

├── Layout

├── Navigation

├── Form

├── Table

├── Chart

├── Dialog

├── Notification

├── Card

├── Commerce

├── Storefront

└── Shared
```

Components are reusable across all channels.

---

# 15. Component Composition

Pages are assembled using components.

```
Page

↓

Sections

↓

Components

↓

Business Data

↓

Rendering
```

Components remain presentation-only.

Business logic belongs to application services.

---

# 16. Component Visibility

Visibility is configurable.

Example:

```
Hero

Enabled

↓

Storefront A

Disabled

↓

Storefront B
```

Component visibility may depend on:

- Storefront
- Campaign
- Locale
- Feature Flag
- Device

---

# 17. Design Tokens vs Business Configuration

The Design System controls presentation only.

Business behavior is configured separately.

Example:

```
Theme

↓

Primary Button Color
```

does not determine

```
Checkout Policy
```

Business configuration remains independent.

---

# 18. Design Accessibility

Every component must support:

- Keyboard Navigation
- Screen Readers
- Responsive Layout
- High Contrast
- Focus Indicators
- Touch Interaction

Accessibility cannot be disabled by Themes.

---

# 19. Responsive Design

Responsive behavior follows Design Tokens.

Supported breakpoints:

- Mobile
- Tablet
- Laptop
- Desktop
- Wide Display

Applications remain functionally identical across devices.

---

# 20. Design Principles

### UXF-201

One platform uses one Design System.

---

### UXF-202

Themes are configuration objects.

---

### UXF-203

Experience Profiles extend Themes.

---

### UXF-204

Themes support inheritance.

---

### UXF-205

Every configurable property supports fallback.

---

### UXF-206

Assets participate in runtime resolution.

---

### UXF-207

Component libraries are shared across all applications.

---

### UXF-208

Business behavior is independent from presentation.

---

### UXF-209

Accessibility is mandatory.

---

### UXF-210

Responsive behavior is defined by Design Tokens.

---

# 21. AI Implementation Guidelines

When generating frontend code, AI agents shall:

- Never hardcode colors.
- Never hardcode fonts.
- Never hardcode logos.
- Never hardcode branding assets.
- Never duplicate UI components.
- Always consume Design Tokens.
- Always resolve Themes through the Theme Engine.
- Always support Experience Inheritance.
- Always support runtime fallback.
- Separate presentation from business logic.

---

# 22. References

This document should be read together with:

- UXF-00 — User Experience Foundation Overview
- UXF-01 — Experience Channels, Personas & Navigation
- UXF-03 — Storefront Template & Page Composition
- UXF-04 — White-label, Localization & Runtime Context Resolution
- UXF-05 — Storefront Runtime Architecture & Business Binding

- BRD
- ABP
- AFM
- YADF
- DIP


---

# Source: UXF-05

- Path: `docs/UXF/UXF-05.md`
- Set: `UXF`
- Version: `1.0`
- Status: `Draft`

# UXF-05 — Experience Runtime & Commerce Runtime Integration

---

# 1. Purpose

This document defines how the Experience Runtime integrates with the Commerce Runtime.

Unlike traditional commerce systems where the frontend owns business behavior, the YSim Platform separates presentation, business capabilities and infrastructure.

The Experience Runtime is responsible for rendering customer experiences.

The Commerce Runtime is responsible for providing business capabilities.

The two runtimes collaborate through Business Bindings.

---

# 2. Core Architecture

The YSim Platform consists of three independent runtime layers.

```
Experience Runtime

↓

Commerce Runtime

↓

Infrastructure Runtime
```

Each runtime owns different responsibilities.

---

# 3. Experience Runtime

The Experience Runtime owns:

- Theme
- Branding
- Layout
- Navigation
- Sections
- Components
- Assets
- Localization
- UX Inheritance
- Runtime Rendering

The Experience Runtime never performs business decisions.

---

# 4. Commerce Runtime

The Commerce Runtime owns:

- Catalog
- Product
- Pricing
- Promotion
- Payment
- Checkout
- Order
- Customer
- Fulfillment Policy
- Allocation
- Settlement
- Reporting

The Commerce Runtime never renders UI.

---

# 5. Infrastructure Runtime

Infrastructure owns:

- Supplier Gateway
- Payment Gateway
- Notification Gateway
- Storage
- Queue
- Cache
- Search
- Monitoring

Infrastructure never communicates directly with Storefront UI.

---

# 6. Runtime Integration

```
Request

↓

Experience Runtime

↓

Business Binding

↓

Commerce Runtime

↓

Application Services

↓

Infrastructure Runtime

↓

Response

↓

Experience Runtime

↓

Rendering
```

---

# 7. Storefront Responsibilities

Storefronts own only:

- Experience
- Navigation
- Layout
- Presentation
- Business Bindings

Storefronts never own:

- Products
- Pricing
- Supplier
- Inventory
- Allocation
- Fulfillment

---

# 8. Business Binding

Business Bindings connect Experience with Commerce.

Example:

```
Featured Products

↓

Catalog

↓

Pricing Profile

↓

Promotion Profile

↓

Visibility Policy

↓

Commerce Runtime
```

The UI never queries business objects directly.

---

# 9. Storefront Profile

A Storefront Profile consists of:

```
Storefront

├── Experience Profile
├── Business Profile
├── Commercial Profile
├── Runtime Policies
├── Navigation
├── Assets
├── Localization
├── Published Snapshot
```

---

# 10. Section Business Binding

Every Section supports Business Binding.

Example:

```
Featured Products

├── Catalog Binding

├── Product Selection Rule

├── Pricing Profile

├── Promotion Profile

├── Sorting Policy

├── Visibility Policy

├── Localization Policy

├── Empty State Policy
```

Another example:

```
Destination Selector

↓

Country Catalog

↓

Availability Policy

↓

Rendering
```

Sections become reusable commercial building blocks.

---

# 11. Widget Binding

Widgets never access databases.

Widgets never call suppliers.

Widgets call Business Capabilities.

```
Widget

↓

Capability

↓

Application Service

↓

Commerce Runtime
```

---

# 12. Commerce Capability Graph

The Experience Runtime consumes platform capabilities.

```
Catalog

Pricing

Promotion

Checkout

Payment

Customer

Support

Order

Fulfillment

Allocation
```

Capabilities remain independent.

---

# 13. Allocation Principle

Allocation is an internal business capability.

Storefronts never know suppliers.

Correct architecture:

```
Storefront

↓

Order

↓

Allocation

↓

Supplier Gateway

↓

Supplier
```

Supplier systems are infrastructure resources.

---

# 14. Product Principle

Storefronts consume only YSim Products.

```
YSim Product

↓

Allocation Rule

↓

Supplier Mapping
```

Supplier mappings remain internal.

---

# 15. Supplier Isolation

Supplier objects are prohibited from appearing inside:

- Storefront
- Components
- Widgets
- Pages
- Catalog
- Checkout

Supplier references may only appear inside:

- Allocation
- Fulfillment
- Inventory
- Supplier Gateway

---

# 16. Runtime Resolution

Rendering requires two parallel pipelines.

```
Experience Runtime

↓

Theme

↓

Layout

↓

Sections

↓

Widgets

──────────────

Commerce Runtime

↓

Catalog

↓

Pricing

↓

Promotion

↓

Payment

↓

Checkout

↓

Support

──────────────

↓

Business Binding

↓

Rendered Experience
```

---

# 17. Runtime Snapshot

Runtime renders immutable snapshots.

```
Published Storefront Snapshot

↓

Experience Snapshot

+

Business Snapshot

↓

Rendering
```

Editable configuration never participates directly.

---

# 18. Business Binding Validation

Before publishing, validation verifies:

✓ Catalog

✓ Pricing

✓ Payment

✓ Checkout

✓ Support

✓ Localization

✓ Runtime Policies

✓ Navigation

✓ Theme

Only valid storefronts may be published.

---

# 19. Runtime Failure Fallback

If runtime cannot resolve a binding:

```
Runtime

↓

Storefront

↓

Organization

↓

Platform
```

Fallback applies independently.

Rendering should continue whenever possible.

---

# 20. Business Configuration Inheritance

Business Configuration supports inheritance.

```
Platform

↓

Organization

↓

Storefront

↓

Campaign

↓

Tracking

↓

Runtime
```

Inherited objects include:

- Catalog
- Payment
- Promotion
- Support
- Checkout
- Pricing
- Navigation
- Assets

---

# 21. Experience + Commerce Synchronization

Experience Runtime and Commerce Runtime remain synchronized through Business Bindings.

Neither runtime directly depends on the implementation details of the other.

---

# 22. Publish Lifecycle

```
Draft

↓

Validate

↓

Preview

↓

Publish

↓

Immutable Snapshot

↓

Runtime Rendering
```

---

# 23. AI Implementation Guidelines

AI agents shall:

Never hardcode business logic inside components.

Never query suppliers directly.

Never bind UI to infrastructure.

Always consume Business Capabilities.

Always separate:

- Experience
- Commerce
- Infrastructure

Always support inheritance.

Always support fallback.

Always render Published Snapshots.

---

# 24. Architectural Principles

### UXF-501

Experience Runtime owns presentation.

---

### UXF-502

Commerce Runtime owns business capabilities.

---

### UXF-503

Infrastructure Runtime owns integrations.

---

### UXF-504

Business Binding connects Experience with Commerce.

---

### UXF-505

Storefronts never know suppliers.

---

### UXF-506

Allocation is the only capability allowed to select suppliers.

---

### UXF-507

Business Configuration supports inheritance.

---

### UXF-508

Business Configuration supports fallback.

---

### UXF-509

Published snapshots are immutable.

---

### UXF-510

Experience Runtime and Commerce Runtime remain independent.

---

# 25. Future Extensions

The architecture supports future extensions without changing storefront implementations.

Examples include:

- Additional suppliers
- New payment gateways
- Dynamic pricing engines
- Recommendation engines
- AI-assisted personalization
- Headless commerce APIs
- Native mobile storefronts
- Partner embedded commerce
- Marketplace channels

These extensions are introduced by extending Business Capabilities and Runtime Configuration rather than modifying Storefront implementations.

---

# 26. References

This document should be read together with:

- UXF-00 — User Experience Foundation Overview
- UXF-01 — Experience Channels, Personas & Navigation
- UXF-02 — Design System, Theme & Experience Inheritance
- UXF-03 — Storefront Template & Page Composition
- UXF-04 — White-label, Localization & Runtime Context Resolution

- BRD
- ABP
- AFM
- YADF
- DIP


---

# Source: YADF-00

- Path: `docs/YADF/YADF-00.md`
- Set: `YADF`
- Version: `2.0`
- Status: `FROZEN`

# YSim AI Development Framework (YADF)

---

# 1. Purpose

YSim AI Development Framework (YADF) là framework chuẩn hóa toàn bộ quy trình phát triển phần mềm của nền tảng YSim với sự hỗ trợ của AI Coding Assistant.

YADF định nghĩa:

- Development Governance
- Architecture Governance
- Sprint Governance
- AI Collaboration
- Verification
- Operational Readiness

YADF là nền tảng để tất cả các dự án trong hệ sinh thái YSim được phát triển theo cùng một phương pháp.

---

# 2. Framework Philosophy

YADF áp dụng nguyên tắc:

> **Business-Driven, Blueprint-Oriented, Contract-Driven, Full-stack AI Development**

Business quyết định yêu cầu.

Architecture quyết định cấu trúc.

Sprint Contract quyết định phạm vi triển khai.

AI chịu trách nhiệm hiện thực hóa (Implementation).

AI không phải là Source of Truth.

---

# 3. Framework Layers

```text
Business Layer
        │
        ▼
Architecture Layer
        │
        ▼
Capability Layer
        │
        ▼
Implementation Layer
        │
        ▼
Verification Layer
        │
        ▼
Operation Layer
```

Mỗi Layer có trách nhiệm rõ ràng và độc lập.


---

# 3A. Commerce & Capability Meta Model

Version 2.1 bổ sung Meta Model chuẩn cho AI Software Factory.

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
Commerce Experience
```

Mọi Capability có giao diện người dùng được triển khai theo mô hình Full-stack Capability Delivery:

```text
Capability
        │
        ├── Backend
        ├── API
        ├── Frontend
        ├── Seed Data
        ├── Demonstration
        └── Verification
```

YADF coi Capability là đơn vị Delivery nhỏ nhất của AI Factory.

---

# 4. Development Lifecycle

```text
Business Requirements
        │
        ▼
Business Registry
        │
        ▼
Architecture Baseline
        │
        ▼
Sprint Contract
        │
        ▼
Repository Discovery
        │
        ▼
Backend + Frontend Implementation
        │
        ▼
Capability Demonstration
        │
        ▼
Verification
        │
        ▼
Acceptance
        │
        ▼
Deployment
        │
        ▼
Operations
```

---

# 5. Core Principles

YADF tuân thủ các nguyên tắc sau:

1. Business là Source of Truth.
2. Registry là Architecture Source of Truth.
3. Sprint Contract là Sprint Source of Truth.
4. AI chỉ là Implementation Agent.
5. Mọi thay đổi phải truy vết được.
6. Mọi Sprint phải độc lập và kiểm thử được.
7. Không thay đổi Architecture trong Sprint nếu chưa được phê duyệt.
8. Mọi thay đổi phải có bằng chứng (Implementation Evidence).
9. Capability có giao diện phải được Demonstration trước khi nghiệm thu.
10. Backend và Frontend được phát triển trong cùng một Sprint.

---

# 6. Sprint Model

Sprint là đơn vị triển khai theo **Technical Capability**.

Mỗi Sprint:

- có Domain Ownership rõ ràng;
- có Sprint Contract riêng;
- có phạm vi nhỏ, độc lập;
- có thể build, test và nghiệm thu độc lập.

Sprint không phải là Business Domain và cũng không phải là Vertical Slice.

---

# 7. Sprint Contract

Sprint Contract là tài liệu bất biến trong quá trình triển khai.

Một Sprint chỉ được bắt đầu khi:

- Business Object đã được xác định.
- Business Capability đã được xác định.
- Business Policy đã được xác định.
- Business Event đã được xác định.
- Business Snapshot đã được xác định.
- API Contract đã được xác định.

Nếu phát hiện vấn đề, AI phải tạo **Architecture Change Proposal (ACP)** thay vì tự thay đổi Sprint Contract.

---

# 8. Repository Discovery

Repository Discovery là bước bắt buộc trước khi triển khai.

AI phải đánh giá:

- Existing Modules
- Existing APIs
- Existing Database Schema
- Existing Migrations
- Existing Events
- Existing Snapshots
- Existing Tests
- Existing Technical Debt
- Gap Analysis

Repository Discovery là cơ sở để lập kế hoạch triển khai Sprint.

---

# 9. Domain Ownership

Mỗi Sprint chỉ được phép thay đổi:

- Domain thuộc Ownership của Sprint.
- Shared Components được Sprint Contract cho phép.

Không được thay đổi Domain khác nếu chưa được phê duyệt.

---

# 10. Dependency Resolution

YADF định nghĩa ba mức xử lý Dependency:

## Level 1 — Available Dependency

Dependency đã tồn tại.

→ Triển khai.

## Level 2 — Mockable Dependency

Dependency chưa tồn tại nhưng được phép Mock.

→ AI tạo Mock/Stub/Fake theo Sprint Contract.

## Level 3 — Architecture Dependency

Dependency thuộc Architecture Contract.

Ví dụ:

- Business Object
- Capability
- Policy
- Event
- Snapshot
- Shared API
- Shared Database Contract

AI không được tự tạo.

Phải sinh:

- Dependency Report
- Architecture Change Proposal (ACP)

---

# 11. Safe Refactoring

AI được phép Refactor khi:

- không thay đổi Business Behavior;
- không thay đổi Public Contract;
- không thay đổi Business Flow;
- không thay đổi Domain Ownership.

Nếu Refactor ảnh hưởng Contract hoặc Architecture:

→ phải tạo ACP.

---

# 12. Verification Model

Definition of Done gồm ba nhóm.

## Technical

- Build
- Migration
- Static Analysis
- Unit Test
- Contract Test

## Business

- Capability
- Policy
- Event
- Snapshot
- Business Scenario

## Operational

- Logging
- Monitoring
- Metrics
- Alert
- Runbook (nếu áp dụng)

---

# 13. Change Control

AI không được thay đổi:

- BRD
- Business Registry
- Architecture Baseline
- Sprint Contract

Mọi thay đổi phải thông qua:

- Architecture Change Proposal (ACP)
- Architecture Review
- Approval

---

# 14. AI Collaboration Principles

AI phải:

- tuân thủ Sprint Contract;
- tuân thủ Registry;
- tuân thủ Engineering Standards;
- sinh báo cáo khi phát hiện bất thường;
- đề xuất thay đổi thay vì tự thay đổi.

AI không được tự định nghĩa Business hoặc Architecture.

---

# 15. Sprint Completion

Một Sprint chỉ được hoàn thành khi đồng thời đạt:

## Technical Done

- Build PASS
- Migration PASS
- Static Analysis PASS
- Test PASS

## Business Done

- Capability hoàn chỉnh
- Policy đúng
- Event đúng
- Snapshot đúng
- Acceptance Scenario PASS

## Operational Done

- Logging
- Monitoring
- Alert
- Metrics
- Feature Flag/Kill Switch (nếu yêu cầu)

Ngoài Source Code, Sprint phải tạo đầy đủ:

- Test
- Seed Data
- Documentation
- Validation Report
- Implementation Evidence

---

# 16. Framework Artifacts

YADF quản lý các nhóm tài liệu sau:

| Artifact | Purpose |
|----------|---------|
| Business Requirements | Định nghĩa yêu cầu nghiệp vụ |
| Enterprise Registries | Source of Truth cho kiến trúc nghiệp vụ |
| Architecture Baseline Pack | Chuẩn kiến trúc nền tảng |
| Domain Implementation Pack | Hướng dẫn triển khai theo Domain |
| Engineering Standards Pack | Quy chuẩn kỹ thuật |
| Sprint Governance Pack | Quản trị Sprint |
| Verification & Acceptance Pack | Kiểm thử và nghiệm thu |
| Operations Readiness Pack | Vận hành và triển khai |

---

# 17. Framework Principles

1. Business drives Architecture.
2. Architecture governs Implementation.
3. Sprint Contract governs Execution.
4. AI implements, never defines Architecture.
5. Every Sprint must be traceable.
6. Every Sprint must be verifiable.
7. Every Sprint must produce Implementation Evidence.
8. Every Release must be operationally ready.
9. Every Architecture change must be approved.
10. One Source of Truth for every architectural concern.

---

# Document Status

**Status: FROZEN**

YADF là framework chuẩn cho toàn bộ hoạt động phát triển phần mềm của nền tảng YSim.

Mọi dự án, Sprint, AI Coding Assistant và quy trình triển khai phải tuân thủ YADF nhằm đảm bảo tính nhất quán, khả năng truy vết và chất lượng của toàn bộ hệ sinh thái YSim.

---


---

# Source: AAP-01

- Path: `docs/AAP/AAP-01.md`
- Set: `AAP`
- Version: `2.1`
- Status: `FROZEN`

# Repository Discovery Model

## AAP-01

---

# 1. Purpose

Repository Discovery Model định nghĩa mô hình khám phá Repository trước khi AI thực hiện bất kỳ Sprint nào.

Repository Discovery là bước bắt buộc.

AI không được phép sinh mã nguồn nếu chưa hoàn thành Repository Discovery.

Repository Discovery giúp AI:

- hiểu kiến trúc hiện tại;
- xác định phạm vi Sprint;
- tránh tạo mã nguồn trùng lặp;
- tránh phá vỡ Architecture Baseline.

---

# 2. Principles

Repository Discovery tuân thủ các nguyên tắc:

- Repository First
- Read Before Write
- Architecture First
- Contract First
- Incremental Discovery
- Evidence Driven
- Full-stack Discovery
- Experience-aware Discovery

Repository Discovery không thay đổi Repository.

Repository Discovery chỉ thu thập tri thức.

---

# 3. Discovery Scope

AI phải khám phá tối thiểu các nhóm sau.

| Area | Description |
|--------|-------------|
| Applications | apps/ |
| Modules | packages/ |
| Shared Libraries | packages/shared |
| Database | schema, migration |
| APIs | REST, GraphQL, Internal |
| Events | Published & Subscribed |
| Snapshots | Business Snapshots |
| Configuration | Runtime Configuration |
| Integration | Gateway, Connector, Adapter |
| Tests | Existing Test Assets |
| Documentation | BRD, ABP, DIP, ESP... |
| Frontend | Portal, Storefront, Components, Routes |
| Design System | Tokens, Themes, Components |

---

# 4. Discovery Objectives

Repository Discovery nhằm trả lời:

- Có Module nào đã tồn tại?
- Capability này đã được triển khai chưa?
- Có API tương tự không?
- Có Event tương tự không?
- Có Snapshot tương tự không?
- Có Migration liên quan không?
- Có Test hiện có không?
- Có Frontend tương ứng không?
- Có Capability Demonstration hiện có không?
- Có Technical Debt nào ảnh hưởng Sprint không?

---

# 5. Discovery Layers

Repository được khám phá theo các tầng.

```text
Documentation

↓

Architecture

↓

Modules

↓

Contracts

↓

Implementation

↓

Frontend Experience

↓

Tests

↓

Infrastructure
```

Không khám phá ngẫu nhiên.

---

# 6. Discovery Order

AI phải thực hiện Discovery theo trình tự.

```text
Sprint Contract

↓

Documentation

↓

Registry

↓

ABP

↓

Repository Structure

↓

Module Discovery

↓

Dependency Discovery

↓

Contract Discovery

↓

Implementation Discovery

↓

Frontend Discovery

↓

Capability Demonstration Discovery

↓

Test Discovery

↓

Gap Analysis
```

---

# 7. Module Discovery

AI phải xác định:

- Module Name
- Module Owner
- Domain
- Public API
- Published Event
- Consumed Event
- Dependencies
- Status

Không tạo Module nếu Module đã tồn tại.

---

# 8. Contract Discovery

AI phải khám phá:

- API Contract
- Event Contract
- Snapshot Contract
- Configuration Contract
- Permission Contract

Contract luôn được ưu tiên hơn Source Code.

---

# 9. Dependency Discovery

AI phải xây dựng Dependency Graph.

Bao gồm:

- Module Dependency
- Event Dependency
- API Dependency
- Configuration Dependency
- Integration Dependency

Circular Dependency phải được báo cáo.

---

# 10. Implementation Discovery

AI xác định:

- Existing Service
- Repository
- Worker
- Scheduler
- Queue
- Connector
- Adapter

Không sinh lại thành phần đã tồn tại.

---

# 11. Database Discovery

AI khám phá:

- Schema
- Entity
- Migration
- Seed
- Index
- Constraint

Migration cũ không được sửa.

---

# 12. Test Discovery

AI xác định:

- Unit Test
- Contract Test
- Integration Test
- Scenario Test
- Performance Test

Nếu thiếu Test phải ghi nhận.

---

# 12A. Frontend Discovery

AI phải khám phá đầy đủ Frontend trước khi lập kế hoạch triển khai.

Bao gồm:

- Portal hiện có
- Storefront hiện có
- Routes
- Pages
- Components
- Design Tokens
- Theme
- State Management
- API Client
- Capability Demonstration Surface

Repository Discovery chỉ hoàn thành khi AI hiểu đầy đủ cả Backend và Frontend của Capability.

---

# 13. Gap Analysis

Sau Discovery AI phải sinh Gap Analysis.

Bao gồm:

- Existing Capability
- Missing Capability
- Reusable Component
- Missing Dependency
- Architecture Risk
- Suggested Scope

Gap Analysis không được tự thay đổi Sprint.

---

# 14. Discovery Output

Repository Discovery sinh các Artifact.

- Discovery Report
- Module Inventory
- Dependency Graph
- Contract Inventory
- Gap Analysis
- Frontend Inventory
- Capability Demonstration Inventory
- Architecture Risk Report

Đây là đầu vào cho Sprint Planning.

---

# 15. Discovery Rules

RD-001 — Discovery là bắt buộc.

RD-002 — Documentation được đọc trước Source Code.

RD-003 — Registry được ưu tiên.

RD-004 — Contract được ưu tiên hơn Implementation.

RD-005 — Không sửa Repository trong Discovery.

RD-006 — Mọi Dependency phải được phát hiện.

RD-007 — Mọi Gap phải được báo cáo.

RD-008 — Không tạo Module nếu đã tồn tại.

RD-009 — Discovery phải sinh Evidence.

RD-010 — Discovery hoàn thành trước Code Generation.

RD-011 — Frontend Discovery là bắt buộc đối với Capability có giao diện.

RD-012 — Capability Demonstration phải được phát hiện hoặc lập kế hoạch.

---

# 16. Repository Knowledge Graph

Repository được mô hình hóa thành Knowledge Graph.

```text
Business Requirement

↓

Capability

↓

Business Object

↓

Module

↓

API

↓

Frontend Experience

↓

Event

↓

Snapshot

↓

Database

↓

Tests
```

AI sử dụng Knowledge Graph để xác định phạm vi ảnh hưởng của Sprint.

---

# 17. Discovery Resolution Pipeline (DiRP)

```text
Sprint Contract
        │
        ▼
Documentation Discovery
        │
        ▼
Registry Discovery
        │
        ▼
Architecture Discovery
        │
        ▼
Repository Discovery
        │
        ▼
Dependency Discovery
        │
        ▼
Contract Discovery
        │
        ▼
Gap Analysis
        │
        ▼
Discovery Evidence
```

Discovery Resolution Pipeline là Pipeline bắt buộc trước mọi Sprint.

---

# 18. Discovery Evidence

Repository Discovery phải sinh tối thiểu:

- Discovery Report
- Module Inventory
- Contract Inventory
- Dependency Graph
- Gap Analysis
- Risk Report

Đây là điều kiện để chuyển sang Sprint Planning.

---

# 19. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0101 | Repository Discovery hoàn thành |
| ACC-0102 | Documentation được đọc trước |
| ACC-0103 | Registry được sử dụng |
| ACC-0104 | Module Inventory đầy đủ |
| ACC-0105 | Dependency Graph được tạo |
| ACC-0106 | Contract Inventory đầy đủ |
| ACC-0107 | Gap Analysis hoàn thành |
| ACC-0108 | Risk Report được sinh |
| ACC-0109 | Discovery không thay đổi Repository |
| ACC-0110 | Discovery Evidence đầy đủ |

---

# 20. Relationship to Other Documents

AAP-01 liên kết với:

- YADF
- ABP-01 Repository Architecture
- ABP-02 Module Architecture
- ABP-03 Dependency Rules
- ABP-15 AI Implementation Architecture
- Sprint Governance Pack (SGP)

Repository Discovery là điểm khởi đầu của mọi Sprint và là cơ sở để AI lập kế hoạch Full-stack Capability Delivery.

---

# 21. Document Status

**Status: FROZEN**

AAP-01 là tài liệu nền tảng quy định mô hình Repository Discovery cho AI.

Mọi AI Coding Assistant phải hoàn thành Repository Discovery trước khi lập kế hoạch hoặc sinh mã nguồn.

---


---

# Source: AAP-02

- Path: `docs/AAP/AAP-02.md`
- Set: `AAP`
- Version: `2.1`
- Status: `FROZEN`

# Sprint Contract Model

## AAP-02

---

# 1. Purpose

Sprint Contract Model định nghĩa mô hình Sprint Contract của nền tảng YSim.

Sprint Contract là đầu vào chính thức của AI trước khi thực hiện Sprint.

Sprint Contract quy định:

- Scope
- Capability
- Ownership
- Dependencies
- Constraints
- Deliverables
- Acceptance Criteria

Sprint Contract là bất biến trong suốt quá trình triển khai.

---

# 2. Principles

Sprint Contract tuân thủ các nguyên tắc:

- Contract First
- Scope Controlled
- Architecture Governed
- Incremental
- Evidence Driven
- Traceable
- Full-stack Capability Delivery
- Experience-oriented Planning

Sprint Contract không phải Prompt.

Sprint Contract không phải Requirement.

Sprint Contract là Implementation Contract.

---

# 3. Sprint Objectives

Một Sprint chỉ được phép triển khai:

- một hoặc nhiều Technical Capability có liên quan;
- trong phạm vi Ownership đã được phê duyệt;
- theo đúng Architecture Baseline.

Sprint không được mở rộng Scope.

---

# 4. Sprint Contract Structure

Sprint Contract bao gồm các phần sau:

```text
Sprint Metadata

↓

Business Context

↓

Technical Capability

↓

Implementation Scope

↓

Dependencies

↓

Constraints

↓

Acceptance Criteria

↓

Full-stack Deliverables

↓

Deliverables

↓

Validation

↓

Evidence
```

---

# 5. Sprint Metadata

Sprint Metadata bao gồm:

- Sprint ID
- Sprint Name
- Version
- Status
- Owner
- Priority
- Target Release

Metadata là định danh duy nhất của Sprint.

---

# 6. Business Context

Business Context xác định:

- Business Domain
- Business Capability
- Business Objects
- Business Policies
- Business Events
- Business Snapshots

AI không được tự mở rộng Business Context.

---

# 7. Technical Capability

Technical Capability mô tả chính xác chức năng kỹ thuật cần triển khai.

Ví dụ:

- Payment Session
- Inventory Allocation
- Settlement Processing
- Notification Delivery

Sprint được tổ chức theo Technical Capability, không theo Business Domain.

Đối với Capability có giao diện người dùng, Sprint phải lập kế hoạch đồng thời cho:

- Backend
- API
- Frontend
- Seed Data
- Capability Demonstration
- Verification

---

# 8. Implementation Scope

Sprint Contract xác định rõ:

Được phép:

- tạo mới;
- mở rộng;
- sửa đổi.

Không được phép:

- thay đổi ngoài phạm vi;
- sửa Domain khác;
- thay đổi Architecture Baseline.

---

# 9. Domain Ownership

Sprint chỉ được Modify các Domain đã được chỉ định.

Ví dụ:

| Domain | Access |
|---------|--------|
| Payment | Modify |
| Order | Read |
| Shared | Approved Extension |
| Customer | Read Only |

Ownership là ràng buộc bắt buộc.

---

# 10. Dependencies

Sprint Contract phải liệt kê:

- Required Modules
- Required APIs
- Required Events
- Required Snapshots
- Required Configurations
- Required Integrations

Dependency được xác minh trong Repository Discovery.

---

# 11. Constraints

Sprint Contract quy định các giới hạn.

Ví dụ:

- Không thay đổi Public API.
- Không thay đổi Event Contract.
- Không đổi Module Ownership.
- Không sửa Migration cũ.
- Không thay đổi Registry.

Constraints luôn có độ ưu tiên cao.

---

# 12. Acceptance Criteria

Acceptance Criteria được chia thành các nhóm.

## Business

- Capability hoàn thành.
- Business Rule đúng.
- Event đúng.
- Snapshot đúng.

## Technical

- Build PASS.
- Static Analysis PASS.
- Contract Validation PASS.

## Operational

- Logging.
- Monitoring.
- Metrics.
- Alert.

---

# 13. Deliverables

Sprint tối thiểu phải tạo:

- Backend Source Code
- Frontend Source Code (nếu có UI)
- Tests
- Migration
- Configuration
- Seed Data
- Capability Demonstration Surface
- Documentation
- Validation Report
- Evidence Package

Deliverables được định nghĩa trước khi triển khai.


---

# 13A. Full-stack Capability Contract

Đối với Capability có giao diện người dùng, Sprint Contract phải mô tả đầy đủ:

- Backend Modules
- Frontend Pages
- API Contracts
- UI Routes
- Design System Components
- Seed Data
- Demonstration Scenarios

Không được lập Sprint chỉ bao gồm Backend nếu Capability yêu cầu trải nghiệm người dùng.


---

# 14. Validation Requirements

Sprint phải vượt qua:

- Architecture Validation
- Dependency Validation
- Contract Validation
- Testing Validation
- Security Validation

Validation là điều kiện để hoàn thành Sprint.

---

# 15. Architecture Change

Nếu AI phát hiện Sprint Contract không thể thực hiện:

AI không được tự thay đổi.

AI phải sinh:

- Architecture Change Proposal (ACP)
- Impact Analysis
- Suggested Resolution

Sprint chỉ tiếp tục sau khi được phê duyệt.

---

# 16. Sprint Lifecycle

```text
Draft

↓

Approved

↓

Repository Discovery

↓

Planning

↓

Backend + Frontend Implementation

↓

Capability Demonstration

↓

Validation

↓

Evidence Generation

↓

Review

↓

Completed
```

Sprint chỉ được chuyển sang bước tiếp theo khi bước hiện tại hoàn thành.

---

# 17. Sprint Deliverable Manifest

Mỗi Sprint phải sinh Sprint Manifest.

Sprint Manifest bao gồm:

- Source Code
- Changed Modules
- New APIs
- New Events
- New Snapshots
- Tests
- Documentation
- Validation Results
- Evidence

Manifest là đầu ra chính thức của Sprint.

---

# 18. Sprint Rules

SC-001 — Sprint Contract là bất biến.

SC-002 — Repository Discovery là bắt buộc.

SC-003 — Không vượt Scope.

SC-004 — Không thay đổi Architecture.

SC-005 — Chỉ Modify Domain Ownership được cấp.

SC-006 — Mọi Dependency phải được xác minh.

SC-007 — Mọi Deliverable phải được sinh.

SC-008 — Validation là bắt buộc.

SC-009 — ACP thay thế việc tự sửa Contract.

SC-010 — Sprint chỉ hoàn thành khi có đầy đủ Evidence.

---

# 19. Sprint Resolution Pipeline (SRP)

```text
Sprint Contract
        │
        ▼
Repository Discovery
        │
        ▼
Dependency Resolution
        │
        ▼
Implementation Planning
        │
        ▼
Implementation
        │
        ▼
Validation
        │
        ▼
Evidence Generation
        │
        ▼
Sprint Manifest
        │
        ▼
Human Review
```

Sprint Resolution Pipeline là mô hình chuẩn cho mọi Sprint trong YSim.

---

# 20. Sprint Evidence

Mỗi Sprint phải sinh tối thiểu:

- Sprint Manifest
- Validation Report
- Test Report
- Coverage Report
- Architecture Compliance Report
- Change Summary
- Review Report
- Demonstration Report

Evidence là điều kiện để nghiệm thu Sprint.

---

# 21. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0201 | Sprint Contract được Approved |
| ACC-0202 | Scope không bị mở rộng |
| ACC-0203 | Repository Discovery hoàn thành |
| ACC-0204 | Dependency được xác minh |
| ACC-0205 | Ownership được tuân thủ |
| ACC-0206 | Constraints không bị vi phạm |
| ACC-0207 | Deliverables đầy đủ |
| ACC-0208 | Validation PASS |
| ACC-0209 | Sprint Manifest được tạo |
| ACC-0210 | Evidence đầy đủ |

---

# 22. Relationship to Other Documents

AAP-02 liên kết với:

- YADF
- ABP-15 AI Implementation Architecture
- AAP-01 Repository Discovery Model
- Sprint Governance Pack (SGP)
- Verification & Acceptance Pack (VAP)
- Codex Implementation Pack (CIP)

Sprint Contract là hợp đồng triển khai duy nhất mà AI được phép thực hiện và là nền tảng của Full-stack Capability Delivery.

---

# 23. Document Status

**Status: FROZEN**

AAP-02 là tài liệu nền tảng quy định mô hình Sprint Contract của nền tảng YSim.

Mọi AI Coding Assistant, Sprint Planning và quy trình triển khai phải tuân thủ Sprint Contract Model trước khi bắt đầu phát triển.

---


---

# Source: AAP-03

- Path: `docs/AAP/AAP-03.md`
- Set: `AAP`
- Version: `2.1`
- Status: `FROZEN`

# AI Planning Model

## AAP-03

---

# 1. Purpose

AI Planning Model định nghĩa mô hình lập kế hoạch triển khai Sprint của AI.

Planning là bước trung gian giữa:

- Repository Discovery
- Code Generation

AI không được sinh mã nguồn trước khi hoàn thành Planning.

---

# 2. Principles

Planning tuân thủ các nguyên tắc:

- Contract First
- Dependency First
- Architecture Safe
- Incremental
- Deterministic
- Evidence Driven
- Full-stack Planning
- Experience-oriented Planning

Planning không được thay đổi Sprint Contract.

Planning chỉ xác định phương án triển khai.

---

# 3. Planning Objectives

Planning nhằm:

- xác định thứ tự triển khai;
- xác định Dependency;
- xác định phạm vi thay đổi;
- giảm rủi ro;
- tối đa khả năng tái sử dụng;
- đảm bảo tuân thủ Architecture.

---

# 4. Planning Inputs

Planning sử dụng:

- Sprint Contract
- Repository Discovery Report
- Dependency Graph
- Module Inventory
- Architecture Baseline
- Engineering Standards

Không sử dụng Prompt tự do làm nguồn quyết định.

---

# 5. Planning Outputs

Planning tạo:

- Sprint Execution Plan
- Task Graph
- Dependency Graph
- Risk Assessment
- Validation Plan
- Demonstration Plan
- Evidence Plan

Đây là đầu vào của Code Generation.

---

# 6. Planning Dimensions

AI phải lập kế hoạch trên các khía cạnh sau.

| Dimension | Description |
|------------|-------------|
| Business | Capability, Scope |
| Architecture | Module, Layer |
| Dependency | Module, Event, API |
| Data | Migration, Snapshot |
| Integration | Connector, Gateway |
| Security | Permission |
| Testing | Test Strategy |
| Operations | Logging, Monitoring |
| Frontend | Pages, Components, Routes |
| Experience | Design System, Demonstration Surface |

---

# 7. Task Decomposition

Sprint được chia thành các Task nhỏ.

Ví dụ:

```text
Capability

↓

Migration

↓

Domain

↓

Application

├── API

├── Backend Services

├── Frontend Pages

├── UI Components

├── Seed Data

├── Demonstration

├── Tests

└── Documentation
```

Task phải có Dependency rõ ràng.

---

# 7A. Full-stack Task Planning

Planning phải tạo Work Package đồng bộ cho từng Capability.

Mỗi Capability có giao diện người dùng phải được phân rã tối thiểu thành:

- Backend
- API
- Frontend
- Design System Integration
- Seed Data
- Capability Demonstration
- Testing
- Documentation

Không được lập kế hoạch chỉ cho Backend nếu Capability yêu cầu Experience.

---

# 8. Task Graph

Planning xây dựng Task Graph.

```text
Migration
      │
      ▼
Domain
      │
      ▼
Application
      │
      ├── API
      ├── Event
      └── Tests
```

Task Graph là Directed Acyclic Graph (DAG).

Không cho phép Circular Task Dependency.

---

# 9. Dependency Resolution

Planning phải phân loại Dependency.

| Type | Strategy |
|------|----------|
| Existing | Reuse |
| Missing | Implement |
| External | Mock hoặc Wait |
| Architecture | ACP |

Planning không được bỏ qua Dependency.

---

# 10. Risk Assessment

Planning đánh giá:

- Architecture Risk
- Technical Risk
- Dependency Risk
- Integration Risk
- Testing Risk

Risk được ghi trong Sprint Plan.

---

# 11. Parallel Planning

AI được phép thực hiện song song khi:

- không vi phạm Dependency;
- không thay đổi cùng một Module;
- không vi phạm Ownership.

Planning phải chỉ rõ các Task có thể chạy song song.

---

# 12. Validation Planning

Planning xác định:

- Unit Test
- Contract Test
- Integration Test
- Scenario Test
- Security Validation

Validation được lập kế hoạch trước khi Code Generation.

---

# 13. Evidence Planning

Planning xác định Evidence cần tạo.

Ví dụ:

- Migration
- Tests
- Validation
- Documentation
- Reports

Evidence không được sinh sau khi kết thúc Sprint.

---

# 14. Architecture Constraints

Planning phải kiểm tra:

- Module Boundary
- Dependency Rules
- Transaction Boundary
- Event Rules
- Snapshot Rules
- Security Rules

Nếu vi phạm:

↓

Architecture Change Proposal.

---

# 15. Planning Rules

PM-001 — Planning là bắt buộc.

PM-002 — Planning sau Discovery.

PM-003 — Planning trước Code Generation.

PM-004 — Task Graph phải là DAG.

PM-005 — Dependency phải được giải quyết.

PM-006 — Validation được lập kế hoạch trước.

PM-007 — Evidence được lập kế hoạch trước.

PM-008 — Không thay đổi Sprint Contract.

PM-009 — Không thay đổi Architecture.

PM-010 — ACP thay thế việc tự sửa Architecture.

---

# 16. AI Planning Resolution Pipeline (APRP)

```text
Sprint Contract
        │
        ▼
Repository Discovery
        │
        ▼
Dependency Resolution
        │
        ▼
Task Decomposition
        │
        ▼
Task Graph
        │
        ▼
Risk Assessment
        │
        ▼
Capability Demonstration Planning
        │
        ▼
Validation Planning
        │
        ▼
Evidence Planning
        │
        ▼
Sprint Execution Plan
```

Planning Resolution Pipeline là đầu vào trực tiếp cho AI Code Generation.

---

# 17. Planning Evidence

Planning phải sinh:

- Sprint Execution Plan
- Task Graph
- Dependency Matrix
- Risk Report
- Validation Plan
- Demonstration Plan
- Evidence Plan

Planning hoàn thành trước khi Code Generation bắt đầu.

---

# 18. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0301 | Planning hoàn thành |
| ACC-0302 | Task Graph hợp lệ |
| ACC-0303 | Không có Circular Dependency |
| ACC-0304 | Dependency được phân loại |
| ACC-0305 | Validation Plan đầy đủ |
| ACC-0306 | Evidence Plan đầy đủ |
| ACC-0307 | Architecture Constraints được kiểm tra |
| ACC-0308 | Risk Assessment hoàn thành |
| ACC-0309 | Sprint Execution Plan được tạo |
| ACC-0310 | Không thay đổi Sprint Contract |

---

# 19. Relationship to Other Documents

AAP-03 liên kết với:

- AAP-01 Repository Discovery Model
- AAP-02 Sprint Contract Model
- ABP-03 Dependency Rules
- ABP-15 AI Implementation Architecture
- Sprint Governance Pack (SGP)

Planning là cầu nối giữa Discovery và Full-stack Code Generation, bảo đảm Backend, Frontend và Capability Demonstration được lập kế hoạch đồng thời.

---

# 20. Document Status

**Status: FROZEN**

AAP-03 là tài liệu nền tảng quy định mô hình lập kế hoạch triển khai của AI.

Mọi AI Coding Assistant phải hoàn thành Planning trước khi sinh mã nguồn.

---


---

# Source: AAP-04

- Path: `docs/AAP/AAP-04.md`
- Set: `AAP`
- Version: `2.1`
- Status: `FROZEN`

# AI Verification Model

## AAP-04

---

# 1. Purpose

AI Verification Model định nghĩa mô hình xác minh kết quả triển khai của AI.

Verification là bước bắt buộc sau Code Generation và trước Human Review.

Verification nhằm xác nhận:

- Sprint Contract đã được thực hiện đầy đủ.
- Kiến trúc không bị vi phạm.
- Deliverables
- Frontend Experience
- Capability Demonstration đầy đủ.
- Evidence đầy đủ.
- Sprint đủ điều kiện nghiệm thu.

Verification không thay thế Testing.

Verification xác nhận toàn bộ Sprint Output.

---

# 2. Principles

Verification tuân thủ các nguyên tắc:

- Verify Before Accept
- Evidence Driven
- Architecture First
- Contract Driven
- Deterministic
- Repeatable
- Explainable
- Full-stack Verification
- Experience Verification

Verification không được dựa trên suy đoán.

---

# 3. Verification Scope

AI phải xác minh tối thiểu:

- Sprint Contract
- Repository Changes
- Architecture Compliance
- Dependency Compliance
- Testing Results
- Documentation
- Evidence
- Deliverables
- Frontend Experience
- Capability Demonstration

---

# 4. Verification Inputs

Verification sử dụng:

- Sprint Contract
- Sprint Execution Plan
- Source Code
- Validation Results
- Test Results
- Repository State
- Architecture Baseline

---

# 5. Verification Outputs

Verification sinh:

- Verification Report
- Compliance Report
- Missing Deliverables
- Risk Summary
- Acceptance Recommendation

---

# 6. Verification Dimensions

Verification bao phủ:

| Dimension | Description |
|------------|-------------|
| Scope | Có vượt Sprint không |
| Architecture | Có vi phạm ABP không |
| Dependency | Có đúng Dependency Rules không |
| Build | Build thành công |
| Testing | Test đạt yêu cầu |
| Documentation | Tài liệu đầy đủ |
| Evidence | Evidence đầy đủ |
| Security | Security Compliance |
| Frontend | UI, Routes, Components |
| Experience | Design System, Demonstration Surface |

---

# 7. Contract Verification

AI xác minh:

- Capability đã hoàn thành
- Deliverables
- Frontend Experience
- Capability Demonstration đầy đủ
- Acceptance Criteria đạt
- Constraints không bị vi phạm

Sprint Contract là tiêu chí cao nhất.

---

# 8. Architecture Verification

AI kiểm tra:

- Module Boundary
- Dependency Rules
- Transaction Boundary
- Event Architecture
- Snapshot Architecture
- Security Architecture
- Configuration Architecture

Không chỉ Build PASS.

---

# 9. Repository Verification

AI kiểm tra:

- File thay đổi
- Module thay đổi
- Migration
- API
- Event
- Snapshot

Không có thay đổi ngoài Scope.

---

# 10. Deliverable Verification

Sprint phải có:

- Backend Source Code
- Frontend Source Code (nếu có UI)
- Migration
- Tests
- Documentation
- Configuration
- Seed Data
- Capability Demonstration Surface
- Validation Report

Thiếu Deliverable → Verification FAIL.

---

# 10A. Frontend & Experience Verification

Đối với Capability có giao diện người dùng, AI phải xác minh:

- Frontend Pages đã được triển khai.
- UI Routes hoạt động.
- API Integration hoàn chỉnh.
- Design System được tuân thủ.
- Capability Demonstration Surface khả dụng.

Verification chỉ PASS khi Backend và Frontend cùng đáp ứng Sprint Contract.

---

# 11. Evidence Verification

Evidence tối thiểu:

- Test Report
- Coverage Report
- Validation Report
- Architecture Compliance
- Demonstration Report
- Screenshot / UI Evidence
- Change Summary

Evidence phải đầy đủ và truy vết được.

---

# 12. Risk Verification

AI đánh giá:

- Architecture Risk
- Regression Risk
- Dependency Risk
- Security Risk
- Operational Risk

Risk phải được ghi trong Verification Report.

---

# 13. Verification Decision

Verification chỉ có bốn trạng thái:

- PASS
- PASS WITH WARNING
- FAIL
- BLOCKED

Không có trạng thái mơ hồ.

---

# 14. Verification Rules

VM-001 — Verification là bắt buộc.

VM-002 — Verification sau Validation.

VM-003 — Verification trước Human Review.

VM-004 — Verification dựa trên Sprint Contract.

VM-005 — Evidence là bắt buộc.

VM-006 — Architecture Compliance là bắt buộc.

VM-007 — Không bỏ qua Deliverables.

VM-008 — Không bỏ qua Risk.

VM-009 — Verification phải Explainable.

VM-010 — Verification Report là Output chính thức.

---

# 15. AI Verification Resolution Pipeline (AVRP)

```text
Sprint Output
        │
        ▼
Contract Verification
        │
        ▼
Architecture Verification
        │
        ▼
Dependency Verification
        │
        ▼
Deliverable Verification
        │
        ▼
Frontend Verification
        │
        ▼
Evidence Verification
        │
        ▼
Risk Verification
        │
        ▼
Verification Report
        │
        ▼
Acceptance Recommendation
```

---

# 16. Verification Evidence

Verification phải sinh:

- Verification Report
- Compliance Report
- Deliverable Checklist
- Evidence Checklist
- Risk Summary
- Acceptance Recommendation

---

# 17. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0401 | Sprint Contract được xác minh |
| ACC-0402 | Không vượt Scope |
| ACC-0403 | Architecture Compliance PASS |
| ACC-0404 | Dependency Compliance PASS |
| ACC-0405 | Deliverables đầy đủ |
| ACC-0406 | Evidence đầy đủ |
| ACC-0407 | Risk được đánh giá |
| ACC-0408 | Verification Report được tạo |
| ACC-0409 | Acceptance Recommendation có sẵn |
| ACC-0410 | Human Review sẵn sàng |

---

# 18. Relationship to Other Documents

AAP-04 liên kết với:

- AAP-01 Repository Discovery Model
- AAP-02 Sprint Contract Model
- AAP-03 AI Planning Model
- ABP-13 Testing Architecture
- ABP-15 AI Implementation Architecture
- Verification & Acceptance Pack (VAP)

Verification là bước cuối cùng của AI trước khi chuyển Sprint sang Human Review, bảo đảm Capability được xác minh đầy đủ ở cả Backend, Frontend và Demonstration.

---

# 19. Document Status

**Status: FROZEN**

AAP-04 là tài liệu nền tảng quy định mô hình xác minh kết quả triển khai của AI.

Mọi AI Coding Assistant phải hoàn thành Verification trước khi Sprint được chuyển sang nghiệm thu.

---


---

# Source: AAP-05

- Path: `docs/AAP/AAP-05.md`
- Set: `AAP`
- Version: `2.1`
- Status: `FROZEN`

# AI Evidence Model

## AAP-05

---

# 1. Purpose

AI Evidence Model định nghĩa mô hình bằng chứng triển khai của AI.

Evidence là đầu ra chính thức của mỗi Sprint.

Evidence được sử dụng cho:

- Human Review
- QA
- Acceptance
- Release
- Audit
- Knowledge Base
- Capability Demonstration

Source Code chỉ là một phần của Evidence.

---

# 2. Principles

AI Evidence tuân thủ các nguyên tắc:

- Evidence First
- Traceable
- Verifiable
- Immutable
- Reproducible
- Complete
- Explainable
- Full-stack Evidence
- Experience Evidence

Mọi Sprint đều phải tạo Evidence.

Không có Evidence thì Sprint chưa hoàn thành.

---

# 3. Evidence Objectives

Evidence nhằm chứng minh:

- Sprint Contract đã được thực hiện.
- Kiến trúc được tuân thủ.
- Deliverables đầy đủ.
- Validation hoàn thành.
- Sprint đủ điều kiện nghiệm thu.

Evidence không phải Documentation.

Evidence là Proof.

---

# 4. Evidence Categories

Platform chuẩn hóa các nhóm Evidence.

| Category | Description |
|----------|-------------|
| Planning Evidence | Sprint Planning |
| Implementation Evidence | Source Code |
| Validation Evidence | Build, Static Analysis |
| Testing Evidence | Test Results |
| Architecture Evidence | Compliance |
| Documentation Evidence | Updated Documents |
| Deployment Evidence | Release Manifest |
| Review Evidence | Human Review |
| Frontend Evidence | UI, Components, Routes |
| Demonstration Evidence | Screenshots, Demo, User Journey |

---

# 5. Evidence Lifecycle

```text
Planned

↓

Generated

↓

Validated

↓

Reviewed

↓

Accepted

↓

Archived
```

Evidence không được sửa sau khi Sprint đã Accepted.

---

# 6. Evidence Traceability

Mỗi Evidence phải truy vết được tới:

- Sprint
- Capability
- Business Requirement
- Business Object
- Module
- Source Commit
- Test
- Validation
- Release

Evidence phải luôn có khả năng truy ngược.

---

# 7. Mandatory Evidence

Mỗi Sprint tối thiểu phải có:

- Sprint Manifest
- Source Code Summary
- Change Summary
- Validation Report
- Test Report
- Architecture Compliance Report
- Documentation Update
- Frontend Build Summary
- Demonstration Report
- Screenshot / UI Evidence
- Review Summary

Thiếu bất kỳ thành phần nào đều khiến Sprint chưa hoàn thành.

---

# 7A. Full-stack Evidence

Đối với Capability có giao diện người dùng, Evidence Package phải bao gồm đầy đủ:

- Backend Source Summary
- Frontend Source Summary
- API Summary
- Seed Data Summary
- Capability Demonstration Report
- Screenshot / UI Evidence
- Design System Compliance
- Integration Evidence

Evidence chỉ được coi là Complete khi cả Backend và Frontend đều có bằng chứng tương ứng.

---

# 8. Evidence Manifest

Evidence được quản lý thông qua Evidence Manifest.

Manifest bao gồm:

- Evidence ID
- Sprint ID
- Version
- Type
- Owner
- Status
- Generated Time

Manifest là điểm truy cập thống nhất tới toàn bộ Evidence.

---

# 9. Evidence Validation

Mọi Evidence phải được kiểm tra:

- Completeness
- Consistency
- Traceability
- Integrity

Evidence không hợp lệ phải được tạo lại.

---

# 10. Evidence Packaging

Evidence được đóng gói thành một Sprint Evidence Package.

Package bao gồm:

- Backend Source Code
- Frontend Source Code
- Reports
- Test Results
- Documentation
- Configuration Changes
- Migration Summary
- Seed Data
- Demonstration Assets

Package là đầu ra chuẩn của Sprint.

---

# 11. Evidence Repository

Evidence được lưu trữ độc lập với Source Code Repository.

Repository phải hỗ trợ:

- Versioning
- Search
- Traceability
- Retention

Evidence không bị mất sau khi Release.

---

# 12. Human Review

Human Review sử dụng Evidence để:

- Review Sprint
- Verify Architecture
- Review Risk
- Approve Release

Human không cần đọc toàn bộ Source Code nếu Evidence đầy đủ.

---

# 13. AI Explainability

AI phải giải thích:

- Tại sao thay đổi.
- Thay đổi ở đâu.
- Phụ thuộc nào bị ảnh hưởng.
- Validation nào đã thực hiện.
- Điều gì chưa hoàn thành.

Explainability là một phần của Evidence.

---

# 14. Evidence Rules

EM-001 — Every Sprint produces Evidence.

EM-002 — Evidence is Traceable.

EM-003 — Evidence is Immutable after Acceptance.

EM-004 — Evidence is Explainable.

EM-005 — Evidence is Versioned.

EM-006 — Evidence is Validated.

EM-007 — Evidence is Complete.

EM-008 — Evidence supports Human Review.

EM-009 — Evidence supports Audit.

EM-010 — Sprint Output equals Evidence Package.

---

# 15. AI Evidence Resolution Pipeline (AERP)

```text
Sprint Output
        │
        ▼
Evidence Collection
        │
        ▼
Frontend Evidence Collection
        │
        ▼
Evidence Validation
        │
        ▼
Evidence Packaging
        │
        ▼
Evidence Manifest
        │
        ▼
Human Review
        │
        ▼
Sprint Acceptance
        │
        ▼
Evidence Archive
```

Evidence Resolution Pipeline là Pipeline chuẩn để tạo đầu ra của mỗi Sprint.

---

# 16. Evidence Deliverables

Evidence Package tối thiểu bao gồm:

- Sprint Manifest
- Validation Report
- Test Report
- Architecture Compliance Report
- Documentation Update
- Source Code Summary
- Change Summary
- Risk Summary
- Demonstration Report
- UI Evidence

---

# 17. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0501 | Evidence Package được tạo |
| ACC-0502 | Sprint Manifest đầy đủ |
| ACC-0503 | Evidence Traceability đầy đủ |
| ACC-0504 | Validation Report có sẵn |
| ACC-0505 | Test Report đầy đủ |
| ACC-0506 | Documentation được cập nhật |
| ACC-0507 | Architecture Compliance PASS |
| ACC-0508 | Explainability đầy đủ |
| ACC-0509 | Human Review có đủ thông tin |
| ACC-0510 | Evidence được lưu trữ |

---

# 18. Relationship to Other Documents

AAP-05 liên kết với:

- AAP-02 Sprint Contract Model
- AAP-03 AI Planning Model
- AAP-04 AI Verification Model
- ABP-13 Testing Architecture
- ABP-14 Deployment Architecture
- ABP-15 AI Implementation Architecture
- Verification & Acceptance Pack (VAP)

Evidence là đầu vào chính cho Acceptance và Release, đồng thời chứng minh Capability đã hoàn thành ở cả Backend, Frontend và Demonstration.

---

# 19. Document Status

**Status: FROZEN**

AAP-05 là tài liệu nền tảng quy định mô hình bằng chứng triển khai của AI.

Mọi AI Coding Assistant phải tạo đầy đủ Evidence Package trước khi Sprint được nghiệm thu.

---



# ALLOWED PATHS

- factory/
- knowledge/
- tools/
- scripts/
- docs/ESPK/

# PROTECTED PATHS

- docs/AFM/
- docs/BRD/
- docs/ABP/
- docs/YADF/
- docs/AAP/
- docs/SGP/
- docs/ESP/
- docs/DIP/
- docs/ROP/

# IMPLEMENTATION RULES

1. Work only within the declared task scope.
2. Do not modify protected paths.
3. Do not change frozen architecture or business decisions.
4. Preserve existing repository structure and conventions.
5. Do not bypass validation.
6. Stop if required context is missing or contradictory.
7. Keep all changes deterministic, reviewable and reversible.

# VALIDATION COMMANDS

- ysf verify
- git diff --check

# REQUIRED OUTPUTS

- repository assessment
- identified risks
- validation result
- implementation recommendation

# COMPLETION CONDITIONS

The task is complete only when:

- the objective is satisfied;
- all requested outputs are produced;
- validation commands pass;
- no protected path is modified;
- all implementation evidence is available.

# STOP CONDITIONS

Stop execution and report the problem when:

- architecture conflict is detected;
- required context is missing;
- a protected file must be modified;
- repository state is unsafe;
- validation cannot pass without expanding scope.
