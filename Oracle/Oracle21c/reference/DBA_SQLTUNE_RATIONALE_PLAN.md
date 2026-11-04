---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SQLTUNE_RATIONALE_PLAN.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.382 DBA\_SQLTUNE\_RATIONALE\_PLAN

`DBA_SQLTUNE_RATIONALE_PLAN` displays the association between rationales and operations in the execution plan of all SQL statements in the database.

Related View

`USER_SQLTUNE_RATIONALE_PLAN` displays the association between rationales and operations in the execution plan of the SQL statements owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER(38)` | `NOT NULL` | Tuning task identifier |
| `EXECUTION_NAME` | `VARCHAR2(128)` | `NOT NULL` | The name of the task execution with which this entry (row) is associated |
| `RATIONALE_ID` | `NUMBER(38)` | `NOT NULL` | Rationale identifier |
| `OBJECT_ID` | `NUMBER(38)` | `NOT NULL` | Advisor framework object identifier |
| `OPERATION_ID` | `NUMBER(38)` | `NOT NULL` | Operation identifier |
| `PLAN_ATTRIBUTE` | `VARCHAR2(34)` |  | Type of the execution plan:  - `Original` - Original plan of the query - `Original with adjusted cost` - Same as `Original` but with adjusted cost - `Using SQL profile` - Plan with SQL profile applied - `Using new indices` - Plan with indexes applied |

See Also:

" [USER\_SQLTUNE\_RATIONALE\_PLAN](USER_SQLTUNE_RATIONALE_PLAN.md) "