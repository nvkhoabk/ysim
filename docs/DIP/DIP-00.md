---
document_code: DIP-00
document_name: Implementation Constitution & Executable Sprint Model
project: YSim v2.1
document_set: Development & Implementation Pack
version: 2.1
status: FROZEN
language: en-US
---

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