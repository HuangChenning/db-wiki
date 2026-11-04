---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_BACKUP_DATAFILE_DETAILS.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

`RC_BACKUP_DATAFILE_DETAILS` provides detailed information about available data file backups for databases registered in the recovery catalog.

This view is primarily intended to be used internally by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `BTYPE` | `CHAR(9)` | The backup type container, which can be `BACKUPSET`, `IMAGECOPY`, or `PROXYCOPY`. |
| `BTYPE_KEY` | `NUMBER` | Unique identifier for the backup type. If `BTYPE` is `BACKUPSET`, then this value is the `BS_KEY` value for the backup set. If `BTYPE` is `IMAGECOPY`, then this value is the value of `COPY_KEY` for the copy. |
| `SESSION_KEY` | `NUMBER` | Session identifier. Use in joins with `RC_RMAN_OUTPUT` and `RC_RMAN_BACKUP_JOB_DETAILS`. |
| `SESSION_RECID` | `NUMBER` | With `SESSION_STAMP`, uniquely identifies output for this backup job from `RC_RMAN_OUTPUT`. |
| `SESSION_STAMP` | `NUMBER` | With `SESSION_RECID`, uniquely identifies output for this backup job from `RC_RMAN_OUTPUT`. |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `ID1` | `NUMBER` | For backups taken as backup sets, this column contains `SET_STAMP`. For proxy copy or image copy backups, this column contains the `RECID` from the control file. |
| `ID2` | `NUMBER` | For backups taken as backup sets, this column contains `SET_COUNT`. For proxy copy or image copy backups, this column contains `STAMP`. |
| `FILE#` | `NUMBER` | The number of this data file. |
| `CREATION_CHANGE#` | `NUMBER` | The checkpoint SCN when this data file was created. |
| `CREATION_TIME` | `DATE` | The time at which this data file was created. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The checkpoint SCN of the most recent `RESETLOGS` operation affecting this data file. |
| `RESETLOGS_TIME` | `DATE` | The time of the most recent `RESETLOGS` operation affecting this data file |
| `INCREMENTAL_LEVEL` | `NUMBER` | For incremental backups, the level of the incremental backup (0 or 1). Otherwise, `NULL`. |
| `INCREMENTAL_CHANGE#` | `NUMBER` | For incremental backups, the incremental backup SCN. Otherwise, `NULL`. |
| `CHECKPOINT_CHANGE#` | `NUMBER` | The current checkpoint SCN for the data file at the time it was backed up. |
| `CHECKPOINT_TIME` | `DATE` | The time corresponding to the current checkpoint SCN for the data file at the time it was backed up. |
| `MARKED_CORRUPT` | `NUMBER` | Number of data file blocks marked corrupt. |
| `FILESIZE` | `NUMBER` | The size of the data file at the time it was backed up. |
| `COMPRESSION_RATIO` | `NUMBER` | Compression ratio for this backup. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - 0: Rows containing data that pertain to the whole multitenant container database (CDB) - 1: Rows containing data that pertains only to the root - n: Where n is the applicable container ID for the rows containing data |
| `PDB_NAME` | `VARCHAR2(31`) | Name of the pluggable database (PDB). |
| `PDB_KEY` | `NUMBER` | The primary key for this PDB in the recovery catalog. |
| `TS#` | `NUMBER` | Tablespace number. |
| `TSNAME` | `VARCHAR2(30)` | The name of the tablespace containing this data file. |
| `FILESIZE_DISPLAY` | `VARCHAR2(32K)` | Same value as `FILESIZE`, but converted to a user-displayable format, for example, 798.01M or 5.25G. |