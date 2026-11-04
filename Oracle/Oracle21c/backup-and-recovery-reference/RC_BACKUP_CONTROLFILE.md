---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_BACKUP_CONTROLFILE.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists information about control files in backup sets.

The `V$BACKUP_DATAFILE` view contains both data file and control file records: a backup data file record with file number `0` represents the backup control file. In the recovery catalog, the `RC_BACKUP_CONTROLFILE` view contains only control file records, while the `RC_BACKUP_DATAFILE` view contains only data file records.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `BCF_KEY` | `NUMBER` | The primary key of the control file backup in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `RECID` | `NUMBER` | The `RECID` value from `V$BACKUP_DATAFILE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The `STAMP` value from `V$BACKUP_DATAFILE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `BS_KEY` | `NUMBER` | The primary key of the backup set to which this record belongs in the recovery catalog. Use this column to join with `RC_BACKUP_SET` or `RC_BACKUP_PIECE`. |
| `SET_STAMP` | `NUMBER` | The `SET_STAMP` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `SET_COUNT` | `NUMBER` | The `SET_COUNT` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the most recent `RESETLOGS` when the record was created. |
| `RESETLOGS_TIME` | `DATE` | The time stamp of the most recent `RESETLOGS` when the record was created. |
| `CHECKPOINT_CHANGE#` | `NUMBER` | The control file checkpoint SCN. |
| `CHECKPOINT_TIME` | `DATE` | The control file checkpoint time. |
| `CREATION_TIME` | `DATE` | The control file creation time. |
| `BLOCK_SIZE` | `NUMBER` | The size of the blocks in bytes. |
| `OLDEST_OFFLINE_RANGE` | `NUMBER` | Internal use only. |
| `STATUS` | `VARCHAR2(1)` | The status of the backup set: `A` (available), `U` (unavailable), or `D` (deleted). |
| `BS_RECID` | `NUMBER` | The control file `RECID` of the backup set that contains this backup control file. |
| `BS_STAMP` | `NUMBER` | The control file stamp of the backup set that contains this control file. |
| `BS_LEVEL` | `NUMBER` | The incremental level (`NULL`, `0`, `1`) of the backup set that contains this backup control file. Although an incremental backup set can contain the control file, it is always contains a complete copy of the control file. There is no such thing as an incremental control file backup. |
| `COMPLETION_TIME` | `DATE` | The date that the control file backup completed. |
| `CONTROLFILE_TYPE` | `VARCHAR2(1)` | The type of control file backup: `B` (normal backup) or `S` (standby backup). |
| `BLOCKS` | `NUMBER` | The number of blocks in the file. |
| `AUTOBACKUP_DATE` | `DATE` | The date of the control file autobackup. |
| `AUTOBACKUP_SEQUENCE` | `NUMBER` | The sequence of the control file autobackup: 1 - 255. |