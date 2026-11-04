---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_DISPATCHER.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.398 DBA\_HIST\_DISPATCHER

`DBA_HIST_DISPATCHER` displays historical information for each dispatcher process present at the time of the snapshot.

This view contains snapshots of information from `V$DISPATCHER` and `V$QUEUE`.

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
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$DISPATCHER](V-DISPATCHER.md) "
- " [V$QUEUE](V-QUEUE.md) "