---
title: ALL_MVIEW_DETAIL_SUBPARTITION
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1148.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_MVIEW_DETAIL_SUBPARTITION` displays the freshness information of the materialized views, with respect to a PCT detail subpartition, accessible to the current user.

Related Views

- `DBA_MVIEW_DETAIL_SUBPARTITION` displays freshness information for all materialized views in the database, with respect to a PCT detail subpartition.
- `USER_MVIEW_DETAIL_SUBPARTITION` displays freshness information for all materialized views, with respect to a PCT detail subpartition, owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the materialized view |
| `MVIEW_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the materialized view |
| `DETAILOBJ_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the detail object |
| `DETAILOBJ_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the detail object |
| `DETAIL_PARTITION_NAME` | `VARCHAR2(30)` |  | Name of the detail object partition |
| `DETAIL_SUBPARTITION_NAME` | `VARCHAR2(30)` |  | Name of the detail object subpartition |
| `DETAIL_SUBPARTITION_POSITION` | `NUMBER` |  | Position of the detail object subpartition |
| `FRESHNESS` | `CHAR(5)` |  | Freshness state (FRESH, STALE, UNKNOWN, NA, and so on) |