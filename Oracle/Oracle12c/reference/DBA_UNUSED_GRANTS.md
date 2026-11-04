---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_UNUSED_GRANTS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_UNUSED_GRANTS` shows all the grants that are not used during the privilege capture.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE` | `VARCHAR2(128)` |  | Name of the privilege analysis policy |
| `RUN_NAME` | `VARCHAR2(128)` |  | Name of the run of the privilege analysis policy |
| `GRANTEE` | `VARCHAR2(128)` |  | Name of the user who is granted with the privilege or role |
| `ROLENAME` | `VARCHAR2(128)` |  | Name of the role that is granted to the grantee |
| `SYS_PRIV` | `VARCHAR2(40)` |  | Name of the system privilege that is granted to the grantee |
| `OBJ_PRIV` | `VARCHAR2(40)` |  | Name of the object privilege that is granted to the grantee |
| `USER_PRIV` | `VARCHAR2(25)` |  | Name of the user privilege that is granted to the grantee |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Name of the owner of the object for which the object privilege is granted |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the object for which the object privilege is granted |
| `OBJECT_TYPE` | `VARCHAR2(23)` |  | Type of the object for which the object privilege is granted |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of the column in the table for which the object privilege is granted |
| `OPTION$` | `NUMBER` |  | Whether the grant option of the privilege is granted |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).