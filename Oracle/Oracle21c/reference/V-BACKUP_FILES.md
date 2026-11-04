---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_FILES.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.95 V$BACKUP\_FILES

`V$BACKUP_FILES` displays information about all RMAN backups (both image copies and backup sets) and archived logs.

This view simulates the `LIST BACKUP` and `LIST COPY` RMAN commands. This view requires that the database be set using the `DBMS_RCVMAN.SETDATABASE` procedure.

| Column | Datatype | Description |
| --- | --- | --- |
| `PKEY` | `NUMBER` | Primary key for the backup |
| `BACKUP_TYPE` | `VARCHAR2(32)` | Type of the backup:  - `BACKUP SET` - `COPY` - `PROXY COPY` |
| `FILE_TYPE` | `VARCHAR2(32)` | Type of the file:  - `DATAFILE` - `CONTROLFILE` - `SPFILE` - `REDO` `LOG` - `ARCHIVED` `LOG` - `COPY` (for an image copy backup) - `PIECE` (for a backup piece) |
| `KEEP` | `VARCHAR2(3)` | Indicates whether the backup has a retention policy different from the value for `CONFIGURE RETENTION POLICY` (`YES`) or not (`NO`) |
| `KEEP_UNTIL` | `DATE` | If the `KEEP UNTIL TIME` clause of the `BACKUP` command was specified, then this column shows the date after which the backup becomes obsolete. If the column is null and `KEEP_OPTIONS` is not null, the backup never becomes obsolete. |
| `KEEP_OPTIONS` | `VARCHAR2(13)` | `KEEP` options for the backup:  - `LOGS` - RMAN keeps the logs needed to recover the backup - `NOLOGS` - RMAN does not keep the logs needed to recover the backup  If this column is null, then the backup has no KEEP options and will be made obsolete based on the retention policy. |
| `STATUS` | `VARCHAR2(16)` | Status of the backup:  - `AVAILABLE` - `UNAVAILABLE` - `EXPIRED` - `OTHER` |
| `FNAME` | `VARCHAR2(1024)` | Name of the file |
| `TAG` | `VARCHAR2(32)` | Tag of the piece, copy, or proxy copy |
| `MEDIA` | `VARCHAR2(80)` | Media ID of the piece or proxy copy |
| `RECID` | `NUMBER` | Recid of the record in the control file |
| `STAMP` | `NUMBER` | Stamp of the record in the control file |
| `DEVICE_TYPE` | `VARCHAR2(255)` | Type of media device that stores the backup |
| `BLOCK_SIZE` | `NUMBER` | Block size for the backup (in bytes) |
| `COMPLETION_TIME` | `DATE` | Time when the backup completed |
| `COMPRESSED` | `VARCHAR2(3)` | Indicates whether the backup piece is compressed (`YES`) or not (`NO`); valid only if `FILE_TYPE` is `PIECE`. Image copies cannot be compressed. |
| `OBSOLETE` | `VARCHAR2(3)` | Indicates whether the backup piece or copy is obsolete (`YES`) or not (`NO`); valid only if `FILE_TYPE` is `PIECE` or `COPY` |
| `BYTES` | `NUMBER` | Size of the file (in bytes) |
| `BS_KEY` | `NUMBER` | Primary key of the backup set (valid only if `BACKUP_TYPE` is `BACKUP SET`) |
| `BS_COUNT` | `NUMBER` | Count of the backup set from the control file record (valid only if `BACKUP_TYPE` is `BACKUP SET`) |
| `BS_STAMP` | `NUMBER` | Stamp of the backup set from the control file record (valid only if `BACKUP_TYPE` is `BACKUP SET`) |
| `BS_TYPE` | `VARCHAR2(32)` | Type of the backup set (valid only if `BACKUP_TYPE` is `BACKUP SET`):  - `DATAFILE` - `ARCHIVED LOG` |
| `BS_INCR_TYPE` | `VARCHAR2(32)` | Incremental type of the backup set (valid only if `BACKUP_TYPE` is `BACKUP SET`) |
| `BS_PIECES` | `NUMBER` | Number of backup pieces in the backup set (valid only if `BACKUP_TYPE` is `BACKUP SET`) |
| `BS_COPIES` | `NUMBER` | Number of copies of the backup set (valid only if `FILE_TYPE` is `PIECE` and `BACKUP_TYPE` is `BACKUP SET`) |
| `BS_COMPLETION_TIME` | `DATE` | Completion time of the backup set (valid only if `BACKUP_TYPE` is `BACKUP SET`) |
| `BS_STATUS` | `VARCHAR2(16)` | Status of the backup set (valid only if `BACKUP_TYPE` is `BACKUP SET`):  - `AVAILABLE` - `UNAVAILABLE` - `EXPIRED` - `OTHER` - Pieces which are part of the backup set do not have uniform status (that is, some of them are available, some not) |
| `BS_BYTES` | `NUMBER` | Sum of all backup piece sizes in the backup set (valid only if `BACKUP_TYPE` is `BACKUP SET`) |
| `BS_COMPRESSED` | `VARCHAR2(3)` | Indicates whether the backup pieces of the backup set are compressed (`YES`) or not (`NO`); valid only if `BACKUP_TYPE` is `BACKUP SET` |
| `BS_TAG` | `VARCHAR2(1024)` | Tags of the backup set. If pieces have different tags, then all piece tags are concatenated and separated by commas. Valid only if `BACKUP_TYPE` is `BACKUP SET`) |
| `BS_DEVICE_TYPE` | `VARCHAR2(255)` | Device type of the backup set. If there is more than one device type, then they are separated by commas. Valid only if `BACKUP_TYPE` is `BACKUP SET` |
| `BP_PIECE#` | `NUMBER` | Number of pieces inside the backup set (valid only if `FILE_TYPE` is `PIECE` and `BACKUP_TYPE` is `BACKUP SET`) |
| `BP_COPY#` | `NUMBER` | Number of copies of the backup set (valid only if `FILE_TYPE` is `PIECE` and `BACKUP_TYPE` is `BACKUP SET`) |
| `DF_FILE#` | `NUMBER` | Absolute file number of the data file (valid only if `FILE_TYPE` is `DATAFILE`) |
| `DF_TABLESPACE` | `VARCHAR2(30)` | Tablespace name of the data file (valid only if `FILE_TYPE` is `DATAFILE`) |
| `DF_RESETLOGS_CHANGE#` | `NUMBER` | System change number (SCN) of the most recent `RESETLOGS` when the control file or data file was created (valid only if `FILE_TYPE` is `DATAFILE`) |
| `DF_CREATION_CHANGE#` | `NUMBER` | Creation SCN of the control file or data file (valid only if `FILE_TYPE` is `CONTROLFILE` or `DATAFILE`) |
| `DF_CHECKPOINT_CHANGE#` | `NUMBER` | System change number (SCN) of the most recent control file or data file checkpoint (valid only if `FILE_TYPE` is `CONTROLFILE` or `DATAFILE`) |
| `DF_CKP_MOD_TIME` | `DATE` | Modification time in case of SPFILE, otherwise time when the control file or data file was checkpointed (valid only if `FILE_TYPE` is `SPFILE`, `CONTROLFILE`, or `DATAFILE`) |
| `RL_THREAD#` | `NUMBER` | Redo log thread number of the archived log (valid only if `FILE_TYPE` is `REDO LOG`) |
| `RL_SEQUENCE#` | `NUMBER` | Redo log sequence number of the archived log (valid only if `FILE_TYPE` is `REDO LOG`) |
| `RL_RESETLOGS_CHANGE#` | `NUMBER` | System change number (SCN) of the most recent `RESETLOGS` when the record was created (valid only if `FILE_TYPE` is `REDO LOG`) |
| `RL_FIRST_CHANGE#` | `NUMBER` | First SCN of the redo log (valid only if `FILE_TYPE` is `REDO LOG`) |
| `RL_FIRST_TIME` | `DATE` | Time when the Oracle Database switched into the redo log (valid only if `FILE_TYPE` is `REDO LOG`) |
| `RL_NEXT_CHANGE#` | `NUMBER` | First SCN of the next redo log in the thread (valid only if `FILE_TYPE` is `REDO LOG`) |
| `RL_NEXT_TIME` | `DATE` | First timestamp of the next redo log in the thread (valid only if `FILE_TYPE` is `REDO LOG`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=BRADV53532) for more information about the `DBMS_RCVMAN.SETDATABASE` procedure