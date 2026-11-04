---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CUBE_MEASURES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.157 ALL\_CUBE\_MEASURES

`ALL_CUBE_MEASURES` describes the measures for the OLAP cubes accessible to the current user.

Related Views

- `DBA_CUBE_MEASURES` describes the measures for all OLAP cubes in the database.
- `USER_CUBE_MEASURES` describes the measures for the OLAP cubes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the cube |
| `CUBE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a cube, such as `UNITS_CUBE` |
| `MEASURE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a measure in the cube, such as `SALES` |
| `MEASURE_ID` | `NUMBER` | `NOT NULL` | ID of a measure |
| `OVERRIDE_SOLVE_SPEC` | `CLOB` |  | Syntax text for the measure's consistent solve specification that overrides that of its cube |
| `MEASURE_TYPE` | `VARCHAR2(7)` |  | Type of the OLAP measure:  - `BASE` - Base measures store the data - `DERIVED` - Derived measures calculate the data from base measures; also called calculated measures |
| `EXPRESSION` | `CLOB` |  | Expression that provides the values of the measure |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the measure in the session language |
| `DATA_TYPE` | `VARCHAR2(106)` |  | Data type of the measure, such as `NUMBER` |
| `DATA_LENGTH` | `NUMBER` | `NOT NULL` | Length of a character data type |
| `DATA_PRECISION` | `NUMBER` |  | Precision of a numeric data type |
| `DATA_SCALE` | `NUMBER` |  | Scale of a numeric data type |
| `LOOP_VAR_OVERRIDE` | `VARCHAR2(200)` |  | The value that overrides the `$LOOP_VAR` property of the OLAP derived measure |
| `LOOP_DENSE_OVERRIDE` | `VARCHAR2(200)` |  | The value that overrides the `$LOOP_DENSE` property of the OLAP derived measure |
| `LOOP_TYPE` | `VARCHAR2(200)` |  | The `$LOOP_TYPE` property of the OLAP derived measure.  Possible values:  - `INNER` - `OUTER` - `DENSE` |

See Also:

- " [DBA\_CUBE\_MEASURES](DBA_CUBE_MEASURES.md) "
- " [USER\_CUBE\_MEASURES](USER_CUBE_MEASURES.md) "