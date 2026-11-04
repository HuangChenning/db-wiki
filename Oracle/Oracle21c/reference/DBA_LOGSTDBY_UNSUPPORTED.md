---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_LOGSTDBY_UNSUPPORTED.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.171 DBA\_LOGSTDBY\_UNSUPPORTED

`DBA_LOGSTDBY_UNSUPPORTED` displays the schemas, tables, and columns in those tables that contain data types that are unsupported by logical standby.

The query results for this view depend on whether the database is currently undergoing a manual rolling upgrade performed using transient logical standby databases. If the database is undergoing such an upgrade, then this view displays information about tables in the database that are unsupported for transient logical standby. If the database is not undergoing such an upgrade, then this view displays information about tables in the database are unsupported for logical standby.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the unsupported table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the unsupported table |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of the unsupported column |
| `ATTRIBUTES` | `VARCHAR2(4000)` |  | If the database is currently undergoing a manual rolling upgrade performed using transient logical standby databases and the value of the `COMPATIBLE` initialization parameter is `20.0` or higher, then this column displays the reason the table is unsupported by SQL Apply. |
| `DATA_TYPE` | `VARCHAR2(106)` |  | Data type of the unsupported column |

Note:

When the value of the `COMPATIBLE` initialization parameter is `20.0` or higher, this view displays all columns in unsupported tables. Otherwise, this view displays only the unsupported columns in unsupported tables.

Note:

A rolling upgrade performed using the `DBMS_ROLLING` PL/SQL package supports more object types than a manual rolling upgrade performed using transient logical standby databases.

See Also:

- " [DBA\_ROLLING\_UNSUPPORTED](DBA_ROLLING_UNSUPPORTED.md) " for more information about determining unsupported data types for a rolling upgrade using the `DBMS_ROLLING` package
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB5214) for more information about rolling operations
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB5460) for more information about unsupported tables for rolling upgrade operations
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS73534) for more information about the `DBMS_ROLLING` package