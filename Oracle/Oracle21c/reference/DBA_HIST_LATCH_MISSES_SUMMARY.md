---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_LATCH_MISSES_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.3 DBA\_HIST\_LATCH\_MISSES\_SUMMARY

`DBA_HIST_LATCH_MISSES_SUMMARY` displays historical summary statistics about missed attempts to acquire a latch.

This view contains snapshots of `V$LATCH_MISSES`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `PARENT_NAME` | `VARCHAR2(50)` | `NOT NULL` | Latch name of a parent latch |
| `WHERE_IN_CODE` | `VARCHAR2(64)` | `NOT NULL` | Location that attempted to acquire the latch |
| `NWFAIL_COUNT` | `NUMBER` |  | Number of times that no-wait acquisition of the latch failed |
| `SLEEP_COUNT` | `NUMBER` |  | Number of times that acquisition attempts caused sleeps |
| `WTR_SLP_COUNT` | `NUMBER` |  | Number of times a waiter slept |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$LATCH\_MISSES](V-LATCH_MISSES.md) "