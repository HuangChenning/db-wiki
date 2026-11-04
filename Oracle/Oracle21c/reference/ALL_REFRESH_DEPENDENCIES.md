---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_REFRESH_DEPENDENCIES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.26 ALL\_REFRESH\_DEPENDENCIES

`ALL_REFRESH_DEPENDENCIES` displays the names of the dependent detail or container tables of all the materialized views in the current schema.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Table name, unique within this schema |
| `PARENT_OBJECT_TYPE` | `CHAR(17)` |  | `MATERIALIZED VIEW` |
| `OLDEST_REFRESH_SCN` | `NUMBER` |  | Minimum SCN of any summary or materialized view that has `TABLE_NAME` as a detail table |
| `OLDEST_REFRESH_DATE` | `DATE` |  | `SYSDATE` when last refreshed |