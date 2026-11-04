---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-QMON_TASKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.151 V$QMON\_TASKS

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. The `CON_ID` value in this view is always 0. The rows pertain to the entire CDB or to the non-CDB. |