---
title: ALL_OBJ_COLATTRS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1156.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_OBJ_COLATTRS` describes object columns and attributes contained in the tables accessible to the current user.

Related Views

- `DBA_OBJ_COLATTRS` describes object columns and attributes contained in all tables in the database.
- `USER_OBJ_COLATTRS` describes object columns and attributes contained in the tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table containing the object column or attribute |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Fully qualified name of the object column or attribute |
| `SUBSTITUTABLE` | `VARCHAR2(15)` |  | Indicates whether the column is substitutable (`Y`) or not (`N`) |

See Also:

- ["DBA\_OBJ\_COLATTRS"](statviews_4155.md)
- ["USER\_OBJ\_COLATTRS"](statviews_5373.md)