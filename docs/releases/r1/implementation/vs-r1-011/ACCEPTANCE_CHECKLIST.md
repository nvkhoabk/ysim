# VS-R1-011 Acceptance Checklist

- [ ] Public GPay webhook route is registered.
- [ ] Verification occurs before lookup or mutation.
- [ ] Only GPAY intents are resolved.
- [ ] Amount and currency match the immutable snapshot.
- [ ] Exact duplicates are suppressed.
- [ ] Conflicting event identifiers are rejected.
- [ ] Successful event confirms the Order exactly once.
- [ ] Verified actor identity is recorded.
- [ ] Response contains no raw signature, certificate or payload.
- [ ] 17 cumulative test files and 149 assertions pass.
- [ ] 16 VS-R1-011 assertions pass.
- [ ] Runtime proof passes twice.
- [ ] Candidate contains exactly 16 paths.
