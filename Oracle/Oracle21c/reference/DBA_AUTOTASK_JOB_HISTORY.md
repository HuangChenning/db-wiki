---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTOTASK_JOB_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.196 DBA\_AUTOTASK\_JOB\_HISTORY

`DBA_AUTOTASK_JOB_HISTORY` displays the history of automated maintenance task job runs. Jobs are added to this view after they finish executing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CLIENT_NAME` | `VARCHAR2(64)` |  | Name of the automated maintenance client |
| `WINDOW_NAME` | `VARCHAR2(261)` |  | Name of the maintenance window |
| `WINDOW_START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Start time of the maintenance window |
| `WINDOW_DURATION` | `INTERVAL DAY(9) TO SECOND(6)` |  | Duration of the maintenance window |
| `JOB_NAME` | `VARCHAR2(261)` |  | Name of the maintenance job |
| `JOB_STATUS` | `VARCHAR2(30)` |  | Status of the maintenance job |
| `JOB_START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Start time of the maintenance job |
| `JOB_DURATION` | `INTERVAL DAY(3) TO SECOND(0)` |  | Duration of the maintenance job |
| `JOB_ERROR` | `NUMBER` |  | Error code for the job (if any) |
| `JOB_INFO` | `VARCHAR2(4000)` |  | Additional information about the job |