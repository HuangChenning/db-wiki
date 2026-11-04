---
title: ALL_TYPE_VERSIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2126.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TYPE_VERSIONS` describes the versions of the object types accessible to the current user.

Related Views

- `DBA_TYPE_VERSIONS` describes the versions of all object types in the database.
- `USER_TYPE_VERSIONS` describes the versions of the object types owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the type |
| `TYPE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the type |
| `VERSION#` | `NUMBER` | `NOT NULL` | Internal version number of the type |
| `TYPECODE` | `VARCHAR2(30)` |  | Typecode of the type |
| `STATUS` | `VARCHAR2(7)` |  | Status of the type: |
| `LINE` | `NUMBER` | `NOT NULL` | Line number of the type's spec |
| `TEXT` | `VARCHAR2(4000)` |  | Text of the type's spec |
| `HASHCODE` | `RAW(17)` |  | Hashcode of the type |

See Also:

- ["DBA\_TYPE\_VERSIONS"](statviews_5076.md)
- ["USER\_TYPE\_VERSIONS"](statviews_5502.md)