---
title: ALL_DIM_CHILD_OF
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1072.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_DIM_CHILD_OF` describes hierarchical relationships of `1` to n between the pairs of levels in the dimensions accessible to the current user.

Related Views

- `DBA_DIM_CHILD_OF` describes all such hierarchical relationships in the database.
- `USER_DIM_CHILD_OF` describes all such hierarchical attributes in the current user's schema.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the dimension |
| `HIERARCHY_NAME` | `VARCHAR2(30)` |  | Hierarchy name |
| `POSITION` | `NUMBER` | `NOT NULL` | Hierarchical position within this hierarchy, position 1 being the most detailed |
| `CHILD_LEVEL_NAME` | `VARCHAR2(30)` |  | Child side of 1:n relationship |
| `JOIN_KEY_ID` | `VARCHAR2(40)` |  | If non-null, then the child joins to the parent |
| `PARENT_LEVEL_NAME` | `VARCHAR2(30)` |  | Parent side of 1:n relationship in relation to the `CHILD_LEVEL_NAME` |