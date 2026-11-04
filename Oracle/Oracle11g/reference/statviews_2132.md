---
title: ALL_VARRAYS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2132.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_VARRAYS` describes the varrays accessible to the current user.

Related Views

- `DBA_VARRAYS` describes all varrays in the database.
- `USER_VARRAYS` describes the varrays owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the table containing the varray |
| `PARENT_TABLE_NAME` | `VARCHAR2(30)` |  | Name of the containing table |
| `PARENT_TABLE_COLUMN` | `VARCHAR2(4000)` |  | Name of the varray column or attribute |
| `TYPE_OWNER` | `VARCHAR2(30)` |  | Owner of the varray type |
| `TYPE_NAME` | `VARCHAR2(30)` |  | Name of the varray type |
| `LOB_NAME` | `VARCHAR2(30)` |  | Name of the LOB if the varray is stored in a LOB |
| `STORAGE_SPEC` | `VARCHAR2(30)` |  | Indicates whether the storage was defaulted (`DEFAULT`) or user-specified (`USER_SPECIFIED`) |
| `RETURN_TYPE` | `VARCHAR2(20)` |  | Return type of the column: |
| `ELEMENT_SUBSTITUTABLE` | `VARCHAR2(25)` |  | Indicates whether the varray element is substitutable (`Y`) or not (`N`) |

See Also:

- ["DBA\_VARRAYS"](statviews_5084.md)
- ["USER\_VARRAYS"](statviews_5508.md)