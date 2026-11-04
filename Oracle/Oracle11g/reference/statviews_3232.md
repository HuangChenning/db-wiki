---
title: DBA_HIST_IOSTAT_FILETYPE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3232.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_IOSTAT_FILETYPE` displays historical I/O statistics by file type. This view contains snapshots of `V$IOSTAT_FILE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `FILETYPE_ID` | `NUMBER` | `NOT NULL` | Type of file (for example, log file, data file, and so on) |
| `FILETYPE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the file, in the case of a data file or temp file. For all other files, a corresponding string to be displayed (for example, `ARCHIVELOG`). |
| `SMALL_READ_MEGABYTES` | `NUMBER` | `NOT NULL` | Number of single block megabytes read |
| `SMALL_WRITE_MEGABYTES` | `NUMBER` | `NOT NULL` | Number of single block megabytes written |
| `LARGE_READ_MEGABYTES` | `NUMBER` | `NOT NULL` | Number of multiblock megabytes read |
| `LARGE_WRITE_MEGABYTES` | `NUMBER` | `NOT NULL` | Number of multiblock megabytes written |
| `SMALL_READ_REQS` | `NUMBER` | `NOT NULL` | Number of single block read requests |
| `SMALL_WRITE_REQS` | `NUMBER` | `NOT NULL` | Number of single block write requests |
| `SMALL_SYNC_READ_REQS` | `NUMBER` | `NOT NULL` | Number of synchronous single block read requests |
| `LARGE_READ_REQS` | `NUMBER` | `NOT NULL` | Number of multiblock read requests |
| `LARGE_WRITE_REQS` | `NUMBER` | `NOT NULL` | Number of multiblock write requests |
| `SMALL_READ_SERVICETIME` | `NUMBER` | `NOT NULL` | Total service time (in milliseconds) for single block read requests |
| `SMALL_WRITE_SERVICETIME` | `NUMBER` | `NOT NULL` | Total service time (in milliseconds) for single block write requests |
| `SMALL_SYNC_READ_LATENCY` | `NUMBER` | `NOT NULL` | Latency for single block synchronous reads (in milliseconds) |
| `LARGE_READ_SERVICETIME` | `NUMBER` | `NOT NULL` | Total service time (in milliseconds) for multiblock read requests |
| `LARGE_WRITE_SERVICETIME` | `NUMBER` | `NOT NULL` | Total service time (in milliseconds) for multiblock write requests |
| `RETRIES_ON_ERROR` | `NUMBER` | `NOT NULL` | Number of read retries on error |