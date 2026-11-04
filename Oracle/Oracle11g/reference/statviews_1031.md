---
title: ALL_CATALOG
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1031.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CATALOG` displays the tables, clusters, views, synonyms, and sequences accessible to the current user.

Related Views

- `DBA_CATALOG` displays all tables, clusters, views, synonyms, and sequences in the entire database.
- `USER_CATALOG` displays the tables, clusters, views, synonyms, and sequences in the current user's schema. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the `TABLE`, `CLUSTER`, `VIEW`, `SYNONYM`, `SEQUENCE`, or `UNDEFINED` |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the `TABLE`, `CLUSTER`, `VIEW`, `SYNONYM`, `SEQUENCE`, or `UNDEFINED` |
| `TABLE_TYPE` | `VARCHAR2(11)` |  | Type of the `TABLE`, `CLUSTER`, `VIEW`, `SYNONYM`, `SEQUENCE`, or `UNDEFINED` |