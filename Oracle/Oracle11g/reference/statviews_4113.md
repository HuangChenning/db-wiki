---
title: DBA_LOCK_INTERNAL
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4113.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_LOCK_INTERNAL` displays a row for each lock or latch that is being held, and one row for each outstanding request for a lock or latch.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SESSION_ID` | `NUMBER` |  | Session holding or acquiring the lock |
| `LOCK_TYPE` | `VARCHAR2(56)` |  | Lock type  See Also: For a listing of lock types, see [Appendix D, "Oracle Enqueue Names"](enqueues.md) |
| `MODE HELD` | `VARCHAR2(40)` |  | Lock mode |
| `MODE REQUESTED` | `VARCHAR2(40)` |  | Lock mode requested |
| `LOCK_ID1` | `VARCHAR2(1130)` |  | Type-specific lock identifier, part 1 |
| `LOCK_ID2` | `VARCHAR2(40)` |  | Type-specific lock identifier, part 2 |