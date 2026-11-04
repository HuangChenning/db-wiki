---
title: "V$BACKUP_ARCHIVELOG_DETAILS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1045.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BACKUP_ARCHIVELOG_DETAILS` contains information about all restorable archive logs. It will include all archived logs backed up in a backup set or proxy copies.

| Column | Datatype | Description |
| --- | --- | --- |
| `BTYPE` | `CHAR(9)` | Backup type container, either `BACKUPSET` or `PROXYCOPY` |
| `BTYPE_KEY` | `NUMBER` | Unique identifier for the backup type. For `BACKUPSET`, it is `BS_KEY`. |
| `SESSION_KEY` | `NUMBER` | Session identifier |
| `SESSION_RECID` | `NUMBER` | Session recid |
| `SESSION_STAMP` | `NUMBER` | Session stamp |
| `ID1` | `NUMBER` | If `BACKUPSET`, it contains `SET_STAMP`  If `PROXYCOPY`, it is `RECID` from the control file |
| `ID2` | `NUMBER` | If `BACKUPSET`, it contains `SET_COUNT`  If `PROXYCOPY`, it is `STAMP` |
| `THREAD#` | `NUMBER` | Thread number |
| `SEQUENCE#` | `NUMBER` | Sequence number |
| `RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs change SCN |
| `RESETLOGS_TIME` | `DATE` | Resetlogs change time |
| `FIRST_CHANGE#` | `NUMBER` | First change SCN |
| `FIRST_TIME` | `DATE` | First change time |
| `NEXT_CHANGE#` | `NUMBER` | Next change SCN |
| `NEXT_TIME` | `DATE` | Next change time |
| `FILESIZE` | `NUMBER` | File size |
| `COMPRESSION_RATIO` | `NUMBER` | The ratio between the total blocks in the archive log and the blocks that RMAN backed up. This is not the ratio from the `AS COMPRESSED BACKUPSET` clause of the `BACKUP` command. |
| `FILESIZE_DISPLAY` | `VARCHAR2(4000)` | Same value as the `FILESIZE` column, but converted to a user-displayable format, for example `n` M, `n` G, `n` T, `n` P, and so on |