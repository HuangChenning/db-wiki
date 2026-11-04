---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_DATAFILE_COPY.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists information about data file copies on disk. It corresponds to the `V$DATAFILE_COPY` view.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `PDB_KEY` | `NUMBER` | The primary key of the PDB in the recovery catalog. Use this column to identify the PDB that owns the data file copies. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `CDF_KEY` | `NUMBER` | The primary key of the data file copy in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `RECID` | `NUMBER` | The data file copy record from `V$DATAFILE_COPY`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The data file copy stamp from `V$DATAFILE_COPY`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `NAME` | `VARCHAR2(1024)` | The file name of the data file copy. |
| `TAG` | `VARCHAR2(32)` | The tag for the data file copy. |
| `FILE#` | `NUMBER` | The absolute file number for the data file. |
| `CREATION_CHANGE#` | `NUMBER` | The creation SCN of the data file. |
| `CREATION_TIME` | `DATE` | Data file creation timestamp. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the most recent `RESETLOGS` when the data file was created. |
| `RESETLOGS_TIME` | `DATE` | The time stamp of the most recent `RESETLOGS` in the data file header. |
| `INCREMENTAL_LEVEL` | `NUMBER` | The incremental level of the copy: `0` or `NULL`. |
| `CHECKPOINT_CHANGE#` | `NUMBER` | The SCN of the most recent data file checkpoint. |
| `CHECKPOINT_TIME` | `DATE` | The time of the most recent data file checkpoint. |
| `ABSOLUTE_FUZZY_CHANGE#` | `NUMBER` | The highest SCN in any block of the file, if known. Recovery must proceed to at least this SCN for the file to become not fuzzy. |
| `RECOVERY_FUZZY_CHANGE#` | `NUMBER` | The SCN to which recovery must proceed for the file to become not fuzzy. If not `NULL`, this file must be recovered at least to the specified SCN before the database can be opened with this file. |
| `RECOVERY_FUZZY_TIME` | `DATE` | The time that is associated with the `RECOVERY_FUZZY_CHANGE#`. |
| `ONLINE_FUZZY` | `VARCHAR2(3)` | `YES` / `NO`. If set to `YES`, this copy was made after an instance failure or `OFFLINE IMMEDATE` (or is a copy that was taken improperly while the database was open). Recovery applies all redo up to the next crash recovery marker to make the file consistent. |
| `BACKUP_FUZZY` | `VARCHAR2(3)` | `YES` / `NO`. If set to `YES`, this is a copy taken using the `BEGIN BACKUP` / `END BACKUP` technique. To make this copy consistent, the recovery process needs to apply all redo up to the marker that is placed in the redo stream when the `ALTER TABLESPACE END BACKUP` command is used. |
| `BLOCKS` | `NUMBER` | The number of blocks in the data file copy (also the size of the data file when the copy was made). |
| `BLOCK_SIZE` | `NUMBER` | The size of the blocks in bytes. |
| `COMPLETION_TIME` | `DATE` | The time when the copy completed. |
| `STATUS` | `VARCHAR2(1)` | The status of the copy: `A` (available), `U` (unavailable), `X` (expired), or `D` (deleted). |
| `KEEP` | `VARCHAR2(3)` | Indicates whether this copy has a retention policy different from the value for `CONFIGURE RETENTION POLICY`. Possible values are `YES` and `NO`. |
| `KEEP_UNTIL` | `DATE` | If the `KEEP UNTIL TIME` clause of the `COPY` command was specified, then this column shows the date after which this data file copy becomes obsolete. If the column is `NULL` and `KEEP OPTIONS` is not `NULL`, the copy never becomes obsolete. |
| `KEEP_OPTIONS` | `VARCHAR2(11)` | The `KEEP` options specified for this data file copy. Possible values are `NOLOGS`, `BACKUP_LOGS`, `LOGS`, and `NULL`. `NOLOGS` indicates a consistent backup made when the database was mounted. `BACKUP_LOGS` indicates that the backup was made in open mode, so archived log backups must be applied to make it consistent. `LOGS` indicates a long-term backup made with the `LOGS` keyword, which is now deprecated. `NULL` indicates that this backup has no `KEEP` options and becomes obsolete based on the retention policy. |
| `SCANNED` | `VARCHAR2(3)` | Whether RMAN scanned the file (`YES` or `NO`). If `YES`, then this copy was created by a server process that examined every block in the file, for example, by the RMAN `COPY` or `RESTORE` command. If `NO`, then RMAN did not examine every block in the file, as when RMAN inspects a non-RMAN generated image copy or restores by proxy copy.  Whenever RMAN creates or restores a data file copy, it adds rows to the `V$DATABASE_BLOCK_CORRUPTION` view and `RC_DATABASE_BLOCK_CORRUPTION` view if it discovers corrupt blocks in the file. If RMAN has scanned the entire file, then the absence of corruption records for this copy means that no corrupt blocks exist in the file. If RMAN did not scan the file, then the absence of corruption records means that corrupt blocks may or may not exist in the file. |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | This data file copy is located in the fast recovery area: `YES` or `NO`. |
| `RSR_KEY` | `NUMBER` | Unique key for the row in `RC_RMAN_STATUS` that created this backup piece. |
| `MARKED_CORRUPT` | `NUMBER` | The number of blocks that were discovered to be corrupt during the course of this backup. These blocks were reformatted as known-corrupt blocks in the output image copy. |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with this file. Each database in a Data Guard environment has a unique `SITE_KEY` value. You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |
| `DB_UNIQUE_NAME` | `VARCHAR2(512)` | The `DB_UNIQUE_NAME` of the database incarnation to which this record belongs. All databases in a Data Guard environment share the same DBID but different `DB_UNIQUE_NAME` values. The value in this column is null when the database name is not known for a specific file. For example, rows for databases managed by versions of RMAN before Oracle Database 11g are null. |
| `FOREIGN_DBID` | `NUMBER` | Foreign DBID of the database from which this data file was transported. The value is `0` if the file backed up is not a foreign database file. |
| `PLUGGED_READONLY` | `VARCHAR2(3)` | `YES` if this is a copy of a transported read-only foreign file; otherwise `NO`. |
| `PLUGIN_CHANGE#` | `NUMBER` | SCN at which the foreign data file was transported into the database. The value is `0` if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is `0` if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_TIME` | `DATE` | The time of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is `0` if this file is not a foreign database file. |
| `SPARSE_BACKUP` | `VARCHAR2(3)` | Indicates if the backup is a sparse backup |