---
title: ALL_DIM_ATTRIBUTES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1071.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_DIM_ATTRIBUTES` describes the relationship between a dimension level and a functionally dependent column. The level columns and the dependent column must be in the same table.

Related Views

- `DBA_DIM_ATTRIBUTES` describes all such dimension relationships in the database.
- `USER_DIM_ATTRIBUTES` describes all such dimension attributes in the current user's schema.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the dimension |
| `ATTRIBUTE_NAME` | `VARCHAR2(30)` |  | Name of the attribute |
| `LEVEL_NAME` | `VARCHAR2(30)` |  | Name of the hierarchy level |
| `COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Dependent column name |
| `INFERRED` | `CHAR(1)` |  | Indicates whether the attribute is inferred from a JOIN KEY specification (`Y`) or not (`N`) |