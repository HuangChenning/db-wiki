---
title: ALL_CUBES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1066.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBES` describes the OLAP cubes accessible to the current user.

Related Views

- `DBA_CUBES` describes all OLAP cubes in the database.
- `USER_CUBES` describes the OLAP cubes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the cube |
| `CUBE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a cube, such as `UNITS_CUBE` |
| `AW_NAME` | `VARCHAR2(30)` |  | Name of the analytic workspace that contains the cube, such as `GLOBAL` |
| `CONSISTENT_SOLVE_SPEC` | `CLOB` |  | Default aggregation rules for the cube |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the cube in the session language |
| `SPARSE_TYPE` | `VARCHAR2(200)` |  | Text value indicating the type of sparsity for the OLAP cube |
| `PRECOMPUTE_CONDITION` | `CLOB` |  | Condition syntax representing the precompute condition of the OLAP cube |
| `PRECOMPUTE_PERCENT` | `NUMBER` |  | Percentage of aggregate data values that are calculated and stored during data maintenance. If the cube is partitioned, then this percentage is for the bottom partitions. |
| `PRECOMPUTE_PERCENT_TOP` | `NUMBER` |  | Percentage of aggregate data values in the top partition that are calculated and stored during data maintenance |
| `PARTITION_DIMENSION_NAME` | `VARCHAR2(30)` |  | Name of the dimension used to partition the cube, such as `TIME` |
| `PARTITION_HIERARCHY_NAME` | `VARCHAR2(30)` |  | Name of the dimension hierarchy used to partition the cube, such as `CALENDAR` |
| `PARTITION_LEVEL_NAME` | `VARCHAR2(30)` |  | Name of the level used to partition the cube, such as `QUARTER` |

See Also:

- ["DBA\_CUBES"](statviews_3142.md)
- ["USER\_CUBES"](statviews_5278.md)