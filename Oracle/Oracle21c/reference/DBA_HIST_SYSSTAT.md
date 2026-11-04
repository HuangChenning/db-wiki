---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SYSSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.74 DBA\_HIST\_SYSSTAT

`DBA_HIST_SYSSTAT` displays historical system statistics information, including OLAP kernel statistics.

This view contains snapshots of `V$SYSSTAT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `STAT_ID` | `NUMBER` | `NOT NULL` | Statistic identifier |
| `STAT_NAME` | `VARCHAR2(64)` | `NOT NULL` | Statistic name |
| `VALUE` | `NUMBER` |  | Statistic value |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SYSSTAT](V-SYSSTAT.md) "