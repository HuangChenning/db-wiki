---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_CAPTURE_PREPARED_DATABASE.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_CAPTURE_PREPARED_DATABASE` displays information about when the local database was prepared for instantiation. If the local database was not prepared for instantiation, then this view contains no rows.

Related View

`DBA_CAPTURE_PREPARED_DATABASE` displays information about when the local database was prepared for instantiation.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TIMESTAMP` | `DATE` |  | Date and time at which the local database was ready to be instantiated |
| `SUPPLEMENTAL_LOG_DATA_PK` | `VARCHAR2(8)` |  | Status of database-level PRIMARY KEY COLUMNS supplemental logging:  - `IMPLICIT` - `EXPLICIT` - `NO` |
| `SUPPLEMENTAL_LOG_DATA_UI` | `VARCHAR2(8)` |  | Status of database-level UNIQUE INDEX COLUMNS supplemental logging:  - `IMPLICIT` - `EXPLICIT` - `NO` |
| `SUPPLEMENTAL_LOG_DATA_FK` | `VARCHAR2(8)` |  | Status of database-level FOREIGN KEY COLUMNS supplemental logging:  - `IMPLICIT` - `EXPLICIT` - `NO` |
| `SUPPLEMENTAL_LOG_DATA_ALL` | `VARCHAR2(8)` |  | Status of database-level ALL COLUMNS supplemental logging:  - `IMPLICIT` - `EXPLICIT` - `NO` |

See Also:

- " [DBA\_CAPTURE\_PREPARED\_DATABASE](DBA_CAPTURE_PREPARED_DATABASE.md) "
- [Oracle Streams Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=STRMS208) for more information about the possible values for the supplemental logging columns in this view