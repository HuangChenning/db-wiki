---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_GOLDENGATE_SUPPORT_MODE.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.323 DBA\_GOLDENGATE\_SUPPORT\_MODE

`DBA_GOLDENGATE_SUPPORT_MODE` displays information about the level of Oracle GoldenGate capture process support for the tables in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Table owner |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Table name |
| `SUPPORT_MODE` | `VARCHAR2(8)` |  | Capture process support level for the table:  - `FULL` - A capture process can capture changes made to all of the columns in the table - `ID KEY` - A capture process can capture changes made to the key columns and any other columns in the table supported by the capture process, except for `LOB`, `LONG`, `LONG RAW`, and `XMLType` columns. - `INTERNAL` - A capture process cannot capture changes made to any columns in the table because the table is secondary to a user-created table and is updated implicitly when changes are made to the user-created table. Such tables include mapping tables for index-organized tables, storage tables for nested tables, materialized view logs, secondary objects associated with domain indexes, and temporary tables. - `NONE` - A capture process cannot capture changes made to any columns in the table because the table is not supported for replication. |