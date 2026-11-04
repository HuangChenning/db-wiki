---
title: RC_BACKUP_PIECE_DETAILS
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews016.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

`RC_BACKUP_PIECE_DETAILS` contains detailed information about all available backup pieces recorded in the recovery catalog. The semantics of most columns are the same as for the `RC_BACKUP_PIECE` recovery catalog view.

This view is primarily intended to be used internally by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `SESSION_KEY` | `NUMBER` | Session identifier. Use in joins with `RC_RMAN_OUTPUT` and `RC_RMAN_BACKUP_JOB_DETAILS`. |
| `SESSION_RECID` | `NUMBER` | Together with `SESSION_STAMP`, uniquely identifies output for this backup job from `RC_RMAN_OUTPUT`. |
| `SESSION_STAMP` | `NUMBER` | Together with `SESSION_RECID`, uniquely identifies output for this backup job from `RC_RMAN_OUTPUT`. |
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
| `COMMENTS` | `VARCHAR2(255)` | Comments about the backup piece. |
| `MEDIA` | `VARCHAR2(80)` | A comment that contains further information about the media manager that created this backup. |
| `MEDIA_POOL` | `NUMBER` | The number of the media pool in which the backup is stored. `0` indicates no media pool. |
| `CONCUR` | `VARCHAR2(3)` | Specifies whether backup media supports concurrent access: `YES` or `NO`. |
| `TAG` | `VARCHAR2(32)` | The tag associated with this backup piece. |
| `START_TIME` | `DATE` | The time when RMAN started to write the backup piece. |
| `COMPLETION_TIME` | `DATE` | The time when the backup piece was completed. |
| `ELAPSED_SECONDS` | `NUMBER` | The duration of the creation of the backup piece. |
| `STATUS` | `VARCHAR2(1)` | The status of the backup piece: `A` for backup pieces that are `AVAILABLE`. (The value is always `A`, because this view shows only available backup pieces.) |
| `BYTES` | `NUMBER` | The size of the backup piece in bytes. |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | `YES` if this backup piece is located in the fast recovery area. `NO` otherwise. |
| `RSR_KEY` | `NUMBER` | Unique key for the row in `RC_RMAN_STATUS` corresponding to the job that created this backup piece. |
| `COMPRESSED` | `VARCHAR2(3)` | `YES` if this backup piece is compressed. `NO` otherwise. |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with this file. Each database in a Data Guard environment has a unique `SITE_KEY` value.You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |
| `ENCRYPTED` | `VARCHAR2(3)` | Indicates whether the backup piece is encrypted (`YES`) or not (`NO`). |
| `BACKED_BY_OSB` | `VARCHAR2(3)` | Indicates whether the backup piece is backed up to Oracle Secure Backup (`YES`) or not (`NO`). |
| `PIECES_PER_SET` | `NUMBER` | Number of backup pieces in the backup set containing this backup piece. |
| `SIZE_BYTES_DISPLAY` | `VARCHAR2(4000)` | Same value as `BYTES`, but converted to a user-displayable format, for example, 798.01M or 5.25G. |