---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_ATTRIBUTE_DIM_TABLES.html
tags:
  - oracle
  - 12c
  - reference
---

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
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the table in the list of tables in the `USING` clause |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_ATTRIBUTE\_DIM\_TABLES](DBA_ATTRIBUTE_DIM_TABLES.md) "
- " [USER\_ATTRIBUTE\_DIM\_TABLES](USER_ATTRIBUTE_DIM_TABLES.md) "