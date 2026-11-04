---
title: DBA_HIST_ENQUEUE_STAT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3221.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_ENQUEUE_STAT` displays historical statistics on the number of enqueue (lock) requests for each type of lock. This view contains snapshots of `V$ENQUEUE_STATISTICS`.

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