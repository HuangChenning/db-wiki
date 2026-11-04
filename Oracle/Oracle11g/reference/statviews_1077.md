---
title: ALL_DIMENSIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1077.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_DIMENSIONS` describes the dimension objects accessible to the current user.

Related Views

- `DBA_DIMENSIONS` describes all dimensions in the database.
- `USER_DIMENSIONS` describes the dimensions in the current user's schema.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the dimension |
| `INVALID` | `VARCHAR2(1)` |  | Indicates whether the dimension is invalid (`Y`) or valid (`N`) |
| `COMPILE_STATE` | `VARCHAR2(13)` |  | Compile status of the dimension: |
| `REVISION` | `NUMBER` |  | Dimension revision level |