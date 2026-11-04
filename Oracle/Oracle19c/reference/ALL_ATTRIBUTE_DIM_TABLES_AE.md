---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_ATTRIBUTE_DIM_TABLES_AE.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.99 ALL\_ATTRIBUTE\_DIM\_TABLES\_AE

`ALL_ATTRIBUTE_DIM_TABLES_AE` describes the tables used by the attribute dimensions (across all editions) accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_DIM_TABLES_AE` describes the tables used by all attribute dimensions (across all editions) in the database.
- `USER_ATTRIBUTE_DIM_TABLES_AE` describes the tables used by the attribute dimensions (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of table used by the attribute dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute dimension |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table or view used by the attribute dimension |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table or view used by the attribute dimension |
| `TABLE_ALIAS` | `VARCHAR2(128)` |  | Alias specified for the table or view; if not specified, the name of the table or view |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the table in the list of tables in the `USING` clause |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the attribute dimension is defined |

Note:

This view is available starting with Oracle Database 19c, Release Update 19.13.

See Also:

- " [DBA\_ATTRIBUTE\_DIM\_TABLES\_AE](DBA_ATTRIBUTE_DIM_TABLES_AE.md) "
- " [USER\_ATTRIBUTE\_DIM\_TABLES\_AE](USER_ATTRIBUTE_DIM_TABLES_AE.md) "