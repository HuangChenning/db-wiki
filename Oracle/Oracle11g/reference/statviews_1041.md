---
title: ALL_COL_PRIVS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1041.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_COL_PRIVS` describes the following types of grants:

- Column object grants for which the current user is the object owner, grantor, or grantee
- Column object grants for which an enabled role or `PUBLIC` is the grantee

Related Views

- `DBA_COL_PRIVS` describes all column object grants in the database.
- `USER_COL_PRIVS` describes the column object grants for which the current user is the object owner, grantor, or grantee.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTOR` | `VARCHAR2(30)` | `NOT NULL` | Name of the user who performed the grant |
| `GRANTEE` | `VARCHAR2(30)` | `NOT NULL` | Name of the user or role to whom access was granted |
| `TABLE_SCHEMA` | `VARCHAR2(30)` | `NOT NULL` | Schema of the object |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the column |
| `PRIVILEGE` | `VARCHAR2(40)` | `NOT NULL` | Privilege on the column |
| `GRANTABLE` | `VARCHAR2(3)` |  | Indicates whether the privilege was granted with the `GRANT OPTION` (`YES`) or not (`NO`) |

See Also:

- ["DBA\_COL\_PRIVS"](statviews_3110.md)
- ["USER\_COL\_PRIVS"](statviews_5248.md)