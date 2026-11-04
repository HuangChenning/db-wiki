---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/SCHEDULER_BATCH_ERRORS.html
tags:
  - oracle
  - 12c
  - reference
---

`SCHEDULER_BATCH_ERRORS` displays the errors caused by each call in the batch after a Scheduler batch call (when the `COMMIT_SEMANTICS` argument has been set to `ABSORB_ERRORS`).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ARRAY_INDEX` | `NUMBER` |  | Index of the job in the batch |
| `OBJECT_TYPE` | `VARCHAR2(30)` |  | Object type:  - `JOB` - `LIGHTWEIGHT JOB` - `UNKNOWN` |
| `OBJECT_NAME` | `VARCHAR2(100)` |  | Full name of the object (including schema) |
| `ATTR_NAME` | `VARCHAR2(30)` |  | Name of the attribute being set (if this is a batch set attribute call); NULL otherwise |
| `ERROR_CODE` | `NUMBER` |  | Top level error code |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Complete error stack |
| `ADDITIONAL_INFO` | `VARCHAR2(4000)` |  | Additional information (currently unused) |