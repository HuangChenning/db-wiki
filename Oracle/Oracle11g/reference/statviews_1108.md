---
title: ALL_IND_SUBPARTITIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1108.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_IND_SUBPARTITIONS` describes, for each index subpartition accessible to the current user, the partition-level partitioning information, the storage parameters for the subpartition, and various partition statistics generated using the `DBMS_STATS` package.

Related Views

- `DBA_IND_SUBPARTITIONS` describes all index subpartitions in the database.
- `USER_IND_SUBPARTITIONS` describes the index subpartitions owned by the current user. This view does not display the `INDEX_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INDEX_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the index |
| `INDEX_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the index |
| `PARTITION_NAME` | `VARCHAR2(30)` |  | Name of the partition |
| `SUBPARTITION_NAME` | `VARCHAR2(30)` |  | Name of the subpartition |
| `HIGH_VALUE` | `LONG` |  | Subpartition bound value expression |
| `HIGH_VALUE_LENGTH` | `NUMBER` | `NOT NULL` | Length of the subpartition bound value expression |
| `SUBPARTITION_POSITION` | `NUMBER` |  | Position of a subpartition within a partition |
| `STATUS` | `VARCHAR2(8)` |  | Indicates whether the index partition is usable (`USABLE`) or not (`UNUSABLE`) |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace containing the partition |
| `PCT_FREE` | `NUMBER` | `NOT NULL` | Minimum percentage of free space in a block |
| `INI_TRANS` | `NUMBER` | `NOT NULL` | Initial number of transactions |
| `MAX_TRANS` | `NUMBER` | `NOT NULL` | Maximum number of transactions |
| `INITIAL_EXTENT` | `NUMBER` |  | Size of the initial extent in bytes |
| `NEXT_EXTENT` | `NUMBER` |  | Size of secondary extents in bytes |
| `MIN_EXTENT` | `NUMBER` |  | Minimum number of extents allowed in the segment |
| `MAX_EXTENT` | `NUMBER` |  | Maximum number of extents allowed in the segment |
| `MAX_SIZE` | `NUMBER` |  | Maximum number of blocks allowed in the segment |
| `PCT_INCREASE` | `NUMBER` | `NOT NULL` | Percentage increase in extent size |
| `FREELISTS` | `NUMBER` |  | Number of process freelists allocated in this segment |
| `FREELIST_GROUPS` | `NUMBER` |  | Number of process freelist groups allocated in this segment |
| `LOGGING` | `VARCHAR2(3)` |  | Indicates whether or not changes to the index are logged: - `YES` - `NO` |
| `COMPRESSION` | `VARCHAR2(8)` |  | Indicates whether this subpartition is compressed (`ENABLED`) or not (`DISABLED`) |
| `BLEVEL` | `NUMBER` |  | B-Tree level (depth of the index from its root block to its leaf blocks). A depth of `0` indicates that the root block and leaf block are the same. |
| `LEAF_BLOCKS` | `NUMBER` |  | Number of leaf blocks in the index |
| `DISTINCT_KEYS` | `NUMBER` |  | Number of distinct keys in the index partition |
| `AVG_LEAF_BLOCKS_PER_KEY` | `NUMBER` |  | Average number of leaf blocks in which each distinct value in the index appears, rounded to the nearest integer. For indexes that enforce `UNIQUE` and `PRIMARY` `KEY` constraints, this value is always `1`. |
| `AVG_DATA_BLOCKS_PER_KEY` | `NUMBER` |  | Average number of data blocks in the table that are pointed to by a distinct value in the index rounded to the nearest integer. This statistic is the average number of data blocks that contain rows that contain a given value for the indexed columns. |
| `CLUSTERING_FACTOR` | `NUMBER` |  | Indicates the amount of order of the rows in the table based on the values of the index. - If the value is near the number of blocks, then the table is very well ordered. In this case, the index entries in a single leaf block tend to point to rows in the same data blocks. - If the value is near the number of rows, then the table is very randomly ordered. In this case, it is unlikely that index entries in the same leaf block point to rows in the same data blocks. |
| `NUM_ROWS` | `NUMBER` |  | Number of rows in this index subpartition |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size used in analyzing this subpartition |
| `LAST_ANALYZED` | `DATE` |  | Date on which this partition was most recently analyzed |
| `BUFFER_POOL` | `VARCHAR2(7)` |  | Buffer pool for the subpartition: - `DEFAULT` - `KEEP` - `RECYCLE` - NULL |
| `FLASH_CACHE` | `VARCHAR2(7)` |  | Database Smart Flash Cache hint to be used for subpartition blocks: - `DEFAULT` - `KEEP` - `NONE`  Solaris and Oracle Linux functionality only. |
| `CELL_FLASH_CACHE` | `VARCHAR2(7)` |  | Cell flash cache hint to be used for subpartition blocks: - `DEFAULT` - `KEEP` - `NONE`  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | Indicates whether column statistics for the subpartition statistics were collected by analyzing the table as a whole (`YES`) or estimated from statistics gathered on partitions and subpartitions (`NO`) |
| `INTERVAL` | `VARCHAR2(3)` |  | Indicates whether the partition is in the interval section of an interval partitioned table (`YES`) or whether the partition is in the range section (`NO`) |
| `SEGMENT_CREATED` | `VARCHAR2(3)` |  | Indicates whether the index subpartition segment has been created (`YES`) or not (`NO`); `N/A` indicates that this index is not subpartitioned |