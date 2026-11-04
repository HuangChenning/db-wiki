---
title: "V$GLOBAL_BLOCKED_LOCKS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1167.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$GLOBAL_BLOCKED_LOCKS` displays global blocked locks.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDR` | `RAW(4 \| 8)` | Address of lock state object |
| `KADDR` | `RAW(4 \| 8)` | Address of lock |
| `SID` | `NUMBER` | Identifier of session holding the lock (number) |
| `TYPE` | `VARCHAR2(2)` | Resource type (char) |
| `ID1` | `NUMBER` | Resource identifier #1 (number) |
| `ID2` | `NUMBER` | Resource identifier #2 (number) |
| `LMODE` | `NUMBER` | Lock mode held (number) |
| `REQUEST` | `NUMBER` | Lock mode requested (number) |
| `CTIME` | `NUMBER` | Time since current mode was granted |