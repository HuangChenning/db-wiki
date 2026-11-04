---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MVIEW_DETAIL_SUBPARTITION.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.284 ALL\_MVIEW\_DETAIL\_SUBPARTITION

`ALL_MVIEW_DETAIL_SUBPARTITION` displays freshness information, with respect to partition change tracking (PCT) detail subpartitions, for the materialized views accessible to the current user.

Related Views

- `DBA_MVIEW_DETAIL_SUBPARTITION` displays freshness information, with respect to PCT detail subpartitions, for all materialized views in the database.
- `USER_MVIEW_DETAIL_SUBPARTITION` displays freshness information, with respect to PCT detail subpartitions, for the materialized views owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the materialized view |
| `MVIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the materialized view |
| `DETAILOBJ_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the detail object |
| `DETAILOBJ_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the detail object |
| `DETAIL_PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the detail object partition |
| `DETAIL_SUBPARTITION_NAME` | `VARCHAR2(128)` |  | Name of the detail object subpartition |
| `DETAIL_SUBPARTITION_POSITION` | `NUMBER` |  | Position of the detail object subpartition |
| `FRESHNESS` | `CHAR(5)` |  | Freshness state of the detail object subpartition (`FRESH` or `STALE`) |