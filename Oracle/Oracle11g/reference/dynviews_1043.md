---
title: "V$AW_SESSION_INFO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1043.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$AW_SESSION_INFO` provides information about each active session. A transaction is a single exchange between a client session and Oracle OLAP. Multiple commands can execute within a single transaction.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | A unique numeric identifier for a session |
| `CLIENT_TYPE` | `VARCHAR2(64)` | `OLAP` |
| `SESSION_STATE` | `VARCHAR2(64)` | TRANSACTING, NOT\_TRANSACTING, EXCEPTION\_HANDLING, CONSTRUCTING, CONSTRUCTED, DECONSTRUCTING, or DECONSTRUCTED |
| `SESSION_HANDLE` | `NUMBER` | The session identifier |
| `USERID` | `VARCHAR2(64)` | The database user name under which the session opened |
| `TOTAL_TRANSACTION` | `NUMBER` | The total number of transactions executed within the session; this number provides a general indication of the level of activity in the session |
| `TRANSACTION_TIME` | `NUMBER` | The elapsed time in milliseconds of the mostly recently completed transaction |
| `TOTAL_TRANSACTION_TIME` | `NUMBER` | The total elapsed time in milliseconds in which transactions were being executed |
| `AVERAGE_TRANSACTION_TIME` | `NUMBER` | The average elapsed time in milliseconds to complete a transaction |
| `TRANSACTION_CPU_TIME` | `NUMBER` | The total CPU time in milliseconds used to complete the most recent transaction |
| `TOTAL_TRANSACTION_CPU_TIME` | `NUMBER` | The total CPU time used to execute all transactions in this session; this total does not include transactions that are currently in progress |
| `AVERAGE_TRANSACTION_CPU_TIME` | `NUMBER` | The average CPU time to complete a transaction; this average does not include transactions that are currently in progress |