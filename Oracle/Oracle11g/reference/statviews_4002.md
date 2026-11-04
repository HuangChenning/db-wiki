---
title: DBA_HIST_LATCH_CHILDREN
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4002.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_LATCH_CHILDREN` displays historical statistics about child latches. This view includes all columns of `DBA_HIST_LATCH` plus the `CHILD#` column. Note that child latches have the same parent if their `LATCH#` columns match each other. This view contains snapshots of `V$LATCH_CHILDREN`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `LATCH_HASH` | `NUMBER` |  | Latch Hash |
| `LATCH_NAME` | `VARCHAR2(64)` |  | Latch name |
| `CHILD#` | `NUMBER` |  | Child latch number (unique only to each parent latch) |
| `GETS` | `NUMBER` |  | Number of times the latch was requested in willing-to-wait mode |
| `MISSES` | `NUMBER` |  | Number of times the latch was requested in willing-to-wait mode and the requestor had to wait |
| `SLEEPS` | `NUMBER` |  | Number of times a willing-to-wait latch request resulted in a session sleeping while waiting for the latch |
| `IMMEDIATE_GETS` | `NUMBER` |  | Number of times a latch was requested in no-wait mode |
| `IMMEDIATE_MISSES` | `NUMBER` |  | Number of times a no-wait latch request did not succeed (that is, missed) |
| `SPIN_GETS` | `NUMBER` |  | Number of willing-to-wait latch requests which missed the first try but succeeded while spinning |
| `SLEEP[1 \| 2 \| 3 \| 4]` | `NUMBER` |  | These columns have been deprecated and are present only for compatibility with previous releases of Oracle. No data is accumulated for these columns; they will always have a value of zero. |
| `WAIT_TIME` | `NUMBER` |  | Elapsed time spent waiting for the latch (in microseconds) |