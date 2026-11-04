---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_IOSTAT_FILETYPE.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.414 DBA\_HIST\_IOSTAT\_FILETYPE

`DBA_HIST_IOSTAT_FILETYPE` displays historical I/O statistics by file type.

This view contains snapshots of `V$IOSTAT_FILE`.

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
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$IOSTAT\_FILE](V-IOSTAT_FILE.md) "