---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WORKLOAD_LONG_SQLTEXT.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.123 DBA\_WORKLOAD\_LONG\_SQLTEXT

`DBA_WORKLOAD_LONG_SQLTEXT` displays the captured SQL statements that are longer than 1000 characters. You can load SQL statements longer than 1000 characters to the `DBA_WORKLOAD_LONG_SQLTEXT` view using the `DBMS_WORKLOAD_REPLAY.LOAD_LONG_SQLTEXT` procedure.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE_ID` | `NUMBER(38)` | `NOT NULL` | Internal key for the workload capture |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL identifier of the parent cursor in the library cache |
| `SQL_FULLTEXT` | `CLOB` |  | Full text for the SQL statement exposed as a CLOB column |

See Also:

- " [DBA\_WORKLOAD\_CAPTURE\_SQLTEXT](DBA_WORKLOAD_CAPTURE_SQLTEXT.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS-GUID-3E8587A7-3CFC-401E-A101-0A20893B5EB7) for information about the `DBMS_WORKLOAD_REPLAY` package