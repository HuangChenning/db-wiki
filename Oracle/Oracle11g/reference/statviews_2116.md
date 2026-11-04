---
title: ALL_TAB_SUBPARTITIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2116.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TAB_SUBPARTITIONS` displays, for each table subpartition accessible to the current user, the subpartition name, name of the table and partition to which it belongs, and its storage attributes.

Related Views

- `DBA_TAB_SUBPARTITIONS` displays such information for all subpartitions in the database.
- `USER_TAB_SUBPARTITIONS` displays such information for subpartitions of all partitioned objects owned by the current user. This view does not display the `TABLE_OWNER` column.

Note:

Statistics are not collected on a per-subpartition basis.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |
| `PARTITION_NAME` | `VARCHAR2(30)` |  | Name of the partition |
| `SUBPARTITION_NAME` | `VARCHAR2(30)` |  | Name of the subpartition |
| `HIGH_VALUE` | `LONG` |  | Subpartition bound value expression |
| `HIGH_VALUE_LENGTH` | `NUMBER` | `NOT NULL` | Length of the subpartition bound value expression |
| `SUBPARTITION_POSITION` | `NUMBER` |  | Position of the subpartition within the partition |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace containing the subpartition |
| `PCT_FREE` | `NUMBER` | `NOT NULL` | Minimum percentage of free space in a block |
| `PCT_USED` | `NUMBER` |  | Minimum percentage of used space in a block |
| `INI_TRANS` | `NUMBER` | `NOT NULL` | Initial number of transactions |
| `MAX_TRANS` | `NUMBER` | `NOT NULL` | Maximum number of transactions |
| `INITIAL_EXTENT` | `NUMBER` |  | Size of the initial extent in bytes (for a range partition); size of the initial extent in blocks (for a composite partition) |
| `NEXT_EXTENT` | `NUMBER` |  | Size of secondary extents in bytes (for a range partition); size of secondary extents in blocks (for a composite partition) |
| `MIN_EXTENT` | `NUMBER` | `NOT NULL` | Minimum number of extents allowed in the segment |
| `MAX_EXTENT` | `NUMBER` | `NOT NULL` | Maximum number of extents allowed in the segment |
| `MAX_SIZE` | `NUMBER` |  | Maximum number of blocks allowed in the segment |
| `PCT_INCREASE` | `NUMBER` |  | Percentage increase in extent size |
| `FREELISTS` | `NUMBER` |  | Number of freelist groups allocated in this segment |
| `FREELIST_GROUPS` | `NUMBER` |  | Number of freelist groups allocated in this segment |
| `LOGGING` | `VARCHAR2(3)` |  | Indicates whether or not changes to the table are logged: - `YES` - `NO` |
| `COMPRESSION` | `VARCHAR2(8)` |  | Indicates whether this subpartition is compressed (`ENABLED`) or not (`DISABLED`) |
| `COMPRESS_FOR` | `VARCHAR2(12)` |  | Default compression for what kind of operations: - `BASIC` - `OLTP` - `QUERY LOW` <sup>Foot 1</sup> - `QUERY HIGH` <sup>Footref 1</sup> - `ARCHIVE LOW` <sup>Footref 1</sup> - `ARCHIVE HIGH` <sup>Footref 1</sup> - NULL |
| `NUM_ROWS` | `NUMBER` |  | Number of rows in the subpartition |
| `BLOCKS` | `NUMBER` |  | Number of blocks in the subpartition |
| `EMPTY_BLOCKS` | `NUMBER` |  | Number of empty blocks in the subpartition |
| `AVG_SPACE` | `NUMBER` |  | Average space in the subpartition |
| `CHAIN_CNT` | `NUMBER` |  | Chain count |
| `AVG_ROW_LEN` | `NUMBER` |  | Average row length |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size |
| `LAST_ANALYZED` | `DATE` |  | Date on which this table was most recently analyzed |
| `BUFFER_POOL` | `VARCHAR2(7)` |  | Buffer pool for this subpartition: - `DEFAULT` - `KEEP` - `RECYCLE` - NULL |
| `FLASH_CACHE` | `VARCHAR2(7)` |  | Database Smart Flash Cache hint to be used for subpartition blocks: - `DEFAULT` - `KEEP` - `NONE`  Solaris and Oracle Linux functionality only. |
| `CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | Cell flash cache hint to be used for subpartition blocks: - `DEFAULT` - `KEEP` - `NONE`  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | Indicates whether column statistics for the subpartition were collected by analyzing the table as a whole (`YES`) or estimated from statistics collected for partitions and subpartitions (`NO`) |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `INTERVAL` | `VARCHAR2(3)` |  | Indicates whether the partition is in the interval section of an interval partitioned table (`YES`) or whether the partition is in the range section (`NO`) |
| `SEGMENT_CREATED` | `VARCHAR2(3)` |  | Indicates whether the table subpartition segment has been created (`YES`) or not (`NO`); `N/A` indicates that this table is not subpartitioned |

<sup>Footnote 1</sup> Hybrid Columnar Compression is a feature of the Enterprise Edition of Oracle Database that is dependent on the underlying storage system. See [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT89198) for more information.