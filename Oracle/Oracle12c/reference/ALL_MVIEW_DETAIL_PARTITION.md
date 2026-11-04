---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_MVIEW_DETAIL_PARTITION.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_MVIEW_DETAIL_PARTITION` displays freshness information, with respect to partition change tracking (PCT) detail partitions, for the materialized views accessible to the current user.

Related Views

- `DBA_MVIEW_DETAIL_PARTITION` displays freshness information, with respect to PCT detail partitions, for all materialized views in the database.
- `USER_MVIEW_DETAIL_PARTITION` displays freshness information, with respect to PCT detail partitions, for the materialized views owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the materialized view |
| `MVIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the materialized view |
| `DETAILOBJ_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the detail object |
| `DETAILOBJ_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the detail object |
| `DETAIL_PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the detail object partition |
| `DETAIL_PARTITION_POSITION` | `NUMBER` |  | Position of the detail object partition |
| `FRESHNESS` | `CHAR(5)` |  | Freshness state of the detail object partition (`FRESH` or `STALE`) |

See Also:

- " [DBA\_MVIEW\_DETAIL\_PARTITION](DBA_MVIEW_DETAIL_PARTITION.md) "
- " [USER\_MVIEW\_DETAIL\_PARTITION](USER_MVIEW_DETAIL_PARTITION.md) "