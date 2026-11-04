---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_MVIEW_LOG_FILTER_COLS.html
tags:
  - oracle
  - 19c
  - reference
---

## 5.194 DBA\_MVIEW\_LOG\_FILTER\_COLS

`DBA_MVIEW_LOG_FILTER_COLS` displays all columns (excluding primary key columns) being logged in the materialized view logs.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the master table being logged |
| `NAME` | `VARCHAR2(128)` |  | Name of the master table being logged |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Column being logged |