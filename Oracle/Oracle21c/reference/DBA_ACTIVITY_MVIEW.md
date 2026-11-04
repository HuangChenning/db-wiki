---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ACTIVITY_MVIEW.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.9 DBA\_ACTIVITY\_MVIEW

`DBA_ACTIVITY_MVIEW` describes materialized view activity snapshots that were recently taken by the Object Activity Tracking System (OATS).

Each row in this view represents one recently completed activity snapshot and describes the materialized view activity that occurred during the snapshot interval.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Activity snapshot identifier |
| `CON_DBNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the container to which the data pertains |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Identifier for the instance in which the activity snapshot was taken |
| `BEGIN_TIME` | `TIMESTAMP(3)` | `NOT NULL` | Begin time for the activity snapshot interval |
| `END_TIME` | `TIMESTAMP(3)` | `NOT NULL` | End time for the activity snapshot interval |
| `MVIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the materialized view for which the activity snapshot was taken |
| `MVIEW_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of materialized view for which the activity snapshot was taken |
| `USER_CLASS` | `VARCHAR2(7)` |  | Indicates whether the activity was performed by the RDBMS (`SYS`) or by a user (`NON-SYS`) |
| `COMPILES` | `NUMBER` |  | Number of times the materialized view was compiled  This number includes:  - Explicit compiles performed with the SQL statement `ALTER` `MATERIALIZED` `VIEW` … `COMPILE` - Automatic compiles that occurred because the structure of an underlying base table changed |
| `REWRITES_TEXTMATCH` | `NUMBER` |  | Number of query rewrites that used the text match rewrite method |
| `REWRITES_GENERAL` | `NUMBER` |  | Number of query rewrites that used general rewrite methods |
| `REWRITES_PARTIAL` | `NUMBER` |  | Number of query rewrites that occurred when the view was partially stale  This number includes:  - `UNION` `ALL` operations involving rewritten queries that had one branch with the materialized view and the other branch with its underlying base tables (partial rewrites) - Single query block rewrites of the materialized view that involved a join back to its underlying base table |
| `REWRITES_DELTA` | `NUMBER` |  | Number of query rewrites that used stale data in the materialized view plus the delta information stored in the materialized view logs |
| `REWRITES_PCT` | `NUMBER` |  | Number of partition change tracking (PCT) rewrites |
| `REWRITES_HINTED` | `NUMBER` |  | Number of query rewrites that occurred because the materialized view was eligible for query rewrite and the `SELECT` statement contained the `REWRITE` hint with the name of the materialized view specified in the hint |
| `NOREWRITES_HINTED` | `NUMBER` |  | Reserved for future use |
| `NOREWRITES_STALE` | `NUMBER` |  | Number of query executions that did not use query rewrite because the materialized view was eligible for query rewrite, but stale |
| `REFRESHES_ON_DEMAND` | `NUMBER` |  | Number of `ON` `DEMAND` refreshes  This type of refresh is performed on materialized views that use the `ON` `DEMAND` refresh mode, which instructs the database to refresh the materialized view only when a manual refresh is launched by one of the three `DBMS_MVIEW` refresh procedures. |
| `REFRESHES_ON_COMMIT` | `NUMBER` |  | Number of `ON` `COMMIT` refreshes  This type of refresh is performed on materialized views that use the `ON` `COMMIT` refresh mode, which instructs the database to refresh the materialized view whenever the database commits a transaction that operates on a master table of the materialized view. |
| `REFRESHES_ON_STATEMENT` | `NUMBER` |  | Number of `ON` `STATEMENT` refreshes  This type of refresh is performed on materialized views that use the `ON` `STATEMENT` refresh mode, which instructs the database to perform an automatic refresh of the materialized view every time a DML operation is performed on any of the view's base tables. |
| `REFRESHES_SCHEDULED` | `NUMBER` |  | Number of scheduled refreshes |
| `REFRESHES_AUTOMATIC` | `NUMBER` |  | Number of automatic refreshes |
| `REFRESHES_FAST` | `NUMBER` |  | Number of incremental refreshes |
| `REFRESHES_COMPLETE` | `NUMBER` |  | Number of full refreshes |
| `REFRESHES_PCT` | `NUMBER` |  | Number of partition change tracking (PCT) refreshes |

Note:

The counts in this view are approximate in order to keep system overhead low. Also, there are database activities, such as statistics collection, query compilation, and query optimization, that may cause the counts to be different than expected or to vary slightly across successive queries.

Note:

This view is available starting with Oracle Database 21c.

See Also:

" [V$ACTIVITY\_MVIEW](V-ACTIVITY_MVIEW.md) " to view in-progress materialized view activity snapshots