---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RSRCMGRMETRIC.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.198 V$RSRCMGRMETRIC

`V$RSRCMGRMETRIC` displays information about resources consumed and wait times per consumer group.

When the `STATISTICS_LEVEL` is set to `TYPICAL` or `ALL`, this view contains information about CPU utilization and wait times even when no Resource Manager plan is set or when the Resource Manager plan does not monitor CPU or session resources. Metrics are collected and stored every minute when CPU utilization is not being monitored.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time of the interval |
| `END_TIME` | `DATE` | End time of the interval |
| `INTSIZE_CSEC` | `NUMBER` | Interval size (in hundredths of a second) |
| `SEQUENCE#` | `NUMBER` | A sequential counter that uniquely describes the `V$RSRC_PLAN_HISTORY` entry to which these consumer group statistics apply. When the instance is restarted, this value is reset to zero. |
| `CONSUMER_GROUP_ID` | `NUMBER` | Consumer group object ID (a unique number, consistent across database shutdowns and startups) |
| `CONSUMER_GROUP_NAME` | `VARCHAR2(30)` | Name of the consumer group |
| `CPU_CONSUMED_TIME` | `NUMBER` | Cumulative amount of CPU time consumed by all sessions in the consumer group, in milliseconds |
| `CPU_WAIT_TIME` | `NUMBER` | Cumulative amount of time that sessions waited for CPU because of resource management, in milliseconds. This does not include waits due to latch or enqueue contention, I/O waits, and so on. When CPU resources are not being actively managed, this value is set to zero. |
| `NUM_CPUS` | `NUMBER` | Number of CPUs that the Resource Manager is utilizing. If instance caging is enabled, then this column is equal to the value of the `CPU_COUNT` initialization parameter. If instance caging is not enabled, then this column is equal to the total number of CPUs in the system. |
| `RUNNING_SESSIONS_LIMIT` | `NUMBER` | Maximum number of sessions in the consumer group that can run simultaneously. The value of this column is `NUM_CPUS` multiplied by the consumer group's `MAX_UTILIZATION_LIMIT` directive in the current Resource Manager plan. |
| `AVG_RUNNING_SESSIONS` | `NUMBER` | Average number of sessions in the consumer group that are currently running |
| `AVG_WAITING_SESSIONS` | `NUMBER` | Average number of sessions in the consumer group that are waiting for CPU due to resource management. When CPU resources are not being actively managed, this value is set to zero. |
| `CPU_UTILIZATION_LIMIT` | `NUMBER` | Maximum percentage of CPU that the consumer group can use at any time, with respect to the total number of CPUs in the system. The value of this column is `RUNNING_SESSIONS_LIMIT` divided by the number of CPUs in the system. If instance caging is enabled, then this value is derived using the `CPU_COUNT` initialization parameter. |
| `AVG_CPU_UTILIZATION` | `NUMBER` | Average percentage of CPU consumed by the consumer group, with respect to the total number of CPUs in the system |
| `CPU_DECISIONS` | `NUMBER` | Percentage of CPU decisions for which the consumer group was present. When CPU resources are not being actively managed, this value is set to zero. This column is deprecated. |
| `CPU_DECISIONS_EXCLUSIVE` | `NUMBER` | Percentage of the CPU decisions for which the consumer group was present and was the only consumer group present. When CPU resources are not being actively managed, this value is set to zero. This column is deprecated. |
| `CPU_DECISIONS_WON` | `NUMBER` | Percentage of the CPU decisions that the consumer group won. When CPU resources are not being actively managed, this value is set to zero. This column is deprecated. |
| `IO_REQUESTS` | `NUMBER` | I/O requests |
| `IO_MEGABYTES` | `NUMBER` | I/O megabytes |
| `AVG_ACTIVE_PARALLEL_STMTS` | `NUMBER` | The average number of parallel statements that were running during the 1-minute metric window |
| `AVG_QUEUED_PARALLEL_STMTS` | `NUMBER` | The average number of parallel statements that were queued during the 1-minute metric window |
| `AVG_ACTIVE_PARALLEL_SERVERS` | `NUMBER` | The average number of parallel servers that were actively running as part of a parallel statement during the 1-minute metric window |
| `AVG_QUEUED_PARALLEL_SERVERS` | `NUMBER` | The average number of parallel servers that were requested by queued parallel statements during the 1-minute metric window |
| `PARALLEL_SERVERS_LIMIT` | `NUMBER` | The number of parallel servers allowed to be used by this consumer group during the 1-minute metric window |
| `PLAN_NAME` | `VARCHAR2(30)` | Resource Manager plan name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [STATISTICS\_LEVEL](STATISTICS_LEVEL.md) "