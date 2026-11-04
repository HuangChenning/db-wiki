---
title: ALL_CUBE_HIER_VIEW_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1060.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBE_HIER_VIEW_COLUMNS` describes the columns of the relational hierarchy views of the OLAP cube dimensions accessible to the current user.

Related Views

- `DBA_CUBE_HIER_VIEW_COLUMNS` describes the columns of the relational hierarchy views of all OLAP cube dimensions in the database.
- `USER_CUBE_HIER_VIEW_COLUMNS` describes the columns of the relational hierarchy views of the OLAP cube dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the cube dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` |  | Name of a cube dimension, such as `TIME` |
| `HIERARCHY_NAME` | `VARCHAR2(30)` |  | Name of a hierarchy for the cube dimension, such as `CALENDAR` |
| `VIEW_NAME` | `VARCHAR2(30)` |  | Name of a view of the hierarchy, such as `TIME_CALENDAR_VIEW` |
| `COLUMN_NAME` | `VARCHAR2(30)` |  | Name of a column in the view, such as `CALENDAR_QUARTER` or `PARENT` |
| `COLUMN_TYPE` | `VARCHAR2(11)` |  | Type of the column: - `KEY` - A key of the hierarchy view (that is, the hierarchy value itself) - `PARENT` - Dimension value of the parent of the current row in the view (or NULL if no parent) - `LEVEL_NAME` - Name of the level (if any) corresponding to a row in the view - `DEPTH` - Depth in the hierarchy tree of the current row in the view - `HIER_ORDER` - A column by which the results may be ordered (if present) - `MEMBER_TYPE` - `ATTRIBUTE` - An attribute owned by the hierarchy - `LEVEL` - One of the level columns comprising the hierarchy |
| `OBJECT_NAME` | `VARCHAR2(30)` |  | Name of a level or attribute for the dimension |

See Also:

- ["DBA\_CUBE\_HIER\_VIEW\_COLUMNS"](statviews_3136.md)
- ["USER\_CUBE\_HIER\_VIEW\_COLUMNS"](statviews_5272.md)