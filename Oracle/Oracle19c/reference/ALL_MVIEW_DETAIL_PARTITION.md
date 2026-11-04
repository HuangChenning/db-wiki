---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_MVIEW_DETAIL_PARTITION.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.274 ALL\_MVIEW\_DETAIL\_PARTITION

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
| `FRESHNESS` | `VARCHAR2(7)` |  | Freshness state of the detail object logical partition. Possible values: - `FRESH` - `STALE` - `UNKNOWN` |
| `LAST_REFRESH_TIME` <sup>Foot 1</sup> | `DATE` |  | Date and time at which the materialized view was last refreshed |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 19c.

See Also:

- " [DBA\_MVIEW\_DETAIL\_PARTITION](DBA_MVIEW_DETAIL_PARTITION.md) "
- " [USER\_MVIEW\_DETAIL\_PARTITION](USER_MVIEW_DETAIL_PARTITION.md) "