---
document_code: V23-FRAMEWORK-DECISIONS
document_name: YSim v2.3 Framework, Product and Documentation Decision Record
project: YSim Platform
document_set: Baseline Governance
version: 2.0
status: APPROVED
language: vi-VN
baseline: v2.3
last_updated: 2026-07-13
---

# YSim v2.3 Framework, Product and Documentation Decision Record

## 1. Mục đích và hiệu lực

Tài liệu này là nguồn quyết định chuẩn đã được phê duyệt cho việc hiệu chỉnh
BRD/UXF, thiết kế YSim AI Development Framework (YADF) v2.3 và triển khai YSim
v2.3.

Các tài liệu BRD, UXF, architecture, domain, YADF, execution contract, sprint
contract, acceptance contract và công cụ tự động hóa không được mâu thuẫn với
các quyết định tại đây.

Các quyết định này là đầu vào bắt buộc, nhưng không thay thế yêu cầu chi tiết,
acceptance criteria hay traceability trong BRD/UXF.

### 1.1 Quy tắc ưu tiên

Khi có mâu thuẫn, áp dụng thứ tự sau:

1. Quyết định mới hơn và cụ thể hơn trong tài liệu này.
2. Requirement v2.3 đã được phê duyệt trong BRD/UXF.
3. Architecture/domain specification đã được phê duyệt.
4. YADF và execution contract.
5. Manifest, prompt, script và implementation.

Không được tự suy diễn để giải quyết mâu thuẫn có ảnh hưởng nghiệp vụ. Mâu
thuẫn chưa có quyết định phải được ghi vào review register và chặn phần triển
khai liên quan.

### 1.2 Trạng thái quyết định

- Tất cả quyết định trong tài liệu này có trạng thái **APPROVED**.
- `POST_V2.3` có nghĩa là được ghi nhận nhưng không triển khai trong v2.3.
- `SUPERSEDED` có nghĩa là quyết định cũ đã bị quyết định mới hơn thay thế.

---

## 2. Execution Framework Decisions

### FD-01 — Đơn vị triển khai nhỏ nhất

**Quyết định:** Vertical slice chạy được.

Mỗi product increment phải chạy xuyên suốt qua các tầng cần thiết:

```text
User Interface
→ API
→ Application/Domain Logic
→ Persistence/Integration
→ API Response
→ User Interface Result
```

Slice chỉ được coi là hoàn thành khi một hành vi người dùng có giá trị nghiệp
vụ chạy được end-to-end. Thành phần rời rạc, scaffold, mock-only hoặc kiểm tra
schema đơn thuần không được coi là product increment hoàn thành.

### FD-02 — Cổng nghiệm thu giữa các slice

**Quyết định:** Codex không được tự chuyển sang vertical slice tiếp theo khi
slice hiện tại chưa có human acceptance.

Trạng thái tối thiểu:

```text
PLANNED → IMPLEMENTING → VERIFYING → CANDIDATE
→ AWAITING_HUMAN_ACCEPTANCE → ACCEPTED | REJECTED | BLOCKED
```

Chỉ `ACCEPTED` mới cho phép bắt đầu slice kế tiếp, trừ khi Authorized Approver
ghi rõ ngoại lệ bằng văn bản.

### FD-03 — Quyền Git của Codex

**Quyết định:** Trong phạm vi một vertical slice, Codex được tự commit và tạo
tag theo contract.

Codex không được tự thay đổi protected branch, rewrite history, xóa tag đã
phát hành hoặc mở rộng phạm vi slice. Mỗi commit/tag phải truy ngược được tới
slice ID, requirement IDs và evidence bundle.

### FD-04 — Candidate tag và accepted tag

**Quyết định:** Tách biệt candidate và accepted.

- Candidate tag được tạo sau khi kiểm chứng tự động đạt yêu cầu.
- Accepted tag chỉ được tạo sau khi Authorized Approver phê duyệt.
- Accepted tag phải trỏ đúng commit đã được nghiệm thu; nếu có sửa đổi, phải
  tạo candidate mới và nghiệm thu lại.
- Quy ước tên chính xác sẽ được YADF/tag contract định nghĩa; không dùng cùng
  một tag để biểu diễn hai trạng thái.

### FD-05 — Nguồn điều khiển mỗi lần Codex chạy

**Quyết định:** Codex đọc trực tiếp toàn bộ bộ tài liệu áp dụng, còn một
machine-readable Execution Contract là nguồn điều khiển thực thi trực tiếp.

Execution Contract phải tham chiếu phiên bản/hash của document baseline,
requirement set, slice scope, protected paths, lệnh kiểm chứng, evidence bắt
buộc, retry budget và stop conditions. Contract không được thay thế hoặc tóm
lược làm mất nghĩa tài liệu chuẩn.

### FD-06 — Hai môi trường kiểm chứng

**Quyết định:** Mỗi slice phải được kiểm chứng tại working tree và clean
checkout từ candidate commit/tag.

Clean checkout phải chạy bằng quy trình tái tạo được, không phụ thuộc file
untracked, cache cục bộ hoặc state ẩn của phiên Codex.

### FD-07 — Evidence trước human acceptance

**Quyết định:** Evidence bundle bắt buộc gồm runtime, API, dữ liệu và
screenshot.

Tối thiểu phải có:

- Runtime evidence: dịch vụ thực sự khởi động và health/readiness có ý nghĩa.
- API evidence: request/response của happy path và critical failure path.
- Data evidence: state trước/sau và invariant nghiệp vụ liên quan.
- Screenshot evidence: UI thực tế tại checkpoint nghiệm thu, không dùng mock.
- Metadata: commit, tag, môi trường, thời điểm, lệnh chạy và kết quả.

### FD-08 — Ngân sách tự sửa lỗi

**Quyết định:** Codex được tự sửa tối đa hai lần cho một failure cycle.

Sau hai lần không đạt, hệ thống phải chuyển `BLOCKED`, bảo toàn log/evidence,
mô tả nguyên nhân và dừng để con người xem xét. Không được reset bộ đếm bằng
cách đổi tên task hoặc chạy lại cùng một phương án.

### FD-09 — Sprint 00

**Quyết định:** Giữ Sprint 00 riêng, chỉ dùng để commissioning môi trường.

Sprint 00 kiểm chứng toolchain, dependency, container/runtime, secret contract,
clean-checkout reproducibility, evidence capture và Git permissions. Sprint 00
không triển khai product feature và không dùng kết quả giả để chứng minh sản
phẩm chạy được.

### FD-10 — Merge sau nghiệm thu

**Quyết định:** Hệ thống tự merge nhánh vertical slice sau khi phê duyệt hợp
lệ và mọi gate còn hiệu lực đều đạt.

Merge phải fail-closed nếu branch lệch candidate commit, approval không hợp lệ,
CI/evidence hết hiệu lực, conflict xuất hiện hoặc protected-branch policy không
được đáp ứng.

### FD-11 — Authorized Approver

**Quyết định:** Chỉ cần một Authorized Approver có thẩm quyền để phê duyệt một
vertical slice và cho phép tạo accepted tag.

Danh sách người có thẩm quyền phải nằm trong governance configuration được
version-control. Người thực thi tự động không được tự thêm mình vào danh sách.

### FD-12 — Cơ chế phê duyệt Markdown

**Quyết định:** Authorized Approver ký trực tiếp trong file Markdown; hệ thống
chỉ xác thực tên trong file với allowlist.

Approval record tối thiểu phải chứa approver name, slice ID, candidate tag,
candidate commit, decision, timestamp và ghi chú. Cơ chế này là control quy
trình, không phải chữ ký mật mã. Bất kỳ thay đổi nào đối với candidate commit
sau phê duyệt đều làm approval mất hiệu lực.

---

## 3. Product Scope Decisions

### SD-01 — Mục tiêu phát hành

**Quyết định:** v2.3 phải hoàn thiện toàn bộ yêu cầu active đã được phê duyệt
trong BRD và UXF thành một hệ thống có khả năng triển khai production.

Từ “production-ready” phải được chứng minh bằng functional acceptance,
security, accessibility, performance, observability, recoverability,
operability và deployment evidence; không chỉ bằng test tự động báo xanh.

### SD-02 — Future/Deferred

**Quyết định:** Tất cả yêu cầu đang được đánh dấu `Future`, `Deferred` hoặc
`Out of Scope` tiếp tục nằm ngoài phạm vi v2.3, trừ các ngoại lệ được ghi rõ
trong SD-03.

### SD-03 — Các ngoại lệ được đưa vào v2.3

Ba năng lực sau được đưa vào phạm vi v2.3 dù tài liệu cũ có thể chưa xếp active:

1. Recommendation Engine đầy đủ theo rule và behavioral signal; chưa dùng ML.
2. Rule-based Fraud/Risk Engine cho login, checkout và payment; ML để sau.
3. Shared Approval Engine dùng chung cho các nghiệp vụ cần phê duyệt.

### SD-04 — Partner Portal

**Quyết định:** Partner Portal là experience channel riêng dành cho payment
partner và eSIM provider, nhưng có trạng thái `POST_V2.3`.

Trong v2.3, credential/webhook và các tác vụ partner cần thiết được quản lý qua
Platform Admin Portal bằng restricted partner role; partner nhận bộ API
documentation riêng. Không được tuyên bố Partner Portal đã được triển khai.

---

## 4. UXF Decisions

### UXD-01 — Mức đầy đủ của UXF

UXF v2.3 phải đặc tả đầy đủ màn hình, luồng, trạng thái, quyền truy cập,
responsive behavior và acceptance criteria cho tất cả experience channel được
triển khai. Các channel được tổ chức theo shared standards và channel
blueprints; Partner Portal được ghi blueprint/placeholder `POST_V2.3`.

### UXD-02 — Dynamic UI

- Storefront và campaign/landing experience là dynamic UI.
- Portal dùng shell ổn định; cho phép cấu hình navigation, capability, widget,
  dashboard, theme và composition trong giới hạn shell contract.
- Runtime metadata không được phép thay đổi tùy ý critical transaction flow.

### UXD-03 — Storefront, guest và Customer Portal authentication

- Storefront không bắt buộc đăng nhập nhưng hỗ trợ đăng nhập.
- Cross-device saved cart là tính năng sau v2.3.
- Customer Portal luôn yêu cầu đăng nhập.
- Guest checkout luôn bắt buộc primary email; phone hoặc verified IM có thể là
  identity bổ sung cho fulfillment/notification.
- Sau payment success, hệ thống tự provision Customer Portal account và gửi
  activation/magic-link/OTP qua kênh đã xác minh. Không gửi password.
- Account chuyển từ `PROVISIONED` sang `ACTIVE` sau khi hoàn tất verification.

### UXD-04 — IM identity

Tài khoản WhatsApp, Telegram, Zalo OA hoặc connector IM khác có thể là danh
tính đăng nhập độc lập khi connector xác minh được ownership và ánh xạ an toàn
tới canonical Identity. Chính sách risk/MFA vẫn được áp dụng.

### UXD-05 — Runtime fallback

UX fallback được phép cho theme, asset không trọng yếu, translation, layout và
optional content. Pricing, currency, tax, payment, legal consent, authorization,
inventory commitment và fulfillment phải fail-closed khi cấu hình bắt buộc
thiếu hoặc không hợp lệ.

### UXD-06 — White-label và Design System

- Toàn hệ thống dùng chung design primitives, semantic tokens, accessibility
  behavior và component contracts.
- White-label cho phép tùy biến theme, brand asset và composition.
- Chỉ Platform Admin Portal là fixed-brand YSim; được đổi theme nhưng không đổi
  brand name.
- Agency Portal, Customer Portal và các tenant portal khác hỗ trợ white-label
  nhưng giữ fixed shell.
- Storefront hỗ trợ white-label và dynamic composition.

### UXD-07 — Accessibility

Toàn hệ thống phải đạt WCAG 2.2 AA. Acceptance phải bao gồm keyboard, focus,
screen reader semantics, contrast, zoom/reflow, motion, error identification và
accessible authentication; không chỉ dựa vào automated scan.

### UXD-08 — Locale

English là canonical và fallback locale; Vietnamese là locale bắt buộc. Locale
khác triển khai dưới dạng package. Legal, tax, payment và consent content không
được fallback theo cách làm thay đổi hoặc che khuất nghĩa bắt buộc.

### UXD-09 — Browser baseline

Hỗ trợ hai major version gần nhất của Chrome, Edge, Firefox và Safari, cùng iOS
Safari, Android Chrome và các WebView theo Embedded Commerce compatibility
contract. Browser matrix phải được chốt tại thời điểm release và kiểm thử trên
thiết bị/engine đại diện.

### UXD-10 — Common UX State Model

Mọi channel phải dùng chung taxonomy và behavior contract cho loading, empty,
zero-result, success, warning, validation error, system error, forbidden,
unauthenticated, offline/degraded, stale/conflict, pending/async và retry.

### UXD-11 — Visual Store/Landing Builder

v2.3 phải có builder drag-and-drop đầy đủ gồm component palette, page tree,
property editor, responsive preview, undo/redo, validation, versioning, preview,
publish, rollback và immutable published snapshot. Builder output phải tuân
theo component schema, security, accessibility và performance budget.

### UXD-12 — Performance budget

UXF phải quy định budget định lượng theo từng channel cho ít nhất LCP, INP,
CLS, initial JavaScript, route payload, API latency và critical journey. Budget
phải gắn với môi trường đo, percentile, device/network profile và release gate;
con số cụ thể được chốt trong channel blueprint.

### UXD-13 — Embedded Commerce

Embedded Commerce v2.3 phải hỗ trợ Headless API, Web SDK/widget và WebView.
Mỗi hình thức phải có authentication, theming, event, versioning, error,
observability và host-integration contract.

### UXD-14 — Risk-aware confirmation

Áp dụng framework xác nhận chung, theo mức rủi ro, cho thao tác tài chính, bảo
mật, publish/configuration và vận hành. Mức xác nhận có thể gồm inline review,
explicit confirmation, re-authentication, MFA hoặc approval; không dùng một
modal giống nhau cho mọi rủi ro.

### UXD-15 — Consent và preference

Storefront và Customer Portal dùng chung Consent Framework và Preference
Center: purpose, lawful basis, version, locale, evidence, withdrawal, channel
preference và propagation. Consent không được trộn với mandatory transaction
terms hoặc preselected marketing choice.

### UXD-16 — Enterprise Data Interaction Model

Các portal chuẩn hóa table, search, filter, sort, pagination, column control,
saved view, bulk action, import/export và async job. Model phải hỗ trợ permission,
large dataset, audit, partial failure và responsive behavior.

### UXD-17 — Identity và Organization context

Một canonical Identity có thể liên kết nhiều User record, mỗi User thuộc một
Organization. Người dùng đăng nhập một lần và chọn/chuyển Organization context;
authorization, audit và data scope được đánh giá lại sau mỗi lần chuyển.

### UXD-18 — Customer Portal và Storefront

Customer Portal là application độc lập, white-label, fixed shell và cần một
Storefront để thực hiện bán hàng. Portal có hai khu vực cố định:

1. Dashboard với widget promotion, highlighted product và flash-sale.
2. Shopping menu gồm catalog, order, reorder và payment đầy đủ.

Mỗi Customer Portal dùng một default Storefront và giữ originating Storefront
context của giao dịch khi deep-link, reorder hoặc support.

### UXD-19 — Phạm vi lịch sử Customer

Tách Global Customer Identity/Profile khỏi Organization Customer Relationship.
Không có Customer Portal tổng hợp cấp YSim. Mỗi white-label Customer Portal chỉ
hiển thị quan hệ, order và entitlement thuộc Organization/brand của portal đó.

### UXD-20 — Bảo vệ eSIM QR

- Người dùng đã đăng nhập Customer Portal có thể xem/tải QR trong authenticated
  session; risk engine có thể yêu cầu step-up MFA/OTP.
- Guest dùng magic link ngắn hạn, single-purpose; có thể bị yêu cầu OTP khi có
  rủi ro.
- QR phải được mã hóa khi lưu, access audited và có cơ chế revoke/rotate khi
  supplier hỗ trợ.

---

## 5. Business and Domain Decisions

### BDD-01 — Organization hierarchy

Một Agency/Organization chỉ có một parent duy nhất trên toàn hệ thống. Không
hỗ trợ một Agency đồng thời thuộc nhiều Distribution Network. Mọi thay đổi
parent phải có effective date, validation, authorization và audit.

### BDD-02 — Procurement Validation trước payment

Trước khi bắt đầu payment, hệ thống phải xác định đường cung ứng khả thi cho
toàn bộ order:

- Nếu inventory có item phù hợp và available, tạo hard reservation khi payment
  bắt đầu.
- Nếu không có stock phù hợp, chạy Procurement Validation với supplier để kiểm
  tra khả năng mua, điều kiện, giá/currency, SLA và constraint trước payment.
- Procurement Validation không phải purchase order và không cam kết supplier
  trước khi payment thành công.

### BDD-03 — Reservation timeout

Reservation timeout theo Payment Policy. Payment method offline/asynchronous
phải có policy riêng và revalidate inventory, procurement, price và promotion
trước khi tiếp tục hoặc xác nhận.

### BDD-04 — Reservation và Allocation

Reservation là giữ tạm trước payment; Allocation chỉ được commit sau payment
success. Việc chuyển trạng thái phải atomic hoặc có saga/compensation rõ ràng,
idempotent và observable.

### BDD-05 — Failure sau payment

Nếu payment thành công nhưng procurement/allocation thất bại, hệ thống retry
theo SLA. Hết SLA thì tự full-refund chỉ khi chưa có item nào được fulfillment;
refund phải idempotent và có customer communication.

### BDD-06 — Multi-item fulfillment

v2.3 không hỗ trợ commercial partial fulfillment. Hệ thống phải hoàn tất
procurement/allocation cho toàn bộ item trước khi bắt đầu delivery.

Nếu lỗi kênh làm delivery đã thành công một phần, hệ thống retry phần còn lại,
ưu tiên kênh đã giao thành công khi phù hợp. Nếu hết SLA mà vẫn thiếu, chuyển
manual resolution; không tự refund khi đã có bất kỳ fulfillment thành công.

### BDD-07 — State machines

Order, Payment, Reservation/Allocation và Fulfillment có state machine riêng.
Overall status là giá trị suy ra từ các state machine và invariant, không được
ghi tay như một nguồn sự thật độc lập.

### BDD-08 — Margin Policy

Giá bán thấp hơn cost hoặc minimum margin được xử lý bằng policy:
`ALLOW`, `WARN`, `REQUIRE_APPROVAL` hoặc `BLOCK`. Policy áp dụng theo market,
organization, product và role; funding promotion phải được kiểm tra riêng.

### BDD-09 — Canonical Pricing Pipeline

Thứ tự chuẩn:

```text
Price Book
→ currency normalization/conversion
→ eligibility
→ promotion stacking
→ discount/funding
→ tax
→ customer fee/surcharge
→ final payable amount
→ reservation snapshot
```

Market policy được phép cấu hình cách tính thuế, rounding, fee và presentation
nhưng không tự ý đảo pipeline nếu chưa có versioned policy contract.

### BDD-10 — Promotion selection

Promotion/coupon hợp lệ được xử lý theo stacking/exclusion rule, priority và
promotion group; trong cùng tập tương đương chọn highest customer benefit bằng
thuật toán deterministic. Tie-breaker phải được version hóa và audit được.

### BDD-11 — Promotion budget

Reserve budget atomically khi payment bắt đầu, consume khi payment success và
release khi payment fail/expire/cancel. Offline payment dùng expiry/revalidation
policy riêng và phải chống overspend dưới concurrency.

### BDD-12 — Pricing snapshots

Dùng ba lifecycle snapshot bất biến: `evaluation`, `reservation`, `final`.
Mỗi snapshot phải lưu input, rule/policy version, breakdown, currency, tax,
funding và timestamp để đối soát.

### BDD-13 — Đổi Payment Method

Khi Payment Method làm thay đổi fee, promotion, tax hoặc tổng tiền, checkout
phải re-price, hiển thị delta và yêu cầu khách xác nhận lại trước khi payment.

### BDD-14 — Promotion Funding Owner

Mỗi Promotion v2.3 chỉ có một Funding Owner. Co-funded promotion là ngoài phạm
vi; không mô phỏng bằng nhiều record thiếu liên kết/audit.

### BDD-15 — Sales Order lifecycle

Sales Order được tạo trước payment ở `PENDING_PAYMENT`. Chỉ sau payment success
mới xác nhận order với khách. Payment fail/expire/cancel phải dẫn tới trạng thái
order tương ứng và giải phóng reservation/promotion budget.

### BDD-16 — Refund

Payment Domain hỗ trợ full và partial refund theo policy và approval. Partial
refund phục vụ điều chỉnh tài chính hợp lệ, nhưng không đồng nghĩa v2.3 hỗ trợ
commercial partial fulfillment. Tự refund theo BDD-05 là pre-approved policy;
case đã giao một phần tuân BDD-06.

### BDD-17 — MFA

MFA bắt buộc cho privileged roles; role khác theo policy. Customer authentication
dùng risk-based step-up cho hành vi nhạy cảm, gồm truy cập eSIM QR khi risk
engine yêu cầu.

### BDD-18 — Data retention

Retention được xác định theo data class và jurisdiction, với platform minimum.
Policy phải bao gồm archival, legal hold, deletion/anonymization, evidence và
exception; yêu cầu pháp lý nghiêm ngặt hơn thắng platform minimum.

### BDD-19 — SLO, RPO và RTO

Định nghĩa theo service tier và mức độ quan trọng. Mỗi service/data store phải
được gán tier, owner, dependency, SLI/SLO, RPO/RTO, alert và recovery test;
con số được chốt trong reliability specification.

### BDD-20 — API credential và webhook

Trong v2.3, Platform Admin Portal quản lý API credential/webhook. Partner được
truy cập hạn chế bằng restricted role và scope, có rotation, expiry, secret
display-once, audit và approval. Cung cấp API documentation riêng cho partner.

### BDD-21 — Communication connectors

Các connector phải triển khai thật trong v2.3: Email, SMS/OTP, Portal inbox,
WhatsApp, Telegram và Zalo OA. Mỗi connector phải có consent, template,
localization, retry, idempotency, delivery status, fallback và observability.
LINE/WeChat và connector khác là ngoài phạm vi nếu BRD active không quy định.

### BDD-22 — Reporting freshness

Freshness theo loại báo cáo:

- Operational: real-time hoặc gần real-time theo event/state hiện hành.
- Commerce/management: near-real-time projection với lag SLO.
- Financial/reconciliation/BI: snapshot-consistent, có `data as of`, cutoff và
  reproducible version.

### BDD-23 — Production configuration lifecycle

Mọi cấu hình production đi qua lifecycle chung:
`Draft → Validate → Review → Approve → Schedule/Publish → Effective → Superseded/Rolled Back`.
Emergency break-glass phải time-bound, least-privilege, audited, có cảnh báo và
post-action review bắt buộc.

### BDD-24 — Parent Support access

Parent Support chỉ truy cập dữ liệu Customer theo support case, đúng scope,
time-bound và audited. Quyền phải được cấp/revoke rõ ràng, masked theo mặc định,
và step-up/approval khi xem dữ liệu nhạy cảm.

### BDD-25 — Recommendation Engine

v2.3 triển khai recommendation bằng business rule và behavioral signal, chưa
dùng ML. Engine phải có consent/purpose control, tenant isolation, explainable
reason, manual merchandising, cold-start/default fallback, suppression và
measurement không làm rò dữ liệu xuyên Organization.

### BDD-26 — Fraud/Risk Engine

v2.3 triển khai rule-based risk cho authentication/account, checkout và
payment. Decision tối thiểu gồm `ALLOW`, `CHALLENGE`, `BLOCK`, `REVIEW`; rule,
signal, reason, override và audit phải versioned. ML scoring là `POST_V2.3`.

### BDD-27 — Shared Approval Engine

Dùng một Shared Approval Engine cho margin exception, refund, configuration,
credential, risk override và nghiệp vụ được BRD quy định. Engine phải hỗ trợ
policy, approver resolution, separation of duties, expiry, escalation,
delegation, evidence và immutable audit. Đây không phải general-purpose BPM
workflow engine.

---

## 6. Documentation Governance Decisions

### DGD-01 — Rebuild registry và traceability

Trước khi sửa YADF, phải rebuild exact BRD/UXF requirement registry và mapping.
Không chấp nhận số lượng ước lượng. Coverage phải machine-checkable và truy
ngược hai chiều giữa requirement, acceptance, architecture/domain và slice.

### DGD-02 — Ổn định Requirement ID

Giữ ổn định ID hiện có. Requirement bị thay thế/xóa dùng `deprecated`, `alias`
hoặc `tombstone`; không tái sử dụng ID cho nghĩa khác. Alias phải trỏ tới
canonical ID và giữ lịch sử lý do/ngày thay đổi.

### DGD-03 — Requirement machine-readable

Mỗi normative BRD/UXF requirement phải có Requirement ID máy đọc được, cùng ít
nhất classification, status, source, priority, acceptance criteria và mapping.
Statement ghép nhiều nghĩa phải được tách đủ nhỏ để nghiệm thu chính xác.

### DGD-04 — Ngôn ngữ tài liệu

- BRD canonical: tiếng Việt.
- UXF, architecture và technical specifications canonical: tiếng Anh.
- Dùng shared canonical glossary để thống nhất thuật ngữ và alias Việt/Anh.
- Requirement ID và enum/status dùng English machine-readable token ổn định.

### DGD-05 — Cách hiệu chỉnh tài liệu

BRD/UXF được sửa tại chỗ trên nhánh v2.3; Git giữ lịch sử. Giữ document code và
filename ổn định, cập nhật version/baseline/changelog. Tài liệu có normative
change phải trở lại `DRAFT`/`IN_REVIEW` cho tới khi được phê duyệt lại; tag v2.2
là baseline lịch sử bất biến.

### DGD-06 — Thứ tự công việc trước YADF

Thứ tự bắt buộc:

1. Inventory và exact registry của BRD/UXF.
2. Áp dụng các quyết định tại tài liệu này vào BRD/UXF.
3. Hoàn thiện acceptance criteria và traceability.
4. Review/re-approve BRD/UXF v2.3.
5. Hiệu chỉnh architecture/domain specifications bị tác động.
6. Sau đó mới thiết kế YADF v2.3, execution contracts và vertical slices.

---

## 7. Supersession và clarification register

| Chủ đề | Quyết định có hiệu lực | Nội dung bị thay thế/làm rõ |
|---|---|---|
| Guest identity | Primary email luôn bắt buộc | Phương án chỉ dùng IM/phone mà không có email |
| eSIM QR | Authenticated session; risk-based step-up; guest short-lived magic link | Cách hiểu rằng mọi lần xem đều bắt buộc đồng thời login và OTP |
| Partial delivery | Retry rồi manual resolution; không auto-refund nếu đã giao bất kỳ phần nào | Auto-refund chung sau SLA |
| Future scope | Giữ ngoài v2.3, trừ SD-03 | Tự động đưa mọi Future/Deferred vào release |
| Partner Portal | Channel riêng nhưng `POST_V2.3` | Tuyên bố portal đã được implement trong v2.3 |
| Full-document execution | Đọc full docs + Execution Contract | Prompt/manifest rút gọn làm nguồn nghĩa duy nhất |

---

## 8. Điều kiện sử dụng tài liệu

Tài liệu này phải được tham chiếu từ `DOCUMENT_BASELINE.md`, `REVIEW_REGISTER.md`
và mọi contract dùng để sửa BRD/UXF hoặc thiết kế YADF v2.3.

Trước khi triển khai, cần chuyển từng quyết định sang requirement/acceptance
machine-readable trong tài liệu sở hữu tương ứng. Không được đánh dấu quyết
định là “implemented” chỉ vì nó đã xuất hiện trong file này.

## 9. Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-13 | Khởi tạo bản ghi quyết định framework; file nguồn bị dừng giữa FD-01. |
| 2.0 | 2026-07-13 | Phục hồi FD-01, bổ sung toàn bộ framework, product scope, UXF, domain và documentation governance decisions đã được phê duyệt. |
