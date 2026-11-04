---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-IOSTAT_FILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.18 V$IOSTAT\_FILE

`V$IOSTAT_FILE` displays information about disk I/O statistics of database files (including data files, temp files, and other types of database files).

I/O statistics for Data files and Temp files are provided for each file. All other file types (for example, control files, log files, archive logs, and so on) have their statistics consolidated into one entry in the view.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE_NO` | `NUMBER` | File identification number |
| `FILETYPE_ID` | `NUMBER` | Type of file (for example, log file, data file, and so on) |
| `FILETYPE_NAME` | `VARCHAR2(28)` | Name of the file, in the case of a data file or temp file. For all other files, a corresponding string to be displayed (for example, `ARCHIVELOG`). |
| `SMALL_READ_MEGABYTES` | `NUMBER` | Number of single block megabytes read |
| `SMALL_WRITE_MEGABYTES` | `NUMBER` | Number of single block megabytes written |
| `LARGE_READ_MEGABYTES` | `NUMBER` | Number of multiblock megabytes read |
| `LARGE_WRITE_MEGABYTES` | `NUMBER` | Number of multiblock megabytes written |
| `SMALL_READ_REQS` | `NUMBER` | Number of single block read requests |
| `SMALL_WRITE_REQS` | `NUMBER` | Number of single block write requests |
| `SMALL_SYNC_READ_REQS` | `NUMBER` | Number of synchronous single block read requests |
| `LARGE_READ_REQS` | `NUMBER` | Number of multiblock read requests |
| `LARGE_WRITE_REQS` | `NUMBER` | Number of multiblock write requests |
| `SMALL_READ_SERVICETIME` | `NUMBER` | Total service time (in milliseconds) for single block read requests |
| `SMALL_WRITE_SERVICETIME` | `NUMBER` | Total service time (in milliseconds) for single block write requests |
| `SMALL_SYNC_READ_LATENCY` | `NUMBER` | Latency for single block synchronous reads (in milliseconds) |
| `LARGE_READ_SERVICETIME` | `NUMBER` | Total service time (in milliseconds) for multiblock read requests |
| `LARGE_WRITE_SERVICETIME` | `NUMBER` | Total service time (in milliseconds) for multiblock write requests |
| `ASYNCH_IO` | `VARCHAR2(9)` | Indicates whether asynchronous I/O is available for the file (`ASYNC_ON`) or not (`ASYNC_OFF`) |
| `ACCESS_METHOD` | `VARCHAR2(11)` | I/O library used to access the file. Possible values include:  - `OS_LIB` - Operating system calls are used to access the file - `ODM_LIB` - Oracle Disk Manager library is used to access the file - `ASM_MANAGED` - The file is managed and accessed though ASM - `DNFS_LIB` - The file is accessed through Direct NFS library |
| `RETRIES_ON_ERROR` | `NUMBER` | Number of read retries on error |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |