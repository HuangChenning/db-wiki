---
title: RC_PROXY_CONTROLFILE
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews037.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

This view contains descriptions of control file backups that were taken using the proxy copy functionality. It corresponds to the `V$PROXY_DATAFILE` view.

In a proxy copy, the media manager takes over the operations of backing up and restoring data. Each row represents a backup of one control file.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `XCF_KEY` | `NUMBER` | The proxy copy primary key in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `RECID` | `NUMBER` | The proxy copy record identifier from `V$PROXY_DATAFILE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The proxy copy stamp from `V$PROXY_DATAFILE`.`RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `TAG` | `VARCHAR2(32)` | The tag for the proxy copy. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The `RESETLOGS` SCN of the database incarnation to which this data file belongs. |
| `RESETLOGS_TIME` | `DATE` | The `RESETLOGS` time stamp of the database incarnation to which this data file belongs. |
| `CHECKPOINT_CHANGE#` | `NUMBER` | Data file checkpoint SCN when this copy was made. |
| `CHECKPOINT_TIME` | `DATE` | Data file checkpoint time when this copy was made. |
| `CREATION_TIME` | `DATE` | The control file creation time. |
| `BLOCK_SIZE` | `NUMBER` | The block size for the copy in bytes. |
| `BLOCKS` | `NUMBER` | The number of blocks in the copy. |
| `MIN_OFFR_RECID` | `NUMBER` | Internal use only. |
| `OLDEST_OFFLINE_RANGE` | `NUMBER` | Internal use only. |
| `DEVICE_TYPE` | `VARCHAR2(255)` | The type of sequential media device. |
| `HANDLE` | `VARCHAR2(1024)` | The name or "handle" for the proxy copy. RMAN passes this value to the operating system-dependent layer that identifies the file. |
| `COMMENTS` | `VARCHAR2(255)` | Comments about the proxy copy. |
| `MEDIA` | `VARCHAR2(80)` | A comment that contains further information about the media manager that created this backup. |
| `MEDIA_POOL` | `NUMBER` | The number of the media pool in which the proxy copy is stored. |
| `START_TIME` | `DATE` | The time when proxy copy was initiated. |
| `COMPLETION_TIME` | `DATE` | The time when the proxy copy was completed. |
| `ELAPSED_SECONDS` | `NUMBER` | The duration of the proxy copy. |
| `STATUS` | `VARCHAR2(1)` | The status of the backup set: `A` (available), `U` (unavailable), `X` (expired), or `D` (deleted). |
| `KEEP` | `VARCHAR2(3)` | Indicates whether this proxy copy has a retention policy different from the value for `CONFIGURE RETENTION POLICY`. Possible values are `YES` and `NO`. |
| `KEEP_OPTIONS` | `VARCHAR2(11)` | The `KEEP` options specified for this control file backup. Possible values are `NOLOGS`, `BACKUP_LOGS`, `LOGS`, and `NULL`. `NOLOGS` indicates a consistent backup made when the database was mounted. `BACKUP_LOGS` indicates that the backup was made in open mode, so archived log backups must be applied to make it consistent. `LOGS` indicates a long-term backup made with the `LOGS` keyword, which is now deprecated. `NULL` indicates that this backup has no `KEEP` options and becomes obsolete based on the retention policy. |
| `KEEP_UNTIL` | `DATE` | If the `KEEP UNTIL TIME` clause of the `BACKUP` command was specified, then this column shows the date after which this control file backup becomes obsolete. If the column is `NULL` and `KEEP OPTIONS` is not `NULL`, the backup never becomes obsolete. |
| `CONTROLFILE_TYPE` | `VARCHAR2(1)` | The type of control file copy: `B` (normal copy) or `S` (standby copy). |
| `RSR_KEY` | `NUMBER` | Unique key for the row in `RC_RMAN_STATUS` that created this backup piece. |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with this file. Each database in a Data Guard environment has a unique `SITE_KEY` value. You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |