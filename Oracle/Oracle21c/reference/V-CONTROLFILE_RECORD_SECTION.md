---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CONTROLFILE_RECORD_SECTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.143 V$CONTROLFILE\_RECORD\_SECTION

`V$CONTROLFILE_RECORD_SECTION` displays information about the control file record sections.

| Column | Datatype | Description |
| --- | --- | --- |
| `TYPE` | `VARCHAR2(28)` | Identifies the type of record section:  - `DATABASE` - `CKPT PROGRESS` - `REDO THREAD` - `REDO LOG` - `DATAFILE` - `FILENAME` - `TABLESPACE` - `TEMPORARY FILENAME` - `RMAN CONFIGURATION` - `LOG HISTORY` - `OFFLINE RANGE` - `ARCHIVED LOG` - `BACKUP SET` - `BACKUP PIECE` - `BACKUP DATAFILE` - `BACKUP REDOLOG` - `DATAFILE COPY` - `BACKUP CORRUPTION` - `COPY CORRUPTION` - `DELETED OBJECT` - `PROXY COPY` - `BACKUP SPFILE` - `DATABASE INCARNATION` - `FLASHBACK LOG` - `RECOVERY DESTINATION` - `INSTANCE SPACE RESERVATION` - `REMOVABLE RECOVERY FILES` - `RMAN STATUS` - `THREAD INSTANCE NAME MAPPING` - `MTTR` - `DATAFILE HISTORY` - `PLUGGED` `IN` `DATAFILE` |
| `RECORD_SIZE` | `NUMBER` | Record size in bytes |
| `RECORDS_TOTAL` | `NUMBER` | Number of records allocated for the section |
| `RECORDS_USED` | `NUMBER` | Number of records used in the section |
| `FIRST_INDEX` | `NUMBER` | Index (position) of the first record |
| `LAST_INDEX` | `NUMBER` | Index of the last record |
| `LAST_RECID` | `NUMBER` | Record ID of the last record |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |