---
title: "V$PROXY_ARCHIVEDLOG"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2105.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PROXY_ARCHIVEDLOG` contains descriptions of archived log backups that were taken using the proxy copy functionality.

In a proxy copy, the media manager takes over the operations of backing up and restoring data. Each row represents a backup of one control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Proxy copy record identifier |
| `STAMP` | `NUMBER` | Proxy copy stamp |
| `DEVICE_TYPE` | `VARCHAR2(17)` | Type of media device that stores the proxy copy |
| `HANDLE` | `VARCHAR2(513)` | Name or "handle" for the proxy copy |
| `COMMENTS` | `VARCHAR2(81)` | Comments about the proxy copy |
| `MEDIA` | `VARCHAR2(65)` | A comment that contains further information about the media manager that created this backup |
| `MEDIA_POOL` | `NUMBER` | Number of the media pool in which the proxy copy is stored |
| `TAG` | `VARCHAR2(32)` | Tag for the proxy copy |
| `STATUS` | `VARCHAR2(1)` | Status of the backup set: - `A` - Available - `U` - Unavailable - `X` - Expired - `D` - Deleted |
| `DELETED` | `VARCHAR2(3)` | Indicates whether this record has been deleted (`YES`) or not (`NO`) |
| `THREAD#` | `NUMBER` | Number of the redo thread |
| `SEQUENCE#` | `NUMBER` | Log sequence number |
| `RESETLOGS_CHANGE#` | `NUMBER` | `RESETLOGS` SCN of the database incarnation to which this archived log belongs |
| `RESETLOGS_TIME` | `DATE` | `RESETLOGS` time stamp of the database incarnation to which this archived log belongs |
| `FIRST_CHANGE#` | `NUMBER` | First SCN of this redo log |
| `FIRST_TIME` | `DATE` | Time when Oracle switched into the redo log |
| `NEXT_CHANGE#` | `NUMBER` | First SCN of the next redo log in the thread |
| `NEXT_TIME` | `DATE` | First time stamp of the next redo log in the thread |
| `BLOCKS` | `NUMBER` | Size of this archived redo log (in operating system blocks) |
| `BLOCK_SIZE` | `NUMBER` | Block size for the copy (in bytes) |
| `START_TIME` | `DATE` | Time when the proxy copy was initiated |
| `COMPLETION_TIME` | `DATE` | Time when the proxy copy was completed |
| `ELAPSED_SECONDS` | `NUMBER` | Duration of the proxy copy |
| `RMAN_STATUS_RECID` | `NUMBER` | Owning `V$RMAN_STATUS` record ID |
| `RMAN_STATUS_STAMP` | `NUMBER` | Owning `V$RMAN_STATUS` stamp |
| `TERMINAL` | `VARCHAR2(3)` | Indicates whether this record corresponds to a terminal archived redo log, as defined in `V$ARCHIVED_LOG` (`YES`) or not (`NO`) |
| `KEEP` | `VARCHAR2(3)` | Indicates whether this backup set has a retention policy that is different than the value for the configure retention policy (`YES`) or not (`NO`) |
| `KEEP_UNTIL` | `DATE` | If specified, then this is the date after which the backup becomes obsolete. If this column is `NULL`, then the backup never expires. |
| `KEEP_OPTIONS` | `VARCHAR2(11)` | Additional retention options for this backup set: - `LOGS` - Indicates a long-term backup made with the LOGS keyword, which is now deprecated - `BACKUP_LOGS` - Indicates that the backup was made in open mode, so archived log backups must be applied to make it consistent - `NOLOGS` - Indicates a consistent backup made when the database was mounted - `NULL` - Indicates that this backup has no KEEP options and becomes obsolete based on the retention policy |