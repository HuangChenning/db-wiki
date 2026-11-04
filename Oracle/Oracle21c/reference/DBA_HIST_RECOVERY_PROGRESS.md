---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_RECOVERY_PROGRESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.30 DBA\_HIST\_RECOVERY\_PROGRESS

`DBA_HIST_RECOVERY_PROGRESS` displays database recovery progress information for an instance.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `START_TIME` | `DATE` | `NOT NULL` | Start time of the recovery operation |
| `TYPE` | `VARCHAR2(64)` | `NOT NULL` | Type of recovery operation being performed:  - `CRASH RECOVERY` - `INSTANCE RECOVERY` - `MEDIA RECOVERY` |
| `ITEM` | `VARCHAR2(32)` | `NOT NULL` | Item being measured.  When `TYPE` is `CRASH RECOVERY` or `INSTANCE RECOVERY`, the possible values are:  - `Log Files` - `Redo Blocks`  When `TYPE` is `MEDIA RECOVERY`, the possible values are:  - `Active Apply Rate` - `Average Apply Rate` - `Maximum Apply Rate` - `Redo Applied` - `Log Files` - `Last Applied Redo` - `Active Time` - `Elapsed Time` - `Apply Time per Log` - `Checkpoint Time per Log` - `Standby Apply Lag` - `Recovery ID` |
| `UNITS` | `VARCHAR2(32)` |  | The units of measurement for each item |
| `SOFAR` | `NUMBER` |  | Amount of work done so far |
| `TOTAL` | `NUMBER` |  | Total amount of work expected |
| `TIMESTAMP` | `DATE` |  | Timestamp of the last redo record applied |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root. - n: Where n is the applicable container ID for the rows containing data |