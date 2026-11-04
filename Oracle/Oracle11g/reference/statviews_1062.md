---
title: ALL_CUBE_HIERARCHIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1062.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBE_HIERARCHIES` describes the OLAP dimension hierarchies accessible to the current user.

Related Views

- `DBA_CUBE_HIERARCHIES` describes all OLAP dimension hierarchies in the database.
- `USER_CUBE_HIERARCHIES` describes the OLAP dimension hierarchies owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a dimension, such as `TIME` |
| `HIERARCHY_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a hierarchy for the dimension, such as `CALENDAR` |
| `HIERARCHY_TYPE` | `VARCHAR2(5)` |  | Type of the hierarchy: - `LEVEL` - `VALUE` |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the hierarchy in the session language |
| `IS_RAGGED` | `NUMBER` |  | Indicates whether ragged hierarchies are permitted in subsequent builds. User dimensions that are enabled for materialized views and Time dimensions are set to `0`. Builds then check the data for ragged hierarchies and fail if one is detected. When User dimensions are set to `1`, the builds do not check for ragged hierarchies. |
| `IS_SKIP_LEVEL` | `NUMBER` |  | Indicates whether skip-level hierarchies are permitted in subsequent builds. User dimensions that are enabled for materialized views and Time dimensions are set to `0`. Builds then check the data for skip-level hierarchies and fail if one is detected. When User dimensions are set to `1`, the builds do not check for skip-level hierarchies. |

See Also:

- ["DBA\_CUBE\_HIERARCHIES"](statviews_3138.md)
- ["USER\_CUBE\_HIERARCHIES"](statviews_5274.md)