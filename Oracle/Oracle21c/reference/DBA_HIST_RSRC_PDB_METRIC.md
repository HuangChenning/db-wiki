---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_RSRC_PDB_METRIC.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.41 DBA\_HIST\_RSRC\_PDB\_METRIC

`DBA_HIST_RSRC_PDB_METRIC` displays information about historical Resource Manager metrics for the past hour by PDB.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `BEGIN_TIME` | `TIMESTAMP(3)` | `NOT NULL` | Begin time of the interval |
| `END_TIME` | `TIMESTAMP(3)` | `NOT NULL` | End time of the interval |
| `INTSIZE_CSEC` | `NUMBER` | `NOT NULL` | Interval size (in hundredths of a second) |
| `SEQUENCE#` | `NUMBER` | `NOT NULL` | A sequential counter that uniquely describes the `V$RSRC_PLAN_HISTORY` entry to which these PDB statistics apply. When the instance is restarted, this value is reset to zero. |
| `CPU_CONSUMED_TIME` | `NUMBER` | `NOT NULL` | Cumulative amount of CPU time consumed by all sessions in the PDB, in milliseconds |
| `CPU_WAIT_TIME` | `NUMBER` | `NOT NULL` | Cumulative amount of time that sessions waited for CPU because of resource management, in milliseconds. This does not include waits due to latch or enqueue contention, I/O waits, and so on. When CPU resources are not being actively managed, this value is set to zero. |
| `AVG_RUNNING_SESSIONS` | `NUMBER` |  | Average number of sessions in the PDB that are currently running |
| `AVG_WAITING_SESSIONS` | `NUMBER` |  | Average number of sessions in the PDB that are waiting for CPU due to resource management. When CPU resources are not being actively managed, this value is set to zero. |
| `AVG_CPU_UTILIZATION` | `NUMBER` |  | Average percentage of CPU consumed by the PDB, with respect to the total number of CPUs in the system |
| `IOPS` | `NUMBER` |  | I/O operations per second during the previous minute for this PDB |
| `IOMBPS` | `NUMBER` |  | I/O megabytes per second during the previous minute for this PDB |
| `IOPS_THROTTLE_EXEMPT` | `NUMBER` |  | Indicates how much of the I/O per second in the current PDB was exempted from throttling.  For example, if the value in the `IOPS` column is 20 I/Os and the value in the `IOPS_THROTTLE_EXEMPT` column is 5 I/Os, then 5 I/Os of the 20 I/Os in that second were exempted from throttling.  I/O throttling is defined by the `MAX_IOPS` database initialization parameter. |
| `IOMBPS_THROTTLE_EXEMPT` | `NUMBER` |  | Indicates how many megabytes of I/O executed per second in the current PDB were exempted from throttling.  For example, if the value in the `IOMBPS` column is 200 megabytes and the value in the `IOMBPS_THROTTLE_EXEMPT` column is 50 megabytes, then 50 megabytes of the 200 megabytes were exempt from throttling.  I/O megabytes per second throttling is defined by the `MAX_MBPS` database initialization parameter. |
| `AVG_IO_THROTTLE` | `NUMBER` |  | Average throttle time per I/O operation in milliseconds during the previous minute for this PDB |
| `AVG_ACTIVE_PARALLEL_STMTS` | `NUMBER` |  | The average number of parallel statements that were running during the 1-minute metric window |
| `AVG_QUEUED_PARALLEL_STMTS` | `NUMBER` |  | The average number of parallel statements that were queued during the 1-minute metric window |
| `AVG_ACTIVE_PARALLEL_SERVERS` | `NUMBER` |  | The average number of parallel servers that were actively running as part of a parallel statement during the 1-minute metric window |
| `AVG_QUEUED_PARALLEL_SERVERS` | `NUMBER` |  | The average number of parallel servers that were requested by queued parallel statements during the 1-minute metric window |
| `SGA_BYTES` | `NUMBER` | `NOT NULL` | The current SGA usage for this PDB in bytes |
| `BUFFER_CACHE_BYTES` | `NUMBER` | `NOT NULL` | The current usage of the buffer cache by this PDB in bytes |
| `SHARED_POOL_BYTES` | `NUMBER` | `NOT NULL` | The current usage of the shared pool by this PDB in bytes |
| `PGA_BYTES` | `NUMBER` | `NOT NULL` | The current PGA usage for this PDB in bytes |
| `PLAN_ID` | `NUMBER` | `NOT NULL` | Resource Manager plan identifier |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `MAX_AVG_RUNNING_SESSIONS` | `NUMBER` | `NOT NULL` | Maximum value of `AVG_RUNNING_SESSIONS` during the last hour |