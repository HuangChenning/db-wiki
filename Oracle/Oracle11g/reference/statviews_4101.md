---
title: DBA_JOBS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4101.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_JOBS` describes all jobs in the database.

Related View

`USER_JOBS` describes the jobs owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOB` | `NUMBER` | `NOT NULL` | Identifier of job. Neither import/export nor repeated executions change this value. |
| `LOG_USER` | `VARCHAR2(30)` | `NOT NULL` | Login user when the job was submitted |
| `PRIV_USER` | `VARCHAR2(30)` | `NOT NULL` | User whose default privileges apply to this job |
| `SCHEMA_USER` | `VARCHAR2(30)` | `NOT NULL` | Default schema used to parse the job  For example, if the `SCHEMA_USER` is `SCOTT` and you submit the procedure `HIRE_EMP` as a job, the Oracle Database looks for `SCOTT`.`HIRE_EMP` |
| `LAST_DATE` | `DATE` |  | Date on which this job last successfully executed |
| `LAST_SEC` | `VARCHAR2(8)` |  | Same as `LAST_DATE`. This is when the last successful execution started. |
| `THIS_DATE` | `DATE` |  | Date that this job started executing (usually null if not executing) |
| `THIS_SEC` | `VARCHAR2(8)` |  | Same as `THIS_DATE`. This is when the last successful execution started. |
| `NEXT_DATE` | `DATE` | `NOT NULL` | Date that this job will next be executed |
| `NEXT_SEC` | `VARCHAR2(8)` |  | Same as `NEXT_DATE`. This is when the last successful execution started. |
| `TOTAL_TIME` | `NUMBER` |  | Total wall clock time spent by the system on this job (in seconds) since the first time this job executed. This value is cumulative. |
| `BROKEN` | `VARCHAR2(1)` |  | `Y`: no attempt is made to run this job  `N`: an attempt is made to run this job |
| `INTERVAL` | `VARCHAR2(200)` | `NOT NULL` | A date function, evaluated at the start of execution, becomes next `NEXT_DATE` |
| `FAILURES` | `NUMBER` |  | Number of times the job has started and failed since its last success |
| `WHAT` | `VARCHAR2(4000)` |  | Body of the anonymous PL/SQL block that the job executes |
| `NLS_ENV` | `VARCHAR2(4000)` |  | Session parameters describing the NLS environment of the job |
| `MISC_ENV` | `RAW(32)` |  | Other session parameters that apply to this job |
| `INSTANCE` | `NUMBER` |  | ID of the instance that can execute or is executing the job. The default is 0. |

See Also:

["USER\_JOBS"](statviews_5342.md)