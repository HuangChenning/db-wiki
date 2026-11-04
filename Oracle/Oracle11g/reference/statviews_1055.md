---
title: ALL_CUBE_DIM_VIEW_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1055.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBE_DIM_VIEW_COLUMNS` describes the columns of the relational views of the OLAP cube dimensions accessible to the current user.

Related Views

- `DBA_CUBE_DIM_VIEW_COLUMNS` describes the columns of the relational views of all OLAP cube dimensions in the database.
- `USER_CUBE_DIM_VIEW_COLUMNS` describes the columns of the relational views of the OLAP cube dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the cube dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` |  | Name of a cube dimension, such as `PRODUCT` |
| `VIEW_NAME` | `VARCHAR2(30)` |  | Name of a view of the dimension, such as `PRODUCT_VIEW` |
| `COLUMN_NAME` | `VARCHAR2(30)` |  | Name of a column in the view, such as `LONG_DESCRIPTION` or `WAREHOUSE_ID` |
| `COLUMN_TYPE` | `VARCHAR2(11)` |  | Type of the column: - `KEY` - A key of the dimension view (that is, the dimension value itself) - `LEVEL_NAME` - Name of the level (if any) corresponding to a row in the view - `DIM_ORDER` - A column by which the results may be ordered (if present) - `MEMBER_TYPE` - `ATTRIBUTE` - An attribute owned by the dimension |
| `OBJECT_NAME` | `VARCHAR2(30)` |  | Name of the level or attribute represented in the column, such as `LONG_DESCRIPTION` or `WAREHOUSE_ID` |

See Also:

- ["DBA\_CUBE\_DIM\_VIEW\_COLUMNS"](statviews_3131.md)
- ["USER\_CUBE\_DIM\_VIEW\_COLUMNS"](statviews_5267.md)