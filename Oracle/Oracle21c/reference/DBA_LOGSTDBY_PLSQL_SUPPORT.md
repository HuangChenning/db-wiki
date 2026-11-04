---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_LOGSTDBY_PLSQL_SUPPORT.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.166 DBA\_LOGSTDBY\_PLSQL\_SUPPORT

`DBA_LOGSTDBY_PLSQL_SUPPORT` shows the PL/SQL packages that are only supported during rolling operations.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner name of the package |
| `PKG_NAME` | `VARCHAR2(128)` |  | Package name of the user invokable procedure |
| `SUPPORT_LEVEL` | `VARCHAR2(12)` |  | Logical standby PL/SQL support level for the package:  - `ALWAYS` - PL/SQL replication is always supported for this package, whether it is called inside or outside of `DBMS_ROLLING` - `DBMS_ROLLING`: PL/SQL replication is supported only when the procedure is called inside `DBMS_ROLLING` |

Note:

In a CDB, this view shows data when queried in the root or a PDB.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS73534) for more information about the `DBMS_ROLLING` package