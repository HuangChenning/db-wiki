---
title: ALL_CONS_OBJ_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1046.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CONS_OBJ_COLUMNS` displays information about the types that object columns (or attributes) or collection elements have been constrained to, in the tables accessible to the current user.

Related Views

- `DBA_CONS_OBJ_COLUMNS` displays information about the types that object columns (or attributes) or collection elements have been constrained to, in all tables in the database.
- `USER_CONS_OBJ_COLUMNS` displays information about the types that object columns (or attributes) or collection elements have been constrained to, in the tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table containing the object column or attribute |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Fully qualified name of the object column or attribute |
| `CONS_TYPE_OWNER` | `VARCHAR2(30)` |  | Owner of the type that the column (or element) is constrained to |
| `CONS_TYPE_NAME` | `VARCHAR2(30)` |  | Name of the type that the column (or element) is constrained to |
| `CONS_TYPE_ONLY` | `VARCHAR2(15)` |  | Indicates whether the column (or element) is constrained to `ONLY` type (`Y`) or not (`N`) |

See Also:

- ["DBA\_CONS\_OBJ\_COLUMNS"](statviews_3119.md)
- ["USER\_CONS\_OBJ\_COLUMNS"](statviews_5258.md)