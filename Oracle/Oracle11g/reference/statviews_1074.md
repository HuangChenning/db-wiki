---
title: ALL_DIM_JOIN_KEY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1074.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_DIM_JOIN_KEY` describes the joins between two dimension tables that are accessible to the current user. The join is always specified between a parent dimension level column and a child column.

Related Views

- `DBA_DIM_JOIN_KEY` describes all such joins in the database.
- `USER_DIM_JOIN_KEY` describes all such joins owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the dimension |
| `DIM_KEY_ID` | `NUMBER` | `NOT NULL` | Join key ID (unique within a dimension) |
| `LEVEL_NAME` | `VARCHAR2(30)` |  | Name of the hierarchy level |
| `KEY_POSITION` | `NUMBER` | `NOT NULL` | Ordinal position of the key column within the level |
| `HIERARCHY_NAME` | `VARCHAR2(30)` |  | Name of the hierarchy |
| `CHILD_JOIN_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the join column table |
| `CHILD_JOIN_TABLE` | `VARCHAR2(30)` | `NOT NULL` | Name of the join column table |
| `CHILD_JOIN_COLUMN` | `VARCHAR2(30)` | `NOT NULL` | Name of the join column |
| `CHILD_LEVEL_NAME` | `VARCHAR2(30)` |  | Name of the child hierarchy level of the join key |