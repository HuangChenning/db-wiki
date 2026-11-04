---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_LATCH_CHILDREN.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.2 DBA\_HIST\_LATCH\_CHILDREN

`DBA_HIST_LATCH_CHILDREN` displays historical statistics about child latches.

This view includes all columns of `DBA_HIST_LATCH` plus the `CHILD#` column. Note that child latches have the same parent if their `LATCH#` columns match each other. This view contains snapshots of `V$LATCH_CHILDREN`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `LATCH_HASH` | `NUMBER` | `NOT NULL` | Latch hash |
| `LATCH_NAME` | `VARCHAR2(64)` | `NOT NULL` | Latch name |
| `CHILD#` | `NUMBER` | `NOT NULL` | Child latch number (unique only to each parent latch) |
| `GETS` | `NUMBER` |  | Number of times the latch was requested in willing-to-wait mode |
| `MISSES` | `NUMBER` |  | Number of times the latch was requested in willing-to-wait mode and the requester had to wait |
| `SLEEPS` | `NUMBER` |  | Number of times a willing-to-wait latch request resulted in a session sleeping while waiting for the latch |
| `IMMEDIATE_GETS` | `NUMBER` |  | Number of times a latch was requested in no-wait mode |
| `IMMEDIATE_MISSES` | `NUMBER` |  | Number of times a no-wait latch request did not succeed (that is, missed) |
| `SPIN_GETS` | `NUMBER` |  | Number of willing-to-wait latch requests which missed the first try but succeeded while spinning |
| `SLEEP[1 \| 2 \| 3 \| 4]` | `NUMBER` |  | These columns have been deprecated and are present only for compatibility with previous releases of Oracle. No data is accumulated for these columns; they will always have a value of zero. |
| `WAIT_TIME` | `NUMBER` |  | Elapsed time spent waiting for the latch (in microseconds) |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [DBA\_HIST\_LATCH](DBA_HIST_LATCH.md) "
- " [V$LATCH](V-LATCH.md) "