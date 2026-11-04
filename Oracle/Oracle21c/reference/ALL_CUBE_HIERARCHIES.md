---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CUBE_HIERARCHIES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.156 ALL\_CUBE\_HIERARCHIES

`ALL_CUBE_HIERARCHIES` describes the OLAP dimension hierarchies accessible to the current user.

Related Views

- `DBA_CUBE_HIERARCHIES` describes all OLAP dimension hierarchies in the database.
- `USER_CUBE_HIERARCHIES` describes the OLAP dimension hierarchies owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a dimension, such as `TIME` |
| `HIERARCHY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a hierarchy for the dimension, such as `CALENDAR` |
| `HIERARCHY_ID` | `NUMBER` | `NOT NULL` | ID of the hierarchy |
| `HIERARCHY_TYPE` | `VARCHAR2(5)` |  | Type of the hierarchy:  - `LEVEL` - `VALUE` |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the hierarchy in the session language |
| `IS_RAGGED` | `NUMBER` |  | Indicates whether ragged hierarchies are permitted in subsequent builds. User dimensions that are enabled for materialized views and Time dimensions are set to `0`. Builds then check the data for ragged hierarchies and fail if one is detected. When User dimensions are set to `1`, the builds do not check for ragged hierarchies. |
| `IS_SKIP_LEVEL` | `NUMBER` |  | Indicates whether skip-level hierarchies are permitted in subsequent builds. User dimensions that are enabled for materialized views and Time dimensions are set to `0`. Builds then check the data for skip-level hierarchies and fail if one is detected. When User dimensions are set to `1`, the builds do not check for skip-level hierarchies. |
| `REFRESH_MVIEW_NAME` | `VARCHAR2(200)` |  | Name of the Refresh Materialized View associated with the hierarchy |
| `CUSTOM_ORDER` | `CLOB` |  | The textual representation of the sort orderby clause used to load dimension members of the hierarchy into the AW |

See Also:

- " [DBA\_CUBE\_HIERARCHIES](DBA_CUBE_HIERARCHIES.md) "
- " [USER\_CUBE\_HIERARCHIES](USER_CUBE_HIERARCHIES.md) "