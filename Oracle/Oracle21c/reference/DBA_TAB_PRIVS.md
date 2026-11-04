---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_TAB_PRIVS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.41 DBA\_TAB\_PRIVS

`DBA_TAB_PRIVS` describes all object grants in the database.

Related View

`USER_TAB_PRIVS` describes the object grants for which the current user is the object owner, grantor, or grantee.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(128)` |  | Name of the user or role to whom access was granted |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the object. The object can be any object, including tables, packages, indexes, sequences, and so on. |
| `GRANTOR` | `VARCHAR2(128)` |  | Name of the user who performed the grant |
| `PRIVILEGE` | `VARCHAR2(40)` |  | Privilege on the object |
| `GRANTABLE` | `VARCHAR2(3)` |  | Indicates whether the privilege was granted with the `GRANT OPTION` (`YES`) or not (`NO`) |
| `HIERARCHY` | `VARCHAR2(3)` |  | Indicates whether the privilege was granted with the `HIERARCHY OPTION` (`YES`) or not (`NO`) |
| `COMMON` | `VARCHAR2(3)` |  | Indicates how the grant was made. Possible values:  - `YES` if the privilege was granted commonly (`CONTAINER=ALL` was used) - `NO` if the privilege was granted locally (`CONTAINER=ALL` was not used) |
| `TYPE` | `VARCHAR2(24)` |  | Type of the object |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the grant was inherited from another container (`YES`) or not (`NO`) |

See Also:

" [USER\_TAB\_PRIVS](USER_TAB_PRIVS.md) "