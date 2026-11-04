---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_SET_DETAILS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.101 V$BACKUP\_SET\_DETAILS

`V$BACKUP_SET_DETAILS` provides detailed information about the backup set.

This view will contain an extra row for each backup session that invokes BACKUP BACKUPSET (that is, creates new copies for the same backup set or copies backup set information from disk to tape). However, the remaining values of other columns belong to the complete backup set.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_KEY` | `NUMBER` | Session identifier |
| `SESSION_RECID` | `NUMBER` | Identifies the job, together with `SESSION_STAMP`. |
| `SESSION_STAMP` | `NUMBER` | Identifies the job, together with `SESSION_RECID` |
| `BS_KEY` | `NUMBER` | Backup set identifier |
| `RECID` | `NUMBER` | RECID from `V$BACKUP_SET` record |
| `STAMP` | `NUMBER` | Stamp from `V$BACKUP_SET` record |
| `SET_STAMP` | `NUMBER` | Backup set stamp |
| `SET_COUNT` | `NUMBER` | Backup count number |
| `BACKUP_TYPE` | `VARCHAR2(1)` | Type of backup (same as in `V$BACKUP_SET)` |
| `CONTROLFILE_INCLUDED` | `VARCHAR2(3)` | Control file included in backup set (same as in `V$BACKUP_SET`) |
| `INCREMENTAL_LEVEL` | `NUMBER` | Incremental level (same as in `V$BACKUP_SET`) |
| `PIECES` | `NUMBER` | Number of pieces (same as in `V$BACKUP_SET`) |
| `START_TIME` | `DATE` | Start time of the backup set (same as in `V$BACKUP_SET`) |
| `COMPLETION_TIME` | `DATE` | Completion time of the backup set (same as in `V$BACKUP_SET`) |
| `ELAPSED_SECONDS` | `NUMBER` | Time taken for backup set creation (same as in `V$BACKUP_SET`) |
| `BLOCK_SIZE` | `NUMBER` | Block size (same as in `V$BACKUP_SET`) |
| `KEEP` | `VARCHAR2(3)` | Keep value (same as in `V$BACKUP_SET`) |
| `KEEP_UNTIL` | `DATE` | Keep Until time (same as in `V$BACKUP_SET`) |
| `KEEP_OPTIONS` | `VARCHAR2(11)` | Keep options (same as in `V$BACKUP_SET`) |
| `DEVICE_TYPE` | `VARCHAR2(17)` | Type of device. If the backup set exists on more than one device type, an \* is indicated here. |
| `COMPRESSED` | `VARCHAR2(3)` | `YES`, if backup is compressed |
| `NUM_COPIES` | `NUMBER` | Number of identical copies |
| `OUTPUT_BYTES` | `NUMBER` | Size of the backup set |
| `ORIGINAL_INPUT_BYTES` | `NUMBER` | Amount of data backed up when the backup set was created |
| `COMPRESSION_RATIO` | `NUMBER` | The ratio between the total blocks in the datafile and the blocks that RMAN backed up. This is not the the ratio from the `AS COMPRESSED BACKUPSET` clause of the `BACKUP` command. |
| `STATUS` | `CHAR(1)` | The status of the backup set. It is always `A` (all backup pieces available), because this view only reflects available backup sets. |
| `ORIGINAL_INPRATE_BYTES` | `NUMBER` | Number of bytes read per second when backup set was initially created |
| `OUTPUT_RATE_BYTES` | `NUMBER` | Number of bytes written per second when the backup set was initially created |
| `ORIGINAL_INPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Input rate to display |
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Size of backup set to display |
| `ORIGINAL_INPRATE_BYTES_DISPLAY` | `VARCHAR2(4000)` | Input rate per second for display |
| `OUTPUT_RATE_BYTES_DISPLAY` | `VARCHAR2(4000)` | Output rate per second for display |
| `TIME_TAKEN_DISPLAY` | `VARCHAR2(4000)` | Elapsed time in hh:mm:ss format |
| `ENCRYPTED` | `VARCHAR2(3)` | A value of `YES` means an encrypted backup, otherwise not an encrypted backup. |
| `BACKED_BY_OSB` | `VARCHAR2(3)` | A value of `YES` means the backup was done to Oracle Secure Backup. Otherwise, backed up by other third party tape library. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$BACKUP\_SET](V-BACKUP_SET.md) "