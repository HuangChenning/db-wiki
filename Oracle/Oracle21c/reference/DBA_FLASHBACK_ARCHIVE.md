---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_FLASHBACK_ARCHIVE.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.329 DBA\_FLASHBACK\_ARCHIVE

`DBA_FLASHBACK_ARCHIVE` describes all flashback archives available in the database.

Related View

`USER_FLASHBACK_ARCHIVE` describes the flashback archives available to the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER_NAME` | `VARCHAR2(255)` |  | Name of the creator of the flashback archive |
| `FLASHBACK_ARCHIVE_NAME` | `VARCHAR2(255)` | `NOT NULL` | Name of the flashback archive |
| `FLASHBACK_ARCHIVE#` | `NUMBER` | `NOT NULL` | Number of the flashback archive |
| `RETENTION_IN_DAYS` | `NUMBER` | `NOT NULL` | Maximum duration (in days) for which data is retained in the flashback archive |
| `CREATE_TIME` | `TIMESTAMP(9)` |  | Time at which the flashback archive was created |
| `LAST_PURGE_TIME` | `TIMESTAMP(9)` |  | Time at which the data in the flashback archive was last purged by the system |
| `STATUS` | `VARCHAR2(7)` |  | Indicates whether the flashback archive is a default flashback archive for the system (`DEFAULT`) or not (NULL) |

See Also:

" [USER\_FLASHBACK\_ARCHIVE](USER_FLASHBACK_ARCHIVE.md) "