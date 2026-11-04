---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_CONTROLFILE_COPY.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists information about control file copies on disk.

A data file copy record with a file number of 0 represents the control file copy in `V$DATAFILE_COPY`.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `CCF_KEY` | `NUMBER` | The primary key of the control file copy in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `RECID` | `NUMBER` | The record identifier from `V$DATAFILE_COPY`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The stamp from `V$DATAFILE_COPY`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `NAME` | `VARCHAR2(1024)` | The control file copy file name. |
| `TAG` | `VARCHAR2(32)` | The tag of the control file copy. `NULL` if no tag used. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the most recent `RESETLOGS` when the record was created. |
| `RESETLOGS_TIME` | `DATE` | The time stamp of the most recent `RESETLOGS` when the record was created. |
| `CHECKPOINT_CHANGE#` | `NUMBER` | The control file checkpoint SCN. |
| `CHECKPOINT_TIME` | `DATE` | The control file checkpoint time. |
| `CREATION_TIME` | `DATE` | The control file creation time. |
| `BLOCKS` | `NUMBER` | The number of blocks in the control file. |
| `BLOCK_SIZE` | `NUMBER` | The block size in bytes. |
| `MIN_OFFR_RECID` | `NUMBER` | Internal use only. |
| `OLDEST_OFFLINE_RANGE` | `NUMBER` | Internal use only. |
| `COMPLETION_TIME` | `DATE` | The time when the copy was generated. |
| `STATUS` | `VARCHAR2(1)` | The status of the copy: `A` (available), `U` (unavailable), `X` (expired), or `D` (deleted). |
| `CONTROLFILE_TYPE` | `VARCHAR2(1)` | The type of control file copy: `B` (normal copy) or `S` (standby copy). |
| `KEEP` | `VARCHAR2(3)` | Indicates whether this copy has a retention policy different from the value for `CONFIGURE RETENTION POLICY`. Possible values are `YES` and `NO`. |
| `KEEP_UNTIL` | `DATE` | If the `KEEP UNTIL TIME` clause of the `COPY` command was specified, then this column shows the date after which this file becomes obsolete. If the column is `NULL` and `KEEP OPTIONS` is not `NULL`, the file never becomes obsolete. |
| `KEEP_OPTIONS` | `VARCHAR2(11)` | The `KEEP` options specified for this control file copy. Possible values are `NOLOGS`, `BACKUP_LOGS`, `LOGS`, and `NULL`. `NOLOGS` indicates a consistent backup made when the database was mounted. `BACKUP_LOGS` indicates that the backup was made in open mode, so archived log backups must be applied to make it consistent. `LOGS` indicates a long-term backup made with the `LOGS` keyword, which is now deprecated. `NULL` indicates that this backup has no `KEEP` options and becomes obsolete based on the retention policy. |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | This copy is located in the fast recovery area: `YES` or `NO`. |
| `RSR_KEY` | `NUMBER` | Unique key for the row in `RC_RMAN_STATUS` that created this backup piece. |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with this file. Each database in a Data Guard environment has a unique `SITE_KEY` value. You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |