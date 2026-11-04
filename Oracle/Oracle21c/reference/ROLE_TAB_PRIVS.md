---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ROLE_TAB_PRIVS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.239 ROLE\_TAB\_PRIVS

`ROLE_TAB_PRIVS` describes table privileges granted to roles. Information is provided only about roles to which the user has access.

Note:

When a user with the `SYSDBA` privilege queries this view, information is provided only about roles to which the user has been explicitly granted access. To view information about all roles, a user with the `SYSDBA` privilege can query the [DBA\_TAB\_PRIVS](DBA_TAB_PRIVS.md) view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROLE` | `VARCHAR2(128)` |  | Name of the role |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the object |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of the column, if applicable |
| `PRIVILEGE` | `VARCHAR2(40)` |  | Object privilege granted to the role |
| `GRANTABLE` | `VARCHAR2(3)` |  | `YES` if the role was granted with `ADMIN OPTION`; otherwise `NO` |
| `COMMON` | `VARCHAR2(3)` |  | Indicates how the grant was made. Possible values:  - `YES` if the privilege was granted commonly (`CONTAINER=ALL` was used) - `NO` if the privilege was granted locally (`CONTAINER=ALL` was not used) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the role grant was inherited from another container (`YES`) or not (`NO`) |