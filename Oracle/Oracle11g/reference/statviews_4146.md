---
title: DBA_MVIEW_LOG_FILTER_COLS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4146.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_MVIEW_LOG_FILTER_COLS` displays all columns (excluding primary key columns) being logged in the materialized view logs.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the master table being logged |
| `NAME` | `VARCHAR2(30)` |  | Name of the master table being logged |
| `COLUMN_NAME` | `VARCHAR2(30)` |  | Column being logged |