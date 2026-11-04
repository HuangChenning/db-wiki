---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_DIM_HIERARCHIES.html
tags:
  - oracle
  - 12c
  - reference
---

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