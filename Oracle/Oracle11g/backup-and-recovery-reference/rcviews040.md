---
title: RC_PROXY_DATAFILE
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews040.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

This view contains descriptions of data file backups that were taken using the proxy copy functionality. It corresponds to the `V$PROXY_DATAFILE` view.

In a proxy copy, the media manager takes over the operations of backing up and restoring data. Each row represents a backup of one database file.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `XDF_KEY` | `NUMBER` | The proxy copy primary key in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `RECID` | `NUMBER` | The proxy copy record identifier from `V$PROXY_DATAFILE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The proxy copy stamp from `V$PROXY_DATAFILE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `TAG` | `VARCHAR2(32)` | The tag for the proxy copy. |
| `FILE#` | `NUMBER` | The absolute file number of the data file that is proxy copied. |
| `CREATION_CHANGE#` | `NUMBER` | The data file creation SCN. |
| `CREATION_TIME` | `DATE` | The data file creation time. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the most recent `RESETLOGS` in the data file header. |
| `RESETLOGS_TIME` | `DATE` | The time stamp of the most recent `RESETLOGS` in the data file header. |
| `INCREMENTAL_LEVEL` | `NUMBER` | 0 if this copy is part of an incremental backup strategy, otherwise `NULL`. |
| `CHECKPOINT_CHANGE#` | `NUMBER` | Checkpoint SCN when the copy was made. |
| `CHECKPOINT_TIME` | `DATE` | Checkpoint time when the copy was made. |
| `ABSOLUTE_FUZZY_CHANGE#` | `NUMBER` | The highest SCN in any block of the file, if known. Recovery must proceed to at least this SCN for the file to become not fuzzy. |
| `RECOVERY_FUZZY_CHANGE#` | `NUMBER` | The SCN to which recovery must proceed for the file to become not fuzzy. If not `NULL`, this file must be recovered at least to the specified SCN before the database can be opened with this file. |
| `RECOVERY_FUZZY_TIME` | `DATE` | The time that is associated with the `RECOVERY_FUZZY_CHANGE#`. |
| `ONLINE_FUZZY` | `VARCHAR2(3)` | `YES` / `NO`. If set to `YES`, this copy was made after an instance failure or `OFFLINE IMMEDIATE` (or is a copy of a copy which was taken improperly while the database was open). Recovery must apply all redo up to the next crash recovery marker to make the file consistent. |
| `BACKUP_FUZZY` | `VARCHAR2(3)` | `YES` / `NO`. If set to `YES`, this is a copy taken using the `BEGIN BACKUP` / `END BACKUP` backup method. To make this copy consistent, recovery must apply all redo up to the marker that is placed in the redo stream when the `ALTER TABLESPACE END BACKUP` statement is issued. |
| `BLOCKS` | `NUMBER` | Size of the data file copy in blocks (also the size of the data file when the copy was made). |
| `BLOCK_SIZE` | `NUMBER` | The block size for the copy in bytes. |
| `DEVICE_TYPE` | `VARCHAR2(255)` | The type of sequential media device. |
| `HANDLE` | `VARCHAR2(1024)` | The name or "handle" for the proxy copy. RMAN passes this value to the operating system-dependent layer that identifies the file. |
| `COMMENTS` | `VARCHAR2(255)` | Comments about the proxy copy. |
| `MEDIA` | `VARCHAR2(80)` | A comment that contains further information about the media manager that created this backup. |
| `MEDIA_POOL` | `NUMBER` | The number of the media pool in which the proxy copy is stored. |
| `START_TIME` | `DATE` | The time when proxy copy was initiated. |
| `COMPLETION_TIME` | `DATE` | The time when the proxy copy was completed. |
| `ELAPSED_SECONDS` | `NUMBER` | The duration of the proxy copy. |
| `STATUS` | `VARCHAR2(1)` | The status of the backup set: `A` (available), `U` (unavailable), `X` (expired), or `D` (deleted). |
| `KEEP` | `VARCHAR2(3)` | Indicates whether this proxy copy has a retention policy different from the value for `CONFIGURE RETENTION POLICY` (`YES` or `NO`). |
| `KEEP_UNTIL` | `DATE` | If the `KEEP UNTIL TIME` clause of the `BACKUP` command was specified, then this column shows the date after which this data file backup becomes obsolete. If the column is `NULL` and `KEEP` `OPTIONS` is not `NULL`, the backup never becomes obsolete. |
| `KEEP_OPTIONS` | `VARCHAR2(11)` | The `KEEP` options specified for this backup. Possible values are `NOLOGS`, `BACKUP_LOGS`, `LOGS`, and `NULL`. `NOLOGS` indicates a consistent backup made when the database was mounted. `BACKUP_LOGS` indicates that the backup was made in open mode, so archived log backups must be applied to make it consistent. `LOGS` indicates a long-term backup made with the `LOGS` keyword, which is now deprecated. `NULL` indicates that this backup has no `KEEP` options and becomes obsolete based on the retention policy. |
| `RSR_KEY` | `NUMBER` | Unique key for the row in `RC_RMAN_STATUS` corresponding to the job that created this proxy copy. |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with this file. Each database in a Data Guard environment has a unique `SITE_KEY` value. You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |
| `FOREIGN_DBID` | `NUMBER` | Foreign DBID of the database from which this data file was transported. The value is `0` if the file backed up is not a foreign database file. |
| `PLUGGED_READONLY` | `VARCHAR2(3)` | `YES` if this is a proxy copy of a transported read-only foreign file; otherwise `NO`. |
| `PLUGIN_CHANGE#` | `NUMBER` | SCN at which the foreign data file was transported into the database. The value is `0` if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is `0` if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_TIME` | `DATE` | The time of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is `0` if this file is not a foreign database file. |