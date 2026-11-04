---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_EXTENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.317 DBA\_EXTENTS

`DBA_EXTENTS` describes the extents comprising the segments in all tablespaces in the database.

Note that if a data file (or entire tablespace) is offline in a locally managed tablespace, you will not see any extent information. If an object has extents in an online file of the tablespace, you will see extent information about the offline data file. However, if the object is entirely in the offline file, a query of this view will not return any records.

Related View

`USER_EXTENTS` describes the extents comprising the segments owned by the current user's objects. This view does not display the `OWNER`, `FILE_ID`, `BLOCK_ID`, or `RELATIVE_FNO` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the segment associated with the extent |
| `SEGMENT_NAME` | `VARCHAR2(128)` |  | Name of the segment associated with the extent |
| `PARTITION_NAME` | `VARCHAR2(128)` |  | Object Partition Name (Set to NULL for nonpartitioned objects) |
| `SEGMENT_TYPE` | `VARCHAR2(18)` |  | Type of the segment: `INDEX PARTITION, TABLE PARTITION` |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing the extent |
| `EXTENT_ID ` | `NUMBER` |  | Extent number in the segment |
| `FILE_ID ` | `NUMBER` |  | Absolute file number of the data file containing the extent |
| `BLOCK_ID` | `NUMBER` |  | Starting block number of the extent |
| `BYTES ` | `NUMBER` |  | Size of the extent in bytes |
| `BLOCKS` | `NUMBER` |  | Size of the extent in Oracle blocks |
| `RELATIVE_FNO` | `NUMBER` |  | Relative file number of the first extent block |

See Also:

" [USER\_EXTENTS](USER_EXTENTS.md) "