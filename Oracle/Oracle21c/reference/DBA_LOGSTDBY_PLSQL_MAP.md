---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_LOGSTDBY_PLSQL_MAP.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.165 DBA\_LOGSTDBY\_PLSQL\_MAP

`DBA_LOGSTDBY_PLSQL_MAP` shows the mapping between a supported user invokable (/external) PL/SQL procedure to the corresponding replicated internal PL/SQL procedure.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner name of the procedure |
| `PKG_NAME` | `VARCHAR2(128)` |  | Package name of the user invokable procedure |
| `PROC_NAME` | `VARCHAR2(128)` |  | Procedure name of the user invokable procedure |
| `INTERNAL_PKG_NAME` | `VARCHAR2(128)` |  | Package name of the internal procedure |
| `INTERNAL_PROC_NAME` | `VARCHAR2(128)` |  | Procedure name of the internal procedure |

Note:

In a CDB, this view shows data when queried in the root or a PDB.