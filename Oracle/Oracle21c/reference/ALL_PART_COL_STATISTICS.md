---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_PART_COL_STATISTICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.1 ALL\_PART\_COL\_STATISTICS

`ALL_PART_COL_STATISTICS` displays column statistics and histogram information for the table partitions accessible to the current user.

Related Views

- `DBA_PART_COL_STATISTICS` displays column statistics and histogram information for all table partitions in the database.
- `USER_PART_COL_STATISTICS` displays column statistics and histogram information for the table partitions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the partitioned table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the table partition |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column |
| `NUM_DISTINCT` | `NUMBER` |  | Number of distinct values in the column |
| `LOW_VALUE` | `RAW(1000)` |  | Low value in the column |
| `HIGH_VALUE` | `RAW(1000)` |  | High value in the column |
| `DENSITY` | `NUMBER` |  | If a histogram is available on `COLUMN_NAME`, then this column displays the selectivity of a value that spans fewer than 2 endpoints in the histogram. It does not represent the selectivity of values that span 2 or more endpoints.  If a histogram is not available on `COLUMN_NAME`, then the value of this column is `1` / `NUM_DISTINCT`. |
| `NUM_NULLS` | `NUMBER` |  | Number of NULLs in the column |
| `NUM_BUCKETS` | `NUMBER` |  | Number of buckets in histogram for the column |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size used in analyzing the column |
| `LAST_ANALYZED` | `DATE` |  | Date on which the column was most recently analyzed |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | `GLOBAL_STATS` will be `YES` if statistics have been gathered or `NO` if statistics have been aggregated from subpartitions or have not been gathered |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `NOTES` | `VARCHAR2(81)` |  | Additional properties of the statistics, if any. Possible values: - `ADAPTIVE_SAMPLING`: The column has synopses, and the synopses are in the adaptive sampling format introduced in Oracle Database 11g Release 1 (11.1). - `HIST_FOR_INCREM_STATS`: A histogram used to support incremental statistics has been created and it is not used for optimization. - `HISTOGRAM_ONLY`: Table statistics were gathered using the `GATHER` `AUTO` option and histograms were gathered without re-gathering other table and column statistics. - `HYPERLOGLOG`: The column has synopses, and the synopses are in the HyperLogLog format introduced in Oracle Database 12c Release 2 (12.2.0.1). - `INCREMENTAL`: The column has synopses. - `STATS_ON_LOAD`: Online statistics were gathered during direct path load.  This column can be used to determine whether synopses in the adaptive sampling format have been phased out entirely and purged properly. |
| `AVG_COL_LEN` | `NUMBER` |  | Average length of the column (in bytes) |
| `HISTOGRAM` | `VARCHAR2(15)` |  | Indicates existence/type of histogram:  - `NONE` - `FREQUENCY` - `HEIGHT BALANCED` - `HYBRID` - `TOP-FREQUENCY` |

See Also:

- " [DBA\_PART\_COL\_STATISTICS](DBA_PART_COL_STATISTICS.md) "
- " [USER\_PART\_COL\_STATISTICS](USER_PART_COL_STATISTICS.md) "