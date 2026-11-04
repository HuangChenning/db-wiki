---
title: ALL_APPLY_KEY_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1012.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_APPLY_KEY_COLUMNS` displays information about the substitute key columns for the tables accessible to the current user. Substitute key columns are set using the `DBMS_APPLY_ADM.SET_KEY_COLUMNS` procedure.

Related View

`DBA_APPLY_KEY_COLUMNS` displays information about the substitute key columns for all tables in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object on which substitute key columns are set |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object on which substitute key columns are set |
| `COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Column name of a column specified as a substitute key column |
| `APPLY_DATABASE_LINK` | `VARCHAR2(128)` |  | Database link to which changes are applied. If null, then changes are applied to the local database. |

See Also:

["DBA\_APPLY\_KEY\_COLUMNS"](statviews_3058.md)