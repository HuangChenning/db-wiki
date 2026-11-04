---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_CHECKED_ROLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.221 DBA\_CHECKED\_ROLES

`DBA_CHECKED_ROLES` lists the roles (without role grant paths) that are used for the role analysis policies reported by the `DBMS__CAPTURE.GENERATE_RESULT` procedure.

This view provides access to analyzed role records in `SYS` tables.

You must have the `CAPTURE_ADMIN` role to access this view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE` | `VARCHAR2(128)` | `NOT NULL` | Name of a role analysis policy |
| `SEQUENCE` | `NUMBER` | `NOT NULL` | The sequence number of the role analysis run during which the role was reported |
| `OS_USER` | `VARCHAR2(128)` |  | Operating system login username |
| `USERHOST` | `VARCHAR2(128)` |  | Client host machine name |
| `MODULE` | `VARCHAR2(64)` |  | Module name |
| `USERNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the user whose role was reported |
| `CHECKED_ROLE` | `VARCHAR2(128)` |  | Checked role |
| `RUN_NAME` | `VARCHAR2(128)` |  | The name of the run during which the role was reported |

See Also:

" [DBA\_CHECKED\_ROLES\_PATH](DBA_CHECKED_ROLES_PATH.md) "