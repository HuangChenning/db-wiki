---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTO_STAT_EXECUTIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.191 DBA\_AUTO\_STAT\_EXECUTIONS

`DBA_AUTO_STAT_EXECUTIONS` displays information about automatic optimizer statistics collection tasks, which are executed by the automated maintenance tasks infrastructure (known as AutoTask).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OPID` | `NUMBER` |  | Unique identifier for the execution of the task |
| `ORIGIN` | `VARCHAR2(19)` |  | Origin of the execution of the task. Possible values: - `AUTO_TASK`: A standard automatic optimizer statistics collection task, which is executed automatically in an Oracle Scheduler window, known as maintenance window - `HIGH_FREQ_AUTO_TASK`: A high-frequency automatic optimizer statistics collection task, which is executed at frequent intervals and complements the standard automatic optimizer statistics collection tasks |
| `STATUS` | `VARCHAR2(49)` |  | Status of the execution of the task. Possible values: - `IN` `PROGRESS`: The operation is currently running - `COMPLETED`: The operation has completed successfully - `FAILED`: The operation has failed - `TIMED` `OUT`: The operation timed out because the time allocated for the maintenance window was not sufficient for the operation to complete |
| `START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Start time for the execution of the task |
| `END_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | End time for the execution of the task |
| `COMPLETED` | `NUMBER` |  | Number of objects for which statistics collection was completed during the execution of the task |
| `FAILED` | `NUMBER` |  | Number of objects for which statistics collection failed during the execution of the task |
| `TIMED_OUT` | `NUMBER` |  | Number of objects for which statistics collection timed out during the execution of the task |
| `IN_PROGRESS` | `NUMBER` |  | Number of objects for which statistics collection is in progress during the execution of the task |