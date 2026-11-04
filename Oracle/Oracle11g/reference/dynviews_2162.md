---
title: "V$RSRC_SESSION_INFO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2162.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RSRC_SESSION_INFO` displays Resource Manager statistics per session.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier |
| `CURRENT_CONSUMER_GROUP_ID` | `NUMBER` | Object ID of the consumer group in which the session currently belongs; NULL if the session has not yet logged in |
| `ORIG_CONSUMER_GROUP_ID` | `NUMBER` | Object ID of the consumer group in which the session was placed by the consumer group mappings; NULL if the session has not yet logged in  This group may not be the current group because the `SWITCH_GROUP` directive in the current plan may have changed the session's current group. This group may not equal the `MAPPED_CONSUMER_GROUP` because the `MAPPED_CONSUMER_GROUP` may not be part of the current plan. |
| `MAPPING_ATTRIBUTE` | `VARCHAR2(32)` | Session attribute that was used to map the session into its original consumer group; NULL if no mapping was used  See Also: ["DBA\_RSRC\_GROUP\_MAPPINGS"](statviews_4225.md) for more details |
| `MAPPED_CONSUMER_GROUP` | `VARCHAR2(32)` | Consumer group to which the session was originally mapped; NULL if no mapping was used  This may not correspond to the original consumer group, because the mapped group may not be part of the current plan.  See Also: ["DBA\_RSRC\_GROUP\_MAPPINGS"](statviews_4225.md) for more details |
| `STATE` | `VARCHAR2(32)` | Current state of the session: - `NOT MANAGED` - Session has not logged in or the current Resource Manager plan does not require the session to be managed at this point in time - `RUNNING` - Session is currently running on the CPU - `WAITING FOR CPU` - Session is ready to run. It is waiting for a CPU quantum to run. - `QUEUED` - Session is queued because the active session limit was reached - `IDLE` - Session is idle - `IDLE BLKR` - Session is idle and blocking another session - `WAITING` - Session is currently in a wait 	See Also: ["V$SESSION\_WAIT"](dynviews_3024.md) for the wait type - `WAITING_FOR_IO` - Session is waiting to submit an I/O request - `UNBOUND` - Session is not bound to any process - `EXITING` - Session is about to terminate |
| `ACTIVE` | `VARCHAR2(5)` | Indicates whether the session is currently active (`TRUE`) or not (`FALSE`). This includes when one of the following conditions is true: - Session is in the top call - Session has a transaction in progress - Session is using temporary space objects - Session holds user enqueues |
| `CURRENT_IDLE_TIME` | `NUMBER` | Number of seconds the session has been idle (in states `IDLE` or `IDLE BLKR`) while in this consumer group; NULL if the current Resource Manager plan does not require updating this statistic. This value is reset to zero when the session becomes active. |
| `CURRENT_CPU_WAIT_TIME` | `NUMBER` | Amount of time (in milliseconds) the session has waited for CPU because of resource management (in state `WAIT FOR CPU`) while in the current consumer group; NULL if the current Resource Manager plan does not require updating this statistic. This does not include waits due to latch or enqueue contention, I/O waits, and so on. If `SWITCH_TIME_IN_CALL` is used, then this will be reset at the end of every call. |
| `CPU_WAIT_TIME` | `NUMBER` | Cumulative amount of time (in milliseconds) the session has waited for CPU (in its lifetime) because of resource management. This does not include waits due to latch or enqueue contention, I/O waits, and so on. |
| `CURRENT_CPU_WAITS` | `NUMBER` | Number of times the session had to wait for CPU because of resource management while in this consumer group; NULL if the current Resource Manager plan does not require updating this statistic. This does not include waits due to latch or enqueue contention, I/O waits, and so on. If `SWITCH_TIME_IN_CALL` is used, then this will be reset at the end of every call. |
| `CPU_WAITS` | `NUMBER` | Cumulative number of times the session had to wait for CPU (in its lifetime) because of resource management. This does not include waits due to latch or enqueue contention, I/O waits, and so on. |
| `CURRENT_CONSUMED_CPU_TIME` | `NUMBER` | Amount of CPU time (in milliseconds) consumed by the session while in the current consumer group; NULL if the current Resource Manager plan does not require updating this statistic. If `SWITCH_TIME_IN_CALL` is used, then this will be reset at the end of every call. |
| `CONSUMED_CPU_TIME` | `NUMBER` | Cumulative amount of CPU time consumed by the session (in its lifetime) (in milliseconds) |
| `CURRENT_ACTIVE_TIME` | `NUMBER` | Amount of time (in milliseconds) the session has been active while in the current consumer group; NULL if the current Resource Manager plan does not require updating this statistic. Active time is time spent running and waiting while executing a call. It does not include the time a session waited for CPU resources. If `SWITCH_TIME_IN_CALL` is used, then this is reset at the end of every call. |
| `ACTIVE_TIME` | `NUMBER` | Cumulative amount of active time (in milliseconds) consumed by the session (in its lifetime) |
| `CURRENT_QUEUED_TIME` | `NUMBER` | Amount of time (in milliseconds) the current request from the session has been queued (in state `QUEUED`). If the session does not have a request currently queued up, then this number will be zero. |
| `QUEUED_TIME` | `NUMBER` | Total amount of time (in milliseconds) the session has spent in the QUEUED state (in its lifetime) |
| `CURRENT_YIELDS` | `NUMBER` | Number of times the session had to yield the CPU to other sessions (due to quantum expiration) while in the current consumer group; NULL if the current Resource Manager plan does not require updating this statistic. If `SWITCH_TIME_IN_CALL` is used, then this is reset at the end of every call. |
| `YIELDS` | `NUMBER` | Cumulative number of times the session had to yield CPU to other sessions due to quantum expiration (in its lifetime) |
| `CURRENT_UNDO_CONSUMPTION` | `NUMBER` | Current amount (in KB) of undo consumed by the session; NULL if the current Resource Manager plan does not have an `UNDO_POOL` directive |
| `MAX_UNDO_CONSUMPTION` | `NUMBER` | Maximum amount of undo consumed (in KB) during the session's lifetime. This value may not be updated because the current Resource Manager plan may not have an `UNDO_POOL` directive. |
| `SQL_CANCELED` | `NUMBER` | Number of times SQL queries running in the session were canceled due to exceeding the Resource Manager plan's `SWITCH_TIME` limit. |
| `QUEUE_TIME_OUTS` | `NUMBER` | Number of times requests from the session timed out because they queued longer than the Resource Manager plan's limit |
| `ESTIMATED_EXECUTION_LIMIT_HIT` | `NUMBER` | Number of times requests from the session were not run because the optimizer's estimated time to execute the query exceeded the `MAX_EST_EXEC_TIME` limit |
| `CURRENT_IO_SERVICE_TIME` | `NUMBER` | Current I/O wait time of the session (in milliseconds) |
| `IO_SERVICE_TIME` | `NUMBER` | Cumulative amount of I/O wait time by the session (in its lifetime) (in milliseconds) |
| `CURRENT_IO_SERVICE_WAITS` | `NUMBER` | Current I/O waits by session |
| `IO_SERVICE_WAITS` | `NUMBER` | Cumulative I/O waits by session (in its lifetime) |
| `CURRENT_SMALL_READ_MEGABYTES` | `NUMBER` | Number of single block megabytes read by the session |
| `SMALL_READ_MEGABYTES` | `NUMBER` | Total number of single block megabytes read by the session (in its lifetime) |
| `CURRENT_LARGE_READ_MEGABYTES` | `NUMBER` | Number of multiblock megabytes read by the session |
| `LARGE_READ_MEGABYTES` | `NUMBER` | Total number of multiblock megabytes read by the session (in its lifetime) |
| `CURRENT_SMALL_WRITE_MEGABYTES` | `NUMBER` | Number of single block megabytes written by the session |
| `SMALL_WRITE_MEGABYTES` | `NUMBER` | Total number of single block megabytes written by the session (in its lifetime) |
| `CURRENT_LARGE_WRITE_MEGABYTES` | `NUMBER` | Number of multiblock megabytes written by the session |
| `LARGE_WRITE_MEGABYTES` | `NUMBER` | Total number of multiblock megabytes written by the session (in its lifetime) |
| `CURRENT_SMALL_READ_REQUESTS` | `NUMBER` | Number of single block read requests by the session |
| `SMALL_READ_REQUESTS` | `NUMBER` | Total number of single block read requests by the session (in its lifetime) |
| `CURRENT_SMALL_WRITE_REQUESTS` | `NUMBER` | Number of single block write requests by the session |
| `SMALL_WRITE_REQUESTS` | `NUMBER` | Total number of single block write requests by the session (in its lifetime) |
| `CURRENT_LARGE_READ_REQUESTS` | `NUMBER` | Number of multiblock read requests by the session |
| `LARGE_READ_REQUESTS` | `NUMBER` | Total number of multiblock read requests by the session (in its lifetime) |
| `CURRENT_LARGE_WRITE_REQUESTS` | `NUMBER` | Number of multiblock write requests by the session |
| `LARGE_WRITE_REQUESTS` | `NUMBER` | Total number of multiblock write requests by the session (in its lifetime) |
| `CURRENT_PQ_ACTIVE_TIME` <sup>Foot 1</sup> | `NUMBER` | Amount of time that the current active parallel statement has been executing, not including the amount of time that the statement has been queued (in milliseconds). If the parallel statement is queued, then the value is 0. |
| `PQ_ACTIVE_TIME` <sup>Footref 1</sup> | `NUMBER` | Cumulative amount of time that parallel statements have been executed over the lifetime of the session (in milliseconds) |
| `DOP` <sup>Footref 1</sup> |  | Degree of parallelism for the active or queued parallel statement |
| `ESTIMATED_EXECUTION_TIME` <sup>Footref 1</sup> | `NUMBER` | Estimated execution time for the parallel statement, as estimated by the optimizer (in milliseconds). You can compare this value to `CURRENT_PQ_ACTIVE_TIME` to estimate how much longer the parallel statement will run. |
| `CURRENT_PQ_QUEUED_TIME` <sup>Footref 1</sup> | `NUMBER` | Amount of time that the current parallel statement in the session has been queued (in milliseconds). If the session does not have a queued parallel statement, then the value is 0. |
| `PQ_QUEUED_TIME` <sup>Footref 1</sup> | `NUMBER` | Total amount of time that the session has spent in the `PQ_QUEUED` state in its lifetime (in milliseconds) |
| `PQ_QUEUED` <sup>Footref 1</sup> | `NUMBER` | Number of times that parallel statements in the session have been queued |
| `PQ_QUEUE_TIME_OUTS` <sup>Footref 1</sup> | `NUMBER` | Number of times that parallel statements in the session timed out because their queue time exceeded the Resource Manager plan's `PARALLEL_QUEUE_TIMEOUT` limit |
| `PQ_ACTIVE` <sup>Footref 1</sup> | `VARCHAR2(5)` | Indicates whether the session is actively running a parallel statement (`TRUE`) or not (`FALSE`). |
| `LAST_ACTION` <sup>Foot 2</sup> | `VARCHAR2(48)` | The most recent action that was taken on this SQL operation by Resource Manager. Its value is one of the following: - `CANCEL_SQL` - `KILL_SESSION` - `LOG_ONLY` - `SWITCH TO <CG NAME>`  For the last value, `<CG NAME>` is the name of the consumer group that the SQL operation was switched to. If the Resource Plan has since been changed then `<CG NAME>` is the ID of the consumer group. |
| `LAST_ACTION_REASON` <sup>Footref 2</sup> | `VARCHAR2(30)` | The reason for the most recent action that was taken on this SQL operation by Resource Manager. Its value is one of the following: |
| `LAST_ACTION_TIME` <sup>Footref 2</sup> | `DATE` | The time of the most recent action that was taken on this SQL operation by Resource Manager |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

<sup>Footnote 2</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.4)