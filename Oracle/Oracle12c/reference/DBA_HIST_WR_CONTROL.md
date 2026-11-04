---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_HIST_WR_CONTROL.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_HIST_WR_CONTROL` displays the control information for the Workload Repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `SNAP_INTERVAL` | `INTERVAL DAY(5) TO SECOND(1)` | `NOT NULL` | Snapshot interval; how often to automatically take snapshots |
| `RETENTION` | `INTERVAL DAY(5) TO SECOND(1)` | `NOT NULL` | Retention setting for the snapshots; amount of time to keep the snapshots |
| `TOPNSQL` | `VARCHAR2(10)` |  | The number of Top SQL flushed for each SQL criteria (elapsed time, CPU time, parse calls, sharable memory, version count) |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |