---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_BACKUP_PIECE_DETAILS.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

`RC_BACKUP_PIECE_DETAILS` contains detailed information about all available backup pieces recorded in the recovery catalog.

The semantics of most columns duplicate the `RC_BACKUP_PIECE` recovery catalog view. This view is primarily intended to be used internally by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `SESSION_KEY` | `NUMBER` | Session identifier. Use in joins with `RC_RMAN_OUTPUT ` and `RC_RMAN_BACKUP_JOB_DETAILS`. |
| `SESSION_RECID` | `NUMBER` | With `SESSION_STAMP`, uniquely identifies output for this backup job from `RC_RMAN_OUTPUT`. |
| `SESSION_STAMP` | `NUMBER` | With `SESSION_RECID`, uniquely identifies output for this backup job from `RC_RMAN_OUTPUT`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DB_ID` | `NUMBER` | The DBID of the database incarnation to which this record belongs. |
| `BP_KEY` | `NUMBER` | The primary key for the backup piece in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `RECID` | `NUMBER` | The backup piece `RECID` from `RC_BACKUP_PIECE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The backup piece stamp propagated from `V$BACKUP_PIECE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `BS_KEY` | `NUMBER` | The primary key of the backup set to which this record belongs in the recovery catalog. Use this column to join with `RC_BACKUP_SET` or `RC_BACKUP_PIECE`. |
| `SET_STAMP` | `NUMBER` | The `SET_STAMP` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `SET_COUNT` | `NUMBER` | The `SET_COUNT` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `BACKUP_TYPE` | `VARCHAR2(1)` | The type of backup. Possible values are `D` for data file or control file backups, `I` for incremental backups, and `L` for archived log file backups. |
| `INCREMENTAL_LEVEL` | `NUMBER` | For incremental backups, indicates the level of incremental backup. Possible values are `NULL` (for full backups), `0` or `1`. |
| `PIECE#` | `NUMBER` | The number of the backup piece. The first piece has the value of 1. |
| `COPY#` | `NUMBER` | Indicates the copy number for backup pieces created with duplex enabled. 1 if the backup piece is not duplexed. |
| `DEVICE_TYPE` | `VARCHAR2(255)` | Type of the device on which the backup piece resides. Set to `DISK` for backup sets on disk. |
| `HANDLE` | `VARCHAR2(1024)` | The file name of the backup piece. |