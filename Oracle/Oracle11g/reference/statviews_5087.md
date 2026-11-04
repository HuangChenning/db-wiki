---
title: DBA_WAITERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5087.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_WAITERS` shows all the sessions that are waiting for a lock. In an Oracle RAC environment, this only applies if the waiter is on the same instance.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WAITING_SESSION` | `NUMBER` |  | The waiting session |
| `HOLDING_SESSION` | `NUMBER` |  | The holding session |
| `LOCK_TYPE` | `VARCHAR2(26)` |  | The lock type |
| `MODE_HELD` | `VARCHAR2(40)` |  | The mode held |
| `MODE_REQUESTED` | `VARCHAR2(40)` |  | The mode requested |
| `LOCK_ID1` | `VARCHAR2(40)` |  | Lock ID 1 |
| `LOCK_ID2` | `VARCHAR2(40)` |  | Lock ID 2 |