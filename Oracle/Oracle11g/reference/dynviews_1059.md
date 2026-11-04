---
title: "V$BACKUP_PIECE_DETAILS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1059.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BACKUP_PIECE_DETAILS` displays information about all available backup pieces.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_KEY` | `NUMBER` | Session identifier |
| `SESSION_RECID` | `NUMBER` | Session recid |
| `SESSION_STAMP` | `NUMBER` | Session stamp |
| `BS_KEY` | `NUMBER` | Backup set identifier |
| `BP_KEY` | `NUMBER` | Backup piece key |
| `RECID` | `NUMBER` | Backup piece record ID |
| `STAMP` | `NUMBER` | Backup piece record stamp |
| `SET_STAMP` | `NUMBER` | Backup set stamp |
| `SET_COUNT` | `NUMBER` | Backup set count |
| `PIECE#` | `NUMBER` | Backup piece number (1-N) |
| `COPY#` | `NUMBER` | Indicates the copy number for backup pieces created with duplex enabled. The value is 1 if the backup piece is not duplexed. |
| `DEVICE_TYPE` | `VARCHAR2(17)` | Type of device on which the backup piece resides. Set to DISK for backup sets on disk. |
| `HANDLE` | `VARCHAR2(513)` | Backup piece handle identifies the backup piece on restore |
| `COMMENTS` | `VARCHAR2(64)` | Comments returned by the operating system or storage subsystem. Set to NULL for backup pieces on disk. This value is informational only. It is not needed for restore. |
| `MEDIA` | `VARCHAR2(65)` | Name of the media on which the backup piece resides. This value is informational only. It is not needed for restore. |
| `MEDIA_POOL` | `NUMBER` | The media pool in which the copy resides. This is the same value that was entered in the `POOL` operand of the Recovery Manager `BACKUP` command. |
| `CONCUR` | `VARCHAR2(3)` | (YES\|NO) indicates whether or not the piece is on a media that can be accessed concurrently |
| `TAG` | `VARCHAR2(32)` | Backup piece tag. The tag is specified at backup set level, but stored at piece level. |
| `STATUS` | `VARCHAR2(1)` | Indicates the status of the piece: `A` (available), `D` (deleted), or `X` (expired) |
| `START_TIME` | `DATE` | Starting time |
| `COMPLETION_TIME` | `DATE` | Completion time |
| `ELAPSED_SECONDS` | `NUMBER` | Number of elapsed seconds |
| `DELETED` | `VARCHAR2(3)` | `NO` indicates that the file still exists. `YES` indicates that the file no longer exists because it has been deleted. |
| `BYTES` | `NUMBER` | Size of the backup piece, in bytes |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | Indicates whether or not the file was created in the fast recovery area (`YES`) or not (`NO`) |
| `RMAN_STATUS_RECID` | `NUMBER` | Owning `V$RMAN_STATUS` record ID |
| `RMAN_STATUS_STAMP` | `NUMBER` | Owning `V$RMAN_STATUS` record stamp |
| `COMPRESSED` | `VARCHAR2(3)` | Indicates whether the backup piece is compressed (`YES`) or not (`NO`) |
| `BACKED_BY_VSS` | `VARCHAR2(3)` | Whether or not the file has been backed up by Volume Shadow Copy Service (VSS). This column is reserved for internal use. |
| `ENCRYPTED` | `VARCHAR2(3)` | A value of `YES` means an encrypted backup, otherwise not an encrypted backup. |
| `BACKED_BY_OSB` | `VARCHAR2(3)` | A value of `YES` means the backup was done to Oracle Secure Backup. Otherwise, backed up by other third party tape library. |
| `PIECES_PER_SET` | `NUMBER` | Number of backup pieces per set |
| `SIZE_BYTES_DISPLAY` | `VARCHAR2(4000)` | Size (in bytes) of the backup piece to display |