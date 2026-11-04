---
title: "V$QMON_TASKS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2120.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$QMON_TASKS` displays information and statistics about all queue background tasks in the system, which would be served by queue monitor servers. There is one row per task. The rows are deleted when the database (or instance in an Oracle RAC environment) restarts.

| Column | Datatype | Description |
| --- | --- | --- |
| `TASK_NAME` | `VARCHAR2(32)` | Task name |
| `TASK_NUMBER` | `NUMBER` | Unique task number |
| `TASK_TYPE` | `VARCHAR2(40)` | Task type |
| `TASK_SUBMIT_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Task submit time |
| `TASK_READY_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Task ready time |
| `TASK_EXPIRY_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when this task expires |
| `TASK_START_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Last actual start time for the task |
| `TASK_STATUS` | `VARCHAR2(32)` | Status of the task |
| `SERVER_NAME` | `VARCHAR2(48)` | Name of the QMON server running this task |
| `MAX_RETRIES` | `NUMBER` | Maximum retry count for the task |
| `NUM_RUNS` | `NUMBER` | Number of runs of the task if repeatable |
| `NUM_FAILURES` | `NUMBER` | Number of failures encountered while running the task |