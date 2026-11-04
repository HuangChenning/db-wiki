---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_CUBE_DIM_VIEWS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.142 ALL\_CUBE\_DIM\_VIEWS

`ALL_CUBE_DIM_VIEWS` describes the relational views of the OLAP dimensions accessible to the current user.

Related Views

- `DBA_CUBE_DIM_VIEWS` describes the relational views of all OLAP dimensions in the database.
- `USER_CUBE_DIM_VIEWS` describes the relational views of the OLAP dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the cube dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a cube dimension, such as `PRODUCT` |
| `VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a view of the cube dimension, such as `PRODUCT_VIEW` |

See Also:

- " [DBA\_CUBE\_DIM\_VIEWS](DBA_CUBE_DIM_VIEWS.md) "
- " [USER\_CUBE\_DIM\_VIEWS](USER_CUBE_DIM_VIEWS.md) "