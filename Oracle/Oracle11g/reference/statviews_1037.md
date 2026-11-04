---
title: ALL_CLUSTER_HASH_EXPRESSIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1037.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CLUSTER_HASH_EXPRESSIONS` displays hash functions for all hash clusters accessible to the current user.

Related Views

- `DBA_CLUSTER_HASH_EXPRESSIONS` displays hash functions for all hash clusters in the database.
- `USER_CLUSTER_HASH_EXPRESSIONS` displays hash functions for all hash clusters owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the cluster |
| `CLUSTER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the cluster |
| `HASH_EXPRESSION` | `LONG` |  | Text of the hash function of the hash cluster |