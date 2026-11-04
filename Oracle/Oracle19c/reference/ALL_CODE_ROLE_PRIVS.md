---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_CODE_ROLE_PRIVS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.123 ALL\_CODE\_ROLE\_PRIVS

`ALL_CODE_ROLE_PRIVS` describes all the roles that are associated with program units owned or accessible by the current user.

Related Views

- `DBA_CODE_ROLE_PRIVS` describes all the roles that are associated with program units in the database.
- `USER_CODE_ROLE_PRIVS` describes all the roles that are associated with program units owned by current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Username of the owner of the object |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `OBJECT_TYPE` | `VARCHAR2(9)` |  | Type of the object |
| `ROLE` | `VARCHAR2(128)` | `NOT NULL` | The role associated with the object |

See Also:

- " [DBA\_CODE\_ROLE\_PRIVS](DBA_CODE_ROLE_PRIVS.md) "
- " [USER\_CODE\_ROLE\_PRIVS](USER_CODE_ROLE_PRIVS.md) "
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=DBSEG782) for more information about granting and revoking roles to and from program units