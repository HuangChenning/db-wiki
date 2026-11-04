---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ANALYTIC_VIEW_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.29 ALL\_ANALYTIC\_VIEW\_COLUMNS

`ALL_ANALYTIC_VIEW_COLUMNS` describes the columns of the analytic views accessible to the current user.

Related Views

- `DBA_ANALYTIC_VIEW_COLUMNS` describes the columns of all analytic views in the database.
- `USER_ANALYTIC_VIEW_COLUMNS` describes the columns of the analytic views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | ` NOT NULL` | Owner of the analytic view |
| `ANALYTIC_VIEW_NAME` | `VARCHAR2(128)` | ` NOT NULL` | Name of the analytic view |
| `DIMENSION_NAME` | `VARCHAR2(128)` |  | Alias of the analytic view dimension in the analytic view; for a measure the value is `MEASURES` |
| `HIER_NAME` | `VARCHAR2(128)` |  | Alias of the analytic view hierarchy within `DIMENSION_NAME` in the analytic view; for a measure the value is `MEASURES` |
| `COLUMN_NAME` | `VARCHAR2(128)` | ` NOT NULL` | Name of the column |
| `ROLE` | `VARCHAR2(4)` | ` NOT NULL` | The role the attribute plays in the analytic view: - `KEY` - `AKEY` - `HIER` - `PROP` - `MEAS` |
| `DATA_TYPE` | `VARCHAR2(106)` | `NOT NULL` | Datatype of the column |
| `DATA_LENGTH` | `NUMBER` | `NOT NULL` | Length of the column (in bytes) |
| `DATA_PRECISION` | `NUMBER` |  | Decimal precision for the `NUMBER` datatype; binary precision for the `FLOAT` datatype, NULL for all other datatypes |
| `DATA_SCALE` | `NUMBER` |  | Number of digits to the right of the decimal point in a number |
| `NULLABLE` | `CHAR(1)` | `NOT NULL` | Indicates whether a column allows NULL values; the value is `N` if there is a `NOT` `NULL` constraint on the column or if the column is part of a `PRIMARY` `KEY` |
| `CHARACTER_SET_NAME` | `VARCHAR2(44)` |  | Name of the character set:  - `CHAR_CS` - `NCHAR_CS` |
| `CHAR_COL_DECL_LENGTH` | `NUMBER` |  | Declaration length of the character type column |
| `CHAR_USED` | `VARCHAR2(1)` |  | Indicates that the column uses `BYTE` length semantics (`B`) or `CHAR` length semantics (`C`), or whether the datatype is not any of the following (NULL): - `CHAR` - `VARCHAR2` - `NCHAR` - `NVARCHAR2` |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the column, with the hierarchy columns first followed by measure columns. The columns for a hierarchy are grouped together, listed in their order in the `HIERARCHIES` clause of the analytic view definition. Within a hierarchy, attributes are listed first in order of their definition in the `ATTRIBUTES` clause of the attribute dimension definition followed by hierarchical attributes in the `DIMENSION` `BY` clause of the analytic view. |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

See Also:

- " [DBA\_ANALYTIC\_VIEW\_COLUMNS](DBA_ANALYTIC_VIEW_COLUMNS.md) "
- " [USER\_ANALYTIC\_VIEW\_COLUMNS](USER_ANALYTIC_VIEW_COLUMNS.md) "