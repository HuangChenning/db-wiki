---
title: DBA_ADVISOR_SQLA_REC_SUM
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3029.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_SQLA_REC_SUM` displays recommendation rollup information for all workload objects in the database after an Access Advisor analysis operation.

Related View

`USER_ADVISOR_SQLA_REC_SUM` displays recommendation rollup information for the workload objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` |  | Unique identifier of the task |
| `TASK_NAME` | `VARCHAR2(30)` |  | Name of the task |
| `REC_ID` | `NUMBER` |  | Identifier of the recommendation |
| `TOTAL_STMTS` | `NUMBER` |  | Total number of statements processed during analysis |
| `TOTAL_PRECOST` | `NUMBER` |  | Total cost of executing the statements in which the recommended object will be utilized, prior to the recommendations |
| `TOTAL_POSTCOST` | `NUMBER` |  | Total cost of executing the statements in which the recommended object will be utilized, after the recommendations have been implemented |

See Also:

["USER\_ADVISOR\_SQLA\_REC\_SUM"](statviews_5211.md)