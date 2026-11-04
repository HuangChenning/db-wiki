---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_DATAFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.91 V$BACKUP\_DATAFILE

`V$BACKUP_DATAFILE` displays information about control files and data files in backup sets from the control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Backup data file record ID |
| `STAMP` | `NUMBER` | Backup data file record stamp |
| `SET_STAMP` | `NUMBER` | Backup set stamp |
| `SET_COUNT` | `NUMBER` | Backup set count |
| `FILE#` | `NUMBER` | Data file number; set to 0 for control file |
| `CREATION_CHANGE#` | `NUMBER` | Creation system change number (SCN) of the data file |
| `CREATION_TIME` | `DATE` | Creation timestamp of the data file |
| `RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs system change number (SCN) of the data file when it was backed up |
| `RESETLOGS_TIME` | `DATE` | Resetlogs timestamp of the data file when it was backed up |
| `INCREMENTAL_LEVEL` | `NUMBER` | Normal full backups have a NULL value, level 0 incremental backups have a value of 0, and level 1 incremental backups have a value of 1 |
| `INCREMENTAL_CHANGE#` | `NUMBER` | All blocks changed after the incremental change number is included in this backup; set to 0 for a full backup |
| `CHECKPOINT_CHANGE#` | `NUMBER` | All changes up to the checkpoint change number are included in this backup |
| `CHECKPOINT_TIME` | `DATE` | Timestamp of the checkpoint |
| `ABSOLUTE_FUZZY_CHANGE#` | `NUMBER` | Highest change number in this backup |
| `MARKED_CORRUPT` | `NUMBER` | Number of blocks marked corrupt |
| `MEDIA_CORRUPT` | `NUMBER` | Number of blocks media corrupt |
| `LOGICALLY_CORRUPT` | `NUMBER` | Number of blocks logically corrupt |
| `DATAFILE_BLOCKS` | `NUMBER` | Size of the data file in blocks at backup time. This value is also the number of blocks taken by the data file restarted from this backup. |
| `BLOCKS` | `NUMBER` | Size of the backup data file (in blocks). Unused blocks are not copied to the backup. |
| `BLOCK_SIZE` | `NUMBER` | Block size |
| `OLDEST_OFFLINE_RANGE` | `NUMBER` | RECID of the oldest offline range record in this backup control file. `0` for data file backups. |
| `COMPLETION_TIME` | `DATE` | Time completed |
| `CONTROLFILE_TYPE` | `VARCHAR2(1)` | `B` - Normal copies  `S` - Standby copies |
| `USED_CHANGE_TRACKING` | `VARCHAR2(3)` | Indicates whether change tracking data was used to accelerate this incremental backup (`YES`) or whether change tracking data was not used (`NO`) |
| `BLOCKS_READ` | `NUMBER` | Number of blocks that were scanned while taking this backup. If this was an incremental backup, and change tracking was used to optimize the backup, then the value of this column will be smaller than `DATAFILE_BLOCKS`. Otherwise, the value of this column will be the same as `DATAFILE_BLOCKS`. Even when change tracking data is used, the value of this column may be larger than `BLOCKS`, because the data read by change tracking is further refined during the process of creating an incremental backup. |
| `USED_OPTIMIZATION` | `VARCHAR2(3)` | Indicates whether backup optimization was applied (`YES`) or not (`NO`) |
| `FOREIGN_DBID` | `NUMBER` | Foreign DBID of the database from which this data file was transported. The value is 0 if the file backed up is not a foreign database file. |
| `PLUGGED_READONLY` | `VARCHAR2(3)` | `YES` if this is a backup of a transported read-only foreign file; otherwise `NO`. |
| `PLUGIN_CHANGE#` | `NUMBER` | SCN at which the foreign data file was transported into the database. The value is 0 if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is 0 if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_TIME` | `DATE` | The time of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is 0 if this file is not a foreign database file. |
| `SECTION_SIZE` | `NUMBER` | Specifies the number of blocks in each section of a multisection backup. Value is 0 for whole file backups. |
| `UNDO_OPTIMIZED` | `VARCHAR2(3)` | Indicates whether undo blocks were ignored when creating the backup data file (`YES`) or not (`NO`) |
| `BLOCKS_SKIPPED_IN_CELL` | `NUMBER` | Number of blocks that were not backed up because they were skipped by the Exadata cell  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `BACKED_BY_PDB` | `VARCHAR2(3)` | Recovery Manager (RMAN) allows a PDB to be backed up in two ways. The value in this column indicates how the PDB backup was taken:  - `YES`: The backup was taken when connected to the PDB - `NO`: The backup was taken when connected to the root container |
| `SPARSE_BACKUP` | `VARCHAR2(3)` | Indicates whether the file is sparse (`YES`) or not (`NO`) |
| `GUID` | `RAW(16)` | The GUID of the PDB to which the backup belongs. This is useful after the PDB is dropped to identify which PDB the backup belongs to. |