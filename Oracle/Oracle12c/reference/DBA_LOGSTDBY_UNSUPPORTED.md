---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_LOGSTDBY_UNSUPPORTED.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_LOGSTDBY_UNSUPPORTED` displays the schemas, tables, and columns in those tables that contain unsupported data types.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the unsupported table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the unsupported table |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of the unsupported column |
| `ATTRIBUTES` | `VARCHAR2(39)` |  | When possible, displays the reason why the table is not supported by SQL Apply. The `ATTRIBUTES` column may be NULL if the table structure itself is not supported by SQL Apply (for example, the table is system-partitioned), or when the structure of the table is supported but certain columns in the table have an unsupported datatype. |
| `DATA_TYPE` | `VARCHAR2(32)` |  | Datatype of the unsupported column |

Note:

A rolling upgrade performed using the `DBMS_ROLLING` PL/SQL package supports more object types than a manual rolling upgrade performed using transient logical standby databases.

See Also:

- " [DBA\_ROLLING\_UNSUPPORTED](DBA_ROLLING_UNSUPPORTED.md) " for more information about determining unsupported data types for a rolling upgrade using the `DBMS_ROLLING` package
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SBYDB5214) for more information about rolling operations
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SBYDB5460) for more information about unsupported tables for rolling upgrade operations
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS73534) for more information about the `DBMS_ROLLING` package