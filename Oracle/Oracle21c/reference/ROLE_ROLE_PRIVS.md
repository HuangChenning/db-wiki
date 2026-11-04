---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ROLE_ROLE_PRIVS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.237 ROLE\_ROLE\_PRIVS

`ROLE_ROLE_PRIVS` describes the roles granted to other roles.

Information is provided only about roles to which the user has access.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROLE` | `VARCHAR2(128)` |  | Name of the role |
| `GRANTED_ROLE` | `VARCHAR2(128)` |  | Role that was granted |
| `ADMIN_OPTION` | `VARCHAR2(3)` |  | Signifies that the role was granted with `ADMIN` option |
| `COMMON` | `VARCHAR2(3)` |  | Indicates how the grant was made. Possible values:  - `YES` if the role was granted commonly (`CONTAINER=ALL` was used) - `NO` if the role was granted locally (`CONTAINER=ALL` was not used) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the role grant was inherited from another container (`YES`) or not (`NO`) |