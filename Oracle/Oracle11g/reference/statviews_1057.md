---
title: ALL_CUBE_DIMENSIONALITY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1057.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBE_DIMENSIONALITY` describes the dimension order for the OLAP cubes accessible to the current user.

Related Views

- `DBA_CUBE_DIMENSIONALITY` describes the dimension order for all OLAP cubes in the database.
- `USER_CUBE_DIMENSIONALITY` describes the dimension order for the OLAP cubes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the cube |
| `CUBE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a cube, such as `UNITS_CUBE` |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a dimension of the cube, such as `PRODUCT` |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order number of the dimension in the cube |
| `IS_SPARSE` | `NUMBER` |  | Indicates whether the dimension is sparse in the cube (`1`) or not sparse (`0`) |
| `ET_ATTR_PREFIX` | `VARCHAR2(200)` |  | Specifies the prefix that will be added to the column names in the Materialized Views to ensure uniqueness. If the user does not specify an `ET_ATTR_PREFIX` for any dimensions in a cube, then they default in the pattern `D1_`, `D2_`, and so on. |

See Also:

- ["DBA\_CUBE\_DIMENSIONALITY"](statviews_3133.md)
- ["USER\_CUBE\_DIMENSIONALITY"](statviews_5269.md)