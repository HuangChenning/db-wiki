---
title: DBA_FLASHBACK_ARCHIVE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3189.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_FLASHBACK_ARCHIVE` describes all flashback archives available in the database.

Related View

`USER_FLASHBACK_ARCHIVE` describes the flashback archives available to the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER_NAME` | `VARCHAR2(30)` |  | Name of the creator of the flashback archive |
| `FLASHBACK_ARCHIVE_NAME` | `VARCHAR2(255)` | `NOT NULL` | Name of the flashback archive |
| `FLASHBACK_ARCHIVE#` | `NUMBER` | `NOT NULL` | Number of the flashback archive |
| `RETENTION_IN_DAYS` | `NUMBER` | `NOT NULL` | Maximum duration (in days) for which data is retained in the flashback archive |
| `CREATE_TIME` | `TIMESTAMP(9)` |  | Time at which the flashback archive was created |
| `LAST_PURGE_TIME` | `TIMESTAMP(9)` |  | Time at which the data in the flashback archive was last purged by the system |
| `STATUS` | `VARCHAR2(7)` |  | Indicates whether the flashback archive is a default flashback archive for the system (`DEFAULT`) or not (NULL) |

See Also:

["USER\_FLASHBACK\_ARCHIVE"](statviews_5310.md)