---
title: "V$CONTROLFILE_RECORD_SECTION"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1088.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$CONTROLFILE_RECORD_SECTION` displays information about the control file record sections.

| Column | Datatype | Description |
| --- | --- | --- |
| `TYPE` | `VARCHAR2(28)` | Identifies the type of record section: - `DATABASE` - `CKPT PROGRESS` - `REDO THREAD` - `REDO LOG` - `DATAFILE` - `FILENAME` - `TABLESPACE` - `TEMPORARY FILENAME` - `RMAN CONFIGURATION` - `LOG HISTORY` - `OFFLINE RANGE` - `ARCHIVED LOG` - `BACKUP SET` - `BACKUP PIECE` - `BACKUP DATAFILE` - `BACKUP REDOLOG` - `DATAFILE COPY` - `BACKUP CORRUPTION` - `COPY CORRUPTION` - `DELETED OBJECT` - `PROXY COPY` - `BACKUP SPFILE` - `DATABASE INCARNATION` - `FLASHBACK LOG` - `RECOVERY DESTINATION` - `INSTANCE SPACE RESERVATION` - `REMOVABLE RECOVERY FILES` - `RMAN STATUS` - `THREAD INSTANCE NAME MAPPING` - `MTTR` - `DATAFILE HISTORY` - `PLUGGED` `IN` `DATAFILE` |
| `RECORD_SIZE` | `NUMBER` | Record size in bytes |
| `RECORDS_TOTAL` | `NUMBER` | Number of records allocated for the section |
| `RECORDS_USED` | `NUMBER` | Number of records used in the section |
| `FIRST_INDEX` | `NUMBER` | Index (position) of the first record |
| `LAST_INDEX` | `NUMBER` | Index of the last record |
| `LAST_RECID` | `NUMBER` | Record ID of the last record |