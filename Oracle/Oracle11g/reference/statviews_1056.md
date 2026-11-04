---
title: ALL_CUBE_DIM_VIEWS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1056.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBE_DIM_VIEWS` describes the relational views of the OLAP dimensions accessible to the current user.

Related Views

- `DBA_CUBE_DIM_VIEWS` describes the relational views of all OLAP dimensions in the database.
- `USER_CUBE_DIM_VIEWS` describes the relational views of the OLAP dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the cube dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a cube dimension, such as `PRODUCT` |
| `VIEW_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a view of the cube dimension, such as `PRODUCT_VIEW` |

See Also:

- ["DBA\_CUBE\_DIM\_VIEWS"](statviews_3132.md)
- ["USER\_CUBE\_DIM\_VIEWS"](statviews_5268.md)