---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MVIEW_DETAIL_RELATIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.283 ALL\_MVIEW\_DETAIL\_RELATIONS

`ALL_MVIEW_DETAIL_RELATIONS` describes the named detail relations that are either specified in the `FROM` list of the subquery that defines a materialized view accessible to the current user, or that are indirectly referenced through views in that `FROM` list. Inline views in the materialized view definition are not represented in this view or the related views.

Related Views

- `DBA_MVIEW_DETAIL_RELATIONS` describes all such detail relations defined for all materialized views in the database.
- `USER_MVIEW_DETAIL_RELATIONS` describes such detail relations defined for all materialized views owned by the current user.

Note:

All three views exclude materialized views that reference remote tables or that includes references to a nonstatic value such as `SYSDATE` or `USER`. These views also exclude materialized views that were created as snapshots before Oracle8i and that were never altered to enable query rewrite.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the materialized view |
| `MVIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the materialized view |
| `DETAILOBJ_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Detail object owner |
| `DETAILOBJ_NAME` | `VARCHAR2(128)` | `NOT NULL` | Detail object name (that is, the name of a table or view) |
| `DETAILOBJ_TYPE` | `VARCHAR2(9)` |  | Detail object type:  - `TABLE` - `VIEW` - `SNAPSHOT` - `CONTAINER` - `UNDEFINED` |
| `DETAILOBJ_ALIAS` | `VARCHAR2(128)` |  | Implicit or explicit alias for detail relation |
| `DETAILOBJ_PCT` | `VARCHAR2(1)` |  | Indicates whether the detail object PCT is supported (`Y`) or not (`N`) |
| `NUM_FRESH_PCT_PARTITIONS` | `NUMBER` |  | Number of fresh PCT partitions |
| `NUM_STALE_PCT_PARTITIONS` | `NUMBER` |  | Number of stale PCT partitions |

See Also:

- " [DBA\_MVIEW\_DETAIL\_RELATIONS](DBA_MVIEW_DETAIL_RELATIONS.md) "
- " [USER\_MVIEW\_DETAIL\_RELATIONS](USER_MVIEW_DETAIL_RELATIONS.md) "