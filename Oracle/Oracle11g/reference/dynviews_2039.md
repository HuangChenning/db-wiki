---
title: "V$LOGMNR_LOGS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2039.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LOGMNR_LOGS` contains log information.

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
| `TYPE` | `VARCHAR2(7)` | Redo log file type: |
| `BLOCKSIZE` | `NUMBER` | Database block size |
| `FILESIZE` | `NUMBER` | Size of the redo file (in bytes) |
| `INFO` | `VARCHAR2(32)` | Informational message. A value of `MISSING_LOGFILE` will be assigned to a row entry where a needed log file is missing from the list of log files. |
| `STATUS` | `NUMBER` | Status of the redo log file: |