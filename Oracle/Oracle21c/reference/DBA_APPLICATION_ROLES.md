---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_APPLICATION_ROLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.111 DBA\_APPLICATION\_ROLES

`DBA_APPLICATION_ROLES` describes all the roles that have authorization policy functions defined.

Related View

`USER_APPLICATION_ROLES` describes all the roles for the current user that have authorization policy functions defined.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROLE` | `VARCHAR2(128)` | `NOT NULL` | Name of the application role |
| `SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Schema of the authorized package |
| `PACKAGE` | `VARCHAR2(128)` | `NOT NULL` | Name of the authorized package |

See Also:

" [USER\_APPLICATION\_ROLES](USER_APPLICATION_ROLES.md) "