---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CONS_OBJ_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.139 ALL\_CONS\_OBJ\_COLUMNS

`ALL_CONS_OBJ_COLUMNS` displays information about the types that object columns (or attributes) or collection elements have been constrained to, in the tables accessible to the current user.

Related Views

- `DBA_CONS_OBJ_COLUMNS` displays information about the types that object columns (or attributes) or collection elements have been constrained to, in all tables in the database.
- `USER_CONS_OBJ_COLUMNS` displays information about the types that object columns (or attributes) or collection elements have been constrained to, in the tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table containing the object column or attribute |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Fully qualified name of the object column or attribute |
| `CONS_TYPE_OWNER` | `VARCHAR2(128)` |  | Owner of the type that the column (or element) is constrained to |
| `CONS_TYPE_NAME` | `VARCHAR2(128)` |  | Name of the type that the column (or element) is constrained to |
| `CONS_TYPE_ONLY` | `VARCHAR2(15)` |  | Indicates whether the column (or element) is constrained to `ONLY` type (`Y`) or not (`N`) |

See Also:

- " [DBA\_CONS\_OBJ\_COLUMNS](DBA_CONS_OBJ_COLUMNS.md) "
- " [USER\_CONS\_OBJ\_COLUMNS](USER_CONS_OBJ_COLUMNS.md) "