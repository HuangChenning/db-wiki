---
title: ALL_IND_PENDING_STATS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1106.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_IND_PENDING_STATS` describes the pending statistics for tables, partitions, and subpartitions accessible to the current user.

Related Views

- `DBA_IND_PENDING_STATS` describes pending statistics for all tables, partitions, and subpartitions in the database.
- `USER_IND_PENDING_STATS` describes pending statistics for tables, partitions, and subpartitions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Name of the index owner |
| `INDEX_NAME` | `VARCHAR2(30)` |  | Index name |
| `TABLE_OWNER` | `VARCHAR2(30)` |  | Table owner name |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table |
| `PARTITION_NAME` | `VARCHAR2(30)` |  | Name of the partition |
| `SUBPARTITION_NAME` | `VARCHAR2(30)` |  | Name of the subpartition |
| `BLEVEL` | `NUMBER` |  | Number of levels in the index |
| `LEAF_BLOCKS` | `NUMBER` |  | Number of leaf blocks in the index |
| `DISTINCT_KEYS` | `NUMBER` |  | Number of distinct keys in the index |
| `AVG_LEAF_BLOCKS_PER_KEY` | `NUMBER` |  | Average number of leaf blocks per key |
| `AVG_DATA_BLOCKS_PER_KEY` | `NUMBER` |  | Average number of data blocks per key |
| `CLUSTERING_FACTOR` | `NUMBER` |  | Clustering factor |
| `NUM_ROWS` | `NUMBER` |  | Number of rows in the index |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size |
| `LAST_ANALYZED` | `DATE` |  | Time of the last analysis |