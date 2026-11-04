---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTOTASK_TASK.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.202 DBA\_AUTOTASK\_TASK

`DBA_AUTOTASK_TASK` displays information about current and past automated maintenance tasks.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CLIENT_NAME` | `VARCHAR2(64)` |  | Name of the client |
| `TASK_NAME` | `VARCHAR2(64)` |  | Name of the task being performed |
| `TASK_TARGET_TYPE` | `VARCHAR2(64)` |  | Target type of the task |
| `TASK_TARGET_NAME` | `VARCHAR2(513)` | `NOT NULL` | Name of the target |
| `OPERATION_NAME` | `VARCHAR2(64)` |  | Operation performed on the object |
| `ATTRIBUTES` | `VARCHAR2(4000)` |  | Attributes of the task |
| `TASK_PRIORITY` | `NUMBER` |  | Task priority, relative to other tasks for this Client |
| `PRIORITY_OVERRIDE` | `NUMBER` |  | Task priority as overridden by the user |
| `STATUS` | `VARCHAR2(8)` |  | Status of the task:  - `DISABLED` - `DEFERRED` - `ENABLED` |
| `DEFERRED_WINDOW_NAME` | `VARCHAR2(65)` |  | Appropriate window for this task |
| `CURRENT_JOB_NAME` | `VARCHAR2(65)` |  | Name of the currently scheduled job, if any |
| `JOB_SCHEDULER_STATUS` | `VARCHAR2(15)` |  | Job status:  - `DISABLED` - `RETRY SCHEDULED` - `SCHEDULED` - `RUNNING` - `COMPLETED` - `BROKEN` - `FAILED` - `REMOTE` - `SUCCEEDED` - `CHAIN_STALLED` |
| `ESTIMATE_TYPE` | `VARCHAR2(7)` |  | Type of resource estimates applied:  - `DERIVED` - `FORCED` - `LOCKED` |
| `ESTIMATED_WEIGHT` | `NUMBER` |  | Task weight indicator |
| `ESTIMATED_DURATION` | `NUMBER` |  | Estimated elapsed time for the job (in seconds) |
| `ESTIMATED_CPU_TIME` | `NUMBER` |  | Estimated CPU time for the job (in seconds) |
| `ESTIMATED_TEMP` | `NUMBER` |  | Estimated temporary space usage for the job (in KB) |
| `ESTIMATED_DOP` | `NUMBER` |  | Estimated degree of parallelism for the job |
| `ESTIMATED_IO_RATE` | `NUMBER` |  | Estimated I/O utilization for the job (in KB per second) |
| `ESTIMATED_UNDO_RATE` | `NUMBER` |  | Estimated UNDO generation rate for the job (in KB per second) |
| `RETRY_COUNT` | `NUMBER` |  | Number of attempts to perform this task since the last successful attempt |
| `LAST_GOOD_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Timestamp of the last successful attempt to perform this task |
| `LAST_GOOD_PRIORITY` | `NUMBER` |  | Job priority of the last successful attempt to perform this task |
| `LAST_GOOD_DURATION` | `NUMBER` |  | Elapsed time (in seconds) of the last successful attempt to perform this task |
| `LAST_GOOD_CPU_TIME` | `NUMBER` |  | CPU time for the job (in seconds) of the last successful attempt to perform this task |
| `LAST_GOOD_TEMP` | `NUMBER` |  | Temporary space usage for the job (in KB) of the last successful attempt to perform this task |
| `LAST_GOOD_DOP` | `NUMBER` |  | Peak degree of parallelism for the job during the last successful attempt to perform this task |
| `LAST_GOOD_IO_RATE` | `NUMBER` |  | I/O utilization rate for the job (in KB per second) of the last successful attempt to perform this task |
| `LAST_GOOD_UNDO_RATE` | `NUMBER` |  | NDO generation rate (in KB per second) of the last successful attempt to perform this task |
| `LAST_GOOD_CPU_WAIT` | `NUMBER` |  | Resource Manager wait time (in seconds) of the last successful attempt to perform this task |
| `LAST_GOOD_IO_WAIT` | `NUMBER` |  | Resource Manager wait time (in seconds) of the last successful attempt to perform this task |
| `LAST_GOOD_UNDO_WAIT` | `NUMBER` |  | Resource Manager wait time (in seconds) of the last successful attempt to perform this task |
| `LAST_GOOD_TEMP_WAIT` | `NUMBER` |  | Resource Manager wait time (in seconds) of the last successful attempt to perform this task |
| `LAST_GOOD_CONCURRENCY` | `NUMBER` |  | Concurrency wait time (in seconds) of the last successful attempt to perform this task |
| `LAST_GOOD_CONTENTION` | `NUMBER` |  | Contention wait time (in seconds) of the last successful attempt to perform this task |
| `NEXT_TRY_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Next projected start time for the deferred maintenance window |
| `LAST_TRY_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time at which the task was last attempted |
| `LAST_TRY_PRIORITY` | `NUMBER` |  | Task priority at the time of the last attempt |
| `LAST_TRY_RESULT` | `VARCHAR2(36)` |  | Result code of the last execution of the task:  - `SUCCEEDED` - `FAILED` - `STOPPED BY USER ACTION` - `STOPPED AT END OF MAINTENANCE WINDOW` - `STOPPED AT INSTANCE SHUTDOWN` - `STOPPED` |
| `LAST_TRY_DURATION` | `NUMBER` |  | Elapsed time of the last run (in seconds) |
| `LAST_TRY_CPU_TIME` | `NUMBER` |  | CPU time during the last run (in seconds) |
| `LAST_TRY_TEMP` | `NUMBER` |  | Temporary space usage for the job (in KB) for the last run |
| `LAST_TRY_DOP` | `NUMBER` |  | Peak degree of parallelism for the job during the last run |
| `LAST_TRY_IO_RATE` | `NUMBER` |  | I/O rate during the last run (in seconds) |
| `LAST_TRY_UNDO_RATE` | `NUMBER` |  | UNDO generation rate during the last run (in seconds) |
| `LAST_TRY_CPU_WAIT` | `NUMBER` |  | Time spent waiting for CPU during the last run (in seconds) |
| `LAST_TRY_IO_WAIT` | `NUMBER` |  | Time spent waiting for I/O during the last run (in seconds) |
| `LAST_TRY_UNDO_WAIT` | `NUMBER` |  | Time spent waiting for UNDO during the last run (in seconds) |
| `LAST_TRY_TEMP_WAIT` | `NUMBER` |  | Time spent waiting for temporary space during the last run (in seconds) |
| `LAST_TRY_CONCURRENCY` | `NUMBER` |  | Concurrency wait time during the last run (in seconds) |
| `LAST_TRY_CONTENTION` | `NUMBER` |  | Contention wait time during the last run (in seconds) |
| `MEAN_GOOD_DURATION` | `NUMBER` |  | Average elapsed time for successful executions of this task (in seconds) |
| `MEAN_GOOD_CPU_TIME` | `NUMBER` |  | Average CPU time for successful executions of this task (in seconds) |
| `MEAN_GOOD_TEMP` | `NUMBER` |  | Average temporary space usage for successful executions of this task (in KB) |
| `MEAN_GOOD_DOP` | `NUMBER` |  | Average peak degree of parallelism for successful executions of this task |
| `MEAN_GOOD_IO` | `NUMBER` |  | Average I/O utilization for successful executions of this task (in KB per second) |
| `MEAN_GOOD_UNDO` | `NUMBER` |  | Average UNDO generation rate for this task (in KB per second) |
| `MEAN_GOOD_CPU_WAIT` | `NUMBER` |  | Average time waiting for CPU for successful executions of this task (in seconds) |
| `MEAN_GOOD_IO_WAIT` | `NUMBER` |  | Average time waiting for I/O for successful executions of this task (in seconds) |
| `MEAN_GOOD_UNDO_WAIT` | `NUMBER` |  | Average time waiting for UNDO for successful executions of this task (in seconds) |
| `MEAN_GOOD_TEMP_WAIT` | `NUMBER` |  | Average time waiting for temporary space for successful executions of this task (in seconds) |
| `MEAN_GOOD_CONCURRENCY` | `NUMBER` |  | Average concurrency wait time for successful executions of this task (in seconds) |
| `MEAN_GOOD_CONTENTION` | `NUMBER` |  | Average contention wait time for successful executions of this task (in seconds) |
| `INFO_FIELD_1` | `VARCHAR2(4000)` |  | Client-interpreted information |
| `INFO_FIELD_2` | `CLOB` |  | Client-interpreted information |
| `INFO_FIELD_3` | `NUMBER` |  | Client-interpreted information |
| `INFO_FIELD_4` | `NUMBER` |  | Client-interpreted information |