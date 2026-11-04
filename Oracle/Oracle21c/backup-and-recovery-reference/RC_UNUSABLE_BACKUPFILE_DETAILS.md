---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_UNUSABLE_BACKUPFILE_DETAILS.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists all backup files (backup pieces, proxy copies or image copies) that are marked `UNAVAILABLE` or `EXPIRED`.

You can select a row and, using `BTYPE_KEY` or `FILETYPE_KEY`, change the status of a backup set or specific file to `AVAILABLE`. This view is primarily intended to be used internally by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `SESSION_KEY` | `NUMBER` | Session identifier. Use in joins with `RC_RMAN_OUTPUT` and `RC_RMAN_BACKUP_JOB_DETAILS`. |
| `RSR_KEY` | `NUMBER` | Unique key for the row in `RC_RMAN_STATUS` corresponding to the job that created this file. |
| `BTYPE` | `CHAR(9)` | The backup type container, which can be `BACKUPSET`, `IMAGECOPY`, or `PROXYCOPY`. |
| `BTYPE_KEY` | `NUMBER` | Unique identifier for the backup type. It is `BS_KEY` / `COPY_KEY`. |
| `ID1` | `NUMBER` | For backups taken as backup sets, this column contains `SET_STAMP`. For proxy copy or image copy backups, this column contains the `RECID` from the control file. |
| `ID2` | `NUMBER` | For backups taken as backup sets, `ID2` contains `SET_COUNT`. For image copy and proxy copy backups `ID2` contains `STAMP`. |
| `FILETYPE` | `VARCHAR2(15)` | The type of this backup file. Possible values are `BACKUPPIECE`, `COPY`, or `PROXYCOPY`. |
| `FILETYPE_KEY` | `NUMBER` | Backup piece key if the file is a backup piece, otherwise `COPY_KEY`. You can use this key to directly change the status of the file to available. |
| `STATUS` | `VARCHAR2(1)` | Can be either `U` (for unavailable backups) or `X` (for expired backups). |
| `FILESIZE` | `NUMBER` | Size in bytes of the unusable backup file. |
| `DEVICE_TYPE` | `VARCHAR2(255)` | Device type storing this unusable backup file. Possible values are `DISK` and `SBT_TAPE`. |
| `FILENAME` | `VARCHAR2(1024)` | File name. |
| `MEDIA` | `VARCHAR2(80)` | A comment that contains further information about the media manager that created this backup. |
| `MEDIA_POOL` | `NUMBER` | The number of the media pool in which the backup is stored. |