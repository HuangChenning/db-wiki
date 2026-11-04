---
title: DBA_RSRC_MANAGER_SYSTEM_PRIVS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4227.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_RSRC_MANAGER_SYSTEM_PRIVS` displays information about all the users and roles that have been granted the `ADMINISTER_RESOURCE_MANAGER` system privilege, which is granted using the `DBMS_RESOURCE_MANAGER_PRIVS` package. This privilege is not granted through the `GRANT` SQL statement.

Related View

`USER_RSRC_MANAGER_SYSTEM_PRIVS` displays information about the users who are granted system privileges for the `DBMS_RESOURCE_MANAGER` package. This view does not display the `GRANTEE` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(30)` | `NOT NULL` | User or role receiving the grant |
| `PRIVILEGE` | `VARCHAR2(40)` | `NOT NULL` | Name of the system privilege |
| `ADMIN_OPTION` | `VARCHAR2(3)` |  | Indicates whether the grant was with the `ADMIN` option (`YES`) or not (`NO`) |

See Also:

- ["USER\_RSRC\_MANAGER\_SYSTEM\_PRIVS"](statviews_5418.md)
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for more information on consumer group privileges