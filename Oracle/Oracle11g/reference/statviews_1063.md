---
title: ALL_CUBE_MEASURES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1063.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBE_MEASURES` describes the measures for the OLAP cubes accessible to the current user.

Related Views

- `DBA_CUBE_MEASURES` describes the measures for all OLAP cubes in the database.
- `USER_CUBE_MEASURES` describes the measures for the OLAP cubes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the cube |
| `CUBE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a cube, such as `UNITS_CUBE` |
| `MEASURE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a measure in the cube, such as `SALES` |
| `OVERRIDE_SOLVE_SPEC` | `CLOB` |  | Syntax text for the measure's consistent solve specification that overrides that of its cube |
| `MEASURE_TYPE` | `VARCHAR2(7)` |  | Type of the OLAP measure: - `BASE` - Base measures store the data - `DERIVED` - Derived measures calculate the data from base measures; also called calculated measures |
| `EXPRESSION` | `CLOB` |  | Expression that provides the values of the measure |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the measure in the session language |
| `DATA_TYPE` | `VARCHAR2(106)` |  | Data type of the measure, such as `NUMBER` |
| `DATA_LENGTH` | `NUMBER` | `NOT NULL` | Length of a character data type |
| `DATA_PRECISION` | `NUMBER` |  | Precision of a numeric data type |
| `DATA_SCALE` | `NUMBER` |  | Scale of a numeric data type |

See Also:

- ["DBA\_CUBE\_MEASURES"](statviews_3139.md)
- ["USER\_CUBE\_MEASURES"](statviews_5275.md)