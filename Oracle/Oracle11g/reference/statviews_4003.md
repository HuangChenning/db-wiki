---
title: DBA_HIST_LATCH_MISSES_SUMMARY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4003.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_LATCH_MISSES_SUMMARY` displays historical summary statistics about missed attempts to acquire a latch. This view contains snapshots of `V$LATCH_MISSES`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `PARENT_NAME` | `VARCHAR2(50)` |  | Latch name of a parent latch |
| `WHERE_IN_CODE` | `VARCHAR2(64)` |  | Location that attempted to acquire the latch |
| `NWFAIL_COUNT` | `NUMBER` |  | Number of times that no-wait acquisition of the latch failed |
| `SLEEP_COUNT` | `NUMBER` |  | Number of times that acquisition attempts caused sleeps |
| `WTR_SLP_COUNT` | `NUMBER` |  | Number of times a waiter slept |