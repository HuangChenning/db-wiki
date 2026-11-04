---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_APPLY_KEY_COLUMNS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_APPLY_KEY_COLUMNS` displays information about the substitute key columns for the tables accessible to the current user. Substitute key columns are set using the `DBMS_APPLY_ADM.SET_KEY_COLUMNS` procedure.

Related View

`DBA_APPLY_KEY_COLUMNS` displays information about the substitute key columns for all tables in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object on which substitute key columns are set |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object on which substitute key columns are set |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Column name of a column specified as a substitute key column |
| `APPLY_DATABASE_LINK` | `VARCHAR2(128)` |  | Database link to which changes are applied. If null, then changes are applied to the local database. |

See Also:

- " [DBA\_APPLY\_KEY\_COLUMNS](DBA_APPLY_KEY_COLUMNS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS315) for more information about the `DBMS_APPLY_ADM.SET_KEY_COLUMNS` procedure