---
title: "V$TRANSACTION_ENQUEUE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3115.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$TRANSACTION_ENQUEUE` displays locks owned by transaction state objects.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDR` | `RAW(4 \| 8)` | Address of lock state object |
| `KADDR` | `RAW(4 \| 8)` | Address of lock |
| `SID` | `NUMBER` | Identifier for session holding or acquiring the lock |
| `TYPE` | `VARCHAR2(2)` | Type of lock. TX indicates transaction enqueue. |
| `ID1` | `NUMBER` | Lock identifier #1 (depends on type) |
| `ID2` | `NUMBER` | Lock identifier #2 (depends on type) |
| `LMODE` | `NUMBER` | Lock mode in which the session holds the lock: |
| `REQUEST` | `NUMBER` | Lock mode in which the process requests the lock: |
| `CTIME` | `NUMBER` | Time since current mode was granted |
| `BLOCK` | `NUMBER` | The lock is blocking another lock |