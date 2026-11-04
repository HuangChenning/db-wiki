---
title: ALL_CUBE_VIEWS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1065.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBE_VIEWS` describes the relational views of the OLAP cubes accessible to the current user.

Related Views

- `DBA_CUBE_VIEWS` describes the relational views of all OLAP cubes in the database.
- `USER_CUBE_VIEWS` describes the relational views of the OLAP cubes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the cube |
| `CUBE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a cube, such as `UNITS_CUBE` |
| `VIEW_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a view of the cube, such as `UNITS_CUBE_VIEW` |

See Also:

- ["DBA\_CUBE\_VIEWS"](statviews_3141.md)
- ["USER\_CUBE\_VIEWS"](statviews_5277.md)