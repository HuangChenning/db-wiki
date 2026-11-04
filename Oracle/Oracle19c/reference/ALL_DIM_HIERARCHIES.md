---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_DIM_HIERARCHIES.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.161 ALL\_DIM\_HIERARCHIES

`ALL_DIM_HIERARCHIES` describes all dimension hierarchies accessible to the current user.

Related Views

- `DBA_DIM_HIERARCHIES` describes all such hierarchies in the database.
- `USER_DIM_HIERARCHIES` describes all such hierarchies owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the dimension |
| `HIERARCHY_NAME` | `VARCHAR2(128)` |  | Hierarchy name |

See Also:

- " [DBA\_DIM\_HIERARCHIES](DBA_DIM_HIERARCHIES.md) "
- " [USER\_DIM\_HIERARCHIES](USER_DIM_HIERARCHIES.md) "