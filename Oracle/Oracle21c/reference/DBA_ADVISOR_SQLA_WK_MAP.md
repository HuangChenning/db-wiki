---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_SQLA_WK_MAP.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.40 DBA\_ADVISOR\_SQLA\_WK\_MAP

`DBA_ADVISOR_SQLA_WK_MAP` displays the workload references for all tasks in the database.

Workload references are necessary to allow the SQL Access Advisor to find required workload data.

Related View

`USER_ADVISOR_SQLA_WK_MAP` displays the workload references for the tasks owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` |  | Unique identifier of the task |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `WORKLOAD_ID` | `NUMBER` |  | Unique identifier of the workload object |
| `WORKLOAD_NAME` | `VARCHAR2(128)` |  | Name of the workload |
| `IS_STS` | `NUMBER` |  | Type of workload source:  - `0` - SQL workload object - `1` - SQL Tuning Set |

See Also:

" [USER\_ADVISOR\_SQLA\_WK\_MAP](USER_ADVISOR_SQLA_WK_MAP.md) "