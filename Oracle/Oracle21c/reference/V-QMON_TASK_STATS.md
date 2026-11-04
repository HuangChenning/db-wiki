---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-QMON_TASK_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.150 V$QMON\_TASK\_STATS

`V$QMON_TASK_STATS` displays information and statistics based on different queue monitor tasks in the system (spilling, time manager activity, and so on). There is one row per kind of task. The rows are deleted when the database (or instance in an Oracle RAC environment) restarts.

| Column | Datatype | Description |
| --- | --- | --- |
| `TASK_NAME` | `VARCHAR2(32)` | Name of the task |
| `TASK_TYPE` | `VARCHAR2(40)` | Type of the task |
| `LAST_CREATED_TASKNUM` | `NUMBER` | Unique task number last created for this task |
| `NUM_TASKS` | `NUMBER` | Number of tasks currently present |
| `TOTAL_TASK_RUN_TIME` | `NUMBER` | Cumulative task run time |
| `TOTAL_TASK_RUNS` | `NUMBER` | Cumulative task runs |
| `TOTAL_TASK_FAILURES` | `NUMBER` | Cumulative failures |
| `METRIC_TYPE` | `VARCHAR2(50)` | Type of metric gathered for this task type |
| `METRIC_VALUE` | `NUMBER` | Value of this metric |
| `LAST_FAILURE` | `VARCHAR2(32)` | Last failure encountered while executing this type of task |
| `LAST_FAILURE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when the last failure occurred |
| `LAST_FAILURE_TASKNUM` | `NUMBER` | Task number of the last failed task for this task |
| `REMARK` | `VARCHAR2(64)` | Remarks about the task |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. The `CON_ID` value in this view is always 0. The rows pertain to the entire CDB or to the non-CDB. |