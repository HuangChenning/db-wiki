---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_PROXY_DATAFILE.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view contains descriptions of data file backups that were taken using the proxy copy functionality. It corresponds to the `V$PROXY_DATAFILE` view.

In a proxy copy, the media manager takes over the operations of backing up and restoring data. Each row represents a backup of one database file.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `PDB_KEY` | `NUMBER` | The primary key of the PDB in the recovery catalog. Use this column to identify the PDB that owns the proxy copies. |
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