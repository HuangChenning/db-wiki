---
title: DBA_SEGMENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4267.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SEGMENTS` describes the storage allocated for all segments in the database.

Related View

`USER_SEGMENTS` describes the storage allocated for the segments owned by the current user's objects. This view does not display the `OWNER`, `HEADER_FILE`, `HEADER_BLOCK`, or `RELATIVE_FNO` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Username of the segment owner |
| `SEGMENT_NAME` | `VARCHAR2(81)` |  | Name, if any, of the segment |
| `PARTITION_NAME` | `VARCHAR2(30)` |  | Object Partition Name (Set to `NULL` for non-partitioned objects) |
| `SEGMENT_TYPE` | `VARCHAR2(18)` |  | Type of segment: - `NESTED TABLE` - `TABLE` - `TABLE PARTITION` - `CLUSTER` - `LOBINDEX` - `INDEX` - `INDEX PARTITION` - `LOBSEGMENT` - `TABLE SUBPARTITION` - `INDEX SUBPARTITION` - `LOB PARTITION` - `LOB SUBPARTITION` - `ROLLBACK` - `TYPE2 UNDO` - `DEFERRED ROLLBACK` - `TEMPORARY` - `CACHE` - `SPACE HEADER` - `UNDEFINED` |
| `SEGMENT_SUBTYPE` | `VARCHAR2(10)` |  | Subtype of LOB segment: `SECUREFILE`, `ASSM`, `MSSM`, and `NULL` |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing the segment |
| `HEADER_FILE` | `NUMBER` |  | ID of the file containing the segment header |
| `HEADER_BLOCK` | `NUMBER` |  | ID of the block containing the segment header |
| `BYTES` | `NUMBER` |  | Size, in bytes, of the segment |
| `BLOCKS` | `NUMBER` |  | Size, in Oracle blocks, of the segment |
| `EXTENTS` | `NUMBER` |  | Number of extents allocated to the segment |
| `INITIAL_EXTENT` | `NUMBER` |  | Size in bytes requested for the initial extent of the segment at create time. (Oracle rounds the extent size to multiples of 5 blocks if the requested size is greater than 5 blocks.) |
| `NEXT_EXTENT` | `NUMBER` |  | Size in bytes of the next extent to be allocated to the segment |
| `MIN_EXTENTS` | `NUMBER` |  | Minimum number of extents allowed in the segment |
| `MAX_EXTENTS` | `NUMBER` |  | Maximum number of extents allowed in the segment |
| `MAX_SIZE` | `NUMBER` |  | Maximum number of blocks allowed in the segment |
| `RETENTION` | `VARCHAR2(7)` |  | Retention option for `SECUREFILE` segment |
| `MINRETENTION` | `NUMBER` |  | Minimum retention duration for `SECUREFILE` segment |
| `PCT_INCREASE` | `NUMBER` |  | Percent by which to increase the size of the next extent to be allocated |
| `FREELISTS` | `NUMBER` |  | Number of process freelists allocated to this segment |
| `FREELIST_GROUPS` | `NUMBER` |  | Number of freelist groups allocated to this segment |
| `RELATIVE_FNO` | `NUMBER` |  | Relative file number of the segment header |
| `BUFFER_POOL` | `VARCHAR2(7)` |  | Buffer pool to be used for segment blocks: |
| `FLASH_CACHE` | `VARCHAR2(7)` |  | Database Smart Flash Cache hint to be used for segment blocks:  Solaris and Oracle Linux functionality only. |
| `CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | Cell flash cache hint to be used for segment blocks:  See Also: Oracle Exadata Storage Server Software documentation for more information |

See Also:

["USER\_SEGMENTS"](statviews_5445.md)