---
title: DBA_HIST_MUTEX_SLEEP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4013.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_MUTEX_SLEEP` displays mutex sleep summary historical statistics information.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database identifier for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `MUTEX_TYPE` | `VARCHAR2(32)` | `NOT NULL` | Mutex type |
| `LOCATION` | `VARCHAR2(40)` | `NOT NULL` | The code location where the waiter slept for the mutex |
| `SLEEPS` | `NUMBER` |  | Number of sleeps for this `MUTEX_TYPE` and `LOCATION` |
| `WAIT_TIME` | `NUMBER` |  | Wait time in microseconds |