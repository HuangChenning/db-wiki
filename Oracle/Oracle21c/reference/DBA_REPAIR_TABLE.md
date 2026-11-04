---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_REPAIR_TABLE.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.286 DBA\_REPAIR\_TABLE

`DBA_REPAIR_TABLE` describes any corruptions found by the `DBMS_REPAIR`.`CHECK_OBJECT` procedure.

This information is used by the `DBMS_REPAIR`.`FIX_CORRUPT_BLOCKS` procedure on execution. To create this view, first run the `DBMS_REPAIR`.`ADMIN_TABLES` procedure. To populate the resulting repair table for an object, run the ` DBMS_REPAIR`.`CHECK_OBJECT` procedure on the object.

Note:

The table created by the `DBMS_REPAIR.ADMIN_TABLES` procedure is called `REPAIR TABLE` by default. If you specify a different name, this view will have the name you specify, preceded by " `DBA_REPAIR_` ".

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_ID` | `NUMBER` | `NOT NULL` | Dictionary object number of the object with the corruption |
| `TABLESPACE_ID` | `NUMBER` | `NOT NULL` | Tablespace number of the corrupt object |
| `RELATIVE_FILE_ID` | `NUMBER)` | `NOT NULL` | Relative file number of the corrupt object |
| `BLOCK_ID` | `NUMBER` | `NOT NULL` | Block number of the corruption |
| `CORRUPT_TYPE` | `NUMBER` | `NOT NULL` | Type of corruption encountered |
| `SCHEMA_NAME` | `VARCHAR2(128)` | `NOT NULL` | Schema of the corrupt object |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the corrupt object |
| `BASEOBJECT_NAME` | `VARCHAR2(128)` | `NULL` | If the object is an index, the name of its base table |
| `PARTITION_NAME` | `VARCHAR2(128)` | `NULL` | Partition or subpartition name, if applicable |
| `CORRUPT_DESCRIPTION` | `VARCHAR2(2000)` | `NULL` | Description of corruption |
| `REPAIR_DESCRIPTION` | `VARCHAR2(200)` | `NULL` | Description of repair action |
| `MARKED_CORRUPT` | `VARCHAR2(10)` | `NOT NULL` | Whether the block is marked corrupt (`TRUE` \| `FALSE`) |
| `CHECK_TIMESTAMP` | `DATE` | `NOT NULL` | Date and time when this row was inserted into the repair table |
| `FIX_TIMESTAMP` | `DATE` | `NULL` | Date and time when the block was modified by the `FIX_CORRUPT_BLOCKS` procedure, if applicable |
| `REFORMAT_TIMESTAMP` | `DATE` | `NULL` | Reserved for future use |