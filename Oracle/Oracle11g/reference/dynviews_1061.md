---
title: "V$BACKUP_SET"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1061.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BACKUP_SET` displays information about backup sets from the control file. A backup set record is inserted after the backup set is successfully completed.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Backup set record ID |
| `STAMP` | `NUMBER` | Backup set record stamp |
| `SET_STAMP` | `NUMBER` | Backup set stamp. The backup set stamp and count uniquely identify the backup set.  Primary key for the `V$BACKUP_SET` table, and the foreign key for the following tables: `V$BACKUP_PIECE`, `V$BACKUP_DATAFILE`, `V$BACKUP_REDOLOG`, `V$BACKUP_CORRUPTION`. |
| `SET_COUNT` | `NUMBER` | Backup set count. The backup set count is incremented by one every time a new backup set is started (if the backup set is never completed the number is "lost"). If the control file is re-created then the count is reset to `1`. Therefore the count must be used with the stamp to uniquely identify a backup set.  Primary key for the `V$BACKUP_SET` table, and the foreign key for the following tables: `V$BACKUP_PIECE`, `V$BACKUP_DATAFILE`, `V$BACKUP_REDOLOG`, `V$BACKUP_CORRUPTION` |
| `BACKUP_TYPE` | `VARCHAR2(1)` | Type of files that are in this backup. If the backup contains archived redo logs, the value is `L`. If this is a datafile full backup, the value is `D`. If this is an incremental backup, the value is `I`. |
| `CONTROLFILE_INCLUDED` | `VARCHAR2(3)` | Set to `YES` if there is a control file included in this backup set, otherwise set to `NO` |
| `INCREMENTAL_LEVEL` | `NUMBER` | Location where this backup set fits into the database's backup strategy. Set to NULL for full datafile, archivelog, controlfile, and spfile backups, set to 0 for incremental level 0 datafile backups, and set to 1 for incremental level 1 datafile backups. |
| `PIECES` | `NUMBER` | Number of distinct backup pieces in the backup set |
| `START_TIME` | `DATE` | Starting time |
| `COMPLETION_TIME` | `DATE` | Time that this backup set completed |
| `ELAPSED_SECONDS` | `NUMBER` | The number of elapsed seconds |
| `BLOCK_SIZE` | `NUMBER` | Block size of the backup set |
| `INPUT_FILE_SCAN_ONLY` | `VARCHAR2(3)` | `YES` indicates no actual backup is performed, but the datafiles are read. `NO` indicates a normal backup is performed. |
| `KEEP` | `VARCHAR2(3)` | (`YES` / `NO`) Indicates whether or not this backup set has a retention policy that is different than the value for the configure retention policy |
| `KEEP_UNTIL` | `DATE` | If `KEEP_UNTIL` \_TIME is specified, this is the date after which the backup becomes obsolete. If this column is null, then the backup never expires. |
| `KEEP_OPTIONS` | `VARCHAR2(10)` | Lists additional retention options for this backup set. Possible values are:  `LOGS` - The logs need to recover this backup are kept  `NOLOGS` - The logs needed to recover this backup will not be kept  `BACKUP_LOGS` - An archive log backup exists to support this backup set |
| `MULTI_SECTION` | `VARCHAR2(3)` | Indicates whether or not this backup set is a multi-section backup. Valid values are `YES` and `NO`. A multi-section backup is a backup in which multiple backup pieces are produced independently in parallel by multiple channels. |