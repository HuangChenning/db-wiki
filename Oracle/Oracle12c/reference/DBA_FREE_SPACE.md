---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_FREE_SPACE.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_FREE_SPACE` describes the free extents in all tablespaces in the database.

Note that if a data file (or entire tablespace) is offline in a locally managed tablespace, you will not see any extent information. If an object has extents in an online file of the tablespace, you will see extent information about the offline data file. However, if the object is entirely in the offline file, a query of this view will not return any records.

Related View

`USER_FREE_SPACE` describes the free extents in the tablespaces accessible to the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing the extent |
| `FILE_ID` | `NUMBER` |  | Absolute file number of the data file containing the extent |
| `BLOCK_ID` | `NUMBER` |  | Starting block number of the extent |
| `BYTES` | `NUMBER` |  | Size of the extent (in bytes) |
| `BLOCKS` | `NUMBER` |  | Size of the extent (in Oracle blocks) |
| `RELATIVE_FNO` | `NUMBER` |  | Relative file number of the file containing the extent |

See Also:

" [USER\_FREE\_SPACE](USER_FREE_SPACE.md) "