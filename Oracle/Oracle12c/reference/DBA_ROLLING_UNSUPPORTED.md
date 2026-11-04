---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_ROLLING_UNSUPPORTED.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_ROLLING_UNSUPPORTED` displays the schemas, tables, and columns in those tables that contain unsupported data types for a rolling upgrade operation for a logical standby database using the `DBMS_ROLLING` PL/SQL package.

Use this view before you perform a rolling upgrade using `DBMS_ROLLING` to determine what is unsupported.

The data pertains to the container in which the view is queried.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Schema name of the unsupported column |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table that the unsupported column belongs to |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of the unsupported column |
| `ATTRIBUTES` | `VARCHAR2(39)` |  | If not a data type issue, displays the reason why the table is unsupported |
| `DATA_TYPE` | `VARCHAR2(32)` |  | Data type of the unsupported column |

See Also:

- " [DBA\_LOGSTDBY\_UNSUPPORTED](DBA_LOGSTDBY_UNSUPPORTED.md) " for more information about determining unsupported data types for a manual rolling upgrade operation using transient logical standby databases
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SBYDB5214) for more information about rolling operations
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SBYDB5460) for more information about unsupported tables for rolling upgrade operations
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS73534) for more information about the `DBMS_ROLLING` package