---
title: DBA_JOBS_RUNNING
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4102.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_JOBS_RUNNING` lists all jobs that are currently running in the instance.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SID` | `NUMBER` |  | Identifier of process that is executing the job. See ["V$LOCK"](dynviews_2027.md). |
| `JOB` | `NUMBER` |  | Identifier of job. This job is currently executing. |
| `FAILURES` | `NUMBER` |  | Number of times this job started and failed since its last success. |
| `LAST_DATE` | `DATE` |  | Date that this job last successfully executed. |
| `LAST_SEC` | `VARCHAR2(8)` |  | Same as `LAST_DATE`. This is when the last successful execution started. |
| `THIS_DATE` | `DATE` |  | Date that this job started executing. |
| `THIS_SEC` | `VARCHAR2(8)` |  | Same as `THIS_DATE`. This is when the last successful execution started. |
| `INSTANCE` | `NUMBER` |  | Indicates which instance can execute or is executing the job; the default is `0`. |