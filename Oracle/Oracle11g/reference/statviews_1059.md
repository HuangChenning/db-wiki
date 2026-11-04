---
title: ALL_CUBE_HIER_LEVELS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1059.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBE_HIER_LEVELS` describes the hierarchy levels for the OLAP cube dimensions accessible to the current user.

Related Views

- `DBA_CUBE_HIER_LEVELS` describes the hierarchy levels for all OLAP cube dimensions in the database.
- `USER_CUBE_HIER_LEVELS` describes the hierarchy levels for the OLAP cube dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the cube dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a cube dimension, such as `TIME` |
| `HIERARCHY_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a hierarchy for the dimension, such as `CALENDAR` |
| `LEVEL_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the dimension level, such as `MONTH` |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order number of the level within the hierarchy; 0 is the top level |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the level in the session language |

See Also:

- ["DBA\_CUBE\_HIER\_LEVELS"](statviews_3135.md)
- ["USER\_CUBE\_HIER\_LEVELS"](statviews_5271.md)