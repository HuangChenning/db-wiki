---
title: ALL_INDEXTYPE_ARRAYTYPES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1110.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_INDEXTYPE_ARRAYTYPES` displays information about the array types specified by the indextypes accessible to the current user.

Related Views

- `DBA_INDEXTYPE_ARRAYTYPES` displays information about the array types specified by all indextypes in the database.
- `USER_INDEXTYPE_ARRAYTYPES` displays information about the array types specified by the indextypes owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the indextype |
| `INDEXTYPE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the indextype |
| `BASE_TYPE_SCHEMA` | `VARCHAR2(30)` |  | Name of the base type schema |
| `BASE_TYPE_NAME` | `VARCHAR2(30)` |  | Name of the base type name |
| `BASE_TYPE` | `VARCHAR2(30)` |  | Datatype of the base type |
| `ARRAY_TYPE_SCHEMA` | `VARCHAR2(30)` | `NOT NULL` | Name of the array type schema |
| `ARRAY_TYPE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the array type name |

See Also:

- ["DBA\_INDEXTYPE\_ARRAYTYPES"](statviews_4082.md)
- ["USER\_INDEXTYPE\_ARRAYTYPES"](statviews_5324.md)