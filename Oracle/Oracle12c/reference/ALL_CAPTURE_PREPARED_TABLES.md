---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_CAPTURE_PREPARED_TABLES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_CAPTURE_PREPARED_TABLES` displays information about the tables prepared for instantiation that are accessible to the current user at the local database.

Related View

`DBA_CAPTURE_PREPARED_TABLES` displays information about all tables prepared for instantiation at the local database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table that is ready to be instantiated |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table that is ready to be instantiated |
| `SCN` | `NUMBER` | `NOT NULL` | Smallest system change number (SCN) for which the table can be instantiated |
| `TIMESTAMP` | `DATE` |  | Date and time at which the table was ready to be instantiated |
| `SUPPLEMENTAL_LOG_DATA_PK` | `VARCHAR2(8)` |  | Status of table-level PRIMARY KEY COLUMNS supplemental logging:  - `IMPLICIT` - `EXPLICIT` - `NO` |
| `SUPPLEMENTAL_LOG_DATA_UI` | `VARCHAR2(8)` |  | Status of table-level UNIQUE INDEX COLUMNS supplemental logging:  - `IMPLICIT` - `EXPLICIT` - `NO` |
| `SUPPLEMENTAL_LOG_DATA_FK` | `VARCHAR2(8)` |  | Status of table-level FOREIGN KEY COLUMNS supplemental logging:  - `IMPLICIT` - `EXPLICIT` - `NO` |
| `SUPPLEMENTAL_LOG_DATA_ALL` | `VARCHAR2(8)` |  | Status of table-level ALL COLUMNS supplemental logging:  - `IMPLICIT` - `EXPLICIT` - `NO` |

See Also:

- " [DBA\_CAPTURE\_PREPARED\_TABLES](DBA_CAPTURE_PREPARED_TABLES.md) "
- [Oracle Streams Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=STRMS208) for more information about the possible values for the supplemental logging columns in this view