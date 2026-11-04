---
title: ALL_DIM_LEVELS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1076.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_DIM_LEVELS` describes the dimension levels accessible to the current user. All columns of a dimension level must come from the same relation.

Related Views

- `DBA_DIM_LEVELS` describes all dimension levels in the database.
- `USER_DIM_LEVELS` describes the levels of all dimensions owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the dimension |
| `LEVEL_NAME` | `VARCHAR2(30)` |  | Unique within a dimension |
| `NUM_COLUMNS` | `NUMBER` |  | Number of columns in the level definition |
| `DETAILOBJ_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the detail object that the keys of this level come from |
| `DETAILOBJ_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table that the keys of this level come from |
| `SKIP_WHEN_NULL` | `VARCHAR2(1)` |  | Indicates whether the level is declared with the `SKIP WHEN NULL` clause (`Y`) or not (`N`) |