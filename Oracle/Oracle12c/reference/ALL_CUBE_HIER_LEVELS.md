---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_CUBE_HIER_LEVELS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_CUBE_HIER_LEVELS` describes the hierarchy levels for the OLAP cube dimensions accessible to the current user.

Related Views

- `DBA_CUBE_HIER_LEVELS` describes the hierarchy levels for all OLAP cube dimensions in the database.
- `USER_CUBE_HIER_LEVELS` describes the hierarchy levels for the OLAP cube dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the cube dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a cube dimension, such as `TIME` |
| `HIERARCHY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a hierarchy for the dimension, such as `CALENDAR` |
| `LEVEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the dimension level, such as `MONTH` |
| `HIERARCHY_LEVEL_ID` | `NUMBER` | `NOT NULL` | ID of the hierarchy level |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order number of the level within the hierarchy; 0 is the top level |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the level in the session language |

See Also:

- " [DBA\_CUBE\_HIER\_LEVELS](DBA_CUBE_HIER_LEVELS.md) "
- " [USER\_CUBE\_HIER\_LEVELS](USER_CUBE_HIER_LEVELS.md) "