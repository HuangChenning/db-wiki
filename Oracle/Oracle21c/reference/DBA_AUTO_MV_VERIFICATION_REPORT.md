---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTO_MV_VERIFICATION_REPORT.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.187 DBA\_AUTO\_MV\_VERIFICATION\_REPORT

`DBA_AUTO_MV_VERIFICATION_REPORT` displays information about verifications associated with automatic materialized views.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `EXECUTION_NAME` | `VARCHAR2(128)` |  | The name of the task execution with which this entry (row) is associated |
| `MESSAGE` | `VARCHAR2(4000)` |  | Message associated with the inference |

Note:

This view is available starting with Oracle Database 21c.