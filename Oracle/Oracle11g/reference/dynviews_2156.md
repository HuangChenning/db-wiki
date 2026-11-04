---
title: "V$RSRC_CONS_GROUP_HISTORY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2156.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RSRC_CONS_GROUP_HISTORY` displays a history of consumer group statistics for each entry in `V$RSRC_PLAN_HISTORY` that has a non-NULL plan.

| Column | Datatype | Description |
| --- | --- | --- |
| `SEQUENCE#` | `NUMBER` | A sequential counter that uniquely describes the `V$RSRC_PLAN_HISTORY` entry to which these consumer group statistics apply. When the instance is restarted, this value is reset to zero. |
| `ID` | `NUMBER` | Consumer group object ID (a unique number, consistent across database shutdowns and startups) |
| `NAME` | `VARCHAR2(30)` | Name of the consumer group |
| `REQUESTS` | `NUMBER` | Cumulative number of requests that were executed in the consumer group |
| `CPU_WAIT_TIME` | `NUMBER` | Cumulative amount of time that sessions waited for CPU because of resource management. This does not include waits due to latch or enqueue contention, I/O waits, and so on. |
| `CPU_WAITS` | `NUMBER` | Cumulative number of times all sessions in the consumer group had to wait for CPU because of resource management. This does not include waits due to latch or enqueue contention, I/O waits, and so on. |
| `CONSUMED_CPU_TIME` | `NUMBER` | Cumulative amount of CPU time consumed by all sessions in the consumer group (in milliseconds) |
| `YIELDS` | `NUMBER` | Cumulative number of times that sessions in the consumer group had to yield CPU to other sessions because of quantum expiration |
| `CPU_DECISIONS` | `NUMBER` | Percentage of CPU decisions for which the consumer group was present |
| `CPU_DECISIONS_EXCLUSIVE` | `NUMBER` | Percentage of the CPU decisions for which the consumer group was present and was the only consumer group present |
| `CPU_DECISIONS_WON` | `NUMBER` | Percentage of the CPU decisions that the consumer group won |
| `ACTIVE_SESS_LIMIT_HIT` | `NUMBER` | Number of times that sessions in the consumer group were queued because the consumer group reached its active session limit |
| `UNDO_LIMIT_HIT` | `NUMBER` | Number of times that queries in the consumer group were cancelled because the consumer group reached its `UNDO_POOL` limit |
| `SWITCHES_IN_CPU_TIME` | `NUMBER` | Number of switches into the consumer group because of the Resource Manager plan's `SWITCH_TIME` limit |
| `SWITCHES_OUT_CPU_TIME` | `NUMBER` | Number of switches out of the consumer group because of the Resource Manager plan's `SWITCH_TIME` limit |
| `SWITCHES_IN_IO_MEGABYTES` | `NUMBER` | Number of switches into the consumer group because of the Resource Manager plan's `SWITCH_IO_MEGABYTES` limit |
| `SWITCHES_OUT_IO_MEGABYTES` | `NUMBER` | Number of switches out of the consumer group because of the Resource Manager plan's `SWITCH_IO_MEGABYTES` limit |
| `SWITCHES_IN_IO_REQUESTS` | `NUMBER` | Number of switches into the consumer group because of the Resource Manager plan's `SWITCH_IO_REQS` limit |
| `SWITCHES_OUT_IO_REQUESTS` | `NUMBER` | Number of switches out of the consumer group because of the Resource Manager plan's `SWITCH_IO_REQS` limit |
| `SQL_CANCELED` | `NUMBER` | Number of times that SQL queries running in the consumer group were aborted because they exceeded the Resource Manager plan's `SWITCH_TIME` limit and `CANCEL_SQL` was specified as the Resource Manager plan's `SWITCH_GROUP` |
| `ACTIVE_SESS_KILLED` | `NUMBER` | Number of times that sessions running in the consumer group were terminated because they exceeded the Resource Manager plan's `SWITCH_TIME` limit and `KILL_SESSION` was specified as the Resource Manager plan's `SWITCH_GROUP` |
| `IDLE_SESS_KILLED` | `NUMBER` | Number of times that sessions in the consumer group were killed because they were idle for too long (reached `MAX_IDLE_TIME`) |
| `IDLE_BLKR_SESS_KILLED` | `NUMBER` | Number of times that sessions in the consumer group were killed because they were idle too long (reached `MAX_IDLE_BLOCKER_TIME`) and were blocking other sessions |
| `QUEUED_TIME` | `NUMBER` | Total amount of time that sessions in the consumer group have spent in the QUEUED state because of the active session limit (in milliseconds) |
| `QUEUE_TIME_OUTS` | `NUMBER` | Number of times that requests from sessions in the consumer group timed out because they were queued for too long (reached `QUEUEING_P1`) |
| `IO_SERVICE_TIME` | `NUMBER` | Cumulative I/O wait time (in milliseconds) |
| `IO_SERVICE_WAITS` | `NUMBER` | Total number of wait requests |
| `SMALL_READ_MEGABYTES` | `NUMBER` | Number of single block megabytes read |
| `SMALL_WRITE_MEGABYTES` | `NUMBER` | Number of single block megabytes written |
| `LARGE_READ_MEGABYTES` | `NUMBER` | Number of multiblock megabytes read |
| `LARGE_WRITE_MEGABYTES` | `NUMBER` | Number of multiblock megabytes written |
| `SMALL_READ_REQUESTS` | `NUMBER` | Number of single block read requests |
| `SMALL_WRITE_REQUESTS` | `NUMBER` | Number of single block write requests |
| `LARGE_READ_REQUESTS` | `NUMBER` | Number of multiblock read requests |
| `LARGE_WRITE_REQUESTS` | `NUMBER` | Number of multiblock write requests |
| `PQS_COMPLETED` <sup>Foot 1</sup> | `NUMBER` | Total number of completed parallel statements in the consumer group |
| `PQ_SERVERS_USED` <sup>Footref 1</sup> | `NUMBER` | Total number of parallel servers used by completed parallel statements in the consumer group |
| `PQS_QUEUED` <sup>Footref 1</sup> | `NUMBER` | Number of times that sessions in the consumer group were queued when trying to run parallel statements |
| `PQ_ACTIVE_TIME` <sup>Footref 1</sup> | `NUMBER` | Cumulative sum of the parallel active times for all completed parallel statements in the consumer group (in milliseconds) |
| `PQ_QUEUED_TIME` <sup>Footref 1</sup> | `NUMBER` | Total amount of time that sessions in the consumer group were queued when trying to run parallel statements (in milliseconds) |
| `PQ_QUEUE_TIME_OUTS` <sup>Footref 1</sup> | `NUMBER` | Number of times that parallel statements from sessions in the consumer group timed out because their queue time exceeded the Resource Manager plan's `PARALLEL_QUEUE_TIMEOUT` limit |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).