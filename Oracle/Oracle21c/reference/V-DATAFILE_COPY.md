---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DATAFILE_COPY.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.158 V$DATAFILE\_COPY

`V$DATAFILE_COPY` displays data file copy information from the control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Data file copy record ID |
| `STAMP` | `NUMBER` | Data file copy record stamp |
| `NAME` | `VARCHAR2(513)` | File name of the data file copy. The maximum length of the name is operating system dependent. |
| `TAG` | `VARCHAR2(32)` | Data file copy tag |
| `FILE#` | `NUMBER` | Absolute data file number |
| `RFILE#` | `NUMBER` | Tablespace relative data file number |
| `CREATION_CHANGE#` | `NUMBER` | Data file creation change# |
| `CREATION_TIME` | `DATE` | Data file creation timestamp |
| `RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs change number of the data file when the copy was made |
| `RESETLOGS_TIME` | `DATE` | Resetlogs timestamp of the data file when the copy was made |
| `INCREMENTAL_LEVEL` | `NUMBER` | Normal full backups have a NULL value, level 0 incremental backups have a value of 0, and level 1 incremental backups have a value of 1 |
| `CHECKPOINT_CHANGE#` | `NUMBER` | Checkpoint change number of the data file when the copy was made |
| `CHECKPOINT_TIME` | `DATE` | Checkpoint timestamp of the data file when the copy was made |
| `ABSOLUTE_FUZZY_CHANGE#` | `NUMBER` | Highest change seen when the data file was copied |
| `RECOVERY_FUZZY_CHANGE#` | `NUMBER` | Highest change written to the file by media recovery |
| `RECOVERY_FUZZY_TIME` | `DATE` | Timestamp of the highest change written to the file by media recovery |
| `ONLINE_FUZZY` | `VARCHAR2(3)` | (`YES` \| `NO`) If set to `YES`, this is a copy taken using an operating system utility after a crash or offline immediate (or an invalid copy taken while data file was online and the database open). Recovery will need to apply all redo up to the next crash recovery marker to make the file consistent. |
| `BACKUP_FUZZY` | `VARCHAR2(3)` | (`YES` \| `NO`) If set to `YES`, this is a copy taken using the `BEGIN BACKUP/END BACKUP` technique. Recovery will need to apply all redo up to the end backup marker to make this copy consistent. |
| `MARKED_CORRUPT` | `NUMBER` | Number of blocks marked corrupt by this copy operation. That is, blocks that were not marked corrupted in the source data file, but were detected and marked as corrupted during the copy operation. |
| `MEDIA_CORRUPT` | `NUMBER` | Total number of media corrupt blocks. For example, blocks with checksum errors are marked media corrupt. |
| `LOGICALLY_CORRUPT` | `NUMBER` | Total number of logically corrupt blocks. For example, applying redo for unrecoverable operations will mark affected blocks logically corrupt. |
| `BLOCKS` | `NUMBER` | Size of the data file copy in blocks (also the size of the data file when the copy was made) |
| `BLOCK_SIZE` | `NUMBER` | Block size of the data file |
| `OLDEST_OFFLINE_RANGE` | `NUMBER` | RECID of the oldest offline range record in this control file copy; 0 for data file copies |
| `DELETED` | `VARCHAR2(3)` | (`YES` \| `NO`) If set to `YES` the data file copy has been deleted or overwritten |
| `STATUS` | `VARCHAR2(1)` | Identifies the status of this data file copy. Possible values are:  `A` - Available  `D` - Deleted  `U` - Unavailable  `X` - Expired |
| `COMPLETION_TIME` | `DATE` | Time when the copy was completed |
| `CONTROLFILE_TYPE` | `VARCHAR2(1)` | `B` indicates normal copies  `S` indicates standby copies |
| `KEEP` | `VARCHAR2(3)` | (`YES` / `NO`) Indicates whether or not this backup set has a retention policy that is different than the value for the configure retention policy |
| `KEEP_UNTIL` | `DATE` | If `KEEP_UNTIL` is specified, this is the date after which the backup becomes obsolete. If this column is null, then the backup never expires. |
| `KEEP_OPTIONS` | `VARCHAR2(11)` | Lists additional retention options for this backup set. Possible values are:  `LOGS` - The logs need to recover this backup are kept  `NOLOGS` - The logs needed to recover this backup will not be kept |
| `SCANNED` | `VARCHAR2(3)` | Indicates whether RMAN scanned the file (`YES`) or not (`NO`) |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | Indicates whether the file was created in the fast recovery area (`YES`) or not (`NO`) |
| `RMAN_STATUS_RECID` | `NUMBER` | Owning `V$RMAN_STATUS` record ID |
| `RMAN_STATUS_STAMP` | `NUMBER` | Owning `V$RMAN_STATUS` record stamp |
| `CONVERTED_FILE` | `VARCHAR2(3)` | (`YES` / `NO`) Indicates whether or not the data file copy was created using the RMAN `CONVERT` command |
| `SAME_ENDIAN` | `VARCHAR2(3)` | If the value of the `CONVERTED_FILE` column is `YES`, then this column indicates whether the data file copy has the same endianness as the source data file (`YES`) or not (`NO`); otherwise NULL |
| `FOREIGN_DBID` | `NUMBER` | Foreign DBID from which this data file came from. The value is 0 if this file is not a foreign database file. |
| `PLUGGED_READONLY` | `VARCHAR2(3)` | `YES` if this is a transported read-only foreign file; otherwise `NO`. |
| `PLUGIN_CHANGE#` | `NUMBER` | SCN at which the foreign data file was transported into the database. The value is 0 if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is 0 if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_TIME` | `DATE` | The time of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is 0 if this file is not a foreign database file. |
| `BACKED_BY_VSS` | `VARCHAR2(3)` | Whether or not the file has been backed up by Volume Shadow Copy Service (VSS). This column is reserved for internal use. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `BACKED_BY_PDB` | `VARCHAR2(3)` | Recovery Manager (RMAN) allows a PDB to be backed up in two ways. The value in this column indicates how the PDB backup was taken:  - `YES`: The backup was taken when connected to the PDB - `NO`: The backup was taken when connected to the root container |
| `SPARSE_BACKUP` | `VARCHAR2(3)` | Indicates whether the file is sparse (`YES`) or not (`NO`) |
| `GUID` | `RAW(16)` | The GUID of the PDB to which the backup belongs. This is useful after the PDB is dropped to identify which PDB the backup belongs to. |