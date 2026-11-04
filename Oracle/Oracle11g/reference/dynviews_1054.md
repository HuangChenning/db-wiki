---
title: "V$BACKUP_DATAFILE_DETAILS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1054.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BACKUP_DATAFILE_DETAILS` contains information about restorable datafiles. It will include all datafiles backed in the backup set, image copies, and proxy copies.

| Column | Datatype | Description |
| --- | --- | --- |
| `BTYPE` | `CHAR(9)` | Backup type container. Possible values are: `BACKUPSET`, `IMAGECOPY`, `PROXYCOPY`. |
| `BTYPE_KEY` | `NUMBER` | Unique identifier for the backup type. For `BACKUPSET`, it is `BS_KEY`. |
| `SESSION_KEY` | `NUMBER` | Session identifier |
| `SESSION_RECID` | `NUMBER` | Session record ID |
| `SESSION_STAMP` | `NUMBER` | Session stamp |
| `ID1` | `NUMBER` | If `BACKUPSET`, it contains `SET_STAMP`.  If `IMAGECOPY` or `PROXYCOPY`, it is `RECID` from the control file. |
| `ID2` | `NUMBER` | If `BACKUPSET`, it contains `SET_COUNT`.  If `IMAGECOPY` or `PROXYCOPY`, it is `STAMP`. |
| `FILE#` | `NUMBER` | File number |
| `CREATION_CHANGE#` | `NUMBER` | File creation change SCN |
| `CREATION_TIME` | `DATE` | File creation time |
| `RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs change SCN |
| `RESETLOGS_TIME` | `DATE` | Resetlogs change time |
| `INCREMENTAL_LEVEL` | `NUMBER` | Normal full backups have a NULL value, level 0 incremental backups have a value of 0, and level 1 incremental backups have a value of 1 |
| `INCREMENTAL_CHANGE#` | `NUMBER` | Incremental change SCN |
| `CHECKPOINT_CHANGE#` | `NUMBER` | Checkpoint change SCN |
| `CHECKPOINT_TIME` | `DATE` | Checkpoint change time |
| `MARKED_CORRUPT` | `NUMBER` | Number of blocks marked corrupt |
| `FILESIZE` | `NUMBER` | File size, in bytes |
| `COMPRESSION_RATIO` | `NUMBER` | The ratio between the total blocks in the datafile and the blocks that RMAN backed up. This is not the the ratio from the `AS COMPRESSED BACKUPSET` clause of the `BACKUP` command. |
| `TS#` | `NUMBER` | Tablespace number |
| `TSNAME` | `VARCHAR2(30)` | Tablespace name |
| `FILESIZE_DISPLAY` | `VARCHAR2(4000)` | Same value as the `FILESIZE` column, but converted to a user-displayable format, for example `n` M, `n` G, `n` T, `n` P, and so on |