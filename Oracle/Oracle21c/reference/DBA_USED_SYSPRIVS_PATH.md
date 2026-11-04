---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_USED_SYSPRIVS_PATH.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.95 DBA\_USED\_SYSPRIVS\_PATH

`DBA_USED_SYSPRIVS_PATH` lists the system privileges that are used for the privilege analysis policies reported by the `DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT` procedure.

This view provides access to analyzed privilege records in `SYS` tables.

You must have the `CAPTURE_ADMIN` role to access this view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE` | `VARCHAR2(128)` | `NOT NULL` | Name of a privilege analysis policy |
| `SEQUENCE` | `NUMBER` | `NOT NULL` | The sequence number of the privilege analysis run during which the privilege was reported |
| `OS_USER` | `VARCHAR2(128)` |  | Operating system login username |
| `USERHOST` | `VARCHAR2(128)` |  | Client host machine name |
| `MODULE` | `VARCHAR2(64)` |  | Module name |
| `USERNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the user whose privilege was reported |
| `USED_ROLE` | `VARCHAR2(128)` |  | Used role |
| `SYS_PRIV` | `VARCHAR2(40)` |  | Used system privilege |
| `ADMIN_OPTION` | `NUMBER` |  | Indicates whether the `ADMIN` option was used:  - `0` - Indicates that the `ADMIN` option was not used - `1` - Indicates that the `ADMIN` option was used |
| `PATH` | `GRANT_PATH` |  | System privilege grant paths |
| `RUN_NAME` | `VARCHAR2(128)` |  | The name of the run during which the privilege was reported |