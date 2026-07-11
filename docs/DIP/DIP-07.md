---
document_code: DIP-07
document_name: Repository Workflow & Git Strategy Standard
project: YSim v2.1
document_set: Development & Implementation Pack
version: 2.1
status: FROZEN
language: en-US
---

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