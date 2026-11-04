---
title: ALL_IND_STATISTICS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1107.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_IND_STATISTICS` displays optimizer statistics for the indexes on the tables accessible to the current user.

Related Views

- `DBA_IND_STATISTICS` displays optimizer statistics for all indexes in the database.
- `USER_IND_STATISTICS` displays optimizer statistics for the indexes on the tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the index |
| `INDEX_NAME` | `VARCHAR2(30)` |  | Name of the index |
| `TABLE_OWNER` | `VARCHAR2(30)` |  | Owner of the indexed object |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the indexed object |
| `PARTITION_NAME` | `VARCHAR2(30)` |  | Name of the partition |
| `PARTITION_POSITION` | `NUMBER` |  | Position of the partition within the index |
| `SUBPARTITION_NAME` | `VARCHAR2(30)` |  | Name of the subpartition |
| `SUBPARTITION_POSITION` | `NUMBER` |  | Position of the subpartition within the partition |
| `OBJECT_TYPE` | `VARCHAR2(12)` |  | Type of the object: - `INDEX` - `PARTITION` - `SUBPARTITION` |
| `BLEVEL` | `NUMBER` |  | B-Tree level |
| `LEAF_BLOCKS` | `NUMBER` |  | Number of leaf blocks in the index |
| `DISTINCT_KEYS` | `NUMBER` |  | Number of distinct keys in the index |
| `AVG_LEAF_BLOCKS_PER_KEY` | `NUMBER` |  | Average number of leaf blocks per key |
| `AVG_DATA_BLOCKS_PER_KEY` | `NUMBER` |  | Average number of data blocks per key |
| `CLUSTERING_FACTOR` | `NUMBER` |  | Indicates the amount of order of the rows in the table based on the values of the index. - If the value is near the number of blocks, then the table is very well ordered. In this case, the index entries in a single leaf block tend to point to rows in the same data blocks. - If the value is near the number of rows, then the table is very randomly ordered. In this case, it is unlikely that index entries in the same leaf block point to rows in the same data blocks. |
| `NUM_ROWS` | `NUMBER` |  | Number of rows in the index |
| `AVG_CACHED_BLOCKS` | `NUMBER` |  | Average number of blocks in the buffer cache |
| `AVG_CACHE_HIT_RATIO` | `NUMBER` |  | Average cache hit ratio for the object |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size used in analyzing the index |
| `LAST_ANALYZED` | `DATE` |  | Date of the most recent time the index was analyzed |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were calculated without merging underlying partitions (`YES`) or not (`NO`) |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `STATTYPE_LOCKED` | `VARCHAR2(5)` |  | Type of statistics lock |
| `STALE_STATS` | `VARCHAR2(3)` |  | Whether statistics for the object are stale or not |

See Also:

- ["DBA\_IND\_STATISTICS"](statviews_4079.md)
- ["USER\_IND\_STATISTICS"](statviews_5321.md)