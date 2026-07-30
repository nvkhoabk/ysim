# VS-R1-012 Acceptance Checklist

- [ ] Accepted VS-R1-011 baseline identity is verified locally and remotely.
- [ ] Candidate inventory contains exactly 15 paths.
- [ ] Historical VS-R1-008 TEST-only policy remains unchanged.
- [ ] New provider-aware policy accepts only TEST and GPAY.
- [ ] GPAY reservation is sandbox-only and requires PROBED contract status.
- [ ] GPAY reference matches `GPY-[0-9A-F]{32}`.
- [ ] PaymentService routes TEST and GPAY to different adapters.
- [ ] Existing idempotency and order-token behavior remains valid.
- [ ] No live external GPay request is executed.
- [ ] Slice tests report 2 files and 18 assertions.
- [ ] Cumulative tests report 19 files and 167 assertions.
- [ ] PostgreSQL runtime proof passes twice before commit.
- [ ] PostgreSQL runtime proof passes twice after commit.
- [ ] Candidate validator passes in committed phase.
- [ ] Working tree is clean before candidate publication.
