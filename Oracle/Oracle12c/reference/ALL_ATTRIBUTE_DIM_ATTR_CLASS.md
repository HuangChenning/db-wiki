---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_ATTRIBUTE_DIM_ATTR_CLASS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_ATTRIBUTE_DIM_ATTR_CLASS` describes the attribute classifications of the attribute dimensions accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_DIM_ATTR_CLASS` describes the attribute classifications of all attribute dimensions in the database.
- `USER_ATTRIBUTE_DIM_ATTR_CLASS` describes the attribute classifications of the attribute dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the attribute dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute dimension |
| `ATTRIBUTE_NAME` | `VARCHAR2(128)` |  | Name of the attribute |
| `CLASSIFICATION` | `VARCHAR2(128)` |  | Classification associated with the attribute |
| `VALUE` | `CLOB` |  | Value of the classification, or `NULL` if not specified |
| `LANGUAGE` | `VARCHAR2(64)` |  | NLS\_LANGUAGE value associated with the classification, or `NULL` if not specified |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the classification in the list of classifications associated with the attribute |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).