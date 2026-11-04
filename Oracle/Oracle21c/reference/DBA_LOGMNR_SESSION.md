---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_LOGMNR_SESSION.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.159 DBA\_LOGMNR\_SESSION

`DBA_LOGMNR_SESSION` displays all active LogMiner persistent sessions in the database.

A persistent LogMiner session is created either by starting Data Guard SQL Apply on a logical standby database for the first time or by creating Replication capture.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ID` | `NUMBER` | `NOT NULL` | Unique session identifier |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Unique session name |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | Global name of the source database whose archived logs are to be mined in this persistent LogMiner session |
| `SOURCE_DBID` | `NUMBER` |  | Database ID of the source database |
| `SOURCE_RESETLOGS_SCN` | `NUMBER` |  | Resetlogs SCN associated with the incarnation of the source database whose archived logs are mined |
| `SOURCE_RESETLOGS_TIME` | `NUMBER` |  | Resetlogs time associated with the incarnation of the source database whose archived logs are mined |
| `FIRST_SCN` | `NUMBER` |  | Only modifications that occurred on or after this SCN can be mined using this persistent session |
| `END_SCN` | `NUMBER` |  | No modifications that occurred on or after this SCN can be mined using this persistent session |
| `BRANCH_SCN` | `NUMBER` |  | SCN at which a branch will be taken in terms of the incarnation corresponding to the source database. This implies a point-in-time recovery was performed at the source database at this SCN. |
| `WAIT_FOR_LOG` | `VARCHAR2(3)` |  | Indicates whether the persistent session waits for RFS to register new archived logs or to fill gaps (`YES`) or not (`NO`) |
| `HOT_MINE` | `VARCHAR2(3)` |  | Indicates whether real-time mining is on (`YES`) or not (`NO`) |
| `SAFE_PURGE_SCN` | `NUMBER` |  | Persistent session can safely be purged up to this SCN |
| `CHECKPOINT_SCN` | `NUMBER` |  | SCN at which the latest checkpoint is taken by the persistent LogMiner session |
| `PURGE_SCN` | `NUMBER` |  | The session has been purged up to this SCN |