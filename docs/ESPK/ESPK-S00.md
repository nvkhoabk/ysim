---
document_code: ESPK-00
document_name: Factory Commissioning & Repository Bootstrap
project: YSim v2.1
document_set: Sprint
version: 2.1
status: FROZEN
language: vi-VN
---
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