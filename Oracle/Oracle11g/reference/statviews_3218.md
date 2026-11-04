---
title: DBA_HIST_DISPATCHER
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3218.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_DISPATCHER` displays historical information for each dispatcher process present at the time of the snapshot. This view contains snapshots of information from `V$DISPATCHER` and `V$QUEUE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `NAME` | `VARCHAR2(4)` | `NOT NULL` | Name of the dispatcher process |
| `SERIAL#` | `NUMBER` |  | Serial number of the dispatcher process |
| `IDLE` | `NUMBER` |  | Total idle time for the dispatcher (in hundredths of a second) |
| `BUSY` | `NUMBER` |  | Total busy time for the dispatcher (in hundredths of a second) |
| `WAIT` | `NUMBER` |  | Total time that all items in the dispatcher queue have waited (in hundredths of a second). Divide by `TOTALQ` for average wait per item. |
| `TOTALQ` | `NUMBER` |  | Total number of items that have ever been in the dispatcher queue |
| `SAMPLED_TOTAL_CONN` | `NUMBER` |  | Cumulative sum of total number of connections to the dispatcher over all samples. To determine the average number of connections to the dispatcher between two snapshots, divide the difference in `SAMPLED_TOTAL_CONN` by the difference in `NUM_SAMPLES` (obtained from `DBA_HIST_SHARED_SERVER_SUMMARY`). |