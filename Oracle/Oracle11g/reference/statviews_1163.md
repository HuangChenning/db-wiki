---
title: ALL_OPERATOR_COMMENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1163.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_OPERATOR_COMMENTS` displays comments for the user-defined operators accessible to the current user.

Related Views

- `DBA_OPERATOR_COMMENTS` displays comments for all user-defined operators in the database.
- `USER_OPERATOR_COMMENTS` displays comments for the user-defined operators owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the user-defined operator |
| `OPERATOR_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the user-defined operator |
| `COMMENTS` | `VARCHAR2(4000)` |  | Comment for the user-defined operator |

See Also:

- ["DBA\_OPERATOR\_COMMENTS"](statviews_4163.md)
- ["USER\_OPERATOR\_COMMENTS"](statviews_5381.md)