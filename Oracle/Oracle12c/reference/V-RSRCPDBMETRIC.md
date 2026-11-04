---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-RSRCPDBMETRIC.html
tags:
  - oracle
  - 12c
  - reference
---

`V$RSRCPDBMETRIC` displays information about resources consumed and wait times per consumer group for a PDB.

When the `STATISTICS_LEVEL` is set to `TYPICAL` or `ALL`, this view contains information about CPU utilization and wait times even when no Resource Manager plan is set or when the Resource Manager plan does not monitor CPU or session resources. Metrics are collected and stored every minute when CPU utilization is not being monitored.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time of the interval |
| `END_TIME` | `DATE` | End time of the interval |
| `INTSIZE_CSEC` | `NUMBER` | Interval size (in hundredths of a second) |
| `SEQUENCE#` | `NUMBER` | A sequential counter that uniquely describes the `V$RSRC_PLAN_HISTORY` entry to which these consumer group statistics apply. When the instance is restarted, this value is reset to zero. |
| `CPU_CONSUMED_TIME` | `NUMBER` | Cumulative amount of CPU time consumed by all sessions in the consumer group, in milliseconds |
| `CPU_WAIT_TIME` | `NUMBER` | Cumulative amount of time that sessions waited for CPU because of resource management, in milliseconds. This does not include waits due to latch or enqueue contention, I/O waits, and so on. When CPU resources are not being actively managed, this value is set to zero. |
| `NUM_CPUS` | `NUMBER` | Number of CPUs that the Resource Manager is utilizing. If instance caging is enabled, then this column is equal to the value of the `CPU_COUNT` initialization parameter. If instance caging is not enabled, then this column is equal to the total number of CPUs in the system. |
| `RUNNING_SESSIONS_LIMIT` | `NUMBER` | Maximum number of sessions in the consumer group that can run simultaneously. The value of this column is set by the Resource Manager plan's `MAX_UTILIZATION_LIMIT` directive. |
| `AVG_RUNNING_SESSIONS` | `NUMBER` | Average number of sessions in the consumer group that are currently running |
| `AVG_WAITING_SESSIONS` | `NUMBER` | Average number of sessions in the consumer group that are waiting for CPU due to resource management. When CPU resources are not being actively managed, this value is set to zero. |
| `CPU_UTILIZATION_LIMIT` | `NUMBER` | Maximum percentage of CPU that the consumer group can use at any time. The value of this column is set by the Resource Manager plan's `MAX_UTILIZATION_LIMIT` directive. If instance caging is enabled, then this value is derived using the `CPU_COUNT` initialization parameter. |
| `AVG_CPU_UTILIZATION` | `NUMBER` | Average percentage CPU consumed by the consumer group |
| `IOPS` | `NUMBER` | I/O operations per second during the previous minute for this PDB |
| `IOMBPS` | `NUMBER` | I/O megabytes per second during the previous minute for this PDB |
| `IOPS_THROTTLE_EXEMPT` | `NUMBER` | Indicates how much of the I/O per second in the current PDB was exempted from throttling.  For example, if the value in the `IOPS` column is 20 I/Os and the value in the `IOPS_THROTTLE_EXEMPT` column is 5 I/Os, then 5 I/Os of the 20 I/Os in that second were exempted from throttling.  I/O throttling is defined by the `MAX_IOPS` database initialization parameter. |
| `IOMBPS_THROTTLE_EXEMPT` | `NUMBER` | Indicates how many megabytes of I/O executed per second in the current PDB were exempted from throttling.  For example, if the value in the `IOMBPS` column is 200 megabytes and the value in the `IOMBPS_THROTTLE_EXEMPT` column is 50 megabytes, then 50 megabytes of the 200 megabytes were exempt from throttling.  I/O megabytes per second throttling is defined by the `MAX_MBPS` database initialization parameter. |
| `AVG_IO_THROTTLE` | `NUMBER` | Average throttle time per I/O operation in milliseconds during the previous minute for this PDB |
| `AVG_ACTIVE_PARALLEL_STMTS` | `NUMBER` | The average number of parallel statements that were running during the 1-minute metric window |
| `AVG_QUEUED_PARALLEL_STMTS` | `NUMBER` | The average number of parallel statements that were queued during the 1-minute metric window |
| `AVG_ACTIVE_PARALLEL_SERVERS` | `NUMBER` | The average number of parallel servers that were actively running as part of a parallel statement during the 1-minute metric window |
| `AVG_QUEUED_PARALLEL_SERVERS` | `NUMBER` | The average number of parallel servers that were requested by queued parallel statements during the 1-minute metric window |
| `PARALLEL_SERVERS_LIMIT` | `NUMBER` | The number of parallel servers allowed to be used by this consumer group during the 1-minute metric window |
| `SGA_BYTES` | `NUMBER` | The current SGA usage by this PDB in bytes |
| `BUFFER_CACHE_BYTES` | `NUMBER` | The current usage of the buffer cache by this PDB in bytes |
| `SHARED_POOL_BYTES` | `NUMBER` | The current usage of the shared pool by this PDB in bytes |
| `PGA_BYTES` | `NUMBER` | The current PGA usage by this PDB in bytes |
| `PLAN_NAME` | `VARCHAR2(30)` | Resource Manager plan name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: 	Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

" [STATISTICS\_LEVEL](STATISTICS_LEVEL.md) "