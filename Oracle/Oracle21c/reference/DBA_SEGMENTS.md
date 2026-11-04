---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SEGMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.353 DBA\_SEGMENTS

`DBA_SEGMENTS` describes the storage allocated for all segments in the database.

Related View

`USER_SEGMENTS` describes the storage allocated for the segments owned by the current user's objects. This view does not display the `OWNER`, `HEADER_FILE`, `HEADER_BLOCK`, or `RELATIVE_FNO` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Username of the segment owner |
| `SEGMENT_NAME` | `VARCHAR2(128)` |  | Name, if any, of the segment |
| `PARTITION_NAME` | `VARCHAR2(128)` |  | Object Partition Name (Set to `NULL` for nonpartitioned objects) |
| `SEGMENT_TYPE` | `VARCHAR2(18)` |  | Type of segment:  - `NESTED TABLE` - `TABLE` - `TABLE PARTITION` - `CLUSTER` - `LOBINDEX` - `INDEX` - `INDEX PARTITION` - `LOBSEGMENT` - `TABLE SUBPARTITION` - `INDEX SUBPARTITION` - `LOB PARTITION` - `LOB SUBPARTITION` - `ROLLBACK` - `TYPE2 UNDO` - `DEFERRED ROLLBACK` - `TEMPORARY` - `CACHE` - `SPACE HEADER` - `UNDEFINED` |
| `SEGMENT_SUBTYPE` | `VARCHAR2(10)` |  | Subtype of LOB segment: `SECUREFILE`, `ASSM`, `MSSM`, and `NULL` |
| `TABLESPACE_NAME ` | `VARCHAR2(30)` |  | Name of the tablespace containing the segment |
| `HEADER_FILE ` | `NUMBER` |  | Absolute file number of the data file containing the segment header |
| `HEADER_BLOCK` | `NUMBER` |  | ID of the block containing the segment header |
| `BYTES ` | `NUMBER` |  | Size, in bytes, of the segment |
| `BLOCKS ` | `NUMBER` |  | Size, in Oracle blocks, of the segment |
| `EXTENTS` | `NUMBER` |  | Number of extents allocated to the segment |
| `INITIAL_EXTENT` | `NUMBER` |  | Size in bytes requested for the initial extent of the segment at create time. (Oracle rounds the extent size to multiples of 5 blocks if the requested size is greater than 5 blocks.) |
| `NEXT_EXTENT ` | `NUMBER` |  | Size in bytes of the next extent to be allocated to the segment |
| `MIN_EXTENTS` | `NUMBER` |  | Minimum number of extents allowed in the segment |
| `MAX_EXTENTS` | `NUMBER` |  | Maximum number of extents allowed in the segment |
| `MAX_SIZE` | `NUMBER` |  | Maximum number of blocks allowed in the segment |
| `RETENTION` | `VARCHAR2(7)` |  | Retention option for `SECUREFILE` segment |
| `MINRETENTION` | `NUMBER` |  | Minimum retention duration for `SECUREFILE` segment |
| `PCT_INCREASE ` | `NUMBER` |  | Percent by which to increase the size of the next extent to be allocated |
| `FREELISTS ` | `NUMBER` |  | Number of process freelists allocated to this segment |
| `FREELIST_GROUPS ` | `NUMBER` |  | Number of freelist groups allocated to this segment |
| `RELATIVE_FNO` | `NUMBER` |  | Relative file number of the segment header |
| `BUFFER_POOL` | `VARCHAR2(7)` |  | Buffer pool to be used for segment blocks:  - `DEFAULT` - `KEEP` - `RECYCLE` |
| `FLASH_CACHE` | `VARCHAR2(7)` |  | Database Smart Flash Cache hint to be used for segment blocks:  - `DEFAULT` - `KEEP` - `NONE`  Solaris and Oracle Linux functionality only. |
| `CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | Cell flash cache hint to be used for segment blocks:  - `DEFAULT` - `KEEP` - `NONE`  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `INMEMORY` | `VARCHAR2(8)` |  | Indicates whether the In-Memory Column Store (IM column store) is enabled (`ENABLED`) or disabled (`DISABLED`) for this segment |
| `INMEMORY_PRIORITY` | `VARCHAR2(8)` |  | Indicates the priority for In-Memory Column Store (IM column store) population:  - `LOW` - `MEDIUM` - `HIGH` - `CRITICAL` - `NONE` - `NULL` |
| `INMEMORY_DISTRIBUTE` | `VARCHAR2(15)` |  | Indicates how the IM column store is distributed in an Oracle Real Application Clusters (Oracle RAC) environment:  - `AUTO` - `BY ROWID RANGE` - `BY PARTITION` - `BY SUBPARTITION` |
| `INMEMORY_DUPLICATE` | `VARCHAR2(13)` |  | Indicates the duplicate setting for the IM column store in an Oracle RAC environment:  - `NO DUPLICATE` - `DUPLICATE` - `DUPLICATE ALL` |
| `INMEMORY_COMPRESSION` | `VARCHAR2(17)` |  | Indicates the compression level for the IM column store:  - `NO MEMCOMPRESS` - `FOR DML` - `FOR QUERY [ LOW \| HIGH ]` - `FOR CAPACITY [ LOW \| HIGH ]` - `AUTO` - `NULL` |
| `CELLMEMORY` <sup>Foot 1</sup> <sup>Foot 1</sup> | `VARCHAR2(24)` |  | The value for columnar compression in the storage cell flash cache. Possible values:  - `ENABLED`: Oracle Exadata Storage will decide automatically whether to cache in columnar form - `DISABLED`: Oracle Exadata Storage is prevented from caching in columnar form - `NO CACHECOMPRESS`: Oracle Exadata Storage will cache in HCC format (no recompression) - `FOR QUERY`: Oracle Exadata Storage will recompress and cache in INMEMORY query high format - `FOR CAPACITY`: Oracle Exadata Storage will recompress and cache in INMEMORY capacity low format |

<sup>Footnote 1</sup>

This column is intended for use with Oracle Exadata

See Also:

" [USER\_SEGMENTS](USER_SEGMENTS.md) "