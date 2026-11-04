---
title: ALL_TAB_STATISTICS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2114.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TAB_STATISTICS` displays optimizer statistics for the tables accessible to the current user.

Related Views

- `DBA_TAB_STATISTICS` displays optimizer statistics for all tables in the database.
- `USER_TAB_STATISTICS` displays optimizer statistics for the tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table |
| `PARTITION_NAME` | `VARCHAR2(30)` |  | Name of the partition |
| `PARTITION_POSITION` | `NUMBER` |  | Position of the partition within the table |
| `SUBPARTITION_NAME` | `VARCHAR2(30)` |  | Name of the subpartition |
| `SUBPARTITION_POSITION` | `NUMBER` |  | Position of the subpartition within the partition |
| `OBJECT_TYPE` | `VARCHAR2(12)` |  | Type of the object: - `TABLE` - `PARTITION` - `SUBPARTITION` |
| `NUM_ROWS` | `NUMBER` |  | Number of rows in the object |
| `BLOCKS` | `NUMBER` |  | Number of used blocks in the object |
| `EMPTY_BLOCKS` | `NUMBER` |  | Number of empty blocks in the object |
| `AVG_SPACE` | `NUMBER` |  | Average available free space in the object |
| `CHAIN_CNT` | `NUMBER` |  | Number of chained rows in the object |
| `AVG_ROW_LEN` | `NUMBER` |  | Average row length, including row overhead |
| `AVG_SPACE_FREELIST_BLOCKS` | `NUMBER` |  | Average freespace of all blocks on a freelist |
| `NUM_FREELIST_BLOCKS` | `NUMBER` |  | Number of blocks on the freelist |
| `AVG_CACHED_BLOCKS` | `NUMBER` |  | Average number of blocks in the buffer cache |
| `AVG_CACHE_HIT_RATIO` | `NUMBER` |  | Average cache hit ratio for the object |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size used in analyzing the table |
| `LAST_ANALYZED` | `DATE` |  | Date of the most recent time the table was analyzed |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were calculated without merging underlying partitions (`YES`) or not (`NO`) |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `STATTYPE_LOCKED` | `VARCHAR2(5)` |  | Type of statistics lock: |
| `STALE_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics for the object are stale (`YES`) or not (`NO`) |

See Also:

- ["DBA\_TAB\_STATISTICS"](statviews_5052.md)
- ["USER\_TAB\_STATISTICS"](statviews_5487.md)