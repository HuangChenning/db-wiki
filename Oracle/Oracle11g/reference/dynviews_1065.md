---
title: "V$BACKUP_SPFILE_DETAILS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1065.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BACKUP_SPFILE_DETAILS` displays information about all restorable SP files backed up in the backup set.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_KEY` | `NUMBER` | Session identifier |
| `SESSION_RECID` | `NUMBER` | Session recid |
| `SESSION_STAMP` | `NUMBER` | Session stamp |
| `BS_KEY` | `NUMBER` | Unique backup set identifier |
| `SET_STAMP` | `NUMBER` | Backup set stamp |
| `SET_COUNT` | `NUMBER` | Backup set count |
| `MODIFICATION_TIME` | `DATE` | Time the backup set was modified |
| `FILESIZE` | `NUMBER` | Size, in bytes, of the SPFILE that was backed up |
| `FILESIZE_DISPLAY` | `VARCHAR2(4000)` | Same value as the `FILESIZE` column, but converted to a user-displayable format, for example `n` M, `n` G, `n` T, `n` P, and so on |