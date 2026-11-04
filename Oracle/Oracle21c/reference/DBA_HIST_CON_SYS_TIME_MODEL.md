---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_CON_SYS_TIME_MODEL.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.388 DBA\_HIST\_CON\_SYS\_TIME\_MODEL

`DBA_HIST_CON_SYS_TIME_MODEL` displays historical system time model statistics, including OLAP timed stastistics. This view contains snapshots of `V$SYS_TIME_MODEL`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `STAT_ID` | `NUMBER` |  | Statistic ID |
| `STAT_NAME` | `VARCHAR2(64)` |  | Statistic name |
| `VALUE` | `NUMBER` |  | Statistic value |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - When queried from a non-CDB, the statistics for that instance are returned, and the `CON_ID` value is `0`. - When queried from the root of a CDB, the statistics in every container are returned, and the `CON_ID` value indicates the container to which the statistics belong. - When queried from a PDB, statistics from that PDB are returned, and the `CON_ID` value is the container ID for that PDB. |