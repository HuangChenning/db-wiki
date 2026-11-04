---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-OBSOLETE_BACKUP_FILES.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.97 V$OBSOLETE\_BACKUP\_FILES

`V$OBSOLETE_BACKUP_FILES` displays all obsolete backups, copies, and archived logs according to the current retention policy.

This view requires that the database is set using the `DBMS_RCVMAN.SETDATABASE` procedure.

| Column | Datatype | Description |
| --- | --- | --- |
| `PKEY` | `NUMBER` | Primary key for the backup |
| `BACKUP_TYPE` | `VARCHAR2(32)` | Type of the backup:  - `BACKUP SET` - `COPY` - `PROXY COPY` |
| `FILE_TYPE` | `VARCHAR2(32)` | Type of the file:  - `DATAFILE` - `CONTROLFILE` - `SPFILE` - `REDO LOG` - `PIECE` |
| `KEEP` | `VARCHAR2(3)` | Indicates whether the backup has a retention policy different from the value for `CONFIGURE RETENTION POLICY` (`YES`) or not (`NO`) |
| `KEEP_UNTIL` | `DATE` | If the `KEEP UNTIL TIME` clause of the `BACKUP` command was specified, then this column shows the date after which the backup becomes obsolete. If the column is null and `KEEP_OPTIONS` is not null, the backup never becomes obsolete. |
| `KEEP_OPTIONS` | `VARCHAR2(13)` | `KEEP` options for the backup:  - `LOGS` - RMAN keeps the logs needed to recover the backup - `NOLOGS` - RMAN does not keep the logs needed to recover the backup  If this column is null, then the backup has no KEEP options and will be made obsolete based on the retention policy. |
| `STATUS` | `VARCHAR2(16)` | Status of the backup:  - `AVAILABLE` - `UNAVAILABLE` - `EXPIRED` - `OTHER` |
| `FNAME` | `VARCHAR2(1024)` | Name of the file |
| `TAG` | `VARCHAR2(32)` | Tag of the piece, copy, or proxy copy |
| `MEDIA` | `VARCHAR2(80)` | Media ID of the piece or proxy copy |
| `RECID` | `NUMBER` | Recid of the record in the controlfile |
| `STAMP` | `NUMBER` | Stamp of the record in the controlfile |
| `DEVICE_TYPE` | `VARCHAR2(255)` | Type of media device that stores the backup |
| `BLOCK_SIZE` | `NUMBER` | Block size for the backup (in bytes) |
| `COMPLETION_TIME` | `DATE` | Time when the backup completed |
| `BS_KEY` | `NUMBER` | Primary key of the backup set (valid only when `BACKUP_TYPE` is `BACKUP SET`) |
| `BS_COUNT` | `NUMBER` | Count of the backup set from the controlfile record (valid only when `BACKUP_TYPE` is `BACKUP SET`) |
| `BS_STAMP` | `NUMBER` | Stamp of the backup set from the controlfile record (valid only when `BACKUP_TYPE` is `BACKUP SET`) |
| `BS_TYPE` | `VARCHAR2(32)` | Type of the backup set (valid only when `BACKUP_TYPE` is `BACKUP SET`):  - `DATAFILE` - `ARCHIVED LOG` |
| `BS_INCR_TYPE` | `VARCHAR2(32)` | Incremental level of the backup set (valid only when `BACKUP_TYPE` is `BACKUP SET`) |
| `BS_PIECES` | `NUMBER` | Number of backup pieces in the backup set (valid only when `BACKUP_TYPE` is `BACKUP SET`) |
| `BS_COMPLETION_TIME` | `DATE` | Completion time of the backup set (valid only when `BACKUP_TYPE` is `BACKUP SET`) |
| `BP_PIECE#` | `NUMBER` | Number of the backup piece (valid only when `FILE_TYPE` is `PIECE` and `BACKUP_TYPE` is `BACKUP SET`) |
| `BP_COPY#` | `NUMBER` | Copy number of the backup piece (valid only when `FILE_TYPE` is `PIECE` and `BACKUP_TYPE` is `BACKUP SET`) |
| `DF_FILE#` | `NUMBER` | Absolute file number of the datafile (valid only when `FILE_TYPE` is `DATAFILE`) |
| `DF_RESETLOGS_CHANGE#` | `NUMBER` | System change number (SCN) of the most recent `RESETLOGS` when the control file or datafile was created (valid only when `FILE_TYPE` is `DATAFILE`) |
| `DF_CREATION_CHANGE#` | `NUMBER` | Creation SCN of the control file or datafile (valid only when `FILE_TYPE` is `DATAFILE`) |
| `DF_CHECKPOINT_CHANGE#` | `NUMBER` | System change number (SCN) of the most recent control file or datafile checkpoint (valid only when `FILE_TYPE` is `DATAFILE`) |
| `DF_CKP_MOD_TIME` | `DATE` | Modification time in case of SPFILE, otherwise time when the control file or datafile was checkpointed (valid only when `FILE_TYPE` is `DATAFILE`) |
| `RL_THREAD#` | `NUMBER` | Number of the redo thread (valid only when `FILE_TYPE` is `REDO LOG`) |
| `RL_SEQUENCE#` | `NUMBER` | Log sequence number (valid only when `FILE_TYPE` is `REDO LOG`) |
| `RL_RESETLOGS_CHANGE#` | `NUMBER` | System change number (SCN) of the most recent `RESETLOGS` when the record was created (valid only when `FILE_TYPE` is `REDO LOG`) |
| `RL_FIRST_CHANGE#` | `NUMBER` | First SCN of the redo log (valid only when `FILE_TYPE` is `REDO LOG`) |
| `RL_FIRST_TIME` | `DATE` | Time when Oracle switched into the redo log (valid only when `FILE_TYPE` is `REDO LOG`) |
| `RL_NEXT_CHANGE#` | `NUMBER` | First SCN of the next redo log in the thread (valid only when `FILE_TYPE` is `REDO LOG`) |
| `RL_NEXT_TIME` | `DATE` | First timestamp of the next redo log in the thread (valid only when `FILE_TYPE` is `REDO LOG`) |

See Also:

[Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=BRADV53532) for more information about the `DBMS_RCVMAN.SETDATABASE` procedure