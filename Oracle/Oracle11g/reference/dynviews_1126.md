---
title: "V$ENQUEUE_LOCK"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1126.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ENQUEUE_LOCK` displays all locks owned by enqueue state objects. The columns in this view are identical to the columns in `V$LOCK`.

See Also:

["V$LOCK"](dynviews_2027.md)

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDR` | `RAW(4 \| 8)` | Address of lock state object |
| `KADDR` | `RAW(4 \| 8)` | Address of lock |
| `SID` | `NUMBER` | Identifier for session holding or acquiring the lock |
| `TYPE` | `VARCHAR2(2)` | Type of lock. Lists user and system types that can have locks. |
| `ID1` | `NUMBER` | Lock identifier #1 (depends on type) |
| `ID2` | `NUMBER` | Lock identifier #2 (depends on type) |
| `LMODE` | `NUMBER` | Lock mode in which the session holds the lock: |
| `REQUEST` | `NUMBER` | Lock mode in which the process requests the lock: |
| `CTIME` | `NUMBER` | Time since current mode was granted |
| `BLOCK` | `NUMBER` | The lock is blocking another lock |