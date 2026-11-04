---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_OBJ_COLATTRS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.292 ALL\_OBJ\_COLATTRS

`ALL_OBJ_COLATTRS` describes object columns and attributes contained in the tables accessible to the current user.

Related Views

- `DBA_OBJ_COLATTRS` describes object columns and attributes contained in all tables in the database.
- `USER_OBJ_COLATTRS` describes object columns and attributes contained in the tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table containing the object column or attribute |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Fully qualified name of the object column or attribute |
| `SUBSTITUTABLE` | `VARCHAR2(15)` |  | Indicates whether the column is substitutable (`Y`) or not (`N`) |

See Also:

- " [DBA\_OBJ\_COLATTRS](DBA_OBJ_COLATTRS.md) "
- " [USER\_OBJ\_COLATTRS](USER_OBJ_COLATTRS.md) "