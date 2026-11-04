---
title: DBA_FREE_SPACE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3194.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_FREE_SPACE` describes the free extents in all tablespaces in the database.

Note that if a datafile (or entire tablespace) is offline in a locally managed tablespace, you will not see any extent information. If an object has extents in an online file of the tablespace, you will see extent information about the offline datafile. However, if the object is entirely in the offline file, a query of this view will not return any records.

Related View

`USER_FREE_SPACE` describes the free extents in the tablespaces accessible to the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing the extent |
| `FILE_ID` | `NUMBER` |  | File identifier number of the file containing the extent |
| `BLOCK_ID` | `NUMBER` |  | Starting block number of the extent |
| `BYTES` | `NUMBER` |  | Size of the extent (in bytes) |
| `BLOCKS` | `NUMBER` |  | Size of the extent (in Oracle blocks) |
| `RELATIVE_FNO` | `NUMBER` |  | Relative file number of the file containing the extent |

See Also:

["USER\_FREE\_SPACE"](statviews_5314.md)