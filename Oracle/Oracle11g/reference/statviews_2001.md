---
title: ALL_PART_COL_STATISTICS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2001.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_PART_COL_STATISTICS` displays column statistics and histogram information for the table partitions accessible to the current user.

Related Views

- `DBA_PART_COL_STATISTICS` displays column statistics and histogram information for all table partitions in the database.
- `USER_PART_COL_STATISTICS` displays column statistics and histogram information for the table partitions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the partitioned table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |
| `PARTITION_NAME` | `VARCHAR2(30)` |  | Name of the table partition |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column |
| `NUM_DISTINCT` | `NUMBER` |  | Number of distinct values in the column |
| `LOW_VALUE` | `RAW(32)` |  | Low value in the column |
| `HIGH_VALUE` | `RAW(32)` |  | High value in the column |
| `DENSITY` | `NUMBER` |  | If a histogram is available on `COLUMN_NAME`, then this column displays the selectivity of a value that spans fewer than 2 endpoints in the histogram. It does not represent the selectivity of values that span 2 or more endpoints.  If a histogram is not available on `COLUMN_NAME`, then the value of this column is `1` / `NUM_DISTINCT`. |
| `NUM_NULLS` | `NUMBER` |  | Number of NULLs in the column |
| `NUM_BUCKETS` | `NUMBER` |  | Number of buckets in histogram for the column |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size used in analyzing the column |
| `LAST_ANALYZED` | `DATE` |  | Date on which the column was most recently analyzed |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | Indicates whether column statistics were collected for the partition as a whole (`YES`) or were estimated from statistics on underlying subpartitions (`NO`) |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `AVG_COL_LEN` | `NUMBER` |  | Average length of the column (in bytes) |
| `HISTOGRAM` | `VARCHAR2(15)` |  | Indicates existence/type of histogram: |

See Also:

- ["DBA\_PART\_COL\_STATISTICS"](statviews_4172.md)
- ["USER\_PART\_COL\_STATISTICS"](statviews_5387.md)