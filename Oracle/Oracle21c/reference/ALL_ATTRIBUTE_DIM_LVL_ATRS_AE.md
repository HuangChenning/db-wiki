---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ATTRIBUTE_DIM_LVL_ATRS_AE.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.99 ALL\_ATTRIBUTE\_DIM\_LVL\_ATRS\_AE

`ALL_ATTRIBUTE_DIM_LVL_ATRS_AE` describes the attributes of the levels of the attribute dimensions (across all editions) accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_DIM_LVL_ATRS_AE` describes the attributes of the levels of all attribute dimensions (across all editions) in the database.
- `USER_ATTRIBUTE_DIM_LVL_ATRS_AE` describes the attributes of the levels of the attribute dimensions (across all editions) owned by the current user. This view does not display the `OWNER` column.

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
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the attribute dimension is defined |

Note:

This view is available starting with Oracle Database 21c, Release Update 21.5.

See Also:

- " [DBA\_ATTRIBUTE\_DIM\_LVL\_ATRS\_AE](DBA_ATTRIBUTE_DIM_LVL_ATRS_AE.md) "
- " [USER\_ATTRIBUTE\_DIM\_LVL\_ATRS\_AE](USER_ATTRIBUTE_DIM_LVL_ATRS_AE.md) "