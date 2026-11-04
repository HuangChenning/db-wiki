---
title: DBA_ROLE_PRIVS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4219.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ROLE_PRIVS` describes the roles granted to all users and roles in the database.

Related View

`USER_ROLE_PRIVS` describes the roles granted to the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(30)` |  | Name of the user or role receiving the grant |
| `GRANTED_ROLE` | `VARCHAR2(30)` | `NOT NULL` | Granted role name |
| `ADMIN_OPTION` | `VARCHAR2(3)` |  | Indicates whether the grant was with the `ADMIN OPTION` (`YES`) or not (`NO`) |
| `DEFAULT_ROLE` | `VARCHAR2(3)` |  | Indicates whether the role is designated as a `DEFAULT ROLE` for the user (`YES`) or not (`NO`) |

See Also:

["USER\_ROLE\_PRIVS"](statviews_5416.md)