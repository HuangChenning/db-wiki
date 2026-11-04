---
title: ALL_LIBRARIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1129.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_LIBRARIES` describes the libraries accessible to the current user.

Related Views

- `DBA_LIBRARIES` describes all libraries in the database.
- `USER_LIBRARIES` describes the libraries owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the library |
| `LIBRARY_NAME` | `VARCHAR2(30)` | `NOT NULL` | Library name |
| `FILE_SPEC` | `VARCHAR2(2000)` |  | Operating system file specification associated with the library |
| `DYNAMIC` | `VARCHAR2(1)` |  | Indicates whether the library is dynamically loadable (`Y`) or not (`N`) |
| `STATUS` | `VARCHAR2(7)` |  | Status of the library: |

See Also:

- ["DBA\_LIBRARIES"](statviews_4105.md)
- ["USER\_LIBRARIES"](statviews_5344.md)