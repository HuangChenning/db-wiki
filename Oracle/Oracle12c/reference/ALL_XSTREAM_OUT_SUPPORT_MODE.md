---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_XSTREAM_OUT_SUPPORT_MODE.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_XSTREAM_OUT_SUPPORT_MODE` displays information about the level of XStream capture process support for the tables accessible to the current user in the database.

Related View

`DBA_XSTREAM_OUT_SUPPORT_MODE` displays information about the level of XStream capture process support for the tables in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Table owner |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Table name |
| `SUPPORT_MODE` | `VARCHAR2(6)` |  | Capture process support level for the table:  - `FULL` - A capture process can capture changes made to all of the columns in the table. - `ID` `KEY` - A capture process can capture changes made to the key columns and any other columns in the table that are supported by the capture process, except for LOB, `LONG`, `LONG` `RAW`, and `XMLType` columns. - `NONE` - A capture process cannot capture changes made to any columns in the table. |

See Also:

" [DBA\_XSTREAM\_OUT\_SUPPORT\_MODE](DBA_XSTREAM_OUT_SUPPORT_MODE.md) "