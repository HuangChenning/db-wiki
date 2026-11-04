---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TAB_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.107 ALL\_TAB\_COLUMNS

`ALL_TAB_COLUMNS` describes the columns of the tables, views, and clusters accessible to the current user.

To gather statistics for this view, use the `DBMS_STATS` package.

This view filters out system-generated hidden columns. The `ALL_TAB_COLS` view does not filter out system-generated hidden columns.

Related Views

- `DBA_TAB_COLUMNS` describes the columns of all tables, views, and clusters in the database.
- `USER_TAB_COLUMNS` describes the columns of the tables, views, and clusters owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table, view, or cluster |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table, view, or cluster |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Column name |
| `DATA_TYPE` | `VARCHAR2(128)` |  | Data type of the column |
| `DATA_TYPE_MOD` | `VARCHAR2(3)` |  | Data type modifier of the column |
| `DATA_TYPE_OWNER` | `VARCHAR2(128)` |  | Owner of the data type of the column |
| `DATA_LENGTH` | `NUMBER` | `NOT NULL` | Length of the column (in bytes) |
| `DATA_PRECISION` | `NUMBER` |  | Decimal precision for `NUMBER` data type; binary precision for `FLOAT` data type; NULL for all other data types |
| `DATA_SCALE` | `NUMBER` |  | Digits to the right of the decimal point in a number |
| `NULLABLE` | `VARCHAR2(1)` |  | Indicates whether a column allows NULLs. The value is `N` if there is a `NOT NULL` constraint on the column or if the column is part of a `PRIMARY KEY.` The constraint should be in an `ENABLE VALIDATE` state. |
| `COLUMN_ID` | `NUMBER` |  | Sequence number of the column as created |
| `DEFAULT_LENGTH` | `NUMBER` |  | Length of the default value for the column |
| `DATA_DEFAULT` | `LONG` |  | Default value for the column |
| `NUM_DISTINCT` | `NUMBER` |  | Number of distinct values in the column.  This column remains for backward compatibility with Oracle7. This information is now in the `{TAB\|PART}_COL_STATISTICS` views. |
| `LOW_VALUE` | `RAW(1000)` |  | Low value in the column.  This column remains for backward compatibility with Oracle7. This information is now in the `{TAB\|PART}_COL_STATISTICS` views. |
| `HIGH_VALUE` | `RAW(1000)` |  | High value in the column.  This column remains for backward compatibility with Oracle7. This information is now in the `{TAB\|PART}_COL_STATISTICS` views. |
| `DENSITY` | `NUMBER` |  | If a histogram is available on `COLUMN_NAME`, then this column displays the selectivity of a value that spans fewer than 2 endpoints in the histogram. It does not represent the selectivity of values that span 2 or more endpoints.  If a histogram is not available on `COLUMN_NAME`, then the value of this column is `1` / `NUM_DISTINCT`.  This column remains for backward compatibility with Oracle7. This information is now in the `{TAB\|PART}_COL_STATISTICS` views. |
| `NUM_NULLS` | `NUMBER` |  | Number of NULLs in the column |
| `NUM_BUCKETS` | `NUMBER` |  | Number of buckets in the histogram for the column  Note: The number of buckets in a histogram is specified in the `SIZE` parameter of the `ANALYZE` SQL statement. However, Oracle Database does not create a histogram with more buckets than the number of rows in the sample. Also, if the sample contains any values that are very repetitious, Oracle Database creates the specified number of buckets, but the value indicated by this column may be smaller because of an internal compression algorithm. |
| `LAST_ANALYZED` | `DATE` |  | Date on which this column was most recently analyzed |
| `SAMPLE_SIZE` | `NUMBER` |  | Sample size used in analyzing this column |
| `CHARACTER_SET_NAME` | `VARCHAR2(44)` |  | Name of the character set:  - `CHAR_CS` - `NCHAR_CS` |
| `CHAR_COL_DECL_LENGTH` | `NUMBER` |  | Declaration length of the character type column |
| `GLOBAL_STATS` | `VARCHAR2(3)` |  | `GLOBAL_STATS` will be `YES` if statistics are gathered or incrementally maintained, otherwise it will be `NO` |
| `USER_STATS` | `VARCHAR2(3)` |  | Indicates whether statistics were entered directly by the user (`YES`) or not (`NO`) |
| `AVG_COL_LEN` | `NUMBER` |  | Average length of the column (in bytes) |
| `CHAR_LENGTH` | `NUMBER` |  | Displays the length of the column in characters. This value only applies to the following datatypes:  - `CHAR` - `VARCHAR2` - `NCHAR` - `NVARCHAR2` |
| `CHAR_USED` | `VARCHAR2(1)` |  | Indicates that the column uses `BYTE` length semantics (`B`) or `CHAR` length semantics (`C`), or whether the datatype is not any of the following (NULL):  - `CHAR` - `VARCHAR2` - `NCHAR` - `NVARCHAR2` |
| `V80_FMT_IMAGE` | `VARCHAR2(3)` |  | Indicates whether the column data is in release 8.0 image format (`YES`) or not (`NO`) |
| `DATA_UPGRADED` | `VARCHAR2(3)` |  | Indicates whether the column data has been upgraded to the latest type version format (`YES`) or not (`NO`) |
| `HISTOGRAM` | `VARCHAR2(15)` |  | Indicates existence/type of histogram:  - `NONE` - `FREQUENCY` - `TOP-FREQUENCY` - `HEIGHT BALANCED` - `HYBRID` |
| `DEFAULT_ON_NULL` | `VARCHAR2(3)` |  | Indicates whether the column has `DEFAULT ON NULL` semantics (`YES`) or not (`NO`) |
| `IDENTITY_COLUMN` | `VARCHAR2(3)` |  | Indicates whether this is an identity column (`YES`) or not (`NO`) |
| `EVALUATION_EDITION` | `VARCHAR2(128)` |  | Name of the edition in which editioned objects referenced in an expression column are resolved |
| `UNUSABLE_BEFORE` | `VARCHAR2(128)` |  | Name of the oldest edition in which the column is usable |
| `UNUSABLE_BEGINNING` | `VARCHAR2(128)` |  | Name of the oldest edition in which the column becomes perpetually unusable |
| `COLLATION` | `VARCHAR2(100)` |  | Collation for the column. Only applies to columns with character data types. |