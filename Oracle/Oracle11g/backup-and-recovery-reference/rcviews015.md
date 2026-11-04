---
title: RC_BACKUP_PIECE
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews015.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

This view lists information about backup pieces. This view corresponds to the `V$BACKUP_PIECE` view. Each backup set contains one or more backup pieces.

Multiple copies of the same backup piece can exist, but each copy has its own record in the control file and its own row in the view.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DB_ID` | `NUMBER` | The database identifier. |
| `BP_KEY` | `NUMBER` | The primary key for the backup piece in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `RECID` | `NUMBER` | The backup piece `RECID` from `V$BACKUP_PIECE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The backup piece stamp propagated from `V$BACKUP_PIECE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `BS_KEY` | `NUMBER` | The primary key of the backup set to which this record belongs in the recovery catalog. Use this column to join with `RC_BACKUP_SET`, `RC_BACKUP_CONTROLFILE`, `RC_BACKUP_DATAFILE`, and so on. |
| `SET_STAMP` | `NUMBER` | The `SET_STAMP` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `SET_COUNT` | `NUMBER` | The `SET_COUNT` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `BACKUP_TYPE` | `VARCHAR2(1)` | The type of the backup: `D` (full or level 0 incremental), `I` (incremental level 1), `L` (archived redo log). |
| `INCREMENTAL_LEVEL` | `NUMBER` | The level of the incremental backup: `NULL,` 0, or 1. |
| `PIECE#` | `NUMBER` | The number of the backup piece. The first piece has the value of 1. |
| `COPY#` | `NUMBER` | The copy number of the backup piece. |
| `DEVICE_TYPE` | `VARCHAR2(255)` | The type of backup device, for example, `DISK`. |
| `HANDLE` | `VARCHAR2(1024)` | The file name of the backup piece. |
| `COMMENTS` | `VARCHAR2(255)` | Comments about the backup piece. |
| `MEDIA` | `VARCHAR2(80)` | A comment that contains further information about the media manager that created this backup. |
| `MEDIA_POOL` | `NUMBER` | The number of the media pool in which the backup is stored. |
| `CONCUR` | `VARCHAR2(3)` | Specifies whether backup media supports concurrent access: `YES` or `NO`. |
| `TAG` | `VARCHAR2(32)` | The tag for the backup piece. Refer to description in [BACKUP](rcmsynta007.md) for default format for tag names. |
| `START_TIME` | `DATE` | The time when RMAN started to write the backup piece. |
| `COMPLETION_TIME` | `DATE` | The time when the backup piece was completed. |
| `ELAPSED_SECONDS` | `NUMBER` | The duration of the creation of the backup piece. |
| `STATUS` | `VARCHAR2(1)` | The status of the backup piece: `A` (available), `U` (unavailable), `D` (deleted), or `X` (expired). Status `D` does not appear unless an older recovery catalog is upgraded. |
| `BYTES` | `NUMBER` | The size of the backup piece in bytes. |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | This backup piece is located in the fast recovery area: `YES` or `NO`. |
| `RSR_KEY` | `NUMBER` | Unique key for the row in `RC_RMAN_STATUS` that created this backup piece. |
| `COMPRESSED` | `VARCHAR2(3)` | Indicates whether the backup piece is compressed (`YES`) or not (`NO`). |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with this file. Each database in a Data Guard environment has a unique `SITE_KEY` value. You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |
| `ENCRYPTED` | `VARCHAR2(3)` | Indicates whether the backup piece is encrypted (`YES`) or not (`NO`). |
| `BACKED_BY_OSB` | `VARCHAR2(3)` | Indicates whether the backup piece is backed up to Oracle Secure Backup (`YES`) or not (`NO`). |