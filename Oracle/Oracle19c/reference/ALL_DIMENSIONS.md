---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_DIMENSIONS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.165 ALL\_DIMENSIONS

`ALL_DIMENSIONS` describes the dimension objects accessible to the current user.

Related Views

- `DBA_DIMENSIONS` describes all dimensions in the database.
- `USER_DIMENSIONS` describes the dimensions in the current user's schema.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the dimension |
| `INVALID` | `VARCHAR2(1)` |  | Indicates whether the dimension is invalid (`Y`) or valid (`N`) |
| `COMPILE_STATE` | `VARCHAR2(13)` |  | Compile status of the dimension:  - `INVALID` - `NEEDS_COMPILE` - `ERROR` |
| `REVISION` | `NUMBER` |  | Dimension revision level |

See Also:

- " [DBA\_DIMENSIONS](DBA_DIMENSIONS.md) "
- " [USER\_DIMENSIONS](USER_DIMENSIONS.md) "