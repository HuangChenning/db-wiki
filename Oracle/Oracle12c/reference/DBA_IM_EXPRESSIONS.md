---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_IM_EXPRESSIONS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_IM_EXPRESSIONS` provides information about the list of expressions (SYS\_IME virtual columns) that are currently enabled for in-memory storage.

Related View

Typically, you can query this view after invoking the `DBMS_INMEMORY_ADMIN.IME_CAPTURE_EXPRESSIONS` PL/SQL procedure to see the list of hot expressions added to different tables across the database.

Based on this view, you can:

- Populate expressions on a particular table immediately
- Drop certain expressions that are marked for in-memory but not desired by users

`USER_IM_EXPRESSIONS` provides information about the list of expressions (SYS\_IME virtual columns) that are currently enabled for in-memory storage in schemas owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(129)` |  | Table owner |
| `TABLE_NAME` | `VARCHAR2(129)` |  | Table name |
| `OBJECT_NUMBER` | `NUMBER` |  | Object number of the table |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Column name of the expression added to the table (with SYS\_IME prefix) |
| `SQL_EXPRESSION` | `LONG` |  | SQL representation of the expression |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).