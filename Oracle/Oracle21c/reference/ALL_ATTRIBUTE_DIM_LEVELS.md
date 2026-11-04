---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ATTRIBUTE_DIM_LEVELS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.96 ALL\_ATTRIBUTE\_DIM\_LEVELS

`ALL_ATTRIBUTE_DIM_LEVELS` describes the levels of the attribute dimensions accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_DIM_LEVELS` describes the levels of all attribute dimensions in the database.
- `USER_ATTRIBUTE_DIM_LEVELS` describes the levels of the attribute dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the attribute dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute dimension |
| `LEVEL_NAME` | `VARCHAR2(128)` |  | Name of the attribute dimension level |
| `SKIP_WHEN_NULL` | `VARCHAR2(1)` |  | Indicates whether to skip the level when the key is NULL; the value can be `Y` or `N`. |
| `LEVEL_TYPE` | `VARCHAR2(10)` |  | Type of attribute dimension level |
| `MEMBER_NAME_EXPR` | `CLOB` | `NOT NULL` | Expression representing the level member name |
| `MEMBER_CAPTION_EXPR` | `CLOB` |  | Expression representing the level member caption, or NULL if not specified |
| `MEMBER_DESCRIPTION_EXPR` | `CLOB` |  | Expression representing the level member description, or NULL if not specified |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the level in the list of attribute dimension levels |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

See Also:

- " [DBA\_ATTRIBUTE\_DIM\_LEVELS](DBA_ATTRIBUTE_DIM_LEVELS.md) "
- " [USER\_ATTRIBUTE\_DIM\_LEVELS](USER_ATTRIBUTE_DIM_LEVELS.md) "