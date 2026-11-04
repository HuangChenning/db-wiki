---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTOTASK_CLIENT_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.194 DBA\_AUTOTASK\_CLIENT\_HISTORY

`DBA_AUTOTASK_CLIENT_HISTORY` displays per-window history of job execution counts for each automated maintenance task.

This information is viewable in the Job History page of Enterprise Manager.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CLIENT_NAME` | `VARCHAR2(64)` |  | Name of the client |
| `WINDOW_NAME` | `VARCHAR2(261)` |  | Name of the maintenance window |
| `WINDOW_START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Maintenance window start time |
| `WINDOW_DURATION` | `INTERVAL DAY(9) TO SECOND(6)` |  | Window duration (NULL for currently open window) |
| `JOBS_CREATED` | `NUMBER` |  | Number of jobs created on behalf of the client in this window |
| `JOBS_STARTED` | `NUMBER` |  | Number of jobs started on behalf of the client during the maintenance window |
| `JOBS_COMPLETED` | `NUMBER` |  | Number of jobs successfully completed on behalf of the client during the maintenance window |
| `WINDOW_END_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Window end time |