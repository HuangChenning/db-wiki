---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_DIM_LEVELS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.172 ALL\_DIM\_LEVELS

All columns of a dimension level must come from the same relation.

Related Views

- `DBA_DIM_LEVELS` describes all dimension levels in the database.
- `USER_DIM_LEVELS` describes the levels of all dimensions owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the dimension |
| `LEVEL_NAME` | `VARCHAR2(128)` |  | Unique within a dimension |
| `NUM_COLUMNS` | `NUMBER` |  | Number of columns in the level definition |
| `DETAILOBJ_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the detail object that the keys of this level come from |
| `DETAILOBJ_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table that the keys of this level come from |
| `SKIP_WHEN_NULL` | `VARCHAR2(1)` |  | Indicates whether the level is declared with the `SKIP WHEN NULL` clause (`Y`) or not (`N`) |

See Also:

- " [DBA\_DIM\_LEVELS](DBA_DIM_LEVELS.md) "
- " [USER\_DIM\_LEVELS](USER_DIM_LEVELS.md) "