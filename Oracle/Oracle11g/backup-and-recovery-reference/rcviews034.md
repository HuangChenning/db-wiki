---
title: RC_PROXY_ARCHIVEDLOG
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews034.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

This view contains descriptions of archived log backups that were taken using the proxy copy functionality. It corresponds to the `V$PROXY_ARCHIVEDLOG` view.

In a proxy copy, the media manager takes over the operations of backing up and restoring data. Each row represents a backup of one control file.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `XAL_KEY` | `NUMBER` | The proxy copy primary key in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `RECID` | `NUMBER` | The proxy copy record identifier from `V$PROXY_ARCHIVEDLOG`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The proxy copy stamp from `V$PROXY_ARCHIVEDLOG`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `TAG` | `VARCHAR2(32)` | The tag for the proxy copy. |
| `DEVICE_TYPE` | `VARCHAR2(255)` | The type of media device that stores the proxy copy. |
| `HANDLE` | `VARCHAR2(1024)` | The name or "handle" for the proxy copy. RMAN passes this value to the media manager that created the proxy copy of the archived redo log. |
| `COMMENTS` | `VARCHAR2(255)` | Comments about the proxy copy. |
| `MEDIA` | `VARCHAR2(80)` | A comment that contains further information about the media manager that created this backup. |
| `MEDIA_POOL` | `NUMBER` | The number of the media pool in which the proxy copy is stored. |
| `STATUS` | `VARCHAR2(1)` | The status of the backup set: `A` (available), `U` (unavailable), `X` (expired), or `D` (deleted). |
| `THREAD#` | `NUMBER` | The number of the redo thread. |
| `SEQUENCE#` | `NUMBER` | The log sequence number. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The `RESETLOGS` SCN of the database incarnation to which this archived log belongs. |
| `RESETLOGS_TIME` | `DATE` | The `RESETLOGS` time stamp of the database incarnation to which this archived log belongs. |
| `FIRST_CHANGE#` | `NUMBER` | The first SCN of this redo log. |
| `FIRST_TIME` | `DATE` | The time when Oracle switched into the redo log. |
| `NEXT_CHANGE#` | `NUMBER` | The first SCN of the next redo log in the thread. |
| `NEXT_TIME` | `DATE` | The first time stamp of the next redo log in the thread. |
| `BLOCKS` | `NUMBER` | The size of this archived redo log in operating system blocks. |
| `BLOCK_SIZE` | `NUMBER` | The block size for the copy in bytes. |
| `DEVICE_TYPE` | `VARCHAR2(255)` | The type of sequential media device. |
| `START_TIME` | `DATE` | The time when proxy copy was initiated. |
| `COMPLETION_TIME` | `DATE` | The time when the proxy copy was completed. |
| `ELAPSED_SECONDS` | `NUMBER` | The duration of the proxy copy. |
| `RSR_KEY` | `NUMBER` | The primary key from the RMAN status record. Use this column to perform a join with `RC_RMAN_STATUS`. |
| `TERMINAL` | `VARCHAR2(3)` | `YES` if this record corresponds to a terminal archived redo log, as defined in `V$ARCHIVED_LOG`. |
| `KEEP` | `VARCHAR2(3)` | Indicates whether this proxy copy has a retention policy different from the value for `CONFIGURE RETENTION POLICY`. Possible values are `YES` and `NO`. |
| `KEEP_OPTIONS` | `VARCHAR2(11)` | The `KEEP` options specified for this proxy copy. Possible values are `NOLOGS`, `BACKUP_LOGS`, `LOGS`, and `NULL`. `NOLOGS` indicates a consistent backup made when the database was mounted. `BACKUP_LOGS` indicates that the backup was made in open mode, so archived log backups must be applied to make it consistent. `LOGS` indicates a long-term backup made with the `LOGS` keyword, which is now deprecated. `NULL` indicates that this backup has no `KEEP` options and becomes obsolete based on the retention policy. |
| `KEEP_UNTIL` | `DATE` | If the `KEEP UNTIL TIME` clause of the `BACKUP` command was specified, then this column shows the date after which this proxy copy becomes obsolete. If the column is `NULL` and `KEEP OPTIONS` is not `NULL`, then the proxy copy never becomes obsolete. |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with this file. Each database in a Data Guard environment has a unique `SITE_KEY` value. You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |