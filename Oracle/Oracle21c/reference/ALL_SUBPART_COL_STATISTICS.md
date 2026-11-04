---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SUBPART_COL_STATISTICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.95 ALL\_SUBPART\_COL\_STATISTICS

`ALL_SUBPART_COL_STATISTICS` describes column statistics and histogram information for subpartitions of partitioned objects accessible to the current user.

Related Views

- `DBA_SUBPART_COL_STATISTICS` provides this information for all subpartitions in the database.
- `USER_SUBPART_COL_STATISTICS` provides this information for subpartitions of all partitioned objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `SUBPARTITION_NAME` | `VARCHAR2(128)` |  | Table subpartition name |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Column name |
| `NUM_DISTINCT` | `NUMBER` |  | Number of distinct values in the column |
| `LOW_VALUE` | `RAW(1000)` |  | Low value in the column |
| `HIGH_VALUE` | `RAW(1000)` |  | High value in the column |
| `DENSITY` | `NUMBER` |  | If a histogram is available on `COLUMN_NAME`, then this column displays the selectivity of a value that spans fewer than 2 endpoints in the histogram. It does not represent the selectivity of values that span 2 or more endpoints.  If a histogram is not available on `COLUMN_NAME`, then the value of this column is `1` / `NUM_DISTINCT`. |
| `NUM_NULLS` | `NUMBER` |  | Number of NULLs in the column |
| `NUM_BUCKETS` | `NUMBER` |  | Number of buckets in histogram for the column |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size used in analyzing this column |
| `LAST_ANALYZED` | `DATE` |  | Date on which this column was most recently analyzed |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | `GLOBAL_STATS` will be `YES` if statistics have been gathered or `NO` if statistics have not been gathered |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `NOTES` | `VARCHAR2(41)` |  | Describes some additional properties of the statistics. For example, if the value is `INCREMENTAL`, the global statistics are derived from synopses, that is, the global statistics are incrementally maintained. |
| `AVG_COL_LEN` | `NUMBER` |  | Average length of the column (in bytes) |
| `HISTOGRAM` | `VARCHAR2(15)` |  | Indicates existence/type of histogram:  - `NONE` - `FREQUENCY` - `HEIGHT BALANCED` - `HYBRID` - `TOP-FREQUENCY` |

See Also:

- " [DBA\_SUBPART\_COL\_STATISTICS](DBA_SUBPART_COL_STATISTICS.md) "
- " [USER\_SUBPART\_COL\_STATISTICS](USER_SUBPART_COL_STATISTICS.md) "