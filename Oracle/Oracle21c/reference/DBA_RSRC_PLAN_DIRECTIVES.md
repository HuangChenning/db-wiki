---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_RSRC_PLAN_DIRECTIVES.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.311 DBA\_RSRC\_PLAN\_DIRECTIVES

`DBA_RSRC_PLAN_DIRECTIVES` displays information about all resource plan directives in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PLAN` | `VARCHAR2(128)` |  | Name of the plan to which the directive belongs |
| `GROUP_OR_SUBPLAN` | `VARCHAR2(128)` |  | Name of the consumer group or subplan referred to |
| `TYPE` | `VARCHAR2(14)` |  | Indicates whether `GROUP_OR_SUBPLAN` refers to a consumer group (`CONSUMER_GROUP`) or a plan (`PLAN`) |
| `CPU_P1` | `NUMBER` |  | This column is deprecated. Use the `MGMT_P1` column instead. |
| `CPU_P2` | `NUMBER` |  | This column is deprecated. Use the `MGMT_P2` column instead. |
| `CPU_P3` | `NUMBER` |  | This column is deprecated. Use the `MGMT_P3` column instead. |
| `CPU_P4` | `NUMBER` |  | This column is deprecated. Use the `MGMT_P4` column instead. |
| `CPU_P5` | `NUMBER` |  | This column is deprecated. Use the `MGMT_P5` column instead. |
| `CPU_P6` | `NUMBER` |  | This column is deprecated. Use the `MGMT_P6` column instead. |
| `CPU_P7` | `NUMBER` |  | This column is deprecated. Use the `MGMT_P7` column instead. |
| `CPU_P8` | `NUMBER` |  | This column is deprecated. Use the `MGMT_P8` column instead. |
| `MGMT_P1` | `NUMBER` |  | Resource allocation at level 1. For share-based plans, indicates the number of shares. |
| `MGMT_P2` | `NUMBER` |  | Resource allocation at level 2. |
| `MGMT_P3` | `NUMBER` |  | Resource allocation at level 3. |
| `MGMT_P4` | `NUMBER` |  | Resource allocation at level 4. |
| `MGMT_P5` | `NUMBER` |  | Resource allocation at level 5. |
| `MGMT_P6` | `NUMBER` |  | Resource allocation at level 6. |
| `MGMT_P7` | `NUMBER` |  | Resource allocation at level 7. |
| `MGMT_P8` | `NUMBER` |  | Resource allocation at level 8. |
| `ACTIVE_SESS_POOL_P1` | `NUMBER` |  | Maximum number of calls this consumer group can run concurrently |
| `QUEUEING_P1` | `NUMBER` |  | Timeout in seconds for waits in the Active Session Limit queue |
| `PARALLEL_TARGET_PERCENTAGE` | `NUMBER` |  | This column is deprecated. Use the `PARALLEL_SERVER_LIMIT` column instead. |
| `PARALLEL_DEGREE_LIMIT_P1` | `NUMBER` |  | Sessions in this consumer group are limited to this maximum degree of parallelism for all parallel operations |
| `SWITCH_GROUP` | `VARCHAR2(128)` |  | Group to switch to once the switch time is reached |
| `SWITCH_FOR_CALL` | `VARCHAR2(5)` |  | Indicates whether to switch back to the initial consumer group once the top call has completed (`TRUE`) or not (`FALSE`) |
| `SWITCH_TIME` | `NUMBER` |  | Amount of run time (in seconds) within a group before the session is automatically switched. As with other switch directives, if `SWITCH_FOR_CALL` is `TRUE`, the run time is accumulated from the start of a call. Otherwise, the run time is accumulated for the length of the session. |
| `SWITCH_IO_MEGABYTES` | `NUMBER` |  | The maximum megabytes of I/O within a group that will trigger the action specified by `SWITCH_GROUP`. As with other switch directives, if `SWITCH_FOR_CALL` is `TRUE`, the maximum megabytes of I/O is accumulated from the start of a call. Otherwise, the maximum megabytes of I/O is accumulated for the length of the session. |
| `SWITCH_IO_REQS` | `NUMBER` |  | The maximum I/O requests within a group that will trigger the action specified by `SWITCH_GROUP`. As with other switch directives, if `SWITCH_FOR_CALL` is `TRUE`, the maximum I/O requests is accumulated from the start of a call. Otherwise, the maximum I/O requests is accumulated for the length of the session. |
| `SWITCH_ESTIMATE` | `VARCHAR2(5)` |  | Indicates whether estimated execution time should be used for switch criteria (`TRUE`) or not (`FALSE`) |
| `MAX_EST_EXEC_TIME` | `NUMBER` |  | Maximum estimated execution time |
| `UNDO_POOL` | `NUMBER` |  | Undo pool size for the consumer group |
| `MAX_IDLE_TIME` | `NUMBER` |  | Maximum idle time for the session |
| `MAX_IDLE_BLOCKER_TIME` | `NUMBER` |  | Maximum idle time for the session when blocking other sessions |
| `MAX_UTILIZATION_LIMIT` | `NUMBER` |  | This column is deprecated. Use `UTILIZATION_LIMIT` instead. |
| `PARALLEL_QUEUE_TIMEOUT` | `NUMBER` |  | Time (in seconds) that a query can remain in the parallel statement queue for the consumer group before it is removed from the queue.  The `PQ_TIMEOUT_ACTION` directive in a Resource Manager plan can be used in conjunction with the `PARALLEL_QUEUE_TIMEOUT` directive to either cancel or run the removed query. If the `PQ_TIMEOUT_ACTION` directive is not specified, the default behavior is to cancel the query with `ORA-07454`. |
| `SWITCH_TIME_IN_CALL` | `NUMBER` |  | This column is deprecated. Specify the time in the `SWITCH_TIME` directive and set `SWITCH_FOR_CALL` to `TRUE`. |
| `SWITCH_IO_LOGICAL` | `NUMBER` |  | The number of logical I/Os that will trigger the action specified by `SWITCH_GROUP`. As with other switch directives, if `SWITCH_FOR_CALL` is `TRUE`, the number of logical I/Os is accumulated from the start of a call. Otherwise, the number of logical IOs is accumulated for the length of the session. |
| `SWITCH_ELAPSED_TIME` | `NUMBER` |  | The elapsed time that will trigger the action specified by `SWITCH_GROUP`. As with other switch directives, if `SWITCH_FOR_CALL` is `TRUE`, the elapsed time is accumulated from the start of a call. Otherwise, the elapsed time is accumulated for the length of the session. |
| `PARALLEL_SERVER_LIMIT` | `NUMBER` |  | Maximum percentage of the parallel target used before queuing subsequent parallel queries |
| `UTILIZATION_LIMIT` | `NUMBER` |  | Maximum resource utilization allowed, expressed in percentage |
| `PARALLEL_STMT_CRITICAL` | `VARCHAR2(12)` |  | Indicates whether parallel statements from this consumer group are eligible for queuing in the parallel statement queue:  - `BYPASS QUEUE` - Parallel statements in this consumer group are critical and should never be queued. - `QUEUE` - All parallel statements in this consumer group, irrespective of the `PARALLEL_DEGREE_POLICY` initialization parameter value, are eligible for being queued. - `FALSE` - Certain parallel statements are eligible for queuing, depending on the `PARALLEL_DEGREE_POLICY` initialization parameter value. This is the default. |
| `SESSION_PGA_LIMIT` | `NUMBER` |  | The maximum amount of untunable PGA in MB that sessions in this consumer group can allocate before being terminated |
| `PQ_TIMEOUT_ACTION` | `VARCHAR2(6)` |  | Indicates the action to be taken on a parallel query in the parallel queue when its queue time exceeds the limit set by the Resource Manager plan’s `PARALLEL_QUEUE_TIMEOUT` directive:  - `CANCEL` - The statement terminates with error ORA-07454 - `RUN` - The statement runs immediately, and may get downgraded if parallel servers are unavailable |