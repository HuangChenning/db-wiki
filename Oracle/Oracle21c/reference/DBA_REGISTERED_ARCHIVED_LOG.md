---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_REGISTERED_ARCHIVED_LOG.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.277 DBA\_REGISTERED\_ARCHIVED\_LOG

`DBA_REGISTERED_ARCHIVED_LOG` displays information about all registered archived logfiles in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CONSUMER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Consumer name of the archived logs |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | Name of the database which generated the redo logs |
| `THREAD#` | `NUMBER` | `NOT NULL` | Thread number of the archived redo log. The thread number is `1` for a single instance. For Real Application Clusters, this column will contain different numbers. |
| `SEQUENCE#` | `NUMBER` | `NOT NULL` | Sequence number of the archived redo log file |
| `FIRST_SCN` | `NUMBER` | `NOT NULL` | System change number (SCN) of the current archived redo log |
| `NEXT_SCN` | `NUMBER` |  | System change number (SCN) of the next archived redo log |
| `FIRST_TIME` | `DATE` |  | Date and time of the current archived redo log |
| `NEXT_TIME` | `DATE` |  | Date and time of the next archived redo log |
| `NAME` | `VARCHAR2(513)` |  | Name of the archived redo log |
| `MODIFIED_TIME` | `DATE` |  | Time when the archived redo log was registered |
| `DICTIONARY_BEGIN` | `VARCHAR2(3)` |  | Indicates whether the beginning of the dictionary build is in the archived redo log (`YES`) or not (`NO`) |
| `DICTIONARY_END` | `VARCHAR2(3)` |  | Indicates whether the end of the dictionary build is in the archived redo log (`YES`) or not (`NO`) |
| `PURGEABLE` | `VARCHAR2(3)` |  | Indicates whether the redo log can be permanently removed (`YES`) or not (`NO`) |
| `RESET_LOGS_CHANGE#` | `NUMBER` | `NOT NULL` | Resetlogs change number of the database when the log was written |
| `RESET_TIMESTAMP` | `NUMBER` | `NOT NULL` | Resetlogs time of the database when the log was written |