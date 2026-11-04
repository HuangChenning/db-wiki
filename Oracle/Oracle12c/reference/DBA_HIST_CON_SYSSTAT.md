---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_HIST_CON_SYSSTAT.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_HIST_CON_SYSSTAT` displays historical system statistics information, including OLAP kernel statistics. This view contains snapshots of `V$CON_SYSSTAT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `STAT_ID` | `NUMBER` | `NOT NULL` | Statistic identifier |
| `STAT_NAME` | `VARCHAR2(64)` | `NOT NULL` | Statistic name |
| `VALUE` | `NUMBER` |  | Statistic value |
| `CON_DBID` | `NUMBER` | `NOT NULL` | The database ID for the PDB of the sampled session |
| `CON_ID` | `NUMBER` | `NOT NULL` | The ID of the container that `CON_DBID` identifies. Possible values include: - When queried from a non-CDB, the statistics for that instance are returned, and the `CON_ID` value is `0`. - When queried from the root of a CDB, the statistics in every container are returned, and the `CON_ID` value indicates the container to which the statistics belong. - When queried from a PDB, statistics from that PDB are returned, and the `CON_ID` value is the container ID for that PDB. |

See Also:

- " [V$CON\_SYSSTAT](V-CON_SYSSTAT.md) "
- " [DBA\_HIST\_SYSSTAT](DBA_HIST_SYSSTAT.md) "

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).