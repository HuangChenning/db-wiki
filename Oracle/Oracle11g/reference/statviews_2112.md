---
title: ALL_TAB_PRIVS_RECD
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2112.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TAB_PRIVS_RECD` describes the following types of grants:

- Object grants for which the current user is the grantee
- Object grants for which an enabled role or `PUBLIC` is the grantee

Related View

`USER_TAB_PRIVS_RECD` describes the object grants for which the current user is the grantee. This view does not display the `GRANTEE` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(30)` | `NOT NULL` | Name of the user or role to whom access was granted |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `GRANTOR` | `VARCHAR2(30)` | `NOT NULL` | Name of the user who performed the grant |
| `PRIVILEGE` | `VARCHAR2(40)` | `NOT NULL` | Privilege on the object |
| `GRANTABLE` | `VARCHAR2(3)` |  | Indicates whether the privilege was granted with the `GRANT OPTION` (`YES`) or not (`NO`) |
| `HIERARCHY` | `VARCHAR2(3)` |  | Indicates whether the privilege was granted with the `HIERARCHY OPTION` (`YES`) or not (`NO`) |

See Also:

["USER\_TAB\_PRIVS\_RECD"](statviews_5485.md)