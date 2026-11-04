---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_SYNC_IO.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.106 V$BACKUP\_SYNC\_IO

`V$BACKUP_SYNC_IO` displays performance information about ongoing and recently completed RMAN backups and restores.

For each backup, it contains one row for each input data file, one row for the aggregate total performance of all data files, and one row for the output backup piece. This data is not stored persistently, and is not preserved when the instance is re-started.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | The Oracle SID of the session doing the backup or restore |
| `SERIAL` | `NUMBER` | The use count for the SID doing the backup or restore |
| `USE_COUNT` | `NUMBER` | A counter that can be used to identify rows from different backup sets |
| `RMAN_STATUS_RECID` | `NUMBER` | Owning `V$RMAN_STATUS` record ID |
| `RMAN_STATUS_STAMP` | `NUMBER` | Owning `V$RMAN_STATUS` record stamp |
| `DEVICE_TYPE` | `VARCHAR2(17)` | The device type where the file is located |
| `TYPE` | `VARCHAR2(9)` | `INPUT`, `OUTPUT`, or `AGGREGATE` |
| `STATUS` | `VARCHAR2(11)` | `NOT STARTED`, `IN PROGRESS`, or `FINISHED` |
| `FILENAME` | `VARCHAR2(513)` | The name of the backup file being read or written |
| `SET_COUNT` | `NUMBER` | The set count of the backup set being read or written |
| `SET_STAMP` | `NUMBER` | The set stamp of the backup set being read or written |
| `BUFFER_SIZE` | `NUMBER` | The size of the buffers being used to read/write this file, in bytes |
| `BUFFER_COUNT` | `NUMBER` | The number of buffers being used to read/write this file |
| `TOTAL_BYTES` | `NUMBER` | The total number of bytes that will be read or written for this file, if known. If not known, this column will be null. |
| `OPEN_TIME` | `DATE` | The time this file was opened. If `TYPE` =' `AGGREGATE` ', then this is the time that the first file in the aggregate was opened. |
| `CLOSE_TIME` | `DATE` | The time this file was closed. If `TYPE` =' `AGGREGATE` ', then this is the time that the last file in the aggregate was closed. |
| `ELAPSED_TIME` | `NUMBER` | The time, in hundredths of a second, that the file was open |
| `MAXOPENFILES` | `NUMBER` | The number of concurrently open DISK files. This value is only present in rows where `TYPE` =' `AGGREGATE` '. |
| `BYTES` | `NUMBER` | The number of bytes read or written so far |
| `EFFECTIVE_BYTES_PER_SECOND` | `NUMBER` | The I/O rate that was achieved with this device during this backup |
| `IO_COUNT` | `NUMBER` | The number of I/Os that were performed to this file |
| `IO_TIME_TOTAL` | `NUMBER` | The total time, in hundredths of a second, taken to do I/O for this file |
| `IO_TIME_MAX` | `NUMBER` | The maximum time taken for a single I/O request |
| `DISCRETE_BYTES_PER_SECOND` | `NUMBER` | The average transfer rate for this file |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |