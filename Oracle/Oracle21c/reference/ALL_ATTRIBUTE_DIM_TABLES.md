---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ATTRIBUTE_DIM_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.106 ALL\_ATTRIBUTE\_DIM\_TABLES

`ALL_ATTRIBUTE_DIM_TABLES` describes the tables used by the attribute dimensions accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_DIM_TABLES` describes the tables used by all attribute dimensions in the database.
- `USER_ATTRIBUTE_DIM_TABLES` describes the tables used by the attribute dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of table used by the attribute dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute dimension |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table or view used by the attribute dimension |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table or view used by the attribute dimension |
| `TABLE_ALIAS` | `VARCHAR2(128)` |  | Alias specified for the table or view; if not specified, the name of the table or view |
| `IS_REMOTE` <sup>Foot 1</sup> | `VARCHAR2(1)` |  | Indicates whether the source is a remote table. The values are:  - `Y` for a remote table - `N` for a local table |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the table in the list of tables in the `USING` clause |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.

See Also:

- " [DBA\_ATTRIBUTE\_DIM\_TABLES](DBA_ATTRIBUTE_DIM_TABLES.md) "
- " [USER\_ATTRIBUTE\_DIM\_TABLES](USER_ATTRIBUTE_DIM_TABLES.md) "