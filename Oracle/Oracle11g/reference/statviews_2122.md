---
title: ALL_TSTZ_TAB_COLS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2122.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TSTZ_TAB_COLS` displays information about the columns of the tables accessible to the current user, which have columns defined on `TIMESTAMP WITH TIME ZONE` data types or object types containing attributes of `TIMESTAMP WITH TIME ZONE` data types.

Related Views

- `DBA_TSTZ_TAB_COLS` displays information about the columns of all tables in the database, which have columns defined on `TIMESTAMP WITH TIME ZONE` data types or object types containing attributes of `TIMESTAMP WITH TIME ZONE` data types. This view does not display the `COLUMN_NAME,` `NESTED`, and `VIRTUAL_COLUMN` columns.
- `USER_TSTZ_TAB_COLS` displays information about the columns of the tables owned by the current user, which have columns defined on `TIMESTAMP WITH TIME ZONE` data types or object types containing attributes of `TIMESTAMP WITH TIME ZONE` data types. This view does not display the `OWNER`, `COLUMN_NAME,` `NESTED`, or `VIRTUAL_COLUMN` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |
| `COLUMN_NAME` <sup>Foot 1</sup> | `VARCHAR2(30)` | `NOT NULL` | Column name |
| `QUALIFIED_COL_NAME` | `VARCHAR2(4000)` |  | Qualified column name |
| `NESTED` | `NUMBER` |  | Indicates whether the column is a nested table (`1`) or not (`0`) |
| `VIRTUAL_COLUMN` <sup>Footref 1</sup> | `NUMBER` |  | Identifies whether the column is a virtual column (`1`) or not (`0`) |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.4)

See Also:

- ["DBA\_TSTZ\_TAB\_COLS"](statviews_5071.md)
- ["USER\_TSTZ\_TAB\_COLS"](statviews_5497.md)