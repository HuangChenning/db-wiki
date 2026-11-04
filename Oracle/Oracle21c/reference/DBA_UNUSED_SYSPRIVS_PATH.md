---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_UNUSED_SYSPRIVS_PATH.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.86 DBA\_UNUSED\_SYSPRIVS\_PATH

`DBA_UNUSED_SYSPRIVS_PATH` lists the system privileges that are not used for the privilege analysis policies reported by the `DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT` procedure.

This view provides access to analyzed privilege records in `SYS` tables.

You must have the `CAPTURE_ADMIN` role to access this view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE` | `VARCHAR2(128)` | `NOT NULL` | Name of a privilege analysis policy |
| `USERNAME` | `VARCHAR2(128)` |  | Name of the user whose privileges are reported |
| `ROLENAME` | `VARCHAR2(128)` |  | Name of the role whose unused privileges are reported (for `ROLE` type privilege analysis or `ROLE AND CONTEXT` privilege analysis) |
| `SYS_PRIV` | `VARCHAR2(40)` |  | Unused system privilege |
| `ADMIN_OPTION` | `NUMBER` |  | Indicates whether the privilege is granted with the `ADMIN` option:  - `0` - Indicates that the privilege is granted without the `ADMIN` option - `1` - Indicates that the privilege is granted with the `ADMIN` option |
| `PATH` | `GRANT_PATH` |  | System privilege grant paths |
| `RUN_NAME` | `VARCHAR2(128)` |  | The name of the run during which the privilege was reported |