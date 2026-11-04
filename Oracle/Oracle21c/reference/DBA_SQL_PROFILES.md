---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SQL_PROFILES.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.369 DBA\_SQL\_PROFILES

`DBA_SQL_PROFILES` displays information about SQL profiles currently created for specific SQL statements.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the SQL profile |
| `CATEGORY` | `VARCHAR2(128)` | `NOT NULL` | Category of the SQL profile |
| `SIGNATURE` | `NUMBER` | `NOT NULL` | Unique identifier generated from normalized SQL text |
| `SQL_TEXT` | `CLOB` | `NOT NULL` | Un-normalized SQL text |
| `CREATED` | `TIMESTAMP(6)` | `NOT NULL` | Timestamp when the SQL profile was created |
| `LAST_MODIFIED` | `TIMESTAMP(6)` |  | Timestamp when the SQL profile was last modified |
| `DESCRIPTION` | `VARCHAR2(500)` |  | Text description provided for the SQL profile |
| `TYPE` | `VARCHAR2(7)` |  | Type of the SQL profile (how it was created):  - `MANUAL` - `AUTO` |
| `STATUS` | `VARCHAR2(8)` |  | Status of the SQL profile:  - `ENABLED` - `DISABLED` - `VOID` |
| `FORCE_MATCHING` | `VARCHAR2(3)` |  | If `YES`, this causes SQL Profiles to target all SQL statements which have the same text after normalizing all literal values to bind variables. If a combination of literal values and bind variables is used in the same SQL text, then no transformation occurs. This is analogous to the matching algorithm use by the `FORCE` option of the `CURSOR_SHARING` parameter.  If `NO`, literals are not transformed. This is analogous to the matching algorithm used by the `EXACT` option of the `CURSOR_SHARING` parameter. |
| `TASK_ID` | `NUMBER` |  | Advisor task ID that generated the SQL profile |
| `TASK_EXEC_NAME` | `VARCHAR2(128)` |  | Advisor execution name for the SQL profile |
| `TASK_OBJ_ID` | `NUMBER` |  | Advisor object ID for the SQL profile |
| `TASK_FND_ID` | `NUMBER` |  | Advisor finding ID for the SQL profile |
| `TASK_REC_ID` | `NUMBER` |  | Advisor recommendation ID for the SQL profile |
| `TASK_CON_DBID` | `NUMBER` |  | Database ID for the PDB tuning task generating the SQL profile |

See Also:

The `DBMS_SQLTUNE` package in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS220)