---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_LOGSTDBY_PLSQL_MAP.html
tags:
  - oracle
  - 12c
  - reference
---

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