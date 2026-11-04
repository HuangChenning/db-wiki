---
title: ALL_USERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2130.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_USERS` lists all users of the database visible to the current user. This view does not describe the users (see the related views).

Related Views

- `DBA_USERS` describes all users of the database, and contains more columns than `ALL_USERS`.
- `USER_USERS` describes the current user, and contains more columns than `ALL_USERS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the user |
| `USER_ID` | `NUMBER` | `NOT NULL` | ID number of the user |
| `CREATED` | `DATE` | `NOT NULL` | User creation date |

See Also:

- ["DBA\_USERS"](statviews_5081.md)
- ["USER\_USERS"](statviews_5506.md)