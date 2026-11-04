---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_WR_CONTROL.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.86 DBA\_HIST\_WR\_CONTROL

`DBA_HIST_WR_CONTROL` displays the control information for the Workload Repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `SNAP_INTERVAL` | `INTERVAL DAY(5) TO SECOND(1)` | `NOT NULL` | Snapshot interval; how often to automatically take snapshots |
| `RETENTION` | `INTERVAL DAY(5) TO SECOND(1)` | `NOT NULL` | Retention setting for the snapshots; amount of time to keep the snapshots |
| `TOPNSQL` | `VARCHAR2(10)` |  | The number of Top SQL flushed for each SQL criteria (elapsed time, CPU time, parse calls, sharable memory, version count) |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `SRC_DBID` | `NUMBER` |  | Database ID of the non-CDB, CDB, or PDB where the AWR snapshot data was collected |
| `SRC_DBNAME` | `VARCHAR2(128)` |  | Database name of the non-CDB, CDB, or PDB where the AWR snapshot data was collected |
| `TABLESPACE_NAME` | `VARCHAR2(128)` |  | Name of the tablespace in which AWR snapshot data resides |