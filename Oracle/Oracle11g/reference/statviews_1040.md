---
title: ALL_COL_PENDING_STATS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1040.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_COL_PENDING_STATS` describes the pending statistics of the columns accessible to the current user.

Related Views

- `DBA_COL_PENDING_STATS` describes the pending statistics of all columns in the database.
- `USER_COL_PENDING_STATS` describes the pending statistics of the columns owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table |
| `PARTITION_NAME` | `VARCHAR2(30)` |  | Name of the partition |
| `SUBPARTITION_NAME` | `VARCHAR2(30)` |  | Name of the subpartition |
| `COLUMN_NAME` | `VARCHAR2(30)` |  | Name of the column |
| `NUM_DISTINCT` | `NUMBER` |  | Number of distinct values in the column |
| `LOW_VALUE` | `RAW(32)` |  | Low value in the column |
| `HIGH_VALUE` | `RAW(32)` |  | High value in the column |
| `DENSITY` | `NUMBER` |  | If a histogram is available on `COLUMN_NAME`, then this column displays the selectivity of a value that spans fewer than 2 endpoints in the histogram. It does not represent the selectivity of values that span 2 or more endpoints.  If a histogram is not available on `COLUMN_NAME`, then the value of this column is `1` / `NUM_DISTINCT`. |
| `NUM_NULLS` | `NUMBER` |  | Number of NULLs in the column |
| `AVG_COL_LEN` | `NUMBER` |  | Average length of the column (in bytes) |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size used in analyzing the column |
| `LAST_ANALYZED` | `DATE` |  | Most recent date on which the column was analyzed |

See Also:

- ["DBA\_COL\_PENDING\_STATS"](statviews_3109.md)
- ["USER\_COL\_PENDING\_STATS"](statviews_5247.md)