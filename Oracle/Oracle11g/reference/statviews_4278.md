---
title: DBA_SQL_PROFILES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4278.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SQL_PROFILES` displays information about SQL profiles currently created for specific SQL statements.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the SQL profile |
| `CATEGORY` | `VARCHAR2(30)` | `NOT NULL` | Category of the SQL profile |
| `SIGNATURE` | `NUMBER` | `NOT NULL` | Unique identifier generated from normalized SQL text |
| `SQL_TEXT` | `CLOB` | `NOT NULL` | Un-normalized SQL text |
| `CREATED` | `DATE` | `NOT NULL` | Timestamp when the SQL profile was created |
| `LAST_MODIFIED` | `DATE` | `NOT NULL` | Timestamp when the SQL profile was last modified |
| `DESCRIPTION` | `VARCHAR2(500)` |  | Text description provided for the SQL profile |
| `TYPE` | `VARCHAR2(9)` |  | Type of the SQL profile (how it was created): - `MANUAL` - `AUTO` |
| `STATUS` | `VARCHAR2(8)` |  | Status of the SQL profile: - `ENABLED` - `DISABLED` - `VOID` |
| `FORCE_MATCHING` | `VARCHAR2(3)` |  | If `YES`, this causes SQL Profiles to target all SQL statements which have the same text after normalizing all literal values to bind variables. If a combination of literal values and bind variables is used in the same SQL text, then no transformation occurs. This is analogous to the matching algorithm use by the `FORCE` option of the `CURSOR_SHARING` parameter.  If `NO`, literals are not transformed. This is analogous to the matching algorithm used by the `EXACT` option of the `CURSOR_SHARING` parameter. |
| `TASK_ID` | `NUMBER` |  | Advisor task ID that generated the SQL profile |
| `EXECUTION_NAME` | `VARCHAR2(30)` |  | Advisor execution name for the SQL profile |
| `OBJECT_ID` | `NUMBER` |  | Advisor object ID for the SQL profile |
| `FINDING_ID` | `NUMBER` |  | Advisor finding ID for the SQL profile |
| `REC_ID` | `NUMBER` |  | Advisor recommendation ID for the SQL profile |

See Also:

The `DBMS_SQLTUNE` package in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm)