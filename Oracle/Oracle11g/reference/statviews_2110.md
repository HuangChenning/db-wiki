---
title: ALL_TAB_PRIVS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2110.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TAB_PRIVS` describes the following types of grants:

- Object grants for which the current user is the object owner, grantor, or grantee
- Object grants for which an enabled role or `PUBLIC` is the grantee

Related Views

- `DBA_TAB_PRIVS` describes all object grants in the database.
- `USER_TAB_PRIVS` describes the object grants for which the current user is the object owner, grantor, or grantee.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTOR` | `VARCHAR2(30)` | `NOT NULL` | Name of the user who performed the grant |
| `GRANTEE` | `VARCHAR2(30)` | `NOT NULL` | Name of the user or role to whom access was granted |
| `TABLE_SCHEMA` | `VARCHAR2(30)` | `NOT NULL` | Schema of the object |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `PRIVILEGE` | `VARCHAR2(40)` | `NOT NULL` | Privilege on the object |
| `GRANTABLE` | `VARCHAR2(3)` |  | Indicates whether the privilege was granted with the `GRANT OPTION` (`YES`) or not (`NO`) |
| `HIERARCHY` | `VARCHAR2(3)` |  | Indicates whether the privilege was granted with the `HIERARCHY OPTION` (`YES`) or not (`NO`) |

See Also:

- ["DBA\_TAB\_PRIVS"](statviews_5051.md)
- ["USER\_TAB\_PRIVS"](statviews_5483.md)