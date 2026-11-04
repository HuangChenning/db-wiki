---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_SET.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.100 V$BACKUP\_SET

`V$BACKUP_SET` displays information about backup sets from the control file.

A backup set record is inserted after the backup set is successfully completed.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Backup set record ID |
| `STAMP` | `NUMBER` | Backup set record stamp |
| `SET_STAMP` | `NUMBER` | Backup set stamp. The backup set stamp and count uniquely identify the backup set.  Primary key for the `V$BACKUP_SET` table, and the foreign key for the following tables: `V$BACKUP_PIECE`, `V$BACKUP_DATAFILE`, `V$BACKUP_REDOLOG`, `V$BACKUP_CORRUPTION`. |
| `SET_COUNT` | `NUMBER` | Backup set count. The backup set count is incremented by one every time a new backup set is started (if the backup set is never completed the number is "lost"). If the control file is re-created then the count is reset to `1`. Therefore the count must be used with the stamp to uniquely identify a backup set.  Primary key for the `V$BACKUP_SET` table, and the foreign key for the following tables: `V$BACKUP_PIECE`, `V$BACKUP_DATAFILE`, `V$BACKUP_REDOLOG`, `V$BACKUP_CORRUPTION` |
| `BACKUP_TYPE` | `VARCHAR2(1)` | Type of files that are in this backup. If the backup contains archived redo logs, the value is `L`. If this is a data file full backup, the value is `D`. If this is an incremental backup, the value is `I`. |
| `CONTROLFILE_INCLUDED` | `VARCHAR2(3)` | Provides information about the control file in the backup set:  - `YES`: The control file included is a primary control file. - `SBY`: The control file included is a standby control file. - `NO`: A control file is not included. |
| `INCREMENTAL_LEVEL` | `NUMBER` | Location where this backup set fits into the database's backup strategy. Set to NULL for full datafile, archivelog, controlfile, and spfile backups, set to 0 for incremental level 0 datafile backups, and set to 1 for incremental level 1 datafile backups. |
| `PIECES` | `NUMBER` | Number of distinct backup pieces in the backup set |
| `START_TIME` | `DATE` | Starting time |
| `COMPLETION_TIME` | `DATE` | Time that this backup set completed |
| `ELAPSED_SECONDS` | `NUMBER` | The number of elapsed seconds |
| `BLOCK_SIZE` | `NUMBER` | Block size of the backup set |
| `INPUT_FILE_SCAN_ONLY` | `VARCHAR2(3)` | `YES` indicates no actual backup is performed, but the data files are read. `NO` indicates a normal backup is performed. |
| `KEEP` | `VARCHAR2(3)` | (`YES` / `NO`) Indicates whether or not this backup set has a retention policy that is different than the value for the configure retention policy |
| `KEEP_UNTIL` | `DATE` | If `KEEP_UNTIL` \_TIME is specified, this is the date after which the backup becomes obsolete. If this column is null, then the backup never expires. |
| `KEEP_OPTIONS` | `VARCHAR2(11)` | Lists additional retention options for this backup set. Possible values are:  `LOGS` - The logs need to recover this backup are kept  `NOLOGS` - The logs needed to recover this backup will not be kept  `BACKUP_LOGS` - An archive log backup exists to support this backup set |
| `MULTI_SECTION` | `VARCHAR2(3)` | Indicates whether or not this backup set is a multi-section backup. Valid values are `YES` and `NO`. A multi-section backup is a backup in which multiple backup pieces are produced independently in parallel by multiple channels. |
| `FOR_XTTS` | `VARCHAR2(3)` | Indicates whether this is a cross platform backup set:  - `YES`: This is a cross platform backup set. - `NO`: This is not a cross platform backup set. |
| `SAME_ENDIAN` | `VARCHAR2(3)` | If the value of `FOR_XTTS` is `YES`, then this column indicates whether the backup set has the same endianess as the current database (`YES`) or not (`NO`); otherwise `NULL`. |
| `INC_DMPFILE` | `VARCHAR2(3)` | If the value of `FOR_XTTS` is `YES`, then this column indicates whether the backup set includes a Data Pump export file of the backed up data files (`YES`) or not (`NO`), otherwise `NULL`. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `GUID` | `RAW(16)` | The GUID of the PDB to which the backup belongs. This is useful after the PDB is dropped to identify which PDB the backup belongs to. |