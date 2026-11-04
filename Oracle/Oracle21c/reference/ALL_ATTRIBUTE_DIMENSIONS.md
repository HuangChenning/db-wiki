---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ATTRIBUTE_DIMENSIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.108 ALL\_ATTRIBUTE\_DIMENSIONS

`ALL_ATTRIBUTE_DIMENSIONS` describes the attribute dimensions accessible to the current user.

Related Views

- `DBA_ATTRIBUTE_DIMENSIONS` describes all attribute dimensions in the database.
- `USER_ATTRIBUTE_DIMENSIONS` describes the attribute dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of attribute dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute dimension |
| `DIMENSION_TYPE` | `VARCHAR2(8)` |  | Type of the attribute dimension: - `TIME` - `STANDARD` |
| `CACHE_STAR` <sup>Foot 1</sup> | `VARCHAR2(12)` | `NOT NULL` | Type of the cache for the dimension star table: - `NONE` indicates that no cache is being used - `DYNAMIC` - `MATERIALIZED` (the default value when a cache is used) |
| `MAT_TABLE_OWNER` <sup>Foot 1</sup> | `VARCHAR2(128)` |  | The owner of the materialized table |
| `MAT_TABLE_NAME` <sup>Foot 1</sup> | `VARCHAR2(128)` |  | The name of the materialized table |
| `ALL_MEMBER_NAME` | `CLOB` | `NOT NULL` | An expression for the name of the ALL member for the attribute dimension |
| `ALL_MEMBER_CAPTION` | `CLOB` |  | An expression for the caption for the ALL member of the attribute dimension, or NULL if not specified |
| `ALL_MEMBER_DESCRIPTION` | `CLOB` |  | An expression for the description for the ALL member of the attribute dimension |
| `COMPILE_STATE` | `VARCHAR2(7)` |  | Compile status of the attribute dimension:  - `VALID` - `INVALID` |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.

See Also:

- " [DBA\_ATTRIBUTE\_DIMENSIONS](DBA_ATTRIBUTE_DIMENSIONS.md) "
- " [USER\_ATTRIBUTE\_DIMENSIONS](USER_ATTRIBUTE_DIMENSIONS.md) "