---
title: DBA_HIST_IOSTAT_DETAIL
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3231.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_IOSTAT_DETAIL` displays I/O statistics aggregated by combination of file type and function (component). This view contains snapshots of `V$IOSTAT_FILE` and `V$IOSTAT_FUNCTION`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `FUNCTION_ID` | `NUMBER` | `NOT NULL` | Function ID |
| `FUNCTION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Function name |
| `FILETYPE_ID` | `NUMBER` | `NOT NULL` | Type of file (for example, log file, data file, and so on) |
| `FILETYPE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the file, in the case of a data file or temp file. For all other files, a corresponding string to be displayed (for example, `ARCHIVELOG`). |
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