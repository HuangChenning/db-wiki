---
title: ALL_LOB_PARTITIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1130.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_LOB_PARTITIONS` displays the LOB partitions in the tables accessible to the current user.

Related Views

- `DBA_LOB_PARTITIONS` displays all LOB partitions in the database.
- `USER_LOB_PARTITIONS` displays the LOB partitions owned by the current user. This view does not display the `TABLE_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(30)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the LOB column |
| `LOB_NAME` | `VARCHAR2(30)` |  | Name of the partitioned LOB item |
| `PARTITION_NAME` | `VARCHAR2(30)` |  | Name of the table partition |
| `LOB_PARTITION_NAME` | `VARCHAR2(30)` |  | Name of the LOB data partition |
| `LOB_INDPART_NAME` | `VARCHAR2(30)` |  | Name of the corresponding LOB index partition |
| `PARTITION_POSITION` | `NUMBER` |  | Position of the LOB data partition within the LOB item |
| `COMPOSITE` | `VARCHAR2(3)` |  | Indicates whether the partition is composite (`YES`) or not (`NO`) |
| `CHUNK` | `NUMBER` |  | Value of the `CHUNK` attribute of the LOB data partition |
| `PCTVERSION` | `NUMBER` |  | Value of the `PCTVERSION` attribute of the LOB data partition |
| `CACHE` | `VARCHAR2(10)` |  | Indicates whether and how the LOB data is to be cached in the buffer cache: - `YES` - LOB data is placed in the buffer cache - `NO` - LOB data either is not brought into the buffer cache or is brought into the buffer cache and placed at the least recently used end of the LRU list - `CACHEREADS` - LOB data is brought into the buffer cache only during read operations but not during write operations |
| `IN_ROW` | `VARCHAR2(3)` |  | Indicates whether the `STORAGE IN ROW` attribute is enabled for the LOB data partition (`YES`) or not (`NO`) |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing the LOB data partition |
| `INITIAL_EXTENT` | `VARCHAR2(40)` |  | Size (in bytes) of the initial extent of the LOB data partition, or `DEFAULT` |
| `NEXT_EXTENT` | `VARCHAR2(40)` |  | Size (in bytes) of secondary extents of the LOB data partition, or `DEFAULT` |
| `MIN_EXTENTS` | `VARCHAR2(40)` |  | Minimum number of extents allowed in the segment of the LOB data partition, or `DEFAULT` |
| `MAX_EXTENTS` | `VARCHAR2(40)` |  | Maximum number of extents allowed in the segment of the LOB data partition, or `DEFAULT` |
| `MAX_SIZE` | `VARCHAR2(40)` |  | Maximum number of blocks allowed in the segment of the LOB data partition, or `DEFAULT` |
| `RETENTION` | `VARCHAR2(7)` |  | Retention option.  Possible values for a SecureFiles segment:  - `NONE` - `AUTO` - `MIN` - `MAX` - `DEFAULT` - `INVALID`  Possible values for a BasicFiles segment:<sup>Foot 1</sup>  - `YES` - `NO` |
| `MINRETENTION` | `VARCHAR2(40)` |  | Minimum retention duration for a SecureFiles segment, or `DEFAULT` |
| `PCT_INCREASE` | `VARCHAR2(40)` |  | Percentage increase in extent size for the LOB data partition, or `DEFAULT` |
| `FREELISTS` | `VARCHAR2(40)` |  | Number of process freelists allocated in the segment of the LOB data partition, or `DEFAULT` |
| `FREELIST_GROUPS` | `VARCHAR2(40)` |  | Number of freelist groups allocated in the segment of the LOB data partition, or `DEFAULT` |
| `LOGGING` | `VARCHAR2(7)` |  | Indicates whether or not changes to the LOB are logged: - `NONE` - Not specified 	See Also: the `*_LOB_SUBPARTITIONS` view - `YES` - `NO` |
| `BUFFER_POOL` | `VARCHAR2(7)` |  | Buffer pool for the LOB partition blocks: - `DEFAULT` - `KEEP` - `RECYCLE` - NULL |
| `FLASH_CACHE` | `VARCHAR2(7)` |  | Database Smart Flash Cache hint to be used for partition blocks: - `DEFAULT` - `KEEP` - `NONE`  Solaris and Oracle Linux functionality only. |
| `CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | Cell flash cache hint to be used for partition blocks: - `DEFAULT` - `KEEP` - `NONE`  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `ENCRYPT` | `VARCHAR2(4)` |  | Indicates whether or not the LOB is encrypted.  Possible values for SecureFiles:  - `YES` - `NO`  Possible value for BasicFiles:  - `NONE` - Not applicable |
| `COMPRESSION` | `VARCHAR2(6)` |  | Level of compression used for this LOB.  Possible values for SecureFiles:  - `LOW` - `MEDIUM` - `HIGH` - `NO` - Compression is off  Possible value for BasicFiles:  - `NONE` - Not applicable |
| `DEDUPLICATION` | `VARCHAR2(15)` |  | Kind of deduplication used for this LOB.  Possible values for SecureFiles:  - `LOB` - Deduplicate - `NO` - Keep duplicates  Possible value for BasicFiles:  - `NONE` - Not applicable |
| `SECUREFILE` | `VARCHAR2(3)` |  | Indicates whether the LOB is SecureFiles (`YES`) or not (`NO`) |
| `SEGMENT_CREATED` | `VARCHAR2(3)` |  | Indicates whether the LOB partition segment has been created (`YES`) or not (`NO`); `N/A` indicates that this LOB is subpartitioned and no segment exists at the partition level |

<sup>Footnote 1</sup> The values listed for a BasicFiles segment are supported starting with Oracle Database 11g Release 2 (11.2.0.2). In previous releases, the value for this column for a BasicFiles segment is NULL.