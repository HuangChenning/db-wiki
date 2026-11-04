---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_JOBS_RUNNING.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.136 DBA\_JOBS\_RUNNING

`DBA_JOBS_RUNNING` lists all jobs that are currently running in the instance.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SID` | `NUMBER` |  | Identifier of process that is executing the job. See " [V$LOCK](V-LOCK.md) ". |
| `JOB ` | `NUMBER` |  | Identifier of job. This job is currently executing. |
| `FAILURES ` | `NUMBER` |  | Number of times this job started and failed since its last success. |
| `LAST_DATE` | `DATE` |  | Date that this job last successfully executed. |
| `LAST_SEC ` | `VARCHAR2(8)` |  | Same as `LAST_DATE`. This is when the last successful execution started. |
| `THIS_DATE ` | `DATE` |  | Date that this job started executing. |
| `THIS_SEC ` | `VARCHAR2(8)` |  | Same as `THIS_DATE`. This is when the last successful execution started. |
| `INSTANCE` | `NUMBER` |  | Indicates which instance can execute or is executing the job; the default is `0`. |