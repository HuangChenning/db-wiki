---
title: ALL_COL_COMMENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1039.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_COL_COMMENTS` displays comments on the columns of the tables and views accessible to the current user.

Related Views

- `DBA_COL_COMMENTS` displays comments on the columns of all tables and views in the database.
- `USER_COL_COMMENTS` displays comments on the columns of the tables and views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the column |
| `COMMENTS` | `VARCHAR2(4000)` |  | Comment on the column |

See Also:

- ["DBA\_COL\_COMMENTS"](statviews_3108.md)
- ["USER\_COL\_COMMENTS"](statviews_5246.md)