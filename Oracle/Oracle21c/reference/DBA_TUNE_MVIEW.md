---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_TUNE_MVIEW.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.70 DBA\_TUNE\_MVIEW

`DBA_TUNE_MVIEW` displays the result of executing the `DBMS_ADVISOR.TUNE_MVIEW` procedure.

Related View

`USER_TUNE_MVIEW` displays the result of executing the `DBMS_ADVISOR.TUNE_MVIEW` procedure. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `ACTION_ID` | `NUMBER` | `NOT NULL` | Identifier of the action |
| `SCRIPT_TYPE` | `VARCHAR2(14)` |  | Type of the script:  - `IMPLEMENTATION` - `UNDO` |
| `STATEMENT` | `CLOB` |  | Action statement |

See Also:

- " [USER\_TUNE\_MVIEW](USER_TUNE_MVIEW.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS65157) for more information about the `DBMS_ADVISOR.TUNE_MVIEW` procedure