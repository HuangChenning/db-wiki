---
title: ALL_CUBE_DIMENSIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1058.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBE_DIMENSIONS` describes the OLAP cube dimensions accessible to the current user.

Related Views

- `DBA_CUBE_DIMENSIONS` describes all OLAP cube dimensions in the database.
- `USER_CUBE_DIMENSIONS` describes the OLAP cube dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the cube dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a cube dimension, such as `TIME` |
| `DIMENSION_TYPE` | `VARCHAR2(17)` |  | Type of the OLAP cube dimension: |
| `AW_NAME` | `VARCHAR2(30)` |  | Name of the analytic workspace that contains the cube dimension, such as `GLOBAL` |
| `DEFAULT_HIERARCHY_NAME` | `VARCHAR2(30)` |  | Name of the default hierarchy for the cube dimension, such as `FISCAL` |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the cube dimension in the session language |

See Also:

- ["DBA\_CUBE\_DIMENSIONS"](statviews_3134.md)
- ["USER\_CUBE\_DIMENSIONS"](statviews_5270.md)