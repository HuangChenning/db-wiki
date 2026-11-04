---
title: ALL_SQLSET_BINDS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2071.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SQLSET_BINDS` displays the bind values associated with all SQL tuning sets accessible to the current user.

Related Views

- `DBA_SQLSET_BINDS` displays the bind values associated with all SQL tuning sets in the database.
- `USER_SQLSET_BINDS` displays the bind values associated with the SQL tuning sets owned by the current user. This view does not display the `SQLSET_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SQLSET_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the SQL tuning set for the statement |
| `SQLSET_OWNER` | `VARCHAR2(30)` |  | User name of the SQL tuning set owner |
| `SQLSET_ID` | `NUMBER` | `NOT NULL` | ID of the SQL tuning set for the statement |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL identifier of the parent cursor in the library cache |
| `FORCE_MATCHING_SIGNATURE` | `NUMBER` | `NOT NULL` | The signature used when the `CURSOR_SHARING` parameter is set to `FORCE` |
| `PLAN_HASH_VALUE` | `NUMBER` | `NOT NULL` | Numerical representation of the SQL plan for the cursor. Comparing one `PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line-by-line). |
| `POSITION` | `NUMBER` | `NOT NULL` | Position |
| `VALUE` | `ANYDATA` |  | Value |
| `CAPTURED` | `CHAR(1)` |  | Binds captured |
| `SQL_SEQ` | `NUMBER` | `NOT NULL` | SQL sequence |