---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_BACKUP_ARCHIVELOG_DETAILS.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

`RC_BACKUP_ARCHIVELOG_DETAILS` provides detailed information about backups of archived redo log files.

This view is primarily intended to be used internally by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `BTYPE` | `CHAR(9)` | The backup type container, which can be `BACKUPSET`, `IMAGECOPY`, or `PROXYCOPY`. |
| `BTYPE_KEY` | `NUMBER` | A unique identifier for the backup type. For backup sets, it is `VS_KEY`; for image copies, it is `COPY_KEY`; for proxy copies it is `XAL_KEY`. |
| `SESSION_KEY` | `NUMBER` | Unique identifier for this session. Use for joins with `RC_RMAN_BACKUP_JOB_DETAILS`. |
| `SESSION_RECID` | `NUMBER` | The `RECID` from the control file for the target database which corresponds to this RMAN session. |
| `SESSION_STAMP` | `NUMBER` | The `STAMP` from the control file for the target database which corresponds to this RMAN session. |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `ID1` | `NUMBER` | For archived logs in backup sets, this column contains `SET_STAMP`. For proxy copy or image copy backups, this column contains the `RECID` from the control file. |
| `ID2` | `NUMBER` | For archived logs in backup sets, this column contains `SET_COUNT`. For image copy or proxy copy backups, this column contains `STAMP`. |
| `THREAD#` | `NUMBER` | Thread number of this archived redo log file. |
| `SEQUENCE#` | `NUMBER` | Sequence number of this archived redo log file. |
| `RESETLOGS_CHANGE#` | `NUMBER` | SCN of `OPEN RESETLOGS` branch for this archived log. |
| `RESETLOGS_TIME` | `DATE` | Time of `OPEN RESETLOGS` branch for this archived log. |
| `FIRST_CHANGE#` | `NUMBER` | Starting SCN for this archived log file. |
| `FIRST_TIME` | `DATE` | Time corresponding to starting SCN for this archived redo log file. |
| `NEXT_CHANGE#` | `NUMBER` | Ending SCN for this archived redo log file. |
| `NEXT_TIME` | `DATE` | Time corresponding to the ending SCN for this archived redo log file. |
| `FILESIZE` | `NUMBER` | Size of backed up redo log file, in bytes. |
| `COMPRESSION_RATIO` | `NUMBER` | Compression ratio for this backup. |
| `FILESIZE_DISPLAY` | `VARCHAR2(32K)` | Same value as `FILESIZE`, but converted to a user-displayable format, for example, 798.01M or 5.25G. |