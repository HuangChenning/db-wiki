---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CAPTURE_PREPARED_SCHEMAS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.121 ALL\_CAPTURE\_PREPARED\_SCHEMAS

`ALL_CAPTURE_PREPARED_SCHEMAS` displays information about the schemas prepared for instantiation that are accessible to the current user at the local database.

Related View

`DBA_CAPTURE_PREPARED_SCHEMAS` displays information about all schemas prepared for instantiation at the local database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEMA_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the schema that is ready to be instantiated |
| `TIMESTAMP` | `DATE` |  | Date and time at which the schema was ready to be instantiated |
| `SUPPLEMENTAL_LOG_DATA_PK` | `VARCHAR2(8)` |  | Status of schema-level PRIMARY KEY COLUMNS supplemental logging:  - `IMPLICIT` - `EXPLICIT` - `NO` |
| `SUPPLEMENTAL_LOG_DATA_UI` | `VARCHAR2(8)` |  | Status of schema-level UNIQUE INDEX COLUMNS supplemental logging:  - `IMPLICIT` - `EXPLICIT` - `NO` |
| `SUPPLEMENTAL_LOG_DATA_FK` | `VARCHAR2(8)` |  | Status of schema-level FOREIGN KEY COLUMNS supplemental logging:  - `IMPLICIT` - `EXPLICIT` - `NO` |
| `SUPPLEMENTAL_LOG_DATA_ALL` | `VARCHAR2(8)` |  | Status of schema-level ALL COLUMNS supplemental logging:  - `IMPLICIT` - `EXPLICIT` - `NO` |

See Also:

" [DBA\_CAPTURE\_PREPARED\_SCHEMAS](DBA_CAPTURE_PREPARED_SCHEMAS.md) "