---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_ENQUEUE_STAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.401 DBA\_HIST\_ENQUEUE\_STAT

`DBA_HIST_ENQUEUE_STAT` displays historical statistics on the number of enqueue (lock) requests for each type of lock.

This view contains snapshots of `V$ENQUEUE_STATISTICS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `EQ_TYPE` | `VARCHAR2(2)` | `NOT NULL` | Type of enqueue requested |
| `REQ_REASON` | `VARCHAR2(64)` | `NOT NULL` | Reason for the enqueue request |
| `TOTAL_REQ#` | `NUMBER` |  | Total number of enqueue requests or enqueue conversions for this type of enqueue |
| `TOTAL_WAIT#` | `NUMBER` |  | Total number of times an enqueue request or conversion resulted in a wait |
| `SUCC_REQ#` | `NUMBER` |  | Number of times an enqueue request or conversion was granted |
| `FAILED_REQ#` | `NUMBER` |  | Number of times an enqueue request or conversion failed |
| `CUM_WAIT_TIME` | `NUMBER` |  | Total amount of time (in milliseconds) spent waiting for the enqueue or enqueue conversion |
| `EVENT#` | `NUMBER` |  | Event number |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$ENQUEUE\_STATISTICS](V-ENQUEUE_STATISTICS.md) "