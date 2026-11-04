---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_INDEXTYPE_ARRAYTYPES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.237 ALL\_INDEXTYPE\_ARRAYTYPES

`ALL_INDEXTYPE_ARRAYTYPES` displays information about the array types specified by the indextypes accessible to the current user.

Related Views

- `DBA_INDEXTYPE_ARRAYTYPES` displays information about the array types specified by all indextypes in the database.
- `USER_INDEXTYPE_ARRAYTYPES` displays information about the array types specified by the indextypes owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the indextype |
| `INDEXTYPE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the indextype |
| `BASE_TYPE_SCHEMA` | `VARCHAR2(128)` |  | Name of the base type schema |
| `BASE_TYPE_NAME` | `VARCHAR2(128)` |  | Name of the base type name |
| `BASE_TYPE` | `VARCHAR2(30)` |  | Datatype of the base type |
| `ARRAY_TYPE_SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Name of the array type schema |
| `ARRAY_TYPE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the array type name |

See Also:

- " [DBA\_INDEXTYPE\_ARRAYTYPES](DBA_INDEXTYPE_ARRAYTYPES.md) "
- " [USER\_INDEXTYPE\_ARRAYTYPES](USER_INDEXTYPE_ARRAYTYPES.md) "