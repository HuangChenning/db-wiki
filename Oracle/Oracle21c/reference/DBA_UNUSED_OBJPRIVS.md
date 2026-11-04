---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_UNUSED_OBJPRIVS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.82 DBA\_UNUSED\_OBJPRIVS

`DBA_UNUSED_OBJPRIVS` lists the object privileges (without privilege grant paths) that are not used for the privilege analysis policies reported by the `DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT` procedure.

This view provides access to analyzed privilege records in `SYS` tables.

You must have the `CAPTURE_ADMIN` role to access this view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE` | `VARCHAR2(128)` | `NOT NULL` | Name of the privilege analysis policy |
| `USERNAME` | `VARCHAR2(128)` |  | Name of the user whose privileges are reported |
| `ROLENAME` | `VARCHAR2(128)` |  | Name of the role whose unused privileges are reported (for `ROLE` type privilege analysis or `ROLE AND CONTEXT` privilege analysis) |
| `OBJ_PRIV` | `VARCHAR2(40)` |  | Unused object privilege |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Object owner |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the object that `USERNAME` has `OBJ_PRIV` on |
| `OBJECT_TYPE` | `VARCHAR2(23)` |  | Type of the object `USERNAME` has `OBJ_PRIV` on |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of the column that `USERNAME` has `OBJ_PRIV` on |
| `GRANT_OPTION` | `NUMBER` |  | Indicates whether the privilege is granted with the `GRANT` option:  - `0` - Indicates that the privilege is granted without the `GRANT` option - `1` - Indicates that the privilege is granted with the `GRANT` option |
| `RUN_NAME` | `VARCHAR2(128)` |  | The name of the run during which the privilege was reported |

See Also:

- " [DBA\_UNUSED\_OBJPRIVS\_PATH](DBA_UNUSED_OBJPRIVS_PATH.md) " for privilege grant path information for unused object privileges
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG-GUID-44CB644B-7B59-4B3B-B375-9F9B96F60186) for more information about privilege analysis
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS74345) for more information about the `DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT` procedure