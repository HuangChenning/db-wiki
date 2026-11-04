---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_ROLE_PRIVS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.638 USER\_ROLE\_PRIVS

`USER_ROLE_PRIVS` describes the roles granted to the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(128)` |  | Name of the user, or `PUBLIC` |
| `GRANTED_ROLE` | `VARCHAR2(128)` |  | Name of the role granted to the user |
| `ADMIN_OPTION` | `VARCHAR2(3)` |  | Indicates whether the grant was with the `ADMIN OPTION` (`YES`) or not (`NO`) |
| `DELEGATE_OPTION` | `VARCHAR2(3)` |  | Indicates whether the grant was with the `DELEGATE OPTION` (`YES`) or not (`NO`) |
| `DEFAULT_ROLE ` | `VARCHAR2(3)` |  | Indicates whether the role is designated as a `DEFAULT ROLE` for the user (`YES`) or not (`NO`) |
| `OS_GRANTED` | `VARCHAR2(3)` |  | Indicates whether the role was granted by the operating system (`YES`) or not (`NO`); occurs if the `OS_ROLES` initialization parameter is `true` |
| `COMMON` | `VARCHAR2(3)` |  | Indicates how the grant was made. Possible values:  - `YES` if the role was granted commonly (`CONTAINER=ALL` was used) - `NO` if the role was granted locally (`CONTAINER=ALL` was not used) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the grant was inherited from another container (`YES`) or not (`NO`) |

See Also:

" [DBA\_ROLE\_PRIVS](DBA_ROLE_PRIVS.md) "