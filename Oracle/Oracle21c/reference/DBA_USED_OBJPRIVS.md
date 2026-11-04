---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_USED_OBJPRIVS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.90 DBA\_USED\_OBJPRIVS

`DBA_USED_OBJPRIVS` lists the object privileges (without privilege grant paths) that are used for the privilege analysis policies reported by the `DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT` procedure.

This view provides access to analyzed privilege records in `SYS` tables.

You must have the `CAPTURE_ADMIN` role to access this view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE` | `VARCHAR2(128)` | `NOT NULL` | Name of the privilege analysis policy |
| `SEQUENCE` | `NUMBER` | `NOT NULL` | The sequence number of the privilege analysis run during which the privilege was reported |
| `OS_USER` | `VARCHAR2(128)` |  | Operating system login username |
| `USERHOST` | `VARCHAR2(128)` |  | Client host machine name |
| `MODULE` | `VARCHAR2(64)` |  | Module name |
| `USERNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the user whose privilege was reported |
| `USED_ROLE` | `VARCHAR2(128)` |  | Used role |
| `OBJ_PRIV` | `VARCHAR2(40)` |  | Used object privilege |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Object owner |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the object that `OBJ_PRIV` was used to access |
| `OBJECT_TYPE` | `VARCHAR2(23)` |  | Type of the object that `OBJ_PRIV` was used to access |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of the column that `OBJ_PRIV` was used to access |
| `GRANT_OPTION` | `NUMBER` |  | Indicates whether the `GRANT` option was used:  - `0` - Indicates that the `GRANT` option was not used - `1` - Indicates that the `GRANT` option was used |
| `RUN_NAME` | `VARCHAR2(128)` |  | The name of the run during which the privilege was reported |

See Also:

- " [DBA\_USED\_OBJPRIVS\_PATH](DBA_USED_OBJPRIVS_PATH.md) " for privilege grant path information for used object privileges
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG-GUID-44CB644B-7B59-4B3B-B375-9F9B96F60186) for more information about privilege analysis
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS74345) for more information about the `DBMS_PRIVILEGE_CAPTURE.GENERATE_RESULT` procedure