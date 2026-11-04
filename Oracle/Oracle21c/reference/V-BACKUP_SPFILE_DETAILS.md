---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_SPFILE_DETAILS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.104 V$BACKUP\_SPFILE\_DETAILS

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |