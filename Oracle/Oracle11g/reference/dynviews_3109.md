---
title: "V$THREAD"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3109.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$THREAD` displays thread information from the control file. This view does not return meaningful results on a physical standby database.

| Column | Datatype | Description |
| --- | --- | --- |
| `THREAD#` | `NUMBER` | Thread number |
| `STATUS` | `VARCHAR2(6)` | Thread status (`OPEN` \| `CLOSED`) |
| `ENABLED` | `VARCHAR2(8)` | Enabled status: `DISABLED`, (enabled) `PRIVATE`, or (enabled) `PUBLIC` |
| `GROUPS` | `NUMBER` | Number of log groups assigned to this thread |
| `INSTANCE` | `VARCHAR2(16)` | Instance name, if available |
| `OPEN_TIME` | `DATE` | Last time the thread was opened |
| `CURRENT_GROUP#` | `NUMBER` | Current log group |
| `SEQUENCE#` | `NUMBER` | Sequence number of current log |
| `CHECKPOINT_CHANGE#` | `NUMBER` | SCN at last checkpoint |
| `CHECKPOINT_TIME` | `DATE` | Time of last checkpoint |
| `ENABLE_CHANGE#` | `NUMBER` | SCN at which thread was enabled |
| `ENABLE_TIME` | `DATE` | Time of enable SCN |
| `DISABLE_CHANGE#` | `NUMBER` | SCN at which thread was disabled |
| `DISABLE_TIME` | `DATE` | Time of disable SCN |
| `LAST_REDO_SEQUENCE#` | `NUMBER` | Last redo sequence number written by LGWR |
| `LAST_REDO_BLOCK` | `NUMBER` | Last redo block written by LGWR |
| `LAST_REDO_CHANGE#` | `NUMBER` | SCN of last redo for the thread |
| `LAST_REDO_TIME` | `DATE` | Time of last redo for the thread |