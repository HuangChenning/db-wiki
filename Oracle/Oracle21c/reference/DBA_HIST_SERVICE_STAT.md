---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SERVICE_STAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.47 DBA\_HIST\_SERVICE\_STAT

`DBA_HIST_SERVICE_STAT` displays the history of important service statistics tracked by the Workload Repository.

The call rate statistics in this view can be used for making run-time routing decisions, for tracking service levels, and for per-instance diagnostics per call rate.

The elapsed timing for each call provides a relative value across instances for how well a node is processing SQL calls issued under a service name. When aggregation is enabled for the service name, this view provides historical data on the timing and work done for calls issued for the whole service. This view contains information from `V$SERVICE_STATS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `SERVICE_NAME_HASH` | `NUMBER` | `NOT NULL` | Hash of the service name |
| `SERVICE_NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the service |
| `STAT_ID` | `NUMBER` | `NOT NULL` | Statistic identifier |
| `STAT_NAME` | `VARCHAR2(64)` | `NOT NULL` | Statistic name |
| `VALUE` | `NUMBER` |  | Value of the statistic |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SERVICE\_STATS](V-SERVICE_STATS.md) "