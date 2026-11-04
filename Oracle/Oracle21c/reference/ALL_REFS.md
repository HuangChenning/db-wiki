---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_REFS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.27 ALL\_REFS

`ALL_REFS` describes the `REF` columns and `REF` attributes in object type columns accessible to the current user.

Related Views

- `DBA_REFS` describes all `REF` columns and `REF` attributes in the database.
- `USER_REFS` describes the `REF` columns and `REF` attributes in object type columns owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the `REF` column or attribute. If it is not a top-level attribute, the value of `COLUMN_NAME` should be a path name starting with the column name. |
| `WITH_ROWID` | `VARCHAR2(3)` |  | Indicates whether the `REF` value is stored with `ROWID` (`YES`) or not (`NO`) |
| `IS_SCOPED` | `VARCHAR2(3)` |  | Indicates whether the `REF` column is scoped (`YES`) or not (`NO`) |
| `SCOPE_TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the scope table, if it exists and is accessible by the user |
| `SCOPE_TABLE_NAME` | `VARCHAR2(128)` |  | Name of the scope table, if it exists and is accessible by the user |
| `OBJECT_ID_TYPE` | `VARCHAR2(33)` |  | Indicates whether the object ID (OID) is `USER-DEFINED` or `SYSTEM GENERATED` |

See Also:

- " [DBA\_REFS](DBA_REFS.md) "
- " [USER\_REFS](USER_REFS.md) "