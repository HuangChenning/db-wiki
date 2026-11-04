---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PROXY_COPY_DETAILS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.138 V$PROXY\_COPY\_DETAILS

`V$PROXY_COPY_DETAILS` contains information about all available control file and datafile proxy copies.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_KEY` | `NUMBER` | Session identifier |
| `SESSION_RECID` | `NUMBER` | Session recid |
| `SESSION_STAMP` | `NUMBER` | Session stamp |
| `COPY_KEY` | `NUMBER` | Copy identifier |
| `FILE#` | `NUMBER` | Absolute datafile number, or 0 if this is a control file backup |
| `HANDLE` | `VARCHAR2(513)` | Proxy copy handle identifies the copy for restore |
| `MEDIA` | `VARCHAR2(65)` | Name of the media on which the copy resides. This value is informational only. It is not needed for restore. |
| `MEDIA_POOL` | `NUMBER` | Media pool in which the copy resides. This is the same value that was entered in the `POOL` operand of the Recovery Manager `BACKUP` command. |
| `TAG` | `VARCHAR2(32)` | Proxy copy tag |
| `CREATION_CHANGE#` | `NUMBER` | Datafile creation change number |
| `CREATION_TIME` | `DATE` | Datafile creation timestamp |
| `CHECKPOINT_CHANGE#` | `NUMBER` | Checkpoint change number of the datafile when the copy was made |
| `CHECKPOINT_TIME` | `DATE` | Checkpoint timestamp of the datafile when the copy was made |
| `OUTPUT_BYTES` | `NUMBER` | Total output bytes written |
| `COMPLETION_TIME` | `DATE` | Completion time |
| `CONTROLFILE_TYPE` | `VARCHAR2(1)` | Type of control file:  - `B` - Normal control file - `S` - Standby control file |
| `KEEP` | `VARCHAR2(3)` | Indicates whether this backup set has a retention policy that is different than the value for the configure retention policy (`YES`) or not (`NO`) |
| `KEEP_UNTIL` | `DATE` | If specified, then this is the date after which the backup becomes obsolete. If this column is NULL, then the backup never expires. |
| `KEEP_OPTIONS` | `VARCHAR2(11)` | Additional retention options for this backup set:  - `LOGS` - Indicates a long-term backup made with the `LOGS` keyword, which is now deprecated - `BACKUP_LOGS` - Indicates that the backup was made in open mode, so archived log backups must be applied to make it consistent - `NOLOGS` - Indicates a consistent backup made when the database was mounted. - NULL - Indicates that this backup has no `KEEP` options and becomes obsolete based on the retention policy |
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for output bytes |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |