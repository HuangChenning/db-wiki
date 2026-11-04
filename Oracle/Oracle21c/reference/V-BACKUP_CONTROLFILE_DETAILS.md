---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_CONTROLFILE_DETAILS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.86 V$BACKUP\_CONTROLFILE\_DETAILS

`V$BACKUP_CONTROLFILE_DETAILS` contains information about restorable control files.

It will include all the control files backed up in the backup set, image copies, and proxy copies.

| Column | Datatype | Description |
| --- | --- | --- |
| `BTYPE` | `CHAR(9)` | Backup type container. Possible values are `BACKUPSET`, `IMAGECOPY`, `PROXYCOPY`. |
| `BTYPE_KEY` | `NUMBER` | Unique identifier for the backup type, either `BS_KEY` or `COPY_KEY`. |
| `SESSION_KEY` | `NUMBER` | Session identifier |
| `SESSION_RECID` | `NUMBER` | Session recid |
| `SESSION_STAMP` | `NUMBER` | Session stamp |
| `ID1` | `NUMBER` | If `BACKUPSET`, it contains `SET_STAMP`  If `IMAGECOPY` or `PROXYCOPY`, it is `RECID` from the control file |
| `ID2` | `NUMBER` | If `BACKUPSET`, it contains `SET_COUNT`  If `IMAGECOPY` or `PROXYCOPY`, it is `STAMP` |
| `CREATION_TIME` | `DATE` | File creation time |
| `RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs change SCN |
| `RESETLOGS_TIME` | `DATE` | Resetlogs change time |
| `CHECKPOINT_CHANGE#` | `NUMBER` | Checkpoint change SCN |
| `CHECKPOINT_TIME` | `DATE` | Checkpoint change time |
| `FILESIZE` | `NUMBER` | File size, in bytes, for the output of backing up this control file |
| `COMPRESSION_RATIO` | `NUMBER` | The ratio between the total blocks in the datafile and the blocks that RMAN backed up. This is not the the ratio from the `AS COMPRESSED BACKUPSET` clause of the `BACKUP` command. |
| `FILESIZE_DISPLAY` | `VARCHAR2(4000)` | Same value as the `FILESIZE` column, but converted to a user-displayable format, for example `n` M, `n` G, `n` T, `n` P, and so on |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |