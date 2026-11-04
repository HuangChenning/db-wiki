---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_RSRC_MANAGER_SYSTEM_PRIVS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.309 DBA\_RSRC\_MANAGER\_SYSTEM\_PRIVS

`DBA_RSRC_MANAGER_SYSTEM_PRIVS` displays information about all the users and roles that have been granted the `ADMINISTER_RESOURCE_MANAGER` system privilege, which is granted using the `DBMS_RESOURCE_MANAGER_PRIVS` package.

This privilege is not granted through the `GRANT` SQL statement.

Related View

`USER_RSRC_MANAGER_SYSTEM_PRIVS` displays information about the users who are granted system privileges for the `DBMS_RESOURCE_MANAGER` package. This view does not display the `GRANTEE` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(128)` | `NOT NULL` | User or role receiving the grant |
| `PRIVILEGE` | `VARCHAR2(40)` | `NOT NULL` | Name of the system privilege |
| `ADMIN_OPTION` | `VARCHAR2(3)` |  | Indicates whether the grant was with the `ADMIN` option (`YES`) or not (`NO`) |

See Also:

- " [USER\_RSRC\_MANAGER\_SYSTEM\_PRIVS](USER_RSRC_MANAGER_SYSTEM_PRIVS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS050) for more information about the `DBMS_RESOURCE_MANAGER` package