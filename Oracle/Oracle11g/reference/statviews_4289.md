---
title: DBA_SQLTUNE_RATIONALE_PLAN
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4289.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SQLTUNE_RATIONALE_PLAN` displays the association between rationales and operations in the execution plan of all SQL statements in the database.

Related View

`USER_SQLTUNE_RATIONALE_PLAN` displays the association between rationales and operations in the execution plan of the SQL statements owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER(38)` | `NOT NULL` | Tuning task identifier |
| `EXECUTION_NAME` | `VARCHAR2(30)` | `NOT NULL` | The name of the task execution with which this entry (row) is associated |
| `RATIONALE_ID` | `NUMBER(38)` | `NOT NULL` | Rationale identifier |
| `OBJECT_ID` | `NUMBER(38)` | `NOT NULL` | Advisor framework object identifier |
| `OPERATION_ID` | `NUMBER(38)` | `NOT NULL` | Operation identifier |
| `PLAN_ATTRIBUTE` | `VARCHAR2(27)` |  | Type of the execution plan: - `Original` - Original plan of the query - `Original with adjusted cost` - Same as `Original` but with adjusted cost - `Using SQL profile` - Plan with SQL profile applied - `Using new indices` - Plan with indexes applied |

See Also:

["USER\_SQLTUNE\_RATIONALE\_PLAN"](statviews_5460.md)