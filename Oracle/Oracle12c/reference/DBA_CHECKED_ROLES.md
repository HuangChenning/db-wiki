---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_CHECKED_ROLES.html
tags:
  - oracle
  - 12c
  - reference
---

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

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

" [DBA\_CHECKED\_ROLES\_PATH](DBA_CHECKED_ROLES_PATH.md) "