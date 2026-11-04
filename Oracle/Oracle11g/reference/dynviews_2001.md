---
title: "V$INDEXED_FIXED_COLUMN"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2001.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$INDEXED_FIXED_COLUMN` displays the columns in dynamic performance tables that are indexed (`X$` tables). The `X$` tables can change without notice. Use this view only to write queries against fixed views (`V$` views) more efficiently.

| Column | Datatype | Description |
| --- | --- | --- |
| `TABLE_NAME` | `VARCHAR2(30)` | Name of the dynamic performance table that is indexed |
| `INDEX_NUMBER` | `NUMBER` | Number that distinguishes to which index a column belongs |
| `COLUMN_NAME` | `VARCHAR2(30)` | Name of the column that is being indexed |
| `COLUMN_POSITION` | `NUMBER` | Position of the column in the index key (this is mostly relevant for multicolumn indexes) |