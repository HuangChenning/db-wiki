---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGMNR_LOGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.54 V$LOGMNR\_LOGS

| Column | Datatype | Description |
| --- | --- | --- |
| `LOG_ID` | `NUMBER` | This column is deprecated. |
| `FILENAME` | `VARCHAR2(512)` | Name of the log file |
| `LOW_TIME` | `DATE` | Oldest date of any records in the file |
| `HIGH_TIME` | `DATE` | Most recent date of any records in the file |
| `DB_ID` | `NUMBER` | Database ID |
| `DB_NAME` | `VARCHAR2(8)` | Name of the database |
| `RESET_SCN` | `NUMBER` | Resetlogs SCN of the database incarnation that generated the log file |
| `RESET_SCN_TIME` | `DATE` | Resetlogs timestamp of the database incarnation that generated the log file |
| `COMPATIBLE` | `VARCHAR2(17)` | The setting of the database COMPATIBLE initialization parameter at the time the log file was generated |
| `THREAD_ID` | `NUMBER` | Thread number |
| `THREAD_SQN` | `NUMBER` | Thread sequence number |
| `LOW_SCN` | `NUMBER` | SCN allocated when log switched into |
| `NEXT_SCN` | `NUMBER` | SCN after this log. Low SCN of the next log. |
| `DICTIONARY_BEGIN` | `VARCHAR2(3)` | Indicates whether dictionary dumped to redo logs starts in this redo log (`YES`) or not (`NO`) |
| `DICTIONARY_END` | `VARCHAR2(3)` | Indicates whether dictionary dumped to redo logs ends in this redo log (`YES`) or not (`NO`) |
| `TYPE` | `VARCHAR2(7)` | Redo log file type:  - `ARCHIVED` - `ONLINE` |
| `BLOCKSIZE` | `NUMBER` | Database block size |
| `FILESIZE` | `NUMBER` | Size of the redo file (in bytes) |
| `INFO` | `VARCHAR2(32)` | Informational message. A value of `MISSING_LOGFILE` will be assigned to a row entry where a needed log file is missing from the list of log files. |
| `STATUS` | `NUMBER` | Status of the redo log file:  - `0` - Will be read - `1` - First to be read - `2` - Not needed - `4` - Missing log file |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |