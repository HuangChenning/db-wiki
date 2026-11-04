---
title: SCHEDULER_BATCH_ERRORS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5173.htm
tags:
  - oracle
  - 11g
  - reference
---

`SCHEDULER_BATCH_ERRORS` displays the errors caused by each call in the batch after a Scheduler batch call (when the `COMMIT_SEMANTICS` argument has been set to `ABSORB_ERRORS`).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ARRAY_INDEX` | `NUMBER` |  | Index of the job in the batch |
| `OBJECT_TYPE` | `VARCHAR2(30)` |  | Object type: |
| `OBJECT_NAME` | `VARCHAR2(100)` |  | Full name of the object (including schema) |
| `ATTR_NAME` | `VARCHAR2(30)` |  | Name of the attribute being set (if this is a batch set attribute call); NULL otherwise |
| `ERROR_CODE` | `NUMBER` |  | Top level error code |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Complete error stack |
| `ADDITIONAL_INFO` | `VARCHAR2(4000)` |  | Additional information (currently unused) |