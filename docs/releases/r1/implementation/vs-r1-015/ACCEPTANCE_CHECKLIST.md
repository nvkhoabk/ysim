# VS-R1-015 Acceptance Checklist

- [ ] Accepted VS-R1-014 baseline verified locally and remotely.
- [ ] Candidate inventory contains exactly 19 paths.
- [ ] Procurement schema has no cross-context foreign keys.
- [ ] Payment, Order and Supplier Mapping snapshots must match.
- [ ] Only SANDBOX + PROBED + PUT mappings are accepted.
- [ ] One source event creates one PENDING_SUPPLIER request.
- [ ] Exact replay returns the existing request.
- [ ] Conflicting replay fails closed.
- [ ] No Gigago or external network request is made.
- [ ] Slice tests report 2 files and 20 assertions.
- [ ] Cumulative tests report 25 files and 225 assertions.
- [ ] PostgreSQL runtime proof passes twice before and after commit.
