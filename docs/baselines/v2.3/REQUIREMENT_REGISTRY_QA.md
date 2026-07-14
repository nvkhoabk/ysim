# BRD/UXF Requirement Registry Semantic QA — Phase 1B (Reconciled in Phase 1C)

This audit preserves all **1309** registry statements and all existing canonical IDs/temporary keys. Findings are candidates for human review, not automatic registry membership changes.

## Extraction coverage by source file

| Source | Independent candidates | Matched candidates | Registry requirements | False-negative candidates | False-positive candidates | Compound candidates | Same-source duplicate groups |
|---|---:|---:|---:|---:|---:|---:|---:|
| `docs/BRD/BRD-BO-INDEX.md` | 71 | 71 | 70 | 0 | 3 | 11 | 0 |
| `docs/BRD/BRD-CAP-INDEX.md` | 55 | 55 | 53 | 0 | 2 | 2 | 1 |
| `docs/BRD/BRD-EVENT-INDEX.md` | 41 | 41 | 53 | 0 | 10 | 3 | 0 |
| `docs/BRD/BRD-META-MODEL.md` | 3 | 3 | 3 | 0 | 0 | 1 | 0 |
| `docs/BRD/BRD-POLICY-INDEX.md` | 42 | 41 | 45 | 1 | 9 | 2 | 0 |
| `docs/BRD/BRD-SNAPSHOT-INDEX.md` | 39 | 38 | 56 | 1 | 10 | 3 | 0 |
| `docs/BRD/BRD-UPDATE-01.md` | 17 | 16 | 29 | 1 | 0 | 0 | 0 |
| `docs/BRD/BRD-WS-01.md` | 34 | 34 | 41 | 0 | 5 | 0 | 0 |
| `docs/BRD/BRD-WS-02.md` | 17 | 17 | 13 | 0 | 1 | 1 | 0 |
| `docs/BRD/BRD-WS-03.md` | 24 | 24 | 23 | 0 | 0 | 3 | 0 |
| `docs/BRD/BRD-WS-04.md` | 27 | 27 | 27 | 0 | 0 | 2 | 0 |
| `docs/BRD/BRD-WS-05.md` | 36 | 36 | 43 | 0 | 0 | 2 | 0 |
| `docs/BRD/BRD-WS-06.md` | 51 | 51 | 51 | 0 | 1 | 0 | 1 |
| `docs/BRD/BRD-WS-07.md` | 58 | 58 | 52 | 0 | 0 | 3 | 1 |
| `docs/BRD/BRD-WS-08.md` | 39 | 39 | 36 | 0 | 0 | 1 | 2 |
| `docs/BRD/BRD-WS-09.md` | 36 | 34 | 35 | 2 | 0 | 0 | 1 |
| `docs/BRD/BRD-WS-10.md` | 40 | 40 | 36 | 0 | 0 | 0 | 2 |
| `docs/BRD/BRD-WS-11.md` | 40 | 40 | 39 | 0 | 0 | 2 | 0 |
| `docs/BRD/BRD-WS-12.md` | 40 | 40 | 40 | 0 | 0 | 0 | 2 |
| `docs/BRD/BRD-WS-13.md` | 59 | 57 | 53 | 2 | 0 | 14 | 0 |
| `docs/BRD/BRD-WS-14.md` | 71 | 70 | 67 | 1 | 0 | 22 | 0 |
| `docs/BRD/BRD-WS-15.md` | 68 | 68 | 65 | 0 | 0 | 16 | 2 |
| `docs/BRD/BRD-WS-16.md` | 58 | 58 | 52 | 0 | 0 | 15 | 2 |
| `docs/BRD/BRD-WS-17.md` | 75 | 73 | 62 | 2 | 0 | 8 | 2 |
| `docs/UXF/INDEX.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `docs/UXF/UXF-00.md` | 34 | 34 | 53 | 0 | 10 | 1 | 0 |
| `docs/UXF/UXF-01.md` | 21 | 21 | 31 | 0 | 10 | 0 | 1 |
| `docs/UXF/UXF-02.md` | 28 | 28 | 39 | 0 | 20 | 9 | 0 |
| `docs/UXF/UXF-03.md` | 25 | 25 | 36 | 0 | 19 | 5 | 0 |
| `docs/UXF/UXF-04.md` | 32 | 32 | 43 | 0 | 19 | 10 | 0 |
| `docs/UXF/UXF-05.md` | 47 | 47 | 63 | 0 | 21 | 1 | 1 |

Totals: candidates **1228**, matched **1218**, false-negative candidates **10**, false-positive candidates **140**, compound candidates **137**.

## Deterministic sample audit

Selection is deterministic: `Sort by (requirement key, source path); take first 10 for four base strata; include all ambiguity and non-active scope entries; take first 10 overlap groups by group_id.`

Unique sampled requirements: **179**.

| Key | Source | Selected for | Result | Checks requiring review |
|---|---|---|---|---|
| `BD-02-001` | `docs/BRD/BRD-WS-02.md:L448-L457` | brd_existing_id | `PASS` | — |
| `BD-02-002` | `docs/BRD/BRD-WS-02.md:L460-L471` | brd_existing_id | `PASS` | — |
| `BD-02-003` | `docs/BRD/BRD-WS-02.md:L474-L485` | brd_existing_id | `PASS` | — |
| `BD-02-004` | `docs/BRD/BRD-WS-02.md:L488-L499` | brd_existing_id | `PASS` | — |
| `BD-02-005` | `docs/BRD/BRD-WS-02.md:L502-L513` | brd_existing_id | `PASS` | — |
| `BD-02-006` | `docs/BRD/BRD-WS-02.md:L516-L525` | brd_existing_id | `PASS` | — |
| `BD-02-007` | `docs/BRD/BRD-WS-02.md:L528-L537` | brd_existing_id | `PASS` | — |
| `BD-03-001` | `docs/BRD/BRD-WS-03.md:L521-L524` | brd_existing_id | `PASS` | — |
| `BD-03-002` | `docs/BRD/BRD-WS-03.md:L527-L530` | brd_existing_id | `PASS` | — |
| `BD-03-003` | `docs/BRD/BRD-WS-03.md:L533-L536` | brd_existing_id | `PASS` | — |
| `BD-06-007` | `docs/BRD/BRD-WS-06.md:L508-L511` | overlap:OVL-EXACT-001 | `PASS` | — |
| `BD-06-016` | `docs/BRD/BRD-WS-06.md:L564-L567` | all_deferred | `PASS` | — |
| `BD-07-003` | `docs/BRD/BRD-WS-07.md:L650-L653` | overlap:OVL-EXACT-002 | `PASS` | — |
| `BD-08-001` | `docs/BRD/BRD-WS-08.md:L534-L537` | overlap:OVL-EXACT-003 | `PASS` | — |
| `BD-08-012` | `docs/BRD/BRD-WS-08.md:L600-L603` | all_out_of_scope, overlap:OVL-EXACT-004 | `PASS` | — |
| `BD-09-002` | `docs/BRD/BRD-WS-09.md:L566-L569` | overlap:OVL-EXACT-005 | `PASS` | — |
| `BD-10-015` | `docs/BRD/BRD-WS-10.md:L729-L732` | all_future | `PASS` | — |
| `BD-10-016` | `docs/BRD/BRD-WS-10.md:L735-L738` | all_out_of_scope, overlap:OVL-EXACT-006 | `PASS` | — |
| `BD-10-019` | `docs/BRD/BRD-WS-10.md:L753-L756` | overlap:OVL-EXACT-007 | `PASS` | — |
| `BD-11-015` | `docs/BRD/BRD-WS-11.md:L704-L707` | all_future | `PASS` | — |
| `BD-12-005` | `docs/BRD/BRD-WS-12.md:L660-L663` | overlap:OVL-EXACT-008 | `PASS` | — |
| `BD-16-026` | `docs/BRD/BRD-WS-16.md:L1025-L1028` | overlap:OVL-EXACT-009 | `PASS` | — |
| `BD-16-027` | `docs/BRD/BRD-WS-16.md:L1031-L1034` | overlap:OVL-EXACT-010 | `PASS` | — |
| `EP-06-004` | `docs/BRD/BRD-WS-06.md:L637-L640` | overlap:OVL-EXACT-001 | `PASS` | — |
| `EP-16-008` | `docs/BRD/BRD-WS-16.md:L1121-L1124` | overlap:OVL-EXACT-010 | `PASS` | — |
| `EP-16-009` | `docs/BRD/BRD-WS-16.md:L1127-L1130` | overlap:OVL-EXACT-009 | `PASS` | — |
| `TMP-BRD-BO-INDEX-001` | `docs/BRD/BRD-BO-INDEX.md:L108` | brd_temporary_key | `PASS` | — |
| `TMP-BRD-BO-INDEX-002` | `docs/BRD/BRD-BO-INDEX.md:L112` | brd_temporary_key | `PASS` | — |
| `TMP-BRD-BO-INDEX-003` | `docs/BRD/BRD-BO-INDEX.md:L154` | brd_temporary_key | `PASS` | — |
| `TMP-BRD-BO-INDEX-004` | `docs/BRD/BRD-BO-INDEX.md:L156-L158` | brd_temporary_key | `PASS` | — |
| `TMP-BRD-BO-INDEX-005` | `docs/BRD/BRD-BO-INDEX.md:L156-L159` | brd_temporary_key | `PASS` | — |
| `TMP-BRD-BO-INDEX-006` | `docs/BRD/BRD-BO-INDEX.md:L156-L160` | brd_temporary_key | `PASS` | — |
| `TMP-BRD-BO-INDEX-007` | `docs/BRD/BRD-BO-INDEX.md:L156-L161` | brd_temporary_key | `PASS` | — |
| `TMP-BRD-BO-INDEX-008` | `docs/BRD/BRD-BO-INDEX.md:L167` | brd_temporary_key | `PASS` | — |
| `TMP-BRD-BO-INDEX-009` | `docs/BRD/BRD-BO-INDEX.md:L169-L171` | brd_temporary_key | `PASS` | — |
| `TMP-BRD-BO-INDEX-010` | `docs/BRD/BRD-BO-INDEX.md:L169-L172` | brd_temporary_key | `PASS` | — |
| `TMP-BRD-BO-INDEX-023` | `docs/BRD/BRD-BO-INDEX.md:L938` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-024` | `docs/BRD/BRD-BO-INDEX.md:L940-L942` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-025` | `docs/BRD/BRD-BO-INDEX.md:L940-L943` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-026` | `docs/BRD/BRD-BO-INDEX.md:L940-L944` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-027` | `docs/BRD/BRD-BO-INDEX.md:L940-L945` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-028` | `docs/BRD/BRD-BO-INDEX.md:L940-L946` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-029` | `docs/BRD/BRD-BO-INDEX.md:L940-L947` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-030` | `docs/BRD/BRD-BO-INDEX.md:L940-L948` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-031` | `docs/BRD/BRD-BO-INDEX.md:L940-L949` | all_ambiguity | `PASS` | — |
| `TMP-BRD-BO-INDEX-032` | `docs/BRD/BRD-BO-INDEX.md:L940-L950` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-033` | `docs/BRD/BRD-BO-INDEX.md:L940-L951` | all_ambiguity | `PASS` | — |
| `TMP-BRD-BO-INDEX-034` | `docs/BRD/BRD-BO-INDEX.md:L940-L952` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-035` | `docs/BRD/BRD-BO-INDEX.md:L940-L953` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-036` | `docs/BRD/BRD-BO-INDEX.md:L940-L954` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-037` | `docs/BRD/BRD-BO-INDEX.md:L940-L955` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-038` | `docs/BRD/BRD-BO-INDEX.md:L940-L956` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-039` | `docs/BRD/BRD-BO-INDEX.md:L940-L957` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-040` | `docs/BRD/BRD-BO-INDEX.md:L940-L958` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-041` | `docs/BRD/BRD-BO-INDEX.md:L960` | all_future | `PASS` | — |
| `TMP-BRD-BO-INDEX-042` | `docs/BRD/BRD-BO-INDEX.md:L962` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-001` | `docs/BRD/BRD-CAP-INDEX.md:L86` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-005` | `docs/BRD/BRD-CAP-INDEX.md:L624` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-006` | `docs/BRD/BRD-CAP-INDEX.md:L625` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-007` | `docs/BRD/BRD-CAP-INDEX.md:L626` | all_ambiguity | `PASS` | — |
| `TMP-BRD-CAP-INDEX-008` | `docs/BRD/BRD-CAP-INDEX.md:L639` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-009` | `docs/BRD/BRD-CAP-INDEX.md:L643` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-010` | `docs/BRD/BRD-CAP-INDEX.md:L644` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-011` | `docs/BRD/BRD-CAP-INDEX.md:L645` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-012` | `docs/BRD/BRD-CAP-INDEX.md:L646` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-013` | `docs/BRD/BRD-CAP-INDEX.md:L647` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-014` | `docs/BRD/BRD-CAP-INDEX.md:L648` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-015` | `docs/BRD/BRD-CAP-INDEX.md:L649` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-016` | `docs/BRD/BRD-CAP-INDEX.md:L650` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-017` | `docs/BRD/BRD-CAP-INDEX.md:L651` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-018` | `docs/BRD/BRD-CAP-INDEX.md:L652` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-019` | `docs/BRD/BRD-CAP-INDEX.md:L653` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-020` | `docs/BRD/BRD-CAP-INDEX.md:L654` | all_ambiguity | `PASS` | — |
| `TMP-BRD-CAP-INDEX-021` | `docs/BRD/BRD-CAP-INDEX.md:L655` | all_future | `PASS` | — |
| `TMP-BRD-CAP-INDEX-022` | `docs/BRD/BRD-CAP-INDEX.md:L656` | all_ambiguity | `PASS` | — |
| `TMP-BRD-CAP-INDEX-023` | `docs/BRD/BRD-CAP-INDEX.md:L658` | all_future | `PASS` | — |
| `TMP-BRD-WS-01-002` | `docs/BRD/BRD-WS-01.md:L53` | all_out_of_scope | `PASS` | — |
| `TMP-BRD-WS-01-020` | `docs/BRD/BRD-WS-01.md:L81` | all_out_of_scope | `PASS` | — |
| `TMP-BRD-WS-01-021` | `docs/BRD/BRD-WS-01.md:L82` | all_out_of_scope | `PASS` | — |
| `TMP-BRD-WS-01-022` | `docs/BRD/BRD-WS-01.md:L83` | all_out_of_scope | `PASS` | — |
| `TMP-BRD-WS-01-023` | `docs/BRD/BRD-WS-01.md:L84` | all_out_of_scope | `PASS` | — |
| `TMP-BRD-WS-01-024` | `docs/BRD/BRD-WS-01.md:L85` | all_out_of_scope | `PASS` | — |
| `TMP-BRD-WS-01-025` | `docs/BRD/BRD-WS-01.md:L86` | all_out_of_scope | `PASS` | — |
| `TMP-BRD-WS-01-026` | `docs/BRD/BRD-WS-01.md:L87` | all_out_of_scope | `PASS` | — |
| `TMP-BRD-WS-01-037` | `docs/BRD/BRD-WS-01.md:L327` | all_future | `PASS` | — |
| `TMP-BRD-WS-01-038` | `docs/BRD/BRD-WS-01.md:L328` | all_future | `PASS` | — |
| `TMP-BRD-WS-01-039` | `docs/BRD/BRD-WS-01.md:L329` | all_future | `PASS` | — |
| `TMP-BRD-WS-01-040` | `docs/BRD/BRD-WS-01.md:L330` | all_future | `PASS` | — |
| `TMP-BRD-WS-01-041` | `docs/BRD/BRD-WS-01.md:L331` | all_future | `PASS` | — |
| `TMP-BRD-WS-02-001` | `docs/BRD/BRD-WS-02.md:L67` | all_out_of_scope | `PASS` | — |
| `TMP-BRD-WS-04-013` | `docs/BRD/BRD-WS-04.md:L424` | all_future | `PASS` | — |
| `TMP-BRD-WS-05-010` | `docs/BRD/BRD-WS-05.md:L208-L212` | all_out_of_scope | `PASS` | — |
| `TMP-BRD-WS-06-002` | `docs/BRD/BRD-WS-06.md:L120` | all_future | `PASS` | — |
| `TMP-BRD-WS-06-018` | `docs/BRD/BRD-WS-06.md:L311` | all_future | `REVIEW` | requirement_type_reasonable |
| `TMP-BRD-WS-06-021` | `docs/BRD/BRD-WS-06.md:L446` | all_future | `PASS` | — |
| `TMP-BRD-WS-06-022` | `docs/BRD/BRD-WS-06.md:L452-L454` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-06-023` | `docs/BRD/BRD-WS-06.md:L452-L455` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-06-024` | `docs/BRD/BRD-WS-06.md:L452-L456` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-06-025` | `docs/BRD/BRD-WS-06.md:L452-L457` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-06-026` | `docs/BRD/BRD-WS-06.md:L452-L458` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-06-027` | `docs/BRD/BRD-WS-06.md:L452-L459` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-06-028` | `docs/BRD/BRD-WS-06.md:L452-L460` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-06-029` | `docs/BRD/BRD-WS-06.md:L462` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-07-002` | `docs/BRD/BRD-WS-07.md:L148` | overlap:OVL-EXACT-002 | `PASS` | — |
| `TMP-BRD-WS-07-013` | `docs/BRD/BRD-WS-07.md:L498` | all_out_of_scope | `PASS` | — |
| `TMP-BRD-WS-07-021` | `docs/BRD/BRD-WS-07.md:L620-L622` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-07-022` | `docs/BRD/BRD-WS-07.md:L620-L623` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-07-023` | `docs/BRD/BRD-WS-07.md:L620-L624` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-07-024` | `docs/BRD/BRD-WS-07.md:L620-L625` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-07-025` | `docs/BRD/BRD-WS-07.md:L620-L626` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-07-026` | `docs/BRD/BRD-WS-07.md:L620-L627` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-07-027` | `docs/BRD/BRD-WS-07.md:L620-L628` | all_deferred | `PASS` | — |
| `TMP-BRD-WS-08-001` | `docs/BRD/BRD-WS-08.md:L97` | overlap:OVL-EXACT-003 | `PASS` | — |
| `TMP-BRD-WS-08-008` | `docs/BRD/BRD-WS-08.md:L316` | all_out_of_scope | `PASS` | — |
| `TMP-BRD-WS-08-009` | `docs/BRD/BRD-WS-08.md:L336-L338` | all_out_of_scope, overlap:OVL-EXACT-004 | `PASS` | — |
| `TMP-BRD-WS-08-012` | `docs/BRD/BRD-WS-08.md:L474` | all_ambiguity | `PASS` | — |
| `TMP-BRD-WS-09-002` | `docs/BRD/BRD-WS-09.md:L136` | overlap:OVL-EXACT-005 | `PASS` | — |
| `TMP-BRD-WS-09-009` | `docs/BRD/BRD-WS-09.md:L366` | all_future | `PASS` | — |
| `TMP-BRD-WS-09-010` | `docs/BRD/BRD-WS-09.md:L411` | all_future | `PASS` | — |
| `TMP-BRD-WS-10-001` | `docs/BRD/BRD-WS-10.md:L183` | all_future | `PASS` | — |
| `TMP-BRD-WS-10-005` | `docs/BRD/BRD-WS-10.md:L410-L412` | all_out_of_scope, overlap:OVL-EXACT-006 | `PASS` | — |
| `TMP-BRD-WS-10-006` | `docs/BRD/BRD-WS-10.md:L452` | overlap:OVL-EXACT-007 | `PASS` | — |
| `TMP-BRD-WS-11-001` | `docs/BRD/BRD-WS-11.md:L98` | all_future | `PASS` | — |
| `TMP-BRD-WS-11-008` | `docs/BRD/BRD-WS-11.md:L420` | all_future | `PASS` | — |
| `TMP-BRD-WS-11-010` | `docs/BRD/BRD-WS-11.md:L550` | all_out_of_scope | `PASS` | — |
| `TMP-BRD-WS-11-011` | `docs/BRD/BRD-WS-11.md:L592` | all_future | `PASS` | — |
| `TMP-BRD-WS-11-012` | `docs/BRD/BRD-WS-11.md:L598-L600` | all_future | `PASS` | — |
| `TMP-BRD-WS-11-013` | `docs/BRD/BRD-WS-11.md:L598-L601` | all_future | `PASS` | — |
| `TMP-BRD-WS-11-014` | `docs/BRD/BRD-WS-11.md:L598-L602` | all_future | `PASS` | — |
| `TMP-BRD-WS-11-015` | `docs/BRD/BRD-WS-11.md:L598-L603` | all_future | `PASS` | — |
| `TMP-BRD-WS-11-016` | `docs/BRD/BRD-WS-11.md:L598-L604` | all_future | `PASS` | — |
| `TMP-BRD-WS-11-017` | `docs/BRD/BRD-WS-11.md:L606` | all_future | `PASS` | — |
| `TMP-BRD-WS-12-001` | `docs/BRD/BRD-WS-12.md:L192` | overlap:OVL-EXACT-008 | `PASS` | — |
| `TMP-BRD-WS-12-003` | `docs/BRD/BRD-WS-12.md:L245` | all_future | `PASS` | — |
| `TMP-BRD-WS-12-004` | `docs/BRD/BRD-WS-12.md:L350` | all_future | `PASS` | — |
| `TMP-BRD-WS-12-011` | `docs/BRD/BRD-WS-12.md:L409` | all_future | `PASS` | — |
| `TMP-BRD-WS-12-012` | `docs/BRD/BRD-WS-12.md:L465` | all_future | `PASS` | — |
| `TMP-BRD-WS-12-013` | `docs/BRD/BRD-WS-12.md:L490` | all_out_of_scope | `PASS` | — |
| `TMP-BRD-WS-13-001` | `docs/BRD/BRD-WS-13.md:L45` | all_future | `PASS` | — |
| `TMP-BRD-WS-13-005` | `docs/BRD/BRD-WS-13.md:L277` | all_future | `PASS` | — |
| `TMP-BRD-WS-13-007` | `docs/BRD/BRD-WS-13.md:L422` | all_future | `PASS` | — |
| `TMP-BRD-WS-13-020` | `docs/BRD/BRD-WS-13.md:L595` | all_future | `PASS` | — |
| `TMP-BRD-WS-13-022` | `docs/BRD/BRD-WS-13.md:L689` | all_future | `PASS` | — |
| `TMP-BRD-WS-13-024` | `docs/BRD/BRD-WS-13.md:L745` | all_future | `PASS` | — |
| `TMP-BRD-WS-13-025` | `docs/BRD/BRD-WS-13.md:L746` | all_future | `PASS` | — |
| `TMP-BRD-WS-17-004` | `docs/BRD/BRD-WS-17.md:L494` | all_future | `REVIEW` | requirement_type_reasonable |
| `TMP-BRD-WS-17-014` | `docs/BRD/BRD-WS-17.md:L855` | all_future | `PASS` | — |
| `TMP-UXF-00-001` | `docs/UXF/UXF-00.md:L248` | uxf_temporary_key | `REVIEW` | requirement_type_reasonable |
| `TMP-UXF-00-002` | `docs/UXF/UXF-00.md:L262` | uxf_temporary_key | `REVIEW` | requirement_type_reasonable |
| `TMP-UXF-00-003` | `docs/UXF/UXF-00.md:L270` | uxf_temporary_key | `REVIEW` | requirement_type_reasonable |
| `TMP-UXF-00-004` | `docs/UXF/UXF-00.md:L304` | all_future, uxf_temporary_key | `REVIEW` | requirement_type_reasonable |
| `TMP-UXF-00-005` | `docs/UXF/UXF-00.md:L345-L347` | uxf_temporary_key | `REVIEW` | requirement_type_reasonable |
| `TMP-UXF-00-006` | `docs/UXF/UXF-00.md:L345-L348` | uxf_temporary_key | `REVIEW` | requirement_type_reasonable |
| `TMP-UXF-00-007` | `docs/UXF/UXF-00.md:L345-L349` | uxf_temporary_key | `REVIEW` | requirement_type_reasonable |
| `TMP-UXF-00-008` | `docs/UXF/UXF-00.md:L345-L350` | uxf_temporary_key | `REVIEW` | requirement_type_reasonable |
| `TMP-UXF-00-009` | `docs/UXF/UXF-00.md:L345-L351` | uxf_temporary_key | `REVIEW` | requirement_type_reasonable |
| `TMP-UXF-00-010` | `docs/UXF/UXF-00.md:L385` | uxf_temporary_key | `PASS` | — |
| `TMP-UXF-03-006` | `docs/UXF/UXF-03.md:L494` | all_ambiguity | `PASS` | — |
| `TMP-UXF-05-033` | `docs/UXF/UXF-05.md:L705` | all_future | `PASS` | — |
| `TMP-UXF-05-034` | `docs/UXF/UXF-05.md:L707-L709` | all_future | `PASS` | — |
| `TMP-UXF-05-035` | `docs/UXF/UXF-05.md:L707-L710` | all_future | `PASS` | — |
| `TMP-UXF-05-036` | `docs/UXF/UXF-05.md:L707-L711` | all_future | `PASS` | — |
| `TMP-UXF-05-037` | `docs/UXF/UXF-05.md:L707-L712` | all_ambiguity | `PASS` | — |
| `TMP-UXF-05-038` | `docs/UXF/UXF-05.md:L707-L713` | all_future | `PASS` | — |
| `TMP-UXF-05-039` | `docs/UXF/UXF-05.md:L707-L714` | all_future | `PASS` | — |
| `TMP-UXF-05-040` | `docs/UXF/UXF-05.md:L707-L715` | all_future | `PASS` | — |
| `TMP-UXF-05-041` | `docs/UXF/UXF-05.md:L707-L716` | all_future | `PASS` | — |
| `TMP-UXF-05-042` | `docs/UXF/UXF-05.md:L707-L717` | all_future | `PASS` | — |
| `TMP-UXF-05-043` | `docs/UXF/UXF-05.md:L719` | all_future | `PASS` | — |
| `UXF-001` | `docs/UXF/UXF-00.md:L603-L606` | uxf_existing_id | `PASS` | — |
| `UXF-002` | `docs/UXF/UXF-00.md:L609-L612` | uxf_existing_id | `PASS` | — |
| `UXF-003` | `docs/UXF/UXF-00.md:L615-L618` | uxf_existing_id | `PASS` | — |
| `UXF-004` | `docs/UXF/UXF-00.md:L621-L624` | uxf_existing_id | `PASS` | — |
| `UXF-005` | `docs/UXF/UXF-00.md:L627-L630` | uxf_existing_id | `PASS` | — |
| `UXF-006` | `docs/UXF/UXF-00.md:L633-L636` | uxf_existing_id | `PASS` | — |
| `UXF-007` | `docs/UXF/UXF-00.md:L639-L642` | uxf_existing_id | `PASS` | — |
| `UXF-008` | `docs/UXF/UXF-00.md:L645-L648` | uxf_existing_id | `PASS` | — |
| `UXF-009` | `docs/UXF/UXF-00.md:L651-L654` | uxf_existing_id | `PASS` | — |
| `UXF-010` | `docs/UXF/UXF-00.md:L657-L660` | uxf_existing_id | `PASS` | — |

## False-negative candidates

- `docs/BRD/BRD-POLICY-INDEX.md:L103` `TABLE` — | Compliance | Chính sách tuân thủ |
- `docs/BRD/BRD-SNAPSHOT-INDEX.md:L123` `TABLE` — | Compliance | Tuân thủ |
- `docs/BRD/BRD-UPDATE-01.md:L274` `TABLE` — | Business Capability | Các Capability cần kích hoạt |
- `docs/BRD/BRD-WS-09.md:L38` `PROSE` — Việc kích hoạt eSIM trên mạng di động (Activation) không thuộc phạm vi Workshop này.
- `docs/BRD/BRD-WS-09.md:L491` `BULLET` — - Two-Factor Authentication (OTP).
- `docs/BRD/BRD-WS-13.md:L416` `PROSE` — Chưa triển khai:
- `docs/BRD/BRD-WS-13.md:L418` `BULLET` — - Machine Learning
- `docs/BRD/BRD-WS-14.md:L559` `BULLET` — - Missing Required Parameter
- `docs/BRD/BRD-WS-17.md:L612` `PROSE` — Version hiện tại chưa triển khai tự động mở rộng tài nguyên.
- `docs/BRD/BRD-WS-17.md:L922` `PROSE` — Version hiện tại chưa triển khai.

## False-positive candidates

- `TMP-BRD-BO-INDEX-023` (`docs/BRD/BRD-BO-INDEX.md:L938`) — Registry entry has no match in the independent semantic candidate scan.
- `TMP-BRD-BO-INDEX-041` (`docs/BRD/BRD-BO-INDEX.md:L960`) — Registry entry has no match in the independent semantic candidate scan.
- `TMP-BRD-BO-INDEX-042` (`docs/BRD/BRD-BO-INDEX.md:L962`) — Registry entry has no match in the independent semantic candidate scan.
- `TMP-BRD-CAP-INDEX-008` (`docs/BRD/BRD-CAP-INDEX.md:L639`) — Registry entry has no match in the independent semantic candidate scan.
- `TMP-BRD-CAP-INDEX-023` (`docs/BRD/BRD-CAP-INDEX.md:L658`) — Registry entry has no match in the independent semantic candidate scan.
- `TMP-BRD-EVENT-INDEX-015` (`docs/BRD/BRD-EVENT-INDEX.md:L779-L781`) — Source section '19. Event Traceability' is navigation/traceability material.
- `TMP-BRD-EVENT-INDEX-016` (`docs/BRD/BRD-EVENT-INDEX.md:L779-L782`) — Source section '19. Event Traceability' is navigation/traceability material.
- `TMP-BRD-EVENT-INDEX-017` (`docs/BRD/BRD-EVENT-INDEX.md:L779-L783`) — Source section '19. Event Traceability' is navigation/traceability material.
- `TMP-BRD-EVENT-INDEX-018` (`docs/BRD/BRD-EVENT-INDEX.md:L779-L784`) — Source section '19. Event Traceability' is navigation/traceability material.
- `TMP-BRD-EVENT-INDEX-019` (`docs/BRD/BRD-EVENT-INDEX.md:L779-L785`) — Source section '19. Event Traceability' is navigation/traceability material.
- `TMP-BRD-EVENT-INDEX-020` (`docs/BRD/BRD-EVENT-INDEX.md:L779-L786`) — Source section '19. Event Traceability' is navigation/traceability material.
- `TMP-BRD-EVENT-INDEX-021` (`docs/BRD/BRD-EVENT-INDEX.md:L779-L787`) — Source section '19. Event Traceability' is navigation/traceability material.
- `TMP-BRD-EVENT-INDEX-022` (`docs/BRD/BRD-EVENT-INDEX.md:L779-L788`) — Source section '19. Event Traceability' is navigation/traceability material.
- `TMP-BRD-EVENT-INDEX-023` (`docs/BRD/BRD-EVENT-INDEX.md:L779-L789`) — Source section '19. Event Traceability' is navigation/traceability material.
- `TMP-BRD-EVENT-INDEX-024` (`docs/BRD/BRD-EVENT-INDEX.md:L779-L790`) — Source section '19. Event Traceability' is navigation/traceability material.
- `TMP-BRD-POLICY-INDEX-011` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L771`) — Source section '21. Policy Traceability' is navigation/traceability material.
- `TMP-BRD-POLICY-INDEX-012` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L772`) — Source section '21. Policy Traceability' is navigation/traceability material.
- `TMP-BRD-POLICY-INDEX-013` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L773`) — Source section '21. Policy Traceability' is navigation/traceability material.
- `TMP-BRD-POLICY-INDEX-014` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L774`) — Source section '21. Policy Traceability' is navigation/traceability material.
- `TMP-BRD-POLICY-INDEX-015` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L775`) — Source section '21. Policy Traceability' is navigation/traceability material.
- `TMP-BRD-POLICY-INDEX-016` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L776`) — Source section '21. Policy Traceability' is navigation/traceability material.
- `TMP-BRD-POLICY-INDEX-017` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L777`) — Source section '21. Policy Traceability' is navigation/traceability material.
- `TMP-BRD-POLICY-INDEX-018` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L778`) — Source section '21. Policy Traceability' is navigation/traceability material.
- `TMP-BRD-POLICY-INDEX-019` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L779`) — Source section '21. Policy Traceability' is navigation/traceability material.
- `TMP-BRD-SNAPSHOT-INDEX-012` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L761-L763`) — Source section '22. Snapshot Traceability' is navigation/traceability material.
- `TMP-BRD-SNAPSHOT-INDEX-013` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L761-L764`) — Source section '22. Snapshot Traceability' is navigation/traceability material.
- `TMP-BRD-SNAPSHOT-INDEX-014` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L761-L765`) — Source section '22. Snapshot Traceability' is navigation/traceability material.
- `TMP-BRD-SNAPSHOT-INDEX-015` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L761-L766`) — Source section '22. Snapshot Traceability' is navigation/traceability material.
- `TMP-BRD-SNAPSHOT-INDEX-016` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L761-L767`) — Source section '22. Snapshot Traceability' is navigation/traceability material.
- `TMP-BRD-SNAPSHOT-INDEX-017` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L761-L768`) — Source section '22. Snapshot Traceability' is navigation/traceability material.
- `TMP-BRD-SNAPSHOT-INDEX-018` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L761-L769`) — Source section '22. Snapshot Traceability' is navigation/traceability material.
- `TMP-BRD-SNAPSHOT-INDEX-019` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L761-L770`) — Source section '22. Snapshot Traceability' is navigation/traceability material.
- `TMP-BRD-SNAPSHOT-INDEX-020` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L761-L771`) — Source section '22. Snapshot Traceability' is navigation/traceability material.
- `TMP-BRD-SNAPSHOT-INDEX-021` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L761-L772`) — Source section '22. Snapshot Traceability' is navigation/traceability material.
- `TMP-BRD-WS-01-037` (`docs/BRD/BRD-WS-01.md:L327`) — Source section 'Impact to Future DIP' is navigation/traceability material.
- `TMP-BRD-WS-01-038` (`docs/BRD/BRD-WS-01.md:L328`) — Source section 'Impact to Future DIP' is navigation/traceability material.
- `TMP-BRD-WS-01-039` (`docs/BRD/BRD-WS-01.md:L329`) — Source section 'Impact to Future DIP' is navigation/traceability material.
- `TMP-BRD-WS-01-040` (`docs/BRD/BRD-WS-01.md:L330`) — Source section 'Impact to Future DIP' is navigation/traceability material.
- `TMP-BRD-WS-01-041` (`docs/BRD/BRD-WS-01.md:L331`) — Source section 'Impact to Future DIP' is navigation/traceability material.
- `TMP-BRD-WS-02-001` (`docs/BRD/BRD-WS-02.md:L67`) — Registry entry has no match in the independent semantic candidate scan.
- `TMP-BRD-WS-06-029` (`docs/BRD/BRD-WS-06.md:L462`) — Registry entry has no match in the independent semantic candidate scan.
- `TMP-UXF-00-032` (`docs/UXF/UXF-00.md:L677-L679`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-00-033` (`docs/UXF/UXF-00.md:L677-L680`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-00-034` (`docs/UXF/UXF-00.md:L677-L681`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-00-035` (`docs/UXF/UXF-00.md:L677-L682`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-00-036` (`docs/UXF/UXF-00.md:L677-L683`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-00-037` (`docs/UXF/UXF-00.md:L677-L684`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-00-038` (`docs/UXF/UXF-00.md:L677-L685`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-00-039` (`docs/UXF/UXF-00.md:L677-L686`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-00-040` (`docs/UXF/UXF-00.md:L677-L687`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-00-041` (`docs/UXF/UXF-00.md:L677-L688`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-01-012` (`docs/UXF/UXF-01.md:L741-L743`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-01-013` (`docs/UXF/UXF-01.md:L741-L744`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-01-014` (`docs/UXF/UXF-01.md:L741-L745`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-01-015` (`docs/UXF/UXF-01.md:L741-L746`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-01-016` (`docs/UXF/UXF-01.md:L741-L747`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-01-017` (`docs/UXF/UXF-01.md:L741-L749`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-01-018` (`docs/UXF/UXF-01.md:L741-L750`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-01-019` (`docs/UXF/UXF-01.md:L741-L751`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-01-020` (`docs/UXF/UXF-01.md:L741-L752`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-01-021` (`docs/UXF/UXF-01.md:L741-L753`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-02-010` (`docs/UXF/UXF-02.md:L624-L626`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-02-011` (`docs/UXF/UXF-02.md:L624-L627`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-02-012` (`docs/UXF/UXF-02.md:L624-L628`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-02-013` (`docs/UXF/UXF-02.md:L624-L629`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-02-014` (`docs/UXF/UXF-02.md:L624-L630`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-02-015` (`docs/UXF/UXF-02.md:L624-L631`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-02-016` (`docs/UXF/UXF-02.md:L624-L632`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-02-017` (`docs/UXF/UXF-02.md:L624-L633`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-02-018` (`docs/UXF/UXF-02.md:L624-L634`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-02-019` (`docs/UXF/UXF-02.md:L624-L635`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-02-020` (`docs/UXF/UXF-02.md:L641-L643`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-02-021` (`docs/UXF/UXF-02.md:L641-L644`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-02-022` (`docs/UXF/UXF-02.md:L641-L645`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-02-023` (`docs/UXF/UXF-02.md:L641-L646`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-02-024` (`docs/UXF/UXF-02.md:L641-L647`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-02-025` (`docs/UXF/UXF-02.md:L641-L649`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-02-026` (`docs/UXF/UXF-02.md:L641-L650`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-02-027` (`docs/UXF/UXF-02.md:L641-L651`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-02-028` (`docs/UXF/UXF-02.md:L641-L652`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-02-029` (`docs/UXF/UXF-02.md:L641-L653`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-03-008` (`docs/UXF/UXF-03.md:L611-L613`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-03-009` (`docs/UXF/UXF-03.md:L611-L614`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-03-010` (`docs/UXF/UXF-03.md:L611-L615`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-03-011` (`docs/UXF/UXF-03.md:L611-L616`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-03-012` (`docs/UXF/UXF-03.md:L611-L617`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-03-013` (`docs/UXF/UXF-03.md:L611-L618`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-03-014` (`docs/UXF/UXF-03.md:L611-L619`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-03-015` (`docs/UXF/UXF-03.md:L611-L620`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-03-016` (`docs/UXF/UXF-03.md:L611-L621`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-03-017` (`docs/UXF/UXF-03.md:L689-L691`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-03-018` (`docs/UXF/UXF-03.md:L689-L692`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-03-019` (`docs/UXF/UXF-03.md:L689-L693`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-03-020` (`docs/UXF/UXF-03.md:L689-L694`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-03-021` (`docs/UXF/UXF-03.md:L689-L695`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-03-022` (`docs/UXF/UXF-03.md:L689-L697`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-03-023` (`docs/UXF/UXF-03.md:L689-L698`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-03-024` (`docs/UXF/UXF-03.md:L689-L699`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-03-025` (`docs/UXF/UXF-03.md:L689-L700`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-03-026` (`docs/UXF/UXF-03.md:L689-L701`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-04-015` (`docs/UXF/UXF-04.md:L602-L604`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-04-016` (`docs/UXF/UXF-04.md:L602-L605`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-04-017` (`docs/UXF/UXF-04.md:L602-L606`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-04-018` (`docs/UXF/UXF-04.md:L602-L607`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-04-019` (`docs/UXF/UXF-04.md:L602-L608`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-04-020` (`docs/UXF/UXF-04.md:L602-L609`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-04-021` (`docs/UXF/UXF-04.md:L602-L610`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-04-022` (`docs/UXF/UXF-04.md:L602-L611`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-04-023` (`docs/UXF/UXF-04.md:L602-L612`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-04-024` (`docs/UXF/UXF-04.md:L680-L682`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-04-025` (`docs/UXF/UXF-04.md:L680-L683`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-04-026` (`docs/UXF/UXF-04.md:L680-L684`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-04-027` (`docs/UXF/UXF-04.md:L680-L685`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-04-028` (`docs/UXF/UXF-04.md:L680-L686`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-04-029` (`docs/UXF/UXF-04.md:L680-L688`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-04-030` (`docs/UXF/UXF-04.md:L680-L689`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-04-031` (`docs/UXF/UXF-04.md:L680-L690`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-04-032` (`docs/UXF/UXF-04.md:L680-L691`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-04-033` (`docs/UXF/UXF-04.md:L680-L692`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-05-023` (`docs/UXF/UXF-05.md:L617-L619`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-05-024` (`docs/UXF/UXF-05.md:L621`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-05-025` (`docs/UXF/UXF-05.md:L623`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-05-026` (`docs/UXF/UXF-05.md:L625`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-05-027` (`docs/UXF/UXF-05.md:L627-L629`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-05-028` (`docs/UXF/UXF-05.md:L627-L630`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-05-029` (`docs/UXF/UXF-05.md:L627-L631`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-05-030` (`docs/UXF/UXF-05.md:L633`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-05-031` (`docs/UXF/UXF-05.md:L635`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-05-032` (`docs/UXF/UXF-05.md:L637`) — Source section is an implementation guideline; requirement ownership/classification needs review.
- `TMP-UXF-05-043` (`docs/UXF/UXF-05.md:L719`) — Registry entry has no match in the independent semantic candidate scan.
- `TMP-UXF-05-044` (`docs/UXF/UXF-05.md:L725-L727`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-05-045` (`docs/UXF/UXF-05.md:L725-L728`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-05-046` (`docs/UXF/UXF-05.md:L725-L729`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-05-047` (`docs/UXF/UXF-05.md:L725-L730`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-05-048` (`docs/UXF/UXF-05.md:L725-L731`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-05-049` (`docs/UXF/UXF-05.md:L725-L733`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-05-050` (`docs/UXF/UXF-05.md:L725-L734`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-05-051` (`docs/UXF/UXF-05.md:L725-L735`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-05-052` (`docs/UXF/UXF-05.md:L725-L736`) — Reference-list instruction is documentation navigation, not a product requirement.
- `TMP-UXF-05-053` (`docs/UXF/UXF-05.md:L725-L737`) — Reference-list instruction is documentation navigation, not a product requirement.

## Compound statement candidates

- `TMP-BRD-BO-INDEX-001` (`docs/BRD/BRD-BO-INDEX.md:L108`): bullets=0, normative signals=2
- `TMP-BRD-BO-INDEX-004` (`docs/BRD/BRD-BO-INDEX.md:L156-L158`): bullets=1, normative signals=2
- `TMP-BRD-BO-INDEX-005` (`docs/BRD/BRD-BO-INDEX.md:L156-L159`): bullets=1, normative signals=2
- `TMP-BRD-BO-INDEX-006` (`docs/BRD/BRD-BO-INDEX.md:L156-L160`): bullets=1, normative signals=2
- `TMP-BRD-BO-INDEX-007` (`docs/BRD/BRD-BO-INDEX.md:L156-L161`): bullets=1, normative signals=2
- `TMP-BRD-BO-INDEX-008` (`docs/BRD/BRD-BO-INDEX.md:L167`): bullets=0, normative signals=2
- `BO-P04` (`docs/BRD/BRD-BO-INDEX.md:L257-L268`): bullets=5, normative signals=1
- `BO-P06` (`docs/BRD/BRD-BO-INDEX.md:L279-L284`): bullets=0, normative signals=2
- `BO-P07` (`docs/BRD/BRD-BO-INDEX.md:L287-L298`): bullets=5, normative signals=1
- `BO-R03` (`docs/BRD/BRD-BO-INDEX.md:L728-L733`): bullets=0, normative signals=2
- `BO-R05` (`docs/BRD/BRD-BO-INDEX.md:L746-L755`): bullets=3, normative signals=1
- `CAP-P08` (`docs/BRD/BRD-CAP-INDEX.md:L331-L342`): bullets=5, normative signals=1
- `CAP-R07` (`docs/BRD/BRD-CAP-INDEX.md:L761-L769`): bullets=4, normative signals=0
- `EVT-P06` (`docs/BRD/BRD-EVENT-INDEX.md:L334-L342`): bullets=4, normative signals=1
- `EVT-P08` (`docs/BRD/BRD-EVENT-INDEX.md:L353-L364`): bullets=5, normative signals=1
- `EVT-C02` (`docs/BRD/BRD-EVENT-INDEX.md:L727-L733`): bullets=2, normative signals=0
- `TMP-BRD-META-MODEL-002` (`docs/BRD/BRD-META-MODEL.md:L292`): bullets=0, normative signals=3
- `POL-P10` (`docs/BRD/BRD-POLICY-INDEX.md:L385-L396`): bullets=5, normative signals=1
- `TMP-BRD-POLICY-INDEX-010` (`docs/BRD/BRD-POLICY-INDEX.md:L685-L689`): bullets=3, normative signals=3
- `SNP-P08` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L365-L375`): bullets=4, normative signals=1
- `TMP-BRD-SNAPSHOT-INDEX-008` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L586`): bullets=0, normative signals=2
- `TMP-BRD-SNAPSHOT-INDEX-011` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L750-L755`): bullets=4, normative signals=1
- `BD-02-007` (`docs/BRD/BRD-WS-02.md:L528-L537`): bullets=0, normative signals=2
- `TMP-BRD-WS-03-008` (`docs/BRD/BRD-WS-03.md:L332`): bullets=0, normative signals=2
- `TMP-BRD-WS-03-010` (`docs/BRD/BRD-WS-03.md:L401`): bullets=0, normative signals=2
- `BD-03-011` (`docs/BRD/BRD-WS-03.md:L583-L592`): bullets=3, normative signals=0
- `BD-04-001` (`docs/BRD/BRD-WS-04.md:L521-L529`): bullets=4, normative signals=0
- `BD-04-005` (`docs/BRD/BRD-WS-04.md:L552-L562`): bullets=6, normative signals=1
- `TMP-BRD-WS-05-010` (`docs/BRD/BRD-WS-05.md:L208-L212`): bullets=3, normative signals=1
- `TMP-BRD-WS-05-017` (`docs/BRD/BRD-WS-05.md:L273-L276`): bullets=1, normative signals=2
- `TMP-BRD-WS-07-010` (`docs/BRD/BRD-WS-07.md:L439-L442`): bullets=2, normative signals=1
- `TMP-BRD-WS-07-012` (`docs/BRD/BRD-WS-07.md:L491-L496`): bullets=4, normative signals=1
- `BD-07-009` (`docs/BRD/BRD-WS-07.md:L686-L689`): bullets=0, normative signals=2
- `TMP-BRD-WS-08-003` (`docs/BRD/BRD-WS-08.md:L110-L113`): bullets=2, normative signals=1
- `TMP-BRD-WS-11-009` (`docs/BRD/BRD-WS-11.md:L488-L492`): bullets=3, normative signals=1
- `BD-11-006` (`docs/BRD/BRD-WS-11.md:L644-L651`): bullets=3, normative signals=0
- `TMP-BRD-WS-13-006` (`docs/BRD/BRD-WS-13.md:L380`): bullets=0, normative signals=2
- `BD-13-001` (`docs/BRD/BRD-WS-13.md:L767-L776`): bullets=5, normative signals=0
- `BD-13-002` (`docs/BRD/BRD-WS-13.md:L779-L788`): bullets=5, normative signals=0
- `BD-13-006` (`docs/BRD/BRD-WS-13.md:L827-L836`): bullets=5, normative signals=0
- `BD-13-007` (`docs/BRD/BRD-WS-13.md:L839-L848`): bullets=5, normative signals=0
- `BD-13-010` (`docs/BRD/BRD-WS-13.md:L865-L883`): bullets=9, normative signals=0
- `BD-13-011` (`docs/BRD/BRD-WS-13.md:L886-L894`): bullets=2, normative signals=0
- `BD-13-012` (`docs/BRD/BRD-WS-13.md:L897-L906`): bullets=3, normative signals=1
- `BD-13-013` (`docs/BRD/BRD-WS-13.md:L909-L920`): bullets=5, normative signals=0
- `BD-13-014` (`docs/BRD/BRD-WS-13.md:L923-L932`): bullets=3, normative signals=0
- `BD-13-017` (`docs/BRD/BRD-WS-13.md:L951-L956`): bullets=0, normative signals=2
- `BD-13-019` (`docs/BRD/BRD-WS-13.md:L967-L978`): bullets=5, normative signals=0
- `EP-13-002` (`docs/BRD/BRD-WS-13.md:L1001-L1012`): bullets=5, normative signals=1
- `EP-13-007` (`docs/BRD/BRD-WS-13.md:L1051-L1067`): bullets=9, normative signals=0
- `TMP-BRD-WS-14-002` (`docs/BRD/BRD-WS-14.md:L124-L128`): bullets=3, normative signals=2
- `TMP-BRD-WS-14-012` (`docs/BRD/BRD-WS-14.md:L369-L384`): bullets=14, normative signals=1
- `TMP-BRD-WS-14-026` (`docs/BRD/BRD-WS-14.md:L664`): bullets=0, normative signals=2
- `TMP-BRD-WS-14-027` (`docs/BRD/BRD-WS-14.md:L738-L743`): bullets=4, normative signals=1
- `TMP-BRD-WS-14-030` (`docs/BRD/BRD-WS-14.md:L755-L766`): bullets=10, normative signals=1
- `BD-14-001` (`docs/BRD/BRD-WS-14.md:L859-L869`): bullets=6, normative signals=0
- `BD-14-003` (`docs/BRD/BRD-WS-14.md:L880-L892`): bullets=4, normative signals=0
- `BD-14-007` (`docs/BRD/BRD-WS-14.md:L923-L937`): bullets=8, normative signals=0
- `BD-14-008` (`docs/BRD/BRD-WS-14.md:L940-L949`): bullets=3, normative signals=0
- `BD-14-010` (`docs/BRD/BRD-WS-14.md:L960-L971`): bullets=5, normative signals=0
- `BD-14-012` (`docs/BRD/BRD-WS-14.md:L982-L995`): bullets=7, normative signals=0
- `BD-14-015` (`docs/BRD/BRD-WS-14.md:L1032-L1038`): bullets=2, normative signals=0
- `BD-14-016` (`docs/BRD/BRD-WS-14.md:L1041-L1051`): bullets=6, normative signals=0
- `BD-14-017` (`docs/BRD/BRD-WS-14.md:L1054-L1064`): bullets=4, normative signals=1
- `BD-14-018` (`docs/BRD/BRD-WS-14.md:L1067-L1078`): bullets=7, normative signals=0
- `BD-14-019` (`docs/BRD/BRD-WS-14.md:L1081-L1088`): bullets=3, normative signals=0
- `BD-14-020` (`docs/BRD/BRD-WS-14.md:L1091-L1098`): bullets=3, normative signals=0
- `BD-14-022` (`docs/BRD/BRD-WS-14.md:L1109-L1126`): bullets=11, normative signals=0
- `BD-14-024` (`docs/BRD/BRD-WS-14.md:L1137-L1151`): bullets=10, normative signals=1
- `BD-14-025` (`docs/BRD/BRD-WS-14.md:L1154-L1175`): bullets=15, normative signals=0
- `BD-14-026` (`docs/BRD/BRD-WS-14.md:L1178-L1187`): bullets=5, normative signals=0
- `EP-14-006` (`docs/BRD/BRD-WS-14.md:L1222-L1229`): bullets=3, normative signals=1
- `BD-15-001` (`docs/BRD/BRD-WS-15.md:L873-L883`): bullets=6, normative signals=0
- `BD-15-002` (`docs/BRD/BRD-WS-15.md:L886-L891`): bullets=0, normative signals=2
- `BD-15-004` (`docs/BRD/BRD-WS-15.md:L904-L921`): bullets=8, normative signals=0
- `BD-15-005` (`docs/BRD/BRD-WS-15.md:L924-L935`): bullets=5, normative signals=0
- `BD-15-009` (`docs/BRD/BRD-WS-15.md:L964-L975`): bullets=3, normative signals=0
- `BD-15-011` (`docs/BRD/BRD-WS-15.md:L984-L994`): bullets=4, normative signals=0
- `BD-15-013` (`docs/BRD/BRD-WS-15.md:L1005-L1015`): bullets=4, normative signals=0
- `BD-15-014` (`docs/BRD/BRD-WS-15.md:L1018-L1025`): bullets=3, normative signals=0
- `BD-15-016` (`docs/BRD/BRD-WS-15.md:L1036-L1044`): bullets=4, normative signals=0
- `BD-15-018` (`docs/BRD/BRD-WS-15.md:L1055-L1064`): bullets=3, normative signals=0
- `BD-15-019` (`docs/BRD/BRD-WS-15.md:L1067-L1076`): bullets=5, normative signals=0
- `BD-15-020` (`docs/BRD/BRD-WS-15.md:L1079-L1086`): bullets=3, normative signals=0
- `BD-15-023` (`docs/BRD/BRD-WS-15.md:L1101-L1114`): bullets=7, normative signals=0
- `BD-15-026` (`docs/BRD/BRD-WS-15.md:L1129-L1142`): bullets=7, normative signals=0
- `BD-15-029` (`docs/BRD/BRD-WS-15.md:L1163-L1174`): bullets=7, normative signals=0
- `BD-15-030` (`docs/BRD/BRD-WS-15.md:L1177-L1187`): bullets=4, normative signals=0
- `TMP-BRD-WS-16-009` (`docs/BRD/BRD-WS-16.md:L597-L602`): bullets=4, normative signals=2
- `BD-16-001` (`docs/BRD/BRD-WS-16.md:L760-L775`): bullets=7, normative signals=0
- `BD-16-002` (`docs/BRD/BRD-WS-16.md:L778-L792`): bullets=8, normative signals=0
- `BD-16-003` (`docs/BRD/BRD-WS-16.md:L795-L806`): bullets=5, normative signals=0
- `BD-16-004` (`docs/BRD/BRD-WS-16.md:L809-L817`): bullets=2, normative signals=0
- `BD-16-006` (`docs/BRD/BRD-WS-16.md:L828-L841`): bullets=7, normative signals=0
- `BD-16-007` (`docs/BRD/BRD-WS-16.md:L844-L854`): bullets=4, normative signals=0
- `BD-16-009` (`docs/BRD/BRD-WS-16.md:L865-L875`): bullets=4, normative signals=0
- `BD-16-010` (`docs/BRD/BRD-WS-16.md:L878-L887`): bullets=3, normative signals=0
- `BD-16-012` (`docs/BRD/BRD-WS-16.md:L898-L909`): bullets=5, normative signals=0
- `BD-16-018` (`docs/BRD/BRD-WS-16.md:L954-L963`): bullets=3, normative signals=0
- `BD-16-025` (`docs/BRD/BRD-WS-16.md:L1012-L1022`): bullets=4, normative signals=0
- `EP-16-001` (`docs/BRD/BRD-WS-16.md:L1057-L1068`): bullets=5, normative signals=0
- `EP-16-006` (`docs/BRD/BRD-WS-16.md:L1103-L1112`): bullets=5, normative signals=0
- `EP-16-010` (`docs/BRD/BRD-WS-16.md:L1133-L1146`): bullets=9, normative signals=1
- `TMP-BRD-WS-17-005` (`docs/BRD/BRD-WS-17.md:L545-L549`): bullets=3, normative signals=1
- `BD-17-002` (`docs/BRD/BRD-WS-17.md:L975-L992`): bullets=11, normative signals=0
- `BD-17-004` (`docs/BRD/BRD-WS-17.md:L1003-L1014`): bullets=5, normative signals=0
- `BD-17-007` (`docs/BRD/BRD-WS-17.md:L1035-L1045`): bullets=4, normative signals=0
- `BD-17-010` (`docs/BRD/BRD-WS-17.md:L1064-L1076`): bullets=6, normative signals=0
- `BD-17-014` (`docs/BRD/BRD-WS-17.md:L1099-L1108`): bullets=3, normative signals=0
- `EP-17-008` (`docs/BRD/BRD-WS-17.md:L1281-L1288`): bullets=3, normative signals=2
- `EP-17-010` (`docs/BRD/BRD-WS-17.md:L1297-L1308`): bullets=5, normative signals=1
- `TMP-UXF-00-016` (`docs/UXF/UXF-00.md:L542`): bullets=0, normative signals=2
- `TMP-UXF-02-010` (`docs/UXF/UXF-02.md:L624-L626`): bullets=1, normative signals=2
- `TMP-UXF-02-011` (`docs/UXF/UXF-02.md:L624-L627`): bullets=1, normative signals=2
- `TMP-UXF-02-012` (`docs/UXF/UXF-02.md:L624-L628`): bullets=1, normative signals=2
- `TMP-UXF-02-013` (`docs/UXF/UXF-02.md:L624-L629`): bullets=1, normative signals=2
- `TMP-UXF-02-014` (`docs/UXF/UXF-02.md:L624-L630`): bullets=1, normative signals=2
- `TMP-UXF-02-015` (`docs/UXF/UXF-02.md:L624-L631`): bullets=1, normative signals=2
- `TMP-UXF-02-016` (`docs/UXF/UXF-02.md:L624-L632`): bullets=1, normative signals=2
- `TMP-UXF-02-017` (`docs/UXF/UXF-02.md:L624-L633`): bullets=1, normative signals=2
- `TMP-UXF-02-018` (`docs/UXF/UXF-02.md:L624-L634`): bullets=1, normative signals=2
- `TMP-UXF-03-008` (`docs/UXF/UXF-03.md:L611-L613`): bullets=1, normative signals=2
- `TMP-UXF-03-009` (`docs/UXF/UXF-03.md:L611-L614`): bullets=1, normative signals=2
- `TMP-UXF-03-010` (`docs/UXF/UXF-03.md:L611-L615`): bullets=1, normative signals=2
- `TMP-UXF-03-011` (`docs/UXF/UXF-03.md:L611-L616`): bullets=1, normative signals=2
- `TMP-UXF-03-016` (`docs/UXF/UXF-03.md:L611-L621`): bullets=1, normative signals=2
- `TMP-UXF-04-003` (`docs/UXF/UXF-04.md:L230`): bullets=0, normative signals=2
- `TMP-UXF-04-007` (`docs/UXF/UXF-04.md:L556-L563`): bullets=6, normative signals=1
- `TMP-UXF-04-015` (`docs/UXF/UXF-04.md:L602-L604`): bullets=1, normative signals=2
- `TMP-UXF-04-016` (`docs/UXF/UXF-04.md:L602-L605`): bullets=1, normative signals=2
- `TMP-UXF-04-017` (`docs/UXF/UXF-04.md:L602-L606`): bullets=1, normative signals=2
- `TMP-UXF-04-018` (`docs/UXF/UXF-04.md:L602-L607`): bullets=1, normative signals=2
- `TMP-UXF-04-019` (`docs/UXF/UXF-04.md:L602-L608`): bullets=1, normative signals=2
- `TMP-UXF-04-020` (`docs/UXF/UXF-04.md:L602-L609`): bullets=1, normative signals=2
- `TMP-UXF-04-021` (`docs/UXF/UXF-04.md:L602-L610`): bullets=1, normative signals=2
- `TMP-UXF-04-022` (`docs/UXF/UXF-04.md:L602-L611`): bullets=1, normative signals=2
- `TMP-UXF-05-023` (`docs/UXF/UXF-05.md:L617-L619`): bullets=0, normative signals=2

## Acceptance mapping

- Distribution: `{"INFERRED_ONLY": 1177, "MISSING": 132}`
- `acceptance_present` is true only for `DIRECT` or `LINKED`.
- `INFERRED_ONLY` records testability without inventing acceptance criteria.

## Scope provenance

- Distribution: `{"BASELINE_INHERITANCE": 1168, "FRAMEWORK_DECISION": 8, "SOURCE_EXPLICIT": 133}`
- Non-active source scope uses `SOURCE_EXPLICIT` with a source anchor.
- SD-03/UXD-11 promotions use `FRAMEWORK_DECISION` with the decision ID.
- Default inherited active scope uses `BASELINE_INHERITANCE`.

## Independent raw reference validation

- Canonical IDs: **576**
- Definitions: **576**
- Valid raw references excluding definitions: **0**
- Dangling raw references: **0**
- Ambiguous ID-like tokens: **559** unique / **633** occurrences
- Prose references absent from `referenced_requirements`: **0**

Ambiguous ID-like token inventory:

- `BO-0001`: 2 occurrence(s)
- `BO-0002`: 2 occurrence(s)
- `BO-0003`: 2 occurrence(s)
- `BO-0004`: 1 occurrence(s)
- `BO-0005`: 1 occurrence(s)
- `BO-0006`: 1 occurrence(s)
- `BO-0007`: 1 occurrence(s)
- `BO-0008`: 1 occurrence(s)
- `BO-0009`: 1 occurrence(s)
- `BO-0010`: 1 occurrence(s)
- `BO-0011`: 1 occurrence(s)
- `BO-0012`: 1 occurrence(s)
- `BO-0013`: 1 occurrence(s)
- `BO-0014`: 1 occurrence(s)
- `BO-0015`: 1 occurrence(s)
- `BO-0101`: 1 occurrence(s)
- `BO-0102`: 1 occurrence(s)
- `BO-0103`: 1 occurrence(s)
- `BO-0104`: 1 occurrence(s)
- `BO-0105`: 1 occurrence(s)
- `BO-0106`: 1 occurrence(s)
- `BO-0107`: 1 occurrence(s)
- `BO-0108`: 1 occurrence(s)
- `BO-0201`: 1 occurrence(s)
- `BO-0202`: 1 occurrence(s)
- `BO-0203`: 1 occurrence(s)
- `BO-0204`: 1 occurrence(s)
- `BO-0205`: 1 occurrence(s)
- `BO-0206`: 1 occurrence(s)
- `BO-0207`: 1 occurrence(s)
- `BO-0208`: 1 occurrence(s)
- `BO-0209`: 1 occurrence(s)
- `BO-0210`: 1 occurrence(s)
- `BO-0301`: 1 occurrence(s)
- `BO-0302`: 1 occurrence(s)
- `BO-0303`: 1 occurrence(s)
- `BO-0304`: 1 occurrence(s)
- `BO-0305`: 1 occurrence(s)
- `BO-0306`: 1 occurrence(s)
- `BO-0307`: 1 occurrence(s)
- `BO-0308`: 1 occurrence(s)
- `BO-0309`: 1 occurrence(s)
- `BO-0401`: 1 occurrence(s)
- `BO-0402`: 1 occurrence(s)
- `BO-0403`: 1 occurrence(s)
- `BO-0404`: 1 occurrence(s)
- `BO-0405`: 1 occurrence(s)
- `BO-0406`: 1 occurrence(s)
- `BO-0407`: 1 occurrence(s)
- `BO-0408`: 1 occurrence(s)
- `BO-0501`: 1 occurrence(s)
- `BO-0502`: 1 occurrence(s)
- `BO-0503`: 1 occurrence(s)
- `BO-0504`: 1 occurrence(s)
- `BO-0505`: 1 occurrence(s)
- `BO-0506`: 1 occurrence(s)
- `BO-0507`: 1 occurrence(s)
- `BO-0508`: 1 occurrence(s)
- `BO-0601`: 1 occurrence(s)
- `BO-0602`: 1 occurrence(s)
- `BO-0603`: 1 occurrence(s)
- `BO-0604`: 1 occurrence(s)
- `BO-0605`: 1 occurrence(s)
- `BO-0606`: 1 occurrence(s)
- `BO-0607`: 1 occurrence(s)
- `BO-0608`: 1 occurrence(s)
- `BO-0701`: 1 occurrence(s)
- `BO-0702`: 1 occurrence(s)
- `BO-0703`: 1 occurrence(s)
- `BO-0704`: 1 occurrence(s)
- `BO-0705`: 1 occurrence(s)
- `BO-0706`: 1 occurrence(s)
- `BO-0707`: 1 occurrence(s)
- `BO-0708`: 1 occurrence(s)
- `BO-0709`: 1 occurrence(s)
- `BO-0710`: 1 occurrence(s)
- `BO-0711`: 1 occurrence(s)
- `BO-0801`: 1 occurrence(s)
- `BO-0802`: 1 occurrence(s)
- `BO-0803`: 1 occurrence(s)
- `BO-0804`: 1 occurrence(s)
- `BO-0805`: 1 occurrence(s)
- `BO-0806`: 1 occurrence(s)
- `BO-0807`: 1 occurrence(s)
- `BO-0808`: 1 occurrence(s)
- `BO-0809`: 1 occurrence(s)
- `BO-0810`: 1 occurrence(s)
- `BO-0901`: 1 occurrence(s)
- `BO-0902`: 1 occurrence(s)
- `BO-0903`: 1 occurrence(s)
- `BO-0904`: 1 occurrence(s)
- `BO-0905`: 1 occurrence(s)
- `BO-0906`: 1 occurrence(s)
- `BO-0907`: 1 occurrence(s)
- `BO-0908`: 1 occurrence(s)
- `BO-0909`: 1 occurrence(s)
- `BO-0910`: 1 occurrence(s)
- `BO-0911`: 1 occurrence(s)
- `BO-0912`: 1 occurrence(s)
- `BO-1001`: 1 occurrence(s)
- `BO-1002`: 1 occurrence(s)
- `BO-1003`: 1 occurrence(s)
- `BO-1004`: 1 occurrence(s)
- `BO-1005`: 1 occurrence(s)
- `BO-1006`: 1 occurrence(s)
- `BO-1007`: 1 occurrence(s)
- `BO-1008`: 1 occurrence(s)
- `BO-1009`: 1 occurrence(s)
- `BO-1101`: 1 occurrence(s)
- `BO-1102`: 1 occurrence(s)
- `BO-1103`: 1 occurrence(s)
- `BO-1104`: 1 occurrence(s)
- `BO-1105`: 1 occurrence(s)
- `BO-1106`: 1 occurrence(s)
- `BO-1107`: 1 occurrence(s)
- `BO-1108`: 1 occurrence(s)
- `BO-1109`: 1 occurrence(s)
- `BO-1201`: 1 occurrence(s)
- `BO-1202`: 1 occurrence(s)
- `BO-1203`: 1 occurrence(s)
- `BO-1204`: 1 occurrence(s)
- `BO-1205`: 1 occurrence(s)
- `BO-1206`: 1 occurrence(s)
- `BO-1207`: 1 occurrence(s)
- `BO-1301`: 1 occurrence(s)
- `BO-1302`: 1 occurrence(s)
- `BO-1303`: 1 occurrence(s)
- `BO-1304`: 1 occurrence(s)
- `BO-1305`: 1 occurrence(s)
- `BO-1306`: 1 occurrence(s)
- `BO-1307`: 1 occurrence(s)
- `BO-1308`: 1 occurrence(s)
- `BO-1309`: 1 occurrence(s)
- `BO-1310`: 1 occurrence(s)
- `BO-1401`: 1 occurrence(s)
- `BO-1402`: 1 occurrence(s)
- `BO-1403`: 1 occurrence(s)
- `BO-1404`: 1 occurrence(s)
- `BO-1405`: 1 occurrence(s)
- `BO-1406`: 1 occurrence(s)
- `BO-1407`: 1 occurrence(s)
- `BO-1501`: 1 occurrence(s)
- `BO-1502`: 1 occurrence(s)
- `BO-1503`: 1 occurrence(s)
- `BO-1504`: 1 occurrence(s)
- `BO-1505`: 1 occurrence(s)
- `BO-1506`: 1 occurrence(s)
- `BO-1507`: 1 occurrence(s)
- `BO-1508`: 1 occurrence(s)
- `BO-1509`: 1 occurrence(s)
- `BO-1510`: 1 occurrence(s)
- `BO-1511`: 1 occurrence(s)
- `BO-1512`: 1 occurrence(s)
- `BO-1513`: 1 occurrence(s)
- `BO-9001`: 1 occurrence(s)
- `BO-9002`: 1 occurrence(s)
- `BO-9003`: 1 occurrence(s)
- `BO-9004`: 1 occurrence(s)
- `BO-9005`: 1 occurrence(s)
- `BO-9006`: 1 occurrence(s)
- `BO-9007`: 1 occurrence(s)
- `BO-9008`: 1 occurrence(s)
- `BO-9009`: 1 occurrence(s)
- `BO-9010`: 1 occurrence(s)
- `BO-9501`: 1 occurrence(s)
- `BO-9502`: 1 occurrence(s)
- `BO-9503`: 1 occurrence(s)
- `BO-9504`: 1 occurrence(s)
- `BO-9505`: 1 occurrence(s)
- `BO-9506`: 1 occurrence(s)
- `BO-9507`: 1 occurrence(s)
- `BO-9801`: 1 occurrence(s)
- `BO-9802`: 1 occurrence(s)
- `BO-9803`: 1 occurrence(s)
- `BO-9804`: 1 occurrence(s)
- `BO-9805`: 1 occurrence(s)
- `BO-9806`: 1 occurrence(s)
- `BO-9807`: 1 occurrence(s)
- `BO-9808`: 1 occurrence(s)
- `BO-9809`: 1 occurrence(s)
- `BO-INDEX`: 10 occurrence(s)
- `CAP-0001`: 2 occurrence(s)
- `CAP-0002`: 2 occurrence(s)
- `CAP-0003`: 2 occurrence(s)
- `CAP-0004`: 1 occurrence(s)
- `CAP-0005`: 1 occurrence(s)
- `CAP-0006`: 1 occurrence(s)
- `CAP-0007`: 1 occurrence(s)
- `CAP-0008`: 1 occurrence(s)
- `CAP-0009`: 1 occurrence(s)
- `CAP-0010`: 1 occurrence(s)
- `CAP-0101`: 1 occurrence(s)
- `CAP-0102`: 1 occurrence(s)
- `CAP-0103`: 1 occurrence(s)
- `CAP-0104`: 1 occurrence(s)
- `CAP-0105`: 1 occurrence(s)
- `CAP-0106`: 1 occurrence(s)
- `CAP-0107`: 1 occurrence(s)
- `CAP-0108`: 1 occurrence(s)
- `CAP-0201`: 1 occurrence(s)
- `CAP-0202`: 1 occurrence(s)
- `CAP-0203`: 1 occurrence(s)
- `CAP-0204`: 1 occurrence(s)
- `CAP-0205`: 1 occurrence(s)
- `CAP-0206`: 1 occurrence(s)
- `CAP-0207`: 1 occurrence(s)
- `CAP-0208`: 1 occurrence(s)
- `CAP-0301`: 1 occurrence(s)
- `CAP-0302`: 1 occurrence(s)
- `CAP-0303`: 1 occurrence(s)
- `CAP-0304`: 1 occurrence(s)
- `CAP-0305`: 1 occurrence(s)
- `CAP-0306`: 1 occurrence(s)
- `CAP-0401`: 1 occurrence(s)
- `CAP-0402`: 1 occurrence(s)
- `CAP-0403`: 1 occurrence(s)
- `CAP-0404`: 1 occurrence(s)
- `CAP-0405`: 1 occurrence(s)
- `CAP-0406`: 1 occurrence(s)
- `CAP-0501`: 1 occurrence(s)
- `CAP-0502`: 1 occurrence(s)
- `CAP-0503`: 1 occurrence(s)
- `CAP-0504`: 1 occurrence(s)
- `CAP-0505`: 1 occurrence(s)
- `CAP-0506`: 1 occurrence(s)
- `CAP-0507`: 1 occurrence(s)
- `CAP-0601`: 1 occurrence(s)
- `CAP-0602`: 1 occurrence(s)
- `CAP-0603`: 1 occurrence(s)
- `CAP-0604`: 1 occurrence(s)
- `CAP-0605`: 1 occurrence(s)
- `CAP-0606`: 1 occurrence(s)
- `CAP-0607`: 1 occurrence(s)
- `CAP-0701`: 1 occurrence(s)
- `CAP-0702`: 1 occurrence(s)
- `CAP-0703`: 1 occurrence(s)
- `CAP-0704`: 1 occurrence(s)
- `CAP-0705`: 1 occurrence(s)
- `CAP-0706`: 1 occurrence(s)
- `CAP-0707`: 1 occurrence(s)
- `CAP-0708`: 1 occurrence(s)
- `CAP-0709`: 1 occurrence(s)
- `CAP-0710`: 1 occurrence(s)
- `CAP-0801`: 1 occurrence(s)
- `CAP-0802`: 1 occurrence(s)
- `CAP-0803`: 1 occurrence(s)
- `CAP-0804`: 1 occurrence(s)
- `CAP-0805`: 1 occurrence(s)
- `CAP-0806`: 1 occurrence(s)
- `CAP-0807`: 1 occurrence(s)
- `CAP-0808`: 1 occurrence(s)
- `CAP-0901`: 1 occurrence(s)
- `CAP-0902`: 1 occurrence(s)
- `CAP-0903`: 1 occurrence(s)
- `CAP-0904`: 1 occurrence(s)
- `CAP-0905`: 1 occurrence(s)
- `CAP-0906`: 1 occurrence(s)
- `CAP-0907`: 1 occurrence(s)
- `CAP-0908`: 1 occurrence(s)
- `CAP-0909`: 1 occurrence(s)
- `CAP-0910`: 1 occurrence(s)
- `CAP-1001`: 1 occurrence(s)
- `CAP-1002`: 1 occurrence(s)
- `CAP-1003`: 1 occurrence(s)
- `CAP-1004`: 1 occurrence(s)
- `CAP-1005`: 1 occurrence(s)
- `CAP-1006`: 1 occurrence(s)
- `CAP-1007`: 1 occurrence(s)
- `CAP-1008`: 1 occurrence(s)
- `CAP-1009`: 1 occurrence(s)
- `CAP-1101`: 1 occurrence(s)
- `CAP-1102`: 1 occurrence(s)
- `CAP-1103`: 1 occurrence(s)
- `CAP-1104`: 1 occurrence(s)
- `CAP-1105`: 1 occurrence(s)
- `CAP-1106`: 1 occurrence(s)
- `CAP-1107`: 1 occurrence(s)
- `CAP-1108`: 1 occurrence(s)
- `CAP-1109`: 1 occurrence(s)
- `CAP-1201`: 1 occurrence(s)
- `CAP-1202`: 1 occurrence(s)
- `CAP-1203`: 1 occurrence(s)
- `CAP-1204`: 1 occurrence(s)
- `CAP-1205`: 1 occurrence(s)
- `CAP-1206`: 1 occurrence(s)
- `CAP-1207`: 1 occurrence(s)
- `CAP-1208`: 1 occurrence(s)
- `CAP-1301`: 1 occurrence(s)
- `CAP-1302`: 1 occurrence(s)
- `CAP-1303`: 1 occurrence(s)
- `CAP-1304`: 1 occurrence(s)
- `CAP-1305`: 1 occurrence(s)
- `CAP-1306`: 1 occurrence(s)
- `CAP-1307`: 1 occurrence(s)
- `CAP-1308`: 1 occurrence(s)
- `CAP-1309`: 1 occurrence(s)
- `CAP-1310`: 1 occurrence(s)
- `CAP-1401`: 1 occurrence(s)
- `CAP-1402`: 1 occurrence(s)
- `CAP-1403`: 1 occurrence(s)
- `CAP-1404`: 1 occurrence(s)
- `CAP-1405`: 1 occurrence(s)
- `CAP-1406`: 1 occurrence(s)
- `CAP-1407`: 1 occurrence(s)
- `CAP-1408`: 1 occurrence(s)
- `CAP-1501`: 1 occurrence(s)
- `CAP-1502`: 1 occurrence(s)
- `CAP-1503`: 1 occurrence(s)
- `CAP-1504`: 1 occurrence(s)
- `CAP-1505`: 1 occurrence(s)
- `CAP-1506`: 1 occurrence(s)
- `CAP-1507`: 1 occurrence(s)
- `CAP-1508`: 1 occurrence(s)
- `CAP-1509`: 1 occurrence(s)
- `CAP-1510`: 1 occurrence(s)
- `CAP-1511`: 1 occurrence(s)
- `CAP-1512`: 1 occurrence(s)
- `CAP-9001`: 1 occurrence(s)
- `CAP-9002`: 1 occurrence(s)
- `CAP-9003`: 1 occurrence(s)
- `CAP-9004`: 1 occurrence(s)
- `CAP-9005`: 1 occurrence(s)
- `CAP-9006`: 1 occurrence(s)
- `CAP-9007`: 1 occurrence(s)
- `CAP-9008`: 1 occurrence(s)
- `CAP-9009`: 1 occurrence(s)
- `CAP-9010`: 1 occurrence(s)
- `CAP-INDEX`: 9 occurrence(s)
- `EVT-000001`: 2 occurrence(s)
- `EVT-000002`: 2 occurrence(s)
- `EVT-000003`: 2 occurrence(s)
- `EVT-000004`: 1 occurrence(s)
- `EVT-000005`: 1 occurrence(s)
- `EVT-000006`: 1 occurrence(s)
- `EVT-000007`: 1 occurrence(s)
- `EVT-000008`: 1 occurrence(s)
- `EVT-010001`: 1 occurrence(s)
- `EVT-010002`: 1 occurrence(s)
- `EVT-010003`: 1 occurrence(s)
- `EVT-010004`: 1 occurrence(s)
- `EVT-010005`: 1 occurrence(s)
- `EVT-020001`: 1 occurrence(s)
- `EVT-020002`: 1 occurrence(s)
- `EVT-020003`: 1 occurrence(s)
- `EVT-020004`: 1 occurrence(s)
- `EVT-030001`: 1 occurrence(s)
- `EVT-030002`: 1 occurrence(s)
- `EVT-030003`: 1 occurrence(s)
- `EVT-030004`: 1 occurrence(s)
- `EVT-040001`: 1 occurrence(s)
- `EVT-040002`: 1 occurrence(s)
- `EVT-040003`: 1 occurrence(s)
- `EVT-040004`: 1 occurrence(s)
- `EVT-040005`: 1 occurrence(s)
- `EVT-050001`: 1 occurrence(s)
- `EVT-050002`: 1 occurrence(s)
- `EVT-050003`: 1 occurrence(s)
- `EVT-050004`: 1 occurrence(s)
- `EVT-050005`: 1 occurrence(s)
- `EVT-050006`: 1 occurrence(s)
- `EVT-050007`: 1 occurrence(s)
- `EVT-060001`: 1 occurrence(s)
- `EVT-060002`: 1 occurrence(s)
- `EVT-060003`: 1 occurrence(s)
- `EVT-060004`: 1 occurrence(s)
- `EVT-060005`: 1 occurrence(s)
- `EVT-060006`: 1 occurrence(s)
- `EVT-060007`: 1 occurrence(s)
- `EVT-060008`: 1 occurrence(s)
- `EVT-070001`: 1 occurrence(s)
- `EVT-070002`: 1 occurrence(s)
- `EVT-070003`: 1 occurrence(s)
- `EVT-070004`: 1 occurrence(s)
- `EVT-070005`: 1 occurrence(s)
- `EVT-070006`: 1 occurrence(s)
- `EVT-070007`: 1 occurrence(s)
- `EVT-080001`: 1 occurrence(s)
- `EVT-080002`: 1 occurrence(s)
- `EVT-080003`: 1 occurrence(s)
- `EVT-080004`: 1 occurrence(s)
- `EVT-080005`: 1 occurrence(s)
- `EVT-080006`: 1 occurrence(s)
- `EVT-080007`: 1 occurrence(s)
- `EVT-090001`: 1 occurrence(s)
- `EVT-090002`: 1 occurrence(s)
- `EVT-090003`: 1 occurrence(s)
- `EVT-090004`: 1 occurrence(s)
- `EVT-090005`: 1 occurrence(s)
- `EVT-090006`: 1 occurrence(s)
- `EVT-090007`: 1 occurrence(s)
- `EVT-100001`: 1 occurrence(s)
- `EVT-100002`: 1 occurrence(s)
- `EVT-100003`: 1 occurrence(s)
- `EVT-100004`: 1 occurrence(s)
- `EVT-100005`: 1 occurrence(s)
- `EVT-110001`: 1 occurrence(s)
- `EVT-110002`: 1 occurrence(s)
- `EVT-110003`: 1 occurrence(s)
- `EVT-110004`: 1 occurrence(s)
- `EVT-120001`: 1 occurrence(s)
- `EVT-120002`: 1 occurrence(s)
- `EVT-120003`: 1 occurrence(s)
- `EVT-120004`: 1 occurrence(s)
- `EVT-120005`: 1 occurrence(s)
- `EVT-120006`: 1 occurrence(s)
- `EVT-130001`: 1 occurrence(s)
- `EVT-130002`: 1 occurrence(s)
- `EVT-130003`: 1 occurrence(s)
- `EVT-130004`: 1 occurrence(s)
- `EVT-130005`: 1 occurrence(s)
- `EVT-130006`: 1 occurrence(s)
- `EVT-140001`: 1 occurrence(s)
- `EVT-140002`: 1 occurrence(s)
- `EVT-140003`: 1 occurrence(s)
- `EVT-140004`: 1 occurrence(s)
- `EVT-140005`: 1 occurrence(s)
- `EVT-140006`: 1 occurrence(s)
- `EVT-140007`: 1 occurrence(s)
- `POL-000001`: 2 occurrence(s)
- `POL-000002`: 2 occurrence(s)
- `POL-000003`: 2 occurrence(s)
- `POL-000004`: 1 occurrence(s)
- `POL-000005`: 1 occurrence(s)
- `POL-010001`: 1 occurrence(s)
- `POL-010002`: 1 occurrence(s)
- `POL-010003`: 1 occurrence(s)
- `POL-010004`: 1 occurrence(s)
- `POL-020001`: 1 occurrence(s)
- `POL-020002`: 1 occurrence(s)
- `POL-020003`: 1 occurrence(s)
- `POL-020004`: 1 occurrence(s)
- `POL-030001`: 1 occurrence(s)
- `POL-030002`: 1 occurrence(s)
- `POL-030003`: 1 occurrence(s)
- `POL-030004`: 1 occurrence(s)
- `POL-030005`: 1 occurrence(s)
- `POL-040001`: 1 occurrence(s)
- `POL-040002`: 1 occurrence(s)
- `POL-040003`: 1 occurrence(s)
- `POL-040004`: 1 occurrence(s)
- `POL-040005`: 1 occurrence(s)
- `POL-050001`: 1 occurrence(s)
- `POL-050002`: 1 occurrence(s)
- `POL-050003`: 1 occurrence(s)
- `POL-050004`: 1 occurrence(s)
- `POL-050005`: 1 occurrence(s)
- `POL-060001`: 1 occurrence(s)
- `POL-060002`: 1 occurrence(s)
- `POL-060003`: 1 occurrence(s)
- `POL-060004`: 1 occurrence(s)
- `POL-060005`: 1 occurrence(s)
- `POL-070001`: 1 occurrence(s)
- `POL-070002`: 1 occurrence(s)
- `POL-070003`: 1 occurrence(s)
- `POL-070004`: 1 occurrence(s)
- `POL-070005`: 1 occurrence(s)
- `POL-070006`: 1 occurrence(s)
- `POL-070007`: 1 occurrence(s)
- `POL-080001`: 1 occurrence(s)
- `POL-080002`: 1 occurrence(s)
- `POL-080003`: 1 occurrence(s)
- `POL-080004`: 1 occurrence(s)
- `POL-080005`: 1 occurrence(s)
- `POL-080006`: 1 occurrence(s)
- `POL-080007`: 1 occurrence(s)
- `POL-080008`: 1 occurrence(s)
- `POL-090001`: 1 occurrence(s)
- `POL-090002`: 1 occurrence(s)
- `POL-090003`: 1 occurrence(s)
- `POL-090004`: 1 occurrence(s)
- `POL-090005`: 1 occurrence(s)
- `POL-090006`: 1 occurrence(s)
- `POL-100001`: 1 occurrence(s)
- `POL-100002`: 1 occurrence(s)
- `POL-100003`: 1 occurrence(s)
- `POL-100004`: 1 occurrence(s)
- `POL-100005`: 1 occurrence(s)
- `POL-100006`: 1 occurrence(s)
- `POL-100007`: 1 occurrence(s)
- `POL-110001`: 1 occurrence(s)
- `POL-110002`: 1 occurrence(s)
- `POL-110003`: 1 occurrence(s)
- `POL-110004`: 1 occurrence(s)
- `POL-110005`: 1 occurrence(s)
- `POL-110006`: 1 occurrence(s)
- `POL-110007`: 1 occurrence(s)
- `POL-110008`: 1 occurrence(s)
- `POL-120001`: 1 occurrence(s)
- `POL-120002`: 1 occurrence(s)
- `POL-120003`: 1 occurrence(s)
- `POL-120004`: 1 occurrence(s)
- `POL-120005`: 1 occurrence(s)
- `POL-120006`: 1 occurrence(s)
- `POL-120007`: 1 occurrence(s)
- `POL-120008`: 1 occurrence(s)
- `POL-120009`: 1 occurrence(s)
- `POL-130001`: 1 occurrence(s)
- `POL-130002`: 1 occurrence(s)
- `POL-130003`: 1 occurrence(s)
- `POL-130004`: 1 occurrence(s)
- `POL-130005`: 1 occurrence(s)
- `POL-130006`: 1 occurrence(s)
- `POL-130007`: 1 occurrence(s)
- `POL-130008`: 1 occurrence(s)
- `POL-130009`: 1 occurrence(s)
- `POL-130010`: 1 occurrence(s)
- `SNP-000001`: 2 occurrence(s)
- `SNP-000002`: 2 occurrence(s)
- `SNP-000003`: 2 occurrence(s)
- `SNP-000004`: 1 occurrence(s)
- `SNP-010001`: 1 occurrence(s)
- `SNP-010002`: 1 occurrence(s)
- `SNP-010003`: 1 occurrence(s)
- `SNP-010004`: 1 occurrence(s)
- `SNP-020001`: 1 occurrence(s)
- `SNP-020002`: 1 occurrence(s)
- `SNP-020003`: 1 occurrence(s)
- `SNP-030001`: 1 occurrence(s)
- `SNP-030002`: 1 occurrence(s)
- `SNP-030003`: 1 occurrence(s)
- `SNP-030004`: 1 occurrence(s)
- `SNP-040001`: 1 occurrence(s)
- `SNP-040002`: 1 occurrence(s)
- `SNP-040003`: 1 occurrence(s)
- `SNP-040004`: 1 occurrence(s)
- `SNP-050001`: 1 occurrence(s)
- `SNP-050002`: 1 occurrence(s)
- `SNP-050003`: 1 occurrence(s)
- `SNP-050004`: 1 occurrence(s)
- `SNP-060001`: 1 occurrence(s)
- `SNP-060002`: 1 occurrence(s)
- `SNP-060003`: 1 occurrence(s)
- `SNP-070001`: 1 occurrence(s)
- `SNP-070002`: 1 occurrence(s)
- `SNP-070003`: 1 occurrence(s)
- `SNP-070004`: 1 occurrence(s)
- `SNP-080001`: 1 occurrence(s)
- `SNP-080002`: 1 occurrence(s)
- `SNP-080003`: 1 occurrence(s)
- `SNP-080004`: 1 occurrence(s)
- `SNP-090001`: 1 occurrence(s)
- `SNP-090002`: 1 occurrence(s)
- `SNP-090003`: 1 occurrence(s)
- `SNP-090004`: 1 occurrence(s)
- `SNP-100001`: 1 occurrence(s)
- `SNP-100002`: 1 occurrence(s)
- `SNP-100003`: 1 occurrence(s)
- `SNP-100004`: 1 occurrence(s)
- `SNP-110001`: 1 occurrence(s)
- `SNP-110002`: 1 occurrence(s)
- `SNP-110003`: 1 occurrence(s)
- `SNP-110004`: 1 occurrence(s)
- `UXF-00`: 8 occurrence(s)
- `UXF-01`: 8 occurrence(s)
- `UXF-02`: 8 occurrence(s)
- `UXF-03`: 8 occurrence(s)
- `UXF-04`: 8 occurrence(s)
- `UXF-05`: 8 occurrence(s)
- `UXF-INDEX`: 1 occurrence(s)

## Normalized overlap metrics

- Requirements with overlap: **107**
- Unique pairs: **134**
- Unique groups: **37**
- Exact duplicate groups: **31**
- Probable semantic overlap groups: **6**

Deterministic representative groups:

- `OVL-EXACT-001` `EXACT_DUPLICATE` `POTENTIAL_ACCIDENTAL_SAME_SOURCE_DUPLICATE`: `BD-06-007`, `EP-06-004`
- `OVL-EXACT-002` `EXACT_DUPLICATE` `POTENTIAL_ACCIDENTAL_SAME_SOURCE_DUPLICATE`: `BD-07-003`, `TMP-BRD-WS-07-002`
- `OVL-EXACT-003` `EXACT_DUPLICATE` `POTENTIAL_ACCIDENTAL_SAME_SOURCE_DUPLICATE`: `BD-08-001`, `TMP-BRD-WS-08-001`
- `OVL-EXACT-004` `EXACT_DUPLICATE` `POTENTIAL_ACCIDENTAL_SAME_SOURCE_DUPLICATE`: `BD-08-012`, `TMP-BRD-WS-08-009`
- `OVL-EXACT-005` `EXACT_DUPLICATE` `POTENTIAL_ACCIDENTAL_SAME_SOURCE_DUPLICATE`: `BD-09-002`, `TMP-BRD-WS-09-002`
- `OVL-EXACT-006` `EXACT_DUPLICATE` `POTENTIAL_ACCIDENTAL_SAME_SOURCE_DUPLICATE`: `BD-10-016`, `TMP-BRD-WS-10-005`
- `OVL-EXACT-007` `EXACT_DUPLICATE` `POTENTIAL_ACCIDENTAL_SAME_SOURCE_DUPLICATE`: `BD-10-019`, `TMP-BRD-WS-10-006`
- `OVL-EXACT-008` `EXACT_DUPLICATE` `POTENTIAL_ACCIDENTAL_SAME_SOURCE_DUPLICATE`: `BD-12-005`, `TMP-BRD-WS-12-001`
- `OVL-EXACT-009` `EXACT_DUPLICATE` `POTENTIAL_ACCIDENTAL_SAME_SOURCE_DUPLICATE`: `BD-16-026`, `EP-16-009`
- `OVL-EXACT-010` `EXACT_DUPLICATE` `POTENTIAL_ACCIDENTAL_SAME_SOURCE_DUPLICATE`: `BD-16-027`, `EP-16-008`

Intentional shared UX candidates and potential accidental duplicates remain separate classifications; no IDs are merged or removed.

## Classification findings

The audit does not accept TMP status or an ID prefix alone as semantic proof of type. Findings below identify temporary entries whose source position conflicts with the current broad type.

- Existing-ID entries reviewed by position rule: **576**
- Existing-ID position confusion findings: **0**
- Temporary-key entries reviewed: **733**
- Temporary-key position confusion findings: **142**

- `TMP-BRD-BO-INDEX-014` (`docs/BRD/BRD-BO-INDEX.md:L233`): Nearest source heading is '8. Registry Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-BO-INDEX-016` (`docs/BRD/BRD-BO-INDEX.md:L712`): Nearest source heading is '12. Business Object Relationship Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-BO-INDEX-017` (`docs/BRD/BRD-BO-INDEX.md:L810-L812`): Nearest source heading is '15. Business Object Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-BO-INDEX-018` (`docs/BRD/BRD-BO-INDEX.md:L810-L813`): Nearest source heading is '15. Business Object Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-BO-INDEX-019` (`docs/BRD/BRD-BO-INDEX.md:L810-L814`): Nearest source heading is '15. Business Object Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-BO-INDEX-020` (`docs/BRD/BRD-BO-INDEX.md:L810-L815`): Nearest source heading is '15. Business Object Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-BO-INDEX-021` (`docs/BRD/BRD-BO-INDEX.md:L810-L816`): Nearest source heading is '15. Business Object Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-BO-INDEX-022` (`docs/BRD/BRD-BO-INDEX.md:L818`): Nearest source heading is '15. Business Object Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-CAP-INDEX-004` (`docs/BRD/BRD-CAP-INDEX.md:L277`): Nearest source heading is '11. Registry Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-EVENT-INDEX-001` (`docs/BRD/BRD-EVENT-INDEX.md:L197`): Nearest source heading is '7. Event Delivery Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-EVENT-INDEX-002` (`docs/BRD/BRD-EVENT-INDEX.md:L205`): Nearest source heading is '7. Event Delivery Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-EVENT-INDEX-007` (`docs/BRD/BRD-EVENT-INDEX.md:L762-L764`): Nearest source heading is '18. Event Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-EVENT-INDEX-008` (`docs/BRD/BRD-EVENT-INDEX.md:L762-L765`): Nearest source heading is '18. Event Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-EVENT-INDEX-009` (`docs/BRD/BRD-EVENT-INDEX.md:L762-L766`): Nearest source heading is '18. Event Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-EVENT-INDEX-010` (`docs/BRD/BRD-EVENT-INDEX.md:L762-L767`): Nearest source heading is '18. Event Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-EVENT-INDEX-011` (`docs/BRD/BRD-EVENT-INDEX.md:L762-L768`): Nearest source heading is '18. Event Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-EVENT-INDEX-012` (`docs/BRD/BRD-EVENT-INDEX.md:L762-L769`): Nearest source heading is '18. Event Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-EVENT-INDEX-013` (`docs/BRD/BRD-EVENT-INDEX.md:L762-L770`): Nearest source heading is '18. Event Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-EVENT-INDEX-014` (`docs/BRD/BRD-EVENT-INDEX.md:L762-L771`): Nearest source heading is '18. Event Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-META-MODEL-001` (`docs/BRD/BRD-META-MODEL.md:L236`): Nearest source heading is 'Principle 6'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-001` (`docs/BRD/BRD-POLICY-INDEX.md:L142`): Nearest source heading is '5. Policy Scope'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-002` (`docs/BRD/BRD-POLICY-INDEX.md:L175`): Nearest source heading is '6. Policy Inheritance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-003` (`docs/BRD/BRD-POLICY-INDEX.md:L249`): Nearest source heading is '9. Policy Identifier'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-008` (`docs/BRD/BRD-POLICY-INDEX.md:L633`): Nearest source heading is '17. Policy Decision Flow'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-009` (`docs/BRD/BRD-POLICY-INDEX.md:L669`): Nearest source heading is '17. Policy Decision Flow'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-010` (`docs/BRD/BRD-POLICY-INDEX.md:L685-L689`): Nearest source heading is '18. Policy Inheritance Matrix'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-011` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L771`): Nearest source heading is '21. Policy Traceability'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-012` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L772`): Nearest source heading is '21. Policy Traceability'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-013` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L773`): Nearest source heading is '21. Policy Traceability'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-014` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L774`): Nearest source heading is '21. Policy Traceability'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-015` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L775`): Nearest source heading is '21. Policy Traceability'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-016` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L776`): Nearest source heading is '21. Policy Traceability'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-017` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L777`): Nearest source heading is '21. Policy Traceability'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-018` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L778`): Nearest source heading is '21. Policy Traceability'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-POLICY-INDEX-019` (`docs/BRD/BRD-POLICY-INDEX.md:L769-L779`): Nearest source heading is '21. Policy Traceability'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-002` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L261-L263`): Nearest source heading is '10. Immutable Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-003` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L273-L275`): Nearest source heading is '11. Business Evidence Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-004` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L273-L276`): Nearest source heading is '11. Business Evidence Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-005` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L273-L277`): Nearest source heading is '11. Business Evidence Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-008` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L586`): Nearest source heading is '16. Snapshot Composition Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-022` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L788-L790`): Nearest source heading is '23. Snapshot Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-023` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L788-L791`): Nearest source heading is '23. Snapshot Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-024` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L788-L792`): Nearest source heading is '23. Snapshot Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-025` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L788-L793`): Nearest source heading is '23. Snapshot Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-026` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L788-L794`): Nearest source heading is '23. Snapshot Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-027` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L788-L795`): Nearest source heading is '23. Snapshot Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-028` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L788-L796`): Nearest source heading is '23. Snapshot Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-029` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L788-L797`): Nearest source heading is '23. Snapshot Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-030` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L788-L798`): Nearest source heading is '23. Snapshot Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-SNAPSHOT-INDEX-031` (`docs/BRD/BRD-SNAPSHOT-INDEX.md:L800`): Nearest source heading is '23. Snapshot Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-UPDATE-01-008` (`docs/BRD/BRD-UPDATE-01.md:L423`): Nearest source heading is '6AH. Business Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-UPDATE-01-010` (`docs/BRD/BRD-UPDATE-01.md:L629`): Nearest source heading is '6I. Business Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-UPDATE-01-020` (`docs/BRD/BRD-UPDATE-01.md:L904-L906`): Nearest source heading is '17. Business Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-UPDATE-01-021` (`docs/BRD/BRD-UPDATE-01.md:L904-L907`): Nearest source heading is '17. Business Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-UPDATE-01-022` (`docs/BRD/BRD-UPDATE-01.md:L904-L908`): Nearest source heading is '17. Business Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-UPDATE-01-023` (`docs/BRD/BRD-UPDATE-01.md:L904-L909`): Nearest source heading is '17. Business Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-UPDATE-01-024` (`docs/BRD/BRD-UPDATE-01.md:L904-L910`): Nearest source heading is '17. Business Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-UPDATE-01-025` (`docs/BRD/BRD-UPDATE-01.md:L904-L911`): Nearest source heading is '17. Business Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-UPDATE-01-026` (`docs/BRD/BRD-UPDATE-01.md:L904-L912`): Nearest source heading is '17. Business Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-UPDATE-01-027` (`docs/BRD/BRD-UPDATE-01.md:L904-L913`): Nearest source heading is '17. Business Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-UPDATE-01-028` (`docs/BRD/BRD-UPDATE-01.md:L904-L914`): Nearest source heading is '17. Business Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-UPDATE-01-029` (`docs/BRD/BRD-UPDATE-01.md:L904-L915`): Nearest source heading is '17. Business Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-04-012` (`docs/BRD/BRD-WS-04.md:L370`): Nearest source heading is '17. Catalog Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-04-014` (`docs/BRD/BRD-WS-04.md:L441`): Nearest source heading is '20. Sales Catalog Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-04-015` (`docs/BRD/BRD-WS-04.md:L449`): Nearest source heading is '21. Currency Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-04-016` (`docs/BRD/BRD-WS-04.md:L471`): Nearest source heading is '21. Currency Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-05-012` (`docs/BRD/BRD-WS-05.md:L245-L247`): Nearest source heading is '10. Currency Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-05-013` (`docs/BRD/BRD-WS-05.md:L245-L248`): Nearest source heading is '10. Currency Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-05-014` (`docs/BRD/BRD-WS-05.md:L245-L249`): Nearest source heading is '10. Currency Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-05-015` (`docs/BRD/BRD-WS-05.md:L245-L250`): Nearest source heading is '10. Currency Governance'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-05-016` (`docs/BRD/BRD-WS-05.md:L273-L275`): Nearest source heading is '11. Margin Policy'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-05-017` (`docs/BRD/BRD-WS-05.md:L273-L276`): Nearest source heading is '11. Margin Policy'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-05-018` (`docs/BRD/BRD-WS-05.md:L273-L277`): Nearest source heading is '11. Margin Policy'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-05-019` (`docs/BRD/BRD-WS-05.md:L273-L278`): Nearest source heading is '11. Margin Policy'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-05-021` (`docs/BRD/BRD-WS-05.md:L492-L494`): Nearest source heading is '20. Commercial Consistency Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-06-018` (`docs/BRD/BRD-WS-06.md:L311`): Nearest source heading is '13. Promotion Rule'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-07-010` (`docs/BRD/BRD-WS-07.md:L439-L442`): Nearest source heading is '15. Purchase Order Policy'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-11-002` (`docs/BRD/BRD-WS-11.md:L108`): Nearest source heading is '4. Enterprise Customer Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-11-003` (`docs/BRD/BRD-WS-11.md:L110`): Nearest source heading is '4. Enterprise Customer Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-14-004` (`docs/BRD/BRD-WS-14.md:L247`): Nearest source heading is '8. Business Rule Engine'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-14-005` (`docs/BRD/BRD-WS-14.md:L297-L299`): Nearest source heading is '11. Rule Version'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-14-006` (`docs/BRD/BRD-WS-14.md:L297-L300`): Nearest source heading is '11. Rule Version'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-14-007` (`docs/BRD/BRD-WS-14.md:L297-L301`): Nearest source heading is '11. Rule Version'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-14-008` (`docs/BRD/BRD-WS-14.md:L297-L302`): Nearest source heading is '11. Rule Version'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-14-009` (`docs/BRD/BRD-WS-14.md:L304`): Nearest source heading is '11. Rule Version'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-15-007` (`docs/BRD/BRD-WS-15.md:L347`): Nearest source heading is '14. Retry Policy'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-16-011` (`docs/BRD/BRD-WS-16.md:L665`): Nearest source heading is '27. Security Policy'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-17-004` (`docs/BRD/BRD-WS-17.md:L494`): Nearest source heading is '18. Capacity Policy'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-17-010` (`docs/BRD/BRD-WS-17.md:L685`): Nearest source heading is '25. Operation Policy'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-BRD-WS-17-013` (`docs/BRD/BRD-WS-17.md:L798-L800`): Nearest source heading is '30. Enterprise Operations Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-00-001` (`docs/UXF/UXF-00.md:L248`): Nearest source heading is '7. Business Binding Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-00-002` (`docs/UXF/UXF-00.md:L262`): Nearest source heading is '7. Business Binding Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-00-003` (`docs/UXF/UXF-00.md:L270`): Nearest source heading is '8. Supplier Isolation Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-00-004` (`docs/UXF/UXF-00.md:L304`): Nearest source heading is '8. Supplier Isolation Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-00-005` (`docs/UXF/UXF-00.md:L345-L347`): Nearest source heading is '10. Product Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-00-006` (`docs/UXF/UXF-00.md:L345-L348`): Nearest source heading is '10. Product Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-00-007` (`docs/UXF/UXF-00.md:L345-L349`): Nearest source heading is '10. Product Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-00-008` (`docs/UXF/UXF-00.md:L345-L350`): Nearest source heading is '10. Product Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-00-009` (`docs/UXF/UXF-00.md:L345-L351`): Nearest source heading is '10. Product Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-00-014` (`docs/UXF/UXF-00.md:L520`): Nearest source heading is '16. Design System Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-00-015` (`docs/UXF/UXF-00.md:L522`): Nearest source heading is '16. Design System Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-00-016` (`docs/UXF/UXF-00.md:L542`): Nearest source heading is '17. White-label Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-00-031` (`docs/UXF/UXF-00.md:L601`): Nearest source heading is '20. Architectural Principles'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-02-010` (`docs/UXF/UXF-02.md:L624-L626`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-02-011` (`docs/UXF/UXF-02.md:L624-L627`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-02-012` (`docs/UXF/UXF-02.md:L624-L628`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-02-013` (`docs/UXF/UXF-02.md:L624-L629`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-02-014` (`docs/UXF/UXF-02.md:L624-L630`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-02-015` (`docs/UXF/UXF-02.md:L624-L631`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-02-016` (`docs/UXF/UXF-02.md:L624-L632`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-02-017` (`docs/UXF/UXF-02.md:L624-L633`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-02-018` (`docs/UXF/UXF-02.md:L624-L634`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-02-019` (`docs/UXF/UXF-02.md:L624-L635`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-03-008` (`docs/UXF/UXF-03.md:L611-L613`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-03-009` (`docs/UXF/UXF-03.md:L611-L614`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-03-010` (`docs/UXF/UXF-03.md:L611-L615`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-03-011` (`docs/UXF/UXF-03.md:L611-L616`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-03-012` (`docs/UXF/UXF-03.md:L611-L617`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-03-013` (`docs/UXF/UXF-03.md:L611-L618`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-03-014` (`docs/UXF/UXF-03.md:L611-L619`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-03-015` (`docs/UXF/UXF-03.md:L611-L620`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-03-016` (`docs/UXF/UXF-03.md:L611-L621`): Nearest source heading is '21. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-04-015` (`docs/UXF/UXF-04.md:L602-L604`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-04-016` (`docs/UXF/UXF-04.md:L602-L605`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-04-017` (`docs/UXF/UXF-04.md:L602-L606`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-04-018` (`docs/UXF/UXF-04.md:L602-L607`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-04-019` (`docs/UXF/UXF-04.md:L602-L608`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-04-020` (`docs/UXF/UXF-04.md:L602-L609`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-04-021` (`docs/UXF/UXF-04.md:L602-L610`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-04-022` (`docs/UXF/UXF-04.md:L602-L611`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-04-023` (`docs/UXF/UXF-04.md:L602-L612`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-05-013` (`docs/UXF/UXF-05.md:L330`): Nearest source heading is '13. Allocation Principle'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-05-023` (`docs/UXF/UXF-05.md:L617-L619`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-05-024` (`docs/UXF/UXF-05.md:L621`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-05-025` (`docs/UXF/UXF-05.md:L623`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-05-026` (`docs/UXF/UXF-05.md:L625`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-05-027` (`docs/UXF/UXF-05.md:L627-L629`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-05-028` (`docs/UXF/UXF-05.md:L627-L630`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-05-029` (`docs/UXF/UXF-05.md:L627-L631`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-05-030` (`docs/UXF/UXF-05.md:L633`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-05-031` (`docs/UXF/UXF-05.md:L635`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.
- `TMP-UXF-05-032` (`docs/UXF/UXF-05.md:L637`): Nearest source heading is '23. AI Implementation Guidelines'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.

## Human decisions required

- Review all false-negative candidates before changing registry membership.
- Decide whether navigation, traceability, and AI implementation guideline entries remain requirements.
- Decide which compound statements must be split during a later content-editing phase.
- Resolve temporary-key classification confusion using source meaning and ownership, not TMP status.
- Classify potential accidental overlap groups; do not merge IDs automatically.

Full occurrence-level evidence, all overlap groups/pairs, all samples and all per-file findings are in `requirements/registry-qa.json`.

## Phase 1C status

All 140 false-positive, 10 false-negative, and 137 compound candidates have ledger dispositions. Composite parents `BO-P06`, `BD-15-002` are reconciled verbatim with two atomic children each and `ALL_CHILDREN` coverage. Canonical/alias mappings: `EP-06-004` → `BD-06-007`, `EP-16-009` → `BD-16-026`, `EP-16-008` → `BD-16-027`, `EP-17-005` → `BD-17-011`, `EP-17-009` → `BD-17-026`, `CAP-EP-006` → `CAP-P07`, `EP-06-005` → `BD-06-011`, `SNP-EP-007` → `SNP-P07`. Retired temporary mappings: `TMP-BRD-WS-07-002` → `BD-07-003`, `TMP-BRD-WS-08-001` → `BD-08-001`, `TMP-BRD-WS-08-009` → `BD-08-012`, `TMP-BRD-WS-09-002` → `BD-09-002`, `TMP-BRD-WS-10-005` → `BD-10-016`, `TMP-BRD-WS-10-006` → `BD-10-019`, `TMP-BRD-WS-12-001` → `BD-12-005`, `TMP-BRD-WS-15-002` → `EP-15-002`, `TMP-UXF-05-013` → `UXF-505`, `TMP-BRD-WS-03-001` → `BD-03-006`, `TMP-BRD-WS-15-001` → `EP-15-001`, `TMP-BRD-WS-15-027` → `EP-15-001`. **0** human decisions remain; registry ready-to-freeze: **yes**.

## Deferred documentation findings

- `DOC-OVL-EXACT-004` (DEFERRED_TO_BRD_CORRECTION): Clarify 'Version 2.0' as the v2.3 baseline when the BRD is revised. Do not modify docs/BRD in Phase 1C. Partial Payment and Partial Refund are distinct capabilities. A decision to support Partial Refund does not activate Partial Payment.
- `DOC-OVL-EXACT-006` (DEFERRED_TO_BRD_CORRECTION): Correct 'Version 2.0' to the v2.3 baseline when the BRD is revised. Auto Payout remains out of scope for v2.3 under SD-02. Do not modify docs/BRD in Phase 1C.
- `DOC-OVL-EXACT-008` (DEFERRED_TO_BRD_CORRECTION): BRD v2.3 must replace 'cuối cùng' with explicit fallback semantics. Distinguish external delivery, durable inbox persistence, and user read state. Add retry policy, durable recovery/DLQ behavior, and source-backed acceptance criteria when the BRD is revised.
- `DOC-OVL-EXACT-009` (DEFERRED_TO_BRD_CORRECTION): The current Federation wording is insufficient for implementation and acceptance. Do not select a protocol or design a solution in Phase 1C. Federation actors and use cases.; Trust boundaries and tenant isolation.; Supported protocol/profile.; Claim/attribute mapping.; Account linking and conflict handling.; Provisioning/deprovisioning or related lifecycle behavior.; Authentication assurance, MFA, and risk interaction.; Audit, revocation, and failure behavior.; Acceptance criteria.
- `DOC-OVL-EXACT-010` (DEFERRED_TO_BRD_CORRECTION): The current Business Event wording is insufficient for implementation and acceptance. Do not design an event solution in Phase 1C. Mandatory security event taxonomy.; Trigger and producer ownership.; Event schema, versioning, and classification.; Tenant/Organization context.; Sensitive-data constraints.; Delivery guarantee, retry, and dead-letter handling.; Ordering, deduplication, and idempotency.; Consumer authorization.; Audit, retention, and observability.; Acceptance criteria.
- `DOC-OVL-EXACT-011` (DEFERRED_TO_BRD_CORRECTION): The independence between Operation Retry and Connector Retry must be specified when the BRD is revised. Do not design a retry policy in Phase 1C. Ownership and scope of each retry layer.; Independent counters and state.; Timeout, backoff, jitter, and retry budget.; Idempotency and duplicate prevention.; Conditions that escalate connector failure to operation failure.; Controls for nested retry amplification and retry storms.; Exhaustion, DLQ, and manual recovery.; Correlation, audit, and observability.; Acceptance criteria.
- `DOC-OVL-EXACT-012` (DEFERRED_TO_BRD_CORRECTION): The Operations Platform Business Event requirement must be specified when the BRD is revised. Do not design an event architecture in Phase 1C. Event taxonomy for operation lifecycle, retry, maintenance, runbook, and recovery.; Trigger and producer ownership.; Operation, correlation, and causation identifiers.; Organization, scope, and actor context.; Payload schema, versioning, and data classification.; Delivery guarantee, ordering, and idempotency.; Retry, DLQ, and replay.; Consumer authorization.; Audit, retention, and observability.; Acceptance criteria.
- `DOC-OVL-EXACT-013` (DEFERRED_TO_BRD_CORRECTION): Do not reclassify CAP-P07 or design an event model in Phase 1C. Consider reclassifying CAP-P07 from BUSINESS_REQUIREMENT to DESIGN_PRINCIPLE when the BRD is revised. Clarify event-role metadata, canonical event reference, ownership, and versioning.; Add validation for dangling or invalid event references.; Add acceptance criteria.
- `DOC-OVL-EXACT-015` (DEFERRED_TO_BRD_CORRECTION): The Gateway, Connector, and Adapter constraint must be clarified when the BRD is revised. Do not interpret or design an integration topology in Phase 1C. Scope inbound, outbound, synchronous, asynchronous, batch, and event interactions.; Clarify whether all three layers are always mandatory or depend on interaction type.; Clarify whether internal domain-to-domain communication is subject to the constraint.; Define approved exception and bypass policy.; Define enforcement, observability, and acceptance criteria.
- `DOC-OVL-EXACT-029` (DEFERRED_TO_UXF_CORRECTION): Replace 'never know suppliers' with explicit technical-decoupling semantics when UXF is revised. Do not reclassify UXF-505 or design an allocation solution in Phase 1C. Consider DESIGN_PRINCIPLE instead of UX_REQUIREMENT when UXF is revised. Distinguish supplier operational identity from provider/brand disclosure.; Add source-backed acceptance criteria.
- `DOC-OVL-PROB-001` (DEFERRED_TO_BRD_CORRECTION): The BRD/domain specification must clarify the Identity–User–Customer relationship. Do not create a detailed data model in Phase 1C. Cardinality between Identity, User, and Customer.; Organization ownership and scope.; Link/unlink behavior and lifecycle.; Account provisioning.; Merge and conflict rules.; Authorization and data-isolation implications.; Acceptance criteria.
- `DOC-OVL-PROB-002` (DEFERRED_TO_BRD_CORRECTION): The BRD must explicitly connect Promotion, Funding Owner, Organization ownership, and the associated financial lifecycle. Do not design a financial model in Phase 1C. Promotion.; Funding Owner.; Organization ownership.; Promotion budget reservation, consumption, and release.; Financial attribution.; Acceptance criteria.
- `DOC-OVL-PROB-003` (DEFERRED_TO_BRD_CORRECTION): The v2.3 BRD must replace the old term with Final Promotion Snapshot and specify the complete snapshot lifecycle. Change 'Promotion Snapshot' to 'Final Promotion Snapshot' in the old requirement.; Specify the Evaluation, Reservation, and Final lifecycle.; Link Promotion budget reserve, consume, and release behavior.; Define snapshot immutability, version, input, funding, currency, and timestamp.; Add transition and acceptance criteria.; Remove the interpretation that no snapshot may exist before Payment Success.
- `DOC-OVL-PROB-004` (DEFERRED_TO_BRD_CORRECTION): The Snapshot/Policy specification must define the joint Security Policy and Retention Policy contract. Do not design a policy engine or storage mechanism in Phase 1C. Policy precedence and conflict-resolution contract.; Jurisdiction and data-class mapping.; Legal hold.; Immutable snapshot behavior with deletion/anonymization.; Audit evidence.; Acceptance criteria.
- `DOC-OVL-PROB-006` (DEFERRED_TO_BRD_CORRECTION): Normalize both version labels to v2.3 when docs/BRD is revised. Phase 1C must not generalize this decision into a platform-wide Attachment policy. The Video exclusion applies only to Customer Support Ticket attachments and Notification attachments. If a shared Attachment capability is later established, its shared relationship must be designed in an architecture phase rather than this reconciliation.

## Human semantic clarifications

- `BD-12-005` (`OVL-EXACT-008`) semantic clarification:
  - Khi tất cả delivery channel bên ngoài được áp dụng đều thất bại hoặc không thể hoàn tất, hệ thống phải fallback về Personal Inbox.
  - Personal Inbox là kênh nội bộ, không phụ thuộc nền tảng communication bên ngoài.
  - Personal Inbox delivery thành công khi notification đã được persist bền vững và có thể truy xuất trong inbox của đúng recipient.
  - Delivery success không đồng nghĩa recipient đã đọc notification.
  - Nếu internal persistence tạm thời thất bại, hệ thống phải retry theo policy và đưa vào durable recovery/DLQ khi cần; không được đánh dấu success giả hoặc bỏ mất notification.
  - Acceptance intent:
    1. External channels được áp dụng đều fail hoặc không thể hoàn tất.
    2. Personal Inbox fallback được tạo.
    3. Notification được persist bền vững và có thể truy xuất cho đúng recipient.
    4. Trạng thái phân biệt DELIVERED_TO_INBOX và READ.
    5. Persistence failure không tạo false success, không làm mất notification và được retry/recover qua durable recovery hoặc DLQ khi cần.
  - Acceptance metadata remains `INFERRED_ONLY` until source-backed acceptance criteria are added.
- `CAP-P07` (`OVL-EXACT-013`) semantic clarification:
  - CAP-P07 mô tả khả năng của Capability Model, không bắt buộc mọi capability phải event-driven.
  - Mỗi capability có thể khai báo vai trò PUBLISHER, SUBSCRIBER, BOTH hoặc NONE.
  - Khi khai báo event role, capability phải tham chiếu canonical Business Event definition và versioned event contract tương ứng.
  - Không tự tạo event relationship nếu registry không khai báo.
- `UXF-505` (`OVL-EXACT-029`) semantic clarification:
  - Storefront không được lựa chọn supplier.
  - Storefront không được gửi supplier-selection instruction hoặc tham gia routing.
  - Storefront không gọi trực tiếp supplier connector/API.
  - Procurement, allocation và supplier routing nằm sau application/domain contract tương ứng.
  - Supplier/provider/network brand có thể được hiển thị read-only nếu catalog, product disclosure, legal hoặc market policy yêu cầu.
  - Dữ liệu supplier được hiển thị không được dùng để điều khiển allocation/routing.
  - Internal supplier identifiers, cost, priority, health và connector details không được lộ ra Storefront nếu không có explicit disclosure contract.
  - Acceptance intent:
    1. Storefront request không chứa supplier-selection instruction.
    2. Storefront không gọi supplier connector.
    3. Allocation là capability quyết định supplier.
    4. Provider/brand disclosure, nếu có, chỉ là read-only presentation.
    5. Internal supplier routing, cost, và health metadata không bị lộ.
  - Acceptance metadata remains `INFERRED_ONLY` until source-backed acceptance criteria are added.
- `BD-03-006` (`OVL-PROB-001`) semantic clarification:
  - Identity là canonical authentication identity.
  - User là actor/membership trong Organization context.
  - Customer là commercial/customer relationship concept.
  - User và Customer có thể liên kết nhưng không phải cùng entity.
  - Không dùng chung lifecycle hoặc mặc định đồng nhất record.
  - Global Customer Identity/Profile phải tách khỏi Organization Customer Relationship theo quyết định v2.3.
  - Một Identity có thể liên kết nhiều User records theo Organization.
- `BD-06-011` (`OVL-PROB-002`) semantic clarification:
  - Mỗi Promotion có đúng một Funding Owner.
  - Funding Owner là Organization tạo Promotion theo source hiện tại.
  - V2.3 không hỗ trợ nhiều Funding Owner hoặc co-funded Promotion.
  - Không suy diễn khả năng chuyển Funding Owner.
  - Nếu tương lai hỗ trợ reassignment, phải có lifecycle, approval, effective date, financial reconciliation và audit.
  - Promotion budget reservation/consumption phải hạch toán về Funding Owner này.
- `BD-06-014` (`OVL-PROB-003`) semantic clarification:
  - Source statement lịch sử được bảo toàn.
  - Effective v2.3 meaning: Final Promotion Snapshot is created only after Payment Success.
  - Từ 'chỉ' của EP-06-006 chỉ giới hạn Final Promotion Snapshot.
  - Requirement này không cấm Evaluation Snapshot hoặc Reservation Snapshot trước Payment Success.
- `SNP-P07` (`OVL-PROB-004`) semantic clarification:
  - Mọi Snapshot đồng thời chịu Security Policy và Retention Policy.
  - Security Policy quản lý authorization, classification, encryption, masking và access audit.
  - Retention Policy quản lý retention duration, archival, legal hold và deletion/anonymization.
  - Policy resolution xét data class, jurisdiction, Organization và platform minimum.
  - Khi policy xung đột hoặc thiếu cấu hình bắt buộc, xử lý fail-closed và chuyển governance/approval; không tự chọn policy thắng.
  - Snapshot immutability không loại bỏ nghĩa vụ retention/deletion.
  - Cơ chế tombstone, crypto-erasure hoặc compliant archival phải được đặc tả ở phase tài liệu phù hợp.

## Semantic equivalence classes

- `OVL-EXACT-014` canonical `EP-15-001`; retired `TMP-BRD-WS-15-001`, `TMP-BRD-WS-15-027`; satisfies `BD-15-002`.

## Transitively resolved overlap groups

None.

## Corrected truncated extractions

- `OVL-EXACT-016` `CORRECTED_TRUNCATED_EXTRACTION`: `TMP-BRD-WS-12-003`, `TMP-BRD-WS-12-004` remain active with corrected statements and full-context evidence.

## Channel-scoped restatements

- `OVL-EXACT-021` `CORRECTED_TRUNCATED_CHANNEL_CONTEXT`: identical predicate, distinct `EXPERIENCE_CHANNEL` applicability scopes for `TMP-UXF-01-001`, `TMP-UXF-01-002`, `TMP-UXF-01-003`.
