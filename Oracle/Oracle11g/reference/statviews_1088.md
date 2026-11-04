---
title: ALL_EVALUATION_CONTEXT_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1088.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_EVALUATION_CONTEXT_TABLES` describes the tables in the rule evaluation contexts accessible to the current user.

Related Views

- `DBA_EVALUATION_CONTEXT_TABLES` describes the tables in all rule evaluation contexts in the database.
- `USER_EVALUATION_CONTEXT_TABLES` describes the tables in the rule evaluation contexts owned by the current user. This view does not display the `EVALUATION_CONTEXT_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `EVALUATION_CONTEXT_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the evaluation context |
| `EVALUATION_CONTEXT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the evaluation context |
| `TABLE_ALIAS` | `VARCHAR2(30)` |  | Alias for a table in the evaluation context |
| `TABLE_NAME` | `VARCHAR2(4000)` |  | Name of the table referred to by the table alias |