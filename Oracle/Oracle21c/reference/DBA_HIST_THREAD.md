---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_THREAD.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.81 DBA\_HIST\_THREAD

`DBA_HIST_THREAD` displays historical thread information from the control file.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `THREAD#` | `NUMBER` | `NOT NULL` | Thread number |
| `THREAD_INSTANCE_NUMBER` | `NUMBER` |  | Instance number of the thread |
| `STATUS` | `VARCHAR2(6)` |  | Thread status (`OPEN`) or (`CLOSED`) |
| `OPEN_TIME` | `DATE` |  | Last time the thread was opened |
| `CURRENT_GROUP#` | `NUMBER` |  | Current log group |
| `SEQUENCE#` | `NUMBER` |  | Sequence number of the current log |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |