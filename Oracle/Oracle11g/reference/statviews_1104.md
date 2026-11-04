---
title: ALL_IND_EXPRESSIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1104.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_IND_EXPRESSIONS` describes the expressions of function-based indexes on tables accessible to the current user.

Related Views

- `DBA_IND_EXPRESSIONS` describes the expressions of all function-based indexes in the database.
- `USER_IND_EXPRESSIONS` describes the expressions of function-based indexes on tables owned by the current user. This view does not display the `INDEX_OWNER` or `TABLE_OWNER` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INDEX_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the index |
| `INDEX_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the index |
| `TABLE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table or cluster |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table or cluster |
| `COLUMN_EXPRESSION` | `LONG` |  | Function-based index expression defining the column |
| `COLUMN_POSITION` | `NUMBER` | `NOT NULL` | Position of the column or attribute within the index |