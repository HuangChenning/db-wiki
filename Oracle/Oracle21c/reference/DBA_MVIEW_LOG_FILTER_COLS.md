---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_MVIEW_LOG_FILTER_COLS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.194 DBA\_MVIEW\_LOG\_FILTER\_COLS

`DBA_MVIEW_LOG_FILTER_COLS` displays all columns (excluding primary key columns) being logged in the materialized view logs.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the master table being logged |
| `NAME` | `VARCHAR2(128)` |  | Name of the master table being logged |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Column being logged |