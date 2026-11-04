---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_UNUSED_PRIVS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.84 DBA\_UNUSED\_PRIVS

`DBA_UNUSED_PRIVS` lists the privileges that are not used for the privilege analysis policies reported by the `DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT` procedure.

This view provides access to analyzed privilege records in `SYS` tables.

You must have the `CAPTURE_ADMIN` role to access this view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE` | `VARCHAR2(128)` | `NOT NULL` | Name of the privilege analysis policy |
| `USERNAME` | `VARCHAR2(128)` |  | Name of the user whose unused privileges are reported |
| `ROLENAME` | `VARCHAR2(128)` |  | Name of the role whose unused privileges are reported (for `ROLE` type privilege analysis or `ROLE AND CONTEXT` privilege analysis) |
| `SYS_PRIV` | `VARCHAR2(40)` |  | Unused system privilege |
| `OBJ_PRIV` | `VARCHAR2(40)` |  | Unused object privilege |
| `USER_PRIV` | `VARCHAR2(25)` |  | Unused user privilege |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Object owner |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the object that `USERNAME` has `OBJ_PRIV` or `USER_PRIV` on |
| `OBJECT_TYPE` | `VARCHAR2(23)` |  | Type of the object that `OBJ_PRIV` has accessed or `USER` if `USER_PRIV` was used |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of the column that `OBJ_PRIV` has access on |
| `OPTION$` | `NUMBER` |  | Indicates whether the privilege is granted with the `GRANT` option or the `ADMIN` option:  - `0` - Indicates that the privilege is granted without the `GRANT` option or `ADMIN` option - `1` - Indicates that the privilege is granted with the `GRANT` option or `ADMIN` option |
| `PATH` | `GRANT_PATH` |  | Privilege grant paths |
| `RUN_NAME` | `VARCHAR2(128)` |  | The name of the run during which the privilege was reported |

See Also:

- " [DBA\_USED\_PRIVS](DBA_USED_PRIVS.md) "
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG-GUID-44CB644B-7B59-4B3B-B375-9F9B96F60186) for more information about privilege analysis
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS74345) for more information about the `DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT` procedure