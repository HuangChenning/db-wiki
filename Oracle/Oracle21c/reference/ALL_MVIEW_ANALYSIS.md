---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MVIEW_ANALYSIS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.280 ALL\_MVIEW\_ANALYSIS

It provides additional information for analysis by applications. Minimal information is displayed for materialized views that do not support query rewrite (such as materialized views with remote master tables or nondeterministic functions).

Related Views

- `DBA_MVIEW_ANALYSIS` describes all such materialized views in the database.
- `USER_MVIEW_ANALYSIS` describes all such materialized views owned by the current user.

Note:

All of the information in these views is also displayed in `ALL_MVIEWS` and its related views. Oracle recommends that you refer to `ALL_MVIEWS` for this information instead of these views.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the materialized view |
| `MVIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the materialized view |
| `MVIEW_TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the container table (see next column) |
| `CONTAINER_NAME` | `VARCHAR2(128)` |  | Name of the internal container in which the materialized view data is held. Normally this is the same as `MVIEW_NAME`. For materialized views created before Oracle8i, Oracle Database attaches the 6-byte prefix `SNAP$_`. If `MVIEW_NAME` has more than 19 bytes, then Oracle Database truncates the name to 19 bytes and adds a 4-byte sequence number as a suffix to produce a nonambiguous `CONTAINER_NAME`. |
| `LAST_REFRESH_SCN` | `NUMBER` |  | System change number (SCN) of the last refresh operation |
| `LAST_REFRESH_DATE` | `DATE` |  | `SYSDATE` of the last refresh |
| `REFRESH_METHOD` | `VARCHAR2(8)` |  | Default refresh method:  - `FORCE` - `FAST` - `COMPLETE` - `NEVER` |
| `SUMMARY` | `VARCHAR2(1)` |  | Indicates whether this materialized view includes a `GROUP BY` clause or aggregation (`Y`) or not (`N`) |
| `FULLREFRESHTIM` | `NUMBER` |  | Approximate refresh time, in seconds, for full refresh |
| `INCREFRESHTIM` | `NUMBER` |  | Approximate refresh time, in seconds, for fast refresh |
| `CONTAINS_VIEWS` | `VARCHAR2(1)` |  | Indicates whether this materialized view contains a view in its definition (`Y`) or not (`N`) |
| `UNUSABLE` | `VARCHAR2(1)` |  | Indicates whether this materialized view is `UNUSABLE` (inconsistent data) (`Y`) or not (`N`). A materialized view can be `UNUSABLE` if a system failure occurs during a full refresh. |
| `RESTRICTED_SYNTAX` | `VARCHAR2(1)` |  | Indicates whether this materialized view had a restriction in its defining query that limits the use of query rewrite (`Y`) or not (`N`). More complete information is provided by the `REWRITE_CAPABILITY` column of the `*_MVIEWS` view. |
| `INC_REFRESHABLE` | `VARCHAR2(1)` |  | Indicates whether this materialized view can be fast refreshed (`Y`) or not (`N`) |
| `KNOWN_STALE` | `VARCHAR2(1)` |  | Indicates whether the data contained in the materialized view is known to be inconsistent with the master table data because that has been updated since the last successful refresh (`Y`) or not (`N`) |
| `INVALID` | `VARCHAR2(1)` |  | Indicates whether this materialized view is in an invalid state (inconsistent metadata) (`Y`) or not (`N`) |
| `REWRITE_ENABLED` | `VARCHAR2(1)` |  | Indicates whether this materialized view is currently enabled for query rewrite (`Y`) or not (`N`) |
| `QUERY_LEN` | `NUMBER` |  | Length (in bytes) of the query field |
| `QUERY` | `LONG` |  | `SELECT` expression of the materialized view definition |
| `REVISION` | `NUMBER` | `NOT NULL` | Reserved for internal use |

See Also:

- " [DBA\_MVIEW\_ANALYSIS](DBA_MVIEW_ANALYSIS.md) "
- " [USER\_MVIEW\_ANALYSIS](USER_MVIEW_ANALYSIS.md) "