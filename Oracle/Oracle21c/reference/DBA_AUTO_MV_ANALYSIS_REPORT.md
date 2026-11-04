---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTO_MV_ANALYSIS_REPORT.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.182 DBA\_AUTO\_MV\_ANALYSIS\_REPORT

`DBA_AUTO_MV_ANALYSIS_REPORT` reports on analyses and recommendations associated with automatic materialized views.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task  The value of this column is always `SYS_AUTO_MV_TASK`. |
| `EXECUTION_NAME` | `VARCHAR2(128)` |  | The name of the task execution with which this entry (row) is associated |
| `SEQUENCE` | `NUMBER` | `NOT NULL` | Sequence number of the journal entry (unique for each task). This sequence number is used to order the data. |
| `MESSAGE` | `VARCHAR2(4000)` |  | Entry in the journal |

Note:

This view is available starting with Oracle Database 21c.