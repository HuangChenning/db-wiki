---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ATTRIBUTE_DIM_CLASS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.88 ALL\_ATTRIBUTE\_DIM\_CLASS

`ALL_ATTRIBUTE_DIM_CLASS` describes the classifications of the attribute dimensions accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_DIM_CLASS` describes the classifications of all attribute dimensions in the database.
- `USER_ATTRIBUTE_DIM_CLASS` describes the classifications of the attribute dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the attribute dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute dimension |
| `CLASSIFICATION` | `VARCHAR2(128)` |  | Classification associated with the attribute dimension |
| `VALUE` | `CLOB` |  | Value of the classification, or NULL if not specified |
| `LANGUAGE` | `VARCHAR2(64)` |  | `NLS_LANGUAGE` value associated with the classification, or NULL if not specified |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the classification in the list of classifications associated with the attribute dimension |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

See Also:

- " [DBA\_ATTRIBUTE\_DIM\_CLASS](DBA_ATTRIBUTE_DIM_CLASS.md) "
- " [USER\_ATTRIBUTE\_DIM\_CLASS](USER_ATTRIBUTE_DIM_CLASS.md) "