---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_RSRC_METRIC.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.40 DBA\_HIST\_RSRC\_METRIC

`DBA_HIST_RSRC_METRIC` displays information about historical Resource Manager metrics for the past hour.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `BEGIN_TIME` | `TIMESTAMP(3)` | `NOT NULL` | Begin time of the interval |
| `END_TIME` | `TIMESTAMP(3)` | `NOT NULL` | End time of the interval |
| `INTSIZE_CSEC` | `NUMBER` | `NOT NULL` | Interval size (in hundredths of a second) |
| `SEQUENCE#` | `NUMBER` | `NOT NULL` | A sequential counter that uniquely describes the `V$RSRC_PLAN_HISTORY` entry to which these consumer group statistics apply. When the instance is restarted, this value is reset to zero. |
| `CONSUMER_GROUP_ID` | `NUMBER` | `NOT NULL` | Consumer group object ID (a unique number, consistent across database shutdowns and startups) |
| `CPU_CONSUMED_TIME` | `NUMBER` | `NOT NULL` | Cumulative amount of CPU time consumed by all sessions in the consumer group, in milliseconds |
| `CPU_WAIT_TIME` | `NUMBER` | `NOT NULL` | Cumulative amount of time that sessions waited for CPU because of resource management, in milliseconds. This does not include waits due to latch or enqueue contention, I/O waits, and so on. When CPU resources are not being actively managed, this value is set to zero. |
| `AVG_RUNNING_SESSIONS` | `NUMBER` |  | Average number of sessions in the consumer group that are currently running |
| `AVG_WAITING_SESSIONS` | `NUMBER` |  | Average number of sessions in the consumer group that are waiting for CPU due to resource management. When CPU resources are not being actively managed, this value is set to zero. |
| `RUNNING_SESSION_LIMIT` | `NUMBER` |  | Maximum number of sessions in the consumer group that can run simultaneously. The value of this column is `NUM_CPUS` multiplied by the consumer group's `MAX_UTILIZATION_LIMIT` directive in the current Resource Manager plan. |
| `AVG_CPU_UTILIZATION` | `NUMBER` |  | Average percentage of CPU consumed by the consumer group, with respect to the total number of CPUs in the system |
| `IO_REQUESTS` | `NUMBER` | `NOT NULL` | I/O requests |
| `IO_MEGABYTES` | `NUMBER` | `NOT NULL` | I/O megabytes |
| `IOPS` | `NUMBER` |  | I/O operations per second during the previous minute for this PDB |
| `IOMBPS` | `NUMBER` |  | I/O megabytes per second during the previous minute for this PDB |
| `AVG_ACTIVE_PARALLEL_STMTS` | `NUMBER` |  | The average number of parallel statements that were running during the 1-minute metric window |
| `AVG_QUEUED_PARALLEL_STMTS` | `NUMBER` |  | The average number of parallel statements that were queued during the 1-minute metric window |
| `AVG_ACTIVE_PARALLEL_SERVERS` | `NUMBER` |  | The average number of parallel servers that were actively running as part of a parallel statement during the 1-minute metric window |
| `AVG_QUEUED_PARALLEL_SERVERS` | `NUMBER` |  | The average number of parallel servers that were requested by queued parallel statements during the 1-minute metric window |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |