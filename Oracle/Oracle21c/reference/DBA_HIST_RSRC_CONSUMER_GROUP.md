---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_RSRC_CONSUMER_GROUP.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.39 DBA\_HIST\_RSRC\_CONSUMER\_GROUP

`DBA_HIST_RSRC_CONSUMER_GROUP` displays historical information about Resource Manager consumer groups.

This view contains snapshots of `V$RSRC_CONS_GROUP_HISTORY`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `SEQUENCE#` | `NUMBER` | `NOT NULL` | A sequential counter that uniquely describes the `DBA_HIST_RSRC_PLAN` entry to which these consumer group statistics apply. When the instance is restarted, this value is reset to zero. |
| `CONSUMER_GROUP_ID` | `NUMBER` | `NOT NULL` | Consumer group object ID (a unique number, consistent across database shutdowns and startups) |
| `CONSUMER_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the consumer group |
| `REQUESTS` | `NUMBER` | `NOT NULL` | Cumulative number of requests that were executed in the consumer group |
| `CPU_WAIT_TIME` | `NUMBER` | `NOT NULL` | Cumulative amount of time that sessions waited for CPU because of resource management. This does not include waits due to latch or enqueue contention, I/O waits, and so on. |
| `CPU_WAITS` | `NUMBER` | `NOT NULL` | Cumulative number of times all sessions in the consumer group had to wait for CPU because of resource management. This does not include waits due to latch or enqueue contention, I/O waits, and so on. |
| `CONSUMED_CPU_TIME` | `NUMBER` | `NOT NULL` | Cumulative amount of CPU time consumed by all sessions in the consumer group (in milliseconds) |
| `YIELDS` | `NUMBER` | `NOT NULL` | Cumulative number of times that sessions in the consumer group had to yield CPU to other sessions because of quantum expiration |
| `ACTIVE_SESS_LIMIT_HIT` | `NUMBER` | `NOT NULL` | Number of times that sessions in the consumer group were queued because the consumer group reached its active session limit |
| `UNDO_LIMIT_HIT` | `NUMBER` | `NOT NULL` | Number of times that queries in the consumer group were cancelled because the consumer group reached its `UNDO_POOL` limit |
| `SWITCHES_IN_CPU_TIME` | `NUMBER` | `NOT NULL` | Number of switches into the consumer group because of the Resource Manager plan's `SWITCH_TIME` limit |
| `SWITCHES_OUT_CPU_TIME` | `NUMBER` | `NOT NULL` | Number of switches out of the consumer group because of the Resource Manager plan's `SWITCH_TIME` limit |
| `SWITCHES_IN_IO_MEGABYTES` | `NUMBER` | `NOT NULL` | Number of switches into the consumer group because of the Resource Manager plan's `SWITCH_IO_MEGABYTES` limit |
| `SWITCHES_OUT_IO_MEGABYTES` | `NUMBER` | `NOT NULL` | Number of switches out of the consumer group because of the Resource Manager plan's `SWITCH_IO_MEGABYTES` limit |
| `SWITCHES_IN_IO_REQUESTS` | `NUMBER` | `NOT NULL` | Number of switches into the consumer group because of the Resource Manager plan's `SWITCH_IO_REQS` limit |
| `SWITCHES_OUT_IO_REQUESTS` | `NUMBER` | `NOT NULL` | Number of switches out of the consumer group because of the Resource Manager plan's `SWITCH_IO_REQS` limit |
| `SWITCHES_IN_IO_LOGICAL` | `NUMBER` |  | Number of switches into the consumer group because of the Resource Manager plan's `SWITCH_IO_LOGICAL` limit |
| `SWITCHES_OUT_IO_LOGICAL` | `NUMBER` |  | Number of switches out of the consumer group because of the Resource Manager plan's `SWITCH_IO_LOGICAL` limit |
| `SWITCHES_IN_ELAPSED_TIME` | `NUMBER` |  | Number of switches into the consumer group because of the Resource Manager plan's `SWITCH_ELAPSED_TIME` limit |
| `SWITCHES_OUT_ELAPSED_TIME` | `NUMBER` |  | Number of switches out of the consumer group because of the Resource Manager plan's `SWITCH_ELAPSED_TIME` limit |
| `PGA_LIMIT_SESSIONS_KILLED` | `NUMBER` |  | The number of sessions that were terminated because their PGA allocation exceeded the PGA limit specified in the Resource Plan’s `SESSION_PGA_LIMIT` directive |
| `SQL_CANCELED` | `NUMBER` | `NOT NULL` | Number of times that SQL queries running in the consumer group were terminated because they exceeded the Resource Manager plan's `SWITCH_TIME` limit and `CANCEL_SQL` was specified as the Resource Manager plan's `SWITCH_GROUP` |
| `ACTIVE_SESS_KILLED` | `NUMBER` | `NOT NULL` | Number of times that sessions running in the consumer group were terminated because they exceeded the Resource Manager plan's `SWITCH_TIME` limit and `KILL_SESSION` was specified as the Resource Manager plan's `SWITCH_GROUP` |
| `IDLE_SESS_KILLED` | `NUMBER` | `NOT NULL` | Number of times that sessions in the consumer group were terminated because they were idle for too long (reached `MAX_IDLE_TIME`) |
| `IDLE_BLKR_SESS_KILLED` | `NUMBER` | `NOT NULL` | Number of times that sessions in the consumer group were terminated because they were idle too long (reached `MAX_IDLE_BLOCKER_TIME`) and were blocking other sessions |
| `QUEUED_TIME` | `NUMBER` | `NOT NULL` | Total amount of time that sessions in the consumer group have spent in the QUEUED state because of the active session limit (in milliseconds) |
| `QUEUE_TIME_OUTS` | `NUMBER` | `NOT NULL` | Number of times that requests from sessions in the consumer group timed out because they were queued for too long (reached `QUEUEING_P1`) |
| `IO_SERVICE_TIME` | `NUMBER` | `NOT NULL` | Cumulative I/O wait time (in milliseconds) |
| `IO_SERVICE_WAITS` | `NUMBER` | `NOT NULL` | Total number of wait requests |
| `SMALL_READ_MEGABYTES` | `NUMBER` | `NOT NULL` | Number of single block megabytes read |
| `SMALL_WRITE_MEGABYTES` | `NUMBER` | `NOT NULL` | Number of single block megabytes written |
| `LARGE_READ_MEGABYTES` | `NUMBER` | `NOT NULL` | Number of multiblock megabytes read |
| `LARGE_WRITE_MEGABYTES` | `NUMBER` | `NOT NULL` | Number of multiblock megabytes written |
| `SMALL_READ_REQUESTS` | `NUMBER` | `NOT NULL` | Number of single block read requests |
| `SMALL_WRITE_REQUESTS` | `NUMBER` | `NOT NULL` | Number of single block write requests |
| `LARGE_READ_REQUESTS` | `NUMBER` | `NOT NULL` | Number of multiblock read requests |
| `LARGE_WRITE_REQUESTS` | `NUMBER` | `NOT NULL` | Number of multiblock write requests |
| `PQS_QUEUED` | `NUMBER` |  | Number of times that sessions in the consumer group were queued when trying to run parallel statements |
| `PQ_QUEUED_TIME` | `NUMBER` |  | Total amount of time that sessions in the consumer group were queued when trying to run parallel statements (in milliseconds) |
| `PQ_QUEUE_TIME_OUTS` | `NUMBER` |  | Number of times that parallel statements from sessions in the consumer group timed out because their queue time exceeded the Resource Manager plan's `PARALLEL_QUEUE_TIMEOUT` limit |
| `PQS_COMPLETED` | `NUMBER` |  | Total number of completed parallel statements in the consumer group |
| `PQ_SERVERS_USED` | `NUMBER` |  | Total number of parallel servers used by completed parallel statements in the consumer group |
| `PQ_ACTIVE_TIME` | `NUMBER` |  | Cumulative sum of the parallel active times for all completed parallel statements in the consumer group (in milliseconds) |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$RSRC\_CONS\_GROUP\_HISTORY](V-RSRC_CONS_GROUP_HISTORY.md) "