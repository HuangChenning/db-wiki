---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_DIM_LEVEL_KEY.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.171 ALL\_DIM\_LEVEL\_KEY

The position of a column within a level is specified by `KEY_POSITION`.

Related Views

- `DBA_DIM_LEVEL_KEY` describes all columns of dimension levels in the database.
- `USER_DIM_LEVEL_KEY` describes all columns of dimension levels owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the dimension |
| `LEVEL_NAME` | `VARCHAR2(128)` |  | Name of the hierarchy level |
| `KEY_POSITION` | `NUMBER` | `NOT NULL` | Ordinal position of the key column within the level |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the key column |

See Also:

- " [DBA\_DIM\_LEVEL\_KEY](DBA_DIM_LEVEL_KEY.md) "
- " [USER\_DIM\_LEVEL\_KEY](USER_DIM_LEVEL_KEY.md) "