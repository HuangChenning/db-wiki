---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_MVIEW_LOG_FILTER_COLS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_MVIEW_LOG_FILTER_COLS` displays all columns (excluding primary key columns) being logged in the materialized view logs.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the master table being logged |
| `NAME` | `VARCHAR2(128)` |  | Name of the master table being logged |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Column being logged |