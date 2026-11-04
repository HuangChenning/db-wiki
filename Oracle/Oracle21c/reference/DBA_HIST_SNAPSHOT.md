---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SNAPSHOT.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.58 DBA\_HIST\_SNAPSHOT

`DBA_HIST_SNAPSHOT` displays information about the snapshots in the Workload Repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `STARTUP_TIME` | `TIMESTAMP(3)` | `NOT NULL` | Startup time of the instance |
| `BEGIN_INTERVAL_TIME` | `TIMESTAMP(3)` | `NOT NULL` | Time at the beginning of the snapshot interval |
| `END_INTERVAL_TIME` | `TIMESTAMP(3)` | `NOT NULL` | Time at the end of the snapshot interval; the actual time the snapshot was taken |
| `FLUSH_ELAPSED` | `INTERVAL DAY(5) TO SECOND(1)` |  | Amount of time to perform the snapshot |
| `SNAP_LEVEL` | `NUMBER` |  | Snapshot level |
| `ERROR_COUNT` | `NUMBER` |  | Number of errors occurring in the tables for the particular snapshot |
| `SNAP_FLAG` | `NUMBER` |  | Condition under which the snapshot was inserted. Possible values are:  `0` - Snapshot was taken automatically by the Manageability Monitor Process (`MMON` process)  `1` - Manual snapshot created using a PL/SQL package  `2` - Imported snapshot  `4` - Snapshot taken while Diagnostic Pack or Tuning Pack was not enabled |
| `SNAP_TIMEZONE` | `INTERVAL` `DAY(0)` `TO` `SECOND(0)` |  | Snapshot time zone expressed as offset from UTC (Coordinated Universal Time) time zone |
| `BEGIN_INTERVAL_TIME_TZ` | `TIMESTAMP(3) WITH TIME ZONE` |  | Time at the beginning of the snapshot interval, with timezone |
| `END_INTERVAL_TIME_TZ` | `TIMESTAMP(3) WITH TIME ZONE` |  | Time at the end of the snapshot interval; the actual time the snapshot was taken, with timezone |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Table F-1](background-processes.md) for more information about the `MMON` process