---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_PERSISTENT_QMN_CACHE.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.21 DBA\_HIST\_PERSISTENT\_QMN\_CACHE

`DBA_HIST_PERSISTENT_QMN_CACHE` displays the historical summary background queue table activity.

This view contains snapshots from `V$PERSISTENT_QMN_CACHE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `QUEUE_TABLE_ID` | `NUMBER` | `NOT NULL` | Queue table object ID |
| `TYPE` | `VARCHAR2(32)` |  | Type of the queue table's queue monitor cache |
| `STATUS` | `NUMBER` |  | Status of the queue table's queue monitor cache |
| `NEXT_SERVICE_TIME` | `TIMESTAMP(3)` |  | Time when the queue table should be serviced by QMON servers |
| `WINDOW_END_TIME` | `TIMESTAMP(3)` |  | Time manager activity period for non-owner queue table operations |
| `TOTAL_RUNS` | `NUMBER` |  | Total number of times this queue table is served |
| `TOTAL_LATENCY` | `NUMBER` |  | Cumulative latency in serving the queue table (in hundredths of a second) |
| `TOTAL_ELAPSED_TIME` | `NUMBER` |  | Total time spent in processing this queue table (in seconds) |
| `TOTAL_CPU_TIME` | `NUMBER` |  | Cumulative CPU time for serving the queue table (in hundredths of a second) |
| `TMGR_ROWS_PROCESSED` | `NUMBER` |  | Number of time manager entries processed |
| `TMGR_ELAPSED_TIME` | `NUMBER` |  | Cumulative time for time management activities (in hundredths of a second) |
| `TMGR_CPU_TIME` | `NUMBER` |  | Cumulative CPU time for time management activities (in hundredths of a second) |
| `LAST_TMGR_PROCESSING_TIME` | `TIMESTAMP(3)` |  | Last timer manager processing time |
| `DEQLOG_ROWS_PROCESSED` | `NUMBER` |  | Number of dequeue log entries processed |
| `DEQLOG_PROCESSING_ELAPSED_TIME` | `NUMBER` |  | Total time for processing dequeue log entries (in hundredths of a second) |
| `DEQLOG_PROCESSING_CPU_TIME` | `NUMBER` |  | Total CPU time for processing dequeue log entries (in hundredths of a second) |
| `LAST_DEQLOG_PROCESSING_TIME` | `TIMESTAMP(3)` |  | Last dequeue log processing time |
| `DEQUEUE_INDEX_BLOCKS_FREED` | `NUMBER` |  | Number of dequeue index blocks freed |
| `HISTORY_INDEX_BLOCKS_FREED` | `NUMBER` |  | Number of history index blocks freed |
| `TIME_INDEX_BLOCKS_FREED` | `NUMBER` |  | Number of time manager index blocks freed |
| `INDEX_CLEANUP_COUNT` | `NUMBER` |  | Number of times index block cleanup was attempted |
| `INDEX_CLEANUP_ELAPSED_TIME` | `NUMBER` |  | Total time for index block cleanup (in hundredths of a second) |
| `INDEX_CLEANUP_CPU_TIME` | `NUMBER` |  | Total CPU time for index block cleanup (in hundredths of a second) |
| `LAST_INDEX_CLEANUP_TIME` | `TIMESTAMP(3)` |  | Last index block cleanup time |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$PERSISTENT\_QMN\_CACHE](V-PERSISTENT_QMN_CACHE.md) "