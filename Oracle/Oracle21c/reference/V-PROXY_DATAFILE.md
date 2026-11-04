---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PROXY_DATAFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.140 V$PROXY\_DATAFILE

`V$PROXY_DATAFILE` contains descriptions of datafile and control file backups that are taken with Proxy Copy. Each row represents a backup of one database file.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Proxy copy record ID |
| `STAMP` | `NUMBER` | Proxy copy record stamp |
| `DEVICE_TYPE` | `VARCHAR2(17)` | Type of the device on which the copy resides |
| `HANDLE` | `VARCHAR2(513)` | Proxy copy handle identifies the copy for restore |
| `COMMENTS` | `VARCHAR2(81)` | Comment returned by the operating system or storage subsystem. This value is informational only. It is not needed for restore. |
| `MEDIA` | `VARCHAR2(65)` | Name of the media on which the copy resides. This value is informational only. It is not needed for restore. |
| `MEDIA_POOL` | `NUMBER` | Media pool in which the copy resides. This is the same value that was entered in the `POOL` operand of the Recovery Manager `BACKUP` command |
| `TAG` | `VARCHAR2(32)` | Proxy copy tag |
| `STATUS` | `VARCHAR2(1)` | Status of the backup set:  - `A` - Available - `U` - Unavailable - `X` - Expired - `D` - Deleted |
| `DELETED` | `VARCHAR2(3)` | Indicates whether this record has been deleted (`YES`) or not (`NO`) |
| `FILE#` | `NUMBER` | Absolute datafile number, or 0 if this is a control file backup |
| `CREATION_CHANGE#` | `NUMBER` | Datafile creation change number |
| `CREATION_TIME` | `DATE` | Datafile creation Timestamp |
| `RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs change number of the datafile when the copy was made |
| `RESETLOGS_TIME` | `DATE` | Resetlogs timestamp of the datafile when the copy was made |
| `CHECKPOINT_CHANGE#` | `NUMBER` | Checkpoint change number of the datafile when the copy was made |
| `CHECKPOINT_TIME` | `DATE` | Checkpoint timestamp of the datafile when the copy was made |
| `ABSOLUTE_FUZZY_CHANGE#` | `NUMBER` | Highest change in any block of the file, if known |
| `RECOVERY_FUZZY_CHANGE#` | `NUMBER` | Highest change written to the file by media recovery |
| `RECOVERY_FUZZY_TIME` | `DATE` | Timestamp of the highest change written to the file by media recovery |
| `INCREMENTAL_LEVEL` | `NUMBER` | If this backup is part of an incremental backup strategy, then 0. Otherwise null. |
| `ONLINE_FUZZY` | `VARCHAR2(3)` | Indicates whether this copy was made after a crash or offline immediate (or is a copy of a copy which was taken improperly while the database was open) (`YES`) or not (`NO`). Recovery will need to apply all redo up to the next crash recovery marker to make the file consistent. |
| `BACKUP_FUZZY` | `VARCHAR2(3)` | Indicates whether this is a copy taken using the `BEGIN BACKUP \| END BACKUP` technique (`YES`) or not (`NO`). The `BEGIN BACKUP \| END BACKUP` technique is used internally when proxy copies of open files are created. Recovery will need to apply all redo up to the end backup marker to make this copy consistent. |
| `BLOCKS` | `NUMBER` | Size of the copy (in blocks). Also the size of the datafile when the copy was made. |
| `BLOCK_SIZE` | `NUMBER` | Block size of the datafile |
| `OLDEST_OFFLINE_RANGE` | `NUMBER` | If the file number is `0 ` (that is, this is a control file backup), the RECID of the oldest offline range record in this control file copy. `0` for datafile copies. |
| `START_TIME` | `DATE` | Starting time |
| `COMPLETION_TIME` | `DATE` | Completion time |
| `ELAPSED_SECONDS` | `NUMBER` | Number of elapsed seconds |
| `CONTROLFILE_TYPE` | `VARCHAR2(1)` | Type of control file:  - `B` - Normal control file - `S` - Standby control file |
| `KEEP` | `VARCHAR2(3)` | Indicates whether this backup set has a retention policy that is different than the value for the configure retention policy (`YES`) or not (`NO`) |
| `KEEP_UNTIL` | `DATE` | If specified, then this is the date after which the backup becomes obsolete. If this column is NULL, then the backup never expires. |
| `KEEP_OPTIONS` | `VARCHAR2(11)` | Additional retention options for this backup set:  - `LOGS` - Indicates a long-term backup made with the `LOGS` keyword, which is now deprecated - `BACKUP_LOGS` - Indicates that the backup was made in open mode, so archived log backups must be applied to make it consistent - `NOLOGS` - Indicates a consistent backup made when the database was mounted. - NULL - Indicates that this backup has no `KEEP` options and becomes obsolete based on the retention policy |
| `RMAN_STATUS_RECID` | `NUMBER` | Owning `V$RMAN_STATUS` record ID |
| `RMAN_STATUS_STAMP` | `NUMBER` | Owning `V$RMAN_STATUS` stamp |
| `FOREIGN_DBID` | `NUMBER` | Foreign DBID of the database from which this datafile was transported. The value is `0` if the file backed up is not a foreign database file. |
| `PLUGGED_READONLY` | `VARCHAR2(3)` | Indicates whether this is a proxy copy of a transported read-only foreign file (`YES`) or not (`NO`) |
| `PLUGIN_CHANGE#` | `NUMBER` | SCN at which the foreign datafile was transported into the database. The value is `0` if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_CHANGE#` | `NUMBER` | SCN of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is `0` if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_TIME` | `DATE` | Time of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is `0` if this file is not a foreign database file. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `BACKED_BY_PDB` | `VARCHAR2(3)` | Recovery Manager (RMAN) allows a PDB to be backed up in two ways. The value in this column indicates how the PDB backup was taken:  - `YES`: The backup was taken when connected to the PDB - `NO`: The backup was taken when connected to the root container |
| `GUID` | `RAW(16)` | The GUID of the PDB to which the backup belongs. This is useful after the PDB is dropped to identify which PDB the backup belongs to. |