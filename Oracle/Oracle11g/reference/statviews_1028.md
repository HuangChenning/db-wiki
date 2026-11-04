---
title: ALL_CAPTURE_PREPARED_DATABASE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1028.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CAPTURE_PREPARED_DATABASE` displays information about when the local database was prepared for instantiation. If the local database was not prepared for instantiation, then this view contains no rows.

Related View

`DBA_CAPTURE_PREPARED_DATABASE` displays information about when the local database was prepared for instantiation.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TIMESTAMP` | `DATE` |  | Date and time at which the local database was ready to be instantiated |
| `SUPPLEMENTAL_LOG_DATA_PK` | `VARCHAR2(8)` |  | Status of database-level PRIMARY KEY COLUMNS supplemental logging: - `IMPLICIT` - `EXPLICIT` - `NO` |
| `SUPPLEMENTAL_LOG_DATA_UI` | `VARCHAR2(8)` |  | Status of database-level UNIQUE INDEX COLUMNS supplemental logging: - `IMPLICIT` - `EXPLICIT` - `NO` |
| `SUPPLEMENTAL_LOG_DATA_FK` | `VARCHAR2(8)` |  | Status of database-level FOREIGN KEY COLUMNS supplemental logging: - `IMPLICIT` - `EXPLICIT` - `NO` |
| `SUPPLEMENTAL_LOG_DATA_ALL` | `VARCHAR2(8)` |  | Status of database-level ALL COLUMNS supplemental logging: - `IMPLICIT` - `EXPLICIT` - `NO` |

See Also:

- ["DBA\_CAPTURE\_PREPARED\_DATABASE"](statviews_3100.md)
- [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_cpmon.htm#STRMS208) for more information about the possible values for the supplemental logging columns in this view