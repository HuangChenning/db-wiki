---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_SYS_PRIVS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.708 USER\_SYS\_PRIVS

`USER_SYS_PRIVS` describes system privileges granted to the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(128)` |  | Name of the user, or `PUBLIC` |
| `PRIVILEGE` | `VARCHAR2(40)` |  | System privilege |
| `ADMIN_OPTION` | `VARCHAR2(3)` |  | Indicates whether the grant was with the `ADMIN` option (`YES`) or not (`NO`) |
| `COMMON` | `VARCHAR2(3)` |  | Indicates how the grant was made. Possible values:  - `YES` if the privilege was granted commonly (`CONTAINER=ALL` was used) - `NO` if the privilege was granted locally (`CONTAINER=ALL` was not used) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the grant was inherited from another container (`YES`) or not (`NO`) |

See Also:

" [DBA\_SYS\_PRIVS](DBA_SYS_PRIVS.md) "