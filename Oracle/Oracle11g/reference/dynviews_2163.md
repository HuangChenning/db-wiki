---
title: "V$RSRCMGRMETRIC"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2163.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RSRCMGRMETRIC` displays information about resources consumed and wait times per consumer group.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time for the metric value |
| `END_TIME` | `DATE` | End time for the metric value |
| `INTSIZE_CSEC` | `NUMBER` | Size of the time period |
| `SEQUENCE#` | `NUMBER` | A sequential counter that uniquely describes the `V$RSRC_PLAN_HISTORY` entry to which these consumer group statistics apply. When the instance is restarted, this value is reset to zero. |
| `CONSUMER_GROUP_ID` | `NUMBER` | Consumer group object ID (a unique number, consistent across database shutdowns and startups) |
| `CONSUMER_GROUP_NAME` | `VARCHAR2(30)` | Name of the consumer group |
| `CPU_CONSUMED_TIME` | `NUMBER` | Cumulative amount of CPU time consumed by all sessions in the consumer group, in milliseconds |
| `CPU_WAIT_TIME` | `NUMBER` | Cumulative amount of time that sessions waited for CPU because of resource management, in milliseconds. This does not include waits due to latch or enqueue contention, I/O waits, and so on. |
| `NUM_CPUS` <sup>Foot 1</sup> | `NUMBER` | Number of CPUs that the Resource Manager is utilizing. If instance caging is enabled, then this column is equal to the value of the `CPU_COUNT` initialization parameter. If instance caging is not enabled, then this column is equal to the total number of CPUs in the system. |
| `RUNNING_SESSIONS_LIMIT` <sup>Footref 1</sup> | `NUMBER` | Maximum number of sessions in the consumer group that can run simultaneously. The value of this column is set by the Resource Manager plan's `MAX_UTILIZATION_LIMIT` directive. |
| `AVG_RUNNING_SESSIONS` <sup>Footref 1</sup> | `NUMBER` | Average number of sessions in the consumer group that are currently running |
| `AVG_WAITING_SESSIONS` <sup>Footref 1</sup> | `NUMBER` | Average number of sessions in the consumer group that are waiting for CPU due to resource management |
| `CPU_UTILIZATION_LIMIT` <sup>Footref 1</sup> | `NUMBER` | Maximum percentage of CPU that the consumer group can utilize at any time. The value of this column is set by the Resource Manager plan's `MAX_UTILIZATION_LIMIT` directive. If instance caging is enabled, then this value is derived using the `CPU_COUNT` initialization parameter. |
| `AVG_CPU_UTILIZATION` <sup>Footref 1</sup> | `NUMBER` | Average percentage CPU consumed by the consumer group |
| `CPU_DECISIONS` | `NUMBER` | Percentage of CPU decisions for which the consumer group was present. This column is deprecated. |
| `CPU_DECISIONS_EXCLUSIVE` | `NUMBER` | Percentage of the CPU decisions for which the consumer group was present and was the only consumer group present. This column is deprecated. |
| `CPU_DECISIONS_WON` | `NUMBER` | Percentage of the CPU decisions that the consumer group won. This column is deprecated. |
| `IO_REQUESTS` | `NUMBER` | I/O requests |
| `IO_MEGABYTES` | `NUMBER` | I/O megabytes |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).