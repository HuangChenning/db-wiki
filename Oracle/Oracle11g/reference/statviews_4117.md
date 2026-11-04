---
title: DBA_LOGMNR_LOG
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4117.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_LOGMNR_LOG` displays all archived logs registered with active LogMiner persistent sessions in the database.

A persistent LogMiner session is created either by starting Data Guard SQL Apply on a logical standby database for the first time or by creating Streams capture.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `LOGMNR_SESSION_ID` | `NUMBER` | `NOT NULL` | Unique identifier of the persistent session |
| `NAME` | `VARCHAR2(513)` |  | Name of the archived log |
| `DBID` | `NUMBER` | `NOT NULL` | Database identifier that produced the archived log |
| `RESETLOGS_SCN` | `NUMBER` | `NOT NULL` | SCN at which resetlogs operation was performed at the source database generating the archived log |
| `RESETLOGS_TIME` | `NUMBER` | `NOT NULL` | Timestamp at which resetlogs operation was performed at the source database generating the archived log |
| `MODIFIED_TIME` | `DATE` |  | Time at which the archived log was registered with LogMiner |
| `THREAD#` | `NUMBER` | `NOT NULL` | Redo thread at the source database that generated the archived log |
| `SEQUENCE#` | `NUMBER` | `NOT NULL` | Logfile sequence number |
| `FIRST_SCN` | `NUMBER` | `NOT NULL` | Lowest SCN of the redo record contained in the logfile |
| `NEXT_SCN` | `NUMBER` | `NOT NULL` | Highest possible SCN of the redo record contained in the logfile |
| `FIRST_TIME` | `DATE` |  | Time of the first redo record contained in the logfile |
| `NEXT_TIME` | `DATE` |  | Time of the last redo record contained in the logfile |
| `DICTIONARY_BEGIN` | `VARCHAR2(3)` |  | Indicates whether the archived log contains the beginning of a LogMiner dictionary (`YES`) or not (`NO`) |
| `DICTIONARY_END` | `VARCHAR2(3)` |  | Indicates whether the archived log contains the end of a LogMiner dictionary (`YES`) or not (`NO`) |
| `KEEP` | `VARCHAR2(3)` |  | Indicates whether the logfile is still required for this LogMiner session (`YES`) or not (`NO`) |
| `SUSPECT` | `VARCHAR2(3)` |  | Indicates whether the archived log content was deemed to be corrupt or the archived log is partially filled (`YES`) or not (`NO`) |