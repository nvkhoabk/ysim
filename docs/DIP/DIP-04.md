---
document_code: DIP-04
document_name: AI Execution Runtime & Bash Runner Standard
project: YSim v2.1
document_set: Development & Implementation Pack
version: 2.1
status: FROZEN
language: en-US
---

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