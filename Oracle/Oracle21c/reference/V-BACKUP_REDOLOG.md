---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_REDOLOG.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.99 V$BACKUP\_REDOLOG

`V$BACKUP_REDOLOG` displays information about archived logs in backup sets from the control file.

Note that online redo logs cannot be backed up directly; they must be archived first to disk and then backed up. An archive log backup set can contain one or more archived logs.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Record ID for this row; it is an integer that identifies this row |
| `STAMP` | `NUMBER` | Timestamp used with RECID to uniquely identify this row |
| `SET_STAMP` | `NUMBER` | One of the foreign keys for the row of the `V$BACKUP_SET` table that identifies this backup set |
| `SET_COUNT` | `NUMBER` | One of the foreign keys for the row of the `V$BACKUP_SET` table that identifies this backup set |
| `THREAD#` | `NUMBER` | Thread number for the log |
| `SEQUENCE#` | `NUMBER` | Log sequence number |
| `RESETLOGS_CHANGE#` | `NUMBER` | Change number of the last resetlogs before the log was written |
| `RESETLOGS_TIME` | `DATE` | Change time of the last resetlogs before the log was written. These will be the same for all logs in a backup set. |
| `FIRST_CHANGE#` | `NUMBER` | SCN when the log was switched into. The redo in the log is at this SCN and greater. |
| `FIRST_TIME` | `DATE` | Time allocated when the log was switched into |
| `NEXT_CHANGE#` | `NUMBER` | SCN when the next log in this thread was switched into. The redo in the log is below this SCN. |
| `NEXT_TIME` | `DATE` | Time when the next log in this thread was switched into |
| `BLOCKS` | `NUMBER` | Size of the log in logical blocks including the header block |
| `BLOCK_SIZE` | `NUMBER` | Size of the log blocks in bytes |
| `TERMINAL` | `VARCHAR2(3)` | Indicates whether this record corresponds to a terminal archived redo log, as defined in `V$ARCHIVED_LOG` (`YES`) or not (`NO`) |
| `SECTION_SIZE` | `NUMBER` | Number of blocks in each section of a multisection log. The value is `0` for whole file logs. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |