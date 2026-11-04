---
title: ALL_CUBE_HIER_VIEWS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1061.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBE_HIER_VIEWS` describes the hierarchies for the OLAP cube dimensions accessible to the current user.

Related Views

- `DBA_CUBE_HIER_VIEWS` describes the hierarchies for all OLAP cube dimensions in the database.
- `USER_CUBE_HIER_VIEWS` describes the hierarchies for the OLAP cube dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the cube dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a cube dimension, such as `TIME` |
| `HIERARCHY_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a hierarchy for the cube dimension, such as `CALENDAR` |
| `VIEW_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a view of the hierarchy, such as `TIME_CALENDAR_VIEW` |

See Also:

- ["DBA\_CUBE\_HIER\_VIEWS"](statviews_3137.md)
- ["USER\_CUBE\_HIER\_VIEWS"](statviews_5273.md)