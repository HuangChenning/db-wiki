---
title: DBA_ADVISOR_SQLA_WK_MAP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3031.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_SQLA_WK_MAP` displays the workload references for all tasks in the database. Workload references are necessary to allow the SQL Access Advisor to find required workload data.

Related View

`USER_ADVISOR_SQLA_WK_MAP` displays the workload references for the tasks owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` |  | Unique identifier of the task |
| `TASK_NAME` | `VARCHAR2(30)` |  | Name of the task |
| `WORKLOAD_ID` | `NUMBER` |  | Unique identifier of the workload object |
| `WORKLOAD_NAME` | `VARCHAR2(30)` |  | Name of the workload |
| `IS_STS` | `NUMBER` |  | Type of workload source: |

See Also:

["USER\_ADVISOR\_SQLA\_WK\_MAP"](statviews_5213.md)