---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_JOBS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.135 DBA\_JOBS

`DBA_JOBS` describes all jobs in the database.

Related View

`USER_JOBS` describes the jobs owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOB ` | `NUMBER` | `NOT NULL` | Identifier of job. Neither import/export nor repeated executions change this value. |
| `LOG_USER ` | `VARCHAR2(128)` | `NOT NULL` | Login user when the job was submitted |
| `PRIV_USER` | `VARCHAR2(128)` | `NOT NULL` | User whose default privileges apply to this job |
| `SCHEMA_USER ` | `VARCHAR2(128)` | `NOT NULL` | Default schema used to parse the job  For example, if the `SCHEMA_USER` is `SCOTT` and you submit the procedure `HIRE_EMP` as a job, the Oracle Database looks for `SCOTT`.`HIRE_EMP` |
| `LAST_DATE` | `DATE` |  | Date on which this job last successfully executed |
| `LAST_SEC ` | `VARCHAR2(8)` |  | Same as `LAST_DATE`. This is when the last successful execution started. |
| `THIS_DATE ` | `DATE` |  | Date that this job started executing (usually null if not executing) |
| `THIS_SEC` | `VARCHAR2(8)` |  | Same as `THIS_DATE`. This is when the last successful execution started. |
| `NEXT_DATE` | `DATE` | `NOT NULL` | Date that this job will next be executed |
| `NEXT_SEC ` | `VARCHAR2(8)` |  | Same as `NEXT_DATE`. The job becomes due for execution at this time. |
| `TOTAL_TIME ` | `NUMBER` |  | Total wall clock time spent by the system on this job (in seconds) when it last executed |
| `BROKEN` | `VARCHAR2(1)` |  | `Y`: no attempt is made to run this job  `N`: an attempt is made to run this job |
| `INTERVAL` | `VARCHAR2(200)` | `NOT NULL` | A date function, evaluated at the start of execution, becomes next `NEXT_DATE` |
| `FAILURES ` | `NUMBER` |  | Number of times the job has started and failed since its last success |
| `WHAT` | `VARCHAR2(4000)` |  | Body of the anonymous PL/SQL block that the job executes |
| `NLS_ENV` | `VARCHAR2(4000)` |  | Session parameters describing the NLS environment of the job |
| `MISC_ENV` | `RAW(32)` |  | Other session parameters of the session that created the job. The job is run using these parameters. |
| `INSTANCE` | `NUMBER` |  | ID of the instance that can execute or is executing the job. The default is 0. |

See Also:

" [USER\_JOBS](USER_JOBS.md) "