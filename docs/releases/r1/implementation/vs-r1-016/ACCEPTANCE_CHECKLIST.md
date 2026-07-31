# VS-R1-016 Acceptance Checklist

- [ ] Accepted VS-R1-015 baseline verified locally and remotely.
- [ ] Candidate inventory contains exactly 17 paths.
- [ ] Canonical test suite manifest contains 16 contiguous suites.
- [ ] Only sandbox base URL is accepted.
- [ ] Production activation is blocked.
- [ ] Submission requires explicit enablement and PROBED contract.
- [ ] Method is PUT and endpoint is createPartnerOrder.
- [ ] Header name is exactly apiKey.
- [ ] Request ID is deterministic and request payload is strict.
- [ ] Response envelope and extra are validated.
- [ ] API key is never returned or logged.
- [ ] Runtime harness sends exactly one simulated request.
- [ ] No live external request is executed.
- [ ] Slice tests report 2 files and 20 assertions.
- [ ] Cumulative tests report 27 files and 245 assertions.
- [ ] Runtime proof passes twice before and after commit.
- [ ] Adapter is not registered in Nest and startup remains credential-independent.
