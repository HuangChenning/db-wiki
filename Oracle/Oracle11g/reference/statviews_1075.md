---
title: ALL_DIM_LEVEL_KEY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1075.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_DIM_LEVEL_KEY` describes a column of a dimension level accessible to the current user. The position of a column within a level is specified by `KEY_POSITION`.

Related Views

- `DBA_DIM_LEVEL_KEY` describes all columns of dimension levels in the database.
- `USER_DIM_LEVEL_KEY` describes all columns of dimension levels owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the dimension |
| `LEVEL_NAME` | `VARCHAR2(30)` |  | Name of the hierarchy level |
| `KEY_POSITION` | `NUMBER` | `NOT NULL` | Ordinal position of the key column within the level |
| `COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the key column |