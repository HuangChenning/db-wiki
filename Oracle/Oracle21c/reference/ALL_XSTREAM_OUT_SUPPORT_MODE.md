---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XSTREAM_OUT_SUPPORT_MODE.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.161 ALL\_XSTREAM\_OUT\_SUPPORT\_MODE

`ALL_XSTREAM_OUT_SUPPORT_MODE` displays information about the level of XStream capture process support for the tables accessible to the current user in the database.

Related View

`DBA_XSTREAM_OUT_SUPPORT_MODE` displays information about the level of XStream capture process support for the tables in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Table owner |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Table name |
| `SUPPORT_MODE` | `VARCHAR2(6)` |  | Capture process support level for the table:  - `FULL` - A capture process can capture changes made to all of the columns in the table. - `ID` `KEY` - A capture process can capture changes made to the key columns and any other columns in the table that are supported by the capture process, except for LOB, `LONG`, `LONG` `RAW`, and `XMLType` columns. - `NONE` - A capture process cannot capture changes made to any columns in the table. |
| `EXPLANATION` <sup>Foot 1</sup> | `VARCHAR2(4000)` |  | Reason the table does not have `FULL` capture process support  This column is populated only when both of the following conditions are met:  - The value of the `COMPATIBLE` initialization parameter is `20.0` or higher - The value of the `SUPPORT_MODE` column is `ID` `KEY` or `NONE` |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.

See Also:

" [DBA\_XSTREAM\_OUT\_SUPPORT\_MODE](DBA_XSTREAM_OUT_SUPPORT_MODE.md) "