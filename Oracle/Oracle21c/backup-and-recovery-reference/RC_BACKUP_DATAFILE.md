---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_BACKUP_DATAFILE.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists information about data files in backup sets. It corresponds to the `V$BACKUP_DATAFILE` view. A backup data file is uniquely identified by `BDF_KEY`.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `PDB_KEY` | `NUMBER` | The primary key of the PDB in the recovery catalog. Use this column to identify the PDB that owns the backups. |
| `BDF_KEY` | `NUMBER` | The primary key of the data file backup in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `RECID` | `NUMBER` | The backup data file `RECID` from `V$BACKUP_DATAFILE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The backup data file stamp from `V$BACKUP_DATAFILE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `BS_KEY` | `NUMBER` | The primary key of the backup set to which this record belongs in the recovery catalog. Use this column to join with `RC_BACKUP_SET` or `RC_BACKUP_PIECE`. |
| `SET_STAMP` | `NUMBER` | The `SET_STAMP` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `SET_COUNT` | `NUMBER` | The `SET_COUNT` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `BS_RECID` | `NUMBER` | The `RECID` from `V$BACKUP_SET`. |
| `BS_STAMP` | `NUMBER` | The `STAMP` from `V$BACKUP_SET`. |
| `BACKUP_TYPE` | `VARCHAR2(1)` | The type of the backup: `D` (full or level 0 incremental) or `I` (incremental level 1). |
| `INCREMENTAL_LEVEL` | `NUMBER` | The level of the incremental backup: `NULL`, 0, or 1. |
| `COMPLETION_TIME` | `DATE` | The completion time of the backup. |
| `FILE#` | `NUMBER` | The absolute file number of the data file. When `FILE#` =0, the record refers to the control file. See the note following this table for special semantics of other columns when `FILE#` =0. |
| `CREATION_CHANGE#` | `NUMBER` | The creation SCN of the data file. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The `SCN` of the most recent `RESETLOGS` in the data file header. |
| `RESETLOGS_TIME` | `DATE` | The time stamp of the most recent `RESETLOGS` in the data file header. |
| `INCREMENTAL_CHANGE#` | `NUMBER` | The SCN that determines whether a block is included in the incremental backup. A block is only included if the SCN in the block header is greater than or equal to `INCREMENTAL_CHANGE#`.  The range of redo covered by the incremental backup begins with `INCREMENTAL_CHANGE#` and ends with `CHECKPOINT_CHANGE#`. |
| `CHECKPOINT_CHANGE#` | `NUMBER` | The checkpoint SCN of this data file in this backup set. |
| `CHECKPOINT_TIME` | `DATE` | The time associated with `CHECKPOINT_CHANGE#`. |
| `ABSOLUTE_FUZZY_CHANGE#` | `NUMBER` | The absolute fuzzy SCN. See the note following this table for special semantics when `FILE#` =0. |
| `DATAFILE_BLOCKS` | `NUMBER` | The number of data blocks in the data file. |
| `BLOCKS` | `NUMBER` | The number of data blocks written to the backup. This value is often less than `DATAFILE_BLOCKS` because for full backups, blocks that have never been used are not included in the backup, and for incremental backups, blocks that have not changed are not included in the backup. This value is never greater than `DATAFILE_BLOCKS`. |
| `BLOCK_SIZE` | `NUMBER` | The size of the data blocks in bytes. |
| `STATUS` | `VARCHAR2(1)` | The status of the backup set: `A` (all pieces available), `D` (all pieces deleted), `O` (some pieces are available but others are not, so the backup set is unusable). |
| `BS_LEVEL` | `NUMBER` | The incremental level (`NULL,` 0, or 1) specified when this backup was created. This value can be different from the `INCREMENTAL_LEVEL` column because if you run, for example, a level 1 incremental backup, but no previous level 0 backup exists for some files, a level 0 backup is automatically taken for these files. In this case, `BS_LEVEL` is 0 and `INCREMENTAL_LEVEL` is 0. |
| `PIECES` | `NUMBER` | The number of backup pieces in the backup set that contains this backup data file. |
| `BLOCKS_READ` | `NUMBER` | Number of blocks that were scanned while taking this backup. If this was an incremental backup, and change tracking was used to optimize the backup, then the value of this column is smaller than `DATAFILE_BLOCKS`. Otherwise, the value of this column equals `DATAFILE_BLOCKS`. Even when change tracking data is used, the value of this column may be larger than `BLOCKS`, because the data read by change tracking is further refined during the process of creating an incremental backup. |
| `CREATION_TIME` | `DATE` | Creation timestamp of the data file. |
| `MARKED_CORRUPT` | `NUMBER` | Number of blocks marked corrupt. |
| `USED_CHANGE_TRACKING` | `VARCHAR2(3)` | Whether change tracking data was used to accelerate this incremental backup (`YES`) or was not used (`NO`). |
| `USED_OPTIMIZATION` | `VARCHAR2(3)` | Whether backup optimization was applied (`YES`) or not (`NO`). |
| `PCT_NOTREAD` | `NUMBER` | The percentage of the file that was skipped during this backup. For incremental backups, this value indicates the efficiency of the block change tracking file. |
| `FOREIGN_DBID` | `NUMBER` | Foreign DBID of the database from which this data file was transported. The value is `0` if the file backed up is not a foreign database file. |
| `PLUGGED_READONLY` | `VARCHAR2(3)` | `YES` if this is a backup of a transported read-only foreign file; otherwise `NO`. |
| `PLUGIN_CHANGE#` | `NUMBER` | SCN at which the foreign data file was transported into the database. The value is `0` if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is `0` if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_TIME` | `DATE` | The time of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is `0` if this file is not a foreign database file. |
| `SECTION_SIZE` | `NUMBER` | Specifies the number of blocks in each section of a multisection backup. Value is 0 for whole file backups. |
| `SPARSE_BACKUP` | `VARCHAR2(3)` | Indicates if the backup is a sparse backup |