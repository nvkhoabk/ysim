# VS-R1-010 — Acceptance Checklist

- [ ] Accepted base is `baseline/r1/vs-r1-009/accepted-v1`.
- [ ] Candidate contains exactly 15 approved paths.
- [ ] `PaymentProvider` includes `TEST` and `GPAY`.
- [ ] Payment schema accepts provider-scoped GPay references.
- [ ] Production activation is blocked.
- [ ] Contract status must be `PROBED`.
- [ ] Verification certificate path must be absolute.
- [ ] Unknown webhook body fields are rejected.
- [ ] Event identifier, timestamp and signature are required.
- [ ] Replay window is enforced.
- [ ] All provider statuses normalize deterministically.
- [ ] Invalid signatures fail closed.
- [ ] No raw signature, certificate or payload appears in the verified result.
- [ ] 15 cumulative test files and 133 assertions pass.
- [ ] Both VS-R1-010 files and all 16 assertions pass.
- [ ] PostgreSQL and crypto runtime proof passes twice.
- [ ] Committed validation passes.
- [ ] Candidate tag is verified remotely.
