---
title: DBA_HIST_IOSTAT_FUNCTION
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3234.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_IOSTAT_FUNCTION` displays historical I/O statistics by function. This view contains snapshots of `V$IOSTAT_FUNCTION`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `FUNCTION_ID` | `NUMBER` | `NOT NULL` | Function ID |
| `FUNCTION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Function name |
| `SMALL_READ_MEGABYTES` | `NUMBER` | `NOT NULL` | Number of single block megabytes read |
| `SMALL_WRITE_MEGABYTES` | `NUMBER` | `NOT NULL` | Number of single block megabytes written |
| `LARGE_READ_MEGABYTES` | `NUMBER` | `NOT NULL` | Number of multiblock megabytes read |
| `LARGE_WRITE_MEGABYTES` | `NUMBER` | `NOT NULL` | Number of multiblock megabytes written |
| `SMALL_READ_REQS` | `NUMBER` | `NOT NULL` | Number of single block read requests |
| `SMALL_WRITE_REQS` | `NUMBER` | `NOT NULL` | Number of single block write requests |
| `LARGE_READ_REQS` | `NUMBER` | `NOT NULL` | Number of multiblock read requests |
| `LARGE_WRITE_REQS` | `NUMBER` | `NOT NULL` | Number of multiblock write requests |
| `NUMBER_OF_WAITS` | `NUMBER` | `NOT NULL` | Number of I/O waits by functionality |
| `WAIT_TIME` | `NUMBER` | `NOT NULL` | Total wait time (in milliseconds) |