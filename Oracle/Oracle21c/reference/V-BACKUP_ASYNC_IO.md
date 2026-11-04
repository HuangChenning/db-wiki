---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_ASYNC_IO.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.85 V$BACKUP\_ASYNC\_IO

`V$BACKUP_ASYNC_IO` displays performance information about ongoing and recently completed RMAN backups and restores.

For each backup, it contains one row for each input data file, one row for the aggregate total performance of all data files, and one row for the output backup piece. This data is not stored persistently, and is not preserved when the instance is re-started.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Oracle SID of the session doing the backup or restore |
| `SERIAL` | `NUMBER` | Use count for the SID doing the backup or restore |
| `USE_COUNT` | `NUMBER` | A counter that can be used to identify rows from different backup sets |
| `RMAN_STATUS_RECID` | `NUMBER` | Owning `V$RMAN_STATUS` record ID |
| `RMAN_STATUS_STAMP` | `NUMBER` | Owning `V$RMAN_STATUS` record stamp |
| `DEVICE_TYPE` | `VARCHAR2(17)` | Device type where the file is located |
| `TYPE` | `VARCHAR2(9)` | `INPUT`, `OUTPUT`, or `AGGREGATE` |
| `STATUS` | `VARCHAR2(11)` | `NOT STARTED`, `IN PROGRESS`, or `FINISHED` |
| `FILENAME` | `VARCHAR2(513)` | Name of the backup file being read or written |
| `SET_COUNT` | `NUMBER` | Set count of the backup set being read or written |
| `SET_STAMP` | `NUMBER` | Set stamp of the backup set being read or written |
| `BUFFER_SIZE` | `NUMBER` | Size of the buffers being used to read/write the file, in bytes |
| `BUFFER_COUNT` | `NUMBER` | Number of buffers being used to read/write the file |
| `TOTAL_BYTES` | `NUMBER` | Total number of bytes that will be read or written for the file, if known. If not known, this column will be null |
| `OPEN_TIME` | `DATE` | Time the file was opened. If `TYPE` =' `AGGREGATE` ', then this is the time that the first file in the aggregate was opened |
| `CLOSE_TIME` | `DATE` | Time the file was closed. If `TYPE` =' `AGGREGATE` ', then this is the time that the last file in the aggregate was closed |
| `ELAPSED_TIME` | `NUMBER` | Time, in hundredths of a second, that the file was open |
| `MAXOPENFILES` | `NUMBER` | Number of concurrently open DISK files. This value is only present in rows where `TYPE` =' `AGGREGATE` '. |
| `BYTES` | `NUMBER` | Number of bytes read or written so far |
| `EFFECTIVE_BYTES_PER_SECOND` | `NUMBER` | I/O rate that was achieved with this device during this backup |
| `IO_COUNT` | `NUMBER` | Number of I/Os that were performed to this file |
| `READY` | `NUMBER` | Number of asynchronous requests for which a buffer was immediately ready for use |
| `SHORT_WAITS` | `NUMBER` | Number of times that a buffer was not immediately available, but a buffer became available after doing a nonblocking poll for I/O completion |
| `SHORT_WAIT_TIME_TOTAL` | `NUMBER` | Total time, in hundredths of a second, taken by nonblocking polls for I/O completion |
| `SHORT_WAIT_TIME_MAX` | `NUMBER` | Maximum time taken for a nonblocking poll for I/O completion, in hundredths of a second |
| `LONG_WAITS` | `NUMBER` | The number of times that a buffer was not immediately available, and only became available after a blocking wait was issued |
| `LONG_WAIT_TIME_TOTAL` | `NUMBER` | The total time, in hundredths of a second, taken by blocking waits for I/O completion |
| `LONG_WAIT_TIME_MAX` | `NUMBER` | The maximum time taken for a blocking wait for I/O completion, in hundredths of a second |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |