---
title: ALL_TAB_PENDING_STATS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2109.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TAB_PENDING_STATS` describes pending statistics for tables, partitions, and subpartitions accessible to the current user.

Related Views

- `DBA_TAB_PENDING_STATS` describes pending statistics for tables, partitions, and subpartitions in the database.
- `USER_TAB_PENDING_STATS` describes pending statistics for tables, partitions, and subpartitions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table |
| `PARTITION_NAME` | `VARCHAR2(30)` |  | Name of the partition |
| `SUBPARTITION_NAME` | `VARCHAR2(30)` |  | Name of the subpartition |
| `NUM_ROWS` | `NUMBER` |  | Number of rows |
| `BLOCKS` | `NUMBER` |  | Number of blocks |
| `AVG_ROW_LEN` | `NUMBER` |  | Average row length |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size |
| `LAST_ANALYZED` | `DATE` |  | Time of last analyze operation |