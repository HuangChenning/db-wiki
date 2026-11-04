---
title: "V$IOSTAT_CONSUMER_GROUP"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2008.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$IOSTAT_CONSUMER_GROUP` displays disk I/O statistics for consumer groups. If the resource manager is enabled, then I/O statistics for all consumer groups that are part of the currently enabled resource plan are captured.

| Column | Datatype | Description |
| --- | --- | --- |
| `CONSUMER_GROUP_ID` | `NUMBER` | Consumer Group ID |
| `SMALL_READ_MEGABYTES` | `NUMBER` | Number of single block megabytes read |
| `SMALL_WRITE_MEGABYTES` | `NUMBER` | Number of single block megabytes written |
| `LARGE_READ_MEGABYTES` | `NUMBER` | Number of multiblock megabytes read |
| `LARGE_WRITE_MEGABYTES` | `NUMBER` | Number of multiblock megabytes written |
| `SMALL_READ_REQS` | `NUMBER` | Number of single block read requests |
| `SMALL_WRITE_REQS` | `NUMBER` | Number of single block write requests |
| `LARGE_READ_REQS` | `NUMBER` | Number of multiblock read requests |
| `LARGE_WRITE_REQS` | `NUMBER` | Number of multiblock write requests |
| `NUMBER_OF_WAITS` | `NUMBER` | Number of I/O waits by consumer group |
| `WAIT_TIME` | `NUMBER` | Total wait time (in milliseconds) |