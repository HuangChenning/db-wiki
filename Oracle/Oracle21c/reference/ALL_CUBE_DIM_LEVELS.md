---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CUBE_DIM_LEVELS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.147 ALL\_CUBE\_DIM\_LEVELS

`ALL_CUBE_DIM_LEVELS` describes the OLAP dimension levels accessible to the current user.

Related Views

- `DBA_CUBE_DIM_LEVELS` describes all OLAP dimension levels in the database.
- `USER_CUBE_DIM_LEVELS` describes the OLAP dimension levels owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a dimension, such as `CUSTOMER` |
| `LEVEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a level in the dimension, such as `WAREHOUSE` |
| `LEVEL_ID` | `NUMBER` | `NOT NULL` | ID of the dimension level |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the dimension level in the session language |

See Also:

- " [DBA\_CUBE\_DIM\_LEVELS](DBA_CUBE_DIM_LEVELS.md) "
- " [USER\_CUBE\_DIM\_LEVELS](USER_CUBE_DIM_LEVELS.md) "