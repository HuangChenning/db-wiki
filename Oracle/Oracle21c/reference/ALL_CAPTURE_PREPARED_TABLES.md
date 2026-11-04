---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CAPTURE_PREPARED_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.122 ALL\_CAPTURE\_PREPARED\_TABLES

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

" [DBA\_CAPTURE\_PREPARED\_TABLES](DBA_CAPTURE_PREPARED_TABLES.md) "