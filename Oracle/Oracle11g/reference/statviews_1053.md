---
title: ALL_CUBE_DIM_LEVELS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1053.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBE_DIM_LEVELS` describes the OLAP dimension levels accessible to the current user.

Related Views

- `DBA_CUBE_DIM_LEVELS` describes all OLAP dimension levels in the database.
- `USER_CUBE_DIM_LEVELS` describes the OLAP dimension levels owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a dimension, such as `CUSTOMER` |
| `LEVEL_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a level in the dimension, such as `WAREHOUSE` |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the dimension level in the session language |

See Also:

- ["DBA\_CUBE\_DIM\_LEVELS"](statviews_3129.md)
- ["USER\_CUBE\_DIM\_LEVELS"](statviews_5265.md)