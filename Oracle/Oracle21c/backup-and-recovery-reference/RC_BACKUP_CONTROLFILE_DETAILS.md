---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_BACKUP_CONTROLFILE_DETAILS.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

`RC_BACKUP_CONTROLFILE_DETAILS` provides detailed information about control file backups that can be restored, including backups in control file image copies, backup sets, and proxy copies.

This view is primarily intended to be used internally by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `BTYPE` | `CHAR(9)` | The type of this control file backup. Possible values are `BACKUPSET`, `IMAGECOPY` or `PROXYCOPY`. |
| `BTYPE_KEY` | `NUMBER` | Unique identifier for the backup type. If `BTYPE` is `BACKUPSET`, then this value is the `BS_KEY` value for the backup set. If `BTYPE` is `IMAGECOPY`, this value is the value of `COPY_KEY` for the copy. If `BTYPE` is `PROXYCOPY`, this is the value of `XCF_KEY` for the proxy copy. |
| `SESSION_KEY` | `NUMBER` | Session identifier. Use in joins with `RC_RMAN_OUTPUT` and `RC_RMAN_BACKUP_JOB_DETAILS`. |
| `SESSION_RECID` | `NUMBER` | The `RECID` from the control file for the target database which corresponds to this RMAN session. |
| `SESSION_STAMP` | `NUMBER` | The `STAMP` from the control file for the target database which corresponds to this RMAN session. |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `ID1` | `NUMBER` | For backups taken as backup sets, this column contains `SET_STAMP`. For proxy copy or image copy backups, this column contains the `RECID` from the control file. |
| `ID2` | `NUMBER` | For backups taken as backup sets, this column contains `SET_COUNT`. For proxy copy or image copy backups, this column contains the value of `STAMP`. |
| `CREATION_TIME` | `DATE` | File creation time for the control file that was backed up. |
| `RESETLOGS_CHANGE#` | `NUMBER` | SCN of the `RESETLOGS` branch where this control file was backed up. |
| `RESETLOGS_TIME` | `DATE` | Time of the `RESETLOGS` branch where this control file was backed up. |
| `CHECKPOINT_CHANGE#` | `NUMBER` | Most recent checkpoint change SCN for the control file that was backed up. |
| `CHECKPOINT_TIME` | `DATE` | Most recent checkpoint time for the control file that was backed up. |
| `FILESIZE` | `NUMBER` | File size, in bytes, for the output of backing up this control file. |
| `COMPRESSION_RATIO` | `NUMBER` | Compression ratio for this backup. |
| `FILESIZE_DISPLAY` | `VARCHAR2(32K)` | Same value as the `FILESIZE` column, but converted to a user-displayable format, for example, 798.01M or 5.25G. |