---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-INDEXED_FIXED_COLUMN.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.5 V$INDEXED\_FIXED\_COLUMN

`V$INDEXED_FIXED_COLUMN` displays the columns in dynamic performance tables that are indexed (`X$` tables).

The `X$` tables can change without notice. Use this view only to write queries against fixed views (`V$` views) more efficiently.

| Column | Datatype | Description |
| --- | --- | --- |
| `TABLE_NAME` | `VARCHAR2(128)` | Name of the dynamic performance table that is indexed |
| `INDEX_NUMBER` | `NUMBER` | Number that distinguishes to which index a column belongs |
| `COLUMN_NAME` | `VARCHAR2(128)` | Name of the column that is being indexed |
| `COLUMN_POSITION` | `NUMBER` | Position of the column in the index key (this is mostly relevant for multicolumn indexes) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |