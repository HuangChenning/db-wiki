---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-THREAD.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.115 V$THREAD

This view does not return meaningful results on a physical standby database.

| Column | Datatype | Description |
| --- | --- | --- |
| `THREAD#` | `NUMBER` | Thread number |
| `STATUS` | `VARCHAR2(6)` | Thread status (`OPEN` \| `CLOSED`) |
| `ENABLED` | `VARCHAR2(8)` | Enabled status: `DISABLED`, (enabled) `PRIVATE`, or (enabled) `PUBLIC` |
| `GROUPS` | `NUMBER` | Number of log groups assigned to this thread |
| `INSTANCE` | `VARCHAR2(80)` | Instance name, if available |
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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |