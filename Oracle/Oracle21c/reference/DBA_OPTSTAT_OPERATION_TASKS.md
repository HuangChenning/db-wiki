---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_OPTSTAT_OPERATION_TASKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.221 DBA\_OPTSTAT\_OPERATION\_TASKS

`DBA_OPTSTAT_OPERATION_TASKS` displays the history of tasks that are performed as part of statistics operations (recorded in `DBA_OPTSTAT_OPERATIONS`). Each task represents a target object to be processed in the corresponding parent operation.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OPID` | `NUMBER` |  | Internal identifier for the statistics operation that the task belongs to |
| `TARGET` | `VARCHAR2(100)` |  | Name of the object that this task operates on |
| `TARGET_OBJN` | `NUMBER` |  | Object number of the target object |
| `TARGET_TYPE` | `VARCHAR2(40)` |  | Type of the target object. Possible values are:  - `TABLE` - `TABLE (GLOBAL STATS ONLY)`: 	Task is created to gather only global statistics of a partitioned table - `TABLE (COORDINATOR JOB)`: 	Coordinator task for a partitioned table when concurrency is on - `TABLE PARTITION` - `TABLE SUBPARTITION` - `INDEX` - `INDEX PARTITION` - `INDEX SUBPARTITION` |
| `TARGET_SIZE` | `NUMBER` |  | Target size (in number of blocks) when the task started |
| `START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Task start time |
| `END_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Task end time |
| `STATUS` | `VARCHAR2(49)` |  | Current task status. Possible values are:  - `PENDING`: Task is queued for processing - `IN PROGRESS`: Task is currently running - `COMPLETED`: Task has completed successfully - `FAILED`: Task has failed - `SKIPPED`: Task has been skipped, as it does not exist any more, or its stats are not stale (applies only to only automatic statistics gathering) - `TIMED OUT`: Maintenance window was not enough to complete this task (applies only to automatic statistics gathering) |
| `JOB_NAME` | `VARCHAR2(50)` |  | Name of the scheduler job that executes this task (for example, when concurrency is on) |
| `ESTIMATED_COST` | `NUMBER` |  | Estimated cost of the task (measured as elapsed time in seconds). This column is populated only when concurrency is on. |
| `BATCHING_COEFF` | `NUMBER` |  | For internal use only |
| `ACTIONS` | `NUMBER` |  | For internal use only |
| `PRIORITY` | `NUMBER` |  | Rank of the task among all target objects for the parent operation |
| `FLAGS` | `NUMBER` |  | For internal use only |
| `NOTES` | `VARCHAR2(4000)` |  | Notes about the underlying task, such as the failure message for tasks with status `FAILED`. |

See Also:

" [DBA\_OPTSTAT\_OPERATIONS](DBA_OPTSTAT_OPERATIONS.md) "