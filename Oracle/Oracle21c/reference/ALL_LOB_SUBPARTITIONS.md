---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_LOB_SUBPARTITIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.261 ALL\_LOB\_SUBPARTITIONS

`ALL_LOB_SUBPARTITIONS` displays partition-level attributes of the LOB data subpartitions accessible to the current user.

Related Views

- `DBA_LOB_SUBPARTITIONS` displays partition-level attributes of all LOB data subpartitions in the database.
- `USER_LOB_SUBPARTITIONS` displays the LOB subpartitions owned by the current user. This view does not display the `TABLE_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the LOB column |
| `LOB_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the partitioned LOB item |
| `LOB_PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the LOB data partition to which this LOB data subpartition belongs |
| `SUBPARTITION_NAME` | `VARCHAR2(128)` |  | Name of the table subpartition to which this LOB subpartition corresponds |
| `LOB_SUBPARTITION_NAME` | `VARCHAR2(128)` |  | Name of the LOB subpartition |
| `LOB_INDSUBPART_NAME` | `VARCHAR2(128)` |  | Name of the corresponding LOB index subpartition |
| `SUBPARTITION_POSITION` | `NUMBER` |  | Position of the LOB data partition within the LOB item |
| `CHUNK` | `NUMBER` |  | Value of the `CHUNK` attribute of the LOB data partition |
| `PCTVERSION` | `NUMBER` | `NOT NULL` | Value of the `PCTVERSION` attribute of the LOB data partition |
| `CACHE` | `VARCHAR2(10)` |  | Indicates whether and how the LOB data is to be cached in the buffer cache:  - `YES` - LOB data is placed in the buffer cache - `NO` - LOB data either is not brought into the buffer cache or is brought into the buffer cache and placed at the least recently used end of the LRU list - `CACHEREADS` - LOB data is brought into the buffer cache only during read operations but not during write operations |
| `IN_ROW` | `VARCHAR2(3)` |  | Indicates whether the `STORAGE IN ROW` attribute of the LOB data partition is enabled (`YES`) or not (`NO`) |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace containing the LOB data partition |
| `INITIAL_EXTENT` | `VARCHAR2(40)` |  | Size in bytes of the initial extent for the LOB data partition |
| `NEXT_EXTENT` | `VARCHAR2(40)` |  | Size in bytes of secondary extents for the LOB data partition |
| `MIN_EXTENTS` | `VARCHAR2(40)` | `NOT NULL` | Minimum number of extents allowed in the segment of the LOB data partition |
| `MAX_EXTENTS` | `VARCHAR2(40)` | `NOT NULL` | Maximum number of extents allowed in the segment of the LOB data partition |
| `MAX_SIZE` | `VARCHAR2(40)` |  | Maximum number of blocks allowed in the segment of the LOB data partition |
| `RETENTION` | `VARCHAR2(7)` |  | Retention option.  Possible values for a SecureFiles segment:  - `NONE` - `AUTO` - `MIN` - `MAX` - `DEFAULT` - `INVALID`  Possible values for a BasicFiles segment:  - `YES` - `NO` |
| `MINRETENTION` | `VARCHAR2(40)` |  | Minimum retention duration for a SecureFiles segment |
| `PCT_INCREASE` | `VARCHAR2(40)` |  | Percentage increase in extent size for the LOB data partition |
| `FREELISTS` | `VARCHAR2(40)` |  | Number of process freelists allocated in the segment of the LOB data partition |
| `FREELIST_GROUPS` | `VARCHAR2(40)` |  | Number of freelist groups allocated in the segment of the LOB data partition |
| `LOGGING` | `VARCHAR2(3)` |  | Indicates whether or not changes to the LOB are logged:  - `YES` - `NO` |
| `BUFFER_POOL` | `VARCHAR2(7)` |  | Buffer pool to be used for the LOB data partition blocks:  - `DEFAULT` - `KEEP` - `RECYCLE` - NULL |
| `FLASH_CACHE` | `VARCHAR2(7)` |  | Database Smart Flash Cache hint to be used for subpartition blocks:  - `DEFAULT` - `KEEP` - `NONE`  Solaris and Oracle Linux functionality only. |
| `CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | Cell flash cache hint to be used for subpartition blocks:  - `DEFAULT` - `KEEP` - `NONE`  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `ENCRYPT` | `VARCHAR2(4)` |  | Indicates whether or not the LOB is encrypted.  Possible values for SecureFiles:  - `YES` - `NO`  Possible value for BasicFiles:  - `NONE` - Not applicable |
| `COMPRESSION` | `VARCHAR2(6)` |  | Level of compression used for this LOB.  Possible values for SecureFiles:  - `LOW` - `MEDIUM` - `HIGH` - `NO` - Compression is off  Possible value for BasicFiles:  - `NONE` - Not applicable |
| `DEDUPLICATION` | `VARCHAR2(15)` |  | Kind of deduplication used for this LOB.  Possible values for SecureFiles:  - `LOB` - Deduplicate - `NO` - Keep duplicates  Possible value for BasicFiles:  - `NONE` - Not applicable |
| `SECUREFILE` | `VARCHAR2(3)` |  | Indicates whether the LOB is SecureFiles (`YES`) or not (`NO`) |
| `SEGMENT_CREATED` | `VARCHAR2(3)` |  | Indicates whether the LOB subpartition segment has been created (`YES`) or not (`NO`); `N/A` indicates that this LOB is not subpartitioned |
| `MAX_INLINE` | `NUMBER` | `NOT NULL` | Size of inline LOB storage (in bytes)  - For inline LOBs (`IN_ROW` `=` `YES`), this column displays the size of inline LOB storage (in bytes). - For out-of-inline LOBs (`IN_ROW` `=` `NO`), the value of this column is `0`. |

See Also:

- " [DBA\_LOB\_SUBPARTITIONS](DBA_LOB_SUBPARTITIONS.md) "
- " [USER\_LOB\_SUBPARTITIONS](USER_LOB_SUBPARTITIONS.md) "