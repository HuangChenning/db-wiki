---
title: DBA_XSTREAM_OUT_SUPPORT_MODE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5109.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_XSTREAM_OUT_SUPPORT_MODE` displays information about the level of capture process support for the tables in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Table owner |
| `OBJECT_NAME` | `VARCHAR2(30)` |  | Table name |
| `SUPPORT_MODE` | `VARCHAR2(6)` |  | Capture process support level for the table: - `FULL` - A capture process can capture changes made to all of the columns in the table. - `ID` `KEY` - A capture process can capture changes made to the key columns and any other columns in the table that are supported by the capture process, except for LOB, `LONG`, `LONG` `RAW`, and `XMLType` columns. - `NONE` - A capture process cannot capture changes made to any columns in the table. |

Note:

The `DBA_XSTREAM_OUT_SUPPORT_MODE` view is available starting with Oracle Database 11g Release 2 (11.2.0.2).