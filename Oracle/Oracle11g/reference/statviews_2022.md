---
title: ALL_REFRESH_DEPENDENCIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2022.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_REFRESH_DEPENDENCIES` displays the names of the dependent detail or container tables of all the materialized views in the current schema.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Table name, unique within this schema |
| `PARENT_OBJECT_TYPE` | `CHAR(17)` |  | `MATERIALIZED VIEW` |
| `OLDEST_REFRESH_SCN` | `NUMBER` |  | Minimum SCN of any summary or materialized view that has `TABLE_NAME` as a detail table |
| `OLDEST_REFRESH_DATE` | `DATE` |  | `SYSDATE` when last refreshed |