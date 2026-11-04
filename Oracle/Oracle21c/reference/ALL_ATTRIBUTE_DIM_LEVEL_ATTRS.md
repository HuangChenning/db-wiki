---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ATTRIBUTE_DIM_LEVEL_ATTRS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.95 ALL\_ATTRIBUTE\_DIM\_LEVEL\_ATTRS

`ALL_ATTRIBUTE_DIM_LEVEL_ATTRS` describes the attributes of the levels of the attribute dimensions accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_DIM_LEVEL_ATTRS` describes the attributes of the levels of all attribute dimensions in the database.
- `USER_ATTRIBUTE_DIM_LEVEL_ATTRS` describes the attributes of the levels of the attribute dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the attribute dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` |  | Name of the attribute dimension |
| `LEVEL_NAME` | `VARCHAR2(128)` |  | Name of the attribute dimension level |
| `ATTRIBUTE_NAME` | `VARCHAR2(128)` |  | Name of the attribute determined by the level |
| `ROLE` | `VARCHAR2(4)` |  | Role of the attribute determined by the level |
| `IS_MINIMAL_DTM` | `VARCHAR2(1)` |  | Indicates whether the attribute is minimally determined (`Y`) or not (`N`) |
| `ORDER_NUM` | `NUMBER` |  | Order of the attribute in the list of attributes determined by the level |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

See Also:

- " [DBA\_ATTRIBUTE\_DIM\_LEVEL\_ATTRS](DBA_ATTRIBUTE_DIM_LEVEL_ATTRS.md) "
- " [USER\_ATTRIBUTE\_DIM\_LEVEL\_ATTRS](USER_ATTRIBUTE_DIM_LEVEL_ATTRS.md) "