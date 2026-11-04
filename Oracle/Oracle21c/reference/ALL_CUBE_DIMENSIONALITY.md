---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CUBE_DIMENSIONALITY.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.151 ALL\_CUBE\_DIMENSIONALITY

`ALL_CUBE_DIMENSIONALITY` describes the dimension order for the OLAP cubes accessible to the current user.

Related Views

- `DBA_CUBE_DIMENSIONALITY` describes the dimension order for all OLAP cubes in the database.
- `USER_CUBE_DIMENSIONALITY` describes the dimension order for the OLAP cubes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the cube |
| `CUBE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a cube, such as `UNITS_CUBE` |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a dimension of the cube, such as `PRODUCT` |
| `DIMENSIONALITY_NAME` | `VARCHAR2(200)` |  | The name of a dimensionality of the cube. For example, a cube dimensioned by the `PRODUCT` dimension can have a product dimension named `PRODUCT_DIM`. |
| `DIMENSIONALITY_ID` | `NUMBER` | `NOT NULL` | ID of the cube dimensionality |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order number of the dimension in the cube |
| `IS_SPARSE` | `NUMBER` |  | Indicates whether the dimension is sparse in the cube (`1`) or not sparse (`0`) |
| `ET_ATTR_PREFIX` | `VARCHAR2(200)` |  | Specifies the prefix that will be added to the column names in the Materialized Views to ensure uniqueness. If the user does not specify an `ET_ATTR_PREFIX` for any dimensions in a cube, then they default in the pattern `D1_`, `D2_`, and so on. |

See Also:

- " [DBA\_CUBE\_DIMENSIONALITY](DBA_CUBE_DIMENSIONALITY.md) "
- " [USER\_CUBE\_DIMENSIONALITY](USER_CUBE_DIMENSIONALITY.md) "