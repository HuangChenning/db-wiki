---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_HIER_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.208 ALL\_HIER\_COLUMNS

`ALL_HIER_COLUMNS` describes the columns of the hierarchies accessible to the current user.

Related Views

- `DBA_HIER_COLUMNS` describes the columns of all hierarchies in the database.
- `USER_HIER_COLUMNS` describes the columns of the hierarchies owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the hierarchy |
| `HIER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the hierarchy |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the column |
| `ROLE` | `VARCHAR2(4)` |  | The role the attribute plays in the hierarchy: - `KEY` - `AKEY` - `HIER` - `PROP` |
| `DATA_TYPE` | `VARCHAR2(106)` |  | Datatype of the column |
| `DATA_LENGTH` | `NUMBER` | `NOT NULL` | Length of the column (in bytes) |
| `DATA_PRECISION` | `NUMBER` |  | Decimal precision for the `NUMBER` datatype; binary precision for the `FLOAT` datatype, NULL for all other datatypes |
| `DATA_SCALE` | `NUMBER` |  | Number of digits to the right of the decimal point in a number |
| `NULLABLE` | `CHAR(1)` |  | Indicates whether a column allows NULL values; the value is `N` if there is a `NOT` `NULL` constraint on the column or if the column is part of a `PRIMARY` `KEY` |
| `CHARACTER_SET_NAME` | `VARCHAR2(44)` |  | Name of the character set:  - `CHAR_CS` - `NCHAR_CS` |
| `CHAR_COL_DECL_LENGTH` | `NUMBER` |  | Declaration length of the character type column |
| `CHAR_USED` | `VARCHAR2(1)` |  | Indicates that the column uses `BYTE` length semantics (`B`) or `CHAR` length semantics (`C`), or whether the datatype is not any of the following (NULL):  - `CHAR` - `VARCHAR2` - `NCHAR` - `NVARCHAR2` |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the column, with attributes first in the order specified in the definition of the hierarchy followed by hierarchical attributes |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

See Also:

- " [DBA\_HIER\_COLUMNS](DBA_HIER_COLUMNS.md) "
- " [USER\_HIER\_COLUMNS](USER_HIER_COLUMNS.md) "