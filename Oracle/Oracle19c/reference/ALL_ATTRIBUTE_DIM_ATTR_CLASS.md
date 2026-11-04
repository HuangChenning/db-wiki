---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_ATTRIBUTE_DIM_ATTR_CLASS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.75 ALL\_ATTRIBUTE\_DIM\_ATTR\_CLASS

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
| `VALUE` | `CLOB` |  | Value of the classification, or NULL if not specified |
| `LANGUAGE` | `VARCHAR2(64)` |  | `NLS_LANGUAGE` value associated with the classification, or NULL if not specified |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the classification in the list of classifications associated with the attribute |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |