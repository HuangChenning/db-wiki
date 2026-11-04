---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_ADVISOR_SQLA_REC_SUM.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_ADVISOR_SQLA_REC_SUM` displays recommendation rollup information for all workload objects in the database after an Access Advisor analysis operation.

Related View

`USER_ADVISOR_SQLA_REC_SUM` displays recommendation rollup information for the workload objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` |  | Unique identifier of the task |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `REC_ID` | `NUMBER` |  | Identifier of the recommendation |
| `TOTAL_STMTS` | `NUMBER` |  | Total number of statements processed during analysis |
| `TOTAL_PRECOST` | `NUMBER` |  | Total cost of executing the statements in which the recommended object will be used, before the recommendations |
| `TOTAL_POSTCOST` | `NUMBER` |  | Total cost of executing the statements in which the recommended object will be utilized, after the recommendations have been implemented |

See Also:

" [USER\_ADVISOR\_SQLA\_REC\_SUM](USER_ADVISOR_SQLA_REC_SUM.md) "