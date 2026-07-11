---
document_code: DIP-05
document_name: AI Prompt Orchestration & Task Assembly Standard
project: YSim v2.1
document_set: Development & Implementation Pack
version: 2.1
status: FROZEN
language: en-US
---

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