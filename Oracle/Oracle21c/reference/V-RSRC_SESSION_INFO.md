---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RSRC_SESSION_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.197 V$RSRC\_SESSION\_INFO

`V$RSRC_SESSION_INFO` displays Resource Manager statistics per session.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier |
| `CURRENT_CONSUMER_GROUP_ID` | `NUMBER` | Object ID of the consumer group in which the session currently belongs; NULL if the session has not yet logged in |
| `CURRENT_CONSUMER_GROUP` | `VARCHAR2(32)` | The name of the consumer group in which the session currently belongs |
| `ORIG_CONSUMER_GROUP_ID` | `NUMBER` | Object ID of the consumer group in which the session was placed by the consumer group mappings; NULL if the session has not yet logged in  This group may not be the current group because the `SWITCH_GROUP` directive in the current plan may have changed the session's current group. This group may not equal the `MAPPED_CONSUMER_GROUP` because the `MAPPED_CONSUMER_GROUP` may not be part of the current plan. |
| `MAPPING_ATTRIBUTE` | `VARCHAR2(32)` | Session attribute that was used to map the session into its original consumer group; NULL if no mapping was used  See Also: " [DBA\_RSRC\_GROUP\_MAPPINGS](DBA_RSRC_GROUP_MAPPINGS.md) " for more details |
| `MAPPED_CONSUMER_GROUP` | `VARCHAR2(32)` | Consumer group to which the session was originally mapped; NULL if no mapping was used  This may not correspond to the original consumer group, because the mapped group may not be part of the current plan.  See Also: " [DBA\_RSRC\_GROUP\_MAPPINGS](DBA_RSRC_GROUP_MAPPINGS.md) " for more details |
| `STATE` | `VARCHAR2(32)` | Current state of the session:  - `NOT MANAGED` - Session has not logged in or the current Resource Manager plan does not require the session to be managed at this point in time - `RUNNING` - Session is currently running on the CPU - `WAITING FOR CPU` - Session is ready to run. It is waiting for a CPU quantum to run. - `QUEUED` - Session is queued because the active session limit was reached - `IDLE` - Session is idle - `IDLE BLKR` - Session is idle and blocking another session - `WAITING` - Session is currently in a wait 	See Also: " [V$SESSION\_WAIT](V-SESSION_WAIT.md) " for the wait type - `WAITING_FOR_IO` - Session is waiting to submit an I/O request - `UNBOUND` - Session is not bound to any process - `EXITING` - Session is about to terminate |
| `ACTIVE` | `VARCHAR2(5)` | Indicates whether the session is currently active (`TRUE`) or not (`FALSE`). This includes when one of the following conditions is true:  - Session is in the top call - Session has a transaction in progress - Session is using temporary space objects - Session holds user enqueues |
| `CURRENT_IDLE_TIME` | `NUMBER` | Number of milliseconds the session has been idle (in states `IDLE` or `IDLE BLKR`) while in this consumer group; NULL if the current Resource Manager plan does not require updating this statistic. This value is reset to zero when the session becomes active. |
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
| `CURRENT_IO_SERVICE_TIME` | `NUMBER` | Current I/O wait time of the session (in milliseconds) for the current SQL operation |
| `IO_SERVICE_TIME` | `NUMBER` | Cumulative amount of I/O wait time by the session (in its lifetime) (in milliseconds) |
| `CURRENT_IO_SERVICE_WAITS` | `NUMBER` | Current I/O waits by session for the current SQL operation |
| `IO_SERVICE_WAITS` | `NUMBER` | Cumulative I/O waits by session (in its lifetime) |
| `CURRENT_SMALL_READ_MEGABYTES` | `NUMBER` | Number of single block megabytes read by the session for the current SQL operation |
| `SMALL_READ_MEGABYTES` | `NUMBER` | Total number of single block megabytes read by the session (in its lifetime) |
| `CURRENT_LARGE_READ_MEGABYTES` | `NUMBER` | Number of multiblock megabytes read by the session for the current SQL operation |
| `LARGE_READ_MEGABYTES` | `NUMBER` | Total number of multiblock megabytes read by the session (in its lifetime) |
| `CURRENT_SMALL_WRITE_MEGABYTES` | `NUMBER` | Number of single block megabytes written by the session for the current SQL operation |
| `SMALL_WRITE_MEGABYTES` | `NUMBER` | Total number of single block megabytes written by the session (in its lifetime) |
| `CURRENT_LARGE_WRITE_MEGABYTES` | `NUMBER` | Number of multiblock megabytes written by the session for the current SQL operation |
| `LARGE_WRITE_MEGABYTES` | `NUMBER` | Total number of multiblock megabytes written by the session (in its lifetime) |
| `CURRENT_SMALL_READ_REQUESTS` | `NUMBER` | Number of single block read requests by the session for the current SQL operation |
| `SMALL_READ_REQUESTS` | `NUMBER` | Total number of single block read requests by the session (in its lifetime) |
| `CURRENT_SMALL_WRITE_REQUESTS` | `NUMBER` | Number of single block write requests by the session for the current SQL operation |
| `SMALL_WRITE_REQUESTS` | `NUMBER` | Total number of single block write requests by the session (in its lifetime) |
| `CURRENT_LARGE_READ_REQUESTS` | `NUMBER` | Number of multiblock read requests by the session for the current SQL operation |
| `LARGE_READ_REQUESTS` | `NUMBER` | Total number of multiblock read requests by the session (in its lifetime) |
| `CURRENT_LARGE_WRITE_REQUESTS` | `NUMBER` | Number of multiblock write requests by the session for the current SQL operation |
| `LARGE_WRITE_REQUESTS` | `NUMBER` | Total number of multiblock write requests by the session (in its lifetime) |
| `CURRENT_PQ_ACTIVE_TIME` | `NUMBER` | Amount of time that the current active parallel statement has been executing for the current SQL operation, not including the amount of time that the statement has been queued (in milliseconds). If the parallel statement is queued, then the value is 0. |
| `PQ_ACTIVE_TIME` | `NUMBER` | Cumulative amount of time that parallel statements have been executed over the lifetime of the session (in milliseconds) |
| `DOP` | `NUMBER` | Degree of parallelism for the active or queued parallel statement, if there are any in the session |
| `PQ_SERVERS` | `NUMBER` | The number of active parallel servers if the session is active and running the parallel query. If the query is queued, the number of parallel servers that this query is trying to run with is shown. |
| `ESTIMATED_EXECUTION_TIME` | `NUMBER` | Estimated execution time for the parallel statement, as estimated by the optimizer (in milliseconds). You can compare this value to `CURRENT_PQ_ACTIVE_TIME` to estimate how much longer the parallel statement will run. |
| `CURRENT_PQ_QUEUED_TIME` | `NUMBER` | Amount of time that the current parallel statement in the session has been queued (in milliseconds) for the current SQL operation. If the session does not have a queued parallel statement, then the value is 0. |
| `PQ_QUEUED_TIME` | `NUMBER` | Total amount of time that the session has spent in the `PQ_QUEUED` state in its lifetime (in milliseconds) |
| `PQ_QUEUED` | `NUMBER` | Number of times that parallel statements in the session have been queued |
| `PQ_QUEUE_TIME_OUTS` | `NUMBER` | Number of times that parallel statements in the session timed out because their queue time exceeded the Resource Manager plan's `PARALLEL_QUEUE_TIMEOUT` limit |
| `PQ_ACTIVE` | `VARCHAR2(5)` | Indicates whether the session is actively running a parallel statement (`TRUE`) or not (`FALSE`). |
| `PQ_STATUS` | `VARCHAR2(44)` | The status of the parallel statement running in this session:  - `Active`: The parallel statement is currently active and running - `Queued`: The parallel statement is queued and is not a possible candidate to be run next - `Queue head`: The parallel statement is queued due to the global systemwide limit and is the next parallel statement to be dequeued and run - `Queue head - waiting on CG limit`: The parallel statement is queued due to the consumer group limit and is the one to be run next from the session's consumer group - `Queue head - waiting on service availability`: The parallel statement is queued since there are not enough parallel servers available for the service this session is running on. This session is the one to be run next from the session's service - `Queue head - waiting on PDB limit`: The parallel statement is queued due to the PDB limit and is the one to be run next from the session's PDB - `NULL`: The session currently does not involve a parallel execution |
| `CURRENT_LOGICAL_IOS` | `NUMBER` | Number of logical I/O requests by the session for the current SQL operation |
| `LOGICAL_IOS` | `NUMBER` | Total number of logical I/O requests in this session's lifetime |
| `CURRENT_ELAPSED_TIME` | `NUMBER` | Elapsed time of the session's current SQL operation |
| `ELAPSED_TIME` | `NUMBER` | Total elapsed time for all of this session's SQL operations in its lifetime |
| `LAST_ACTION` | `VARCHAR2(48)` | The most recent action that was taken on this SQL operation by Resource Manager. Its value is one of the following:  - `CANCEL_SQL` - `KILL_SESSION` - `LOG_ONLY` - `SWITCH TO <CG NAME>`  For the last value, \<CG NAME> is the name of the consumer group that the SQL operation was switched to. If the Resource Plan has since been changed then \<CG NAME> is the ID of the consumer group. |
| `LAST_ACTION_REASON` | `VARCHAR2(30)` | The reason for the most recent action that was taken on this SQL operation by Resource Manager. Its value is one of the following:  - `SWITCH_CPU_TIME` - `SWITCH_IO_REQS` - `SWITCH_IO_MBS` - `SWITCH_ELAPSED_TIME` - `SWITCH_IO_LOGICAL` |
| `LAST_ACTION_TIME` | `DATE` | The time of the most recent action that was taken on this SQL operation by Resource Manager |
| `CURRENT_PGA` | `NUMBER` | Amount of PGA memory (in bytes) used by the session for the current SQL operation |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |