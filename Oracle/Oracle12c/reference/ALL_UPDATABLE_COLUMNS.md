---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_UPDATABLE_COLUMNS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_UPDATABLE_COLUMNS` describes all columns in a join view that are updatable by the current user, subject to appropriate privileges.

Related Views

- `DBA_UPDATABLE_COLUMNS` describes all columns in a join view that are updatable by the database administrator, subject to appropriate privileges.
- `USER_UPDATABLE_COLUMNS` describes all columns owned by the current user that are in a join view and are updatable by the current user, subject to appropriate privileges.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Column name |
| `UPDATABLE` | `VARCHAR2(3)` |  | Indicates whether the column is updatable (`YES`) or not (`NO`) |
| `INSERTABLE ` | `VARCHAR2(3)` |  | Indicates whether the column is insertable (`YES`) or not (`NO`) |
| `DELETABLE` | `VARCHAR2(3)` |  | Indicates whether the column is deletable (`YES`) or not (`NO`) |

See Also:

- " [DBA\_UPDATABLE\_COLUMNS](DBA_UPDATABLE_COLUMNS.md) "
- " [USER\_UPDATABLE\_COLUMNS](USER_UPDATABLE_COLUMNS.md) "
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT1151) for information on updatable join views