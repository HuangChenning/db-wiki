---
title: ALL_COL_PRIVS_MADE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1042.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_COL_PRIVS_MADE` describes the column object grants for which the current user is the object owner or grantor.

Related View

`USER_COL_PRIVS_MADE` describes the column object grants for which the current user is the object owner. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(30)` | `NOT NULL` | Name of the user or role to whom access was granted |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the column |
| `GRANTOR` | `VARCHAR2(30)` | `NOT NULL` | Name of the user who performed the grant |
| `PRIVILEGE` | `VARCHAR2(40)` | `NOT NULL` | Privilege on the column |
| `GRANTABLE` | `VARCHAR2(3)` |  | Indicates whether the privilege was granted with the `GRANT OPTION` (`YES`) or not (`NO`) |

See Also:

["USER\_COL\_PRIVS\_MADE"](statviews_5249.md)