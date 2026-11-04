---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTOTASK_SCHEDULE_CONTROL.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.199 DBA\_AUTOTASK\_SCHEDULE\_CONTROL

`DBA_AUTOTASK_SCHEDULE_CONTROL` displays the status of automated tasks.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Identifier of the database used by the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Identifier of the task |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the task |
| `TASK_NAME` | `VARCHAR2(64)` |  | Name of the task |
| `STATUS` | `VARCHAR2(10)` |  | Status of the task  Possible values:  - `FAILED` - `RUNNING` - `SCHEDULED` - `SKIPPED` - `SUCCEEDED` - `TERMINATED` |
| `ELAPSED_TIME` | `NUMBER` |  | Elapsed time of the last execution (in seconds) |
| `LAST_SCHEDULE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` |  | Last time the task was scheduled to execute |
| `LAST_EXEC_INSTNUM` | `NUMBER` |  | Oracle RAC instance number for the database instance used for the last execution of the task |