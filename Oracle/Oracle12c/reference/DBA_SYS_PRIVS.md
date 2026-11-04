---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_SYS_PRIVS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_SYS_PRIVS` describes system privileges granted to users and roles.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(128)` |  | Grantee name, user, or role receiving the grant |
| `PRIVILEGE` | `VARCHAR2(40)` |  | System privilege |
| `ADMIN_OPTION` | `VARCHAR2(3)` |  | Indicates whether the grant was with the `ADMIN` option (`YES`) or not (`NO`) |
| `COMMON` | `VARCHAR2(3)` |  | Indicates how the grant was made. Possible values:  - `YES` if the privilege was granted commonly (`CONTAINER=ALL` was used) - `NO` if the privilege was granted locally (`CONTAINER=ALL` was not used) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the grant was inherited from another container (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |

See Also:

" [USER\_SYS\_PRIVS](USER_SYS_PRIVS.md) "