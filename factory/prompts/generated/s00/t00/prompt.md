# ROLE

You are the primary AI coding agent operating the YSim Software Factory.

# EXECUTION ID

- Sprint: S00
- Task: T00
- Prompt ID: s00-t00
- Provider: codex

# OBJECTIVE

Review and verify the YSim Software Factory repository baseline for Sprint-00 without modifying business source code.


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
?? factory/prompts/generated/s01/t04/
?? factory/reports/s01/s01-t04-logging-errors.md
```

## Recent Commits

```text
e5e1ac3 (HEAD -> feat/s01-platform-foundation, tag: s01-t03-complete) feat(s01-t03): add typed configuration and environment validation
7548433 (origin/feat/s01-platform-foundation) prepared
af7d70e (tag: s01-t02-complete) feat(s01-t02): bootstrap NestJS API application
bdcec14 (tag: s01-t01-complete) feat(s01-t01): establish monorepo workspace foundation
e3ed5dd prepared
d6629e4 chore(s01): add sequential sprint auto runner
10ace03 docs(s01-t00): complete repository audit and execution plan
3a89828 fix(s01): align prompt manifests and validator with ysf schema
9154741 fix(s01): align t00 prompt manifest with ysf schema
5be8413 (tag: architecture-v2.2, origin/chore/s00-factory-commissioning, chore/s00-factory-commissioning) release(architecture): freeze architecture baseline v2.2
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

- AFM-00 (docs/AFM/AFM-00.md)
- DIP-00 (docs/DIP/DIP-00.md)
- DIP-01 (docs/DIP/DIP-01.md)
- DIP-02 (docs/DIP/DIP-02.md)
- DIP-04 (docs/DIP/DIP-04.md)
- DIP-05 (docs/DIP/DIP-05.md)
- DIP-06 (docs/DIP/DIP-06.md)
- DIP-09 (docs/DIP/DIP-09.md)
- ESPK-S00 (docs/ESPK/ESPK-S00.md)
- YADF-00 (docs/YADF/YADF-00.md)
- AAP-01 (docs/AAP/AAP-01.md)
- AAP-02 (docs/AAP/AAP-02.md)
- AAP-03 (docs/AAP/AAP-03.md)
- AAP-04 (docs/AAP/AAP-04.md)
- AAP-05 (docs/AAP/AAP-05.md)
- AAP-06 (docs/AAP/AAP-06.md)
- ABP-01 (docs/ABP/ABP-01.md)
- ABP-02 (docs/ABP/ABP-02.md)
- ABP-07 (docs/ABP/ABP-07.md)
- ABP-14 (docs/ABP/ABP-14.md)
- ABP-15 (docs/ABP/ABP-15.md)
- AFM-01 (docs/AFM/AFM-01.md)
- DIP-03 (docs/DIP/DIP-03.md)
- DIP-07 (docs/DIP/DIP-07.md)
- DIP-08 (docs/DIP/DIP-08.md)
- DIP-10 (docs/DIP/DIP-10.md)
- ESP-00 (docs/ESP/ESP-00.md)
- ESP-01 (docs/ESP/ESP-01.md)
- ESP-02 (docs/ESP/ESP-02.md)
- ESP-03 (docs/ESP/ESP-03.md)

# CONTEXT

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


---

# Source: AAP-06

- Path: `docs/AAP/AAP-06.md`
- Set: `AAP`
- Version: `2.1`
- Status: `FROZEN`

# Architecture Change Proposal Model

## AAP-06

---

# 1. Purpose

Architecture Change Proposal (ACP) Model định nghĩa quy trình đề xuất thay đổi kiến trúc trong quá trình AI triển khai Sprint.

AI không được tự thay đổi Architecture Baseline.

Mọi thay đổi kiến trúc đều phải thông qua ACP.

---

# 2. Principles

ACP tuân thủ các nguyên tắc:

- Architecture First
- Human Governed
- Proposal Before Change
- Impact Driven
- Evidence Based
- Traceable
- Versioned
- Full-stack Impact Analysis
- Experience-aware Governance

ACP không phải Implementation.

ACP là Proposal.

---

# 3. ACP Objectives

ACP được sử dụng khi:

- Sprint Contract không thể thực hiện.
- Architecture Baseline có mâu thuẫn.
- Dependency không còn phù hợp.
- Thiết kế hiện tại gây rủi ro lớn.
- Có giải pháp tốt hơn nhưng ảnh hưởng Architecture.

ACP không được dùng cho thay đổi nhỏ trong phạm vi Sprint.

---

# 4. ACP Trigger Conditions

AI phải tạo ACP khi gặp một trong các trường hợp:

- Vi phạm Module Boundary.
- Vi phạm Dependency Rules.
- Cần tạo Business Object mới.
- Cần thay đổi Registry.
- Cần thay đổi Event Contract.
- Cần thay đổi Snapshot Contract.
- Cần thay đổi Public API.
- Cần thay đổi Frontend Contract.
- Cần thay đổi Design System Foundation.
- Cần thay đổi Experience Composition.
- Cần thay đổi Ownership.

Nếu không thuộc các trường hợp trên thì không tạo ACP.

---

# 5. ACP Structure

ACP bao gồm:

```text
Proposal Metadata

↓

Problem Statement

↓

Current Architecture

↓

Proposed Change

↓

Impact Analysis

↓

Alternative Options

↓

Recommendation

↓

Decision
```

---

# 6. Proposal Metadata

Bao gồm:

- ACP ID
- Sprint ID
- Version
- Status
- Created By
- Created Time

ACP có Version độc lập.

---

# 7. Problem Statement

ACP phải mô tả rõ:

- vấn đề là gì;
- xảy ra ở đâu;
- vì sao không thể tiếp tục;
- ảnh hưởng tới Sprint nào.

Không mô tả chung chung.

---

# 8. Current Architecture

ACP phải chỉ rõ:

- Module
- Capability
- Business Object
- API
- Event
- Snapshot
- Frontend
- Design System
- Experience Composition
- Dependency

đang bị ảnh hưởng.

---

# 9. Proposed Change

ACP mô tả:

- thay đổi đề xuất;
- phạm vi;
- Architecture Component liên quan;
- Registry cần cập nhật (nếu có).

Proposal không chứa Source Code.

---

# 10. Impact Analysis

ACP đánh giá ảnh hưởng tới:

- Business Capability
- Module
- Domain
- API
- Event
- Snapshot
- Database
- Integration
- Security
- Testing
- Deployment
- Frontend
- Design System
- Customer Experience

Impact phải đầy đủ.

---

# 10A. Full-stack Impact Assessment

Đối với Capability có giao diện người dùng, ACP phải đánh giá đồng thời tác động đến:

- Backend Architecture
- API Contract
- Frontend Pages
- UI Components
- Design System
- Storefront Runtime
- Capability Demonstration
- Test Strategy

Không được đánh giá thay đổi kiến trúc chỉ ở Backend nếu thay đổi đó ảnh hưởng Experience.

---

# 11. Alternative Options

ACP phải có tối thiểu:

- Option A
- Option B

Nếu có thể:

- Option C

AI không chỉ đưa ra một phương án duy nhất.

---

# 12. Recommendation

AI đưa ra:

- Recommended Option
- Lý do
- Ưu điểm
- Rủi ro
- Điều kiện áp dụng

Recommendation phải giải thích được.

---

# 13. Decision Workflow

```text
Draft

↓

Architecture Review

↓

Business Review (if required)

↓

Approved / Rejected

↓

Architecture Baseline Update

↓

Sprint Resume
```

AI không được tự chuyển sang bước cuối.

---

# 14. Architecture Baseline Update

Nếu ACP được phê duyệt:

- cập nhật Architecture Baseline;
- cập nhật Registry;
- cập nhật Sprint Contract nếu cần.

Chỉ sau đó AI mới được tiếp tục triển khai.

---

# 15. ACP Traceability

ACP phải truy vết được tới:

- Sprint
- Capability
- Module
- Business Object
- Registry
- Architecture Baseline
- Decision
- Reviewer

---

# 16. ACP Rules

ACP-001 — AI không tự thay đổi Architecture.

ACP-002 — ACP phải có Impact Analysis.

ACP-003 — ACP phải có Alternative Options.

ACP-004 — ACP phải có Recommendation.

ACP-005 — ACP không chứa Source Code.

ACP-006 — ACP phải được Review.

ACP-007 — ACP phải được Version.

ACP-008 — ACP phải truy vết được.

ACP-009 — Sprint chỉ tiếp tục sau khi ACP được quyết định.

ACP-010 — ACP được lưu như một Architecture Artifact.

---

# 17. Architecture Change Resolution Pipeline (ACRP)

```text
Architecture Conflict
        │
        ▼
Full-stack Impact Identification
        │
        ▼
Problem Identification
        │
        ▼
Impact Analysis
        │
        ▼
Alternative Analysis
        │
        ▼
Recommendation
        │
        ▼
Architecture Review
        │
        ▼
Decision
        │
        ▼
Architecture Baseline Update
        │
        ▼
Sprint Resume
```

---

# 18. ACP Deliverables

Một ACP tối thiểu phải tạo:

- ACP Document
- Impact Analysis
- Architecture Diagram Update (nếu có)
- Registry Change Summary
- Frontend Impact Summary
- Demonstration Impact Summary
- Recommendation
- Decision Record

---

# 19. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0601 | ACP được tạo đúng điều kiện |
| ACC-0602 | Problem Statement rõ ràng |
| ACC-0603 | Impact Analysis đầy đủ |
| ACC-0604 | Alternative Options tồn tại |
| ACC-0605 | Recommendation có giải thích |
| ACC-0606 | ACP không chứa Source Code |
| ACC-0607 | Architecture Review hoàn thành |
| ACC-0608 | Decision được ghi nhận |
| ACC-0609 | Architecture Baseline được cập nhật (nếu Approved) |
| ACC-0610 | Sprint chỉ tiếp tục sau Decision |

---

# 20. Relationship to Other Documents

AAP-06 liên kết với:

- AAP-01 Repository Discovery Model
- AAP-02 Sprint Contract Model
- AAP-03 AI Planning Model
- AAP-04 AI Verification Model
- AAP-05 AI Evidence Model
- ABP-15 AI Implementation Architecture
- Architecture Baseline Pack (ABP)
- Sprint Governance Pack (SGP)

ACP là cơ chế quản trị mọi thay đổi kiến trúc phát sinh trong quá trình AI triển khai, bảo đảm mọi thay đổi đều được đánh giá trên cả Backend, Frontend và Experience.

---

# 21. Document Status

**Status: FROZEN**

AAP-06 là tài liệu nền tảng quy định mô hình đề xuất thay đổi kiến trúc của nền tảng YSim.

Mọi AI Coding Assistant phải sử dụng ACP khi phát hiện nhu cầu thay đổi Architecture Baseline.

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

# Source: ABP-07

- Path: `docs/ABP/ABP-07.md`
- Set: `ABP`
- Version: `1.0`
- Status: `FROZEN`

# Configuration Architecture

## ABP-07

---

# 1. Purpose

Configuration Architecture định nghĩa kiến trúc quản lý Configuration của nền tảng YSim.

Tài liệu này chuẩn hóa:

- Configuration Lifecycle
- Configuration Ownership
- Configuration Versioning
- Runtime Configuration
- Configuration Distribution
- Configuration Governance
- Configuration Security
- Configuration Deployment

Configuration là một thành phần kiến trúc của Platform.

---

# 2. Configuration Principles

YSim áp dụng các nguyên tắc:

- Configuration Driven
- Business Managed
- Versioned
- Approved
- Traceable
- Runtime Reloadable
- Environment Aware
- Policy Controlled

Business Behavior ưu tiên điều khiển bằng Configuration thay vì Hard-code.

---

# 3. Configuration Definition

Configuration là tập hợp các tham số điều khiển hành vi của Platform.

Configuration không phải Source Code.

Configuration không phải Business Data.

Configuration có vòng đời độc lập.

---

# 4. Configuration Categories

Platform chuẩn hóa các nhóm Configuration.

| Category | Examples |
|-----------|----------|
| Platform Configuration | Cache, Timeout, Retry |
| Business Configuration | Commercial Parameters |
| Organization Configuration | Branding, Theme |
| Security Configuration | MFA, Password Policy |
| Integration Configuration | Connector, Endpoint |
| Notification Configuration | Template, Channel |
| Reporting Configuration | KPI, Dashboard |
| Scheduler Configuration | Job Schedule |

---

# 5. Configuration Ownership

Mỗi Configuration chỉ có một Owner.

Owner chịu trách nhiệm:

- tạo;
- cập nhật;
- phê duyệt;
- phát hành;
- ngừng sử dụng.

Không có Configuration không có Ownership.

---

# 6. Configuration Lifecycle

```text
Draft

↓

Review

↓

Approved

↓

Published

↓

Effective

↓

Deprecated

↓

Archived
```

Không sử dụng Configuration chưa được Published.

---

# 7. Configuration Version

Mọi Configuration đều hỗ trợ Version.

Version mới không ghi đè Version cũ.

Platform luôn lưu lịch sử Version.

---

# 8. Effective Date

Configuration hỗ trợ:

- Effective From
- Effective Until

Platform luôn áp dụng Version có hiệu lực tại thời điểm xử lý.

---

# 9. Runtime Reload

Platform phải hỗ trợ Runtime Reload.

Không yêu cầu Restart Service khi:

- thay đổi Reference Data;
- thay đổi Metadata;
- thay đổi Business Rule;
- thay đổi Policy;
- thay đổi Dictionary;
- thay đổi Configuration thông thường.

Các trường hợp cần Restart phải được quy định rõ.

---

# 10. Configuration Dependency

Configuration có thể phụ thuộc nhau.

Ví dụ:

```text
Price Policy

↓

Promotion Policy

↓

Settlement Policy
```

Dependency phải được kiểm tra trước khi Publish.

Không cho phép tạo Dependency vòng (Circular Dependency).

---

# 11. Configuration Package

Configuration hỗ trợ Package.

Package bao gồm:

- Configuration
- Reference Data
- Dictionary
- Metadata
- Business Rule
- Policy

Package được sử dụng cho:

- Migration
- Deployment
- Environment Synchronization

---

# 12. Environment Management

Configuration được quản lý theo Environment.

Ví dụ:

- Development
- Test
- UAT
- Staging
- Production

Platform phải hỗ trợ Promote Configuration giữa các Environment.

---

# 13. Configuration Validation

Trước khi Publish phải Validate:

- Schema
- Dependency
- Reference
- Effective Date
- Conflict
- Security

Không Publish Configuration không hợp lệ.

---

# 14. Configuration Security

Configuration chịu Security Policy.

Có thể áp dụng:

- Approval Workflow
- Permission
- Data Masking
- Encryption
- Audit

Configuration nhạy cảm phải được bảo vệ.

---

# 15. Configuration Traceability

Mỗi Configuration phải truy vết được:

- Business Requirement
- Business Object
- Policy
- Rule
- Version
- Owner
- Approval
- Deployment Package

---

# 16. Configuration Rollback

Platform phải hỗ trợ Rollback.

Rollback không làm mất Version cũ.

Rollback luôn tạo Audit và Business Event.

---

# 17. Configuration Distribution

Configuration được phân phối thông qua Configuration Service.

Module không đọc trực tiếp Database Configuration.

Module luôn sử dụng Contract của Configuration Service.

---

# 18. Configuration Rules

CA-001 — Configuration ưu tiên hơn Hard-code.

CA-002 — Configuration phải có Version.

CA-003 — Configuration phải có Approval.

CA-004 — Configuration hỗ trợ Effective Date.

CA-005 — Configuration hỗ trợ Runtime Reload.

CA-006 — Configuration phải có Traceability.

CA-007 — Configuration phải có Owner.

CA-008 — Configuration hỗ trợ Package.

CA-009 — Configuration được Validate trước khi Publish.

CA-010 — Configuration tuân thủ Security Policy.

---

# 19. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0701 | Configuration có Owner |
| ACC-0702 | Configuration có Version |
| ACC-0703 | Configuration có Approval |
| ACC-0704 | Configuration hỗ trợ Effective Date |
| ACC-0705 | Configuration được Validate trước Publish |
| ACC-0706 | Runtime Reload hoạt động đúng |
| ACC-0707 | Không có Circular Dependency |
| ACC-0708 | Configuration được Audit |
| ACC-0709 | Configuration được quản lý theo Environment |
| ACC-0710 | Configuration sử dụng Configuration Service thay vì truy cập trực tiếp Database |

Checklist này được sử dụng trong:

- Architecture Review
- AI Review
- CI/CD Validation
- Code Review

---

# 20. Relationship to Other Baselines

Configuration Architecture liên kết với:

- ABP-03 Dependency Rules
- ABP-04 Transaction Boundary
- ABP-05 Event Architecture
- ABP-06 Snapshot Architecture
- BRD-POLICY-INDEX
- BRD-BO-INDEX

Configuration là thành phần điều khiển hành vi của Platform, không phải Business Data.

---

# 21. Document Status

**Status: FROZEN**

ABP-07 là tài liệu nền tảng quy định kiến trúc Configuration của nền tảng YSim.

Mọi Module, Sprint và AI Implementation phải tuân thủ các nguyên tắc trong tài liệu này.

---


---

# Source: ABP-14

- Path: `docs/ABP/ABP-14.md`
- Set: `ABP`
- Version: `1.0`
- Status: `FROZEN`

# Deployment Architecture

## ABP-14

---

# 1. Purpose

Deployment Architecture định nghĩa kiến trúc triển khai và phát hành của nền tảng YSim.

Tài liệu này chuẩn hóa:

- Deployment Unit
- Release Architecture
- Environment Strategy
- Deployment Pipeline
- Rollback
- Release Governance
- Operational Readiness

Deployment Architecture đảm bảo mọi Release có thể được triển khai, kiểm soát và khôi phục một cách an toàn.

---

# 2. Deployment Principles

YSim áp dụng các nguyên tắc:

- Release by Contract
- Immutable Artifact
- Environment Independent
- Configuration Driven
- Safe Deployment
- Reproducible
- Traceable
- Rollback Ready

---

# 3. Deployment Architecture

```text
Source Code

↓

Build Artifact

↓

Release Package

↓

Deployment Package

↓

Environment

↓

Runtime Platform
```

Artifact không thay đổi sau khi phát hành.

---

# 4. Deployment Unit

Deployment Unit là đơn vị nhỏ nhất được phép triển khai.

Ví dụ:

- API Service
- Worker
- Scheduler
- Portal
- Gateway

Deployment Unit không nhất thiết trùng với Module.

---

# 5. Release Unit

Release Unit là tập hợp các Deployment Unit được phát hành cùng nhau.

Một Release Unit phải có:

- Version
- Manifest
- Release Note
- Migration
- Validation Report

---

# 6. Environment Strategy

Platform chuẩn hóa các môi trường:

- Local
- Development
- Integration
- UAT
- Staging
- Production

Không Hard-code cấu hình theo Environment.

---

# 7. Deployment Pipeline

```text
Build

↓

Package

↓

Validation

↓

Deployment

↓

Verification

↓

Monitoring

↓

Acceptance
```

Deployment chỉ được tiếp tục nếu vượt qua từng bước.

---

# 8. Configuration during Deployment

Deployment không thay đổi Source Code.

Khác biệt giữa các Environment được điều khiển bởi:

- Configuration
- Secret
- Policy
- Environment Variable

---

# 9. Database Migration

Migration tuân thủ:

- Forward Only
- Versioned
- Repeatable
- Auditable

Không sửa Migration đã phát hành.

---

# 10. Release Verification

Sau Deployment phải thực hiện:

- Health Check
- Smoke Test
- Contract Validation
- Business Verification
- Monitoring Validation

Release chỉ được chấp nhận khi Verification thành công.

---

# 11. Rollback Strategy

Platform hỗ trợ:

- Application Rollback
- Configuration Rollback
- Feature Rollback

Database Rollback không phải cơ chế mặc định.

Nếu dữ liệu đã thay đổi, xử lý theo Migration hoặc Compensation.

---

# 12. Feature Management

Platform hỗ trợ:

- Feature Flag
- Kill Switch
- Progressive Enablement

Feature có thể được bật/tắt mà không cần triển khai lại khi kiến trúc cho phép.

---

# 13. Release Traceability

Mỗi Release phải truy vết được tới:

- Sprint
- Capability
- Source Commit
- Build
- Artifact
- Migration
- Test Evidence
- Deployment Record

---

# 14. Operational Readiness

Một Release chỉ sẵn sàng Production khi có:

- Build PASS
- Verification PASS
- Monitoring
- Alert
- Runbook
- Rollback Plan
- Release Approval

---

# 15. Deployment Rules

DEP-001 — Artifact là Immutable.

DEP-002 — Configuration tách khỏi Source Code.

DEP-003 — Migration chỉ tiến về phía trước.

DEP-004 — Release phải có Manifest.

DEP-005 — Release phải có Validation Report.

DEP-006 — Rollback phải được định nghĩa trước.

DEP-007 — Mọi Release đều có Traceability.

DEP-008 — Production chỉ nhận Release đã được Approval.

DEP-009 — Feature Flag ưu tiên hơn Branching Runtime.

DEP-010 — Deployment phải Observable.

---

# 16. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-1401 | Immutable Artifact |
| ACC-1402 | Environment Independent |
| ACC-1403 | Configuration tách khỏi Code |
| ACC-1404 | Migration Versioned |
| ACC-1405 | Release Manifest đầy đủ |
| ACC-1406 | Verification hoàn thành |
| ACC-1407 | Rollback Plan tồn tại |
| ACC-1408 | Feature Flag đúng chuẩn |
| ACC-1409 | Monitoring sau Release |
| ACC-1410 | Release có đầy đủ Traceability |

---

# 17. Relationship to Other Baselines

Deployment Architecture liên kết với:

- ABP-07 Configuration Architecture
- ABP-09 Security Architecture
- ABP-10 Observability Architecture
- ABP-12 Error Handling Architecture
- ABP-13 Testing Architecture

Deployment là cầu nối giữa Development và Operations.

---

# 18. Document Status

**Status: FROZEN**

ABP-14 là tài liệu nền tảng quy định kiến trúc triển khai và phát hành của nền tảng YSim.

Mọi Release, Deployment Pipeline và AI Implementation phải tuân thủ các nguyên tắc trong tài liệu này.

---


---

# Source: ABP-15

- Path: `docs/ABP/ABP-15.md`
- Set: `ABP`
- Version: `1.0`
- Status: `FROZEN`

# AI Implementation Architecture

## ABP-15

---

# 1. Purpose

AI Implementation Architecture định nghĩa kiến trúc triển khai phần mềm bằng AI của nền tảng YSim.

Tài liệu này chuẩn hóa:

- AI Working Model
- Sprint Execution
- Repository Discovery
- Implementation Strategy
- Validation
- Evidence Generation
- Architecture Governance

AI là Implementation Agent của Platform.

---

# 2. AI Principles

YSim áp dụng các nguyên tắc:

- Contract Driven
- Registry Governed
- Sprint Based
- Evidence Driven
- Repository Aware
- Architecture Safe
- Human Governed
- AI Assisted

AI không phải Architecture Owner.

AI không phải Business Owner.

AI chỉ hiện thực hóa kiến trúc đã được phê duyệt.

---

# 3. AI Implementation Lifecycle

```text
Sprint Contract

↓

Repository Discovery

↓

Implementation Planning

↓

Code Generation

↓

Validation

↓

Evidence Generation

↓

Human Review

↓

Sprint Completion
```

Mọi Sprint đều phải tuân theo Lifecycle này.

---

# 4. Repository Discovery

Repository Discovery là bước bắt buộc.

AI phải xác định:

- Existing Modules
- Existing APIs
- Existing Events
- Existing Snapshots
- Existing Database
- Existing Migrations
- Existing Tests
- Existing Contracts

Nếu không thực hiện Discovery, AI không được phép triển khai.

---

# 5. Sprint Contract

Sprint Contract là đầu vào duy nhất của AI.

Sprint Contract xác định:

- Scope
- Capability
- Ownership
- Constraints
- Acceptance Criteria
- Dependencies

AI không được tự mở rộng Scope.

---

# 6. Architecture Governance

AI phải tuân thủ:

- BRD
- Registry
- ABP
- DIP
- ESP
- Sprint Contract

Nếu phát hiện mâu thuẫn:

↓

Architecture Change Proposal (ACP)

AI không được tự thay đổi Architecture.

---

# 7. Dependency Resolution

AI chỉ được sử dụng:

- Public Contract
- Approved API
- Registered Event
- Registered Snapshot
- Approved Shared Component

Không sử dụng Internal Implementation của Module khác.

---

# 8. Code Generation Principles

Code phải:

- tuân thủ Module Boundary;
- tuân thủ Dependency Rules;
- tuân thủ Security Policy;
- tuân thủ Configuration Architecture;
- tuân thủ Event Architecture.

Code Generation không được phá vỡ Architecture.

---

# 9. AI Validation

Sau khi sinh mã nguồn, AI phải thực hiện:

- Static Validation
- Build Validation
- Contract Validation
- Architecture Validation
- Dependency Validation

Validation thất bại thì Sprint chưa hoàn thành.

---

# 10. Implementation Evidence

Mỗi Sprint phải sinh đầy đủ:

- Source Code
- Migration
- Test
- Seed Data
- Configuration
- Documentation
- Validation Report
- Review Report

Evidence là một phần của Sprint Output.

---

# 11. Architecture Compliance

AI phải kiểm tra:

- Module Boundary
- Dependency Rules
- Event Contract
- Snapshot Contract
- Security Rules
- Configuration Rules

Không chỉ Build PASS.

---

# 12. AI Output Package

Một Sprint tối thiểu tạo ra:

- Source Code
- Test
- Migration
- API
- Event
- Documentation
- Validation
- Evidence

Không chỉ tạo Source Code.

---

# 13. Human Review

AI không tự phê duyệt.

Human Review xác nhận:

- Business Alignment
- Architecture Compliance
- Sprint Acceptance
- Release Readiness

---

# 14. AI Rules

AI-001 — Repository Discovery là bắt buộc.

AI-002 — Sprint Contract là bất biến.

AI-003 — Không sửa ngoài Scope.

AI-004 — Không thay đổi Architecture.

AI-005 — Không tạo Business Object mới.

AI-006 — Không thay đổi Registry.

AI-007 — Mọi thay đổi kiến trúc phải tạo ACP.

AI-008 — Mọi Sprint phải sinh Evidence.

AI-009 — Validation là bắt buộc.

AI-010 — Human Review là bước cuối cùng.

---

# 15. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-1501 | Repository Discovery hoàn thành |
| ACC-1502 | Sprint Contract được tuân thủ |
| ACC-1503 | Không vượt Scope |
| ACC-1504 | Dependency hợp lệ |
| ACC-1505 | Kiến trúc không bị thay đổi |
| ACC-1506 | Validation hoàn thành |
| ACC-1507 | Test đầy đủ |
| ACC-1508 | Evidence đầy đủ |
| ACC-1509 | ACP được tạo nếu cần |
| ACC-1510 | Human Review hoàn thành |

---

# 16. AI Resolution Pipeline (AIRP)

```text
Sprint Contract
        │
        ▼
Repository Discovery
        │
        ▼
Architecture Resolution
        │
        ▼
Implementation Planning
        │
        ▼
Code Generation
        │
        ▼
Validation Resolution
        │
        ▼
Evidence Generation
        │
        ▼
Human Review
        │
        ▼
Sprint Completion
```

AIRP là Pipeline chuẩn cho mọi AI Coding Assistant.

---

# 17. Relationship to Other Baselines

AI Implementation Architecture liên kết với:

- YADF
- ABP-00 ~ ABP-14
- DIP
- ESP
- SGP
- VAP
- ORP
- CIP

Đây là tài liệu chuyển đổi từ kiến trúc sang triển khai.

---

# 18. Document Status

**Status: FROZEN**

ABP-15 là tài liệu nền tảng quy định kiến trúc triển khai bằng AI của nền tảng YSim.

Mọi AI Coding Assistant, Sprint và quy trình phát triển phải tuân thủ tài liệu này.

---


---

# Source: AFM-01

- Path: `docs/AFM/AFM-01.md`
- Set: `AFM`
- Version: `2.1`
- Status: `FROZEN`

# AI Factory Framework v2.1 Update

## AFM-01

---

# 1. Purpose

AFM-01 mô tả các thay đổi kiến trúc và phương pháp phát triển được bổ sung trong YSim AI Software Factory v2.1.

Đây là tài liệu cập nhật cho AFM-00.

AFM-01 không thay thế AFM-00.

AFM-01 chỉ mô tả các Capability và nguyên tắc mới được bổ sung trước khi triển khai Development & Implementation Pack (DIP).

---

# 2. Objectives

Version 2.1 được phát hành nhằm:

- hoàn thiện mô hình Sprint-Driven Development;
- bổ sung Full-stack Capability Delivery;
- bổ sung Commerce Experience Platform (CXP);
- chuẩn hóa Frontend Engineering;
- tăng khả năng kiểm thử trực tiếp sau mỗi Sprint.

Version 2.1 không thay đổi kiến trúc nền tảng của AI Factory.

---

# 3. Major Enhancements

YSim AI Software Factory v2.1 bổ sung các nhóm năng lực sau:

| Enhancement | Description |
|-------------|-------------|
| Full-stack Capability Delivery | Backend và Frontend được phát triển trong cùng một Sprint |
| Capability Demonstration Model | Mỗi Capability phải có giao diện kiểm thử trực tiếp |
| Commerce Experience Platform (CXP) | Business Domain mới phục vụ Storefront và Digital Commerce |
| Unified Inheritance Framework | Chuẩn hóa cơ chế kế thừa theo Organization |
| Frontend Engineering Standards | Chuẩn hóa kiến trúc và quy tắc phát triển Frontend |

---

# 4. Full-stack Capability Delivery

Từ phiên bản 2.1, một Sprint không còn chỉ triển khai Backend.

Mỗi Sprint phải tạo ra một Capability hoàn chỉnh gồm:

```text
Business Capability

↓

Backend Services

↓

API & Events

↓

Frontend Experience

↓

Seed Data

↓

Verification

↓

Demonstration

↓

Operational Evidence
```

Backend và Frontend được phát triển đồng thời trên cùng một Capability.

---

# 5. Capability Demonstration Model

Mỗi Capability phải có một **Capability Demonstration Surface (CDS)**.

CDS là giao diện tối thiểu cho phép:

- kiểm thử nghiệp vụ;
- xác nhận API;
- kiểm tra Permission;
- trình diễn kết quả Sprint;
- nghiệm thu từng Capability.

Capability chỉ được coi là hoàn thành khi có thể được kiểm thử trực tiếp.

---

# 6. Commerce Experience Platform (CXP)

Version 2.1 bổ sung Business Domain mới:

**Commerce Experience Platform (CXP)**

CXP cung cấp:

- Store Management
- Theme Engine
- Landing Builder
- Storefront Runtime
- Publishing Service
- Checkout Experience
- Payment Offering
- Campaign Management
- Tracking & Analytics
- SEO Management

CXP là nền tảng giúp đối tác có thể tạo và vận hành website bán hàng trực tiếp trên YSim mà không phụ thuộc vào nền tảng thương mại điện tử bên ngoài.

---

# 7. Payment Experience Model

Version 2.1 chuẩn hóa mô hình Payment Experience.

Frontend không hiển thị Gateway.

Frontend hiển thị Payment Offering.

Ví dụ:

- Credit Card
- PayPal
- Apple Pay
- Google Pay
- Alipay
- WeChat Pay
- Bank QR

Gateway và Merchant được lựa chọn bởi Payment Orchestrator theo cấu hình của Organization.

---

# 8. Unified Inheritance Framework

Version 2.1 mở rộng mô hình kế thừa theo Organization.

Các đối tượng có thể:

- Override
- Inherit

từ Parent Organization.

Áp dụng cho:

- Pricing
- Payment Profile
- Theme
- Notification
- Feature Configuration
- Store Configuration

Framework sử dụng cùng một nguyên tắc kế thừa trên toàn bộ hệ thống.

---

# 9. Frontend Architecture

Frontend trở thành một phần chính thức của AI Factory.

Monorepo tối thiểu gồm:

```text
apps/

api/

worker/

scheduler/

admin-portal/

agency-portal/

customer-portal/

storefront-runtime/

developer-portal/
```

Frontend phải tuân thủ cùng Architecture và Engineering Standards như Backend.

---

# 10. Sprint Delivery Model

Một Sprint của Version 2.1 bao gồm:

```text
Planning

↓

Backend

↓

Frontend

↓

Integration

↓

Seed Data

↓

Capability Demonstration

↓

Verification

↓

Release
```

Không được phép hoàn thành Sprint khi chưa có Demonstration.

---

# 11. Definition of Done

Version 2.1 mở rộng Definition of Done thành bốn nhóm:

- Technical Done
- Business Done
- Demonstration Done
- Operational Done

Demonstration Done là yêu cầu bắt buộc đối với mọi Capability có giao diện người dùng.

---

# 12. AI Working Model

AI Agent phải:

- triển khai Backend và Frontend đồng thời;
- sử dụng API Contract thống nhất;
- sinh Seed Data;
- tạo Demonstration Scenario;
- tạo đầy đủ Verification Evidence.

AI không được hoàn thành Sprint chỉ với Source Code Backend.

---

# 13. Relationship to Other Documents

AFM-01 cập nhật các bộ tài liệu sau:

- BRD
- YADF
- ABP
- AAP
- SGP
- ESP

Các bộ tài liệu này sẽ được cập nhật trong Version 2.1 trước khi bắt đầu Development & Implementation Pack (DIP).

---

# 14. Migration Strategy

Version 2.1 là bản cập nhật không phá vỡ (Non-breaking Update).

Tất cả tài liệu Version 2.0 vẫn có hiệu lực.

Các tài liệu Version 2.1 chỉ bổ sung các Capability còn thiếu và mở rộng phạm vi của AI Software Factory.

---

# 15. Framework Status

Sau Version 2.1, AI Factory bao gồm:

```text
AFM
AI Factory Manual

↓

BRD
Business Knowledge

↓

YADF
Architecture & Domain Foundation

↓

ABP
Architecture Blueprint

↓

AAP
AI Collaboration

↓

SGP
Sprint Governance

↓

ESP
Engineering Standards

↓

DIP
Development & Implementation

↓

VAP
Verification & Acceptance

↓

ROP
Release & Operations
```

Framework đã sẵn sàng để bước vào giai đoạn triển khai Development & Implementation Pack.

---

# 16. Document Status

**Status: FROZEN**

AFM-01 là tài liệu công bố chính thức các thay đổi của YSim AI Software Factory Version 2.1.

Mọi tài liệu được cập nhật sau AFM-01 phải tuân thủ các nguyên tắc được định nghĩa trong tài liệu này.

---


---

# Source: DIP-03

- Path: `docs/DIP/DIP-03.md`
- Set: `DIP`
- Version: `2.1`
- Status: `FROZEN`

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


---

# Source: DIP-07

- Path: `docs/DIP/DIP-07.md`
- Set: `DIP`
- Version: `2.1`
- Status: `FROZEN`

# Repository Workflow & Git Strategy Standard

## DIP-07

---

# 1. Purpose

Repository Workflow & Git Strategy Standard định nghĩa quy trình quản lý Source Code, Branch, Commit, Merge và Release trong suốt vòng đời triển khai của YSim AI Software Factory.

Tiêu chuẩn này bảo đảm mọi thay đổi do AI Coding Agent hoặc Developer tạo ra đều có khả năng truy vết, khôi phục và kiểm toán.

Repository Workflow là cầu nối giữa AI Execution Runtime và Software Delivery Pipeline.

---

# 2. Position in Software Factory

```text
Executable Sprint Package

↓

AI Execution Runtime

↓

Repository Workflow

↓

Git Repository

↓

CI/CD

↓

Release
```

Repository là Source of Truth của Source Code.

---

# 3. Objectives

Repository Workflow nhằm:

- chuẩn hóa Git Strategy;
- hỗ trợ AI Coding;
- hỗ trợ Resume;
- hỗ trợ Rollback;
- giảm Merge Conflict;
- tăng khả năng Audit;
- tăng khả năng Release Automation.

---

# 4. Principles

Repository Workflow tuân thủ:

- Repository First
- One Sprint One Scope
- Commit Frequently
- Small Increment
- Traceable
- Reversible
- Repeatable
- Automation Friendly
- AI Friendly

---

# 5. Repository Structure

Repository phải tuân thủ cấu trúc chuẩn của YSim.

Ví dụ:

```text
apps/
packages/
database/
docs/
scripts/
infrastructure/
ai/
```

AI không được tự ý thay đổi cấu trúc Repository đã được đóng băng.

---

# 6. Working Tree Policy

Trước khi bắt đầu Sprint:

Runner phải kiểm tra:

- Working Tree sạch.
- Không có Merge đang mở.
- Không có Rebase chưa hoàn tất.
- Không có Conflict.

Nếu Repository không sạch, Sprint phải dừng.

---

# 7. Branch Strategy

Branch mặc định:

```text
main
```

Branch triển khai:

```text
feature/s03-identity

feature/s14-product

feature/s19-cxp-store-builder
```

Branch sửa lỗi:

```text
hotfix/payment-timeout
```

Branch phát hành:

```text
release/v2.1.0
```

---

# 8. Sprint Branch

Mỗi Sprint nên có Branch riêng.

Ví dụ:

```text
feature/s11-identity

↓

Commit

↓

Review

↓

Merge

↓

Delete Branch
```

Không triển khai nhiều Sprint trên cùng một Branch.

---

# 9. Commit Strategy

Khuyến nghị Commit theo từng Task.

Ví dụ:

```text
chore(s11): repository discovery

feat(s11): identity entities

feat(s11): authentication api

feat(s11): login frontend

test(s11): identity verification

docs(s11): sprint evidence
```

Commit phải nhỏ, rõ ràng và có khả năng Rollback.

---

# 10. Commit Rules

Commit Message gồm:

- Type
- Sprint ID
- Capability
- Description

Ví dụ:

```text
feat(s14): implement product pricing api
```

Không sử dụng:

```text
update
fix
test
misc
```

làm Commit Message đơn lẻ.

---

# 11. Merge Policy

Merge chỉ được phép khi:

- Validation PASS
- Evidence đầy đủ
- Acceptance PASS
- Không có Conflict

Merge phải được thực hiện sau Review.

---

# 12. Tagging Strategy

Release Tag:

```text
v2.1.0
```

Sprint Tag (tùy chọn):

```text
s11-complete
```

Tag phải trỏ tới Commit đã được Acceptance.

---

# 13. Rollback Strategy

Rollback có thể thực hiện theo:

- Commit
- Task
- Sprint
- Release

Rollback không được làm mất Evidence.

---

# 14. Resume Strategy

Runner phải sử dụng:

```text
runtime/state.json
```

để Resume.

Resume không tạo Commit mới cho Task đã PASS.

---

# 15. Conflict Resolution

Nếu xảy ra:

- Merge Conflict
- Repository Conflict
- Protected File Conflict

Runner phải:

- dừng Sprint;
- lưu Conflict Report;
- không Commit.

Nếu Conflict liên quan Architecture:

→ tạo ACP.

---

# 16. Protected Areas

AI không được sửa trực tiếp:

```text
docs/frozen/

architecture/

release/

database/history/
```

Trừ khi Sprint cho phép rõ ràng.

---

# 17. Repository Validation

Trước Commit:

Runner phải kiểm tra:

- Build
- Tests
- Lint
- File Structure
- Naming
- Manifest

Validation FAIL → không Commit.

---

# 18. Release Workflow

```text
Feature Branch

↓

Validation

↓

Evidence

↓

Acceptance

↓

Merge

↓

Release Branch

↓

Tag

↓

Production
```

---

# 19. Repository Rules

REPO-001 — Repository là Source of Truth.

REPO-002 — Mỗi Sprint một Branch.

REPO-003 — Commit theo Task.

REPO-004 — Merge sau Acceptance.

REPO-005 — Tag sau Release.

REPO-006 — Resume phải an toàn.

REPO-007 — Không Commit khi Validation FAIL.

REPO-008 — Protected Files không được sửa.

REPO-009 — Rollback phải giữ Evidence.

REPO-010 — Repository phải luôn Build được.

---

# 20. Compliance Checklist

| Rule | Validation |
|------|------------|
| RWC-0701 | Working Tree sạch |
| RWC-0702 | Branch đúng chuẩn |
| RWC-0703 | Commit đúng quy tắc |
| RWC-0704 | Validation PASS |
| RWC-0705 | Evidence đầy đủ |
| RWC-0706 | Acceptance PASS |
| RWC-0707 | Merge đúng quy trình |
| RWC-0708 | Rollback khả thi |
| RWC-0709 | Protected Files không bị thay đổi |
| RWC-0710 | Tuân thủ DIP |

---

# 21. Relationship to Other Documents

DIP-07 liên kết với:

- DIP-00 Implementation Constitution
- DIP-01 Executable Sprint Package Standard
- DIP-02 AI Context Resolution & Prompt Assembly Standard
- DIP-03 Seed & Reference Data Standard
- DIP-04 AI Execution Runtime & Bash Runner Standard
- DIP-05 AI Prompt Orchestration & Task Assembly Standard
- DIP-06 Validation, Evidence & Acceptance Standard
- SGP Sprint Governance Pack
- ESP Engineering Standards Pack
- ROP Release & Operations Pack

DIP-07 là tiêu chuẩn chính thức cho Repository Workflow và Git Strategy của YSim AI Software Factory.

---

# 22. Repository Lifecycle

```text
Sprint Planning

↓

Create Branch

↓

Repository Validation

↓

AI Execution

↓

Task Commit

↓

Validation

↓

Evidence

↓

Acceptance

↓

Merge

↓

Tag

↓

Release
```

Repository Lifecycle là quy trình chuẩn áp dụng cho mọi Sprint.

---

# 23. Document Status

**Status: FROZEN**

Từ phiên bản 2.1, mọi Sprint của YSim phải tuân thủ Repository Workflow và Git Strategy theo tiêu chuẩn của DIP-07.

Repository là Source of Truth cho Source Code. Mọi thay đổi phải được thực hiện thông qua Branch, Commit, Validation, Evidence và Acceptance nhằm bảo đảm khả năng truy vết, khôi phục và tự động hóa toàn bộ quy trình triển khai.


---

# Source: DIP-08

- Path: `docs/DIP/DIP-08.md`
- Set: `DIP`
- Version: `2.1`
- Status: `FROZEN`

# Full-stack Capability Delivery Standard

## DIP-08

---

# 1. Purpose

Full-stack Capability Delivery Standard định nghĩa phương pháp triển khai một Business Capability hoàn chỉnh trong YSim AI Software Factory.

Capability là đơn vị triển khai chuẩn của toàn bộ nền tảng.

Không triển khai Backend riêng.

Không triển khai Frontend riêng.

Không triển khai API riêng.

Một Sprint phải hoàn thành toàn bộ Capability.

---

# 2. Position in Software Factory

```text
Business Capability

↓

Implementation Planning

↓

Backend

+

API

+

Frontend

+

Experience

+

Seed

+

Demonstration

↓

Validation

↓

Acceptance
```

Capability là Deliverable của Sprint.

---

# 3. Objectives

Tiêu chuẩn này nhằm:

- triển khai theo Capability;
- giảm Integration Gap;
- giảm Late Testing;
- tăng khả năng Demonstration;
- tăng tốc Feedback;
- giảm Technical Debt.

---

# 4. Principles

Capability Delivery tuân thủ:

- Capability First
- Backend + Frontend Together
- Demonstration First
- Incremental Delivery
- Continuous Validation
- User Journey Oriented
- Experience Driven
- Testable by Design
- Deployable by Design

---

# 5. Capability Definition

Một Capability tối thiểu gồm:

- Business Rules
- Database
- Domain Model
- Repository
- API
- Backend Service
- Frontend
- Experience API
- UI Components
- Seed Data
- Demonstration
- Tests
- Documentation

Không được thiếu bất kỳ thành phần bắt buộc nào.

---

# 6. Capability Structure

```text
Capability

├── Business Rules

├── Domain

├── Persistence

├── API

├── Backend

├── Integration

├── Experience API

├── Frontend

├── Design System

├── Demonstration

├── Tests

└── Documentation
```

---

# 7. Sprint Deliverables

Một Sprint phải sinh:

## Backend

- Entity
- Repository
- Service
- Controller
- Events

---

## API

- REST API
- OpenAPI
- Contract Test

---

## Frontend

- Pages
- Components
- Forms
- Validation
- Routing

---

## Experience

- Experience API
- User Journey
- Storefront (nếu có)
- Dashboard (nếu có)

---

## Data

- Migration
- Seed
- Demo Data

---

## Quality

- Tests
- Validation
- Evidence

---

# 8. Frontend Requirement

Capability có UI phải cung cấp:

- Navigation
- CRUD
- Search
- Error Handling
- Loading State
- Empty State
- Success State
- Permission State

Frontend không chỉ dùng để Demo.

Frontend là Deliverable chính thức.

---

# 9. Experience API

Frontend không được gọi trực tiếp nhiều Business API.

Experience API chịu trách nhiệm:

- Aggregation
- Composition
- Read Model
- User Journey

Experience API là một phần của Capability.

---

# 10. Capability Demonstration

Sau Sprint phải Demonstrate được.

Ví dụ:

Identity

↓

Login

↓

Dashboard

↓

Logout

hoặc

Product

↓

Create

↓

Edit

↓

Publish

↓

Search

↓

Delete

Demonstration phải chạy được.

---

# 11. Capability Completion

Capability chỉ COMPLETE khi:

✓ Backend PASS

✓ API PASS

✓ Frontend PASS

✓ Demonstration PASS

✓ Tests PASS

✓ Documentation PASS

✓ Evidence PASS

---

# 12. Sprint Flow

```text
Business

↓

Planning

↓

Backend

↓

API

↓

Frontend

↓

Seed

↓

Experience

↓

Testing

↓

Demonstration

↓

Acceptance
```

---

# 13. Design System Integration

Frontend phải sử dụng:

- Shared Components
- Shared Theme
- Shared Tokens

Không được tạo UI Framework riêng.

---

# 14. Multi-channel Delivery

Capability có thể phục vụ:

- Admin Portal
- Merchant Portal
- Customer Portal
- Storefront
- Landing Page
- Mobile App
- Public API

Backend không phụ thuộc Channel.

---

# 15. Capability Evidence

Evidence tối thiểu:

- Build
- Tests
- Screenshots
- API Results
- Prompt
- Logs
- Validation
- Demonstration

---

# 16. Capability Rules

CAP-001 — Sprint triển khai theo Capability.

CAP-002 — Backend và Frontend triển khai cùng Sprint.

CAP-003 — Experience API là bắt buộc nếu Capability có UI.

CAP-004 — Demonstration là Deliverable.

CAP-005 — Seed là Deliverable.

CAP-006 — Tests là Deliverable.

CAP-007 — Documentation là Deliverable.

CAP-008 — Evidence là Deliverable.

CAP-009 — Design System phải được sử dụng.

CAP-010 — Capability chỉ COMPLETE sau Acceptance.

---

# 17. Compliance Checklist

| Rule | Validation |
|------|------------|
| CDC-0801 | Backend đầy đủ |
| CDC-0802 | API đầy đủ |
| CDC-0803 | Frontend đầy đủ |
| CDC-0804 | Experience API đầy đủ |
| CDC-0805 | Seed đầy đủ |
| CDC-0806 | Demonstration PASS |
| CDC-0807 | Documentation đầy đủ |
| CDC-0808 | Evidence đầy đủ |
| CDC-0809 | Acceptance PASS |
| CDC-0810 | Tuân thủ DIP |

---

# 18. Relationship to Other Documents

DIP-08 liên kết với:

- DIP-00
- DIP-01
- DIP-02
- DIP-03
- DIP-04
- DIP-05
- DIP-06
- DIP-07

và:

- BRD
- ABP
- ESP
- SGP
- ROP

DIP-08 là tiêu chuẩn triển khai Capability của YSim AI Software Factory.

---

# 19. Capability Lifecycle

```text
Capability Defined

↓

Sprint Planned

↓

Context Loaded

↓

AI Coding

↓

Validation

↓

Demonstration

↓

Acceptance

↓

Released
```

---

# 20. Document Status

**Status: FROZEN**

Từ phiên bản 2.1, mọi Sprint của YSim phải triển khai theo mô hình **Full-stack Capability Delivery**.

Capability là đơn vị triển khai, nghiệm thu và phát hành chính thức của nền tảng.

Không chấp nhận Sprint chỉ hoàn thành Backend, API hoặc Frontend riêng lẻ.


---

# Source: DIP-10

- Path: `docs/DIP/DIP-10.md`
- Set: `DIP`
- Version: `2.1`
- Status: `FROZEN`

# DIP-10 — Implementation Roadmap & Capability Matrix

---

# 1. Purpose

This document defines the official implementation roadmap for the YSim AI Software Factory.

It provides the master execution plan for all implementation phases, sprint sequencing, capability dependencies and release milestones.

The roadmap serves as the primary planning reference for:

- Architecture Implementation
- Sprint Planning
- Capability Planning
- AI Execution Planning
- Release Planning
- Resource Allocation

This document is the authoritative implementation roadmap for the platform.

---

# 2. Objectives

The objectives of this roadmap are to:

- establish the implementation sequence;
- minimize capability dependency conflicts;
- standardize sprint planning;
- support AI-driven execution;
- enable incremental capability delivery;
- support parallel development where applicable.

---

# 3. Delivery Philosophy

YSim adopts a Capability-driven Delivery Model.

Every sprint delivers one or more complete business capabilities.

A capability always includes:

- Backend
- API
- Frontend
- Experience Layer
- Seed Data
- Demonstration
- Testing
- Documentation
- Evidence

The implementation unit is the **Business Capability**, not an individual technical layer.

---

# 4. Overall Delivery Model

```text
Business Capability
        │
        ▼
Executable Sprint Package (ESPK)
        │
        ▼
AI Runtime
        │
        ▼
Implementation
        │
        ▼
Validation
        │
        ▼
Capability Demonstration
        │
        ▼
Acceptance
        │
        ▼
Release
```

---

# 5. Implementation Phases

## Phase 0 — Factory Commissioning

| Sprint | Capability |
|---------|------------|
| S00 | Factory Commissioning & Repository Bootstrap |

---

## Phase 1 — Platform Foundation

| Sprint | Capability |
|---------|------------|
| S01 | Platform Foundation |
| S02 | Configuration & Infrastructure |

---

## Phase 2 — Identity Platform

| Sprint | Capability |
|---------|------------|
| S03 | Identity, Authentication & Access Control |
| S04 | Organization, Tenant & Inheritance |

---

## Phase 3 — Commerce Foundation

| Sprint | Capability |
|---------|------------|
| S05 | Product Catalog |
| S06 | Pricing & Commercial Rules |

---

## Phase 4 — Commerce Experience Platform (CXP)

| Sprint | Capability |
|---------|------------|
| S07 | Commerce Experience Platform Foundation |
| S08 | Store Builder, Theme Engine & Publishing |
| S09 | Checkout, Payment Offering & Payment Routing |

---

## Phase 5 — Sales & Order Management

| Sprint | Capability |
|---------|------------|
| S10 | Customer, Cart & Quote |
| S11 | Sales Order |
| S12 | Fulfillment |

---

## Phase 6 — Partner Platform

| Sprint | Capability |
|---------|------------|
| S13 | Partner, Agency & Commission |

---

## Phase 7 — Inventory Platform

| Sprint | Capability |
|---------|------------|
| S14 | Inventory, Resource & eSIM Stock |

---

## Phase 8 — Financial Platform

| Sprint | Capability |
|---------|------------|
| S15 | Billing |
| S16 | Payment |
| S17 | Financial Event, Ledger & Settlement |

---

## Phase 9 — CRM Platform

| Sprint | Capability |
|---------|------------|
| S18 | CRM & Customer Care |

---

## Phase 10 — Analytics Platform

| Sprint | Capability |
|---------|------------|
| S19 | Analytics & Operational Intelligence |

---

## Phase 11 — Platform Operations

| Sprint | Capability |
|---------|------------|
| S20 | Platform Operations Center |
| S21 | Reporting & Business Intelligence |
| S22 | Monitoring & Health Platform |
| S23 | Scheduler & Background Jobs |

---

# 6. Capability Delivery Matrix

| Sprint | Backend | API | Frontend | Seed | Demo | Tests | Evidence |
|---------|----------|------|-----------|------|------|--------|-----------|
| S00 | ✓ | - | - | ✓ | - | ✓ | ✓ |
| S01 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S02 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S03 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S04 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S05 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S06 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S07 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S08 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S09 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S10-S23 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

Every sprint from **S01 onward** shall follow the Full-stack Capability Delivery Standard defined in **DIP-08**.

---

# 7. Capability Dependency Graph

```text
Platform Foundation
        │
        ▼
Identity
        │
        ▼
Organization
        │
        ▼
Configuration
        │
        ▼
Product
        │
        ▼
Pricing
        │
        ▼
Commerce Experience Platform
        │
        ▼
Checkout
        │
        ▼
Sales Order
        │
        ▼
Fulfillment
        │
        ▼
Billing
        │
        ▼
Settlement
```

AI Runtime shall respect this dependency graph during implementation planning.

---

# 8. Parallel Development

Capabilities may be implemented in parallel only when:

- no direct dependency exists;
- they belong to different business domains;
- they do not modify the same bounded context;
- repository conflicts are avoided.

Example:

```text
CRM
      ||
Analytics
      ||
Operations
```

---

# 9. Release Strategy

Releases are based on **Capability Groups**, not individual sprints.

| Release | Included Capability Groups |
|----------|---------------------------|
| Alpha | Platform Foundation + Identity |
| Beta | Commerce Foundation |
| RC | Commerce Experience Platform |
| GA | Full Platform |

---

# 10. Exit Criteria

A capability is considered completed only when:

- Backend implementation is complete.
- API contracts are validated.
- Frontend is operational.
- Experience Layer is available.
- Seed Data is generated.
- Demonstration succeeds.
- Tests pass.
- Documentation is updated.
- Evidence package is complete.
- Acceptance is approved.

---

# 11. Relationship to Other Documents

This roadmap is governed by:

- AFM-00 — Architecture Freeze Manifest
- BRD Series
- ABP Series
- YADF-00
- AAP Series
- SGP Series
- ESP Series
- DIP-00 → DIP-09
- ROP Series

This document serves as the implementation planning bridge between the Development & Implementation Framework and the Executable Sprint Packages (ESPK).

---

# 12. Future Delivery Model

Beginning with **YSim v2.1**, capability implementation shall transition from documentation-driven delivery to **Executable Sprint Packages (ESPK)**.

The relationship is defined as follows:

```text
DIP
        │
        ▼
Implementation Framework
        │
        ▼
Executable Sprint Package (ESPK)
        │
        ▼
AI Runtime
        │
        ▼
Codex / AI Coding Agent
        │
        ▼
Capability Delivery
```

DIP defines **how** implementation is performed.

ESPK defines **what** is implemented.

---

# 13. Architecture Decision

The Development & Implementation Pack (DIP) is officially frozen at version **2.1**.

The DIP consists of:

- DIP-00 — Implementation Constitution
- DIP-01 — Executable Sprint Package Standard
- DIP-02 — AI Context Resolution & Prompt Assembly Standard
- DIP-03 — Seed & Reference Data Standard
- DIP-04 — AI Execution Runtime & Bash Runner Standard
- DIP-05 — AI Prompt Orchestration & Task Assembly Standard
- DIP-06 — Validation, Evidence & Acceptance Standard
- DIP-07 — Repository Workflow & Git Strategy Standard
- DIP-08 — Full-stack Capability Delivery Standard
- DIP-09 — AI Execution Governance & Exception Handling Standard
- DIP-10 — Implementation Roadmap & Capability Matrix

Subsequent implementation work shall be delivered as **Executable Sprint Packages (ESPK)** rather than additional DIP capability documents.

---

# 14. Document Status

**Status:** FROZEN

This document establishes the official implementation roadmap for the YSim AI Software Factory v2.1.

All implementation activities shall comply with this roadmap unless superseded by an approved Architecture Change Proposal (ACP).


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

# Source: ESP-03

- Path: `docs/ESP/ESP-03.md`
- Set: `ESP`
- Version: `2.1`
- Status: `FROZEN`

# Enterprise Naming Standards

## ESP-03

---

# 1. Purpose

Enterprise Naming Standards định nghĩa hệ thống quy tắc đặt tên thống nhất cho toàn bộ nền tảng YSim.

Tiêu chuẩn này áp dụng cho:

- Business Objects
- Business Capabilities
- Domains
- Modules
- Applications
- APIs
- Events
- Snapshots
- Source Code
- Database Objects
- Configuration
- Infrastructure
- AI Artifacts
- Documentation
- Frontend
- Design System
- Experience Components

Naming là ngôn ngữ chung của toàn bộ Platform.

---

# 2. Objectives

Enterprise Naming nhằm:

- Chuẩn hóa ngôn ngữ kỹ thuật.
- Tăng khả năng đọc hiểu.
- Tăng khả năng tìm kiếm.
- Hỗ trợ AI Repository Discovery.
- Hỗ trợ Traceability.
- Giảm trùng lặp thuật ngữ.

---

# 3. Naming Principles

Tên phải:

- Meaningful
- Consistent
- Domain Driven
- Business Aligned
- Technology Neutral
- Predictable
- Search Friendly
- AI Friendly
- Full-stack Consistency
- Experience-aware Naming

Tên không được phụ thuộc vào cá nhân.

---

# 4. Enterprise Naming Hierarchy

Naming được chuẩn hóa theo thứ tự:

```text
Business Domain
        │
Business Capability
        │
Business Object
        │
Module
        │
Component
        │
Class
        │
Method
        │
Variable
```

Tên ở tầng dưới phải phản ánh đúng tầng trên.

---

# 5. Language Standards

Toàn bộ tên phải sử dụng:

- English
- Singular form (đối với Business Object và Entity)
- PascalCase, camelCase hoặc kebab-case theo từng loại Artifact

Không sử dụng:

- tiếng Việt;
- viết tắt nội bộ;
- tên không có nghĩa.

---

# 6. Business Naming

Business Object:

```text
Customer
Order
Payment
Settlement
Partner
Agency
Package
Activation
```

Không sử dụng:

```text
CustomerData
OrderInfo
PackageObject
```

Business Object chỉ sử dụng danh từ.

---

# 7. Capability Naming

Capability sử dụng:

```text
Customer Management

Payment Processing

Package Catalog

Settlement Management
```

Capability sử dụng:

> Noun + Action

hoặc

> Business Function

Không sử dụng tên mang tính kỹ thuật.

---

# 8. Module Naming

Module sử dụng:

```text
customer

payment

pricing

settlement

notification
```

Quy tắc:

- lowercase
- singular
- kebab-case nếu nhiều từ

Ví dụ:

```text
customer-care

payment-gateway

partner-management
```

---

# 8A. Frontend & Experience Naming

Frontend được chuẩn hóa theo Capability.

Ví dụ:

```text
pages/

login/

product-catalog/

checkout/

order-history/
```

Component:

```text
ProductCard

CheckoutSummary

PaymentMethodSelector

OrderStatusBadge
```

Design System:

```text
Button

Input

Modal

Toast

ThemeProvider
```

Capability Demonstration:

```text
demo-login

demo-checkout

demo-payment

demo-order
```

Tên phải phản ánh đúng Business Capability, không phụ thuộc Framework hoặc UI Library.


---

# 9. Application Naming

Applications sử dụng:

```text
portal

admin

api

agency

worker

scheduler
```

Không đặt tên theo công nghệ.

Ví dụ:

❌ nest-api

❌ node-api

---

# 10. Package Naming

Packages:

```text
core

shared

contracts

events

utils

sdk
```

Package Name phải phản ánh chức năng.

---

# 11. Class Naming

Class:

- PascalCase

Ví dụ:

```text
CustomerService

CreateOrderUseCase

PaymentRepository

SettlementEvent
```

Không sử dụng:

```text
customerService

Customer_Service

ServiceCustomer
```

---

# 12. Interface Naming

Interface:

```text
PaymentGateway

CustomerRepository

NotificationProvider
```

Không thêm tiền tố:

```text
IPayment

ICustomerRepository
```

Trừ khi ngôn ngữ/framework bắt buộc.

---

# 13. Method Naming

Method:

- camelCase
- Verb + Object

Ví dụ:

```text
createOrder()

activateEsim()

calculatePrice()

findCustomer()

sendNotification()
```

Không sử dụng:

```text
doIt()

process()

run()

executeTask()
```

trừ khi đó là tên chuẩn của Framework hoặc Pattern.

---

# 14. Variable Naming

Variable:

- camelCase

Ví dụ:

```text
customerId

paymentAmount

activationResult

orderStatus
```

Không sử dụng:

```text
tmp

data

obj

var1
```

ngoại trừ biến lặp ngắn trong phạm vi rất nhỏ (`i`, `j`, `item`) khi ngữ cảnh rõ ràng.

---

# 15. Constant Naming

Constant:

```text
MAX_RETRY_COUNT

DEFAULT_TIMEOUT

SYSTEM_USER
```

Toàn bộ viết:

UPPER_SNAKE_CASE

---

# 16. API Naming

Endpoint:

```text
GET /customers

POST /orders

POST /payments

GET /packages
```

Quy tắc:

- lowercase
- plural resource
- kebab-case nếu nhiều từ

Ví dụ:

```text
/partner-orders

/customer-profiles
```

---

# 17. Event Naming

Event:

```text
OrderCreated

PaymentSucceeded

PackageAssigned

SettlementCompleted
```

Pattern:

```text
BusinessObject + PastTenseVerb
```

---

# 18. Snapshot Naming

Snapshot:

```text
CustomerSnapshot

PackageSnapshot

SettlementSnapshot
```

Pattern:

```text
BusinessObject + Snapshot
```

---

# 19. Database Naming

Table:

```text
customers

orders

payments

packages
```

Primary Key:

```text
id
```

Foreign Key:

```text
customer_id

order_id

package_id
```

Index:

```text
idx_customer_phone

idx_order_status
```

Unique Constraint:

```text
uk_partner_code
```

---

# 20. Configuration Naming

Environment Variable:

```text
DATABASE_URL

REDIS_URL

JWT_SECRET

ONEPAY_API_KEY
```

Toàn bộ:

UPPER_SNAKE_CASE

---

# 21. AI Artifact Naming

AI Workspace:

```text
SPR-017.yaml

verification-report.md

evidence.json

planning-report.md
```

Tên phải phản ánh loại Artifact và mục đích sử dụng.

Capability Demonstration:

```text
demo-login.md

demo-checkout.md

demo-order-payment.md
```

Screenshot:

```text
login-page.png

checkout-page.png

payment-success.png
```


---

# 22. Prohibited Naming

Không sử dụng:

- temp
- test1
- data
- object
- abc
- xyz
- newCustomer2
- finalVersion
- tmp

Tên phải có ý nghĩa nghiệp vụ hoặc kỹ thuật rõ ràng.

---

# 23. Naming Rules

NS-001 — Toàn bộ tên sử dụng tiếng Anh.

NS-002 — Business Object sử dụng danh từ số ít.

NS-003 — Method sử dụng Verb + Object.

NS-004 — Event sử dụng BusinessObject + PastTenseVerb.

NS-005 — Snapshot sử dụng BusinessObject + Snapshot.

NS-006 — API sử dụng resource dạng số nhiều.

NS-007 — Không sử dụng viết tắt nội bộ.

NS-008 — Không sử dụng tên mơ hồ.

NS-009 — Naming phải thống nhất trên toàn Platform.

NS-010 — AI phải tuân thủ Enterprise Naming Standards.

NS-011 — Frontend Page, Component và Route phải đặt tên theo Business Capability.

NS-012 — Capability Demonstration Asset phải sử dụng tiền tố `demo-`.


---

# 24. Naming Compliance Checklist

| Rule | Validation |
|------|------------|
| ENC-0301 | Business Naming đúng chuẩn |
| ENC-0302 | Module Naming đúng chuẩn |
| ENC-0303 | Class Naming đúng chuẩn |
| ENC-0304 | Method Naming đúng chuẩn |
| ENC-0305 | Variable Naming đúng chuẩn |
| ENC-0306 | API Naming đúng chuẩn |
| ENC-0307 | Event Naming đúng chuẩn |
| ENC-0308 | Database Naming đúng chuẩn |
| ENC-0309 | Configuration Naming đúng chuẩn |
| ENC-0310 | AI Artifact Naming đúng chuẩn |
| ENC-0311 | Frontend Naming đúng chuẩn |
| ENC-0312 | Demonstration Naming đúng chuẩn |

---

# 25. Relationship to Other Documents

ESP-03 liên kết với:

- BRD Business Object Registry
- BRD Capability Registry
- YADF Meta Model
- ABP-04 Domain Architecture
- ABP-05 Event Architecture
- ESP-01 Repository Architecture Standards
- ESP-02 Source Code Engineering Standards
- ESP-04 API Standards

Enterprise Naming Standards là ngôn ngữ thống nhất giữa Business Architecture, Engineering Architecture, Frontend, Design System và Capability Demonstration.

---

# 26. Document Status

**Status: FROZEN**

ESP-03 là tài liệu chuẩn hóa hệ thống đặt tên của nền tảng YSim.

Mọi Business Artifact, Engineering Artifact và AI Artifact phải tuân thủ Enterprise Naming Standards.

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
