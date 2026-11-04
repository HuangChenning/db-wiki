---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_CUBE_VIEWS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.153 ALL\_CUBE\_VIEWS

`ALL_CUBE_VIEWS` describes the relational views of the OLAP cubes accessible to the current user.

Related Views

- `DBA_CUBE_VIEWS` describes the relational views of all OLAP cubes in the database.
- `USER_CUBE_VIEWS` describes the relational views of the OLAP cubes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the cube |
| `CUBE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a cube, such as `UNITS_CUBE` |
| `VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a view of the cube, such as `UNITS_CUBE_VIEW` |

See Also:

- " [DBA\_CUBE\_VIEWS](DBA_CUBE_VIEWS.md) "
- " [USER\_CUBE\_VIEWS](USER_CUBE_VIEWS.md) "