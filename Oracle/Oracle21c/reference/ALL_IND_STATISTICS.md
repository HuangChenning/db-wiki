---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_IND_STATISTICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.234 ALL\_IND\_STATISTICS

`ALL_IND_STATISTICS` displays optimizer statistics for the indexes on the tables accessible to the current user collected using the `DBMS_STATS` package.

Related Views

- `DBA_IND_STATISTICS` displays optimizer statistics for all indexes in the database.
- `USER_IND_STATISTICS` displays optimizer statistics for the indexes on the tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the index |
| `INDEX_NAME` | `VARCHAR2(128)` |  | Name of the index |
| `TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the indexed object |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the indexed object |
| `PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the partition |
| `PARTITION_POSITION` | `NUMBER` |  | Position of the partition within the index |
| `SUBPARTITION_NAME` | `VARCHAR2(128)` |  | Name of the subpartition |
| `SUBPARTITION_POSITION` | `NUMBER` |  | Position of the subpartition within the partition |
| `OBJECT_TYPE` | `VARCHAR2(12)` |  | Type of the object:  - `INDEX` - `PARTITION` - `SUBPARTITION` |
| `BLEVEL` | `NUMBER` |  | B-Tree level |
| `LEAF_BLOCKS` | `NUMBER` |  | Number of leaf blocks in the index |
| `DISTINCT_KEYS` | `NUMBER` |  | Number of distinct keys in the index |
| `AVG_LEAF_BLOCKS_PER_KEY` | `NUMBER` |  | Average number of leaf blocks per key |
| `AVG_DATA_BLOCKS_PER_KEY` | `NUMBER` |  | Average number of data blocks per key |
| `CLUSTERING_FACTOR` | `NUMBER` |  | Indicates the amount of order of the rows in the table based on the values of the index.  - If the value is near the number of blocks, then the table is very well ordered. In this case, the index entries in a single leaf block tend to point to rows in the same data blocks. - If the value is near the number of rows, then the table is very randomly ordered. In this case, it is unlikely that index entries in the same leaf block point to rows in the same data blocks. |
| `NUM_ROWS` | `NUMBER` |  | Number of rows in the index |
| `AVG_CACHED_BLOCKS` | `NUMBER` |  | Average number of blocks in the buffer cache |
| `AVG_CACHE_HIT_RATIO` | `NUMBER` |  | Average cache hit ratio for the object |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size used in analyzing the index |
| `LAST_ANALYZED` | `DATE` |  | Date of the most recent time the index was analyzed |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | `GLOBAL_STATS` will be `YES` if statistics are gathered or incrementally maintained, otherwise it will be `NO` |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `STATTYPE_LOCKED` | `VARCHAR2(5)` |  | Type of statistics lock |
| `STALE_STATS` | `VARCHAR2(3)` |  | Whether statistics for the object are stale or not |
| `SCOPE` | `VARCHAR2(7)` |  | The value is `SHARED` for statistics gathered on any table other than global temporary tables.  For a global tempoary table, the possible values are:  - `SESSION` - Indicates that the statistics are session-specific - `SHARED` - Indicates that the statistics are shared across all sessions  See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS-GUID-01FAB8ED-E4A3-4C3E-8FE2-88717DCDDA06) for information about using the `GLOBAL_TEMP_TABLE_STATS` preference of the `DBMS_STATS` package to control whether to gather session or shared statistics for global temporary tables. |

See Also:

- " [DBA\_IND\_STATISTICS](DBA_IND_STATISTICS.md) "
- " [USER\_IND\_STATISTICS](USER_IND_STATISTICS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS-GUID-01FAB8ED-E4A3-4C3E-8FE2-88717DCDDA06) for more information about the `DBMS_STATS` package