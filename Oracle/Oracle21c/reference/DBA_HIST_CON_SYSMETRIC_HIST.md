---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_CON_SYSMETRIC_HIST.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.389 DBA\_HIST\_CON\_SYSMETRIC\_HIST

`DBA_HIST_CON_SYSMETRIC_HIST` externalizes all available history of the system metric values for the entire set of data kept in the database. This view contains snapshots of `V$CON_SYSMETRIC_HISTORY`.

Note:

This view is not populated and is reserved for future use.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `BEGIN_TIME` | `DATE` |  | Begin time of the interval |
| `END_TIME` | `DATE` |  | End time of the interval |
| `INTSIZE` | `NUMBER` |  | Interval size (in hundredths of a second) |
| `GROUP_ID` | `NUMBER` |  | Group ID |
| `METRIC_ID` | `NUMBER` |  | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` |  | Metric name |
| `VALUE` | `NUMBER` |  | Metric value |
| `METRIC_UNIT` | `VARCHAR2(64)` |  | Unit of measurement |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - When queried from a non-CDB, the statistics for that instance are returned, and the `CON_ID` value is `0`. - When queried from the root of a CDB, the statistics in every container are returned, and the `CON_ID` value indicates the container to which the statistics belong. - When queried from a PDB, statistics from that PDB are returned, and the `CON_ID` value is the container ID for that PDB. |

See Also:

- " [V$CON\_SYSMETRIC\_HISTORY](V-CON_SYSMETRIC_HISTORY.md) "
- " [DBA\_HIST\_SYSMETRIC\_HISTORY](DBA_HIST_SYSMETRIC_HISTORY.md) "