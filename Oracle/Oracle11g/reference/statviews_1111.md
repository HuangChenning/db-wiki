---
title: ALL_INDEXTYPE_COMMENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1111.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_INDEXTYPE_COMMENTS` displays comments for the user-defined indextypes accessible to the current user.

Related Views

- `DBA_INDEXTYPE_COMMENTS` displays comments for all user-defined indextypes in the database.
- `USER_INDEXTYPE_COMMENTS` displays comments for the user-defined indextypes owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the user-defined indextype |
| `INDEXTYPE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the user-defined indextype |
| `COMMENTS` | `VARCHAR2(4000)` |  | Comment for the user-defined indextype |

See Also:

- ["DBA\_INDEXTYPE\_COMMENTS"](statviews_4083.md)
- ["USER\_INDEXTYPE\_COMMENTS"](statviews_5325.md)