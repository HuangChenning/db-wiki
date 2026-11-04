---
title: ALL_DIM_HIERARCHIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1073.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_DIM_HIERARCHIES` describes all dimension hierarchies accessible to the current user.

Related Views

- `DBA_DIM_HIERARCHIES` describes all such hierarchies in the database.
- `USER_DIM_HIERARCHIES` describes all such hierarchies owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the dimension |
| `HIERARCHY_NAME` | `VARCHAR2(30)` |  | Hierarchy name |