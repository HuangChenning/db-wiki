---
title: "V$DATAFILE_COPY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1101.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DATAFILE_COPY` displays datafile copy information from the control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Datafile copy record ID |
| `STAMP` | `NUMBER` | Datafile copy record stamp |
| `NAME` | `VARCHAR2(513)` | Filename of the datafile copy. The maximum length of the name is OS dependent. |
| `TAG` | `VARCHAR2(32)` | Datafile copy tag |
| `FILE#` | `NUMBER` | Absolute datafile number |
| `RFILE#` | `NUMBER` | Tablespace relative datafile number |
| `CREATION_CHANGE#` | `NUMBER` | Datafile creation change# |
| `CREATION_TIME` | `DATE` | Datafile creation timestamp |
| `RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs change number of the datafile when the copy was made |
| `RESETLOGS_TIME` | `DATE` | Resetlogs timestamp of the datafile when the copy was made |
| `INCREMENTAL_LEVEL` | `NUMBER` | Normal full backups have a NULL value, level 0 incremental backups have a value of 0, and level 1 incremental backups have a value of 1 |
| `CHECKPOINT_CHANGE#` | `NUMBER` | Checkpoint change number of the datafile when the copy was made |
| `CHECKPOINT_TIME` | `DATE` | Checkpoint timestamp of the datafile when the copy was made |
| `ABSOLUTE_FUZZY_CHANGE#` | `NUMBER` | Highest change seen when the datafile was copied |
| `RECOVERY_FUZZY_CHANGE#` | `NUMBER` | Highest change written to the file by media recovery |
| `RECOVERY_FUZZY_TIME` | `DATE` | Timestamp of the highest change written to the file by media recovery |
| `ONLINE_FUZZY` | `VARCHAR2(3)` | (`YES` \| `NO`) If set to `YES`, this is a copy taken using an operating system utility after a crash or offline immediate (or an invalid copy taken while datafile was online and the database open). Recovery will need to apply all redo up to the next crash recovery marker to make the file consistent. |
| `BACKUP_FUZZY` | `VARCHAR2(3)` | (`YES` \| `NO`) If set to `YES`, this is a copy taken using the `BEGIN BACKUP/END BACKUP` technique. Recovery will need to apply all redo up to the end backup marker to make this copy consistent. |
| `MARKED_CORRUPT` | `NUMBER` | Number of blocks marked corrupt by this copy operation. That is, blocks that were not marked corrupted in the source datafile, but were detected and marked as corrupted during the copy operation. |
| `MEDIA_CORRUPT` | `NUMBER` | Total number of media corrupt blocks. For example, blocks with checksum errors are marked media corrupt. |
| `LOGICALLY_CORRUPT` | `NUMBER` | Total number of logically corrupt blocks. For example, applying redo for unrecoverable operations will mark affected blocks logically corrupt. |
| `BLOCKS` | `NUMBER` | Size of the datafile copy in blocks (also the size of the datafile when the copy was made) |
| `BLOCK_SIZE` | `NUMBER` | Block size of the datafile |
| `OLDEST_OFFLINE_RANGE` | `NUMBER` | RECID of the oldest offline range record in this control file copy; 0 for datafile copies |
| `DELETED` | `VARCHAR2(3)` | (`YES` \| `NO`) If set to `YES` the datafile copy has been deleted or overwritten |
| `STATUS` | `VARCHAR2(1)` | Identifies the status of this datafile copy. Possible values are:  `A` - Available  `D` - Deleted  `U` - Unavailable  `X` - Expired |
| `COMPLETION_TIME` | `DATE` | Time when the copy was completed |
| `CONTROLFILE_TYPE` | `VARCHAR2(1)` | `B` indicates normal copies  `S` indicates standby copies |
| `KEEP` | `VARCHAR2(3)` | (`YES` / `NO`) Indicates whether or not this backup set has a retention policy that is different than the value for the configure retention policy |
| `KEEP_UNTIL` | `DATE` | If `KEEP_UNTIL` is specified, this is the date after which the backup becomes obsolete. If this column is null, then the backup never expires. |
| `KEEP_OPTIONS` | `VARCHAR2(10)` | Lists additional retention options for this backup set. Possible values are:  `LOGS` - The logs need to recover this backup are kept  `NOLOGS` - The logs needed to recover this backup will not be kept |
| `SCANNED` | `VARCHAR2(3)` | Indicates whether RMAN scanned the file (`YES`) or not (`NO`) |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | Indicates whether the file was created in the fast recovery area (`YES`) or not (`NO`) |
| `RMAN_STATUS_RECID` | `NUMBER` | Owning `V$RMAN_STATUS` record ID |
| `RMAN_STATUS_STAMP` | `NUMBER` | Owning `V$RMAN_STATUS` record stamp |
| `CONVERTED_FILE` | `VARCHAR2(3)` | (`YES` / `NO`) Indicates whether or not the datafile copy was created using the RMAN `CONVERT` command |
| `SAME_ENDIAN` | `VARCHAR2(3)` | If the value of the `CONVERTED_FILE` column is `YES`, then this column indicates whether the datafile copy has the same endianness as the source datafile (`YES`) or not (`NO`); otherwise NULL |
| `FOREIGN_DBID` | `NUMBER` | Foreign DBID from which this data file came from. The value is 0 if this file is not a foreign database file. |
| `PLUGGED_READONLY` | `VARCHAR2(3)` | `YES` if this is a transported read-only foreign file; otherwise `NO`. |
| `PLUGIN_CHANGE#` | `NUMBER` | SCN at which the foreign datafile was transported into the database. The value is 0 if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is 0 if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_TIME` | `DATE` | The time of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is 0 if this file is not a foreign database file. |
| `BACKED_BY_VSS` | `VARCHAR2(3)` | Whether or not the file has been backed up by Volume Shadow Copy Service (VSS). This column is reserved for internal use. |