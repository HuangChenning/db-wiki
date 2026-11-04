---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_DIM_CHILD_OF.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.168 ALL\_DIM\_CHILD\_OF

`ALL_DIM_CHILD_OF` describes hierarchical relationships of `1` to n between the pairs of levels in the dimensions accessible to the current user.

Related Views

- `DBA_DIM_CHILD_OF` describes all such hierarchical relationships in the database.
- `USER_DIM_CHILD_OF` describes all such hierarchical attributes in the current user's schema.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the dimension |
| `HIERARCHY_NAME` | `VARCHAR2(128)` |  | Hierarchy name |
| `POSITION` | `NUMBER` | `NOT NULL` | Hierarchical position within this hierarchy, position 1 being the most detailed |
| `CHILD_LEVEL_NAME` | `VARCHAR2(128)` |  | Child side of 1:n relationship |
| `JOIN_KEY_ID` | `VARCHAR2(40)` |  | If non-null, then the child joins to the parent |
| `PARENT_LEVEL_NAME` | `VARCHAR2(128)` |  | Parent side of 1:n relationship in relation to the `CHILD_LEVEL_NAME` |

See Also:

- " [DBA\_DIM\_CHILD\_OF](DBA_DIM_CHILD_OF.md) "
- " [USER\_DIM\_CHILD\_OF](USER_DIM_CHILD_OF.md) "