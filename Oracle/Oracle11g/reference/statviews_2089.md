---
title: ALL_SUBPART_COL_STATISTICS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2089.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SUBPART_COL_STATISTICS` describes column statistics and histogram information for subpartitions of partitioned objects accessible to the current user.

Related Views

- `DBA_SUBPART_COL_STATISTICS` provides this information for all subpartitions in the database.
- `USER_SUBPART_COL_STATISTICS` provides this information for subpartitions of all partitioned objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |
| `SUBPARTITION_NAME` | `VARCHAR2(30)` |  | Table subpartition name |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Column name |
| `NUM_DISTINCT` | `NUMBER` |  | Number of distinct values in the column |
| `LOW_VALUE` | `RAW(32)` |  | Low value in the column |
| `HIGH_VALUE` | `RAW(32)` |  | High value in the column |
| `DENSITY` | `NUMBER` |  | If a histogram is available on `COLUMN_NAME`, then this column displays the selectivity of a value that spans fewer than 2 endpoints in the histogram. It does not represent the selectivity of values that span 2 or more endpoints.  If a histogram is not available on `COLUMN_NAME`, then the value of this column is `1` / `NUM_DISTINCT`. |
| `NUM_NULLS` | `NUMBER` |  | Number of NULLs in the column |
| `NUM_BUCKETS` | `NUMBER` |  | Number of buckets in histogram for the column |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size used in analyzing this column |
| `LAST_ANALYZED` | `DATE` |  | Date on which this column was most recently analyzed |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | Indicates whether column statistics for the subpartition were collected by analyzing the table as a whole (`YES`) or estimated from statistics gathered on partitions and subpartitions (`NO`) |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `AVG_COL_LEN` | `NUMBER` |  | Average length of the column (in bytes) |
| `HISTOGRAM` | `VARCHAR2(15)` |  | Indicates existence/type of histogram: |