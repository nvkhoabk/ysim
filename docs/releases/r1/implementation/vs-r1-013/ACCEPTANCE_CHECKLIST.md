# VS-R1-013 Acceptance Checklist

- [ ] Accepted VS-R1-012 baseline verified locally and remotely.
- [ ] Candidate inventory contains exactly 16 paths.
- [ ] Outbox migration hash and schema contract are verified.
- [ ] Payment Success event contract is versioned.
- [ ] Deduplication key is deterministic and 64 lowercase hexadecimal chars.
- [ ] Event payload contains no access token, email, certificate or signature.
- [ ] Outbox insert is in the same transaction as Payment success.
- [ ] Duplicate webhook produces no second outbox event.
- [ ] Non-success transitions do not enqueue Payment Success.
- [ ] Slice tests report 2 files and 18 assertions.
- [ ] Cumulative tests report 21 files and 185 assertions.
- [ ] PostgreSQL runtime proof passes twice before commit.
- [ ] PostgreSQL runtime proof passes twice after commit.
- [ ] Candidate validator passes in committed phase.
- [ ] Working tree is clean before publication.
