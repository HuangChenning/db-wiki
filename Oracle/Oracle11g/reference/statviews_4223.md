---
title: DBA_RSRC_CONSUMER_GROUP_PRIVS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4223.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_RSRC_CONSUMER_GROUP_PRIVS` displays information about all resource consumer groups and the users and roles assigned to them. The grant referred to in this view and the related view is the grant of the `SWITCH_CONSUMER_GROUP` object privilege, which is granted using the `DBMS_RESOURCE_MANAGER_PRIVS` package. This privilege is not granted through the `GRANT` SQL statement.

Related View

`USER_RSRC_CONSUMER_GROUP_PRIVS` displays information about the resource consumer groups to which the current user is assigned. This view does not display the `GRANTEE` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(30)` | `NOT NULL` | User or role receiving the grant |
| `GRANTED_GROUP` | `VARCHAR2(30)` |  | Granted consumer group name |
| `GRANT_OPTION` | `VARCHAR2(3)` |  | Indicates whether the grant was with the `GRANT` option (`YES`) or not (`NO`) |
| `INITIAL_GROUP` | `VARCHAR2(3)` |  | Indicates whether the consumer group is designated as the default for this user or role (`YES`) or not (`NO`) |

See Also:

- ["USER\_RSRC\_CONSUMER\_GROUP\_PRIVS"](statviews_5417.md)
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for more information on consumer group privileges