---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WI_JOBS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.109 DBA\_WI\_JOBS

Each row in `DBA_WI_JOBS ` describes a Workload Intelligence job, that is, a task that applies the algorithms of Workload Intelligence on a given capture directory.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOB_ID` | `NUMBER` | `NOT NULL` | The job identifier |
| `JOB_NAME` | `VARCHAR2(128)` | `NOT NULL` | A name that uniquely identifies the given job |
| `CAPTURE_DIRECTORY` | `VARCHAR2(4000)` | `NOT NULL` | Path to the capture directory on which the given job has been applied |
| `MODEL_ORDER` | `NUMBER` |  | The order of the markov model that describes the workload associated with the current job. If `NULL`, the corresponding order has not been calculated yet. |
| `THRESHOLD` | `NUMBER` |  | A number in the range \[0, 1\] that represents the threshold that the user has given as an input parameter to the current job of Workload Intelligence for the identification of significant patterns. If `NULL`, the process of pattern identification has not been initiated yet. |