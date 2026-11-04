---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_REFRESH_DEPENDENCIES.html
tags:
  - oracle
  - 19c
  - reference
---

## 3.25 ALL\_REFRESH\_DEPENDENCIES

`ALL_REFRESH_DEPENDENCIES` displays the names of the dependent detail or container tables of all the materialized views in the current schema.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Table name, unique within this schema |
| `PARENT_OBJECT_TYPE` | `CHAR(17)` |  | `MATERIALIZED VIEW` |
| `OLDEST_REFRESH_SCN` | `NUMBER` |  | Minimum SCN of any summary or materialized view that has `TABLE_NAME` as a detail table |
| `OLDEST_REFRESH_DATE` | `DATE` |  | `SYSDATE` when last refreshed |