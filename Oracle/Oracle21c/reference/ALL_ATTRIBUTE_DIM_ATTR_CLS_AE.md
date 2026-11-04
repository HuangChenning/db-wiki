---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ATTRIBUTE_DIM_ATTR_CLS_AE.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.85 ALL\_ATTRIBUTE\_DIM\_ATTR\_CLS\_AE

`ALL_ATTRIBUTE_DIM_ATTR_CLS_AE` describes the attribute classifications of the attribute dimensions (across all editions) accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_DIM_ATTR_CLS_AE` describes the attribute classifications of all attribute dimensions (across all editions) in the database.
- `USER_ATTRIBUTE_DIM_ATTR_CLS_AE` describes the attribute classifications of the attribute dimensions (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the attribute dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute dimension |
| `ATTRIBUTE_NAME` | `VARCHAR2(128)` |  | Name of the attribute |
| `CLASSIFICATION` | `VARCHAR2(128)` |  | Classification associated with the attribute |
| `VALUE` | `CLOB` |  | Value of the classification, or NULL if not specified |
| `LANGUAGE` | `VARCHAR2(64)` |  | `NLS_LANGUAGE` value associated with the classification, or NULL if not specified |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the classification in the list of classifications associated with the attribute |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the attribute dimension is defined |

Note:

This view is available starting with Oracle Database 21c, Release Update 21.5.

See Also:

- " [DBA\_ATTRIBUTE\_DIM\_ATTR\_CLS\_AE](DBA_ATTRIBUTE_DIM_ATTR_CLS_AE.md) "
- " [USER\_ATTRIBUTE\_DIM\_ATTR\_CLS\_AE](USER_ATTRIBUTE_DIM_ATTR_CLS_AE.md) "