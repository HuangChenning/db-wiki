---
title: DBA_AUTOTASK_JOB_HISTORY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3087.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_AUTOTASK_JOB_HISTORY` displays the history of automated maintenance task job runs. Jobs are added to this view after they finish executing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CLIENT_NAME` | `VARCHAR2(64)` |  | Name of the automated maintenance client |
| `WINDOW_NAME` | `VARCHAR2(65)` |  | Name of the maintenance window |
| `WINDOW_START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Start time of the maintenance window |
| `WINDOW_DURATION` | `INTERVAL DAY(9) TO SECOND(6)` |  | Duration of the maintenance window |
| `JOB_NAME` | `VARCHAR2(65)` |  | Name of the maintenance job |
| `JOB_STATUS` | `VARCHAR2(30)` |  | Status of the maintenance job |
| `JOB_START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Start time of the maintenance job |
| `JOB_DURATION` | `INTERVAL DAY(3) TO SECOND(0)` |  | Duration of the maintenance job |
| `JOB_ERROR` | `NUMBER` |  | Error code for the job (if any) |
| `JOB_INFO` | `VARCHAR2(4000)` |  | Additional information about the job |