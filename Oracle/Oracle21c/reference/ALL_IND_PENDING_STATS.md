---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_IND_PENDING_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.233 ALL\_IND\_PENDING\_STATS

`ALL_IND_PENDING_STATS` describes the pending statistics for tables, partitions, and subpartitions accessible to the current user collected using the `DBMS_STATS` package.

Related Views

- `DBA_IND_PENDING_STATS` describes pending statistics for all tables, partitions, and subpartitions in the database.
- `USER_IND_PENDING_STATS` describes pending statistics for tables, partitions, and subpartitions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Name of the index owner |
| `INDEX_NAME` | `VARCHAR2(128)` |  | Index name |
| `TABLE_OWNER` | `VARCHAR2(128)` |  | Table owner name |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table |
| `PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the partition |
| `SUBPARTITION_NAME` | `VARCHAR2(128)` |  | Name of the subpartition |
| `BLEVEL` | `NUMBER` |  | Number of levels in the index |
| `LEAF_BLOCKS` | `NUMBER` |  | Number of leaf blocks in the index |
| `DISTINCT_KEYS` | `NUMBER` |  | Number of distinct keys in the index |
| `AVG_LEAF_BLOCKS_PER_KEY` | `NUMBER` |  | Average number of leaf blocks per key |
| `AVG_DATA_BLOCKS_PER_KEY` | `NUMBER` |  | Average number of data blocks per key |
| `CLUSTERING_FACTOR` | `NUMBER` |  | Clustering factor |
| `NUM_ROWS` | `NUMBER` |  | Number of rows in the index |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size |
| `LAST_ANALYZED` | `DATE` |  | Time of the last analysis |

See Also:

- " [DBA\_IND\_PENDING\_STATS](DBA_IND_PENDING_STATS.md) "
- " [USER\_IND\_PENDING\_STATS](USER_IND_PENDING_STATS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS059) for more information about the `DBMS_STATS` package