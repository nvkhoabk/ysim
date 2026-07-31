# VS-R1-014 Acceptance Checklist

- [ ] Accepted VS-R1-013 baseline is verified locally and remotely.
- [ ] Candidate inventory contains exactly 16 paths.
- [ ] Machine values come only from `PACKAGE_SPEC.json`.
- [ ] Publisher claims only available unpublished events.
- [ ] Claim uses `FOR UPDATE SKIP LOCKED`.
- [ ] Lease duration is bounded from 5 to 300 seconds.
- [ ] Attempt number fences stale success and failure completion.
- [ ] Retry starts at 5 seconds and caps at 15 minutes.
- [ ] Failure text is sanitized and limited to 500 characters.
- [ ] Payment Success payload shape is strict and safe.
- [ ] One invocation publishes at most one event.
- [ ] No scheduler or external provider call is introduced.
- [ ] Slice tests report 2 files and 20 assertions.
- [ ] Cumulative tests report 23 files and 205 assertions.
- [ ] PostgreSQL runtime proof passes twice before commit.
- [ ] PostgreSQL runtime proof passes twice after commit.
- [ ] Candidate validator and clean-tree check pass.
