---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ATTRIBUTE_DIMENSIONS_AE.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.109 ALL\_ATTRIBUTE\_DIMENSIONS\_AE

`ALL_ATTRIBUTE_DIMENSIONS_AE` describes the attribute dimensions (across all editions) accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_DIMENSIONS_AE` describes all attribute dimensions (across all editions) in the database.
- `USER_ATTRIBUTE_DIMENSIONS_AE` describes the attribute dimensions (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of attribute dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute dimension |
| `DIMENSION_TYPE` | `VARCHAR2(8)` |  | Type of the attribute dimension: - `TIME` - `STANDARD` |
| `CACHE_STAR` | `VARCHAR2(12)` | `NOT NULL` | Type of the cache for the dimension star table: - `NONE` indicates that no cache is being used - `DYNAMIC` - `MATERIALIZED` (the default value when a cache is used) |
| `MAT_TABLE_OWNER` | `VARCHAR2(128)` |  | The owner of the materialized table |
| `MAT_TABLE_NAME` | `VARCHAR2(128)` |  | The name of the materialized table |
| `ALL_MEMBER_NAME` | `CLOB)` | `NOT NULL` | An expression for the name of the ALL member for the attribute dimension |
| `ALL_MEMBER_CAPTION` | `CLOB` |  | An expression for the caption for the ALL member of the attribute dimension, or NULL if not specified |
| `ALL_MEMBER_DESCRIPTION` | `CLOB` |  | An expression for the description for the ALL member of the attribute dimension |
| `COMPILE_STATE` | `VARCHAR2(7)` |  | Compile status of the attribute dimension:  - `VALID` - `INVALID` |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the attribute dimension is defined |

Note:

This view is available starting with Oracle Database 21c, Release Update 21.5.

See Also:

- " [DBA\_ATTRIBUTE\_DIMENSIONS\_AE](DBA_ATTRIBUTE_DIMENSIONS_AE.md) "
- " [USER\_ATTRIBUTE\_DIMENSIONS\_AE](USER_ATTRIBUTE_DIMENSIONS_AE.md) "