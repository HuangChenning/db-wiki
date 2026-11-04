---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ACTIVITY_TABLE.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.11 DBA\_ACTIVITY\_TABLE

`DBA_ACTIVITY_TABLE` describes table activity snapshots that were recently taken by the Object Activity Tracking System (OATS).

Each row in this view represents one recently completed activity snapshot and describes the table activity that occurred during the snapshot interval.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Activity snapshot identifier |
| `CON_DBNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the container to which the data pertains |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Identifier for the instance in which the activity snapshot was taken |
| `BEGIN_TIME` | `TIMESTAMP(3)` | `NOT NULL` | Begin time for the activity snapshot interval |
| `END_TIME` | `TIMESTAMP(3)` | `NOT NULL` | End time for the activity snapshot interval |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table for which the activity snapshot was taken |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table for which the activity snapshot was taken |
| `USER_CLASS` | `VARCHAR2(7)` |  | Reserved for future use |
| `SCANS` | `NUMBER` |  | Number of table scans |
| `LOADS` | `NUMBER` |  | Number of table loads |
| `LOAD_ROWS` | `NUMBER` |  | Number of rows that were loaded into the table |
| `INSERT_ROWS` | `NUMBER` |  | Number of rows that were inserted into the table |
| `DELETE_ROWS` | `NUMBER` |  | Number of rows that were deleted from the table |
| `UPDATE_ROWS` | `NUMBER` |  | Number of table rows that were updated |
| `TRUNCATES` | `NUMBER` |  | Number of table truncations |
| `TRUNCATED_ROWS` | `NUMBER` |  | Number of table rows that were deleted due to table truncations |
| `PARTITION_TRUNCATES` | `NUMBER` |  | Number of table partition or subpartition truncations |
| `PARTITION_TRUNCATED_ROWS` | `NUMBER` |  | Number of table rows that were deleted due to table partition or subpartition truncations |
| `PARTITION_CREATES` | `NUMBER` |  | Number of table partitions or subpartitions that were created |
| `PARTITION_DROPS` | `NUMBER` |  | Number of table partition or subpartition drops |
| `PARTITION_DROPS_ROWS` | `NUMBER` |  | Number of table rows that were dropped due to table partition or subpartition drops |
| `PARTITION_MOVES` | `NUMBER` |  | Number of table partition or subpartition moves |
| `PARTITION_MOVES_ROWS` | `NUMBER` |  | Number of table rows that were moved due to table partition or subpartition moves |
| `PARTITION_SPLITS` | `NUMBER` |  | Number of table partition or subpartition splits |
| `PARTITION_SPLITS_ROWS` | `NUMBER` |  | Number of table rows that were split due to table partition or subpartition splits |
| `PARTITION_MERGES` | `NUMBER` |  | Number of table partition or subpartition merges |
| `PARTITION_MERGES_ROWS` | `NUMBER` |  | Number of table rows that were merged due to table partition or subpartition merges |
| `PARTITION_COALESCES` | `NUMBER` |  | Number of table partition or subpartition coalesces |
| `PARTITION_COALESCE_ROWS` | `NUMBER` |  | Number of table rows that were redistributed due to table partition or subpartition coalesces |
| `PARTITION_EXCHANGES` | `NUMBER` |  | Number of table partition or subpartition exchanges |
| `PARTITION_EXCHANGES_ROWS` | `NUMBER` |  | Number of table rows that were exchanged due to table partition or subpartition exchanges |

Note:

The counts in this view are approximate in order to keep system overhead low. Also, there are database activities, such as statistics collection, query compilation, and query optimization, that may cause the counts to be different than expected or to vary slightly across successive queries.

Note:

This view does not contain information related to temporary tables or external tables.

Note:

This view is available starting with Oracle Database 21c.

See Also:

" [V$ACTIVITY\_TABLE](V-ACTIVITY_TABLE.md) " to view in-progress table activity snapshots