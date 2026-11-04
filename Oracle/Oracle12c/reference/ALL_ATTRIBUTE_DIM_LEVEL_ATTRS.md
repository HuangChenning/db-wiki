---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_ATTRIBUTE_DIM_LEVEL_ATTRS.html
tags:
  - oracle
  - 12c
  - reference
---

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

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_ATTRIBUTE\_DIM\_LEVEL\_ATTRS](DBA_ATTRIBUTE_DIM_LEVEL_ATTRS.md) "
- " [USER\_ATTRIBUTE\_DIM\_LEVEL\_ATTRS](USER_ATTRIBUTE_DIM_LEVEL_ATTRS.md) "