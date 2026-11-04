---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_CUBE_SUB_PARTITION_LEVELS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_CUBE_SUB_PARTITION_LEVELS` describes the OLAP secondary partition levels in the database that are accessible by the user.

Related Views

- `DBA_CUBE_SUB_PARTITION_LEVELS` describes the OLAP secondary partition levels in the database.
- `USER_CUBE_SUB_PARTITION_LEVELS` describes the OLAP secondary partition levels in the database that are owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the OLAP secondary partition level |
| `CUBE_NAME` | `VARCHAR2(128)` |  | Name of the OLAP cube |
| `SUB_PARTITION_LEVEL_NAME` | `VARCHAR2(200)` |  | Name of the secondary partition level of the OLAP cube |
| `PRECOMPUTE_PERCENT` | `NUMBER` |  | Precompute percent of the secondary partition level of the OLAP cube |
| `PARTITION_DIMENSION_NAME` | `VARCHAR2(128)` |  | Name of the cube dimension for which there is a secondary partition level on the OLAP cube |
| `PARTITION_HIERARCHY_NAME` | `VARCHAR2(128)` |  | Name of the hierarchy for which there is a secondary partition level on the OLAP cube |
| `PARTITION_LEVEL_NAME` | `VARCHAR2(128)` |  | Name of the hierarchy level for which there is a secondary partition level on the OLAP cube |
| `SUB_PARTITION_LEVEL_ORDER` | `NUMBER` |  | Order number of the secondary partition level on the OLAP cube |

See Also:

- " [DBA\_CUBE\_SUB\_PARTITION\_LEVELS](DBA_CUBE_SUB_PARTITION_LEVELS.md) "
- " [USER\_CUBE\_SUB\_PARTITION\_LEVELS](USER_CUBE_SUB_PARTITION_LEVELS.md) "