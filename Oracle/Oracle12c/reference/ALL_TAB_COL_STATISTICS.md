---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_TAB_COL_STATISTICS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_TAB_COL_STATISTICS` displays column statistics and histogram information extracted from `ALL_TAB_COLUMNS`.

Related Views

- `DBA_TAB_COL_STATISTICS` displays such information extracted from " [DBA\_TAB\_COLUMNS](DBA_TAB_COLUMNS.md) ".
- `USER_TAB_COL_STATISTICS` displays such information extracted from " [USER\_TAB\_COLUMNS](USER_TAB_COLUMNS.md) ". This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Column name |
| `NUM_DISTINCT` | `NUMBER` |  | Number of distinct values in the column |
| `LOW_VALUE` | `RAW(1000)` |  | Low value in the column |
| `HIGH_VALUE` | `RAW(1000)` |  | High value in the column |
| `DENSITY` | `NUMBER` |  | If a histogram is available on `COLUMN_NAME`, then this column displays the selectivity of a value that spans fewer than 2 endpoints in the histogram. It does not represent the selectivity of values that span 2 or more endpoints.  If a histogram is not available on `COLUMN_NAME`, then the value of this column is `1` / `NUM_DISTINCT`. |
| `NUM_NULLS` | `NUMBER` |  | Number of NULLs in the column |
| `NUM_BUCKETS` | `NUMBER` |  | Number of buckets in histogram for the column |
| `LAST_ANALYZED` | `DATE` |  | Date on which this column was most recently analyzed |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size used in analyzing this column |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | `GLOBAL_STATS` will be `YES` if statistics are gathered or incrementally maintained, otherwise it will be `NO` |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `NOTES` | `VARCHAR2(41)` |  | Describes some additional properties of the statistics. For example, if the value is `INCREMENTAL`, the global statistics are derived from synopses, that is, the global statistics are incrementally maintained. |
| `AVG_COL_LEN` | `NUMBER` |  | Average length of the column (in bytes) |
| `HISTOGRAM` | `VARCHAR2(15)` |  | Indicates existence/type of histogram:  - `NONE` - `FREQUENCY` - `HEIGHT BALANCED` - `HYBRID` - `TOP-FREQUENCY` |
| `SCOPE` | `VARCHAR2(7)` |  | The value is `SHARED` for statistics gathered on any table other than global temporary tables.  For a global tempoary table, the possible values are:  - `SESSION` - Indicates that the statistics are session-specific - `SHARED` - Indicates that the statistics are shared across all sessions  See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS68486) for information about using the `GLOBAL_TEMP_TABLE_STATS` preference of the `DBMS_STATS` package to control whether to gather session or shared statistics for global temporary tables. |