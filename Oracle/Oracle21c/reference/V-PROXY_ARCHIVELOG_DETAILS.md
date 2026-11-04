---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PROXY_ARCHIVELOG_DETAILS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.136 V$PROXY\_ARCHIVELOG\_DETAILS

`V$PROXY_ARCHIVELOG_DETAILS` contains information about all available archive log proxy copies.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_KEY` | `NUMBER` | Session identifier |
| `SESSION_RECID` | `NUMBER` | Session recid |
| `SESSION_STAMP` | `NUMBER` | Session stamp |
| `COPY_KEY` | `NUMBER` | Copy identifier |
| `THREAD#` | `NUMBER` | Redo thread number |
| `SEQUENCE#` | `NUMBER` | Redo log sequence number |
| `RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs change number of the database when this log was written |
| `RESETLOGS_TIME` | `DATE` | Resetlogs time of the database when this log was written |
| `HANDLE` | `VARCHAR2(513)` | Proxy copy handle identifies the copy for restore |
| `MEDIA` | `VARCHAR2(65)` | Name of the media on which the copy resides. This value is informational only. It is not needed for restore. |
| `MEDIA_POOL` | `NUMBER` | Media pool in which the copy resides. This is the same value that was entered in the `POOL` operand of the Recovery Manager `BACKUP` command. |
| `TAG` | `VARCHAR2(32)` | Proxy copy tag |
| `FIRST_CHANGE#` | `NUMBER` | First change number in the archived log |
| `NEXT_CHANGE#` | `NUMBER` | First change number in the next log |
| `FIRST_TIME` | `DATE` | Timestamp of the first change |
| `NEXT_TIME` | `DATE` | Timestamp of the next change |
| `OUTPUT_BYTES` | `NUMBER` | Total output bytes written |
| `COMPLETION_TIME` | `DATE` | Completion time |
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(3)` | Displayable format for output bytes |
| `KEEP` | `DATE` | Indicates whether this backup set has a retention policy that is different than the value for the configure retention policy (`YES`) or not (`NO`) |
| `KEEP_UNTIL` | `VARCHAR2(11)` | If specified, then this is the date after which the backup becomes obsolete. If this column is `NULL`, then the backup never expires. |
| `KEEP_OPTIONS` | `VARCHAR2(4000)` | Additional retention options for this backup set:  - `LOGS` - Indicates a long-term backup made with the LOGS keyword, which is now deprecated - `BACKUP_LOGS` - Indicates that the backup was made in open mode, so archived log backups must be applied to make it consistent - `NOLOGS` - Indicates a consistent backup made when the database was mounted - `NULL` - Indicates that this backup has no KEEP options and becomes obsolete based on the retention policy |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |