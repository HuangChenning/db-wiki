---
title: "V$QMON_TASK_STATS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2119.htm
tags:
  - oracle
  - 11g
  - reference
---

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