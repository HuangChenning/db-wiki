---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SQLSET_BINDS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.82 ALL\_SQLSET\_BINDS

`ALL_SQLSET_BINDS` displays the bind values associated with all SQL tuning sets accessible to the current user.

Related Views

- `DBA_SQLSET_BINDS` displays the bind values associated with all SQL tuning sets in the database.
- `USER_SQLSET_BINDS` displays the bind values associated with the SQL tuning sets owned by the current user. This view does not display the `SQLSET_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SQLSET_NAME` | `VARCHAR2(128)` |  | Name of the SQL tuning set for the statement |
| `SQLSET_OWNER` | `VARCHAR2(128)` |  | User name of the SQL tuning set owner |
| `SQLSET_ID` | `NUMBER` |  | ID of the SQL tuning set for the statement |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB |
| `SQL_ID` | `VARCHAR2(13)` |  | SQL identifier of the parent cursor in the library cache |
| `FORCE_MATCHING_SIGNATURE` | `NUMBER` |  | The signature used when the `CURSOR_SHARING` parameter is set to `FORCE` |
| `PLAN_HASH_VALUE` | `NUMBER` |  | Numerical representation of the SQL plan for the cursor. Comparing one `PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line-by-line). |
| `POSITION` | `NUMBER` |  | Bind position |
| `VALUE` | `ANYDATA` |  | Bind value. This column is `NULL` for PL/SQL bind types. |
| `CAPTURED` | `CHAR(1)` |  | Binds captured |
| `SQL_SEQ` | `NUMBER` |  | SQL sequence |

See Also:

- " [DBA\_SQLSET\_BINDS](DBA_SQLSET_BINDS.md) "
- " [USER\_SQLSET\_BINDS](USER_SQLSET_BINDS.md) "