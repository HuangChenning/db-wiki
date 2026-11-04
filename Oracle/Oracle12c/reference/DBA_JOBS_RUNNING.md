---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_JOBS_RUNNING.html
tags:
  - oracle
  - 12c
  - reference
---

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