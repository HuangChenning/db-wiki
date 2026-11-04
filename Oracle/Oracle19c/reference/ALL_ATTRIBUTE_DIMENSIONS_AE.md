---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_ATTRIBUTE_DIMENSIONS_AE.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.101 ALL\_ATTRIBUTE\_DIMENSIONS\_AE

`ALL_ATTRIBUTE_DIMENSIONS_AE` describes the attribute dimensions (across all editions) accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_DIMENSIONS_AE` describes all attribute dimensions (across all editions) in the database.
- `USER_ATTRIBUTE_DIMENSIONS_AE` describes the attribute dimensions (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of attribute dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute dimension |
| `DIMENSION_TYPE` | `VARCHAR2(8)` |  | Type of the attribute dimension: - `TIME` - `STANDARD` |
| `ALL_MEMBER_NAME` | `CLOB)` | `NOT NULL` | An expression for the name of the ALL member for the attribute dimension |
| `ALL_MEMBER_CAPTION` | `CLOB` |  | An expression for the caption for the ALL member of the attribute dimension, or NULL if not specified |
| `ALL_MEMBER_DESCRIPTION` | `CLOB` |  | An expression for the description for the ALL member of the attribute dimension |
| `COMPILE_STATE` | `VARCHAR2(7)` |  | Compile status of the attribute dimension:  - `VALID` - `INVALID` |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the attribute dimension is defined |

Note:

This view is available starting with Oracle Database 19c, Release Update 19.13.

See Also:

- " [DBA\_ATTRIBUTE\_DIMENSIONS\_AE](DBA_ATTRIBUTE_DIMENSIONS_AE.md) "
- " [USER\_ATTRIBUTE\_DIMENSIONS\_AE](USER_ATTRIBUTE_DIMENSIONS_AE.md) "