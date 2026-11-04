---
title: RC_BACKUP_SET
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews018.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

This view lists information about backup sets for all incarnations of the database. It corresponds to the `V$BACKUP_SET` view. A backup set record is inserted after the backup has successfully completed.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DB_ID` | `NUMBER` | The unique database identifier. |
| `BS_KEY` | `NUMBER` | The primary key of the backup set in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. Use this column to join with `RC_BACKUP_PIECE`. |
| `RECID` | `NUMBER` | The backup set `RECID` from `V$BACKUP_SET`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. Use either `RECID` and `STAMP` or `SET_STAMP` and `SET_COUNT` to access `V$BACKUP_SET`. |
| `STAMP` | `NUMBER` | The backup set `STAMP` from `V$BACKUP_SET`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. Use either `RECID` and `STAMP` or `SET_STAMP` and `SET_COUNT` to access `V$BACKUP_SET`. |
| `SET_STAMP` | `NUMBER` | The `SET_STAMP` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies this record in the target database control file. Use either `RECID` and `STAMP` or `SET_STAMP` and `SET_COUNT` to access `V$BACKUP_SET`. |
| `SET_COUNT` | `NUMBER` | The `SET_COUNT` value from `V$BACKUP_SET`.`SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies this record in the target database control file. Use either `RECID` and `STAMP` or `SET_STAMP` and `SET_COUNT` to access `V$BACKUP_SET`. |
| `BACKUP_TYPE` | `VARCHAR2(1)` | The type of the backup: `D` (full backup or level 0 incremental), `I` (incremental level 1), `L` (archived redo log). |
| `INCREMENTAL_LEVEL` | `NUMBER` | The level of the incremental backup: `NULL,` 0, or 1. |
| `PIECES` | `NUMBER` | The number of backup pieces in the backup set. |
| `START_TIME` | `DATE` | The time when the backup began. |
| `COMPLETION_TIME` | `DATE` | The time when the backup completed. |
| `ELAPSED_SECONDS` | `NUMBER` | The duration of the backup in seconds. |
| `STATUS` | `VARCHAR2(1)` | The status of the backup set: `A` (all backup pieces available), `D` (all backup pieces deleted), `O` (some backup pieces are available but others are not, so the backup set is unusable). |
| `CONTROLFILE_INCLUDED` | `VARCHAR2(7)` | Possible values are `NONE` (backup set does not include a backup control file), `BACKUP` (backup set includes a normal backup control file), and `STANDBY` (backup set includes a standby control file). |
| `INPUT_FILE_SCAN_ONLY` | `VARCHAR2(3)` | This backup set record was created by the `BACKUP` `VALIDATE` command. No real backup set exists. This record is only a placeholder used to keep track of which data files were scanned and which corrupt blocks (if any) were found in those files.  If `COMPATIBLE` is set to 11.0.0 or greater, then RMAN does not populate this column. |
| `KEEP` | `VARCHAR2(3)` | Indicates whether this backup set has a retention policy different from the value for `CONFIGURE RETENTION POLICY`. Possible values are `YES` and `NO`. |
| `KEEP_UNTIL` | `DATE` | If the `KEEP UNTIL TIME` clause of the `BACKUP` command was specified, then this column shows the date after which this backup becomes obsolete. If the column is `NULL` and `KEEP OPTIONS` is not `NULL`, then the backup never becomes obsolete. |
| `KEEP_OPTIONS` | `VARCHAR2(11)` | The `KEEP` options specified for this backup set. Possible values are `NOLOGS`, `BACKUP_LOGS`, `LOGS`, and `NULL`. `NOLOGS` indicates a consistent backup made when the database was mounted. `BACKUP_LOGS` indicates that the backup was made in open mode, so archived log backups must be applied to make it consistent. `LOGS` indicates a long-term backup made with the `LOGS` keyword, which is now deprecated. `NULL` indicates that this backup has no `KEEP` options and becomes obsolete based on the retention policy. |
| `BLOCK_SIZE` | `NUMBER` | Block size of the backup set. |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with this backup set. Each database in a Data Guard environment has a unique `SITE_KEY` value.You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |
| `MULTI_SECTION` | `VARCHAR2(3)` | `Y` if this is a multisection backup; otherwise null. |