---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_GOLDENGATE_SUPPORT_MODE.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.349 DBA\_GOLDENGATE\_SUPPORT\_MODE

`DBA_GOLDENGATE_SUPPORT_MODE` displays information about the level of Oracle GoldenGate capture process support for the tables in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Table owner |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Table name |
| `SUPPORT_MODE` | `VARCHAR2(8)` |  | Capture process support level for the table:  - `FULL` - A capture process can capture changes made to all of the columns in the table - `ID` `KEY` - A capture process can capture changes made to the key columns and any other columns in the table supported by the capture process, except for `LOB`, `LONG`, `LONG RAW`, and `XMLType` columns. - `INTERNAL` - A capture process cannot capture changes made to any columns in the table because the table is secondary to a user-created table and is updated implicitly when changes are made to the user-created table. Such tables include mapping tables for index-organized tables, storage tables for nested tables, materialized view logs, secondary objects associated with domain indexes, and temporary tables. - `PLSQL` - A capture process can capture changes made to the table as long as Procedural Supplemental Logging is enabled on the source database. Such tables include hierarchy-enabled tables, AQ queue tables, and tables containing columns of type `MDSYS.SDO_TOPO_GEOMETRY`, `MDSYS.SDO_GEORASTER`, or `MDSYS.SDO_RDF_TRIPLE_S`. - `NONE` - A capture process cannot capture changes made to any columns in the table because the table is not supported for replication. |
| `EXPLANATION` <sup>Foot 1</sup> | `VARCHAR2(4000)` |  | Reason the table does not have `FULL` capture process support  This column is populated only when both of the following conditions are met:  - The value of the `COMPATIBLE` initialization parameter is `20.0` or higher - The value of the `SUPPORT_MODE` column is `ID` `KEY`, `INTERNAL`, `PLSQL`, or `NONE` |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.