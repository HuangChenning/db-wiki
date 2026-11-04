---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TAB_PRIVS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.115 ALL\_TAB\_PRIVS

`ALL_TAB_PRIVS` describes the following types of grants:

- Object grants for which the current user is the object owner, grantor, or grantee
- Object grants for which an enabled role or `PUBLIC` is the grantee

Related Views

- `DBA_TAB_PRIVS` describes all object grants in the database.
- `USER_TAB_PRIVS` describes the object grants for which the current user is the object owner, grantor, or grantee.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTOR` | `VARCHAR2(128)` |  | Name of the user who performed the grant |
| `GRANTEE` | `VARCHAR2(128)` |  | Name of the user or role to whom access was granted |
| `TABLE_SCHEMA` | `VARCHAR2(128)` |  | Schema of the object |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the object |
| `PRIVILEGE` | `VARCHAR2(40)` |  | Privilege on the object |
| `GRANTABLE` | `VARCHAR2(3)` |  | Indicates whether the privilege was granted with the `GRANT OPTION` (`YES`) or not (`NO`) |
| `HIERARCHY` | `VARCHAR2(3)` |  | Indicates whether the privilege was granted with the `HIERARCHY OPTION` (`YES`) or not (`NO`) |
| `COMMON` | `VARCHAR2(3)` |  | Indicates how the grant was made. Possible values:  - `YES` if the privilege was granted commonly (`CONTAINER=ALL` was used) - `NO` if the privilege was granted locally (`CONTAINER=ALL` was not used) |
| `TYPE` | `VARCHAR2(24)` |  | Type of the object |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the privilege grant was inherited from another container (`YES`) or not (`NO`) |

See Also:

- " [DBA\_TAB\_PRIVS](DBA_TAB_PRIVS.md) "
- " [USER\_TAB\_PRIVS](USER_TAB_PRIVS.md) "