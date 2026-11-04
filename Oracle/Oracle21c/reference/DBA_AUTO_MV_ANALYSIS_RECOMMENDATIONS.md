---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTO_MV_ANALYSIS_RECOMMENDATIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.181 DBA\_AUTO\_MV\_ANALYSIS\_RECOMMENDATIONS

`DBA_AUTO_MV_ANALYSIS_RECOMMENDATIONS` displays recommendations associated with automatic materialized views.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task  The value of this column is always `SYS_AUTO_MV_TASK`. |
| `EXECUTION_NAME` | `VARCHAR2(128)` | `NOT NULL` | The name of the task execution with which this entry (row) is associated |
| `RECOMMENDATIONS` | `CLOB` |  | Recommendation for the task |

Note:

This view is available starting with Oracle Database 21c.