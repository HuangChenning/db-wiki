---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CUBE_ATTR_VISIBILITY.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.143 ALL\_CUBE\_ATTR\_VISIBILITY

`ALL_CUBE_ATTR_VISIBILITY` describes the OLAP attributes visible for the dimensions, hierarchies, and levels accessible to the current user.

Related Views

- `DBA_CUBE_ATTR_VISIBILITY` describes all OLAP attributes visible for the dimensions, hierarchies, and levels in the database.
- `USER_CUBE_ATTR_VISIBILITY` describes the OLAP attributes visible for the dimensions, hierarchies, and levels owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the cube dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` |  | Name of a cube dimension (such as `TIME`) |
| `ATTRIBUTE_NAME` | `VARCHAR2(128)` |  | Name of an attribute of the dimension (such as `LONG_DESCRIPTION` or `END_DATE`) |
| `HIERARCHY_NAME` | `VARCHAR2(128)` |  | Name of a hierarchy for the dimension (such as `CALENDAR`) |
| `LEVEL_NAME` | `VARCHAR2(128)` |  | Name of the dimension level (such as `MONTH`) |
| `FROM_TYPE` | `VARCHAR2(10)` |  | Identifies the dimension type that the current row derives the attribute visibility from. Possible values:  - `DIMENSION` - Derives the attribute visibility from itself. - `HIERARCHY` - Derives the attribute visibility from the `VisibleAttributes` explicitly set on the associated `DIMENSION` or itself. - `DIM_LEVEL` - Derives the attribute visibility from the `VisibleAttributes` explicitly set on the associated `DIMENSION` or itself. - `HIER_LEVEL` - Derives the attribute visibility from the `VisibleAttributes` explicitly set on the associated `DIMENSION`, `HIERARCHY`, `DIM_LEVEL`, or itself. |
| `TO_TYPE` | `VARCHAR2(10)` |  | Identifies the dimension type for the current row. Possible values:  - `DIMENSION` - When the `TO_TYPE` is `DIMENSION`, then only the `DIMENSION_NAME` is populated. - `HIERARCHY` - When the `TO_TYPE` is `HIERARCHY`, then only the `DIMENSION_NAME` and `HIERARCHY_NAME` are populated. - `DIM_LEVEL` - When the `TO_TYPE` is `DIM_LEVEL`, then only the `DIMENSION_NAME` and `LEVEL_NAME` are populated. - `HIER_LEVEL` - When the `TO_TYPE` is `HIER_LEVEL`, then only the `HIERARCHY_NAME` and `LEVEL_NAME` are populated. |

See Also:

- " [DBA\_CUBE\_ATTR\_VISIBILITY](DBA_CUBE_ATTR_VISIBILITY.md) "
- " [USER\_CUBE\_ATTR\_VISIBILITY](USER_CUBE_ATTR_VISIBILITY.md) "