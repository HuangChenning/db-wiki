---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_NESTED_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.291 ALL\_NESTED\_TABLES

`ALL_NESTED_TABLES` describes the nested tables in tables accessible to the current user.

Related Views

- `DBA_NESTED_TABLES` describes all nested tables in the database.
- `USER_NESTED_TABLES` describes nested tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the nested table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the nested table |
| `TABLE_TYPE_OWNER` | `VARCHAR2(128)` |  | Owner of the type of which the nested table was created |
| `TABLE_TYPE_NAME` | `VARCHAR2(128)` |  | Name of the type of the nested table |
| `PARENT_TABLE_NAME` | `VARCHAR2(128)` |  | Name of the parent table containing the nested table |
| `PARENT_TABLE_COLUMN` | `VARCHAR2(4000)` |  | Column name of the parent table that corresponds to the nested table |
| `STORAGE_SPEC` | `VARCHAR2(30)` |  | Indicates whether storage for the nested table is `USER_SPECIFIED` or `DEFAULT` |
| `RETURN_TYPE` | `VARCHAR2(20)` |  | Return type of the varray column (`LOCATOR`) or (`VALUE`) |
| `ELEMENT_SUBSTITUTABLE` | `VARCHAR2(25)` |  | Indicates whether the nested table element is substitutable (`Y`) or not (`N`) |

See Also:

- " [DBA\_NESTED\_TABLES](DBA_NESTED_TABLES.md) "
- " [USER\_NESTED\_TABLES](USER_NESTED_TABLES.md) "