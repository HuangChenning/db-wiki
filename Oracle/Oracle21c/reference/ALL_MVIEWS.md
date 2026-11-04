---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MVIEWS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.289 ALL\_MVIEWS

`ALL_MVIEWS` describes all materialized views accessible to the current user.

Related Views

- `DBA_MVIEWS` describes all materialized views in the database.
- `USER_MVIEWS` describes all materialized views owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Schema in which the materialized view was created |
| `MVIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the materialized view |
| `CONTAINER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the container in which the materialized view's data is held. Normally this is the same as `MVIEW_NAME`. For materialized views created before Oracle8i, Oracle Database attaches the 6-byte prefix `SNAP$_`. If `MVIEW_NAME` has more than 19 bytes, then Oracle Database truncates the name to 19 bytes and may add a 4-byte sequence number as a suffix to produce a nonambiguous `CONTAINER_NAME`. |
| `QUERY` | `LONG` |  | Query that defines the materialized view |
| `QUERY_LEN` | `NUMBER(38)` |  | Length (in bytes) of the defining query |
| `UPDATABLE` | `VARCHAR2(1)` |  | Indicates whether the materialized view is updatable (`Y`) or not (`N`) |
| `UPDATE_LOG` | `VARCHAR2(128)` |  | For updatable materialized views, the filename of the update log |
| `MASTER_ROLLBACK_SEG` | `VARCHAR2(128)` |  | Rollback segment for the master site or the master materialized view site |
| `MASTER_LINK` | `VARCHAR2(128)` |  | Database link for the master site or the master materialized view site |
| `REWRITE_ENABLED` | `VARCHAR2(1)` |  | Indicates whether rewrite is enabled (`Y`) or not (`N`) |
| `REWRITE_CAPABILITY` | `VARCHAR2(9)` |  | Indicates whether the materialized view is eligible for rewrite, and if so, what rules must be followed:  - `NONE` - Materialized view cannot be used for rewrite, because rewrite is disallowed or prevented - `TEXTMATCH` - Defining query of the materialized view contained restrictions on the use of query rewrite - `GENERAL` - Defining query of the materialized view contained no restrictions on the use of query rewrite, so Oracle Database can apply any rewrite rule that is supported |
| `REFRESH_MODE` | `VARCHAR2(9)` |  | Refresh mode of the materialized view:  - `COMMIT` - Oracle Database refreshes this materialized view when a transaction on one of the materialized view's masters commits - `DEMAND` - Oracle Database refreshes this materialized view whenever an appropriate refresh procedure is called - `STATEMENT` - Oracle Database refreshes this materialized view whenever a DML operation is performed on any of the materialized view’s base tables - `NEVER` - Oracle Database never refreshes this materialized view |
| `REFRESH_METHOD` | `VARCHAR2(8)` |  | Default method used to refresh the materialized view (can be overridden through the API):  - `COMPLETE` - Materialized view is completely refreshed from the masters - `FORCE` - Oracle Database performs a fast refresh if possible, otherwise a complete refresh - `FAST` - Oracle Database performs an incremental refresh applying changes that correspond to changes in the masters since the last refresh - `NEVER` - User specified that Oracle Database should not refresh this materialized view |
| `BUILD_MODE` | `VARCHAR2(9)` |  | Indicates how the materialized view was populated during creation:  - `IMMEDIATE` - Populated from the masters during creation - `DEFERRED` - Not populated during creation. Must be explicitly populated later by the user. - `PREBUILT` - Populated with an existing table during creation. The relationship of the contents of this prebuilt table to the materialized view's masters is unknown to Oracle Database. |
| `FAST_REFRESHABLE` | `VARCHAR2(18)` |  | Indicates whether the materialized view is eligible for incremental (fast) refresh. Oracle Database calculates this value statically, based on the materialized view definition query:  - `NO` - Materialized view is not fast refreshable, and hence is complex - `DML` - Fast refresh is supported only for DML operations - `DIRLOAD_DML` - Fast refresh is supported for both direct loads and DML operations - `DIRLOAD_LIMITEDDML` - Fast refresh is supported for direct loads and a subset of DML operations |
| `LAST_REFRESH_TYPE` | `VARCHAR2(8)` |  | Method used for the most recent refresh:  - `COMPLETE` - Most recent refresh was complete - `FAST` - Most recent refresh was fast (incremental) - `NA` - Materialized view has not yet been refreshed (for example, if it was created `DEFERRED`) |
| `LAST_REFRESH_DATE` | `DATE` |  | Date on which the materialized view was most recently refreshed (blank if not yet populated) |
| `LAST_REFRESH_END_TIME` | `DATE` |  | End time of the most recent refresh on the materialized view (blank if not yet populated) |
| `STALENESS` | `VARCHAR2(19)` |  | Relationship between the contents of the materialized view and the contents of the materialized view's masters:  - `FRESH` - Materialized view is a read-consistent view of the current state of its masters - `IMPORT` - Materialized view is imported from another database (the value of the `UNKNOWN_IMPORT` column is `Y`). Therefore, it is unknown whether the materialized view is in a read-consistent view of its masters from any point in time. The `STALENESS` of this view will turn to `FRESH` on a complete refresh. - `NEEDS_COMPILE` - Some object upon which the materialized view depends has changed. An `ALTER MATERIALIZED VIEW...COMPILE` statement is required to validate this materialized view and compute the staleness of the contents. - `STALE` - Materialized view is out of date because one or more of its masters has changed. If the materialized view was `FRESH` before it became `STALE`, then it is a read-consistent view of a former state of its masters. - `UNDEFINED` - Materialized view has remote masters. The concept of staleness is not defined for such materialized views. - `UNKNOWN` - Oracle Database does not know whether the materialized view is in a read-consistent view of its masters from any point in time (this is the case for materialized views created on prebuilt tables) - `UNUSABLE` - Materialized view is not a read-consistent view of its masters from any point in time |
| `AFTER_FAST_REFRESH` | `VARCHAR2(19)` |  | Specifies the staleness value that will occur if a fast refresh is applied to this materialized view. Its values are the same as for the `STALENESS` column, plus the value `NA`, which is used when fast refresh is not applicable to this materialized view. |
| `UNKNOWN_PREBUILT` | `VARCHAR2(1)` |  | Indicates whether the materialized view is prebuilt (`Y`) or not (`N`) |
| `UNKNOWN_PLSQL_FUNC` | `VARCHAR2(1)` |  | Indicates whether the materialized view contains PL/SQL functions (`Y`) or not (`N`) |
| `UNKNOWN_EXTERNAL_TABLE` | `VARCHAR2(1)` |  | Indicates whether the materialized view contains external tables (`Y`) or not (`N`) |
| `UNKNOWN_CONSIDER_FRESH` | `VARCHAR2(1)` |  | Indicates whether the materialized view is considered fresh (`Y`) or not (`N`) |
| `UNKNOWN_IMPORT` | `VARCHAR2(1)` |  | Indicates whether the materialized view is imported (`Y`) or not (`N`) |
| `UNKNOWN_TRUSTED_FD` | `VARCHAR2(1)` |  | Indicates whether the materialized view uses trusted constraints for refresh (`Y`) or not (`N`) |
| `COMPILE_STATE` | `VARCHAR2(19)` |  | Validity of the materialized view with respect to the objects upon which it depends:  - `VALID` - Materialized view has been validated without error, and no object upon which it depends has changed since the last validation - `NEEDS_COMPILE` - Some object upon which the materialized view depends has changed. An `ALTER MATERIALIZED VIEW...COMPILE` statement is required to validate this materialized view. - `ERROR` - Materialized view has been validated with one or more errors |
| `USE_NO_INDEX` | `VARCHAR2(1)` |  | Indicates whether the materialized view was created using the `USING NO INDEX` clause (`Y`) or the materialized view was created with the default index (`N`). The `USING NO INDEX` clause suppresses the creation of the default index. |
| `STALE_SINCE` | `DATE` |  | Time from when the materialized view became stale |
| `NUM_PCT_TABLES` | `NUMBER` |  | Number of PCT detail tables |
| `NUM_FRESH_PCT_REGIONS` | `NUMBER` |  | Number of fresh PCT partition regions |
| `NUM_STALE_PCT_REGIONS` | `NUMBER` |  | Number of stale PCT partition regions |
| `SEGMENT_CREATED` | `VARCHAR2(3)` |  | Indicates whether the materialized view was created using the SEGMENT CREATION DEFERRED clause. The value is YES if the segment for the materialized view is created and NO if it is not. |
| `EVALUATION_EDITION` | `VARCHAR2(128)` |  | Name of the edition in which editioned objects referenced in an expression column are resolved |
| `UNUSABLE_BEFORE` | `VARCHAR2(128)` |  | Name of the oldest edition in which the stored results of the materialized view's subquery may be used for query rewrite. In editions before the specified edition, the stored results of the materialized view's data are considered unusable. This value is NULL if no such edition is specified. |
| `UNUSABLE_BEGINNING` | `VARCHAR2(128)` |  | Name of the oldest edition in which the stored results of the materialized view's subquery may not be used for query rewrite. The data is unusable for query rewrite in the specified edition and in any descendants of this edition. This value is NULL if no such edition is specified. |
| `DEFAULT_COLLATION` | `VARCHAR2(100)` |  | Default collation for the materialized view |
| `ON_QUERY_COMPUTATION` | `VARCHAR2(1)` |  | Indicates whether the materialized view is a real-time materialized view (`Y`) or not (`N`) |
| `AUTO` <sup>Foot 1</sup> | `VARCHAR2(3)` |  | Indicates whether the materialized view is an automatic materialized view (`YES`) or not (`NO`) |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.

See Also:

- " [DBA\_MVIEWS](DBA_MVIEWS.md) "
- " [USER\_MVIEWS](USER_MVIEWS.md) "
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DWHSG-GUID-A7AE8E5D-68A5-4519-81EB-252EAAF0ADFF) for more information on materialized views to support data warehousing