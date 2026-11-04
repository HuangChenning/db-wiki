---
title: DBA_EXTENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3178.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_EXTENTS` describes the extents comprising the segments in all tablespaces in the database.

Note that if a datafile (or entire tablespace) is offline in a locally managed tablespace, you will not see any extent information. If an object has extents in an online file of the tablespace, you will see extent information about the offline datafile. However, if the object is entirely in the offline file, a query of this view will not return any records.

Related View

`USER_EXTENTS` describes the extents comprising the segments owned by the current user's objects. This view does not display the `OWNER`, `FILE_ID`, `BLOCK_ID`, or `RELATIVE_FNO` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the segment associated with the extent |
| `SEGMENT_NAME` | `VARCHAR2(81)` |  | Name of the segment associated with the extent |
| `PARTITION_NAME` | `VARCHAR2(30)` |  | Object Partition Name (Set to NULL for non-partitioned objects) |
| `SEGMENT_TYPE` | `VARCHAR2(18)` |  | Type of the segment: `INDEX PARTITION, TABLE PARTITION` |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing the extent |
| `EXTENT_ID` | `NUMBER` |  | Extent number in the segment |
| `FILE_ID` | `NUMBER` |  | File identifier number of the file containing the extent |
| `BLOCK_ID` | `NUMBER` |  | Starting block number of the extent |
| `BYTES` | `NUMBER` |  | Size of the extent in bytes |
| `BLOCKS` | `NUMBER` |  | Size of the extent in Oracle blocks |
| `RELATIVE_FNO` | `NUMBER` |  | Relative file number of the first extent block |

See Also:

["USER\_EXTENTS"](statviews_5301.md)