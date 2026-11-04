---
title: DBA_ORPHAN_KEY_TABLE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4166.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ORPHAN_KEY_TABLE` reports key values from indexes where the underlying base table has block corruptions. To create the view, run the `DBMS_REPAIR`.`ADMIN_TABLES` procedure. To populate the orphan key table for an index, run the `DBMS_REPAIR`.`DUMP_ORPHAN_KEYS` procedure on the index. For each key in the index that points to a corrupt data block, Oracle inserts a row into the orphan key table.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEMA_NAME` | `VARCHAR2(30)` | `NOT NULL` | Schema name of the index |
| `INDEX_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the index |
| `IPART_NAME` | `VARCHAR2(30)` | `NULL` | Name of the index partition or subpartition |
| `INDEX_ID` | `NUMBER` | `NOT NULL` | Dictionary object ID of the index |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the base table of the index |
| `PART_NAME` | `VARCHAR2(30)` | `NULL` | Name of the base table partition or subpartition |
| `TABLE_ID` | `NUMBER` | `NOT NULL` | Dictionary object ID of the base table |
| `KEYDATA` | `UROWID` | `NOT NULL` | Physical rowid of the corrupt data row |
| `KEY` | `UROWID` | `NOT NULL` | Key values for the index entry |
| `DUMP_TIMESTAMP` | `DATE` | `NOT NULL` | Timestamp when the entry was made into the orphan key table |