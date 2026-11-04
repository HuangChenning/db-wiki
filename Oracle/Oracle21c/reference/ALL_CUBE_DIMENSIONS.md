---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CUBE_DIMENSIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.152 ALL\_CUBE\_DIMENSIONS

`ALL_CUBE_DIMENSIONS` describes the OLAP cube dimensions accessible to the current user.

Related Views

- `DBA_CUBE_DIMENSIONS` describes all OLAP cube dimensions in the database.
- `USER_CUBE_DIMENSIONS` describes the OLAP cube dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the cube dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a cube dimension, such as `TIME` |
| `DIMENSION_ID` | `NUMBER` | `NOT NULL` | ID of the cube dimension |
| `DIMENSION_TYPE` | `VARCHAR2(17)` |  | Type of the OLAP cube dimension:  - `STANDARD` - `TIME` |
| `AW_NAME` | `VARCHAR2(128)` |  | Name of the analytic workspace that contains the cube dimension, such as `GLOBAL` |
| `DEFAULT_HIERARCHY_NAME` | `VARCHAR2(128)` |  | Name of the default hierarchy for the cube dimension, such as `FISCAL` |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the cube dimension in the session language |
| `HIERARCHY_CONSISTENCY_RULE` | `VARCHAR2(200)` |  | Hierarchy consistency rule of the OLAP cube dimension. Possible values:  - `CONSISTENT` - `STAR_CONSISTENT` - `SOLVE_CONSISTENT` |
| `ADD_UNIQUE_KEY_PREFIX` | `VARCHAR2(3)` |  | `Add_Unique_Key_Prefix` flag of the OLAP cube dimension. Possible values:  - YES: This is the value if `AddUniqueKeyPrefix="True"` was set in the metadata. 	This tells the system to add the level name prefix to the dimension members. This should be done when a dimension member can have the same value across different levels, for example, New York (state) and New York (city). - NO: This is the value if `AddUniqueKeyPrefix="True"` was not set in the metadata. |
| `CUSTOM_ORDER` | `CLOB` |  | The textual representation of the sort orderby clause used to load dimension members into the AW |

See Also:

- " [DBA\_CUBE\_DIMENSIONS](DBA_CUBE_DIMENSIONS.md) "
- " [USER\_CUBE\_DIMENSIONS](USER_CUBE_DIMENSIONS.md) "