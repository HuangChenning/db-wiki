---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_VARRAYS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.139 ALL\_VARRAYS

`ALL_VARRAYS` describes the varrays accessible to the current user.

Related Views

- `DBA_VARRAYS` describes all varrays in the database.
- `USER_VARRAYS` describes the varrays owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table containing the varray |
| `PARENT_TABLE_NAME` | `VARCHAR2(128)` |  | Name of the containing table |
| `PARENT_TABLE_COLUMN` | `VARCHAR2(4000)` |  | Name of the varray column or attribute |
| `TYPE_OWNER` | `VARCHAR2(128)` |  | Owner of the varray type |
| `TYPE_NAME` | `VARCHAR2(128)` |  | Name of the varray type |
| `LOB_NAME` | `VARCHAR2(128)` |  | Name of the LOB if the varray is stored in a LOB |
| `STORAGE_SPEC` | `VARCHAR2(30)` |  | Indicates whether the storage was defaulted (`DEFAULT`) or user-specified (`USER_SPECIFIED`) |
| `RETURN_TYPE` | `VARCHAR2(20)` |  | Return type of the column:  - `LOCATOR` - `VALUE` |
| `ELEMENT_SUBSTITUTABLE` | `VARCHAR2(25)` |  | Indicates whether the varray element is substitutable (`Y`) or not (`N`) |

See Also:

- " [DBA\_VARRAYS](DBA_VARRAYS.md) "
- " [USER\_VARRAYS](USER_VARRAYS.md) "