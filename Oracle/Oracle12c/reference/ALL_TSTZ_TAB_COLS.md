---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_TSTZ_TAB_COLS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_TSTZ_TAB_COLS` displays information about the columns of the tables accessible to the current user, which have columns defined on `TIMESTAMP WITH TIME ZONE` data types or object types containing attributes of `TIMESTAMP WITH TIME ZONE` data types.

Related Views

- `DBA_TSTZ_TAB_COLS` displays information about the columns of all tables in the database, which have columns defined on `TIMESTAMP WITH TIME ZONE` data types or object types containing attributes of `TIMESTAMP WITH TIME ZONE` data types. This view does not display the `COLUMN_NAME`, `NESTED`, and `VIRTUAL_COLUMN` columns.
- `USER_TSTZ_TAB_COLS` displays information about the columns of the tables owned by the current user, which have columns defined on `TIMESTAMP WITH TIME ZONE` data types or object types containing attributes of `TIMESTAMP WITH TIME ZONE` data types. This view does not display the `OWNER`, `COLUMN_NAME`, `NESTED`, and `VIRTUAL_COLUMN` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Column name |
| `QUALIFIED_COL_NAME` | `VARCHAR2(4000)` |  | Qualified column name |
| `NESTED` | `NUMBER` |  | Indicates whether the column is a nested table (`1`) or not (`0`) |
| `VIRTUAL_COLUMN` | `NUMBER` |  | Indicates whether the column is a virtual column (`1`) or not (`0`) |
| `SCALAR_COLUMN` | `NUMBER` |  | Indicates whether the column is a scalar column (`1`) or not (`0`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `UNUSED_COLUMN` | `NUMBER` |  | Indicates whether the column is an unused column (`1`) or not (`0`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |

See Also:

- " [DBA\_TSTZ\_TAB\_COLS](DBA_TSTZ_TAB_COLS.md) "
- " [USER\_TSTZ\_TAB\_COLS](USER_TSTZ_TAB_COLS.md) "