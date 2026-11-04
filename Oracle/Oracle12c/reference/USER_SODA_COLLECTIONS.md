---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_SODA_COLLECTIONS.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_SODA_COLLECTIONS` displays information about Simple Oracle Document Access (SODA) collections.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `URI_NAME` | `NVARCHAR2(255)` | `NOT NULL` | Collection name |
| `OBJECT_TYPE` | `VARCHAR2(10)` | `NOT NULL` | Indicates whether the collection is table-based (`TABLE`) or view-based (`VIEW`) |
| `OBJECT_SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Name of the schema that includes the table or view on which the collection is based |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table or view on which the collection is based |
| `CREATED_ON` | `TIMESTAMP(6)` | `NOT NULL` | Collection creation time |
| `CREATE_MODE` | `VARCHAR2(10)` | `NOT NULL` | Creation mode. Possible values:  - `DDL`: A new table was created at collection creation time - `MAP`: The collection was created by mapping a preexisting table or view  Note: For view-based collections, the value of this column is always `MAP`. New views are not created for view-based collections. A view-based collection is always created by mapping a preexisting view. |
| `JSON_DESCRIPTOR` | `VARCHAR2(4000)` | `NOT NULL` | Collection metadata, expressed in JavaScript Object Notation (JSON) |