---
title: DBA_LOGSTDBY_UNSUPPORTED
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4128.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_LOGSTDBY_UNSUPPORTED` displays the schemas, tables, and columns in those tables that contain unsupported datatypes. Use this view when you are preparing to create a logical standby database. This view is for logical standby databases only.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the unsupported table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the unsupported table |
| `COLUMN_NAME` | `VARCHAR2(30)` |  | Name of the unsupported column |
| `ATTRIBUTES` | `VARCHAR2(39)` |  | Displays the reason why the table is not supported by SQL Apply. If the structure of the table is unsupported (not just the datatype of some columns), then this view displays all columns in the table, with one of the following values displayed for each column in the table: - `IOT with Overflow` - `IOT with LOB` - `Mapping table for physical rowid of IOT` - `IOT with row movement` - `Table Compression` - `Object Table` - `AQ queue table` - `Unsupported Virtual Column` - `Encrypted Column`  If the structure of the table is supported but certain columns in the table have unsupported datatypes, the `ATTRIBUTE` column will be NULL. |
| `DATA_TYPE` | `VARCHAR2(32)` |  | Datatype of the unsupported column |