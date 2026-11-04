---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CUBES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.162 ALL\_CUBES

`ALL_CUBES` describes the OLAP cubes accessible to the current user.

Related Views

- `DBA_CUBES` describes all OLAP cubes in the database.
- `USER_CUBES` describes the OLAP cubes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the cube |
| `CUBE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a cube, such as `UNITS_CUBE` |
| `CUBE_ID` | `NUMBER` | `NOT NULL` | ID of a cube |
| `AW_NAME` | `VARCHAR2(128)` |  | Name of the analytic workspace that contains the cube, such as `GLOBAL` |
| `CONSISTENT_SOLVE_SPEC` | `CLOB` |  | Default aggregation rules for the cube |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the cube in the session language |
| `SPARSE_TYPE` | `VARCHAR2(200)` |  | Text value indicating the type of sparsity for the OLAP cube |
| `PRECOMPUTE_CONDITION` | `CLOB` |  | Condition syntax representing the precompute condition of the OLAP cube |
| `PRECOMPUTE_PERCENT` | `NUMBER` |  | Percentage of aggregate data values that are calculated and stored during data maintenance. If the cube is partitioned, then this percentage is for the bottom partitions. |
| `PRECOMPUTE_PERCENT_TOP` | `NUMBER` |  | Percentage of aggregate data values in the top partition that are calculated and stored during data maintenance |
| `PARTITION_DIMENSION_NAME` | `VARCHAR2(128)` |  | Name of the dimension used to partition the cube, such as `TIME` |
| `PARTITION_HIERARCHY_NAME` | `VARCHAR2(128)` |  | Name of the dimension hierarchy used to partition the cube, such as `CALENDAR` |
| `PARTITION_LEVEL_NAME` | `VARCHAR2(128)` |  | Name of the level used to partition the cube, such as `QUARTER` |
| `REFRESH_MVIEW_NAME` | `VARCHAR2(200)` |  | Name of the refresh materialized view for the OLAP cube |
| `REWRITE_MVIEW_NAME` | `VARCHAR2(200)` |  | Name of the rewrite materialized view for the OLAP cube |
| `DEFAULT_BUILD_SPEC` | `CLOB` |  | The default build specification for the OLAP cube |
| `MEASURE_STORAGE` | `VARCHAR2(200)` |  | The measure storage for the OLAP cube. Possible values:  - `INDEPENDENT` - `SHARED` |
| `SQL_CUBE_STORAGE_TYPE` | `CLOB` |  | The SQL cube storage type for the OLAP cube. This value represents a SQL data type. |
| `CUBE_STORAGE_TYPE` | `VARCHAR2(200)` |  | The cube storage type for the OLAP cube. This value represents a DML data type. |

See Also:

- " [DBA\_CUBES](DBA_CUBES.md) "
- " [USER\_CUBES](USER_CUBES.md) "